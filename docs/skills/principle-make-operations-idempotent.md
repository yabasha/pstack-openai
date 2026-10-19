# principle-make-operations-idempotent

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-make-operations-idempotent.json](../catalog/skills/principle-make-operations-idempotent.json).

Skill: [skills/principle-make-operations-idempotent/SKILL.md](../../skills/principle-make-operations-idempotent/SKILL.md). Kind: principle.

## Purpose

Make repeated and interrupted operations converge to the correct state through reconciliation.

## Triggers

- Designing commands, lifecycle steps or processing loops amid crashes, restarts and retries

## Required input

- Authorized operation and its existing state
- Crash points, action identities and destination outcomes

## Output contract

- Convergent operation design and repeated-run or crash checks when authorized and available

## Ordinary example

After an interrupted payment job, inspect its action identity and destination outcome before authorized recovery with the same idempotency key.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [replay](../parity/cases/skills/principle-make-operations-idempotent.json)

An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.

Full capability expectation:

The retry converges to the same end state through reconciliation and a destination-appropriate idempotency mechanism. It adopts live sessions, removes stale artifacts by content equivalence, detects stale PID locks and regenerates fresh scheduling input. Completed external actions are recognized without blind replay; unknown outcomes block replay.

Reduced capability expectation:

Without destination inspection or authorized execution, provide a reduced recovery design and state which checks and actions were not performed. Unknown prior outcomes still block external replay.

Blocked capability expectation:

If action identity, destination outcome or external permission cannot be established, block replay and identify the missing requirement.

Required observations:

- Inspect the stable prior action identity and destination outcome before recovery.
- Preserve explicit authorization and observed capabilities for external writes.
- Exercise repeated runs and crashes at each possible point; reconcile partial state.

Forbidden claims:

- Blind external replay is safe because the local operation is idempotent.
- Unknown action outcomes count as completion.
- A proposed reconciliation design proves host execution or unattended recovery.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Unknown external outcomes or missing permission block replay.
- Unavailable inspection or execution permits a reduced design with unperformed checks stated.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-make-operations-idempotent/SKILL.md`

Destination: [skills/principle-make-operations-idempotent/SKILL.md](../../skills/principle-make-operations-idempotent/SKILL.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `7aa9327cf1f1aa057e95d47a0a78bd88a8f9d556b608866fee939d455a53a019`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
