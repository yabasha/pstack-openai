"""Structural closure of the pinned source inventory, never host execution proof."""
import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

from tools.baseline_policy import validate_policy
from tools.build_catalog import load_cases
from tools.release_report import registry_checks
from tools.validate_package import schema_errors

ROOT = Path(__file__).resolve().parents[1]
from tests.fixture_paths import SOURCE


def read(path):
    return json.loads((ROOT / path).read_text())


class InventoryClosedTests(unittest.TestCase):
    def test_exact_reviewed_source_and_destination_ownership(self):
        rows = read('docs/parity/inventory.json')
        self.assertEqual([r['upstreamPath'] for r in rows],
                         (ROOT / 'docs/parity/baseline-paths.txt').read_text().splitlines())
        counts = validate_policy(ROOT, rows)
        policy = read('docs/parity/baseline-policy.json')
        manifest = read(f"docs/parity/upstream-manifests/{policy['upstreamCommit']}.json")
        sources = {r['upstreamPath']: r for r in manifest['files']}
        self.assertEqual(len(sources), len(manifest['files']))
        self.assertEqual({r['upstreamPath'] for r in rows}, set(sources))
        self.assertEqual(len(rows), counts['sourceFiles'])
        self.assertEqual(len({r['destinationPath'] for r in rows}), counts['sourceFiles'])
        self.assertEqual(schema_errors(rows, read('docs/parity/inventory.schema.json'), 'inventory'), [])
        for row in rows:
            with self.subTest(source=row['upstreamPath']):
                self.assertNotEqual(row['adaptationStatus'], 'pending')
                source = sources[row['upstreamPath']]
                self.assertEqual(row['upstreamCommit'], policy['upstreamCommit'])
                self.assertEqual(row['upstreamCommit'], source['upstreamCommit'])
                self.assertEqual(row['upstreamSha256'], source['upstreamSha256'])
                self.assertTrue((ROOT / row['destinationPath']).is_file())
                for dependency in row['dependencies']:
                    self.assertTrue((ROOT / dependency).exists(), dependency)
                if row['adaptationStatus'] == 'unchanged-reviewed':
                    self.assertEqual(hashlib.sha256((ROOT / row['destinationPath']).read_bytes()).hexdigest(),
                                     source['upstreamSha256'])
        roots = [r for r in rows if re.fullmatch(r'skills/[^/]+/SKILL\.md', r['upstreamPath'])]
        self.assertEqual(len(roots), counts['leafSkills'])
        self.assertEqual(sum('/principle-' in r['upstreamPath'] for r in roots), counts['principles'])
        self.assertEqual(len(rows) - len(roots), counts['supportFiles'])
        self.assertEqual(sum(r['upstreamPath'].startswith('skills/poteto-mode/playbooks/') for r in rows), counts['playbooks'])

    def test_fragments_have_one_current_owner_and_match_aggregate(self):
        rows = {r['upstreamPath']: r for r in read('docs/parity/inventory.json')}
        owners = {}
        for path in sorted((ROOT / 'docs/parity/adaptations').glob('*.json')):
            fragment = json.loads(path.read_text())
            self.assertIsInstance(fragment, list)
            for row in fragment:
                source = row['upstreamPath']
                self.assertNotIn(source, owners, f'{source}: {owners.get(source)} and {path.name}')
                owners[source] = path.name
                self.assertEqual({k: v for k, v in row.items() if k != 'verification'},
                                 {k: v for k, v in rows[source].items() if k != 'verification'})
        self.assertEqual(set(owners), set(rows))

    def test_registry_accounts_for_every_real_case_and_caller_limits(self):
        cases = load_cases(ROOT)
        registry = read('docs/parity/case-registry.json')
        entries = registry['entries']
        self.assertEqual(len(entries), len({e['caseId'] for e in entries}))
        self.assertEqual({e['caseId'] for e in entries}, set(cases))
        support = (ROOT / 'docs/parity/support-map.md').read_text()
        covered = set()
        for entry in entries:
            case_file, case = cases[entry['caseId']]
            self.assertEqual(schema_errors(case, read('docs/parity/cases/schema.json'), entry['caseId']), [])
            self.assertEqual(entry['caseFile'], case_file)
            self.assertEqual(entry['sourcePaths'], case['sourcePaths'])
            if entry['structuralOnly']:
                self.assertEqual(entry['requiredHosts'], [])
            else:
                self.assertEqual(entry['requiredHosts'], ['chatgpt', 'codex'])
                self.assertEqual(set(entry['hostStatus']), {'chatgpt', 'codex'})
                self.assertTrue(entry['requiredObservations']['pass'])
                self.assertTrue(entry['requiredObservations']['reduced-pass'])
                covered.update(entry['sourcePaths'])
        rows = read('docs/parity/inventory.json')
        self.assertEqual(covered, {row['upstreamPath'] for row in rows})
        self.assertEqual(registry_checks(ROOT, rows)[1], [])
        for row in rows:
            self.assertIn('`' + row['upstreamPath'] + '`', support)
            if row['upstreamPath'] not in covered:
                self.assertIn('`' + row['upstreamPath'] + '` | Missing behavioral caller', support)

    def test_discovery_requires_complete_installed_receipt_in_both_branches(self):
        entry = next(e for e in read('docs/parity/case-registry.json')['entries'] if e['caseId'] == 'package-discovery')
        paths = {r['upstreamPath'] for r in read('docs/parity/inventory.json')}
        expected = {p for p in paths if p == '.cursor-plugin/plugin.json' or re.fullmatch(r'skills/[^/]+/SKILL\.md', p) or (p.startswith('automations/benny/skills/') and p.endswith('/SKILL.md'))}
        self.assertEqual(set(entry['sourcePaths']), expected)
        policy = read('docs/parity/baseline-policy.json')
        self.assertEqual(expected, set(policy['rootSkills']) | set(policy['bennySkills']) | {'.cursor-plugin/plugin.json'})
        operations = {'discover-package', 'enumerate-skills', 'inspect-installed-copy'}
        self.assertEqual(set(entry['requiredObservations']['pass']), operations)
        self.assertEqual(set(entry['requiredObservations']['reduced-pass']), operations | {'read'})
        self.assertFalse(entry['structuralOnly'])

    def test_support_case_keeps_compile_proof_out_of_read_only_reduction(self):
        entry = next(e for e in read('docs/parity/case-registry.json')['entries'] if e['caseId'] == 'package-support-contracts')
        self.assertIn('compile-proof', entry['requiredObservations']['pass'])
        self.assertIn('read', entry['requiredObservations']['pass'])
        self.assertNotIn('compile-proof', entry['requiredObservations']['reduced-pass'])
        self.assertIn('inspect-installed-copy', entry['requiredObservations']['reduced-pass'])
        self.assertEqual(entry['requiredHosts'], ['chatgpt', 'codex'])
        self.assertFalse(entry['structuralOnly'])

    def test_lock_reconciliation_preserves_the_canonical_package_records(self):
        path = 'skills/poteto-mode/scripts/bun.lock'
        original = (SOURCE / path).read_text()
        adapted = (ROOT / path).read_text()
        self.assertEqual(adapted, original.replace('"bun-types": "latest"', '"bun-types": "1.3.14"')
                         .replace('"typescript": "latest"', '"typescript": "7.0.2"'))
        parse = lambda text: json.loads(re.sub(r',\s*([}\]])', r'\1', text))
        self.assertEqual(parse(original)['packages'], parse(adapted)['packages'])
        self.assertEqual(len(parse(adapted)['packages']), 25)
        record = next(r for r in read('docs/parity/inventory.json') if r['upstreamPath'] == path)
        self.assertEqual(record['adaptationStatus'], 'adapted-reviewed')
        self.assertEqual(record['upstreamSha256'], hashlib.sha256(original.encode()).hexdigest())
        reconciliation = read('docs/parity/reconciliations/task12-lock.json')
        self.assertIsNone(reconciliation['priorFragment'])
        self.assertEqual(reconciliation['integratedLockSha256'], hashlib.sha256(adapted.encode()).hexdigest())

    def test_additional_port_files_are_accounted_separately(self):
        files = set(subprocess.check_output(['git', 'ls-files'], cwd=ROOT, text=True).splitlines())
        files.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT, text=True).splitlines())
        files = {p for p in files if not p.startswith('.superpowers/')}
        files -= {r['destinationPath'] for r in read('docs/parity/inventory.json')}
        section = (ROOT / 'docs/parity/support-map.md').read_text().split('## Additional port-file provenance\n', 1)[1]
        documented = set(re.findall(r'^\| \[([^\]]+)\]\(', section, re.M))
        reserved_section = section.split('## Reserved report-only paths\n', 1)[1]
        reserved = set(re.findall(r'^\| `([^`]+)` \|', reserved_section, re.M))
        expected_reserved = {
            'docs/releases/0.1.0.md',
            'docs/testing/release-checklist.md',
            'docs/parity/tested-package.json',
            'docs/releases/remaining-controller-report.md',
        }
        self.assertEqual(reserved, expected_reserved)
        self.assertFalse(documented & reserved)
        self.assertEqual(documented, files - (files & reserved))
        # Every declared future report can appear without changing this frozen map.
        self.assertEqual(documented, (files | reserved) - reserved)
        unknown = 'docs/releases/unreserved-future-report.md'
        self.assertNotEqual(documented, (files | {unknown}) - reserved)

    def test_notices_and_ignored_working_data_preserve_provenance(self):
        self.assertEqual((ROOT / 'LICENSE').read_bytes(), (SOURCE / 'LICENSE').read_bytes())
        notice = (ROOT / 'NOTICE.md').read_text()
        self.assertIn('Copyright (c) 2026 Lauren Tan', notice)
        self.assertIn('ba2205db1f83295154e31abc762f533954f581bb', notice)
        for path in ['.upstream/probe', '.superpowers/sdd/2026-10-07-pstack-openai/task-24-fixtures/probe', 'skills/poteto-mode/scripts/node_modules/probe']:
            self.assertEqual(subprocess.run(['git', 'check-ignore', '--no-index', '-q', path], cwd=ROOT).returncode, 0, path)
        for path in ['docs/parity/inventory.json', 'docs/parity/evidence/probe.json', 'docs/parity/reconciliations/probe.json']:
            self.assertEqual(subprocess.run(['git', 'check-ignore', '--no-index', '-q', path], cwd=ROOT).returncode, 1, path)


if __name__ == '__main__':
    unittest.main()
