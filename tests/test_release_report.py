"""Release policy fixtures are structural tests, never host observations."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from tools.release_report import summarize_release, assess_release, DISCOVERY

ROOT = Path(__file__).resolve().parents[1]
COMMIT = 'a' * 40


class ReleaseSummaryTests(unittest.TestCase):
    def test_not_run_is_not_coverage(self):
        result = summarize_release([], [{'status': 'not-run', 'packageCommit': COMMIT}], COMMIT)
        self.assertFalse(result['releasable'])
        self.assertEqual(result['workflowCoverage']['observedSourceFiles'], 0)

    def test_blocked_is_not_pass(self):
        result = summarize_release([], [{'status': 'blocked', 'host': 'codex', 'packageCommit': COMMIT}], COMMIT)
        self.assertFalse(result['releasable'])
        self.assertEqual(result['byHost']['codex']['pass'], 0)

    def test_mixed_package_versions_rejected(self):
        result = summarize_release([], [{'packageVersion': v, 'packageCommit': COMMIT} for v in ('1', '2')], COMMIT)
        self.assertIn('mixed package versions', result['blockers'])

    def test_stale_evidence_invalidated(self):
        result = summarize_release([], [{'caseId': 'old', 'packageCommit': 'b' * 40}], COMMIT)
        self.assertEqual(len(result['staleEvidence']), 1)
        self.assertFalse(result['releasable'])

def write(root, path, value):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2) if not isinstance(value, str) else value)


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def commit(root):
    git(root, 'add', '.')
    git(root, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
        '-c', 'commit.gpgsign=false', 'commit', '-qm', 'fixture')
    return git(root, 'rev-parse', 'HEAD')


def fixture(root):
    inventory = json.loads((ROOT / 'docs/parity/inventory.json').read_text())
    paths = [r['upstreamPath'] for r in inventory]
    for row in inventory:
        row['destinationPath'] = row['upstreamPath']
        row['dependencies'] = []
        row['adaptationStatus'] = 'adapted-reviewed'
        row['disposition'] = 'runtime'
        row['verification'] = {h: {'status': 'reduced-pass', 'evidence': ['docs/parity/evidence/results.json']} for h in ('chatgpt', 'codex')}
        write(root, row['destinationPath'], 'Fixture content.\n')
    for path in ('docs/parity/inventory.schema.json', 'docs/parity/cases/schema.json'):
        write(root, path, json.loads((ROOT / path).read_text()))
    write(root, 'plugin.json', {'version': '0.1.0'})
    write(root, 'docs/parity/inventory.json', inventory)
    discovery_paths = sorted(p for p in paths if p == '.cursor-plugin/plugin.json' or
                             re.fullmatch(r'skills/[^/]+/SKILL\.md', p) or
                             (p.startswith('automations/benny/skills/') and p.endswith('/SKILL.md')))
    entries = []
    for case_id, scope in (('all-callers', paths), ('package-discovery', discovery_paths)):
        case_path = f'docs/parity/cases/{case_id}.json'
        write(root, case_path, dict(id=case_id, sourcePaths=scope, prompt='Observe fixture',
              requirements=['Observe'], expectedFull='Full observation', expectedReduced='Reduced observation',
              expectedBlocked='Explicit block', forbiddenClaims=['Inferred pass']))
        entries.append(dict(caseId=case_id, caseFile=case_path, sourcePaths=scope,
              requiredHosts=['chatgpt', 'codex'], structuralOnly=False,
              executionModes={'pass':['direct','workers'],'reduced-pass':['direct','sequential','workers']}, requiredPermissions={'pass':[],'reduced-pass':[]},
              hostStatus={'chatgpt': 'not-run', 'codex': 'not-run'},
              requiredObservations={'pass': sorted(DISCOVERY) if case_id == 'package-discovery' else ['read'],
                  'reduced-pass': sorted(DISCOVERY | {'read'}) if case_id == 'package-discovery' else ['read']}))
    write(root, 'docs/parity/case-registry.json', dict(schemaVersion=1, entries=entries, structuralChecks=[]))
    for path in sorted((ROOT / 'docs/catalog/skills').glob('*.json')):
        item = json.loads(path.read_text())
        item['caseIds'] = ['all-callers']
        write(root, path.relative_to(ROOT), item)
    git(root, 'init', '-q')
    frozen = commit(root)
    evidence = []
    report_paths = ['docs/parity/evidence/results.json']
    for host in ('chatgpt', 'codex'):
        receipt_path = f'docs/parity/evidence/{host}.txt'
        receipt = dict(schemaVersion=1, kind='pstack-package-discovery', host=host,
              packageVersion='0.1.0', packageCommit=frozen, installedCopy=f'fixture-only:{host}',
              rootSkills=sorted(Path(p).parent.name for p in paths if re.fullmatch(r'skills/[^/]+/SKILL\.md', p)),
              excludedSkills=sorted(p for p in discovery_paths if p.startswith('automations/')))
        write(root, receipt_path, receipt)
        report_paths.append(receipt_path)
        for entry in entries:
            discovery = entry['caseId'] == 'package-discovery'
            operations = sorted(DISCOVERY | {'spawn', 'inspect-result'}) if discovery else ['read']
            evidence.append(dict(caseId=entry['caseId'], sourcePaths=entry['sourcePaths'],
                packageVersion='0.1.0', packageCommit=frozen, host=host, hostMode='synthetic-fixture',
                date='2026-10-08', documentedCapabilities=[], exposedTools=['fixture'],
                successfulOperations=[dict(operation=op, tool='fixture', evidence=receipt_path) for op in operations],
                permissions=dict(execution='granted', writes='denied', externalActions='denied'),
                models=dict(requested='unknown', actual='unknown'), priorActionIdentities=[],
                input='Synthetic input', observedOutput='Synthetic output', artifacts=[receipt_path],
                status='pass' if discovery else 'reduced-pass', execution='workers' if discovery else 'sequential',
                limits=[] if discovery else ['Sequential fixture only; writes and external actions denied']))
    write(root, 'docs/parity/evidence/results.json', evidence)
    write(root, 'docs/parity/tested-package.json', dict(schemaVersion=1, kind='pstack-tested-package', testedCommit=frozen, reportPaths=report_paths))
    commit(root)
    return frozen


class RootPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_temp = tempfile.TemporaryDirectory(prefix='release-policy-', dir=ROOT.parent)
        cls.base = Path(cls.base_temp.name)
        cls.frozen = fixture(cls.base)

    @classmethod
    def tearDownClass(cls):
        cls.base_temp.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='release-case-', dir=ROOT.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(self.base, self.root, dirs_exist_ok=True)

    def read(self, path):
        return json.loads((self.root / path).read_text())

    def report(self):
        return assess_release(self.root, self.frozen, '0.1.0')

    def change_records(self, transform):
        path = 'docs/parity/evidence/results.json'
        records = self.read(path)
        transform(records)
        write(self.root, path, records)

    def assertBlocked(self, phrase):
        report = self.report()
        self.assertFalse(report['releasable'])
        self.assertTrue(any(phrase in b for b in report['blockers']), report['blockers'])

    def test_positive_complete_reduced_policy_with_frozen_ancestor(self):
        report = self.report()
        self.assertTrue(report['releasable'], report['blockers'])
        self.assertEqual(report['testedCommit'], self.frozen)
        self.assertNotEqual(report['reportCommit'], self.frozen)
        self.assertEqual(report['byHost']['codex']['reduced-pass'], 1)
        self.assertEqual(report['byHost']['codex']['pass'], 1)
        self.assertTrue(report['byHost']['codex']['packageDiscovery'])
        self.assertEqual(report['workflowCoverage']['sourceFiles'],
                         len(self.read('docs/parity/inventory.json')))

    def test_summary_does_not_claim_filesystem_proof(self):
        result = summarize_release(self.read('docs/parity/inventory.json'), self.read('docs/parity/evidence/results.json'), self.frozen)
        self.assertFalse(result['releasable'])
        self.assertTrue(result['logicalEligibility'])
        self.assertTrue(result['validationRequired'])
        self.assertIn('unverified', result['proof'])

    def test_required_case_missing(self):
        self.change_records(lambda records: records.pop(0))
        self.assertBlocked('required case lacks validated result')

    def test_registry_applicability_cannot_be_count_only(self):
        path = 'docs/parity/case-registry.json'
        registry = self.read(path)
        registry['entries'][0]['requiredHosts'] = ['codex']
        write(self.root, path, registry)
        self.assertBlocked('no behavioral caller applicability')

    def test_missing_artifact(self):
        (self.root / 'docs/parity/evidence/codex.txt').unlink()
        self.assertBlocked('artifacts: missing')

    def test_stale_required_evidence(self):
        self.change_records(lambda records: records[0].update(packageCommit='b' * 40))
        self.assertBlocked('stale evidence')

    def test_wrong_version(self):
        self.change_records(lambda records: records[0].update(packageVersion='9.0.0'))
        self.assertBlocked('packageVersion differs')

    def test_incomplete_reduced_discovery_is_rejected(self):
        self.change_records(lambda records: records[1].update(status='reduced-pass', execution='sequential', limits=['Reduced']))
        self.assertBlocked('actual package discovery')

    def test_discovery_requires_installed_enumeration(self):
        path = 'docs/parity/evidence/codex.txt'
        value = self.read(path)
        value['rootSkills'].pop()
        write(self.root, path, value)
        self.assertBlocked('exact installed-copy enumeration')

    def test_no_pass_transfer_to_report_head(self):
        report = assess_release(self.root, git(self.root, 'rev-parse', 'HEAD'), '0.1.0')
        self.assertFalse(report['releasable'])
        self.assertTrue(report['staleEvidence'])

    def test_operative_change_invalidates_frozen_proof(self):
        write(self.root, 'skills/architect/SKILL.md', 'Changed operative content.\n')
        commit(self.root)
        self.assertBlocked('Operative package differs')

    def test_report_marker_cannot_exempt_operative_change(self):
        path = 'docs/parity/tested-package.json'
        value = self.read(path)
        value['reportPaths'].append('skills/architect/SKILL.md')
        write(self.root, path, value)
        commit(self.root)
        self.assertBlocked('cannot exempt operative content')

    def test_blocked_optional_is_visible_and_accepted(self):
        self.change_records(lambda records: records[0].update(status='blocked', execution='unavailable',
            permissions=dict(execution='unavailable', writes='denied', externalActions='denied'),
            successfulOperations=[], limits=['Execution unavailable in synthetic fixture']))
        path = 'docs/parity/inventory.json'
        rows = self.read(path)
        for row in rows:
            row['verification']['chatgpt']['status'] = 'blocked'
        write(self.root, path, rows)
        commit(self.root)
        report = self.report()
        self.assertTrue(report['releasable'], report['blockers'])
        self.assertEqual(report['byHost']['chatgpt']['blocked'], 1)

    def test_pending_disposition_rejected(self):
        path = 'docs/parity/inventory.json'
        rows = self.read(path)
        rows[0]['adaptationStatus'] = 'pending'
        write(self.root, path, rows)
        self.assertBlocked('unreviewed disposition')

    def test_required_fail_and_not_run_rejected(self):
        for status in ('fail', 'not-run'):
            with self.subTest(status=status):
                self.change_records(lambda records: records[0].update(status=status))
                self.assertBlocked('required case lacks validated result')

    def test_cli_exit_zero_and_one(self):
        command = ['python3', '-B', str(ROOT / 'tools/release_report.py'), '--root', str(self.root), '--commit', self.frozen, '--version', '0.1.0']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)['releasable'])
        result = subprocess.run(command[:-1] + ['9.0.0'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)['releasable'])

    def test_unregistered_case_cannot_disappear(self):
        case = self.read('docs/parity/cases/all-callers.json')
        case['id'] = 'unregistered'
        write(self.root, 'docs/parity/cases/unregistered.json', case)
        self.assertBlocked('case lacks registry applicability')

    def test_conflicting_fragment_rejected(self):
        row = self.read('docs/parity/inventory.json')[0]
        row['rationale'] = 'Conflicting mapping rationale'
        write(self.root, 'docs/parity/adaptations/conflict.json', [row])
        self.assertBlocked('conflicting adaptation fragment')

    def test_invalid_evidence_does_not_inflate_observed_coverage(self):
        for host in ('chatgpt', 'codex'):
            (self.root / f'docs/parity/evidence/{host}.txt').unlink()
        report = self.report()
        self.assertEqual(report['workflowCoverage']['observedSourceFiles'], 0)
        for host in ('chatgpt','codex'):
            self.assertEqual(0,report['byHost'][host]['pass'])
            self.assertEqual(0,report['byHost'][host]['reduced-pass'])
            self.assertEqual(1,report['rawClaimsByHost'][host]['pass'])

    def test_duplicate_discovery_cannot_count_as_validated_pass(self):
        self.change_records(lambda records: records.append(dict(records[1])))
        report=self.report()
        self.assertEqual(0,report['byHost']['chatgpt']['pass'])
        self.assertFalse(report['byHost']['chatgpt']['packageDiscovery'])
        self.assertTrue(any('duplicate/conflicting' in e for e in report['blockers']))

    def test_discovery_excludes_nested_skills(self):
        path = 'docs/parity/evidence/codex.txt'
        value = self.read(path)
        value['excludedSkills'] = []
        write(self.root, path, value)
        self.assertBlocked('exact installed-copy enumeration')

    def test_same_count_wrong_canonical_path_rejected(self):
        path = 'docs/parity/inventory.json'
        rows = self.read(path)
        rows[0]['upstreamPath'] = '.cursor-plugin/other.json'
        write(self.root, path, rows)
        self.assertBlocked('canonical source paths')

    def test_discovery_operations_cannot_come_from_other_case(self):
        self.change_records(lambda records: records.__setitem__(slice(None), [r for r in records if r['caseId'] != 'package-discovery']))
        self.assertBlocked('actual package discovery')

    def test_ignored_uncommitted_receipt_cannot_supply_proof(self):
        # This ignored proof path is absent from both immutable trees.
        git(self.root, 'config', 'core.excludesFile', str(self.root / '.git/info/exclude'))
        (self.root / '.git/info/exclude').write_text('ignored-receipt.txt\n')
        original = self.read('docs/parity/evidence/codex.txt')
        write(self.root, 'ignored-receipt.txt', original)
        self.change_records(lambda records: records[3].update(
            artifacts=['ignored-receipt.txt'], successfulOperations=[
                dict(operation=op, tool='fixture', evidence='ignored-receipt.txt')
                for op in sorted(DISCOVERY | {'spawn', 'inspect-result'})]))
        commit(self.root)
        self.assertBlocked('proof files are not committed')

    def test_extra_root_skill_rejected(self):
        write(self.root, 'skills/unregistered/SKILL.md', 'Unexpected root skill\n')
        self.assertBlocked('actual root skill discovery differs')

    def sequential_discovery(self):
        def reduce(records):
            for record in records:
                if record['caseId'] == 'package-discovery':
                    record.update(status='reduced-pass', execution='sequential',
                        limits=['No independent workers; writes and external actions denied'])
                    receipt = record['artifacts'][0]
                    record['successfulOperations'] = [dict(operation=op, tool='fixture', evidence=receipt)
                        for op in sorted(DISCOVERY | {'read'})]
        self.change_records(reduce)

    def test_complete_sequential_discovery_without_workers_is_ready(self):
        self.sequential_discovery()
        commit(self.root)
        report = self.report()
        self.assertTrue(report['releasable'], report['blockers'])
        for host in ('chatgpt', 'codex'):
            self.assertTrue(report['byHost'][host]['packageDiscovery'])
            self.assertEqual(report['byHost'][host]['pass'], 0)
            self.assertEqual(report['byHost'][host]['reduced-pass'], 2)
        self.assertEqual(report['workflowCoverage']['fullObservedSourceFiles'], 0)

    def test_sequential_discovery_requires_all_operations(self):
        self.sequential_discovery()
        self.change_records(lambda records: records[1]['successfulOperations'].pop(0))
        self.assertBlocked('missing required observation')

    def test_sequential_discovery_requires_exact_receipt(self):
        self.sequential_discovery()
        path = 'docs/parity/evidence/chatgpt.txt'
        receipt = self.read(path)
        receipt['packageCommit'] = 'b' * 40
        write(self.root, path, receipt)
        self.assertBlocked('exact installed-copy enumeration')

    def test_sequential_discovery_requires_complete_enumeration(self):
        self.sequential_discovery()
        path = 'docs/parity/evidence/chatgpt.txt'
        receipt = self.read(path)
        receipt['rootSkills'].pop()
        write(self.root, path, receipt)
        self.assertBlocked('exact installed-copy enumeration')

    def test_discovery_registry_requires_reduced_observations(self):
        path = 'docs/parity/case-registry.json'
        registry = self.read(path)
        registry['entries'][1]['requiredObservations']['reduced-pass'] = ['read']
        write(self.root, path, registry)
        self.assertBlocked('package-discovery registry contract is incomplete')
