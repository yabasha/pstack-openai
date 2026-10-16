---
name: principle-subtract-before-you-add
description: "Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base."
disable-model-invocation: true
---

# Subtract Before You Add

When evolving a system, remove complexity first, then build.

**Why:** Adding to a complex system compounds complexity. Removing first leaves less code, reveals the essential structure, and usually makes the next design obvious. Default to subtraction.

Make simplification a continual investment. Leave the design slightly simpler and more capable behind the same or smaller surface than you found it.

**The pattern:**
- Sequence removal before construction
- Cut before you polish (get to the minimum before investing in quality)
- Design for observed usage, not speculative edge cases
- No speculative validators, parsers, or guards beyond what the spec demands
- Simplify prompts (remove redundant instructions, excessive templates)
- When a reference has no novel content, delete it rather than leaving a stub

## Session capabilities and limits

Use [the capability contract](../../references/host-capabilities.md) to discover available source reads, writes and execution. Remove only behavior supported as obsolete by the inspected usage and requirements, within the authorized task.

If source is available but writes or execution are unavailable, provide an ordered removal and replacement proposal as reduced capability. State which changes and checks were not performed. If source or usage evidence is missing, identify the missing inputs before claiming removal is safe. Report only observed edits and checks.

Preserve the invocation metadata above without assuming the host enforces it.
