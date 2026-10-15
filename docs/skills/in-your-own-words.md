# in-your-own-words

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/in-your-own-words.json](../catalog/skills/in-your-own-words.json).

Skill: [skills/in-your-own-words/SKILL.md](../../skills/in-your-own-words/SKILL.md). Kind: skill.

## Purpose

Restate the user goals and problem while keeping assumptions explicit.

## Triggers

- Explicit in-your-own-words invocation.

## Required input

- The current user request and authorized current-chat context.

## Output contract

- Restate the user goals and problem while keeping assumptions explicit.

## Ordinary example

Invoke in-your-own-words. User goal: diagnose why the overnight import duplicates invoices, using the supplied logs and a local fixture. No implementation is authorized yet.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [goal-restatement](../parity/cases/skills/in-your-own-words.json)

Invoke in-your-own-words. User goal: diagnose why the overnight import duplicates invoices, using the supplied logs and a local fixture. No implementation is authorized yet.

Full capability expectation:

Restate the user goals and problem while keeping assumptions explicit. The inspected response follows the complete skill contract and cites accessible evidence where needed.

Reduced capability expectation:

Use the supplied excerpt only and disclose any missing history, status read or outside verification.

Blocked capability expectation:

Identify the missing required input or operation without inventing intent, status or validation.

Required observations:

- Retain the actual supplied context, response and reviewer findings.
- Use only authorized context and available operations.
- Inspect the response against the complete skill contract and distinguish observations from assumptions.
- Restate the desired outcome and problem without starting implementation.
- Keep unproven causes and missing details explicit.

Forbidden claims:

- Invented history, status, intent or verification.
- External actions or unrelated history access without authorization.
- A source inspection presented as installed-host verification.

## Dependencies

No dependencies declared in the reviewed record.

## Host limits

- Missing required source or operations remain explicit gaps.
- Discovery and host behavior require fresh observed evidence.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/in-your-own-words/SKILL.md`

Destination: [skills/in-your-own-words/SKILL.md](../../skills/in-your-own-words/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `fa8ba74e27d7be371dc270ec78bbf816411477d0dfab185356c861ac8dd413ad`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
