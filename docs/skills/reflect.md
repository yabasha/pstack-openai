# reflect

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/reflect.json](../catalog/skills/reflect.json).

Skill: [skills/reflect/SKILL.md](../../skills/reflect/SKILL.md). Kind: workflow.

## Purpose

Mine an active session for durable learnings and route them into explicitly approved skill edits.

## Triggers

- reflect
- /reflect

## Required input

- Authorized active transcript or limited session digest
- Invoked skills and referenced context
- Explicit approved Accepted subset

## Output contract

- Judgment, tooling and divergent findings
- Full Accepted, Rejected and Backlog synthesis
- Approved applied edits or blocked drafts with evidence

## Ordinary example

Reflect on a debugging session, reject already-covered advice, route enforceable checks to Backlog and show proposed skill edits for approval.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [approval-before-edit](../parity/cases/skills/reflect.json)

Reflect on this active session. Review the judgment, tooling and divergent lenses, synthesize all findings, and propose durable skill improvements. Show all Accepted, Rejected and Backlog items before editing. I have not approved any edits or tracker writes.

Full capability expectation:

Locate only the active transcript or disclose a digest fallback. Run three independent parallel reviewers with the complete judgment, tooling and divergent prompts, then an independent synthesizer with their full outputs. Preserve evidence, actual-use/missed-trigger routing, already-covered rejection and structural Backlog checks. Present the full Accepted/Rejected/Backlog result and wait for explicit subset approval before edits. File Backlog only with explicit tracker authorization. Use the approved authoring workflow for substantive changes and descriptions; verify any validator and written results before reporting.

Reduced capability expectation:

If independent workers are unavailable, disclose reduced capability and apply all three lenses and synthesis sequentially without claiming independence or model diversity. Use a limited digest when history is unavailable. Preserve full output and the explicit approval gate. Without an authoring workflow or tracker authorization, return drafts and unfiled Backlog with limits.

Blocked capability expectation:

Without usable authorized history or digest, block evidence-backed reflection. Denied reads block affected findings. Without explicit approval, apply no Accepted edit. Denied writes or unavailable required authoring/validation block the affected application and leave proposals reviewable.

Required observations:

- Authorized active-session history or an explicitly limited digest
- Independent reviewers and synthesizer with observed spawn and result inspection for full behavior
- Read access to referenced context and target skills
- Explicit user approval of the Accepted subset before skill changes
- Authorized writes and available authoring/validation workflow for approved substantive edits

Forbidden claims:

- Skill edits before explicit Accepted-subset approval
- Automatic tracker writes without explicit authorization
- Sequential role passes described as independent reviewers
- Reading unrelated workspace chats to locate the active transcript
- Requested models represented as observed models or guaranteed diversity
- Invented citations, applied edits, filed issues or host passes

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md)

## Host limits

- Independent parallel review requires observed authorized worker tools; sequential lenses are reduced capability.
- History gaps and unavailable context reads limit findings.
- Substantive edits and description tuning require an available authorized authoring workflow.
- Tracker writes require explicit authorization.
- Host behavior remains not-run.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/reflect/SKILL.md`

Destination: [skills/reflect/SKILL.md](../../skills/reflect/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `1f5a8c246cdee8251f8667d85bd5d97f6c2801f505843c26ddbd6c621632519b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/reflect/references/divergent-reviewer.md`

Destination: [skills/reflect/references/divergent-reviewer.md](../../skills/reflect/references/divergent-reviewer.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `f6030d88e20e906ef5e2d9ba44cb013ce610c49c2fe2ef74c377d32e0dc9e939`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/reflect/references/judgment-reviewer.md`

Destination: [skills/reflect/references/judgment-reviewer.md](../../skills/reflect/references/judgment-reviewer.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `38f917619fbf346062d643e0ad6b12fc952d58678dfcbbf42ffcf6d8b9c08307`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/reflect/references/synthesizer.md`

Destination: [skills/reflect/references/synthesizer.md](../../skills/reflect/references/synthesizer.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `6af816963de74d1a1aef4070273c1ff533d2072732e488e159ddc0b299fec3cd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/reflect/references/tooling-reviewer.md`

Destination: [skills/reflect/references/tooling-reviewer.md](../../skills/reflect/references/tooling-reviewer.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `f81b8697e7366fbbc18feba52c6e3253a101f751091364ebc4396a1d9b5753b4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
