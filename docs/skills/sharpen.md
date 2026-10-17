# sharpen

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/sharpen.json](../catalog/skills/sharpen.json).

Skill: [skills/sharpen/SKILL.md](../../skills/sharpen/SKILL.md). Kind: skill.

## Purpose

Frame the task around its intended outcome, preserve user constraints and choose an outside verification.

## Triggers

- Explicit sharpen invocation.

## Required input

- The current user request and authorized current-chat context.

## Output contract

- Frame the task around its intended outcome, preserve user constraints and choose an outside verification.

## Ordinary example

Invoke sharpen on a task to diagnose slow search. The user requires an offline fixture and prohibits production data. Inspect the supplied fixture results and propose or run an authorized independent check.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [task-sharpen](../parity/cases/skills/sharpen.json)

Invoke sharpen on a task to diagnose slow search. The user requires an offline fixture and prohibits production data. Inspect the supplied fixture results and propose or run an authorized independent check.

Full capability expectation:

Frame the task around its intended outcome, preserve user constraints and choose an outside verification. The inspected response follows the complete skill contract and cites accessible evidence where needed.

Reduced capability expectation:

Use the supplied excerpt only and disclose any missing history, status read or outside verification.

Blocked capability expectation:

Identify the missing required input or operation without inventing intent, status or validation.

Required observations:

- Retain the actual supplied context, response and reviewer findings.
- Use only authorized context and available operations.
- Inspect the response against the complete skill contract and distinguish observations from assumptions.
- Preserve the offline fixture and production-data prohibition.
- Perform the authorized task rather than returning only a rewritten prompt; disclose an unavailable outside check.

Forbidden claims:

- Invented history, status, intent or verification.
- External actions or unrelated history access without authorization.
- A source inspection presented as installed-host verification.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing required source or operations remain explicit gaps.
- Discovery and host behavior require fresh observed evidence.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/sharpen/SKILL.md`

Destination: [skills/sharpen/SKILL.md](../../skills/sharpen/SKILL.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `6bcd73916696eb9c5b79b6f960983760c34bcc28937c11142dd8d86b5107aa46`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
