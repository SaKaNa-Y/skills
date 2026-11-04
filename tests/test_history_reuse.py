import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('reuse', Path(__file__).parents[1] / 'skills/evolve-skills/scripts/history_reuse.py')
reuse = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reuse)


class HistoryReuseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.rel = 'skills/example/001-case/record.md'
        self.record = self.root / self.rel
        self.record.parent.mkdir(parents=True)
        (self.root / 'skills/example/index.md').write_text('# Example\n')
        self.item = {'version': 1, 'id': 'sit-summary', 'situation': 'Earlier work omitted',
                     'applicability': {'when': 'whole task', 'exclude': 'latest edit only'},
                     'skills': ['example'], 'search_terms': ['cumulative'],
                     'events': [{'id': 'event-one', 'identity': 'distinct', 'summary': 'Recorded omission', 'sources': [self.rel]}],
                     'interpretation': 'An observation, not a cause', 'revisit': 'Check available scope'}
        self.write_record()
        self.write_json('manifest.json', {'records': [{'path': self.rel}]})

    def write_json(self, name, data):
        p = self.root / name
        p.parent.mkdir(exist_ok=True)
        p.write_text(json.dumps(data))

    def write_record(self, body='Historical evidence\n'):
        self.record.write_text(body + '\n```evolution-situation\n' + json.dumps(self.item) + '\n```\n')

    def acknowledge(self):
        r = reuse.assess(self.root)
        entry = r['situations']['sit-summary']
        self.write_json('reuse/reviews.json', {'version': 1, 'situations': {'sit-summary': {
            'inputs': entry['inputs'], 'association_sha256': entry['association_sha256'], 'basis': 'Read evidence and association'}}})

    def test_render_is_deterministic_and_does_not_acknowledge(self):
        first, code = reuse.run('render', self.root)
        self.assertEqual(code, 0)
        data = (self.root / 'reuse/index.md').read_bytes()
        reuse.run('render', self.root)
        self.assertEqual(data, (self.root / 'reuse/index.md').read_bytes())
        self.assertEqual(first['review_needed'], ['sit-summary'])
        self.assertFalse((self.root / 'reuse/reviews.json').exists())

    def test_source_change_requires_review_even_after_render(self):
        self.acknowledge()
        self.assertEqual(reuse.run('render', self.root)[0]['review_needed'], [])
        self.write_record('New contrary evidence\n')
        report, code = reuse.run('check', self.root)
        self.assertEqual(code, 1)
        self.assertEqual(report['review_needed'], ['sit-summary'])
        self.assertEqual(reuse.run('render', self.root)[0]['review_needed'], ['sit-summary'])

    def test_association_change_does_not_hide_behind_excluded_block(self):
        self.acknowledge()
        before = reuse.source_hash(self.record)
        self.item['interpretation'] = 'Changed interpretation'
        self.write_record()
        self.assertEqual(before, reuse.source_hash(self.record))
        self.assertEqual(reuse.assess(self.root)['review_needed'], ['sit-summary'])

    def test_multiple_blocks_preserve_historical_body_hash(self):
        before = reuse.source_hash(self.record)
        other = dict(self.item, id='sit-second')
        self.record.write_text(self.record.read_text() + '```evolution-situation\n' + json.dumps(other) + '\n```\n')
        self.assertEqual(before, reuse.source_hash(self.record))
        self.assertEqual(len(reuse.collect(self.root)[0]), 2)

    def test_duplicate_id_leaves_output_intact(self):
        reuse.run('render', self.root)
        output = self.root / 'reuse/index.md'
        before = output.read_bytes()
        self.record.write_text(self.record.read_text() * 2)
        report, code = reuse.run('render', self.root)
        self.assertEqual(code, 1)
        self.assertTrue(report['errors'])
        self.assertEqual(before, output.read_bytes())

    def test_missing_source_and_escape_are_rejected(self):
        for source in ('missing.md', '../outside.md'):
            self.item['events'][0]['sources'] = [source]
            self.write_record()
            self.assertTrue(reuse.assess(self.root)['errors'])

    def test_redirect_cycle_is_rejected(self):
        self.item.update(state='replaced', redirects=['sit-summary'])
        self.write_record()
        self.assertTrue(any('cycle' in x['reason'] for x in reuse.assess(self.root)['errors']))

    def test_unknown_redirect_is_rejected(self):
        self.item.update(state='replaced', redirects=['sit-missing'])
        self.write_record()
        self.assertTrue(reuse.assess(self.root)['errors'])

    def test_inventory_does_not_count_nested_evidence_as_primary(self):
        nested = self.record.parent / 'evidence/old/record.md'
        nested.parent.mkdir(parents=True)
        nested.write_text('old copy')
        self.assertEqual(list(reuse.inventory(self.root)['records']), [self.rel])
        self.assertFalse((self.root / 'reuse').exists())

    def test_coverage_reports_change_added_and_unresolved(self):
        h = reuse.source_hash(self.record)
        self.write_json('reuse/screening.json', {'version': 1, 'snapshot': {self.rel: h}, 'records': {
            self.rel: {'sha256': h, 'disposition': 'unresolved', 'situations': [], 'basis': 'Version missing'}}})
        self.write_record('changed body')
        report = reuse.assess(self.root)
        self.assertEqual(report['coverage']['changed'], [self.rel])
        self.assertEqual(report['coverage']['unresolved'], [self.rel])

    def test_retained_screening_input_change_requires_rescreen(self):
        evidence = self.root / 'retained/account.md'
        evidence.parent.mkdir()
        evidence.write_text('Screened account')
        h = reuse.source_hash(self.record)
        self.write_json('reuse/screening.json', {'version': 1, 'snapshot': {self.rel: h}, 'records': {
            self.rel: {'sha256': h, 'disposition': 'no-candidate', 'situations': [],
                       'basis': 'Read retained account', 'inputs': {'retained/account.md': reuse.source_hash(evidence)}}}})
        reuse.run('render', self.root)
        old_identity = reuse.assess(self.root)['input_sha256']
        evidence.write_text('New observation')
        self.assertNotEqual(old_identity, reuse.assess(self.root)['input_sha256'])
        self.assertEqual(reuse.run('check', self.root)[0]['coverage']['changed'], [self.rel])

    def test_invalid_new_entry_during_render_is_rejected(self):
        original = reuse.assess
        calls = []
        def changing(root, temporary=None):
            calls.append(1)
            if len(calls) == 2:
                (root / 'reuse').mkdir(exist_ok=True)
                (root / 'reuse/unexpected').write_text('concurrent invalid input')
            return original(root, temporary)
        with patch.object(reuse, 'assess', changing):
            with self.assertRaisesRegex(ValueError, 'changed'):
                reuse.run('render', self.root)
        self.assertFalse((self.root / 'reuse/index.md').exists())

    def test_unclosed_block_reports_error(self):
        self.record.write_text('```evolution-situation\n{}')
        self.assertTrue(reuse.assess(self.root)['errors'])

    def test_symlink_source_is_rejected(self):
        alias = self.root / 'alias.md'
        alias.symlink_to(self.record)
        self.item['events'][0]['sources'] = ['alias.md']
        self.write_record()
        self.assertTrue(reuse.assess(self.root)['errors'])

    def test_failed_replace_preserves_output(self):
        reuse.run('render', self.root)
        output = self.root / 'reuse/index.md'
        before = output.read_bytes()
        with patch.object(reuse.os, 'replace', side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):
                reuse.run('render', self.root)
        self.assertEqual(before, output.read_bytes())
        self.assertEqual(list(output.parent.glob('.index-*')), [])

    def test_changed_input_during_render_is_rejected(self):
        original = reuse.assess
        calls = []
        def changing(root, temporary=None):
            calls.append(1)
            if len(calls) == 2:
                self.write_record('concurrent change')
            return original(root, temporary)
        with patch.object(reuse, 'assess', changing):
            with self.assertRaisesRegex(ValueError, 'changed'):
                reuse.run('render', self.root)
        self.assertFalse((self.root / 'reuse/index.md').exists())


if __name__ == '__main__':
    unittest.main()
