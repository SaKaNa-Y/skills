"""Check history isolation, evidence integrity and incomplete legacy states."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_skill_history import HistoryChecker
from check_markdown_links import Checker


class HistoryChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.history = self.root / 'docs/skill-evolution'
        self.record = 'skills/example/001-change/record.md'
        self.put('skills/example/SKILL.md', '---\nname: example\n---\n# Example\n', root=True)
        self.put('README.md', '# History\n')
        self.put('skills/example/index.md', '# Example\n[change](001-change/record.md)\n')
        self.put(self.record, '# Change\n')
        self.data = {'version': 1, 'skills': [{'name': 'example', 'status': 'active'}],
                     'records': [{'path': self.record, 'status': 'completed',
                                  'adoption': 'no-change', 'validation': 'inconclusive'}],
                     'files': [], 'migration': []}

    def put(self, path, content, root=False):
        target = (self.root if root else self.history) / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        return target

    def run_check(self):
        self.put('manifest.json', json.dumps(self.data))
        return HistoryChecker(self.root).run()

    def evidence(self, content='# Original\n', kind='original'):
        path = 'skills/example/001-change/evidence/legacy/SKILL.md'
        target = self.put(path, content)
        self.data['files'].append({'path': path, 'kind': kind,
                                   'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
        return target

    def test_complete_tree_and_legacy_links(self):
        self.evidence('[old relative reference](missing.md)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)
        self.assertEqual(Checker(self.root).run()['exit_code'], 0)

    def test_broken_curated_navigation_fails_both_checkers(self):
        self.put(self.record, '[lost](missing.md)\n')
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.assertEqual(Checker(self.root).run()['exit_code'], 1)

    def test_paused_requires_next_action(self):
        self.data['records'][0]['status'] = 'paused'
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.data['records'][0]['next_action'] = 'Compare the saved candidate to the source.'
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_unknown_and_applied_need_historical_limitation(self):
        self.data['records'][0].update(status='unknown', adoption='applied')
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.data['records'][0]['limitations'] = ['Original recovery input was not recorded.']
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_changed_evidence_and_unlisted_file(self):
        target = self.evidence()
        target.write_text('changed')
        self.assertTrue(any('SHA-256' in x['reason'] for x in self.run_check()['errors']))
        self.data['files'] = []
        self.assertTrue(any('missing integrity' in x['reason'] for x in self.run_check()['errors']))

    def test_path_escape_rejected_without_reading_outside(self):
        self.data['files'] = [{'path': '../outside', 'sha256': 'fake', 'kind': 'original'}]
        self.assertTrue(any('Invalid relative' in x['reason'] for x in self.run_check()['errors']))

    def test_symlink_escape_rejected(self):
        target = self.evidence()
        target.unlink()
        target.symlink_to(self.root / 'skills/example/SKILL.md')
        self.assertEqual(self.run_check()['exit_code'], 1)

    def test_sanitized_derivative_needs_note(self):
        self.evidence(kind='sanitized')
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.data['files'][0]['note'] = 'Home directory replaced; original hash is historical only.'
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_private_warning_does_not_echo_sensitive_contents(self):
        secret = 'ghp_' + 'a' * 35
        self.evidence(secret)
        result = self.run_check()
        self.assertTrue(result['warnings'])
        self.assertNotIn(secret, json.dumps(result))

    def test_temporary_dependency_is_not_durable(self):
        self.put('.scratch/skill-evolution/input.txt', 'input', root=True)
        self.put(self.record, '[input](../../../../../.scratch/skill-evolution/input.txt)\n')
        self.assertTrue(any('temporary' in x['reason'] for x in self.run_check()['errors']))

    def test_encoded_temporary_dependency_is_rejected(self):
        self.put('.scratch/skill-evolution/input.txt', 'input', root=True)
        self.put(self.record, '[input](../../../../../%2Escratch/skill-evolution/input.txt)\n')
        self.assertTrue(any('temporary' in e['reason'] for e in self.run_check()['errors']))

    def test_external_temporary_named_path_is_not_local_dependency(self):
        self.put(self.record, '[external](https://example.test/.scratch/input.txt)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_stale_identity_and_duplicate_sequence(self):
        self.data['skills'][0]['name'] = 'old-name'
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.data['skills'][0]['name'] = 'example'
        path = 'skills/example/001-second/record.md'
        self.put(path, '# Another\n')
        self.data['records'].append(dict(self.data['records'][0], path=path))
        self.assertTrue(any('Duplicate' in x['reason'] for x in self.run_check()['errors']))

    def test_malformed_metadata_is_reported(self):
        self.data['records'][0]['next_action'] = {'unexpected': 'object'}
        self.assertEqual(self.run_check()['exit_code'], 1)

    def test_manifest_symlink_is_not_followed(self):
        outside = self.put('outside.json', json.dumps(self.data), root=True)
        (self.history / 'manifest.json').symlink_to(outside)
        result = HistoryChecker(self.root).run()
        self.assertEqual(result['exit_code'], 1)
        self.assertIn('symlinks', result['errors'][0]['reason'])

    def test_source_rename_without_history_move_fails(self):
        self.put('skills/example/SKILL.md', '---\nname: renamed\n---\n', root=True)
        self.assertTrue(any('reconcile rename' in e['reason'] for e in self.run_check()['errors']))

    def test_source_name_scalar_profile(self):
        for scalar in ('example', "'example'", '"example"', 'example # comment'):
            self.put('skills/example/SKILL.md', f'---\nname: {scalar}\n---\n', root=True)
            self.assertEqual(self.run_check()['exit_code'], 0)
        for header in ('name: [example]', 'name: example\nname: example', 'description: missing name'):
            self.put('skills/example/SKILL.md', f'---\n{header}\n---\n', root=True)
            self.assertEqual(self.run_check()['exit_code'], 1)

    def test_active_work_is_valid(self):
        self.data['records'][0]['status'] = 'active'
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_duplicate_migration_and_source_integrity(self):
        target = self.evidence()
        entry = self.data['files'][0]
        item = {'source': 'old/evidence.md', 'destination': entry['path'],
                'disposition': 'retained', 'reason': 'Preserve original',
                'source_sha256': entry['sha256']}
        self.data['migration'] = [item]
        self.assertEqual(self.run_check()['exit_code'], 0)
        self.data['migration'].append(dict(item))
        self.assertTrue(any('Duplicate migration' in e['reason'] for e in self.run_check()['errors']))
        self.data['migration'] = [dict(item, source_sha256='0' * 64)]
        self.assertTrue(any('differs from declared' in e['reason'] for e in self.run_check()['errors']))
        self.data['migration'][0]['source_sha256'] = 'invalid'
        self.assertTrue(any('Invalid source SHA' in e['reason'] for e in self.run_check()['errors']))

    def test_sanitized_migration_matches_provenance(self):
        self.evidence(kind='sanitized')
        entry = self.data['files'][0]
        entry.update(note='Redacted original', original_sha256='0' * 64)
        self.data['migration'] = [{'source': 'old/input.md', 'destination': entry['path'],
                                  'source_sha256': '1' * 64, 'disposition': 'sanitized',
                                  'reason': 'Redact'}]
        self.assertEqual(self.run_check()['exit_code'], 1)
        self.data['migration'][0]['source_sha256'] = '0' * 64
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_orphan_iteration_and_unlisted_material(self):
        self.put('skills/example/002-orphan/notes.txt', 'orphan')
        result = self.run_check()
        self.assertTrue(any('no registered record' in e['reason'] for e in result['errors']))
        self.assertTrue(any('Unlisted file' in e['reason'] for e in result['errors']))

    def test_structured_temporary_recovery_is_rejected(self):
        self.put('.local/input.txt', 'input')
        self.data['records'][0]['recovery'] = ['.local/input.txt']
        self.assertTrue(any('Structured path depends' in e['reason'] for e in self.run_check()['errors']))

    def test_missing_migration_destination(self):
        self.data['migration'] = [{'source': 'old/file.md', 'destination': 'missing.md',
                                  'disposition': 'retained', 'reason': 'Move'}]
        self.assertEqual(self.run_check()['exit_code'], 1)

    def test_local_archive_is_explicit_and_checks_its_own_links(self):
        import shutil
        self.evidence('Private host path /Users/example/work\n')
        self.put('manifest.json', json.dumps(self.data))
        local = self.root / '.local/history'
        shutil.copytree(self.history, local)
        self.assertTrue(HistoryChecker(self.root).run()['warnings'])
        result = HistoryChecker(self.root, local_history='.local/history').run()
        self.assertEqual(result['exit_code'], 0)
        self.assertEqual(result['warnings'], [])
        (local / self.record).write_text('[missing](missing.md)\n')
        self.assertEqual(HistoryChecker(self.root, local_history='.local/history').run()['exit_code'], 1)
        self.assertEqual(HistoryChecker(self.root).run()['exit_code'], 0)

    def test_local_mode_cannot_disable_publication_checks_on_public_tree(self):
        self.put('manifest.json', json.dumps(self.data))
        result = HistoryChecker(self.root, local_history='docs/skill-evolution').run()
        self.assertEqual(result['exit_code'], 1)

    def test_local_archive_still_checks_evidence_hashes(self):
        import shutil
        self.evidence()
        self.put('manifest.json', json.dumps(self.data))
        local = self.root / '.local/history'
        shutil.copytree(self.history, local)
        (local / self.data['files'][0]['path']).write_text('changed')
        result = HistoryChecker(self.root, local_history='.local/history').run()
        self.assertTrue(any('SHA-256' in x['reason'] for x in result['errors']))

    def test_local_archive_cannot_depend_on_other_private_directory(self):
        import shutil
        self.put('manifest.json', json.dumps(self.data))
        local = self.root / '.local/history'
        shutil.copytree(self.history, local)
        (self.root / '.local/other').mkdir()
        (self.root / '.local/other/input.md').write_text('outside')
        (local / self.record).write_text('[outside](../../../../other/input.md)')
        result = HistoryChecker(self.root, local_history='.local/history').run()
        self.assertTrue(any('temporary material' in x['reason'] for x in result['errors']))


if __name__ == '__main__':
    unittest.main()
