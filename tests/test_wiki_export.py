"""Offline export checks against the actual canonical documentation."""
import hashlib
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.export_wiki import export_wiki

ROOT = Path(__file__).resolve().parents[1]
HERD = ROOT.parent


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
        self.assertEqual(len(leaves), 51)
        self.assertEqual(sum(p.stem.startswith('principle-') for p in leaves), 24)
        for source in leaves + [ROOT / 'docs/setup/chatgpt.md', ROOT / 'docs/setup/codex.md']:
            self.assertTrue(any(source.relative_to(ROOT).as_posix() in p.read_text() for p in pages if p.suffix == '.md'))
        home = (output / 'Home.md').read_text()
        self.assertIn('0.1.0', home)
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
