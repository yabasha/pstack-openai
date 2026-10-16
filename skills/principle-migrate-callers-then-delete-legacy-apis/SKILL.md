---
name: principle-migrate-callers-then-delete-legacy-apis
description: "Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers."
disable-model-invocation: true
---

# Migrate Callers Then Delete Legacy APIs

When we decide a new API is the right design, migrate callers and remove the old API in the same refactor wave instead of preserving compatibility layers.

**Rule:**
- Do not keep legacy API paths only because internal callers still exist
- Inventory callers, migrate them, and delete the old API immediately
- Treat temporary adapters as exceptional and time-boxed, not default architecture
- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative

Keeping both old and new APIs creates dual-path complexity, slows cleanup, and makes the codebase feel append-only.

## Session capabilities and authorization

Read [host capabilities](../../references/host-capabilities.md) before acting. Preserve user authorization and host permissions for caller edits, API deletion and test changes. The invocation metadata above is preserved source metadata; do not assume the host enforces it.

Inspect source and caller usage before deciding deletion is safe. Confirm the applicability conditions above, then review caller migration and legacy API removal together. If external compatibility or coordinated breaking changes are unresolved, identify the missing evidence or decision before deleting.

If writes or execution are unavailable, give a coordinated migration and deletion proposal as reduced capability. State which edits and checks were not performed. Missing source or caller evidence blocks safety and completion claims. Report completion only from observed changes and checks.
