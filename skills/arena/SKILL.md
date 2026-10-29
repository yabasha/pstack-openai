---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and integration](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md). Use only exposed, authorized operations. Read each applied principle leaf in full before dependent work. Missing required reads block that work. Invocation aliases are guidance, not proof of registered host commands.

Independent candidates and a fresh independent judge require observed worker operations and inspected artifacts. If unavailable, produce authorized sequential alternatives and parent comparison only as reduced capability. Do not claim independence, background execution, model diversity or a full arena pass. If independence is required, leave that gate blocked.

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Open an exposed todo list with one entry per phase before launching anything. Without one, use an authorized local Markdown checklist and disclose the reduced binding.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Use an explicitly supplied, authorized `arena runners` preference if available. Otherwise request two inherited workers, one per seat. The source defaults used two specific model families. Their source-host slugs are not portable availability evidence. Select an explicit model or effort only from current exposed documentation or observed enumeration under the model-role contract. An `auto` or `inherit-parent` entry means omit explicit model selection. On rejection, record it and disclose a supported same-family alternative when available, otherwise an authorized inherited alternative. If the exact model is required, block instead. Record requested and observed model and effort separately, using unknown when unobserved. More seats can cover multiple design directions. Same model N times is appropriate when work is generation-bound rather than judgment-sensitive. Unknown models leave diversity unverified.
4. Assign output paths. Each candidate writes to its own authorized location, a git worktree where supported, otherwise a distinct local candidate directory. Follow [separate-before-serializing-shared-state](../principle-separate-before-serializing-shared-state/SKILL.md). Confirm isolation and write permissions before dispatch. Record immutable assignment identity, input SHA, owner, role and evidence links under the assignment contract. Workers never integrate shared files. Worktree creation and persistence require observed authorized capabilities.

## Phase B: Fan out

Dispatch all N independent candidates together through the exposed worker operation, using observed background execution when available. Give each the same task, shared grounding path, its isolated output path, and instructions to produce both the artifact and a short rationale. Withhold the rubric from candidates. Inspect terminal results and artifact paths before accepting completion; a wait notification alone is insufficient.

A fresh worker can still inherit the parent's conversation, including its rubric. Use an exposed context-isolation setting for blind candidates, such as `fork_turns: "none"` where the host documents it, and inspect that dispatch setting. Asking a worker to ignore inherited grading cues does not remove exposure. If isolation is unavailable, disclose that limit and withhold the blind comparison claim. Quarantine exposed attempts rather than relabeling them as blind; any replacement gets a new immutable assignment and its own output path.

Each rationale names the alternatives the candidate considered and what it rejected.

If a configured runner is rejected, record the rejected selection and never retry it unchanged. Use only a documented supported and authorized same-family fallback, or drop the seat when none is available. Replace dropped seats up to the configured count, or the two-seat default, using an authorized surviving selection or inheritance. Disclose replacement models and preserve explicit exact-model requirements as blocked. Each replacement gets a fresh immutable assignment and output owner. Never replace a writer until its terminal state or safe quarantine is inspected. If execution leaves fewer than two completed candidates, label incomplete competition. Zero survivors blocks synthesis. Never integrate partial or cancelled artifacts as completed candidates.

## Phase C: Cross-judge

After all Phase B candidates reach terminal state and their accepted artifacts are inspected, inspect the authorized cross-judge pool in preference order. A judge must use an observed model family different from the parent's. An auto or inherit-parent alias never judges. Do not infer a family from a source-host alias or invent model mappings. Try only currently supported, authorized selections and track rejected entries so no rejected model is retried. Preserve exact-model requirements.

Spawn one fresh readonly judge only when a different family is supported. Give it the rubric and completed artifacts by path label. Verify actual parent and judge model families in the result before accepting the independent cross-family claim. If the selected model resolves to the parent's family, quarantine that verdict. Unknown observed families leave that gate unverified. If no different-family judge can run, skip judging, let the parent choose alone, and label the result reduced capability. Do not replace it with an inherited or same-family judge. A required independent or cross-family gate remains blocked.

The judge scores each criterion and recommends a base with rationale. It has no candidate write ownership and never starts while candidates are still writing. Its missing or unverified verdict must remain explicit in the synthesis record.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge when a verified judge ran. Otherwise record parent-only selection and reduced capability. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the [Laziness Protocol](../principle-laziness-protocol/SKILL.md).

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per [redesign-from-first-principles](../principle-redesign-from-first-principles/SKILL.md). Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and deliver the consensus shape within authorized scope. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per [prove-it-works](../principle-prove-it-works/SKILL.md).

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

Apply [unslop](../unslop/SKILL.md) to the synthesis prose. External publication, commits, messages and setup require their own authorization.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts and their source candidates, the rejections, the dropouts if any, and the verification result.
