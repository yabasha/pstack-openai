---
name: principle-never-block-on-the-human
description: "Apply when tempted to ask 'should I do X?' on reversible work. Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible actions."
disable-model-invocation: true
---

# Never Block on the Human

The human supervises asynchronously. Agents must stay unblocked. Make reasonable decisions, proceed, and let the human course-correct after the fact.

**Why:** Every permission pause stalls the pipeline and makes the human the bottleneck. Since code changes are reversible and reviewable, a wrong decision usually costs less than blocking.

**Pattern:**
- **Proceed, then present.** Do the work, show the result. Don't ask "should I do X?" Do X, explain why.
- **Make the system self-healing.** When you notice a problem, log it and fix it in the next round.

**Boundaries:**
- **Irreversible actions** (force-push, delete production data, send external messages) still require confirmation.
- **Reversible actions** (write code, edit notes, split tasks) should proceed without blocking.
- **Product direction** comes from the human. *Execution* should not block.

## Authorization and session capabilities

Apply the proceed-then-present pattern to authorized work within the assigned scope. Reversibility does not grant permission. An explicit user review gate still controls the gated action; prepare its reviewable result and continue independent authorized work while awaiting review. Human product direction remains authoritative.

Use the capabilities actually available in the current session, following [host capabilities](../../references/host-capabilities.md). If writes are denied or unavailable, provide a reviewable proposed change and say it was not applied. Continue work that available permissions support. If no permitted action can advance the task, report the missing capability or input. Do not claim an edit, save or execution succeeded without observing it.

Keep problem logging and next-round fixes within authorized scope and available persistence. Preserve confirmation for irreversible actions, and any explicit user or host approval requirement, including external messages.

The source invocation metadata is retained. Do not assume every host enforces `disable-model-invocation`.
