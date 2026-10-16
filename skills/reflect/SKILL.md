---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

The parent discovers the active session through authorized exposed history or file tools. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment contract](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md). Record observed read, history, spawn, result inspection, execution and write bindings as applicable. Preserve the active controller.

Use only the transcript location supplied for this active workspace or an exposed active-chat reference. Verify its opening user prompt before use. Do not search unrelated workspace or user chat directories. If no active transcript resolves, write a tight session digest, mark its omissions, and pass that instead. If neither authorized history nor a usable digest exists, stop with blocked evidence-backed reflection.

### 2. Spawn three reviewers in parallel

When authorized independent workers are exposed, assign three reviewers in parallel under the assignment contract. Give each an immutable revision, role, separate output ownership and the complete corresponding template. Reviewers may read transcript-referenced context through available authorized tools but may not write code, edit skills, commit or send messages.

| Lens | Selection role | Prompt template |
| --- | --- | --- |
| Judgment | reflect judgment, divergent, synthesizer | [judgment reviewer](references/judgment-reviewer.md) |
| Tooling | reflect tooling | [tooling reviewer](references/tooling-reviewer.md) |
| Divergent | reflect judgment, divergent, synthesizer | [divergent reviewer](references/divergent-reviewer.md) |

Use the model-role contract for each selection role. Honor an explicitly supplied authorized role preference only when its model and effort are currently supported; otherwise retain inherit-parent and disclose the limit. Record requested and observed values separately. A rejected choice requires disclosed supported fallback or a block when the exact choice is required. Different role prompts do not establish model diversity.

Pass each template in full, substituting the transcript path or digest where marked. Inspect every worker result and its artifacts; a completion notification is insufficient. If independent workers are unavailable, perform the same three lens passes sequentially as reduced capability, followed by synthesis. Do not claim independent review.

### 3. Synthesize

Assign an independent synthesizer under the same capability, model-role and assignment contracts when available. Give it the [synthesizer template](references/synthesizer.md) in full with each reviewer's full output inlined where marked. Its spot-verification uses only authorized transcript-referenced context reads. Inspect its result. In the reduced sequential branch, apply the same synthesis prompt after all three lens passes. The synthesizer returns a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. See the [encode lessons in structure principle](../principle-encode-lessons-in-structure/SKILL.md).

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect future agents that load the changed skill. Do not auto-apply.

File Backlog items to the team devex tracker only when the user has explicitly authorized that tracker write and the exposed tool permits it. Otherwise provide an unfiled Backlog draft and state the limit. Backlog filing never authorizes Accepted edits.

For each approved Accepted item, follow the Routing field exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to an available authorized skill-authoring workflow and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to that skill-authoring workflow and run its description-optimization loop.
- `new skill via create-skill: <kebab-name>`: hand creation to that skill-authoring workflow. Do not invent the shape ad hoc.

If a required authoring workflow is unavailable, keep the approved proposal as a draft and report application blocked. Do not claim its draft / test / iterate or description-optimization loop ran.

If your environment ships an authorized SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
