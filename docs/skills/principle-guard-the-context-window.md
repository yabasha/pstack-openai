# principle-guard-the-context-window

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-guard-the-context-window.json](../catalog/skills/principle-guard-the-context-window.json).

Skill: [skills/principle-guard-the-context-window/SKILL.md](../../skills/principle-guard-the-context-window/SKILL.md). Kind: principle.

## Purpose

Protect the finite context window by isolating large payloads, keeping frequently used content inline and bounding phases.

## Triggers

- Large outputs or long files
- Repeated reads
- Fan-out planning or a filling context window

## Required input

- Authorized task and accessible evidence
- Current evidence-access and independent-worker capabilities
- Phase scope and turn budgets

## Output contract

- Summaries in the main thread and bounded evidence phases
- Observed delegation results or explicit reduced and blocked limits

## Ordinary example

For a large repository corpus, assign authorized workers bounded document groups and inspect their summaries. Without workers, read narrower groups sequentially and label reduced capability.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [large-corpus](../parity/cases/skills/principle-guard-the-context-window.json)

Apply principle-guard-the-context-window to an accessible large corpus with verbose command output, screenshots and long documents. Keep the main thread useful, plan bounded phases and use independent workers only when authorized and available. Report unavailable access or delegation honestly.

Full capability expectation:

Use authorized independent workers with observed identities and inspected results to summarize bulky accessible evidence. Keep summaries in the main thread, frequently used content inline and phases bounded by file limits, turn budgets and mechanism costs.

Reduced capability expectation:

When independent workers are unavailable or unauthorized but evidence is readable, label reduced capability, narrow the accessible corpus into bounded sequential phases and keep summaries in the main thread. State that no independent workers ran.

Blocked capability expectation:

When required evidence cannot be accessed, identify the missing material and access limits; do not claim to have inspected or summarized it. Provide only a provisional bounded plan.

Required observations:

- Isolate verbose outputs, screenshots and large documents; retain summaries in the main thread.
- Keep templates and references used on every invocation inline.
- Limit files per phase, set turn budgets and account for mechanism costs.
- Check current read and independent-worker capabilities and authorization before delegating; inspect actual worker results.
- If delegation is unavailable, narrow accessible evidence sequentially as reduced capability without inventing workers.

Forbidden claims:

- Workers exist or ran without observed authorized delegation.
- Sequential reading establishes independent-worker capability.
- Unread evidence was inspected or summarized.
- Case definitions or structural checks prove host behavior.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Independent workers require authorization, exposed operations, observed identities and inspected results.
- Sequential narrowing is reduced capability and does not prove independent workers.
- Inaccessible evidence prevents inspection claims.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/principle-guard-the-context-window/SKILL.md`

Destination: [skills/principle-guard-the-context-window/SKILL.md](../../skills/principle-guard-the-context-window/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `af0b9dd70b43628ce4a59a4d332e9d9ad055084e460f430e7a757495c627e81a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
