---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
disable-model-invocation: true
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Before dispatch, read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), and the [assignment contract](../../references/orchestration-contract.md). Bind worker operations to tools actually exposed and authorized in this session. Request the inherited parent model and effort unless a supported explicit selection is observed. Retain rejections and disclose replacements; an unavailable required selection is blocked. Record requested and observed selections separately, using unknown for unobserved values.

Keep explorers and explainers read-only. Worker assignments record their role, distinct angle, exact input revision, identity and inspected results under the assignment contract. Reading a prompt does not register a worker. If independent workers are unavailable or unauthorized, disclose reduced capability and perform the same exploration and explanation roles sequentially. Never claim parallel or independent exploration from sequential work. If source access is unavailable or denied, report the gap and limit the explanation to inspected evidence.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): use parallel explorers when available, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Dispatch all explorers together through an observed worker binding, with distinct assignments:

- Role: how explorer
- Model and effort: follow the model-role contract
- Access: read-only

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. If workers are unavailable, explore those distinct angles sequentially and retain separate findings. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Assign one explainer worker that explores and explains in one pass:

- Role: how explainer
- Model and effort: follow the model-role contract
- Access: read-only

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. The explainer reads and traces the source itself. If workers are unavailable, apply this role sequentially. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once all explorer results have been inspected, assign one explainer worker to synthesize their findings into one explanation:

- Role: how explainer
- Model and effort: follow the model-role contract
- Access: read-only

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in. In reduced capability, synthesize the sequential findings under the same read-only role.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
