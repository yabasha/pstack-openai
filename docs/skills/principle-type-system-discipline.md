# principle-type-system-discipline

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-type-system-discipline.json](../catalog/skills/principle-type-system-discipline.json).

Skill: [skills/principle-type-system-discipline/SKILL.md](../../skills/principle-type-system-discipline/SKILL.md). Kind: principle.

## Purpose

Use types to exclude invalid states, distinguish semantic IDs and require complete handling of variants.

## Triggers

- Designing types
- Reviewing function signatures
- Writing code in a statically typed language

## Required input

- Authorized task, source model and invariants
- Language constraints and authoritative schemas

## Output contract

- Types and interfaces that exclude invalid states, with boundary parsers, exhaustive handling and observed compiler checks when available

## Ordinary example

Replace completed plus optional completedAt with open and done variants, where done carries its timestamp.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [invalid-state](../parity/cases/skills/principle-type-system-discipline.json)

Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.

Full capability expectation:

Replace contradictory optional fields with explicit open and done variants or one authoritative completion value. Construct constrained values, brand semantic IDs, parse external data at boundaries, avoid unsupported casts, require exhaustive handling, and derive types from owned schemas where available. Strengthen types where an operation is partial, keeping total sum on plain lists. Verify with the available compiler that an invalid state or missing variant fails, or identify the actual language limit and the remaining validation requirement.

Reduced capability expectation:

When source, writes, or compiler execution are unavailable, provide the proposed typed model and explain actual language limits. State which invalid states the construction excludes, which checks remain runtime checks, and which edits or compiler checks were not performed.

Blocked capability expectation:

If the relevant language or source cannot be established sufficiently to assess the invariant, report the missing inputs or denied capability and leave the result unverified.

Required observations:

- Inspect the model and relevant language/compiler constraints.
- Use authorized file access and compiler execution when available; do not install tools incidentally.

Forbidden claims:

- An unchecked cast proves validity.
- Every language can encode every invariant.
- A proposed type model or structural package check proves compiler rejection or host behavior.
- Unavailable writes or checks succeeded.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/typescript-best-practices/SKILL.md](../../skills/typescript-best-practices/SKILL.md)
- [skills/principle-boundary-discipline/SKILL.md](../../skills/principle-boundary-discipline/SKILL.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md)

## Host limits

- Some invariants require runtime validation because the language cannot encode them.
- Unavailable access, writes or compiler execution permit only a reduced proposal with unperformed checks stated.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-type-system-discipline/SKILL.md`

Destination: [skills/principle-type-system-discipline/SKILL.md](../../skills/principle-type-system-discipline/SKILL.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `5cdaf79785e3c12b2592b9469ee8c272143eb86ab7a18d8382197cea5fd30106`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
