# principle-build-the-lever

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-build-the-lever.json](../catalog/skills/principle-build-the-lever.json).

Skill: [skills/principle-build-the-lever/SKILL.md](../../skills/principle-build-the-lever/SKILL.md). Kind: principle.

## Purpose

Build the smallest rerunnable tool that performs or proves nontrivial work, making its result reviewable.

## Triggers

- Nontrivial edits, migrations, analyses or checks
- Explicit principle-build-the-lever invocation

## Required input

- Authorized task and source
- A hand-done first unit and its expected result
- Available write, execution and worker capabilities

## Output contract

- A safe rerunnable codemod, script, generator or shared delegate skill file
- Observed rerun and diff proof, or an explicit reduced proposal and blocked proof

## Ordinary example

Migrate one file by hand, build an idempotent codemod, and rerun it on that file to compare the result before applying it to the remaining files.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [repeatable-change](../parity/cases/skills/principle-build-the-lever.json)

Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.

Full capability expectation:

Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.

Reduced capability expectation:

When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.

Blocked capability expectation:

If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.

Required observations:

- Source reads; authorized artifact writes and execution for full proof.
- Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.

Forbidden claims:

- A proposed tool was saved, run or verified without observed evidence.
- Hand-applied changes alone satisfy the principle.
- Sequential work proves independent workers.
- Invocation grants commit, delegation or external-action permission.

## Dependencies

- [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md)
- [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)

## Host limits

- Writes and commits require authorization; proof requires observed execution and comparisons.
- Delegation requires authorization and exposed independent workers; deterministic tools take priority.
- No host behavior has been tested.
- Preserve disable-model-invocation metadata without assuming host enforcement.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-build-the-lever/SKILL.md`

Destination: [skills/principle-build-the-lever/SKILL.md](../../skills/principle-build-the-lever/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `3434b0ad0c640c6f1d7960be7a8986c3bcdc14e26060360dec29903df60074ff`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
