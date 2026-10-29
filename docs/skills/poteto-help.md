# poteto-help

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/poteto-help.json](../catalog/skills/poteto-help.json).

Skill: [skills/poteto-help/SKILL.md](../../skills/poteto-help/SKILL.md). Kind: skill.

## Purpose

Answer pstack setup and workflow questions with one usable prompt and its source.

## Triggers

- /poteto-help
- A question about pstack setup, skills, playbooks, principles or run recovery

## Required input

- User question and conversation context
- Selected local route and observed host capabilities

## Output contract

- Direct answer
- At most one example prompt and a source link
- Explicit missing or pending capability and dependency limits

## Ordinary example

For a question about reproducing an app bug, read the Bug fix playbook, provide its reproduction and verification recipe, and disclose missing app verification support without starting work.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [route-recipe](../parity/cases/skills/poteto-help.json)

Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.

Full capability expectation:

Route to the existing reviewed Bug fix playbook under poteto-mode, provide one reproduction-and-verification recipe and a source link, and do not start a help-only run.

Reduced capability expectation:

When app verification is unavailable, offer only the checks actually supported, label the reduction, and do not promise a video or independent workers. If the playbook is pending, identify its source route as pending rather than claim an existing port.

Blocked capability expectation:

When the selected local playbook cannot be read, report that routing cannot yet establish an existing ported recipe. Give the pinned source reference and explain the missing local dependency without starting work.

Required observations:

- Read the selected local leaf and Bug fix playbook before recommending their details.
- Provide at most one concrete prompt, the source link, and the relevant verification requirement.
- Check whether the referenced playbook and app verification tool exist; disclose pending or missing dependencies.
- For any customization follow-up, explain source options but gate personal-mode drafting and custom skill edits on reviewed dispositions for the complete baseline and observed supported behavior or explicit blocks for each host, independently of authorization.

Forbidden claims:

- A recipe proves host behavior passed.
- Cursor modes, slash commands, model rules or loop APIs are registered on this host.
- Missing local playbooks are existing reviewed ports.
- A help question authorizes execution, installation, external writes or scheduling.
- User authorization alone permits personal customization before complete baseline review and per-host evidence or explicit blocks.

## Dependencies

- [skills/poteto-mode/SKILL.md](../../skills/poteto-mode/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [skills/setup-pstack/SKILL.md](../../skills/setup-pstack/SKILL.md)
- [README.md](../../README.md)
- [docs/guide/01-setup.md](../guide/01-setup.md)
- [skills/poteto-help/references/prompting.md](../../skills/poteto-help/references/prompting.md)
- [docs/guide/02-poteto-mode.md](../guide/02-poteto-mode.md)
- [references/agent-prompts/poteto-agent.md](../../references/agent-prompts/poteto-agent.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/how/SKILL.md](../../skills/how/SKILL.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/teach/SKILL.md](../../skills/teach/SKILL.md)
- [skills/recall/SKILL.md](../../skills/recall/SKILL.md)
- [skills/blast-radius/SKILL.md](../../skills/blast-radius/SKILL.md)
- [skills/architect/SKILL.md](../../skills/architect/SKILL.md)
- [skills/arena/SKILL.md](../../skills/arena/SKILL.md)
- [skills/swarm/SKILL.md](../../skills/swarm/SKILL.md)
- [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md)
- [skills/tdd/SKILL.md](../../skills/tdd/SKILL.md)
- [skills/typescript-best-practices/SKILL.md](../../skills/typescript-best-practices/SKILL.md)
- [skills/no-comments/SKILL.md](../../skills/no-comments/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [skills/technical-writing/SKILL.md](../../skills/technical-writing/SKILL.md)
- [skills/bro/SKILL.md](../../skills/bro/SKILL.md)
- [skills/create-verification-skill/SKILL.md](../../skills/create-verification-skill/SKILL.md)
- [skills/maintain-verification-skill/SKILL.md](../../skills/maintain-verification-skill/SKILL.md)
- [skills/benchmark-checklist/SKILL.md](../../skills/benchmark-checklist/SKILL.md)
- [skills/figure-it-out/SKILL.md](../../skills/figure-it-out/SKILL.md)
- [skills/show-me-your-work/SKILL.md](../../skills/show-me-your-work/SKILL.md)
- [skills/automate-me/SKILL.md](../../skills/automate-me/SKILL.md)
- [skills/reflect/SKILL.md](../../skills/reflect/SKILL.md)
- [skills/correct/SKILL.md](../../skills/correct/SKILL.md)
- [skills/make-bot-ui/SKILL.md](../../skills/make-bot-ui/SKILL.md)
- [docs/guide/06-verify-and-ship.md](../guide/06-verify-and-ship.md)
- [skills/poteto-mode/playbooks/multi-phase-plan.md](../../skills/poteto-mode/playbooks/multi-phase-plan.md)
- [docs/guide/08-principles.md](../guide/08-principles.md)
- [docs/guide/07-overnight.md](../guide/07-overnight.md)
- [docs/guide/10-recipes-and-pitfalls.md](../guide/10-recipes-and-pitfalls.md)
- [docs/guide/09-make-it-yours.md](../guide/09-make-it-yours.md)
- [skills/poteto-help/references/recipes.md](../../skills/poteto-help/references/recipes.md)

## Host limits

- Pending playbooks require final integration review.
- Cursor installation, modes, rule files and loop facilities do not register portable runtime behavior.
- Workers, model panels, history and proof require observed support.
- Help questions do not authorize execution.
- Both hosts remain not-run.
- Explain source customization options when asked, but do not act on personal-mode drafting or custom skill edits until every baseline inventory disposition is reviewed and each host has observed evidence for supported behavior or an explicit block. User authorization is a separate requirement and does not satisfy this baseline prerequisite.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/poteto-help/SKILL.md`

Destination: [skills/poteto-help/SKILL.md](../../skills/poteto-help/SKILL.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `768368881379d688c4e3bbdae55dd2d7874fde98a258324d3527de1bf09f9bd1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/poteto-help/references/prompting.md`

Destination: [skills/poteto-help/references/prompting.md](../../skills/poteto-help/references/prompting.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `463f450c44a60afd001a2f69fdf8a5dea174351f339369b12ec3c41515e564d3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/poteto-help/references/recipes.md`

Destination: [skills/poteto-help/references/recipes.md](../../skills/poteto-help/references/recipes.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5323aca73a39a3b607c2bb22cd33551fe893563dfd4b104df838da010e9fc702`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
