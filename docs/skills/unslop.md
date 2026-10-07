# unslop

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/unslop.json](../catalog/skills/unslop.json).

Skill: [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md). Kind: skill.

## Purpose

Remove AI writing patterns while preserving meaning and intended tone.

## Triggers

- Invoke unslop to edit prose; the source description says it must always apply.

## Required input

- The actual text to rewrite.
- The complete numbered pattern list.

## Output contract

- Rewritten text that preserves meaning and intended tone.

## Ordinary example

Rewrite a supplied paragraph to remove chatbot praise, filler, jargon, and unnecessary passive voice without adding facts.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [prose-rewrite](../parity/cases/skills/unslop.json)

Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.

Full capability expectation:

Return plain prose that removes chatbot praise, fancy substitutes for is, superficial -ing phrases, AI vocabulary, contrast framing, filler, jargon, and unnecessary passive voice while retaining supported meaning. Apply all applicable numbered rules through 33, including dense sentences, adverbs, mannered prose, and over-compression.

Reduced capability expectation:

If only part of the draft is accessible, rewrite that part and state the scope limit. Lack of file-write permission still permits an in-chat rewrite; do not claim a saved edit.

Blocked capability expectation:

If the draft is absent or unreadable, request the actual text and do not invent a rewrite or claim completion.

Required observations:

- Access to the supplied draft and the complete unslop pattern list.
- Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.
- Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes.

Forbidden claims:

- New facts, invented citations, measured deltas, or mechanisms absent from the draft.
- A file was edited without an observed authorized write.
- Host enforcement of disable-model-invocation or host behavioral parity based on structural checks.

## Dependencies

No dependencies declared in the reviewed record.

## Host limits

- Missing text prevents a faithful rewrite; partial access limits scope.
- Saving edits requires available file tools and user authorization; an in-chat rewrite needs no file tools.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/unslop/SKILL.md`

Destination: [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `195411d320b5b328f9f642baf59757ed19aaf0931c0838740e0aca273d538dc1`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
