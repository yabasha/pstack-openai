---
name: principle-exhaust-the-design-space
description: "Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing."
disable-model-invocation: true
---

# Exhaust the Design Space

When a novel interaction or architectural decision has no established precedent, explore several concrete alternatives before implementation. Building the wrong thing costs more than exploring three options.

**The rule.** When the right answer is not obvious, build 2-3 competing prototypes or sketches. Compare them side by side. Only then commit. Design it twice is this rule by another name. A second flavor of the first shape does not count.

**When it applies:**
- Novel UI interactions (no prior art in the codebase)
- Architectural choices with multiple viable approaches
- Product design decisions where user experience depends on feel, not logic

**When it doesn't:**
- Mechanical implementation where the pattern is established
- Bug fixes or refactors with a clear target state
- Changes where constraints dictate a single viable approach

## Capability and authorization limits

Read [host capabilities](../../references/host-capabilities.md) before prototype writes or execution. Use available tools only within the authorized task and host permissions. Choosing an approach after comparison does not authorize a version-control commit, publication or external write.

When execution is unavailable, compare distinct sketches or proposals and label them untested. State which runtime behavior or interaction feel remains unverified. If writes are unavailable, present sketches in the response. If the decision requires construction or evaluation that cannot be performed, report that step as blocked and name the missing capability. Claim successful execution only from observed results.

Preserve the invocation metadata above. Its presence does not establish that the host enforces it.
