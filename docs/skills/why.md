# why

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/why.json](../catalog/skills/why.json).

Skill: [skills/why/SKILL.md](../../skills/why/SKILL.md). Kind: workflow.

## Purpose

Investigate historical motivation, design rationale, regressions, postmortems and data-backed thresholds with cited confidence tiers.

## Triggers

- why does X work this way
- why we picked Y
- Design rationale, regressions, postmortems or threshold origins

## Required input

- Question and code target
- Files, symbols, commits, PRs and ticket leads
- Available authorized source reads and worker capabilities

## Output contract

- The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don’t Know, Sources Consulted, Confidence Summary
- Seven-category coverage, exact queries, citations, contradictions and explicit gaps
- Preserve / Change / Avoid / Risk constraints when a code change is contemplated

## Ordinary example

Trace a retry threshold through git history, PR discussion, a linked ticket and release telemetry, separating stated rationale from correlation.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [history-evidence](../parity/cases/skills/why.json)

Why does this retry threshold exist? The code history records a change, a shared ticket states a customer constraint, telemetry correlates with the release, and chat is unavailable. Distinguish the evidence from inference.

Full capability expectation:

Independent category investigators return searched queries, citations, contradictions and gaps. The synthesizer spot-checks citations and reports the eight source-defined sections, distinguishing the historical change from the ticket's stated motivation and telemetry inference; unavailable chat is an explicit gap.

Reduced capability expectation:

Without independent workers, sequential category passes and synthesis are labelled reduced capability. With missing connectors or gh, available history is inspected and each inaccessible source is named without invented rationale or complete-coverage claims.

Blocked capability expectation:

If no authorized source or history reads are available, report the blocked investigation and exact access gaps rather than producing an evidence-backed rationale.

Required observations:

- Anchor files, symbols, commit history and PR or ticket leads before investigation.
- Discover all seven evidence categories; record missing connectors and denied history as gaps.
- Use category investigators and a citation-checking synthesizer when independent workers are available; disclose sequential reduced capability otherwise.
- Preserve Direct, Supported, Inferred, Speculative and Unknown tiers, contradictions, exact queries and source citations.
- Keep source history, shared-record evidence and inference distinct; preserve source-specific search and privacy limits.

Forbidden claims:

- Code mechanics alone prove author intent.
- Missing connectors returned no relevant records.
- Sequential passes are independent investigators.
- Requested models prove actual model selection.
- Telemetry correlation proves causation.
- Structural validation proves host behavior.
- Read permission authorizes external writes or private-content redistribution.

## Dependencies

- [skills/why/references/investigator-prompt.md](../../skills/why/references/investigator-prompt.md)
- [skills/why/references/epistemics.md](../../skills/why/references/epistemics.md)
- [skills/why/references/sources/incident-postmortem.md](../../skills/why/references/sources/incident-postmortem.md)
- [skills/why/references/sources/slack.md](../../skills/why/references/sources/slack.md)
- [skills/why/references/sources/datadog.md](../../skills/why/references/sources/datadog.md)
- [skills/why/references/sources/notion.md](../../skills/why/references/sources/notion.md)
- [skills/why/references/sources/databricks.md](../../skills/why/references/sources/databricks.md)
- [skills/why/references/sources/sentry.md](../../skills/why/references/sources/sentry.md)
- [skills/why/references/sources/linear.md](../../skills/why/references/sources/linear.md)
- [skills/why/references/sources/code-archaeology.md](../../skills/why/references/sources/code-archaeology.md)
- [skills/why/references/synthesizer-prompt.md](../../skills/why/references/synthesizer-prompt.md)
- [skills/why/references/source-playbook.md](../../skills/why/references/source-playbook.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Missing connectors and authenticated PR reads remain explicit gaps.
- Unavailable independent workers require disclosed sequential reduced capability.
- Read-only investigation preserves private-record visibility and requires separate authorization for external writes.
- Invocation metadata is preserved without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/why/references/investigator-prompt.md`

Destination: [skills/why/references/investigator-prompt.md](../../skills/why/references/investigator-prompt.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6892956a7ab0b5ee6c4babaf4f793703abe89b350ea7cb9463b4a56eea1c8266`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

### `skills/why/references/epistemics.md`

Destination: [skills/why/references/epistemics.md](../../skills/why/references/epistemics.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `fcc0f559c072832c869a5ada72434b4849320a637ae63c09e8ee14f7ad787059`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

### `skills/why/references/sources/incident-postmortem.md`

Destination: [skills/why/references/sources/incident-postmortem.md](../../skills/why/references/sources/incident-postmortem.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `a899470f05f86029630a13a2696491cc708ca7b56a6e822a69ff6e954d6ff8cf`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/slack.md`

Destination: [skills/why/references/sources/slack.md](../../skills/why/references/sources/slack.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `58fee61d024b3700b407e7acbed367944720ff05adfddb6954d36c88368f3ba7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/datadog.md`

Destination: [skills/why/references/sources/datadog.md](../../skills/why/references/sources/datadog.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `ebe9c07bac28e47757ee7f16fb93b0c01d427a08c501957d047f395a2f37b7e7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/notion.md`

Destination: [skills/why/references/sources/notion.md](../../skills/why/references/sources/notion.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `3bcfa695c49dfad4ac036d5d7181c12585f55ac04f1936198d16ab75a2788997`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/databricks.md`

Destination: [skills/why/references/sources/databricks.md](../../skills/why/references/sources/databricks.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `236ede7aab6454662a992db088a5393537a5233a4c26719c93188f9e174488f6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/sentry.md`

Destination: [skills/why/references/sources/sentry.md](../../skills/why/references/sources/sentry.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6f292bc4fb1548e956f95e1900b9481abf5134254419f1cd9edec95428c82d73`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/linear.md`

Destination: [skills/why/references/sources/linear.md](../../skills/why/references/sources/linear.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `01304e7f1badfcfb78babbb0edcadeb3cc8dd3f713793420cdff24ba190f907c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/sources/code-archaeology.md`

Destination: [skills/why/references/sources/code-archaeology.md](../../skills/why/references/sources/code-archaeology.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `8c14aa382f0de40829b2668d43e3f54814480bb93a486c9282ada4003f6b9dbd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/synthesizer-prompt.md`

Destination: [skills/why/references/synthesizer-prompt.md](../../skills/why/references/synthesizer-prompt.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `733a3e9cf897b1aca56aaddeae01a3832e4bfed024c2f602db2d1bf807d7a73b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/why/references/source-playbook.md`

Destination: [skills/why/references/source-playbook.md](../../skills/why/references/source-playbook.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `9ae9dcb9d09111c9facc68510331c5aba4aed9b1b057314ff1fc0e166ad3993a`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

### `skills/why/SKILL.md`

Destination: [skills/why/SKILL.md](../../skills/why/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `442215bf70e491d4d31bd200c197f2ec447445df38e074c40880fc4bf30a1f9e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
