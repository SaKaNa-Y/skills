#!/usr/bin/env python3
"""Read-only checks for public summaries or explicitly selected local history."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from check_markdown_links import Checker, HISTORY_PATTERNS

HISTORY = Path('docs/skill-evolution')
SEQUENCE = re.compile(r'^[0-9]{3,}-[a-z0-9]+(?:-[a-z0-9]+)*$')
ENVIRONMENT = {'node_modules', '.venv', '__pycache__', '.git', 'offline-dependencies'}
PRIVATE = re.compile(r'/(?:Users|home)/[^/\s]+/|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}')


class HistoryChecker:
    def __init__(self, root, max_bytes=5 * 1024 * 1024, local_history=None):
        self.root = Path(root).resolve()
        self.local = local_history is not None
        self.local_path = Path(local_history) if self.local else None
        self.history = self.root / (Path(local_history) if self.local else HISTORY)
        self.max_bytes = max_bytes
        self.errors, self.warnings = [], []
        self.stats = {}

    def issue(self, path, reason, warning=False):
        # Never include source contents or a suspected secret in diagnostics.
        (self.warnings if warning else self.errors).append({'path': str(path), 'reason': reason})

    def target(self, value):
        if not isinstance(value, str) or not value or '\\' in value or Path(value).is_absolute() or '..' in Path(value).parts:
            self.issue('manifest.json', 'Invalid relative history path')
            return None
        if {'.scratch', '.local'}.intersection(Path(value).parts):
            self.issue(value, 'Structured path depends on temporary material')
            return None
        path = self.history / value
        try:
            path.resolve().relative_to(self.history.resolve())
        except (ValueError, OSError, RuntimeError):
            self.issue(value, 'Path escapes history root')
            return None
        if not path.is_file():
            self.issue(value, 'Required file is missing')
            return None
        return path

    def check_source_name(self, name):
        source = self.root / 'skills' / name / 'SKILL.md'
        try:
            source.resolve().relative_to(self.root)
            with source.open(encoding='utf-8-sig') as stream:
                prefix = stream.read(65536)
        except (OSError, ValueError, UnicodeError):
            self.issue(name, 'Cannot read owned skill identity inside candidate tree')
            return
        header = re.match(r'\A---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)', prefix, re.S)
        if not header:
            self.issue(name, 'Owned skill needs closed initial YAML frontmatter within 64 KiB')
            return
        fields = re.findall(r'^name:[ \t]*(.*)$', header.group(1), re.M)
        if len(fields) != 1:
            self.issue(name, 'Owned skill needs exactly one top-level name scalar')
            return
        # This bounded identity reader deliberately supports only kebab-case
        # scalar names, optionally quoted, and an optional YAML comment.
        scalar = re.fullmatch(r"(?:([a-z0-9]+(?:-[a-z0-9]+)*)|'([a-z0-9]+(?:-[a-z0-9]+)*)'|\"([a-z0-9]+(?:-[a-z0-9]+)*)\")(?:[ \t]+#[^\r\n]*)?[ \t\r]*", fields[0])
        if not scalar:
            self.issue(name, 'Unsupported owned skill name scalar')
        elif next(value for value in scalar.groups() if value is not None) != name:
            self.issue(name, 'Declared skill name differs from history identity; reconcile rename')

    def run(self):
        if self.local and (self.local_path.is_absolute() or ".." in self.local_path.parts):
            self.issue("manifest.json", "Local history needs a repository-relative path without traversal")
            return self.report()
        try:
            self.history.resolve().relative_to(self.root)
        except (ValueError, OSError, RuntimeError):
            self.issue('manifest.json', 'History root escapes candidate tree')
            return self.report()
        if self.local and not self.history.resolve().is_relative_to(self.root / '.local'):
            self.issue('manifest.json', 'Local history must be inside the candidate .local directory')
            return self.report()
        if self.history.is_symlink() or (self.history / 'manifest.json').is_symlink():
            self.issue('manifest.json', 'History symlinks are unsupported')
            return self.report()
        try:
            data = json.loads((self.history / 'manifest.json').read_text())
        except (OSError, ValueError):
            self.issue('manifest.json', 'Missing or invalid history manifest')
            return self.report()
        if not isinstance(data, dict) or data.get('version') != 1:
            self.issue('manifest.json', 'Expected manifest version 1')
            return self.report()
        for key in ('skills', 'records', 'files', 'migration'):
            if not isinstance(data.get(key), list) or any(not isinstance(x, dict) for x in data[key]):
                self.issue('manifest.json', f'{key} must be an array of objects')
        if self.errors:
            return self.report()
        for item in data['records']:
            for key in ('recovery', 'limitations'):
                if key in item and (not isinstance(item[key], list) or any(not isinstance(x, str) for x in item[key])):
                    self.issue('manifest.json', f'{key} must be an array of strings')
            if 'next_action' in item and not isinstance(item['next_action'], str):
                self.issue('manifest.json', 'next_action must be a string')
        for item in data['skills']:
            for key in ('previous_names', 'successors'):
                if key in item and (not isinstance(item[key], list) or any(not isinstance(x, str) for x in item[key])):
                    self.issue('manifest.json', f'{key} must be an array of strings')
        if self.errors:
            return self.report()
        names = set()
        for skill in data['skills']:
            name, status = skill.get('name'), skill.get('status')
            if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in names:
                self.issue('manifest.json', 'Invalid or duplicate skill identity')
                continue
            names.add(name)
            self.target(f'skills/{name}/index.md')
            if status not in ('active', 'retired', 'transferred'):
                self.issue(name, 'Invalid skill status')
            if status == 'active':
                if not (self.root / 'skills' / name / 'SKILL.md').is_file():
                    self.issue(name, 'Active history has no owned skill source')
                else:
                    self.check_source_name(name)
            if status in ('retired', 'transferred') and not skill.get('reason'):
                self.issue(name, 'Inactive identity needs a reason')
        for skill in data['skills']:
            for successor in skill.get('successors', []):
                if successor not in names:
                    self.issue(skill.get('name'), 'Unknown successor identity')
        records, sequences = set(), set()
        for record in data['records']:
            value = record.get('path')
            path = self.target(value)
            if path is None:
                continue
            parts = Path(value).parts
            valid = ((len(parts) == 4 and parts[0] == 'skills' and parts[1] in names) or
                     (len(parts) == 3 and parts[0] == 'discussions'))
            if not valid or parts[-1] != 'record.md' or not SEQUENCE.fullmatch(parts[-2]):
                self.issue(value, 'Invalid record location or sequence name')
                continue
            seq = (str(Path(value).parent.parent), int(parts[-2].split('-')[0]))
            if value in records or seq in sequences:
                self.issue(value, 'Duplicate record or sequence number')
            records.add(value)
            sequences.add(seq)
            if record.get('status') not in ('active', 'completed', 'paused', 'blocked', 'abandoned', 'unknown'):
                self.issue(value, 'Invalid lifecycle status')
            if record.get('status') == 'unknown' and not record.get('limitations'):
                self.issue(value, 'Unknown legacy lifecycle needs an explicit limitation')
            if record.get('status') in ('paused', 'blocked') and not record.get('next_action', '').strip():
                self.issue(value, 'Paused or blocked work needs a next action')
            if record.get('adoption') not in ('applied', 'not-applied', 'unknown', 'proposed', 'candidate', 'rejected', 'no-change', 'superseded', 'rolled-back'):
                self.issue(value, 'Invalid adoption status')
            if record.get('validation') not in ('supported', 'unsupported', 'inconclusive', 'pending', 'not-run', 'unknown'):
                self.issue(value, 'Invalid validation status')
            if record.get('adoption') == 'applied' and not record.get('recovery') and not record.get('limitations'):
                self.issue(value, 'Applied change needs recovery files or an explicit historical limitation')
            for recovery in record.get('recovery', []):
                self.target(recovery)
        listed, file_entries = set(), {}
        for item in data['files']:
            value = item.get('path')
            path = self.target(value)
            if path is None:
                continue
            if value in listed:
                self.issue(value, 'Duplicate integrity entry')
            listed.add(value)
            file_entries[value] = item
            if 'original_sha256' in item and not re.fullmatch(r'[0-9a-f]{64}', str(item['original_sha256'])):
                self.issue(value, 'Invalid original SHA-256')
            if item.get('kind') not in ('original', 'sanitized', 'curated', 'recovery'):
                self.issue(value, 'Invalid evidence kind')
            if item.get('kind') == 'sanitized' and not item.get('note'):
                self.issue(value, 'Sanitized derivative needs a provenance/limitation note')
            if hashlib.sha256(path.read_bytes()).hexdigest() != item.get('sha256'):
                self.issue(value, 'SHA-256 mismatch')
        migration_sources = set()
        for item in data['migration']:
            source = item.get('source')
            if not isinstance(source, str) or not source or '\\' in source or Path(source).is_absolute() or '..' in Path(source).parts:
                self.issue('manifest.json', 'Invalid migration source path')
                continue
            if source in migration_sources:
                self.issue(source, 'Duplicate migration source')
            migration_sources.add(source)
            original_hash = item.get('source_sha256')
            if original_hash is not None and not re.fullmatch(r'[0-9a-f]{64}', str(original_hash)):
                self.issue(source, 'Invalid source SHA-256')
            disposition = item.get('disposition')
            if disposition not in ('retained', 'sanitized', 'quarantined', 'removed') or not item.get('reason'):
                self.issue('manifest.json', 'Migration item needs disposition and reason')
            if disposition in ('retained', 'sanitized'):
                destination = self.target(item.get('destination'))
                entry = file_entries.get(item.get('destination'))
                if destination and original_hash is not None:
                    if disposition == 'retained' and hashlib.sha256(destination.read_bytes()).hexdigest() != original_hash:
                        self.issue(source, 'Retained destination differs from declared source SHA-256')
                    if disposition == 'sanitized' and (not entry or entry.get('kind') != 'sanitized' or entry.get('original_sha256') != original_hash):
                        self.issue(source, 'Sanitized migration lacks matching derivative provenance')
        allowed_root = {'README.md', 'manifest.json', 'skills', 'discussions'}
        if self.local:
            allowed_root.update({'retained', 'migration'})
        for path in self.history.iterdir():
            if path.name not in allowed_root:
                self.issue(path.name, 'Unexpected history root entry')
        expected_files = {'README.md', 'manifest.json'} | records | {f'skills/{name}/index.md' for name in names}
        record_dirs = {str(Path(value).parent) for value in records}
        self.target('README.md')
        for path in sorted(self.history.rglob('*')):
            relative = str(path.relative_to(self.history))
            if path.is_dir() and path.parent == self.history / 'skills' and path.name not in names:
                self.issue(relative, 'History identity missing from manifest')
            parts = path.relative_to(self.history).parts
            if path.is_dir() and ((len(parts) == 3 and parts[0] == 'skills') or (len(parts) == 2 and parts[0] == 'discussions')) and parts[-1] not in ('evidence', 'recovery') and relative not in record_dirs:
                self.issue(relative, 'Iteration directory has no registered record')
            if path.is_symlink():
                self.issue(relative, 'History symlinks are unsupported')
                continue
            if ENVIRONMENT.intersection(path.relative_to(self.history).parts):
                self.issue(relative, 'Execution environment belongs outside durable history')
            if not path.is_file():
                continue
            if relative not in expected_files and relative not in listed:
                self.issue(relative, 'Unlisted file outside curated navigation')
            if path.name == 'record.md' and '/evidence/' not in relative and '/recovery/' not in relative and relative not in records:
                self.issue(relative, 'Record missing from manifest')
            if ('evidence' in path.relative_to(self.history).parts or 'recovery' in path.relative_to(self.history).parts) and relative not in listed:
                self.issue(relative, 'Evidence or recovery file missing integrity entry')
            if self.local:
                continue
            if path.stat().st_size > self.max_bytes:
                self.issue(relative, 'Oversized material needs publication review', warning=True)
            else:
                try:
                    text = path.read_text()
                except UnicodeError:
                    self.issue(relative, 'Binary material needs publication review', warning=True)
                else:
                    if PRIVATE.search(text):
                        self.issue(relative, 'Possible private material needs publication review', warning=True)
        checker = Checker(self.root)
        patterns = [pattern.removeprefix(str(HISTORY) + '/') for pattern in HISTORY_PATTERNS]
        sources = sorted({p for pattern in patterns for p in self.history.glob(pattern)})
        for source in sources:
            if not checker.inside(source):
                self.issue(str(source.relative_to(self.root)), 'Source escapes candidate tree')
                continue
            for line, raw, destination in checker.document(source).links:
                try:
                    url = urlsplit(destination)
                    if not url.scheme and not url.netloc:
                        local_path = unquote(url.path, errors='strict')
                        resolved = (source.parent / local_path).resolve()
                        parts = resolved.relative_to(self.root).parts
                        if '.scratch' in parts or ('.local' in parts and not (self.local and resolved.is_relative_to(self.history.resolve()))):
                            self.issue(str(source.relative_to(self.root)), 'Curated record depends on temporary material')
                except (OSError, ValueError, UnicodeError, RuntimeError):
                    # The shared link checker reports malformed or escaped paths.
                    pass
                checker.check_link(source, line, raw, destination)
        for item in checker.errors + checker.incomplete:
            self.issue(item['source'], f"Line {item['line']}: {item['reason']}")
        self.stats = {'skills': len(names), 'records': len(records), 'integrity_files': len(listed),
                      'migration_entries': len(data['migration']), 'curated_documents': len(sources),
                      'local_links_checked': checker.checked}
        return self.report()

    def report(self):
        return {'exit_code': 1 if self.errors else 0, 'status': 'failed' if self.errors else 'passed',
                'errors': self.errors, 'warnings': self.warnings, 'counts': self.stats}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path, help='Complete candidate tree')
    parser.add_argument('--local-history', type=Path, help='Explicit repository-relative archive below .local; check integrity without publication warnings')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--strict', action='store_true', help='Fail on publication review warnings too')
    args = parser.parse_args(argv)
    try:
        report = HistoryChecker(args.root, local_history=args.local_history).run()
    except (ImportError, OSError, ValueError, TypeError) as error:
        print(f'History check incomplete ({type(error).__name__}); inspect manifest schema and dependencies.', file=sys.stderr)
        return 2
    if args.strict and report['warnings']:
        report.update(exit_code=1, status='failed')
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['status']}: {len(report['errors'])} errors, {len(report['warnings'])} publication warnings")
        for group in ('errors', 'warnings'):
            for item in report[group]:
                print(f"{group}: {item['path']}: {item['reason']}")
    return report['exit_code']


if __name__ == '__main__':
    sys.exit(main())
