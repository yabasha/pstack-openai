# show-me-your-work

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/show-me-your-work.json](../catalog/skills/show-me-your-work.json).

Skill: [skills/show-me-your-work/SKILL.md](../../skills/show-me-your-work/SKILL.md). Kind: skill.

## Purpose

Keep a reviewable local decision trail for long-running or unattended work.

## Triggers

- /show-me-your-work
- Autonomous or multi-phase runs
- Work reviewed after a human steps away

## Required input

- Decisions and evidence pointers
- Authorized local log path
- This run transcript and reviewer capabilities

## Output contract

- Append-only six-column TSV
- Transcript audit with superseding corrections
- Attention section with observed reviewer model and flags or explicit gaps

## Ordinary example

Record a verified checkpoint and a reverted decision, resolve their evidence, audit this run and request an independent different-family reviewer.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [decision-trail](../parity/cases/skills/show-me-your-work.json)

Keep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.

Full capability expectation:

Save and read back one canonical six-column TSV with sanitized single-line cells and formula-prefix protection. Preserve run start boundaries and append-only corrections. Resolve evidence, audit this run against its transcript, and obtain independent different-family review. End every trail-producing reply with Attention, observed reviewer model and row-specific flags or No flags. Exclude secrets and unobserved results.

Reduced capability expectation:

When history or different-family review is unavailable, preserve the local trail and report the precise audit or review gap in Attention. Sequential self-review is reduced capability and never substitutes for independent cross-model review. If durable writes are unavailable, provide an unsaved in-chat handoff only when authorized and disclose that no durable trail was saved.

Blocked capability expectation:

Denied persistence blocks a claimed saved trail. Missing helper blocks helper execution unless an authorized equivalent preserves sanitization. Missing transcript or observed different-family reviewer blocks the corresponding full audit or cross-model claim. Report denied or unavailable capabilities without invented success.

Required observations:

- Authorized local persistence and readback
- Accessible history for this run
- task 16 logging helper or equally safe TSV append
- Authorized independent reviewer with observed different model family for full review

Forbidden claims:

- Secrets or private unrelated transcripts in the trail
- Saved trail without write and readback
- Edited or deleted prior rows
- Independent cross-model review from self-review or unknown model family
- Tests green, completed work or evidence resolution without observation
- Commit, publication or external writes without explicit authorization

## Dependencies

- [skills/show-me-your-work/references/decision-log-template.tsv](../../skills/show-me-your-work/references/decision-log-template.tsv)
- [skills/show-me-your-work/scripts/log.sh](../../skills/show-me-your-work/scripts/log.sh)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- The logging helper is present and reviewed; authorized execution, local persistence and readback still require observed host capabilities.
- History, durable write and readback, and independent different-family review require observed authorized bindings.
- Sequential self-review does not satisfy cross-model review.
- No secrets or unsupported completion claims; commits and external actions need explicit authorization.
- Host behavior remains not-run; disable-model-invocation metadata does not prove host enforcement.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/show-me-your-work/SKILL.md`

Destination: [skills/show-me-your-work/SKILL.md](../../skills/show-me-your-work/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `bcff5f7f9fd23f92c12b251f9cd6b947e9485e1055cfacb6fdd9cae0789d7550`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/show-me-your-work/references/decision-log-template.tsv`

Destination: [skills/show-me-your-work/references/decision-log-template.tsv](../../skills/show-me-your-work/references/decision-log-template.tsv).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6779378006a2f5225e8c06deb84f1d913fb532041ebbb6e50d94600bfe3f4b76`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

### `skills/show-me-your-work/scripts/log.sh`

Destination: [skills/show-me-your-work/scripts/log.sh](../../skills/show-me-your-work/scripts/log.sh).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `a65a4bc5fb7cdeadbdb7b7ff1ca4682f4d9c42420942b2977cd17b46c4ac338e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
