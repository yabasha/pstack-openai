---
name: no-comments
description: "Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints."
disable-model-invocation: true
---

# No comments

Spawn Comment Sicko. Act on accepted findings.

Defer to Comment Sicko's fresh perspective.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Steps

1. Discover the independent-worker tools exposed in this session through [session capabilities](../../references/host-capabilities.md). Spawn an independent worker with the [Comment Sicko role](../../references/agent-prompts/comment-sicko.md) under the [orchestration contract](../../references/orchestration-contract.md), following [model roles](../../references/model-roles.md) and [workflow ownership](../../references/workflow-ownership.md). Pass the scope. Do not restate its rules.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, run `/how` or `/why` using [how](../how/SKILL.md) or [why](../why/SKILL.md) on their symbol. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. Reject a second, report it open, and fail `/no-comments`.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, run `/architect` using [architect](../architect/SKILL.md) once for the accepted set and surrounding code. Stop at the sketch. Architect shapes. Step 4 implements.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The [principle-fix-root-causes](../principle-fix-root-causes/SKILL.md) and [principle-redesign-from-first-principles](../principle-redesign-from-first-principles/SKILL.md) skills guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise delete, report the constraint open, and sketch out-of-scope work.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.

## Capability and permission limits

The Comment Sicko role edits only scoped comments when writes are authorized and available. Its final response is a report; that format does not prohibit its comment edits. This coordinator reviews those edits and implements accepted application-code fixes in steps 3 and 4, within caller authorization and scope. Verify edits before reporting deletion counts. Legal and license headers, justified public API contracts, and the role's other proven exceptions survive.

If independent workers are unavailable, use an authorized sequential review as reduced capability, retaining the same scope, investigations and review rules. Authorized scoped comment deletion and accepted fixes can still proceed. Do not claim a fresh independent perspective or a worker result.

If writes are denied, unavailable or unauthorized, use an authorized reduced read-only review. Report proposed deletions and fixes, actual deletion count zero, and unimplemented encodings and constraints. If actual edits are required and no reduction is authorized, report blocked. Missing scope, base branch, role or required investigative skill is a stated limit. Do not invent inspection or verdicts; report affected findings as skips and leave unresolved claims open.

Step 5 does not grant write permission. Without encoding approval, delete the unprotected comment only when scoped comment writes are authorized and available; otherwise report its proposed deletion and the constraint open. Unattended or eval execution never supplies approval by itself.
