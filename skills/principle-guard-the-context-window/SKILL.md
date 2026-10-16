---
name: principle-guard-the-context-window
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads."
disable-model-invocation: true
---

# Guard the Context Window

The context window is finite and non-renewable within a session. Every token should be worth its cost.

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Isolate large payloads.** Route verbose outputs, screenshots, and large documents to subagents. The main context gets summaries, not raw data.
- **Keep frequently used content inline.** Templates and references used on every invocation belong in the skill file, not in separate files that cost a read each time.
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.

## Capability and permission boundaries

Use the [session capability contract](../../references/host-capabilities.md) to check evidence access and independent-worker operations. Delegate only when the task authorizes it and the session exposes those operations. Follow the [assignment and integration contract](../../references/orchestration-contract.md), retain observed worker identities and inspect their results before reporting summaries. This principle grants no additional permissions.

If independent workers are unavailable or unauthorized, narrow accessible evidence into bounded sequential phases. Keep summaries in the main thread and label this reduced capability. Sequential work does not establish worker independence. If required evidence is inaccessible, name the missing input and access limit; keep the plan provisional and do not claim to have read or summarized it.

Preserve the invocation metadata above without assuming the host enforces it. Report delegation and inspection only after observing the authorized operations.
