---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
disable-model-invocation: true
---

# Swarm

Fan out N independent parallel workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report. Invocation metadata expresses upstream intent; do not assume the host enforces it.

Use [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), and the [assignment contract](../../references/orchestration-contract.md). Discover exposed operations and confirm authorization before dispatch. Upstream cloud/background execution and cloud branch selection require corresponding observed host bindings. Do not create remote branches or install capabilities as an incidental step.

## Start

Open a task list with one entry per phase before launching anything. Use an in-chat list if no task-list tool is exposed.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the host concurrency limit.
4. Select the swarm worker model through current exposed model capabilities and the user's selection. The canonical configured/default model policy is host-specific; do not assume its model slug is supported here. For `auto` or `inherit-parent`, omit explicit model selection where the operation supports inheritance. Disclose any rejection and replacement. Use a supported same-family alternative when available and authorized, otherwise inherited selection; block an arm that requires an unavailable exact model. For a model race, name each arm's requested model up front and record actual models only when observed. Unknown actual models leave diversity unverified.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact full SHAs. A measurement brief also names the method, including sample count, what one sample is, and order. The worker records both in its result. Create immutable assignments and append-only attempt events under the assignment contract. Distinct output ownership applies even when race briefs are identical.

## Phase B: Fan out

Dispatch all N assignments as one fan-out batch through exposed independent-worker operations, within actual concurrency limits. Prefer cloud/background execution when supported and authorized. Use local execution only when the worker needs something on the user's computer. If the host cannot provide the requested environment, disclose the limit before an authorized alternative. A non-default pushed branch requires an exposed base-branch binding and exact revision verification; never infer checkout from a branch label.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence and links to existing artifacts. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first. Keep these report labels separate from assignment terminal states.

If a worker drops out, proceed with N-1 and note it. Record interrupted execution and retain the affected slice as a coverage gap unless another valid assignment covers it.

Unavailable or denied independent execution blocks full swarm behavior. Authorized sequential work is reduced capability. Preserve slice briefs and evidence checks, but do not claim parallel workers, independent results, background execution or race parity.

## Phase C: Aggregate

Wait for terminal results and inspect each result and its artifacts. Reject a return that omits the SHAs or method its brief names. Capture each raw return separately in coordinator-owned append-only files, distinct from each other and all final output files by resolved path. After inspecting the first return and reconfirming permissions, request at most one metadata-only reporting correction from the same worker as a continuation of result inspection. It may report only evidence supported by the already-completed attempt. Preserve assignment identity, revision, scope, method, owner, output path and output bytes. Do not rerun execution or reconstruct an unobserved method. Record the correction event under the same assignment with retryCount 1. After a second miss, or if the worker or evidence is unavailable, retain failed or blocked status and a gap. A gap does not count as a pass. New substantive execution needs a fresh worker with a linked immutable assignment, distinct owner and output path; it cannot inherit the old ownership or reset the original allowance. Missing artifacts and stale revisions also prevent acceptance; this correction policy cannot turn them into success. Follow the assignment contract's bootstrap-only identity observation before immutable substantive assignment and its exact method, result-file and event schemas.

For coverage, every required slice needs a valid result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps. Selecting a winner does not hide gaps in required coverage.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts. Cancel workers only through authorized exposed stop bindings. Inspect terminal state and quarantine partial artifacts from integration. If stopping cannot be observed, say termination is unverified. Cancellation never makes partial output a pass. Preserve durable assignment records with readback when available; missing persistence leaves recovery limits visible.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used. Include capability reductions, blocked assignments, fallback model selections, cancellation limits and unverified coverage. A source review or structural check never proves host behavior.
