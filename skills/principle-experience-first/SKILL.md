---
name: principle-experience-first
description: "Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones."
disable-model-invocation: true
---

# Experience First

When implementation convenience conflicts with user delight, choose delight.

- Every feature, control, and option must be justified
- Ship less, ship better (polished experience with three features beats rough one with ten)
- Prototype before committing (design decisions are cheaper in throwaway HTML than production code)
- Get the details right (transitions, alignment, spacing, feedback, error states)
- Tighten the core loop (every feature should serve the central workflow or get out of the way)

The user is whoever consumes the work. For a UI that is the end user. For a library or an internal API it is the colleague who imports it. The engineer who maintains the code next is a user too. Weigh their experience the same way, and explain impact from their perspective.

Foundations should serve the experience. Foundational thinking governs the *sequence* of work. This principle governs the *target*.

## Capability and permission boundaries

Read [host capabilities](../../references/host-capabilities.md) before using tools. Apply this principle to the authorized task and available user context. Inspection, throwaway prototypes, production edits and execution require available tools and the corresponding permissions. Choosing delight does not expand authorization.

When context is sufficient but writes or execution are unavailable, provide a reduced-capability recommendation and prototype plan. Identify operations not performed; denied or unavailable execution is blocked. If essential user or workflow context is missing, state the gap and keep the design provisional. Claim completed prototypes, edits or checks only after observing their results.
