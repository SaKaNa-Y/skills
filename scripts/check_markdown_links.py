#!/usr/bin/env python3
"""Check local references in a complete candidate tree without changing files."""

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


HISTORY_PATTERNS = ('docs/skill-evolution/README.md',
                    'docs/skill-evolution/skills/*/index.md',
                    'docs/skill-evolution/skills/*/*/record.md',
                    'docs/skill-evolution/discussions/*/record.md')
SOURCE_PATTERNS = ('*.md', 'skills/**/*.md', 'docs/agents/**/*.md', 'docs/adr/**/*.md') + HISTORY_PATTERNS
EXCLUDED_PARTS = {'node_modules', '.git', '.venv', '__pycache__', 'tests', 'fixtures'}


@dataclass
class Document:
    anchors: set = field(default_factory=set)
    links: list = field(default_factory=list)


def located(rule):
    """Retain the original inline syntax and its offset before URL normalization."""
    def run(state, silent):
        start, count = state.pos, len(state.tokens)
        matched = rule(state, silent)
        if matched and not silent:
            for token in state.tokens[count:]:
                if token.type in ('link_open', 'image') and 'raw' not in token.meta:
                    token.meta.update(raw=state.src[start:state.pos],
                                      line=state.src[:start].count('\n'))
        return matched
    return run


def unresolved_reference(state, silent):
    """Flag explicit unresolved references before escapes/entities become text."""
    from markdown_it.helpers import parseLinkLabel

    # Label parsing calls skipToken in silent mode. Do not recurse into this
    # diagnostic rule while the parser is locating a label boundary.
    if silent:
        return False
    start = state.pos + (1 if state.src.startswith('![', state.pos) else 0)
    if start >= state.posMax or state.src[start] != '[':
        return False
    end = parseLinkLabel(state, start, True)
    if end < 0 or end + 1 >= state.posMax or state.src[end + 1] != '[':
        return False
    finish = parseLinkLabel(state, end + 1, True)
    if finish < 0:
        return False
    token = state.push('unsupported_reference', '', 0)
    token.content = state.src[state.pos:finish + 1]
    token.meta['line'] = state.src[:state.pos].count('\n')
    state.pos = finish + 1
    return True


def heading_text(children):
    parts = []
    for child in children or []:
        if child.type == 'image':
            parts.append(heading_text(child.children))
        elif child.type in ('text', 'code_inline', 'unsupported_reference'):
            parts.append(child.content)
        elif child.type in ('softbreak', 'hardbreak'):
            parts.append('\n')
    return ''.join(parts)


def descendants(tokens):
    for token in tokens or []:
        yield token
        yield from descendants(token.children)


class Checker:
    def __init__(self, root):
        from github_slugger import GithubSlugger
        from markdown_it import MarkdownIt
        from markdown_it.rules_inline import autolink, image, link

        self.root = root.resolve()
        self.slugger_type = GithubSlugger
        self.parser = MarkdownIt('commonmark').enable(['table', 'strikethrough'])
        # Inspect every destination, including file: URLs that a renderer rejects.
        # This program never renders HTML or opens URLs.
        self.parser.validateLink = lambda destination: True
        for name, rule in [('link', link), ('image', image), ('autolink', autolink)]:
            self.parser.inline.ruler.at(name, located(rule))
        self.parser.inline.ruler.after('image', 'unresolved_reference', unresolved_reference)
        self.documents = {}
        self.errors, self.incomplete, self.skipped = [], [], []
        self.checked = 0

    def issue(self, group, source, line, link, reason):
        group.append(dict(source=str(source.relative_to(self.root)), line=line,
                          link=link, reason=reason))

    def inside(self, path):
        try:
            path.resolve().relative_to(self.root)
            return True
        except (ValueError, OSError, RuntimeError):
            return False

    def document(self, path):
        if path in self.documents:
            return self.documents[path]
        doc = self.documents[path] = Document()
        try:
            text = path.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError) as error:
            self.issue(self.incomplete, path, 1, '', f'Cannot read Markdown: {error}')
            return doc
        # Remove frontmatter without moving any source lines.
        if text.startswith('---\n'):
            end = re.search(r'^---\s*$', text[4:], re.M)
            if not end:
                self.issue(self.incomplete, path, 1, '', 'Unclosed YAML frontmatter')
                return doc
            stop = 4 + end.end()
            text = '\n' * text[:stop].count('\n') + text[stop:]
        tokens = self.parser.parse(text)
        slugger = self.slugger_type()
        for index, token in enumerate(tokens):
            if token.type == 'heading_open':
                inline = tokens[index + 1]
                title = heading_text(inline.children)
                doc.anchors.add(slugger.slug(title))
            if token.type == 'html_block':
                self.check_html(path, token.map[0] + 1, token.content)
            if token.type != 'inline':
                continue
            base = token.map[0] + 1
            for child in token.children or []:
                line = base + child.meta.get('line', 0)
                if child.type in ('link_open', 'image'):
                    dest = child.attrGet('href' if child.type == 'link_open' else 'src')
                    doc.links.append((line, child.meta.get('raw', dest), dest))
                elif child.type == 'html_inline':
                    self.check_html(path, base, child.content)
            for child in descendants(token.children):
                if child.type == 'unsupported_reference':
                    self.issue(self.incomplete, path, base + child.meta.get('line', 0), child.content,
                               'Unresolved or unsupported reference syntax')
        return doc

    def check_html(self, path, line, text):
        if re.sub(r'<!--.*?-->', '', text, flags=re.S).strip():
            self.issue(self.incomplete, path, line, text.strip(),
                       'Raw HTML is outside the supported Markdown profile')

    def check_link(self, source, line, raw, destination):
        try:
            url = urlsplit(destination)
        except ValueError:
            self.issue(self.incomplete, source, line, raw, 'Cannot parse destination')
            return
        if url.scheme or url.netloc:
            group = self.incomplete if url.scheme.lower() == 'file' else self.skipped
            self.issue(group, source, line, raw, 'External destination (not fetched)')
            return
        if url.query or url.path.startswith('/'):
            self.issue(self.incomplete, source, line, raw,
                       'Local queries or absolute paths are unsupported')
            return
        try:
            decoded = unquote(url.path, errors='strict')
            anchor = unquote(url.fragment, errors='strict')
            if '\x00' in decoded or '\\' in decoded:
                raise ValueError('Unsupported path character')
            target = source.parent / decoded if decoded else source
            if not self.inside(target):
                self.issue(self.incomplete, source, line, raw, 'Target escapes the candidate root')
                return
            target = target.resolve()
            self.checked += 1
            if not target.exists():
                self.issue(self.errors, source, line, raw, 'Target does not exist in candidate tree')
            elif anchor:
                if not target.is_file() or target.suffix.lower() != '.md':
                    self.issue(self.incomplete, source, line, raw,
                               'Fragments on non-Markdown targets are unsupported')
                elif anchor not in self.document(target).anchors:
                    self.issue(self.errors, source, line, raw, f'Heading anchor not found: {anchor}')
        except (OSError, ValueError, UnicodeError, RuntimeError) as error:
            self.issue(self.incomplete, source, line, raw, f'Cannot resolve target: {error}')

    def run(self):
        sources = sorted({p for pattern in SOURCE_PATTERNS for p in self.root.glob(pattern)
                          if not EXCLUDED_PARTS.intersection(p.relative_to(self.root).parts)})
        if not self.root.is_dir() or not sources:
            self.issue(self.incomplete, self.root, 1, '', 'Root has no public Markdown sources')
        for source in sources:
            if not self.inside(source):
                self.issue(self.incomplete, source, 1, '', 'Source escapes the candidate root')
                continue
            for line, raw, dest in self.document(source).links:
                self.check_link(source, line, raw, dest)
        status = 2 if self.incomplete else 1 if self.errors else 0
        return dict(status=('passed', 'broken', 'incomplete')[status], exit_code=status,
                    root=str(self.root), source_patterns=SOURCE_PATTERNS,
                    files_scanned=len(sources), local_links_checked=self.checked,
                    errors=self.errors, incomplete=self.incomplete, skipped=self.skipped)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        'Exit 0: complete with no broken local links; 1: broken links; '
        '2: incomplete check. External URLs are listed but never fetched. '
        'Sources: root *.md, skills/**/*.md, docs/agents/**/*.md, docs/adr/**/*.md; '
        'tests, fixtures and dependency directories are excluded.'))
    parser.add_argument('--root', required=True, type=Path, help='Complete candidate tree, not a diff overlay')
    parser.add_argument('--json', action='store_true', help='Print the structured report')
    args = parser.parse_args(argv)
    try:
        report = Checker(args.root).run()
    except ImportError as error:
        print(f'Check incomplete: {error}. Install scripts/requirements.txt in a virtual environment.', file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"{report['status']}: {report['files_scanned']} files, "
              f"{report['local_links_checked']} local links, "
              f"{len(report['skipped'])} external links skipped")
        for group in ('errors', 'incomplete', 'skipped'):
            for issue in report[group]:
                print(f"{group}: {issue['source']}:{issue['line']}: {issue['link']} — {issue['reason']}")
    return report['exit_code']


if __name__ == '__main__':
    sys.exit(main())
