import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from tools.validate_package import validate_package, inspect_package, quoted_regions

ROOT = Path(__file__).resolve().parents[1]


def record(path, status='adapted-reviewed'):
    return dict(upstreamPath=path, upstreamCommit='a'*40, upstreamSha256='b'*64,
                destinationPath=path, disposition='runtime', rationale='Reviewed fixture.',
                dependencies=[], licenseProvenance=dict(license='MIT', copyright='Copyright (c) 2026 Lauren Tan', sourcePath='LICENSE'),
                adaptationStatus=status, verification={h: dict(status='not-run', evidence=[]) for h in ('chatgpt', 'codex')})


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for path in ('inventory.schema.json',):
            self.write('docs/parity/'+path, (ROOT/'docs/parity'/path).read_text())
        self.write('docs/parity/cases/schema.json', (ROOT/'docs/parity/cases/schema.json').read_text() if (ROOT/'docs/parity/cases/schema.json').exists() else '{}')
        self.write('plugin.json', '{}')
        self.write('skills/demo/SKILL.md', '---\nname: demo\n---\nDo work.\n')
        self.rows = [record('skills/demo/SKILL.md')]

    def write(self, path, content):
        file = self.root/path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content)
        return file

    def fails(self, path):
        self.assertTrue(any(path in error for error in validate_package(self.root, self.rows)))

    def test_actual_patterns_fenced_links_are_literal_data(self):
        source = (ROOT/'skills/typescript-best-practices/references/patterns.md').read_text()
        self.assertIn('type Pairs<T> = [T, T][];', source)
        self.write('skills/demo/SKILL.md', source)
        self.assertEqual(validate_package(self.root, self.rows), [])
        self.write('skills/demo/SKILL.md', source + '\n[real](gone.md) [real][undefined]\n')
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any('gone.md' in error for error in errors))
        self.assertTrue(any('undefined Markdown reference' in error for error in errors))

    def test_fenced_literals_do_not_hide_operative_remnants(self):
        self.write('skills/demo/SKILL.md', '```text\n[example](url) [T,T][]\nUse Task and gpt-4.\n```\n')
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any("remnant 'Task'" in error for error in errors))
        self.assertTrue(any("remnant 'gpt-4'" in error for error in errors))
        self.assertFalse(any('missing path' in error or 'undefined Markdown' in error for error in errors))

    def test_actual_reflection_quote_requires_exact_hash_line_and_token(self):
        import hashlib
        path = 'skills/reflect/references/synthesizer.md'
        source = (ROOT/path).read_text()
        file = self.write('skills/demo/SKILL.md', source)
        entries = [dict(entry, path='skills/demo/SKILL.md') for entry in
                   json.loads((ROOT/'docs/parity/remnant-dispositions.json').read_text())
                   if entry['path'] == path]
        self.assertEqual({entry['token'] for entry in entries}, {'gpt-4', 'gpt-4o'})
        self.assertEqual({entry['sha256'] for entry in entries}, {hashlib.sha256(file.read_bytes()).hexdigest()})
        self.write('docs/parity/remnant-dispositions.json', json.dumps(entries))
        self.assertEqual(validate_package(self.root, self.rows), [])
        self.write('skills/demo/SKILL.md', source + '\nUse Task and gpt-4 for workers.\n')
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any(':28:' in error for error in errors))
        self.assertTrue(any("remnant 'Task'" in error for error in errors))
        self.assertTrue(any("remnant 'gpt-4o'" in error for error in errors))
        for entry in entries:
            entry['sha256'] = hashlib.sha256(file.read_bytes()).hexdigest()
        self.write('docs/parity/remnant-dispositions.json', json.dumps(entries))
        errors = validate_package(self.root, self.rows)
        self.assertFalse(any(':28:' in error for error in errors))
        self.assertTrue(any('for workers' in line for line in file.read_text().splitlines()))
        self.assertTrue(any("remnant 'Task'" in error for error in errors))
        self.assertTrue(any("remnant 'gpt-4'" in error for error in errors))

    def test_actual_why_template_preserves_contract_and_real_links(self):
        source = (ROOT/'skills/why/references/synthesizer-prompt.md').read_text()
        self.assertIn('Source: [PR #123](url) / ticket ID / file:line.', source)
        self.write('skills/demo/SKILL.md', source)
        self.assertEqual(validate_package(self.root, self.rows), [])
        self.write('skills/demo/SKILL.md', source + '\n[operative](url)\n')
        self.fails('skills/demo/url')

    def test_broken_reference(self):
        self.write('skills/demo/SKILL.md', '[missing](missing.md)')
        self.fails('skills/demo/missing.md')

    def test_inline_code_references_are_ignored(self):
        for content in ('Use `[T, T][]`.', 'Use ``[T, `T`][]``.', 'Use `[missing](gone.md)`.', 'Use `[label]: gone.md`.', '`first line\n[T, T][]`', '`first line\n< 5 [T, T][]`', '`first line\n<span> [T, T][]`'):
            with self.subTest(content=content):
                self.write('skills/demo/SKILL.md', content)
                self.assertEqual(validate_package(self.root, self.rows), [])

    def test_inline_code_keeps_same_line_reference_checks(self):
        self.write('skills/demo/SKILL.md', '`[T, T][]` then [real][missing]')
        self.assertTrue(any('[missing]: undefined Markdown reference' in error for error in validate_package(self.root, self.rows)))

    def test_unmatched_inline_delimiters_keep_reference_checks(self):
        for content in ('`[real][missing]', '``[real][missing]`', '`[real][missing]``', '\\`[real][missing]`', '`[real][missing]\n\n`'):
            with self.subTest(content=content):
                self.write('skills/demo/SKILL.md', content)
                self.assertTrue(any('[missing]: undefined Markdown reference' in error for error in validate_package(self.root, self.rows)))

    def test_inline_code_keeps_same_line_link_containment(self):
        self.write('skills/demo/SKILL.md', '`[T, T][]` then [outside](../../../outside.md)')
        self.assertTrue(any('escapes package' in error for error in validate_package(self.root, self.rows)))

    def test_inline_code_does_not_exempt_remnants(self):
        self.write('skills/demo/SKILL.md', '`Task`')
        self.assertTrue(any("remnant 'Task'" in error for error in validate_package(self.root, self.rows)))

    def test_inline_delimiters_do_not_cross_interrupting_blocks(self):
        for boundary in ('# H', '> quote', '- item', '1. item', '-', '--', '---', '===', '```text', '~~~text', '<div>', '</DIV>', '<script>', '<?process', '<![CDATA[', '<!DOCTYPE html>', '<!-- comment -->'):
            for link, expected in (('[real][missing]', 'undefined Markdown reference'), ('[outside](../../../outside.md)', 'escapes package')):
                with self.subTest(boundary=boundary, link=link):
                    self.write('skills/demo/SKILL.md', f'`\n{boundary}\n{link}\n`')
                    self.assertTrue(any(expected in error for error in validate_package(self.root, self.rows)))

    def test_absolute_reference_api_and_cli(self):
        self.write('skills/demo/SKILL.md', '[outside](/tmp/outside.md)')
        self.fails('/tmp/outside.md')
        inventory = self.write('docs/parity/inventory.json', json.dumps(self.rows))
        result = subprocess.run(['python3', str(ROOT/'tools/validate_package.py'), '--root', str(self.root), '--inventory', str(inventory)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('/tmp/outside.md', result.stdout)
        inside = self.write('inside.md', 'Existing file.')
        self.write('skills/demo/SKILL.md', f'[absolute inside]({inside})')
        self.fails(str(inside))

    def test_source_only_range_stays_inside_quote(self):
        import hashlib
        file = self.write('skills/demo/SKILL.md', '```text\nTask upstream example\n```\n[operative](gone.md)\n')
        entry = dict(path='skills/demo/SKILL.md', sha256=hashlib.sha256(file.read_bytes()).hexdigest(), token='Task', startLine=2, endLine=4, kind='source-only', rationale='Quoted source example.', reviewed=True)
        self.write('docs/parity/remnant-dispositions.json', json.dumps([entry]))
        self.fails('skills/demo/gone.md')
        entry['endLine'] = 999999
        self.write('docs/parity/remnant-dispositions.json', json.dumps([entry]))
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any('range' in error and 'skills/demo/SKILL.md' in error for error in errors))
        self.assertTrue(any('skills/demo/gone.md' in error for error in errors))
        entry['startLine'] = entry['endLine'] = 2
        self.write('docs/parity/remnant-dispositions.json', json.dumps([entry]))
        self.fails('skills/demo/gone.md')

    def test_source_only_operative_token_is_not_quote(self):
        import hashlib
        file = self.write('skills/demo/SKILL.md', 'Use Task to do work. [missing](gone.md)\n')
        entry = dict(path='skills/demo/SKILL.md', sha256=hashlib.sha256(file.read_bytes()).hexdigest(), token='Task', startLine=1, endLine=1, kind='source-only', rationale='Claims to be an example.', reviewed=True)
        self.write('docs/parity/remnant-dispositions.json', json.dumps([entry]))
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any('explicit quote' in error for error in errors))
        self.assertTrue(any('skills/demo/gone.md' in error for error in errors))

    def test_inline_backticks_do_not_open_fenced_example(self):
        import hashlib
        file = self.write('skills/demo/SKILL.md', '```not a fence```\nUse Task. [operative](gone.md)\n```\n')
        entry = dict(path='skills/demo/SKILL.md', sha256=hashlib.sha256(file.read_bytes()).hexdigest(), token='Task', startLine=2, endLine=2, kind='source-only', rationale='Claims a fenced source example.', reviewed=True)
        self.write('docs/parity/remnant-dispositions.json', json.dumps([entry]))
        errors = validate_package(self.root, self.rows)
        self.assertTrue(any('explicit quote' in error for error in errors))
        self.assertTrue(any('skills/demo/gone.md' in error for error in errors))

    def test_fence_opening_and_closing_syntax(self):
        self.assertEqual(quoted_regions(['```python', 'Task example', '````  ']), [(2, 2)])
        self.assertEqual(quoted_regions(['~~~text `info`', 'Task example', '~~~']), [(2, 2)])
        self.assertEqual(quoted_regions(['```text', 'Task example', '```not closing', 'more example', '```']), [(2, 4)])
        self.assertEqual(quoted_regions(['    ```', 'Task operative', '```']), [])
        self.assertEqual(quoted_regions(['> Task quoted example', 'Operative text']), [(1, 1)])

    def test_path_escape(self):
        self.rows[0]['destinationPath'] = '../outside.md'
        self.fails('../outside.md')

    def test_symlink_escape(self):
        (self.root/'skills/demo/link.md').symlink_to(ROOT/'README.md')
        self.write('skills/demo/SKILL.md', '[unsafe](link.md)')
        self.fails('skills/demo/link.md')

    def test_duplicate_root_skill(self):
        self.write('skills/other/SKILL.md', '---\nname: demo\n---\n')
        self.fails('skills/other/SKILL.md')

    def test_benny_not_registered(self):
        self.write('skills/benny/SKILL.md', '---\nname: benny\n---\n')
        self.fails('skills/benny/SKILL.md')

    def test_deferred_reference_blocks_full_acceptance(self):
        self.write('skills/demo/SKILL.md', '[pending](../../references/pending.md)')
        self.rows.append(record('references/pending.md', 'pending'))
        errors, deferred = inspect_package(self.root, self.rows, 'skills/demo/SKILL.md')
        self.assertEqual(errors, [])
        self.assertIn('references/pending.md', '\n'.join(deferred))
        self.fails('references/pending.md')

    def test_missing_scoped_target_is_not_deferred(self):
        self.rows.append(record('references/missing-own.md', 'pending'))
        errors, deferred = inspect_package(self.root, self.rows, 'references/missing-own.md')
        self.assertTrue(any('references/missing-own.md' in error for error in errors))
        self.assertEqual(deferred, [])
        inventory = self.write('docs/parity/inventory.json', json.dumps(self.rows))
        result = subprocess.run(['python3', str(ROOT/'tools/validate_package.py'), '--root', str(self.root), '--inventory', str(inventory), '--scope', 'references/missing-own.md'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('references/missing-own.md', result.stdout)
        self.assertNotIn('DEFERRED', result.stdout)

    def test_nested_cases_and_global_duplicate_ids(self):
        case = dict(id='same', sourcePaths=['skills/demo/SKILL.md'], prompt='Do work.', requirements=['Result.'], expectedFull='Full.', expectedReduced='Reduced.', expectedBlocked='Blocked.', forbiddenClaims=['No inventions.'])
        self.write('docs/parity/cases/skills/demo.json', json.dumps(case))
        self.write('docs/parity/cases/playbooks/demo.json', json.dumps([case]))
        self.assertTrue(any('duplicate case id same' in error for error in validate_package(self.root, self.rows)))
        del case['expectedBlocked']
        self.write('docs/parity/cases/playbooks/demo.json', json.dumps([case]))
        errors, _ = inspect_package(self.root, self.rows, 'skills/demo/SKILL.md')
        self.assertTrue(any('cases/playbooks/demo.json.expectedBlocked' in error for error in errors))
        self.write('docs/parity/cases/skills/demo.json', json.dumps(case))
        self.assertTrue(any('cases/skills/demo.json.expectedBlocked' in error for error in validate_package(self.root, self.rows)))

    def test_case_symlink_escape_is_rejected_before_read(self):
        # Guard the actual read boundary so the test proves rejection before I/O.
        from unittest.mock import patch
        target = ROOT/'plugin.json'
        link = self.root/'docs/parity/cases/skills/escape.json'
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target)
        original = Path.read_text
        def guarded(file, *args, **kwargs):
            if file == link:
                raise AssertionError('Escaping case symlink must not be read')
            return original(file, *args, **kwargs)
        with patch.object(Path, 'read_text', guarded):
            self.fails('docs/parity/cases/skills/escape.json')

    def test_cursor_remnant_needs_disposition(self):
        self.write('skills/demo/SKILL.md', 'Use AskQuestion and Task with .cursor/config.')
        self.fails('skills/demo/SKILL.md')

    def test_unknown_enum(self):
        self.rows[0]['adaptationStatus'] = 'reviewed'
        self.fails('adaptationStatus')

    def test_case_array_scope_and_schema(self):
        case = dict(id='demo', sourcePaths=['skills/demo/SKILL.md'], prompt='Do work.', requirements=['One result.'], expectedFull='Workers finish.', expectedReduced='Sequential result.', expectedBlocked='Explain missing tools.', forbiddenClaims=['Do not invent workers.'])
        self.write('docs/parity/cases/demo.json', json.dumps([case]))
        self.assertEqual(inspect_package(self.root, self.rows, 'skills/demo/SKILL.md')[0], [])
        del case['expectedBlocked']
        self.write('docs/parity/cases/demo.json', json.dumps([case]))
        self.fails('expectedBlocked')

    def test_broad_disposition_fails(self):
        self.write('docs/parity/remnant-dispositions.json', json.dumps([dict(path='skills/*', sha256='a'*64, token='Task', startLine=1, endLine=999, kind='source-only', rationale='Ignore all examples.', reviewed=True)]))
        self.fails('skills/*')

    def test_manifest_reference_escape(self):
        self.write('plugin.json', json.dumps({'extensions': {'com.openai': {'interface': {'logo': '../outside.png'}}}}))
        self.fails('../outside.png')

    def test_port_added_document_reference(self):
        self.write('docs/guide.md', '[broken](gone.md)')
        self.fails('docs/gone.md')

    def test_source_example_requires_exact_review(self):
        import hashlib
        file = self.write('skills/demo/SKILL.md', '```text\nTask upstream example\n```\n')
        self.write('docs/parity/remnant-dispositions.json', json.dumps([dict(path='skills/demo/SKILL.md', sha256=hashlib.sha256(file.read_bytes()).hexdigest(), token='Task', startLine=2, endLine=2, kind='source-only', rationale='Quoted source example.', reviewed=True)]))
        self.assertEqual(validate_package(self.root, self.rows), [])
        file.write_text(file.read_text()+'Task operative instruction\n')
        self.fails('skills/demo/SKILL.md')

    def test_cli_exit_codes(self):
        inventory = self.write('docs/parity/inventory.json', json.dumps(self.rows))
        command = ['python3', str(ROOT/'tools/validate_package.py'), '--root', str(self.root), '--inventory', str(inventory)]
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        self.write('skills/demo/SKILL.md', '[bad](gone.md)')
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/demo/gone.md', result.stdout)
        inventory.write_text('{')
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)
        self.assertEqual(subprocess.run(command+['--unknown'], capture_output=True).returncode, 2)

class FragmentClosureTests(unittest.TestCase):
    setUp = PackageTests.setUp
    write = PackageTests.write
    fails = PackageTests.fails

    def test_inert_review_sources_are_excluded_but_operative_links_and_destinations_rejected(self):
        self.write(".upstream/reviews/source.md", "Use Task and [missing](gone.md).\n")
        self.assertEqual([], validate_package(self.root, self.rows))
        self.write("skills/demo/SKILL.md", "[source](../../.upstream/reviews/source.md)\n")
        self.fails("inert")
        self.rows[0]["destinationPath"] = ".upstream/reviews/source.md"
        self.fails("inert")

    def test_unknown_duplicate_and_conflicting_active_fragments_rejected(self):
        import copy
        for bad in ('unknown','duplicate','conflict'):
            fragment = copy.deepcopy(self.rows)
            if bad == 'unknown': fragment[0]['upstreamPath'] = 'skills/unknown/SKILL.md'
            if bad == 'duplicate': fragment += copy.deepcopy(fragment)
            if bad == 'conflict': fragment[0]['upstreamCommit'] = 'c'*40
            self.write('docs/parity/adaptations/one.json', json.dumps(fragment))
            self.assertTrue(any('fragment' in e for e in validate_package(self.root,self.rows)), bad)
        self.write('docs/parity/adaptations/one.json', json.dumps(self.rows))
        self.assertEqual([],validate_package(self.root,self.rows))
