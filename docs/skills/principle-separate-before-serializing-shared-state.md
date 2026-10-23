# principle-separate-before-serializing-shared-state

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-separate-before-serializing-shared-state.json](../catalog/skills/principle-separate-before-serializing-shared-state.json).

Skill: [skills/principle-separate-before-serializing-shared-state/SKILL.md](../../skills/principle-separate-before-serializing-shared-state/SKILL.md). Kind: principle.

## Purpose

Eliminate shared mutable write targets before structurally serializing access to a required shared object.

## Triggers

- Concurrent actors might write to the same file, branch, key or state object

## Required input

- Concurrent actors and mutable write targets
- Ownership requirements and any real canonical-object invariant

## Output contract

- Distinct owned writable outputs merged at the read or reporting boundary
- Structural serialization when a shared write target is required

## Ordinary example

Give an indexer and a metrics worker separate state files instead of separate fields in one state.json; combine their independent facts when reading the report.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [two-writers](../parity/cases/skills/principle-separate-before-serializing-shared-state.json)

An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.

Full capability expectation:

Assign indexer-state.json and metrics-state.json to distinct writers before considering a lock. Explain why separate fields in one state.json still share mutation. If one canonical write target is a real invariant, use lockfiles, sequential phases, a single writer or atomic compare-and-swap. Observe authorized operations before claiming implementation.

Reduced capability expectation:

If concurrent workers or writes are unavailable, provide the isolated-output design and label any authorized sequential fallback reduced capability. State which execution and concurrency checks were not performed.

Blocked capability expectation:

If required writes or execution are denied or unavailable, block implementation and identify the missing capability or permission. Preserve the isolation-first recommendation.

Required observations:

- Identify the shared mutable target.
- Isolate writable output before considering locking.
- Merge independent facts only at the read or reporting boundary; serialize structurally only for a real single-object invariant.

Forbidden claims:

- Instructions or conventions prevent concurrent write races.
- Locking is the default before checking whether sharing is necessary.
- Different fields in one state.json are isolated write targets.
- A design or sequential fallback proves concurrent worker execution or race prevention.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Writes, worker dispatch and external actions require available capabilities and permission.
- Unavailable implementation leaves a design with unperformed checks stated.
- Sequential fallback is reduced capability and does not prove concurrent execution.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-separate-before-serializing-shared-state/SKILL.md`

Destination: [skills/principle-separate-before-serializing-shared-state/SKILL.md](../../skills/principle-separate-before-serializing-shared-state/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `05294b40448e927c5da1c7b6f5c6b9fed3744637e3833d2d948b9154a9dd00bb`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
