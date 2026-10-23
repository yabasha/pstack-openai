---
name: in-your-own-words
description: "Restate in your own words what you think the user's goals are and what problem they're trying to solve. Use for /in-your-own-words."
disable-model-invocation: true
---

Restate in your own words what you think the user's goals are and what problem they're trying to solve.

## Session capabilities and limits

Use the user's supplied message and authorized context to restate the goal. Keep assumptions and unresolved ambiguities explicit. Do not invent missing intent, retrieve unrelated history, start implementation or take external action from a restatement request. This task can be completed directly in the current context; it requires no worker, execution or durable write. Invocation metadata does not establish host enforcement.
