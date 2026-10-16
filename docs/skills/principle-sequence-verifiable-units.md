# principle-sequence-verifiable-units

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-sequence-verifiable-units.json](../catalog/skills/principle-sequence-verifiable-units.json).

Skill: [skills/principle-sequence-verifiable-units/SKILL.md](../../skills/principle-sequence-verifiable-units/SKILL.md). Kind: principle.

## Purpose

Sequence work and delivery into small units that each end in a verified state.

## Triggers

- Multi-step sweeps, migrations and runs of similar edits
- Stacking commits and PRs

## Required input

- Authorized work and known-good baseline
- Per-unit changes, specific checks and delivery order

## Output contract

- Ordered units with checks before advancement
- Independently landable delivery sequence when authorized and verified

## Ordinary example

Migrate one schema boundary, run its concrete migration check, then begin the next unit only after green; deliver the failing test before its fix.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [migration-units](../parity/cases/skills/principle-sequence-verifiable-units.json)

Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.

Full capability expectation:

Inspect a clean trunk baseline and rebase when authorized. Every ordered migration unit identifies its known-good start, one change and concrete check; advance only on green. Delivery uses a failing test before its fix, or another justified order such as subtraction before reshape, baseline before treatment or scaffold before feature. Every commit lands on its own. Use the prove-it-works and build-the-lever principles to keep checks real and cheap.

Reduced capability expectation:

When execution or Git writes are unavailable or unauthorized, provide a reduced ordered migration and delivery plan with a concrete check per unit. State which checks and Git operations were not performed; do not treat an unrun check as green.

Blocked capability expectation:

Block advancement past a failed or unavailable required check and identify the missing capability or permission. Preserve the current unit for diagnosis.

Required observations:

- Each ordered unit ends in a specific check.
- Start from a known-good baseline and verify one change before the next.
- Order independently landable commits and PRs so a reviewer can replay the argument.
- Preserve authorization and observed execution limits.

Forbidden claims:

- An unrun or failed check is green.
- A batch check replaces verification of each unit.
- A delivery plan proves independently landable commits or actual host execution.
- The principle authorizes rebase, commit or PR writes without permission.

## Dependencies

- [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md)
- [skills/principle-build-the-lever/SKILL.md](../../skills/principle-build-the-lever/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Unavailable required execution blocks advancement and leaves the unit unverified.
- Rebase, commits and PR operations require authorization and observed capabilities.
- Reduced planning identifies unperformed checks and Git operations.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-sequence-verifiable-units/SKILL.md`

Destination: [skills/principle-sequence-verifiable-units/SKILL.md](../../skills/principle-sequence-verifiable-units/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `2ccbbacc56ace5afdfb8670cef19d7bd009fb2a0033b9a741cbdf2b6baf72187`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/bounded-improvement.json](../parity/evidence/chatgpt/bounded-improvement.json), [docs/parity/evidence/chatgpt/comparable-revisions.json](../parity/evidence/chatgpt/comparable-revisions.json), [docs/parity/evidence/chatgpt/migration-units.json](../parity/evidence/chatgpt/migration-units.json), [docs/parity/evidence/chatgpt/no-persistent-tool.json](../parity/evidence/chatgpt/no-persistent-tool.json), [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/preserved-behavior.json](../parity/evidence/chatgpt/preserved-behavior.json), [docs/parity/evidence/chatgpt/reproduce-before-fix.json](../parity/evidence/chatgpt/reproduce-before-fix.json), [docs/parity/evidence/chatgpt/units-and-proof.json](../parity/evidence/chatgpt/units-and-proof.json), [docs/parity/evidence/chatgpt/verifiable-feature.json](../parity/evidence/chatgpt/verifiable-feature.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/bounded-improvement.json](../parity/evidence/codex/bounded-improvement.json), [docs/parity/evidence/codex/comparable-revisions.json](../parity/evidence/codex/comparable-revisions.json), [docs/parity/evidence/codex/migration-units.json](../parity/evidence/codex/migration-units.json), [docs/parity/evidence/codex/no-persistent-tool.json](../parity/evidence/codex/no-persistent-tool.json), [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/preserved-behavior.json](../parity/evidence/codex/preserved-behavior.json), [docs/parity/evidence/codex/reproduce-before-fix.json](../parity/evidence/codex/reproduce-before-fix.json), [docs/parity/evidence/codex/units-and-proof.json](../parity/evidence/codex/units-and-proof.json), [docs/parity/evidence/codex/verifiable-feature.json](../parity/evidence/codex/verifiable-feature.json).
