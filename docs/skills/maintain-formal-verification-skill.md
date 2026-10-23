# maintain-formal-verification-skill

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/maintain-formal-verification-skill.json](../catalog/skills/maintain-formal-verification-skill.json).

Skill: [skills/maintain-formal-verification-skill/SKILL.md](../../skills/maintain-formal-verification-skill/SKILL.md). Kind: skill.

## Purpose

Keep a property check aligned with covered code and distinguish stale verification from product bugs.

## Triggers

- /maintain-formal-verification-skill
- covered code changed since its last verification sync

## Required input

- Actual covered source, repository history and current check results
- Observed host capabilities and authorized isolated execution

## Output contract

- Scoped check result, counterexample or explicit draft/blocker
- Covered-code record, tool and bounds, surviving evidence and truthful sync point

## Ordinary example

Inspect a newly added lease writer, update its model, replay the counterexample and report a product bug without changing the promise.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [formal-maintain-contract](../parity/cases/skills/maintain-formal-verification-skill.json)

Maintain a recorded lease invariant check after a new writer splits an atomic operation; the old check passes.

Full capability expectation:

Run the old check, inspect every covered-code change including moved code and new writers, update the verification from code and intentional-change evidence, rerun and demonstrate a failing variant. Replay counterexamples, separate model drift from bugs, and update only completed-check sync points. Keep verification edits separate from product fixes.

Reduced capability expectation:

With readable code but no execution, produce an authorized draft or read-only assessment; leave validation not-run and registration unverified. A generated-input fallback tests the real code and is explicitly testing, not formal proof.

Blocked capability expectation:

Missing reads, history, execution or safe mutation isolation blocks the dependent step. Do not overwrite user changes, install tools, weaken properties or advance a blocked sync point.

Required observations:

- Observed repository reads, history and authorized isolated writes
- Execution of a bounded check and a deliberate failing variant
- Verified project-local discovery and surviving artifacts
- No verifier installation or product fixes without applicable authorization

Forbidden claims:

- A model pass proves the whole system
- Generated-input testing is formal proof
- An unrun recipe is verified or discovered
- A timeout or cancellation is a pass
- An uncommitted checkout is fully described by HEAD alone
- The skill authorizes product fixes, installations, publication or schedules

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/create-formal-verification-skill/SKILL.md](../../skills/create-formal-verification-skill/SKILL.md)

## Host limits

- No execution means no observed proof; unavailable persistence or discovery remains explicit.
- Generated-input testing is not formal verification.
- Negative controls require owned isolation and verified cleanup.
- Tool installation, settings, product fixes and external actions require applicable authorization.
- Both host workflows remain not-run until separately observed.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/maintain-formal-verification-skill/SKILL.md`

Destination: [skills/maintain-formal-verification-skill/SKILL.md](../../skills/maintain-formal-verification-skill/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `0c96f54293542d3818b68754562b338073958781a9684454611dca37592e2d2c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
