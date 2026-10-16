# typescript-best-practices

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/typescript-best-practices.json](../catalog/skills/typescript-best-practices.json).

Skill: [skills/typescript-best-practices/SKILL.md](../../skills/typescript-best-practices/SKILL.md). Kind: skill.

## Purpose

Apply the canonical concrete TypeScript typing, boundary validation, testing and telemetry practices when reading or editing TypeScript.

## Triggers

- /typescript-best-practices
- Reading or editing any .ts or .tsx file.

## Required input

- Provided TypeScript or readable repository files.
- Existing runtime schemas and generated types.
- The type-system-discipline and boundary-discipline principles, and the complete patterns reference.

## Output contract

- A review or authorized refactor that applies the source rules and preserves total operations and hot-path exceptions.
- Observed check results, or explicit missing capabilities and unperformed checks.

## Ordinary example

Replace a JSON.parse cast and optional-field state bag with schema parsing and a kind-discriminated union; keep number[] for a total sum and strengthen a partial newest-session input.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [typed-boundary](../parity/cases/skills/typescript-best-practices.json)

Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: "dark", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === "object" && x !== null && "id" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.

Full capability expectation:

Use unknown at entry, UserSchema.parse or safeParse at the boundary and infer the domain type. Replace optional bags with a kind-discriminated union and use inline never exhaustiveness. Verify all guard claims or use existing schema validation. Use NonEmpty<Session> or a Session | undefined result for newest; keep number[] for total sum. Prefer satisfies for config and derive shapes with Pick/Omit/Parameters/ReturnType/Awaited/typeof. Preserve readonly __brand branding and validation before casts, constructive non-empty/pair/start-duration models, the narrowing hierarchy, isX/hasX naming, forward-compatible wire parsing, versioned persisted JSON with try/catch and no deep revalidation. Use object args except hot paths; real framework tests and running UI checks where available; structured diagnostics without shipped console.log. Retain and use the complete patterns reference; report observed check results only.

Reduced capability expectation:

If writes or execution are denied or unavailable, provide the refactor and explain which checks or saves remain unperformed. If a required principle or patterns reference is unavailable, identify the missing dependency and label the review partial. Do not install a schema library or invent repository definitions.

Blocked capability expectation:

If neither provided TypeScript nor repository input can be read, state the missing input and stop before claiming a review or refactor. Identify denied read access explicitly.

Required observations:

- Read the complete leaf, patterns reference, type-system-discipline principle and boundary-discipline principle.
- Apply the concrete rules to provided code; reuse existing schema validation and derive types rather than duplicating an interface or adding a dependency.
- Read repository symbols before saved edits and run available authorized checks; report unavailable checks.

Forbidden claims:

- Generic typing advice replacing concrete source practices or omitting patterns.md.
- Unchecked casts, a lying guard, any for external data, duplicate schema interfaces, or a new schema dependency for one guard.
- Unnecessary NonEmpty types for total operations or changed hot-path allocation exceptions.
- Claims of saved edits, compile/test/UI success, metadata enforcement, or host parity without observed evidence.

## Dependencies

- [skills/typescript-best-practices/references/patterns.md](../../skills/typescript-best-practices/references/patterns.md)
- [skills/principle-type-system-discipline/SKILL.md](../../skills/principle-type-system-discipline/SKILL.md)
- [skills/principle-boundary-discipline/SKILL.md](../../skills/principle-boundary-discipline/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing input blocks review; missing principle or patterns reference makes it partial.
- Denied or unavailable writes allow an unsaved proposed refactor.
- Compiler, test and UI results require observed execution; no dependency installation is implicit.
- Preserve paths and disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/typescript-best-practices/SKILL.md`

Destination: [skills/typescript-best-practices/SKILL.md](../../skills/typescript-best-practices/SKILL.md).

Upstream commit: `99743e9c151c8537cbbf1f98bb38f34ef3368453`. SHA-256: `28f9e61710e205f6f3c5476f333483cff0e988f6a5b639e2faad536344b40c5e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/typescript-best-practices/references/patterns.md`

Destination: [skills/typescript-best-practices/references/patterns.md](../../skills/typescript-best-practices/references/patterns.md).

Upstream commit: `99743e9c151c8537cbbf1f98bb38f34ef3368453`. SHA-256: `faa1362055374452efccac1b629677c61acfb0bcc6c4e3311836b5715638ee18`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
