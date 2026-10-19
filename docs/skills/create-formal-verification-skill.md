# create-formal-verification-skill

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/create-formal-verification-skill.json](../catalog/skills/create-formal-verification-skill.json).

Skill: [skills/create-formal-verification-skill/SKILL.md](../../skills/create-formal-verification-skill/SKILL.md). Kind: skill.

## Purpose

Generate a bounded, reproducible property check and a project-local rerun skill.

## Triggers

- /create-formal-verification-skill
- verify a costly race or invariant

## Required input

- Actual covered source, repository history and current check results
- Observed host capabilities and authorized isolated execution

## Output contract

- Scoped check result, counterexample or explicit draft/blocker
- Covered-code record, tool and bounds, surviving evidence and truthful sync point

## Ordinary example

Verify a retry lease cannot have two owners, detect an isolated broken variant and report the bounds.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [formal-create-contract](../parity/cases/skills/create-formal-verification-skill.json)

Generate a project-local check for a retry lease that must never have two owners.

Full capability expectation:

Select a costly property, trace model steps to real code, state tool/version, bounds and exclusions, run the check, detect an isolated broken variant, restore and rerun, then follow the generated skill. Record only an actually checked committed sync point; report existing violations without weakening the property.

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
- [skills/maintain-formal-verification-skill/SKILL.md](../../skills/maintain-formal-verification-skill/SKILL.md)

## Host limits

- No execution means no observed proof; unavailable persistence or discovery remains explicit.
- Generated-input testing is not formal verification.
- Negative controls require owned isolation and verified cleanup.
- Tool installation, settings, product fixes and external actions require applicable authorization.
- Both host workflows remain not-run until separately observed.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/create-formal-verification-skill/SKILL.md`

Destination: [skills/create-formal-verification-skill/SKILL.md](../../skills/create-formal-verification-skill/SKILL.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `6c934cd15a9583533ff9b7a9cad62775d7e80402d26d3ba7f74f79ea21a1d8eb`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
