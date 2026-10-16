# principle-redesign-from-first-principles

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-redesign-from-first-principles.json](../catalog/skills/principle-redesign-from-first-principles.json).

Skill: [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md). Kind: principle.

## Purpose

Integrate a requirement by redesigning the affected structure as if the requirement had been present from the start, preserving option value.

## Triggers

- Integrating a new requirement into an existing design

## Required input

- Authorized task and new requirement
- All affected source files and current design context

## Output contract

- A redesign propagated through types, docs, examples and rationale, delivered incrementally
- Observed edits and checks, or an explicit reduced or provisional proposal

## Ordinary example

When adding tenant ownership, rethink the data model and access paths with ownership as a foundational assumption, update references, and deliver coherent increments.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [new-requirement](../parity/cases/skills/principle-redesign-from-first-principles.json)

Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.

Full capability expectation:

Read all affected files, compare the design with a fresh design that assumes tenant ownership, redesign the affected structure instead of stacking a workaround, propagate the change through types, docs, examples and rationale, and deliver the whole redesign incrementally. Report only observed edits and checks.

Reduced capability expectation:

With source available but writes or execution unavailable, provide a concrete redesign and incremental sequence as reduced capability. Identify unperformed edits and checks and preserve authorization boundaries.

Blocked capability expectation:

If affected source or required design context is unavailable, identify the missing inputs and keep any redesign provisional. Do not claim the current design was inspected or changed.

Required observations:

- Available affected source and current design
- Authorized scope and available read capability
- Write and execution capabilities for implementation and checks

Forbidden claims:

- A workaround stacked onto existing structure satisfies the redesign
- Implementation or checks occurred without observed authorized operations
- Source review or structural checks prove host behavioral parity
- Unavailable source was inspected
- The principle grants broader write or external permissions

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Inspection requires available source; edits require authorization and writes; checks require observed execution.
- Unavailable writes or execution permit a reduced design proposal; missing design context keeps proposals provisional.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-redesign-from-first-principles/SKILL.md`

Destination: [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `a1c7fd0a96b40e12a74bceb0e6bb20a9666dd844dcabfb624acb27da23b929fe`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: [docs/parity/evidence/chatgpt/new-requirement.json](../parity/evidence/chatgpt/new-requirement.json), [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/preserved-behavior.json](../parity/evidence/chatgpt/preserved-behavior.json).
- codex: `not-run`. Tested release evidence: [docs/parity/evidence/codex/new-requirement.json](../parity/evidence/codex/new-requirement.json), [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/preserved-behavior.json](../parity/evidence/codex/preserved-behavior.json).
