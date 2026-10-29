"""Read-only release policy assessment.

summarize_release is a pure, list-only summary. Its releasable value is False
pending root proof; logicalEligibility describes only the supplied list facts.
assess_release and the CLI supply the boolean decision after registry, artifact,
structural and immutable Git checks. No list-only call asserts filesystem proof.

Policy accepts explicit blocked optional capabilities and validated reductions,
while both hosts must observe package discovery and invocation. Discovery uses
the package-discovery case with discover-package, enumerate-skills and
inspect-installed-copy operations. Direct or worker pass and sequential reduced-pass
can prove complete discovery. Reduced execution never proves independent workers.
These labels describe observations, never host API names. Every source file must
have a behavioral caller case on both hosts; structural cases cannot replace it.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.build_catalog import load_cases, validate_entries
from tools.validate_evidence import validate_evidence
from tools.validate_package import schema_errors, validate_package
from tools.sync_upstream import committed_tree, rollback_tested_commit, TESTED_PACKAGE_PATH

HOSTS = ('chatgpt', 'codex')
STATUSES = ('pass', 'reduced-pass', 'blocked', 'fail', 'not-run')
DISCOVERY = {'discover-package', 'enumerate-skills', 'inspect-installed-copy'}
CONTRACT_ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text())


def summarize_release(inventory: list[dict], evidence: list[dict], commit: str, *, expected_counts=None) -> dict:
    """Summarize unverified claims without asserting missing root proof."""
    blockers, stale = [], []
    paths = [r.get('upstreamPath', '') for r in inventory]
    leaves = [p for p in paths if re.fullmatch(r'skills/[^/]+/SKILL\.md', p)]
    playbooks = [p for p in paths if re.fullmatch(r'skills/poteto-mode/playbooks/[^/]+\.md', p)]
    counts = dict(sourceFiles=len(paths), leafSkills=len(leaves),
                  principles=sum(p.startswith('skills/principle-') for p in leaves),
                  supportFiles=len(paths)-len(leaves), playbooks=len(playbooks))
    if counts != (expected_counts or dict(sourceFiles=164, leafSkills=51, principles=24, supportFiles=113, playbooks=23)):
        blockers.append('incomplete source closure for reviewed baseline policy')
    if len(set(paths)) != len(paths):
        blockers.append('duplicate or conflicting source dispositions')
    if not re.fullmatch('[0-9a-f]{40}', commit):
        blockers.append('commit must be an exact lowercase Git SHA')
    for row in inventory:
        if row.get('adaptationStatus') not in ('unchanged-reviewed', 'adapted-reviewed', 'reference-only-reviewed'):
            blockers.append(f"unreviewed disposition: {row.get('upstreamPath')}")
        if row.get('disposition') not in ('runtime', 'reference-only', 'metadata-replaced', 'relocated'):
            blockers.append(f"invalid disposition: {row.get('upstreamPath')}")
        for host in HOSTS:
            status = row.get('verification', {}).get(host, {}).get('status')
            if status not in ('pass', 'reduced-pass', 'blocked'):
                blockers.append(f"{host}: unresolved source verification: {row.get('upstreamPath')}")
    by_host = {h: {s: 0 for s in STATUSES} for h in HOSTS}
    observed = set()
    versions = {r.get('packageVersion') for r in evidence if r.get('packageVersion')}
    if len(versions) > 1:
        blockers.append('mixed package versions')
    for record in evidence:
        identity = {'caseId': record.get('caseId'), 'host': record.get('host'), 'packageCommit': record.get('packageCommit')}
        if record.get('packageCommit') != commit:
            stale.append(identity)
            continue
        host, status = record.get('host'), record.get('status')
        if host in HOSTS and status in STATUSES:
            by_host[host][status] += 1
        if status in ('pass', 'reduced-pass'):
            observed.update(record.get('sourcePaths', []))
        if status not in ('pass', 'reduced-pass', 'blocked'):
            blockers.append(f"unresolved evidence: {identity}")
        if status == 'blocked' and not record.get('limits'):
            blockers.append(f"blocked evidence needs explicit limits: {identity}")
    if stale:
        blockers.append('stale evidence cannot transfer to the requested commit')
    counts['observedSourceFiles'] = len(observed & set(paths))
    return dict(workflowCoverage=counts, byHost=by_host, blockers=blockers,
                staleEvidence=stale, releasable=False, logicalEligibility=not blockers,
                validationRequired=True,
                proof='unverified list claims; root validation required',
                limitations=[{'caseId': r.get('caseId'), 'host': r.get('host'),
                              'status': r.get('status'), 'limits': r.get('limits', [])}
                             for r in evidence if r.get('status') != 'pass'])


def registry_checks(root, inventory):
    registry = read_json(root / 'docs/parity/case-registry.json')
    if registry.get('schemaVersion') != 1 or not isinstance(registry.get('entries'), list):
        raise ValueError('invalid registry version or entries')
    cases = load_cases(root)
    entries, errors = {}, []
    sources = {r['upstreamPath'] for r in inventory}
    coverage = {h: set() for h in HOSTS}
    case_schema = read_json(CONTRACT_ROOT / 'docs/parity/cases/schema.json')
    for entry in registry['entries']:
        case_id = entry['caseId']
        if case_id in entries:
            raise ValueError('duplicate registry case: ' + case_id)
        entries[case_id] = entry
        if case_id not in cases:
            raise ValueError('missing registered case: ' + case_id)
        case_file, case = cases[case_id]
        errors += schema_errors(case, case_schema, case_id)
        if case_file != entry['caseFile'] or set(case['sourcePaths']) != set(entry['sourcePaths']):
            errors.append('registry case scope mismatch: ' + case_id)
        if not set(entry['sourcePaths']) <= sources:
            errors.append('registry contains unknown source: ' + case_id)
        hosts = entry['requiredHosts']
        if len(hosts) != len(set(hosts)) or not set(hosts) <= set(HOSTS) or type(entry['structuralOnly']) is not bool:
            raise ValueError('invalid registry applicability: ' + case_id)
        if entry['structuralOnly']:
            if hosts:
                errors.append('structural case has required hosts: ' + case_id)
            continue
        if not hosts:
            errors.append('behavioral case lacks required hosts: ' + case_id)
        for status in ('pass','reduced-pass'):
            for field, allowed in (('executionModes',{'direct','workers'} if status == 'pass' else {'direct','workers','sequential'}),('requiredPermissions',{'execution','writes','externalActions'})):
                values=entry.get(field,{}).get(status)
                if not isinstance(values,list) or len(values)!=len(set(values)) or not set(values)<=allowed or (field=='executionModes' and not values):
                    errors.append('invalid case '+field+': '+case_id)
        if entry.get('requiredMethod') not in (None,'arena','swarm','swarm-partition'):
            errors.append('unknown required method: '+case_id)
        if entry.get('requiredMethod') and (entry['executionModes']['pass'] != ['workers'] or not {'execution','writes'} <= set(entry['requiredPermissions']['pass'])):
            errors.append('method requires worker execution and write permissions: '+case_id)
        for host in hosts:
            coverage[host].update(entry['sourcePaths'])
    for host in HOSTS:
        for path in sorted(sources - coverage[host]):
            errors.append(f'{host}: no behavioral caller applicability: {path}')
    for case_id in sorted(set(cases) - set(entries)):
        errors.append('case lacks registry applicability: ' + case_id)
    discovery = entries.get('package-discovery')
    discovery_sources = {p for p in sources if p == '.cursor-plugin/plugin.json'
                         or re.fullmatch(r'skills/[^/]+/SKILL\.md', p)
                         or (p.startswith('automations/benny/skills/') and p.endswith('/SKILL.md'))}
    if (not discovery or discovery['structuralOnly']
            or set(discovery['requiredHosts']) != set(HOSTS)
            or set(discovery['sourcePaths']) != discovery_sources
            or not DISCOVERY <= set(discovery.get('requiredObservations', {}).get('pass', []))
            or not (DISCOVERY | {'read'}) <= set(discovery.get('requiredObservations', {}).get('reduced-pass', []))):
        errors.append('package-discovery registry contract is incomplete')
    catalog = [read_json(p) for p in sorted((root / 'docs/catalog/skills').glob('*.json'))]
    validate_entries(inventory, catalog)
    for item in catalog:
        catalog_sources = set()
        for case_id in item['caseIds']:
            entry = entries.get(case_id)
            if not entry or entry['structuralOnly'] or set(entry['requiredHosts']) != set(HOSTS):
                errors.append('catalog case lacks full applicability: ' + case_id)
            else:
                catalog_sources.update(entry['sourcePaths'])
        if not set(item['sourcePaths']) <= catalog_sources:
            errors.append('catalog sources lack caller cases: ' + item['name'])
    return entries, errors


def identity_checks(root, commit, version, inventory):
    """C7 permits only the existing immutable tested-package marker contract."""
    head = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'],
                          check=True, capture_output=True, text=True).stdout.strip()
    files = committed_tree(root, head)
    for path, (data, mode) in files.items():
        target = root / path
        if target.is_symlink() or not target.is_file() or target.read_bytes() != data or (target.stat().st_mode & 0o777) != mode:
            raise ValueError('working tree differs from report revision: ' + path)
    untracked = subprocess.run(['git', '-C', str(root), 'ls-files', '--others', '--exclude-standard'],
                               check=True, capture_output=True, text=True).stdout
    if untracked.strip():
        raise ValueError('untracked package files prevent immutable proof')
    # Ignored receipts and definitions must not supply uncommitted proof.
    proof_paths = set()
    for directory in ('docs/parity/evidence', 'docs/parity/cases', 'docs/catalog/skills', 'docs/parity/adaptations'):
        proof_paths.update(p.relative_to(root).as_posix() for p in (root / directory).rglob('*.json'))
    for path in (root / 'docs/parity/evidence').rglob('*.json'):
        records = read_json(path)
        for record in records if isinstance(records, list) else [records]:
            proof_paths.update(record['artifacts'])
            proof_paths.update(op['evidence'] for op in record['successfulOperations'])
    if not proof_paths <= set(files):
        raise ValueError('proof files are not committed: ' + ', '.join(sorted(proof_paths - set(files))))
    if head != commit:
        tested, tested_version = rollback_tested_commit(root, head, files, inventory)
        if tested != commit or tested_version != version:
            raise ValueError('tested-package identity differs from requested commit/version')
    elif TESTED_PACKAGE_PATH in files:
        marker = read_json(root / TESTED_PACKAGE_PATH)
        if marker.get('testedCommit') != commit:
            raise ValueError('report revision is not the declared tested commit')
    if json.loads(files['plugin.json'][0])['version'] != version:
        raise ValueError('requested version differs from package manifest')
    return head


def discovery_receipt(root, record, inventory, commit, version):
    """Require the installed-copy observation to carry exact enumeration data."""
    names = sorted(Path(r['destinationPath']).parent.name for r in inventory
                   if re.fullmatch(r'skills/[^/]+/SKILL\.md', r['destinationPath']))
    excluded = sorted(r['destinationPath'] for r in inventory
                      if r['upstreamPath'].startswith('automations/benny/skills/')
                      and r['upstreamPath'].endswith('/SKILL.md'))
    for operation in record['successfulOperations']:
        if operation['operation'] != 'inspect-installed-copy' or operation['evidence'] not in record['artifacts']:
            continue
        try:
            receipt = read_json(root / operation['evidence'])
            if (set(receipt) == {'schemaVersion', 'kind', 'host', 'packageCommit', 'packageVersion', 'installedCopy', 'rootSkills', 'excludedSkills'}
                    and receipt.get('schemaVersion') == 1 and receipt.get('kind') == 'pstack-package-discovery'
                    and receipt.get('host') == record['host'] and receipt.get('packageCommit') == commit
                    and receipt.get('packageVersion') == version and isinstance(receipt.get('installedCopy'), str)
                    and receipt['installedCopy'].strip() and receipt.get('rootSkills') == names
                    and receipt.get('excludedSkills') == excluded):
                return True
        except (OSError, ValueError, AttributeError):
            continue
    return False


def assess_release(root: Path, commit: str, version: str) -> dict:
    """Assess complete root proof, returning a final boolean release decision."""
    root = root.resolve()
    report = dict(workflowCoverage={}, byHost={}, blockers=[], staleEvidence=[], releasable=False)
    try:
        inventory = read_json(root / 'docs/parity/inventory.json')
        errors = schema_errors(inventory, read_json(CONTRACT_ROOT / 'docs/parity/inventory.schema.json'), 'inventory')
        if errors:
            report['blockers'] += errors
            return report
        evidence, evidence_files = [], {}
        for path in sorted((root / 'docs/parity/evidence').rglob('*.json')):
            records = read_json(path)
            records = records if isinstance(records, list) else [records]
            for record in records:
                if not isinstance(record, dict):
                    raise ValueError('evidence must contain objects')
                evidence.append(record)
                evidence_files[id(record)] = path.relative_to(root).as_posix()
        from tools.baseline_policy import POLICY_PATH, validate_policy
        counts = validate_policy(root, inventory) if (root / POLICY_PATH).exists() else None
        report = summarize_release(inventory, evidence, commit, expected_counts=counts)
        report['rawClaimsByHost'] = {h: dict(v) for h,v in report['byHost'].items()}
        report['byHost'] = {h: {s: 0 for s in STATUSES} for h in HOSTS}
        report['proof'] = 'root structural, applicability, artifacts and immutable package checks'
        errors = report['blockers']
        expected = ((root if counts is not None else CONTRACT_ROOT) / 'docs/parity/baseline-paths.txt').read_text().splitlines()
        if sorted(r['upstreamPath'] for r in inventory) != expected:
            errors.append('inventory does not match canonical source paths')
        baseline = inventory if counts is not None else read_json(CONTRACT_ROOT / 'docs/parity/inventory.json')
        identities = {r['upstreamPath']: (r['upstreamCommit'], r['upstreamSha256']) for r in baseline}
        if any(identities.get(r['upstreamPath']) != (r['upstreamCommit'], r['upstreamSha256']) for r in inventory):
            errors.append('canonical source hashes or pin differ')
        # The structural validator applies fragments; release closure must also
        # reject stale/conflicting fragments rather than let them override rows.
        rows = {r['upstreamPath']: r for r in inventory}
        for path in sorted((root / 'docs/parity/adaptations').glob('*.json')):
            for fragment in read_json(path):
                current = rows.get(fragment['upstreamPath'])
                if current is None or any(v != current.get(k) for k, v in fragment.items() if k != 'verification'):
                    errors.append('conflicting adaptation fragment: ' + str(path.relative_to(root)))
        errors += validate_package(root, inventory)
        expected_skills = {r['destinationPath'] for r in inventory
                           if re.fullmatch(r'skills/[^/]+/SKILL\.md', r['destinationPath'])}
        actual_skills = {p.relative_to(root).as_posix() for p in (root / 'skills').glob('*/SKILL.md')}
        if actual_skills != expected_skills:
            errors.append('actual root skill discovery differs from inventoried leaves')
        entries, registry_errors = registry_checks(root, inventory)
        errors += registry_errors
        valid, seen, discovery = {}, set(), {h: set() for h in HOSTS}
        for record in evidence:
            issues = validate_evidence(record, commit, root)
            if record.get('packageVersion') != version:
                issues.append('packageVersion differs from requested version')
            key = (record.get('host'), record.get('caseId'))
            if key in seen:
                valid.pop(key, None)
                issues.append('duplicate/conflicting case observation')
            seen.add(key)
            if record.get('status') == 'blocked' and (not record.get('limits') or not record.get('artifacts')):
                issues.append('blocked case requires limits and an artifact')
            if not issues and record['caseId'] == 'package-discovery' and record['status'] in ('pass', 'reduced-pass'):
                if not discovery_receipt(root, record, inventory, commit, version):
                    issues.append('package discovery lacks exact installed-copy enumeration receipt')
            errors += [f'{key}: {issue}' for issue in issues]
            if not issues:
                valid[key] = record
        for (host, case_id), record in valid.items():
            if case_id == 'package-discovery' and record['status'] in ('pass', 'reduced-pass'):
                discovery[host].update(op['operation'] for op in record['successfulOperations'])
        for case_id, entry in entries.items():
            if entry['structuralOnly']:
                continue
            for host in entry['requiredHosts']:
                record = valid.get((host, case_id))
                if not record or record['status'] not in ('pass', 'reduced-pass', 'blocked'):
                    errors.append(f'{host}: required case lacks validated result: {case_id}')
        for host in HOSTS:
            for status in STATUSES:
                report['byHost'][host][status] = sum(h == host and r['status'] == status for (h,_),r in valid.items())
            report['byHost'][host]['packageDiscovery'] = DISCOVERY <= discovery[host]
            if not DISCOVERY <= discovery[host]:
                errors.append(f'{host}: actual package discovery and invocation missing')
            report['byHost'][host]['validatedCases'] = sum(h == host for h, _ in valid)
        report['workflowCoverage']['observedSourceFiles'] = len({
            p for r in valid.values() if r['status'] in ('pass', 'reduced-pass') for p in r['sourcePaths']})
        report['workflowCoverage']['fullObservedSourceFiles'] = len({
            p for r in valid.values() if r['status'] == 'pass' for p in r['sourcePaths']})
        for row in inventory:
            for host in HOSTS:
                verification = row['verification'][host]
                linked = [r for (h, _), r in valid.items() if h == host and row['upstreamPath'] in r['sourcePaths'] and evidence_files[id(r)] in verification['evidence']]
                if not linked or not any(r['status'] == verification['status'] for r in linked):
                    errors.append(f'{host}: source verification lacks matching linked evidence: {row["upstreamPath"]}')
                for link in verification['evidence']:
                    if not any(evidence_files[id(r)] == link for r in linked):
                        errors.append(f'{host}: invalid source evidence link: {link}')
        if not errors:
            report['reportCommit'] = identity_checks(root, commit, version, inventory)
        report['testedCommit'] = commit
        report['packageVersion'] = version
    except (OSError, ValueError, KeyError, TypeError, AttributeError, subprocess.CalledProcessError) as exc:
        report['blockers'].append(f'root validation failed: {exc}')
    report['releasable'] = not report['blockers']
    report['validationRequired'] = bool(report['blockers'])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--version', required=True)
    args = parser.parse_args()
    report = assess_release(args.root, args.commit, args.version)
    print(json.dumps(report, indent=2))
    return 0 if report['releasable'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
