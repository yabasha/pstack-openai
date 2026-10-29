# principle-model-the-domain

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-model-the-domain.json](../catalog/skills/principle-model-the-domain.json).

Skill: [skills/principle-model-the-domain/SKILL.md](../../skills/principle-model-the-domain/SKILL.md). Kind: principle.

## Purpose

Encode domain rules in concrete structures that remove invalid states, repeated assumptions and scattered branches.

## Triggers

- Writing stateful logic
- Branches or repeated shape assumptions spread across files
- Phase-named modules repeat domain rules

## Required input

- Authorized task and relevant source
- Domain invariants, transitions and access patterns

## Output contract

- Concrete domain structure and valid state transitions with explained invariants; implementation and observed checks when authorized and available

## Ordinary example

Replace queued, running and completed job booleans with states carrying worker IDs or results and explicit allowed transitions.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [state-shape](../parity/cases/skills/principle-model-the-domain.json)

A job has isQueued, isRunning and isComplete flags. Running jobs require a worker ID; complete jobs require a result. Retries and cancellation add more branches across phase-named modules. Apply principle-model-the-domain and express valid state transitions in a concrete domain structure.

Full capability expectation:

A concrete state machine, discriminated union or equivalent domain structure represents queued, running, completed and cancelled states with state-specific data and explicit permitted transitions. The response explains invariants, domain ownership and removed branches, implements within authorization when requested, and reports only observed checks.

Reduced capability expectation:

If writes or execution are unavailable, provide the concrete state structure and transition rules as a reduced design proposal. State that implementation and checks were not performed.

Blocked capability expectation:

If the state rules or source needed to determine valid transitions are missing, identify the missing inputs and label any provisional design; do not claim verified transitions.

Required observations:

- Read the supplied state rules and propose a concrete domain structure that encodes permitted transitions and state-specific data.
- Explain which invalid combinations and duplicated lifecycle checks the structure removes.
- Consider domain ownership rather than organizing repeated rules by execution phase; avoid abstraction that adds indirection without removing complexity.
- Use available source, authorized writes and observed execution for implementation claims.

Forbidden claims:

- Structural package validation proves behavioral parity.
- An unexecuted proposal proves invalid states cannot occur in the existing implementation.
- Metadata proves host enforcement of explicit invocation.
- Unavailable writes or execution succeeded.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing source or domain rules keep the design provisional.
- Unavailable writes or execution allow a reduced proposal with unperformed checks stated.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/principle-model-the-domain/SKILL.md`

Destination: [skills/principle-model-the-domain/SKILL.md](../../skills/principle-model-the-domain/SKILL.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `52c0d85e0c3827c41c18299b642657d7b47eaf77b7b31609e42e0df42b84c75f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
