# recall

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/recall.json](../catalog/skills/recall.json).

Skill: [skills/recall/SKILL.md](../../skills/recall/SKILL.md). Kind: workflow.

## Purpose

Reconstruct scoped recent working context from history, shared records and independently checked live state.

## Triggers

- recall my work on X
- catch me up
- what have I been working on
- where did I leave off
- before starting or resuming work

## Required input

- Topic, workspace and exact time range
- Complete or partial supplied capsule
- Authorized history, shared sources and current-state reads

## Output contract

- Capsule with at most five bullets
- Every evidenced thread with one permitted status tag
- At most five recurring problems and one concrete next action
- Cited history and shared records with explicit access gaps

## Ordinary example

Recall seven days of cache work in the active workspace, use a complete supplied capsule first, sweep prior incidents and verify the current branch and PR state.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [scoped-history](../parity/cases/skills/recall.json)

Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.

Full capability expectation:

State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.

Reduced capability expectation:

When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.

Blocked capability expectation:

Denied or unavailable required history, shared source or live reads block the affected conclusion. Report gaps and what the supplied capsule supports, without claiming mined history, checked current state, independence or a completed thread. An unknown status cannot receive an invented done tag.

Required observations:

- Authorized scoped history and shared-record reads
- Independent workers for parallel mining when exposed and authorized
- Independent live file, git, PR and ticket state reads

Forbidden claims:

- A complete capsule proves current state or permits skipping a named-target shared-record sweep
- A partial capsule is complete
- Sequential passes are independent parallel workers
- Unavailable sources are searched-empty results
- Transcript UUID ordering proves recency
- History proves a PR remains open or merged today
- All history silently means recent N
- Other-workspace history access without authorization
- Requested models prove observed models
- Missing evidence warrants verified uncommitted or merged status

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [skills/poteto-mode/playbooks/session-pickup.md](../../skills/poteto-mode/playbooks/session-pickup.md)
- [skills/automate-me/SKILL.md](../../skills/automate-me/SKILL.md)

## Host limits

- History layout and UUID availability depend on observed host tools.
- Independent parallel mining requires authorized exposed workers; sequential passes are reduced capability.
- Unavailable live reads block affected status claims even with a complete capsule.
- session-pickup and automate-me are present and reviewed. Actual history access and baseline acceptance gates still apply.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/recall/SKILL.md`

Destination: [skills/recall/SKILL.md](../../skills/recall/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `d265b0e5b6dc5b89c0407f3387d24462c988e1990a37d5359735137908128c5a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
