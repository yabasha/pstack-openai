# bro

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/bro.json](../catalog/skills/bro.json).

Skill: [skills/bro/SKILL.md](../../skills/bro/SKILL.md). Kind: skill.

## Purpose

Restate the previous assistant message in plain, coherent, concise language without jargon.

## Triggers

- User invokes bro to simplify the previous assistant message.

## Required input

- The actual previous assistant message.

## Output contract

- A simpler, concise restatement of that message.

## Ordinary example

After an explanation about concurrent writes, invoke bro to get the same point in plain language.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [plain-restate](../parity/cases/skills/bro.json)

Invoke bro.

Full capability expectation:

Restates the actual immediately preceding assistant message in plain, coherent, concise language without adding claims. For the seeded assistant turn, explains that changes should happen one at a time so writers do not overwrite each other.

Reduced capability expectation:

If only an excerpt of the previous message is available, restates that excerpt and names the context limit without claiming it is the complete message.

Blocked capability expectation:

If the previous assistant message is unavailable, says it cannot restate the message and requests the missing text without inventing its contents.

Required observations:

- Before invocation, seed this exact sentence as the immediately preceding ASSISTANT turn: We should serialize mutations to the shared state to prevent concurrent writers from clobbering each other.
- Preserve a conversation artifact identifying the seeded assistant turn and its exact text; do not substitute an assertion about prior text inside the user invocation.
- Access to the actual previous assistant message.
- User invocation of bro; preserve disable-model-invocation metadata.

Forbidden claims:

- New facts, advice, promises, or outcomes absent from the previous message.
- Claims that unavailable conversation history was read.
- Claims of host behavioral verification from structural validation.

## Dependencies

No dependencies declared in the reviewed record.

## Host limits

- Missing conversation history prevents faithful restatement; partial history limits restatement to the available text.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/bro/SKILL.md`

Destination: [skills/bro/SKILL.md](../../skills/bro/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `aa329d0ceeeecb6822a7174ad76bb07a7826a3c52ceb6a588dec4138815084bb`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
