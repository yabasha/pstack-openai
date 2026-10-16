---
name: principle-redesign-from-first-principles
description: "Apply when integrating a new requirement into an existing design. Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on."
disable-model-invocation: true
---

# Redesign From First Principles

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been there from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.

## Capability and permission boundaries

Use the [session capability contract](../../references/host-capabilities.md) before reading source, editing files or running checks. Apply the redesign within the authorized task. Propagating references does not grant permission to change unrelated files or perform external actions.

If source is available but writes or execution are unavailable, provide a concrete redesign and incremental sequence as reduced capability. State which edits and checks were not performed. If affected source or design context is missing, identify the missing inputs and keep any redesign provisional. Claim implementation or verification only after observing the authorized operation.
