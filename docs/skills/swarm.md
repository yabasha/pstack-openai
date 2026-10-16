# swarm

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/swarm.json](../catalog/skills/swarm.json).

Skill: [skills/swarm/SKILL.md](../../skills/swarm/SKILL.md). Kind: workflow.

## Purpose

Fan out N workers over slices, identical race briefs or a mixture, then return one evidenced report.

## Triggers

- /swarm
- swarm this
- Parallel coverage
- Races
- Gauntlets
- Exploration

## Required input

- Done predicate, required artifacts, N and partition slices or race arms
- Exact full revisions, measurement method, race selection rule and authorized outputs

## Output contract

- Consolidated in-chat result table and evidenced issue one-liners
- Explicit gaps, dropouts, race rule and capability limits

## Ordinary example

Use /swarm to cover separate repository slices at an exact commit; reject a result missing its sampling method, retry it once and report any remaining coverage gap.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [partition-and-race](../parity/cases/skills/swarm.json)

Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.

Full capability expectation:

Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.

Reduced capability expectation:

Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.

Blocked capability expectation:

Unavailable or denied worker execution blocks full swarm behavior. Missing exact required model, source revision, artifact access or permission blocks the affected assignment. An unobserved stop leaves termination unverified and partial artifacts excluded.

Required observations:

- Independent worker spawn, wait and result inspection when available and authorized
- Exact SHA and measurement method in assignment and result
- Distinct writable outputs and existing evidence artifacts
- Stop, terminal inspection and artifact quarantine for cancellation

Forbidden claims:

- Sequential work proves independent workers or race parity
- Missing SHA, method, artifacts or coverage counts as PASS
- More than one retry for invalid SHA or method evidence
- Requested models prove actual models or diversity
- Cancellation notification proves termination without terminal inspection
- Unapproved external action or cloud setup is authorized by swarm

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Full behavior needs authorized independent spawn, wait and result inspection
- Sequential fallback is reduced capability and does not establish race parity
- Cloud/background execution, base-branch selection and exact models require observed host support
- Cancellation requires observed stop, terminal inspection and artifact quarantine
- Missing persistence leaves recovery unverified
- Host behavior remains not-run

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/swarm/SKILL.md`

Destination: [skills/swarm/SKILL.md](../../skills/swarm/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `bdcee4168e22428036e93d7cdeec3f391dbc4132f927f6db2540328c22db0273`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
