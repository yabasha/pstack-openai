---
name: sharpen
description: "Sharpen a task before starting: the expert approach, what the user is really after, and the right level of specification. Use for /sharpen."
disable-model-invocation: true
---

Before starting, ask how a top expert would approach this task (their raw sources, their real methods, an outside check that the result is right), what the user is really after, and whether the task is over- or underspecified. Loosen constraints that don't serve the goal as readily as you add ones that do, and leave choices that are the user's to make open instead of deciding them. Fold in only what makes the work better, not bigger, but always keep one outside check that the result is right, without narrating the framing, then do the work. Don't hand back a rewritten prompt.

## Session capabilities and authorization

Work within the user's stated requirements, authorization and current host permissions. Loosen only assumptions you introduced or constraints the user explicitly made optional. If changing a user constraint would materially change the outcome, leave that choice to the user and continue independent authorized work. Select the outside check from accessible evidence or authorized available operations under [host capabilities](../../references/host-capabilities.md). If it cannot run, identify the missing check and report the result as unverified; do not invent independent validation. This skill grants no delegation, installation, scheduling, publication or external-write permission. Invocation metadata does not establish host enforcement.
