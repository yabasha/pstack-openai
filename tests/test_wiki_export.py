"""Offline export checks against the actual canonical documentation."""
import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.export_wiki import export_wiki

ROOT = Path(__file__).resolve().parents[1]
HERD = Path.home() / 'Herd'


class WikiExportTests(unittest.TestCase):
    def fixture(self):
        context = tempfile.TemporaryDirectory(prefix='task23d-wiki-', dir=HERD)
        self.addCleanup(context.cleanup)
        return Path(context.name)

    def test_wiki_catalog_complete(self):
        output = self.fixture()
        pages = export_wiki(ROOT, output)
        leaves = list((ROOT / 'docs/skills').glob('*.md'))
        leaves = [p for p in leaves if p.name != 'README.md']
        from tools.baseline_policy import validate_policy
        inventory = json.loads((ROOT / 'docs/parity/inventory.json').read_text())
        counts = validate_policy(ROOT, inventory)
        expected = {Path(r['upstreamPath']).parent.name for r in inventory
                    if re.fullmatch(r'skills/[^/]+/SKILL\.md', r['upstreamPath'])}
        self.assertEqual({p.stem for p in leaves}, expected)
        self.assertEqual(len(leaves), counts['leafSkills'])
        self.assertEqual(sum(p.stem.startswith('principle-') for p in leaves), counts['principles'])
        for source in leaves + [ROOT / 'docs/setup/chatgpt.md', ROOT / 'docs/setup/codex.md']:
            self.assertTrue(any(source.relative_to(ROOT).as_posix() in p.read_text() for p in pages if p.suffix == '.md'))
        home = (output / 'Home.md').read_text()
        version = json.loads((ROOT / 'plugin.json').read_text())['version']
        self.assertIn(f'Package version: `{version}`.', home)
        self.assertRegex(home, r'Package commit: `[a-f0-9]{40}`')

    def test_wiki_links_resolve(self):
        output = self.fixture()
        export_wiki(ROOT, output)
        from tools.export_wiki import validate_links
        self.assertEqual([], validate_links({p.name:p.read_bytes() for p in output.iterdir()}))
        for overview in ('docs/skills/README.md', 'docs/principles/README.md', 'docs/guide/README.md'):
            source = (ROOT / overview).read_text()
            exported = next(p.read_text() for p in output.glob('*.md') if f'Source: `{overview}`' in p.read_text())
            for label in re.findall(r'\[([^\]]+)\]\(', source):
                self.assertIn(f'[{label}](', exported)

    def test_existing_output_not_overwritten(self):
        output = self.fixture()
        keep = output / 'keep.txt'
        keep.write_text('owned by somebody else')
        with self.assertRaises(ValueError):
            export_wiki(ROOT, output)
        self.assertEqual(keep.read_text(), 'owned by somebody else')
        with self.assertRaises(ValueError):
            export_wiki(ROOT, ROOT / 'docs')
        link = self.fixture() / 'linked'
        link.symlink_to(self.fixture(), target_is_directory=True)
        with self.assertRaises(ValueError):
            export_wiki(ROOT, link)

    def test_no_network_or_settings_changes(self):
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts}
        with patch('socket.socket', side_effect=AssertionError('network forbidden')):
            export_wiki(ROOT, self.fixture())
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in before})


if __name__ == '__main__':
    unittest.main()

class WikiAnchorTests(unittest.TestCase):
    def test_fenced_capture_literals_are_not_operative_links(self):
        from tools.export_wiki import validate_links
        captures = [
            '```json\n{"command":"printf \'```\'; [captured](/outside-root/file.md)"}\n```\n',
            '````json\n```\n[captured](/outside-root/file.md)\n````\n',
            '~~~json\n```\n[captured](/outside-root/file.md)\n~~~~\n',
            '```json\n``` trailing data\n[captured](/outside-root/file.md)\n```\n',
            '```json\n{"unclosed":"[captured](/outside-root/file.md)"}\n',
        ]
        for capture in captures:
            with self.subTest(capture=capture):
                self.assertEqual([], validate_links({'Home.md': capture.encode()}))
                if capture.endswith(('```\n', '````\n', '~~~~\n')):
                    self.assertTrue(validate_links({'Home.md': (capture + '\n[unsafe](/outside-root/live.md)\n').encode()}))

    def test_export_preserves_captured_fences_and_rejects_unsafe_live_link(self):
        from types import SimpleNamespace
        with tempfile.TemporaryDirectory(dir=HERD) as directory:
            root = Path(directory) / 'source'
            (root / 'docs/skills').mkdir(parents=True)
            (root / 'plugin.json').write_text(json.dumps({'version': 'fixture'}))
            for source in (ROOT / 'docs/skills').glob('*.md'):
                (root / 'docs/skills' / source.name).write_text('# Fixture\n')
            (root / 'docs/troubleshooting.md').write_text('# Fixture\n')
            (root / 'docs/safe.md').write_text('# Safe\n')
            capture = '````json\n{"command":"printf \'```\'; [captured](/outside-root/file.md)"}\n```\n[captured](/outside-root/second.md)\n````\n'
            page = root / 'docs/compatibility.md'
            page.write_text('# Fixture\n' + capture + '[operative](safe.md#safe)\n')
            output = Path(directory) / 'output'
            output.mkdir()
            with patch('tools.export_wiki.subprocess.run', return_value=SimpleNamespace(stdout='a' * 40)):
                export_wiki(root, output)
            exported = (output / 'docs--compatibility.md').read_text()
            self.assertIn(capture, exported)
            self.assertIn('[operative](docs--safe#safe)', exported)
            rejected = Path(directory) / 'rejected'
            rejected.mkdir()
            page.write_text(page.read_text() + '[unsafe](/outside-root/live.md)\n')
            with patch('tools.export_wiki.subprocess.run', return_value=SimpleNamespace(stdout='a' * 40)):
                with self.assertRaisesRegex(ValueError, 'unsafe documentation link'):
                    export_wiki(root, rejected)
            self.assertEqual([], list(rejected.iterdir()))

    def test_heading_fragments_and_directory_suffix(self):
        from tools.export_wiki import validate_links
        pages = {'Home.md': b'# Home\n[a](topic#same-1) [b](#home)\n', 'topic.md': b'# Same\n## Same\n'}
        self.assertEqual([],validate_links(pages))
        pages['Home.md'] += b'[bad](#missing)\n'
        self.assertTrue(validate_links(pages))
        from tools.export_wiki import heading_ids
        self.assertEqual({'same','same-1','same-1-1','inline-code'},heading_ids('# Same\n## Same\n# Same-1\n# Inline `code`\n```text\n# Not a heading\n```\n'))

    def test_directory_fragment_survives_export(self):
        import shutil
        with tempfile.TemporaryDirectory(dir=HERD) as directory:
            root=Path(directory)/'source';root.mkdir()
            shutil.copytree(ROOT/'docs',root/'docs')
            shutil.copytree(ROOT/'references',root/'references')
            shutil.copytree(ROOT/'skills',root/'skills')
            shutil.copytree(ROOT/'automations',root/'automations')
            for name in ('plugin.json','README.md','UPSTREAM.md','LICENSE'):
                shutil.copy2(ROOT/name,root/name)
            # Only this selected page matters in the focused export fixture.
            for p in list((root/'docs').rglob('*.md')):
                if 'skills' not in p.parts: p.write_text('# Fixture\n')
            for p in (root/'docs/skills').glob('*.md'): p.write_text('# Fixture\n')
            (root/'docs/compatibility.md').write_text('# Fixture\n[directory](fixture-support/#fixture-support)\n')
            support=root/'docs/fixture-support';support.mkdir();(support/'one.txt').write_text('fixture')
            output=Path(directory)/'output';output.mkdir()
            from types import SimpleNamespace
            with patch('tools.export_wiki.subprocess.run',return_value=SimpleNamespace(stdout='a'*40)):
                export_wiki(root,output)
            self.assertIn('(docs--fixture-support#fixture-support)',(output/'docs--compatibility.md').read_text())
