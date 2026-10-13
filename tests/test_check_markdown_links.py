"""Behavioral checks for the public candidate-tree link checker."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_markdown_links.py'
spec = importlib.util.spec_from_file_location('check_markdown_links', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LinkChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')
        return target

    def run_check(self):
        return checker.Checker(self.root).run()

    def test_historical_unchanged_incoming_reference(self):
        # Minimal verbatim excerpts from the Oct 11 Yak revision. The reference
        # was unchanged; the renamed destination made it invalid. See fixtures.md.
        main = 'skills/yak-shaving-triage/SKILL.md'
        ref = self.put('skills/yak-shaving-triage/references/discovery-lenses.md',
                       'Then [return the evidence to Guard the Next Branch]'
                       '(../SKILL.md#1-guard-the-next-branch).\n')
        before = ref.read_bytes()
        self.put(main, '## 1. Guard the Next Branch\n')
        self.assertEqual(self.run_check()['exit_code'], 0)
        self.put(main, '## 1. Establish capture and guard the next branch\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 1)
        self.assertEqual(report['errors'][0]['source'], str(ref.relative_to(self.root)))
        self.assertEqual(ref.read_bytes(), before)
        self.put(str(ref.relative_to(self.root)), before.decode().replace(
            '#1-guard-the-next-branch', '#1-establish-capture-and-guard-the-next-branch'))
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_missing_file_and_candidate_isolation(self):
        self.put('README.md', '[outside](skills/evolve-skills/SKILL.md)\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 1)  # Never falls back to this repository.
        self.assertIn('does not exist', report['errors'][0]['reason'])

    def test_formatted_unicode_and_duplicate_headings(self):
        self.put('README.md', '# **Hello** `world` & café 中文!\n'
                 '# Repeat\n# Repeat\n# Repeat-1\n# Repeat\n'
                 '[one](#hello-world--café-中文)\n[two](#repeat-1)\n'
                 '[three](#repeat-1-1)\n[four](#repeat-2)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_setext_headings(self):
        self.put('README.md', 'Title\n=====\n\n[x](#title)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_image_alt_formatting_in_headings(self):
        self.put('exists.png', 'image')
        self.put('README.md', '# ![a _b_ c](exists.png)\n[x](#a-b-c)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_escaped_and_entity_brackets_are_literal(self):
        self.put('README.md', r'\[example][undefined]' + '\n&#91;example][undefined]\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_reference_detection_respects_label_code_and_escape_boundaries(self):
        for text in (r'[example\][undefined]', '[a `][undefined]`'):
            with self.subTest(text=text):
                self.put('README.md', text + '\n')
                self.assertEqual(self.run_check()['exit_code'], 0)

    def test_unsupported_reference_inside_image_is_reported(self):
        self.put('exists.png', 'image')
        self.put('README.md', '# ![a [b][no]](exists.png)\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 2)
        self.assertIn('[b][no]', report['incomplete'][0]['link'])

    def test_literal_percent_filename(self):
        self.put('a%zz.md', '# Fine\n')
        self.put('README.md', '[x](a%zz.md)\n[encoded](a%25zz.md)\n')
        self.assertEqual(self.run_check()['exit_code'], 0)

    def test_references_images_spaces_parentheses_and_titles(self):
        self.put('docs/agents/a (b).md', '# Target\n')
        self.put('image.png', 'image')
        self.put('README.md', '[named][ref]\n![image][pic]\n[ref][]\n[ref]\n'
                 '[inline](<docs/agents/a (b).md#target> "Title")\n'
                 '[encoded](docs/agents/a%20%28b%29.md#target)\n\n'
                 '[ref]: <docs/agents/a (b).md#target>\n[pic]: image.png\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 0)
        self.assertEqual(report['local_links_checked'], 6)

    def test_code_examples_and_frontmatter_are_not_links(self):
        self.put('README.md', '---\ndescription: "[example](absent)"\n---\n'
                 '`[inline](absent)`\n\n```md\n[example](absent)\n```\n'
                 '\n~~~md\n[example](absent)\n~~~\n\n    [example](absent)\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 0)
        self.assertEqual(report['local_links_checked'], 0)

    def test_source_lines_and_original_syntax(self):
        self.put('README.md', '---\nname: demo\n---\n\nA paragraph\n'
                 'with [bad](no%20file.md "title").\n')
        error = self.run_check()['errors'][0]
        self.assertEqual(error['line'], 6)
        self.assertEqual(error['link'], '[bad](no%20file.md "title")')

    def test_tables_and_nested_image_links(self):
        self.put('README.md', '| Link |\n| --- |\n| [bad](missing.md) |\n\n'
                 '[![alt](missing.png)](also-missing.md)\n')
        self.assertEqual(len(self.run_check()['errors']), 3)

    def test_external_links_not_fetched(self):
        self.put('README.md', '[web](https://invalid.example)\n'
                 '<https://invalid.example/auto>\n[email](mailto:user@example.invalid)\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 0)
        self.assertEqual(len(report['skipped']), 3)

    def test_outside_root_and_symlinks_are_incomplete(self):
        self.put('README.md', '[outside](../outside.md)\n[alias](alias.md)\n')
        (self.root / 'alias.md').symlink_to(SCRIPT)
        report = self.run_check()
        self.assertEqual(report['exit_code'], 2)
        self.assertTrue(any('escapes' in item['reason'] for item in report['incomplete']))

    def test_unsupported_syntax_is_not_success(self):
        for text in ('<a id="custom"></a>\n', '[x][undefined]\n',
                     '[x](README.md?view=1)\n', '[x](/absolute.md)\n',
                     '[x](file:///tmp/outside.md)\n', '[x](README.md#%FF)\n'):
            with self.subTest(text=text):
                self.put('README.md', text)
                self.assertEqual(self.run_check()['exit_code'], 2)

    def test_non_markdown_fragment_incomplete_but_directory_valid(self):
        self.put('README.md', '[dir](docs/)\n[pdf](docs/a.pdf#page=1)\n')
        self.put('docs/a.pdf', 'placeholder')
        self.assertEqual(self.run_check()['exit_code'], 2)

    def test_scope_includes_unchanged_public_docs_excludes_private_and_fixtures(self):
        for path in ('AGENTS.md', 'skills/demo/SKILL.md', 'docs/agents/guide.md', 'docs/adr/0001.md'):
            self.put(path, '[bad](missing.md)\n')
        for path in ('docs/skill-evolution/old.md', 'docs/plans/plan.md',
                     'docs/research/a.md', 'tests/fixtures/a.md',
                     'skills/demo/tests/example.md', 'skills/demo/node_modules/a.md'):
            self.put(path, '[bad](missing.md)\n')
        report = self.run_check()
        self.assertEqual(report['files_scanned'], 4)
        self.assertEqual(len(report['errors']), 4)

    def test_empty_missing_and_unreadable_roots(self):
        self.assertEqual(self.run_check()['exit_code'], 2)
        self.assertEqual(checker.Checker(self.root / 'absent').run()['exit_code'], 2)
        self.put('README.md', '').write_bytes(b'\xff')
        self.assertEqual(self.run_check()['exit_code'], 2)

    def test_comments_are_ignored_and_incomplete_takes_precedence(self):
        self.put('README.md', '<!-- [x](missing.md) -->\n')
        self.assertEqual(self.run_check()['exit_code'], 0)
        self.put('README.md', '[bad](missing.md)\n\n<div>unsupported</div>\n')
        report = self.run_check()
        self.assertEqual(report['exit_code'], 2)
        self.assertEqual(len(report['errors']), 1)

    def test_cli_reports_all_three_statuses_and_does_not_write(self):
        for text, code, status in [('# OK\n', 0, 'passed'),
                                   ('[bad](absent)\n', 1, 'broken'),
                                   ('<div>x</div>\n', 2, 'incomplete')]:
            self.put('README.md', text)
            before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
            result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), '--json'],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, code, result.stderr)
            self.assertEqual(json.loads(result.stdout)['status'], status)
            self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})


if __name__ == '__main__':
    unittest.main()
