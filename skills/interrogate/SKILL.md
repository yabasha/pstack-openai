---
name: interrogate
description: 'Use for "interrogate", "adversarial review", "multi-model review", "challenge this", "stress test this code", "find blind spots", or "tear this apart". Adversaries try to break a change; only findings proven by a rerun survive.'
disable-model-invocation: true
---

# Interrogate

Adversaries try to break a change or design. A verified finding requires a run against the real code and a lead rerun that demonstrates a failure of the stated intent. Report findings, never apply fixes.

## Frame

Read [session capabilities](../../references/host-capabilities.md), [model selection](../../references/model-roles.md), [assignment contract](../../references/orchestration-contract.md), and [Arena](../arena/SKILL.md). Use the scope the user names. Otherwise inspect the branch diff from its merge base through the working tree, including scoped untracked files. State the intent in your own words. Resolve uncertainty that affects the review before claiming a grounded result.

## Isolate and dispatch

Use Arena's framing, runner selection and isolated output ownership, substituting authorized interrogate reviewer preferences. Every adversary receives the identical scope, intent and reproduction brief. Do not perform Arena's judging, base selection or grafting. Different adversaries can find different failures, and every verified failure belongs in the result.

Before dispatch, identify the exact base revision and capture the scoped staged, unstaged and untracked changes without resetting, stashing or editing the user's checkout. Record the snapshot's files and hashes. Copy that reviewed scope into each task-owned isolated writable worktree or equivalent supported isolation. Verify its bytes and resulting diff before execution. Do not copy secrets, unrelated untracked files, installed dependencies or running services implicitly. Give each worker a separate immutable assignment and output path. Never let a repro mutate the original checkout or another worker's artifacts.

Use only exposed authorized worker and execution operations for this host. Host-specific agent types, background flags and model slugs are not portable capabilities. Preserve explicit model selections, track requested and observed models separately, and report unknown model diversity honestly. On unavailable workers, an authorized sequential run can be useful but is reduced capability. Missing writable isolation or execution does not grant permission to install dependencies, use a live account, contact a service or write externally.

Give each adversary this brief:

> Break this change. Prove each finding with a run against the reviewed real code, such as a failing test, a repro script or command output that shows wrong behavior. For a design, use an authorized local prototype or probe. Keep repros inside your isolated output. Return the exact command, revision, environment, exit code, actual output and output required by the intent. Leave out anything you did not run. No findings is a valid result. Do not fix the change or modify shared state.

## Verify

Inspect each terminal worker result and artifact under the assignment contract. The lead reruns each proposed command in a separate authorized isolated copy of the same snapshot. Retain a finding only when the observed failure breaks the stated intent. Deduplicate by root cause. Record commands, outputs and dropped claims before reporting. A successful process, reviewer agreement or static code citation alone is not a reproduction. A command that passes drops that finding, with the reason.

If execution or writes are denied, honor the read-only scope. Inspect supplied code and existing evidence, label the result a reduced static review, and place unrun suspicions under Unverified observations. Do not fabricate a rerun, report a full Interrogate pass, or say no bugs exist. If the required input or an indispensable safe reproduction environment is missing, leave that verification gate blocked. Existing legacy rubric references are retained for staged-source accounting and are not mandatory inputs to this revised workflow.

## Output

- Intent, scope and exact snapshot identity.
- Reviewers, requested and observed models, worker independence and capability limits.
- Findings, each with its command, environment, actual and required output, exit code, lead rerun evidence, violated intent and adversary attribution. Say "no verified findings" when none survive, with the execution limits.
- Dropped, per adversary, with counts and reasons. Distinguish disproven claims from unrun or blocked claims.
- Unverified observations and missing verification when operating in reduced capability.

The source checkout, dependency approvals and user authorization remain unchanged. A review never authorizes fixes, publication or personal settings changes.
