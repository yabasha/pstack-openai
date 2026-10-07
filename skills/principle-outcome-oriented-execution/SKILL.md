---
name: principle-outcome-oriented-execution
description: "Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code."
disable-model-invocation: true
---

# Outcome-Oriented Execution

Optimize for the intended, verifiable end state rather than preserving smooth intermediate states.

**Why:** Keeping every intermediate step fully stable often creates temporary compatibility code that becomes long-lived debt. Converge on the target architecture and prove correctness at explicit verification boundaries.

**Core rule:**
- Prioritize end-state integrity over transitional stability
- Intermediate breakage is acceptable when it is planned, scoped, and reversible

**Guardrails:**
- Use this for planned rewrites and migrations with explicit phase boundaries
- Declare where temporary breakage is acceptable
- Keep high-signal checks for actively touched areas while migrating
- Require full static and runtime verification at plan completion

## Capability and permission limits

Use [session capability discovery](../../references/host-capabilities.md) before inspecting source, editing files or running checks. Planned intermediate breakage stays within the authorized migration scope and host permissions. It does not authorize external actions or irreversible changes.

If writes or execution are unavailable, provide the target architecture, phase boundaries, acceptable reversible breakage and required verification as a reduced migration plan. Report unperformed implementation and checks explicitly. If source or the target is missing, identify the missing input before proceeding. Denied or unavailable execution leaves verification blocked; require observed full static and runtime checks before claiming plan completion.

The original `disable-model-invocation` metadata is retained. Its enforcement depends on the host and must not be assumed.
