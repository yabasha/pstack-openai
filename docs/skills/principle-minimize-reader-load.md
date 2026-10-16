# principle-minimize-reader-load

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-minimize-reader-load.json](../catalog/skills/principle-minimize-reader-load.json).

Skill: [skills/principle-minimize-reader-load/SKILL.md](../../skills/principle-minimize-reader-load/SKILL.md). Kind: principle.

## Purpose

Reduce the layers readers trace and the hidden or mutable state they must hold to understand code.

## Triggers

- Reviewing or shaping code that is hard to trace
- Considering another layer or piece of state

## Required input

- Concrete source path, caller evidence and mutable state
- Authorized task and available session capabilities

## Output contract

- Simpler trace path and smaller state scope with meaningful boundaries and invariants preserved
- Source-grounded proposal and explicit missing checks when writes or execution are unavailable

## Ordinary example

Trace an invoice total through two one-caller pass-through wrappers, collapse them where they hide no decisions, and derive total from rows instead of synchronizing a cached module value.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [trace-load](../parity/cases/skills/principle-minimize-reader-load.json)

Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.

Full capability expectation:

Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.

Reduced capability expectation:

With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits.

Blocked capability expectation:

Without readable source or sufficient caller and state evidence, identify the missing access or evidence and stop concrete refactoring and completion claims.

Required observations:

- Read source and callers; writes and execution require available tools and authorization.
- Inspect both layers to trace and state to hold.
- Preserve meaningful abstraction boundaries and invariants.

Forbidden claims:

- A structural validator pass proves host behavior or a measured reader time.
- Fewer lines alone prove reduced reader load.
- All abstraction layers should be removed regardless of interface compression.
- Unavailable writes or execution succeeded.
- Preserved invocation metadata proves host enforcement.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/principle-guard-the-context-window/SKILL.md](../../skills/principle-guard-the-context-window/SKILL.md)

## Host limits

- Concrete refactoring requires inspected source and caller evidence plus authorized writes; verification requires observed execution.
- Missing writes or execution permit a reduced proposal; missing source or sufficient evidence blocks concrete refactoring claims.
- The under-30-second reader test is a criterion unless measured.
- Invocation metadata is preserved without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-minimize-reader-load/SKILL.md`

Destination: [skills/principle-minimize-reader-load/SKILL.md](../../skills/principle-minimize-reader-load/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `42551c5dc74cd578163c148da552db3ff67d29b78600ef216bfd311fb828fe69`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/preserved-behavior.json](../parity/evidence/chatgpt/preserved-behavior.json), [docs/parity/evidence/chatgpt/trace-load.json](../parity/evidence/chatgpt/trace-load.json).
- codex: `not-run`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/preserved-behavior.json](../parity/evidence/codex/preserved-behavior.json), [docs/parity/evidence/codex/trace-load.json](../parity/evidence/codex/trace-load.json).
