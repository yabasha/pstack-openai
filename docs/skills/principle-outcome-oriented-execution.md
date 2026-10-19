# principle-outcome-oriented-execution

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-outcome-oriented-execution.json](../catalog/skills/principle-outcome-oriented-execution.json).

Skill: [skills/principle-outcome-oriented-execution/SKILL.md](../../skills/principle-outcome-oriented-execution/SKILL.md). Kind: principle.

## Purpose

Converge on the intended verifiable migration end state without retaining throwaway compatibility states.

## Triggers

- Planned rewrites and migrations with explicit phase boundaries

## Required input

- Named target architecture
- Migration phases and authorized scope
- Relevant source and available verification tools

## Output contract

- Migration with declared reversible breakage boundaries, checks for touched areas and full static and runtime verification at completion, or an explicit reduced plan

## Ordinary example

Migrate a module to the agreed interface in phases, declare temporary caller breakage, check touched code during migration and verify the completed target after removing temporary adapters.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [migration-end-state](../parity/cases/skills/principle-outcome-oriented-execution.json)

Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.

Full capability expectation:

Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.

Reduced capability expectation:

When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.

Blocked capability expectation:

If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.

Required observations:

- Named target architecture and explicit migration phase boundaries
- Available source inspection, authorized scoped writes and command execution for full implementation

Forbidden claims:

- Full verification without observed static and runtime checks
- Unplanned, unscoped or irreversible breakage is acceptable
- Throwaway compatibility states are the completed target
- Invocation metadata proves host enforcement

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Source inspection, authorized writes and observed execution are required for full implementation and verification.
- Missing writes or execution permit a reduced migration plan; missing source or target blocks grounded implementation.
- Preserved disable-model-invocation metadata does not prove host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-outcome-oriented-execution/SKILL.md`

Destination: [skills/principle-outcome-oriented-execution/SKILL.md](../../skills/principle-outcome-oriented-execution/SKILL.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `10eb91633aa570355ba4bb37088fcade2b22e498df7a58edc749e65bc5a78e2d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
