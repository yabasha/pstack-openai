import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from tools.validate_package import validate_package, inspect_package

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

    def test_broken_reference(self):
        self.write('skills/demo/SKILL.md', '[missing](missing.md)')
        self.fails('skills/demo/missing.md')

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
