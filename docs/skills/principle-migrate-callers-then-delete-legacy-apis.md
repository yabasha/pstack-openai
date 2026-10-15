# principle-migrate-callers-then-delete-legacy-apis

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-migrate-callers-then-delete-legacy-apis.json](../catalog/skills/principle-migrate-callers-then-delete-legacy-apis.json).

Skill: [skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md). Kind: principle.

## Purpose

Migrate internal callers and delete the old API in the same refactor wave.

## Triggers

- Introducing a new internal API while old callers still exist

## Required input

- Agreed new contract, source and caller usage evidence
- Confirmed applicability and authorized task

## Output contract

- Coordinated caller migration, legacy API removal and updated contract tests
- Reduced proposal or explicit block when required capabilities or evidence are missing

## Ordinary example

Inventory callers of an internal request API, move them to the new contract, update contract tests and delete the old API in one reviewed unit.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [caller-migration](../parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json)

Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.

Full capability expectation:

Inventory all callers, migrate every caller and remove the old API in the same reviewed refactor unit. Update tests to assert the new contract and delete tests protecting only obsolete implementation details. Use temporary adapters only as exceptional time-boxed measures. Confirm applicability and report observed checks.

Reduced capability expectation:

With source available but writes or execution unavailable, provide a coordinated caller migration and API deletion proposal as reduced capability. State which changes and checks were not performed.

Blocked capability expectation:

If source or caller evidence is missing, or external compatibility or coordinated breaking-change requirements are unresolved, block claims that immediate deletion is safe or complete and identify the missing evidence or decision.

Required observations:

- Source and caller usage evidence
- No external compatibility requirement and coordinated breaking changes accepted
- Authorized writes for migration and deletion
- Execution for observed checks

Forbidden claims:

- Old API preserved solely because internal callers still exist
- Partial migration presented as completed caller migration
- Default permanent compatibility adapter
- Deletion claimed safe without checking external consumers and applicability
- Unperformed writes or checks claimed complete
- Structural validation claimed as host behavior or metadata enforcement

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Applies when no external users require backward compatibility, coordinated breaking changes are acceptable and the new API simplifies a refactor.
- Edits require authorization and writes; actual checks require execution.
- Unavailable writes or execution allow a reduced proposal; missing caller evidence or unresolved applicability blocks safe deletion claims.
- Invocation metadata is preserved without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md`

Destination: [skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `09978915a4a11990cf0a9a02d9c08cc59e0b7a04c5c24b83aa560fbe4146f75b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
