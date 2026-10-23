# technical-writing

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/technical-writing.json](../catalog/skills/technical-writing.json).

Skill: [skills/technical-writing/SKILL.md](../../skills/technical-writing/SKILL.md). Kind: skill.

## Purpose

Write or review clear technical documents using Diátaxis, Google developer style, STE instruction rules, and Global English syntax.

## Triggers

- /technical-writing
- Writing or reviewing docs, RFCs, readmes, PR descriptions, or commit messages.

## Required input

- The actual document text and its intended purpose.
- Real codebase symbols, paths, flags, commands, and facts.
- The unslop skill.

## Output contract

- A document or review that preserves named symbols and facts, removes filler, and applies all four layers. PR descriptions and commit messages skip Diátaxis as the leaf requires.
- A proposed diff for any new abstract-metaphor offender and replacement; do not edit unslop.

## Ordinary example

Rewrite a how-to about budget.mjs and budget.json while keeping the lower-only --write rule and CI failure condition.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [dense-doc](../parity/cases/skills/technical-writing.json)

Rewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.

Full capability expectation:

Remove filler, retain every named symbol and condition, and keep a clear how-to purpose. Apply Diátaxis, reader-directed sentences, STE rules, Global English, and unslop. Provide the rewrite or authorized document edit; propose any new abstract-metaphor offender with a diff without editing unslop.

Reduced capability expectation:

If required source text is incomplete or unslop is unavailable, identify the missing input or dependency and label the review partial. Returning the requested supplied-text rewrite in conversation is full direct completion; a specifically requested saved edit still requires an observed authorized write.

Blocked capability expectation:

If no document text can be read or supplied, state the missing input and do not invent a rewrite or claim review completion.

Required observations:

- Read the supplied document and preserve its how-to purpose.
- Preserve budget.mjs, budget.json, --write, CI, the count condition, and the lower-only restriction.
- Apply all four layers and the unslop skill; do not invent facts.

Forbidden claims:

- Changing real symbol names or lower-only --write behavior.
- Claiming unslop was applied without reading it.
- Claiming edits were saved without observed authorized writes.
- Claiming host enforcement of disable-model-invocation metadata or host parity from structural validation.

## Dependencies

- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing document input blocks review; unavailable unslop makes the review partial.
- Unavailable or denied document writes allow a proposed rewrite in the conversation without a save claim.
- Saved or external changes require the relevant tools and authorization.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/technical-writing/SKILL.md`

Destination: [skills/technical-writing/SKILL.md](../../skills/technical-writing/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `61fe9c424a798ebf36ad94941f87be049cb8827bdf86d21474a0dde37b513c43`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
