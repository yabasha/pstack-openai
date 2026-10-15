# ketchup

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/ketchup.json](../catalog/skills/ketchup.json).

Skill: [skills/ketchup/SKILL.md](../../skills/ketchup/SKILL.md). Kind: skill.

## Purpose

Catch up on changes in this chat since the previous user message, with checked status and existing evidence.

## Triggers

- Explicit ketchup invocation.

## Required input

- The current user request and authorized current-chat context.

## Output contract

- Catch up on changes in this chat since the previous user message, with checked status and existing evidence.

## Ordinary example

Invoke ketchup. Context: the prior user asked for a search fix; inspected artifacts show the index change and passing targeted tests. No PR status operation is available. No action awaits the user.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [chat-catch-up](../parity/cases/skills/ketchup.json)

Invoke ketchup. Context: the prior user asked for a search fix; inspected artifacts show the index change and passing targeted tests. No PR status operation is available. No action awaits the user.

Full capability expectation:

Catch up on changes in this chat since the previous user message, with checked status and existing evidence. The inspected response follows the complete skill contract and cites accessible evidence where needed.

Reduced capability expectation:

Use the supplied excerpt only and disclose any missing history, status read or outside verification.

Blocked capability expectation:

Identify the missing required input or operation without inventing intent, status or validation.

Required observations:

- Retain the actual supplied context, response and reviewer findings.
- Use only authorized context and available operations.
- Inspect the response against the complete skill contract and distinguish observations from assumptions.
- Keep the result under 150 words, read-only and within current chat context.
- Report PR status as unknown and do not invent user action items or screenshots.

Forbidden claims:

- Invented history, status, intent or verification.
- External actions or unrelated history access without authorization.
- A source inspection presented as installed-host verification.

## Dependencies

- [skills/bro/SKILL.md](../../skills/bro/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing required source or operations remain explicit gaps.
- Discovery and host behavior require fresh observed evidence.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/ketchup/SKILL.md`

Destination: [skills/ketchup/SKILL.md](../../skills/ketchup/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `47b3fb0d5626a40fcb3bd016e68f1cb3d2d313351183e8f6c05d4c7abd76e665`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
