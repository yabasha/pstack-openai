# principle-laziness-protocol

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-laziness-protocol.json](../catalog/skills/principle-laziness-protocol.json).

Skill: [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md). Kind: principle.

## Purpose

Prefer deletion and the smallest change that preserves required behavior.

## Triggers

- Refactoring
- Evaluating diff size
- Considering abstractions, layers or signal threading

## Required input

- Authorized task
- Implementation and caller source
- Required behavior and public contracts

## Output contract

- Minimal refactor and observed checks, or explicit reduced proposal or blocked assessment

## Ordinary example

Remove a forwarding adapter that adds no behavior, preserving the service rounding and tax contract.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [smaller-solution](../parity/cases/skills/principle-laziness-protocol.json)

Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.

Full capability expectation:

Remove redundant forwarding layers where caller contracts permit, preserve required behavior, and report the smallest diff with observed verification. Apply the more-than-3-files-or-layers flattening test without treating a rich interface as a deep call chain.

Reduced capability expectation:

If writes or execution are unavailable, give a specific read-only deletion proposal based on available source. Label reduced capability and state which edits and checks were not performed.

Blocked capability expectation:

If relevant source cannot be read or supplied, state that the abstraction and behavior cannot be assessed; request the missing implementation and callers without claiming a refactor.

Required observations:

- Read the implementation and callers before choosing deletion.
- Preserve rounding, tax behavior and required public contracts.
- Prefer deletion, keep the call hierarchy flat, consolidate repeated decisions and minimize the diff.
- Question signal threading and remove tiny pass-throughs, representation leaks and duplicated choices.
- File read, authorized write and execution capabilities are needed to implement and verify the change.

Forbidden claims:

- Behavior preserved without relevant evidence.
- Edits or checks completed when unavailable or denied.
- New abstraction or signal threading justified only by elegance.
- Structural validation proves host behavioral parity.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Reads need available source; edits need authorized writes; execution claims need observed checks.
- No host behavior has been tested.
- Preserve disable-model-invocation metadata without assuming host enforcement.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/principle-laziness-protocol/SKILL.md`

Destination: [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `1be6e7a435f26a75a76eb848b9c3d611b9977d0f5822361753244da25ca3ca45`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
