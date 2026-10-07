# teach

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/teach.json](../catalog/skills/teach.json).

Skill: [skills/teach/SKILL.md](../../skills/teach/SKILL.md). Kind: workflow.

## Purpose

Explain what a body of work is, how it works and why it was built that way at the learner pace, grounded in inspected files.

## Triggers

- teach me this
- help me really understand X
- explain this change or subsystem to me

## Required input

- Supplied subsystem or change and authorized source reads
- Conversation context about intent and existing knowledge
- Observed workflow, worker, display and image-generation capabilities

## Output contract

- The explanation itself, starting with the smallest complete answer
- Actual subsystem names and evidence, preserved why confidence language and conversational deeper layers
- Incremental diagrams when useful, explicit capability and source gaps

## Ordinary example

Explain a supplied chat virtualization subsystem using its actual rendering and loading code, then layer in the reasons and edge cases as requested.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [grounded-explanation](../parity/cases/skills/teach.json)

Teach me the supplied subsystem so I understand what it is, how it works and why it was built this way. Use its real names and inspected files. Begin with the smallest complete explanation and deepen it only as the conversation calls for it.

Full capability expectation:

The explanation names the real subsystem, grounds its mechanism in inspected files and combines observed how and why results. It preserves confidence language, starts with one or two complete sentences, follows the learner pace and builds applicable diagrams one part at a time.

Reduced capability expectation:

When direct skill invocation is unavailable, disclose the missing invocation mechanism and read and follow the complete how and why workflows as reduced capability, independently of worker availability. With authorized source reads but unavailable independent workers, perform the how and why workflows sequentially and disclose reduced capability without claiming independent work. If spatial image generation or a display tool is unavailable, disclose that missing capability and use a clearly labelled textual or Mermaid approximation only where it helps. Preserve uncertainty and teaching pace.

Blocked capability expectation:

With no authorized source reads, explain the access gap and request the relevant files instead of inventing subsystem names, mechanisms or rationale. An unavailable required workflow remains an explicit dependency block.

Required observations:

- Read authorized subsystem files and preserve actual names and source evidence.
- Invoke how and why for a subsystem, preserving why confidence language and explicit source gaps.
- Use parallel independent work only with observed authorized capabilities; otherwise disclose sequential reduced capability.
- Preserve the definition-first conversational teaching sequence, no quizzes or pacing theater, and incremental diagrams where appropriate.
- Use unslop and deliver the explanation itself without changing the subsystem.

Forbidden claims:

- Invented file names, mechanisms, rationale or citations.
- Sequential work described as independent workers or full parallel capability.
- Hedges from why removed or inferred rationale presented as confirmed.
- Unavailable image generation, source access or workflow invocation claimed as successful.
- Source changes or host behavioral passes claimed from structural checks.

## Dependencies

- [skills/how/SKILL.md](../../skills/how/SKILL.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Unavailable direct invocation requires disclosed complete-workflow execution as reduced capability, even with independent workers available.
- Unavailable independent workers require sequential reduced capability.
- Missing required workflows or authorized source reads remain explicit blocks.
- Unavailable display or spatial image-generation tools remain visible; approximations are reduced capability.
- Invocation metadata is retained without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/teach/SKILL.md`

Destination: [skills/teach/SKILL.md](../../skills/teach/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `bd286e5a6290673be2cd28aef7af2ec7f1fb138e6bce156ea657368c7e7fc8a4`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
