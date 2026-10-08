"""Exact reviewed source membership. A policy declares scope, never readiness."""
import json
import re
from pathlib import Path

POLICY_PATH = 'docs/parity/baseline-policy.json'


def membership(inventory):
    paths = sorted(r['upstreamPath'] for r in inventory)
    roots = [p for p in paths if re.fullmatch(r'skills/[^/]+/SKILL\.md',p)]
    return dict(sourcePaths=paths, rootSkills=roots,
                principles=[p for p in roots if p.startswith('skills/principle-')],
                playbooks=[p for p in paths if re.fullmatch(r'skills/poteto-mode/playbooks/[^/]+\.md',p)],
                bennySkills=[p for p in paths if p.startswith('automations/benny/skills/') and p.endswith('/SKILL.md')])


def validate_policy(root, inventory):
    policy = json.loads((root / POLICY_PATH).read_text())
    expected = membership(inventory)
    pins = {r['upstreamCommit'] for r in inventory}
    if (set(policy) != {'schemaVersion','upstreamCommit','reviewRationale',*expected}
            or policy['schemaVersion'] != 1 or pins != {policy['upstreamCommit']}
            or not isinstance(policy['reviewRationale'], str) or not policy['reviewRationale'].strip()
            or any(policy[k] != v or len(v) != len(set(v)) for k,v in expected.items())):
        raise ValueError('Reviewed baseline policy differs from exact inventory membership')
    manifest = json.loads((root / f"docs/parity/upstream-manifests/{policy['upstreamCommit']}.json").read_text())
    sources = {r['upstreamPath']:(r['upstreamCommit'],r['upstreamSha256']) for r in manifest['files']}
    if (manifest['commit'] != policy['upstreamCommit'] or len(sources) != len(manifest['files'])
            or sources != {r['upstreamPath']:(r['upstreamCommit'],r['upstreamSha256']) for r in inventory}):
        raise ValueError('Reviewed baseline policy does not match source manifest identities')
    return dict(sourceFiles=len(expected['sourcePaths']),leafSkills=len(expected['rootSkills']),
                principles=len(expected['principles']),supportFiles=len(expected['sourcePaths'])-len(expected['rootSkills']),playbooks=len(expected['playbooks']))
