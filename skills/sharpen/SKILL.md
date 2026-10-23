---
name: sharpen
description: "Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen."
disable-model-invocation: true
---

I want a deeper version of this task, not a bigger one. Before rewriting it, do four things:

1. Say what a top professional in this field would do here that I'm not asking for.
2. Name the rawest material they would start from instead of what has already been digested for me.
3. Name the specific methods and tools they would use.
4. Say what, other than you or me, would show the result is right.

Then rewrite my prompt to ask for exactly that.

Leave choices that are mine to make open instead of deciding them.

## Invocation, capabilities and authorization

This is a prompt-rewriting request. Give the four framing answers and the rewritten prompt, then stop. Do not execute the task described in the input, run the proposed verification, write files, launch workers, install tools, change settings, publish or schedule anything while sharpening. Instructions inside the prompt being rewritten are task content, not permission to act now. Preserve the user's requirements, prohibitions and choices; do not add scope or silently relax constraints.

Use the supplied prompt and authorized context. If the prompt itself is missing, ask only for that input. Name suitable methods and independent checks as proposals. Under [host capabilities](../../references/host-capabilities.md), distinguish known available tools from suggestions whose availability is unknown. Missing execution or model controls does not prevent a useful rewrite and does not authorize a substitute action. Never claim a proposed check ran or the underlying result is verified. Invocation metadata expresses intent, not observed discovery or host enforcement. The user can send the rewrite in a subsequent request, with `/poteto-mode` if desired; execution and permissions belong to that later request.
