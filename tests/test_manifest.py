"""Portable package discovery and opt-in integration boundaries."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ManifestTests(unittest.TestCase):
    def manifest(self):
        return json.loads((ROOT / 'plugin.json').read_text())

    def test_one_portable_manifest(self):
        manifest = self.manifest()
        self.assertEqual(manifest['$schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertEqual(manifest['name'], 'pstack-openai')
        self.assertEqual(manifest['version'], '0.1.1')
        self.assertEqual(manifest['license'], 'MIT')
        self.assertLessEqual(set(manifest), {'$schema', 'name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords', 'extensions'})
        self.assertEqual(set(manifest['extensions']), {'com.openai'})
        interface = manifest['extensions']['com.openai']['interface']
        self.assertEqual(interface['displayName'], 'pstack-openai')
        # Portable discovery uses root skills/, not a manifest path override.
        self.assertNotIn('skills', manifest)
        self.assertNotIn('skills', manifest['extensions']['com.openai'])
        self.assertNotIn('interface', manifest)
        self.assertEqual(manifest['homepage'], 'https://github.com/cursor/plugins/blob/main/pstack/docs/guide/README.md')
        self.assertEqual(manifest['author'], {'name': 'Lauren Tan', 'url': 'https://x.com/poteto'})
        self.assertEqual(interface['websiteURL'], manifest['homepage'])
        self.assertEqual(interface['developerName'], manifest['author']['name'])
        self.assertNotIn('repository', manifest)
        asset = interface['logo']
        self.assertEqual(asset, './assets/logo.png')
        path = (ROOT / asset).resolve()
        self.assertTrue(path.is_relative_to(ROOT.resolve()))
        self.assertTrue(path.is_file())
        records = json.loads((ROOT / 'docs/parity/adaptations/02-manifest.json').read_text())
        record = next(row for row in records if row['upstreamPath'] == 'assets/logo.png')
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record['upstreamSha256'])
        self.assertEqual(record['adaptationStatus'], 'unchanged-reviewed')
        for row in records:
            for host in ('chatgpt', 'codex'):
                self.assertEqual(row['verification'][host], {'status': 'not-run', 'evidence': []})

    def test_no_incidental_integrations(self):
        manifest = self.manifest()
        for settings in (manifest, manifest['extensions']['com.openai']):
            for key in ('hooks', 'apps', 'mcpServers', 'mcp', 'agents'):
                self.assertNotIn(key, settings)
        for path in ('mcp.json', '.mcp.json', '.app.json', 'hooks', '.codex-plugin', '.cursor-plugin', '.codex/agents'):
            self.assertFalse((ROOT / path).exists(), path)


if __name__ == '__main__':
    unittest.main()
