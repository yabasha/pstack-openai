---
name: principle-make-operations-idempotent
description: "Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs."
disable-model-invocation: true
---

# Make Operations Idempotent

Design operations so they converge to the correct state regardless of how many times they run or where they start from. Every state-mutating operation should answer: "What happens if this runs twice? What happens if the previous run crashed halfway?"

**Why:** Commands, lifecycle operations, and processing loops run where crashes, restarts, and retries are normal. If partial state changes the next run's outcome, every restart becomes a debugging session.

**The pattern:**
- Convergent startup: scan for existing state, clean stale artifacts, adopt live sessions
- Content-based cleanup: compare by content equivalence, not creation order
- Self-healing locks: use PID-based stale lock detection
- Idempotent scheduling: failed work respawns cleanly, fresh input regenerated after each cycle

**The test:**
1. What happens if this runs twice in a row?
2. What happens if the previous run crashed at every possible point?
3. Does re-execution converge to the same end state?

If any answer is "it depends on what state was left behind," the operation needs a reconciliation step.

## Capability and recovery boundaries

Use [session capability discovery](../../references/host-capabilities.md) to establish the tools and permissions available for inspection, execution and durable state. Apply the [assignment and integration contract](../../references/orchestration-contract.md) when recovery involves worker attempts or interrupted external actions.

Before replaying an external action, record explicit authorization, a stable action identity, its destination and the last observed outcome. Inspect the prior action and destination state after interruption. Recognize completed actions without repeating their side effects. Retry only with authorization, an observed safe replay decision and an idempotency mechanism appropriate to that destination. An unknown outcome blocks replay. Local convergence alone does not establish external replay safety.

If inspection, writes, execution or persistence are unavailable, state the missing capability and provide an authorized reduced recovery design where useful. Identify checks and actions not performed; do not claim successful recovery, durable continuity or unattended execution from a design alone. Preserve the invocation metadata above without assuming the host enforces it.
