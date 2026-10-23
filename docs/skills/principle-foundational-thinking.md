# principle-foundational-thinking

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-foundational-thinking.json](../catalog/skills/principle-foundational-thinking.json).

Skill: [skills/principle-foundational-thinking/SKILL.md](../../skills/principle-foundational-thinking/SKILL.md). Kind: principle.

## Purpose

Choose core data, access patterns and ownership before logic; sequence foundations so later work stays simple.

## Triggers

- Choosing core types and data structures before logic
- Sequencing infrastructure and feature work
- Considering state shared by concurrent actors

## Required input

- Authorized task and relevant source
- Required behavior and dominant access patterns
- Concurrent actors and state ownership

## Output contract

- Core data and ownership design, coherent work sequence, and actual implementation checks when authorized and available

## Ordinary example

Before building a job queue, define job state and worker ownership, trace claim and status queries, and isolate concurrently mutable state.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [shape-first](../parity/cases/skills/principle-foundational-thinking.json)

Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.

Full capability expectation:

Identify job identity, state and ownership before queue logic. Trace enqueue, claim, completion and state-list access patterns; choose structures for those paths and isolate concurrently mutable state. Remove dead code first, sequence useful infrastructure before features, and test behavior and edge cases. Report actual edits and checks.

Reduced capability expectation:

With supplied source but unavailable writes or execution, provide a concrete shape, ownership and sequencing proposal. Label reduced capability and list edits and checks not performed.

Blocked capability expectation:

If required source or access patterns are unavailable, state the missing inputs and stop implementation claims. Any provisional design must identify its assumptions.

Required observations:

- Identify core types, data shape, dominant access patterns and ownership before writing logic.
- Ask what happens when another actor modifies shared state concurrently; isolate state when the answer is not nothing.
- Remove dead code before foundations; sequence shared types, CI, linting and test infrastructure before features, and tests before fixes.
- Converge types and data models, prefer explicit code, avoid premature abstractions, and test behavior and edge cases.
- Keep increments coherent and commits small and single-purpose; do not distribute a capability as special-case caller coordination.
- Source inspection, authorized writes and observed execution are needed for implementation and verification.

Forbidden claims:

- Core data or ownership can be deferred until after logic.
- Shared mutable state is safe without considering concurrent actors.
- Edits, tests or commits completed without observed authorized operations.
- Structural validation proves host behavioral parity.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Source inspection requires available inputs; edits require authorization and writes; checks require observed execution.
- Unavailable writes or execution permit a reduced design proposal; missing source keeps designs provisional.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/principle-foundational-thinking/SKILL.md`

Destination: [skills/principle-foundational-thinking/SKILL.md](../../skills/principle-foundational-thinking/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `864b827e8199d946ce58beca0f89c4ed4099ed6e426fb698a3aaa45de2a9eea2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
