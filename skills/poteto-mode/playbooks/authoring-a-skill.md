### Authoring or modifying a skill

**You own the skill's voice.**

1. Use the **create-skill** authoring skill when the session exposes it. This package does not ship that built-in dependency. Discover an available authoring workflow through [session capabilities](../../../references/host-capabilities.md), read its instructions and inspect its actual validator before using it. A supported host workflow may provide a capability-specific alternative, but is not the missing create-skill implementation. If neither workflow is available, report authoring blocked. With authorized local writes, offer a provisional draft and manual structural checklist as reduced capability. Do not claim the required authoring workflow ran.
2. Validate the skill: frontmatter has `name` and `description`, referenced files exist, cross-skill links resolve. Report the validator used, its actual results and any checks it does not cover. If execution is unavailable, mark validation unverified and report the checklist findings separately. Structural validation does not verify trigger performance; leave unknown trigger performance unverified.
3. Test cases if structural. Skip if subjective. Read-only tests use fixtures. Report what ran and what remains unverified.
4. Run [Opening a PR](opening-a-pr.md) within the active [workflow ownership](../../../references/workflow-ownership.md), actual capabilities and user authorization. Until that dependency is available, retain the validated local artifact or provisional draft and report PR delivery deferred. Commits and external writes require their own authorization. Do not claim a PR exists without an observed result.

When in doubt, delete. Keep only prose that changes a decision. Tell it to do the thing and skip the reason. Explain only when the rule is confusing without one. Match tone to scope. Point at structural sources such as types, READMEs and config per the [encode-lessons-in-structure principle](../../principle-encode-lessons-in-structure/SKILL.md). Delegate to other skills by path. Don't restate. Propose a new skill for a workflow you keep hitting that is not captured.

**Reply:** summary of the skill, key design decisions, validation notes. Include the authoring workflow actually used, missing dependencies, skipped subjective tests, unknown trigger performance and PR delivery status.
