"""Structural catalog checks; these do not execute host workflows."""
import copy
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inputs():
    inventory = json.loads((ROOT / 'docs/parity/inventory.json').read_text())
    entries = [json.loads(p.read_text()) for p in sorted((ROOT / 'docs/catalog/skills').glob('*.json'))]
    return inventory, entries


class CatalogTests(unittest.TestCase):
    def test_deferred_canonical_root_links_only_its_inert_destination(self):
        from tools.build_catalog import build_catalog
        inventory, entries = inputs()
        pages = build_catalog(ROOT, inventory, entries)
        for row in inventory:
            source = row['upstreamPath']
            if re.fullmatch(r'skills/[^/]+/SKILL.md', source) and row['destinationPath'] != source:
                page = pages[f'docs/skills/{source.split("/")[1]}.md']
                self.assertIn('This source is not an invocable skill.', page)
                self.assertIn(row['destinationPath'], page)
                self.assertNotIn(f'](../../{source})', page)

    def test_catalog_exact_name_sets(self):
        from tools.build_catalog import build_catalog
        inventory, entries = inputs()
        pages = build_catalog(ROOT, inventory, entries)
        expected = {r['upstreamPath'].split('/')[1] for r in inventory
                    if re.fullmatch(r'skills/[^/]+/SKILL.md', r['upstreamPath'])}
        from tools.baseline_policy import validate_policy
        counts = validate_policy(ROOT, inventory)
        self.assertEqual(counts['leafSkills'], len(expected))
        self.assertEqual(expected, {e['name'] for e in entries})
        self.assertEqual(counts['principles'], sum(e['kind'] == 'principle' for e in entries))
        self.assertEqual({f'docs/skills/{name}.md' for name in expected} |
                         {'docs/skills/README.md', 'docs/principles/README.md'}, set(pages))
        for bad in (entries[:-1], entries + [dict(entries[0], name='extra')], entries + [entries[0]]):
            with self.assertRaises(ValueError):
                build_catalog(ROOT, inventory, bad)

    def test_catalog_required_fields(self):
        from tools.build_catalog import build_catalog
        inventory, entries = inputs()
        schema = json.loads((ROOT / 'docs/catalog/schema.json').read_text())
        self.assertEqual(set(entries[0]), set(schema['required']))
        pages = build_catalog(ROOT, inventory, entries)
        for entry in entries:
            page = pages[f"docs/skills/{entry['name']}.md"]
            for field in schema['required']:
                broken = copy.deepcopy(entries)
                del broken[0][field]
                with self.assertRaises(ValueError):
                    build_catalog(ROOT, inventory, broken)
            for field in ('purpose', 'ordinaryExample'):
                self.assertIn(entry[field], page)
            for field in ('triggers', 'inputs', 'outputs', 'capabilityLimits'):
                for value in entry[field]:
                    self.assertIn(value, page)
            for label in ('Full', 'Reduced', 'Blocked', 'Upstream commit', 'SHA-256'):
                self.assertIn(label, page)
            rows = {row['upstreamPath']: row for row in inventory}
            for source in entry['sourcePaths']:
                section = page.split(f'### `{source}`\n', 1)[1].split('### ', 1)[0]
                self.assertIn(rows[source]['upstreamSha256'], section)
                self.assertIn(rows[source]['disposition'], section)
            self.assertIn('[current parity inventory](../parity/inventory.json)', page)
            for host in ('chatgpt', 'codex'):
                self.assertIn(f'[{host} host report](../testing/{host}.md)', page)
            self.assertNotRegex(page, r'(?m)^- (?:chatgpt|codex): `(?:not-run|pass|reduced-pass|blocked|fail)`')
            self.assertNotIn('Tested release evidence:', page)
        broken = copy.deepcopy(entries)
        broken[0]['name'] = '../escape'
        with self.assertRaises(ValueError):
            build_catalog(ROOT, inventory, broken)
        broken = copy.deepcopy(entries)
        broken[0]['kind'] = 'other'
        with self.assertRaises(ValueError):
            build_catalog(ROOT, inventory, broken)

    def test_verification_advancement_does_not_change_frozen_pages(self):
        from tools.build_catalog import build_catalog
        inventory, entries = inputs()
        pages = build_catalog(ROOT, inventory, entries)
        advanced = copy.deepcopy(inventory)
        for row in advanced:
            for host, verification in row['verification'].items():
                verification['status'] = 'fail' if verification['status'] != 'fail' else 'pass'
                verification['evidence'] = [f'docs/testing/{host}.md']
        advanced_pages = build_catalog(ROOT, advanced, entries)
        self.assertEqual(set(pages), set(advanced_pages))
        changed = [path for path in pages
                   if pages[path].encode() != advanced_pages[path].encode()]
        self.assertEqual([], changed, 'Post-freeze verification must not change source-frozen catalog pages')

    def test_catalog_stale_generation(self):
        from tools.build_catalog import build_catalog, sync_catalog
        inventory, entries = inputs()
        pages = build_catalog(ROOT, inventory, entries)
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as tmp:
            fixture = Path(tmp)
            sentinel = fixture / 'docs/skills/unrelated.md'
            sentinel.parent.mkdir(parents=True)
            sentinel.write_text('preserve me')
            self.assertEqual(len(pages), len(sync_catalog(fixture, pages, check=True)))
            sync_catalog(fixture, pages, check=False)
            self.assertEqual([], sync_catalog(fixture, pages, check=True))
            target = fixture / 'docs/skills/architect.md'
            target.write_text('stale')
            self.assertEqual(['docs/skills/architect.md'], sync_catalog(fixture, pages, check=True))
            self.assertEqual('stale', target.read_text())
            self.assertEqual('preserve me', sentinel.read_text())
            files = {'docs/parity/inventory.json', 'docs/catalog/schema.json',
                     'docs/testing/chatgpt.md', 'docs/testing/codex.md'}
            files.update(str(path.relative_to(ROOT)) for path in (ROOT / 'docs/parity/cases').rglob('*.json'))
            files.update(str(path.relative_to(ROOT)) for path in (ROOT / 'docs/catalog/skills').glob('*.json'))
            rows = {row['upstreamPath']: row for row in inventory}
            for entry in entries:
                files.update(entry['dependencies'])
                files.update(rows[source]['destinationPath'] for source in entry['sourcePaths'])
            for source in files:
                destination = fixture / source
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / source, destination)
            cli = subprocess.run([sys.executable, '-B', str(ROOT / 'tools/build_catalog.py'),
                                  '--root', str(fixture), '--check'], capture_output=True, text=True)
            self.assertEqual(1, cli.returncode, cli.stdout + cli.stderr)
            self.assertIn('docs/skills/architect.md', cli.stdout)
            self.assertEqual('stale', target.read_text())
            with self.assertRaises(ValueError):
                sync_catalog(fixture, {'README.md': 'unsafe'}, check=False)
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'tools/build_catalog.py'),
                                 '--root', str(ROOT), '--check'], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_catalog_example_case_link(self):
        from tools.build_catalog import build_catalog, load_cases
        inventory, entries = inputs()
        pages = build_catalog(ROOT, inventory, entries)
        cases = load_cases(ROOT)
        for entry in entries:
            page = pages[f"docs/skills/{entry['name']}.md"]
            for case_id in entry['caseIds']:
                path, case = cases[case_id]
                self.assertTrue(set(entry['sourcePaths']) & set(case['sourcePaths']))
                self.assertIn(case['prompt'], page)
                self.assertIn(f'[{case_id}]', page)
                for field in ('expectedFull', 'expectedReduced', 'expectedBlocked'):
                    self.assertIn(case[field], page)
            for link in re.findall(r'\]\(([^)]+)\)', page):
                self.assertTrue((ROOT / f"docs/skills/{entry['name']}.md").parent.joinpath(link).resolve().exists(), link)
        broken = copy.deepcopy(entries)
        broken[0]['caseIds'] = ['missing-case']
        with self.assertRaises(ValueError):
            build_catalog(ROOT, inventory, broken)


if __name__ == '__main__':
    unittest.main()
