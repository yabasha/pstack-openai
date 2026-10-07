---
name: automate-me
description: "Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via create-skill + unslop, optionally pulling fresh evidence from recent transcripts."
disable-model-invocation: true
---

# Automate me

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them such as `jay-mode` or `priya-mode`.

This flow sequences history mining, an exposed `create-skill` authoring companion, and [unslop](../unslop/SKILL.md). If the companion is absent, disclose it and use the [Authoring or modifying a skill playbook](../poteto-mode/playbooks/authoring-a-skill.md) as an explicit reduced fallback. Read that guidance in full before authoring. Do not claim the missing companion ran.

## Portable prerequisites

Preserve the complete pstack baseline before personal customization. Do not draft or edit a personal mode until every baseline inventory disposition is reviewed and each host has observed evidence for supported behavior or an explicit block. User authorization is a separate requirement and does not satisfy this prerequisite. Before then, explain the workflow and identify the unmet gate without making personal configuration changes.

Discover actual read, history, user-question, worker, execution and write operations through [session capabilities](../../references/host-capabilities.md). Follow [workflow ownership](../../references/workflow-ownership.md) and the [assignment contract](../../references/orchestration-contract.md). Source invocation aliases and metadata guide invocation; they do not register host APIs. No scheduling or remote creation is part of this flow.

## Flow

### 0. Check for an existing skill

Look recursively in the authorized project and personal skill locations for `*-mode/SKILL.md` matching the user's handle. Preserve an existing source-host project or personal location instead of migrating it implicitly. Discover host skill paths before choosing a new destination. Mode skills can live in a personal category directory under the project skill root, not only at the top level. If one exists, confirm intent with the exposed user-question operation, or a concise chat question if unavailable, unless they already said "update my skill" or similar:

- Update the existing skill. This is the default for repeat runs.
- Start fresh. Ask why before doing this rare reset.

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited using `git log -1 --format=%cI <path>` when available. If the edit boundary cannot be established, declare the gap and ask for the boundary before mining.
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Locate the active workspace's transcripts before fanning out. Use only an explicitly supplied workspace transcript path or an observed history binding scoped to that workspace. The source uses the system prompt's `agent-transcripts/` directory. If no scoped history exists, disclose the gap and use user-supplied evidence as reduced capability. Do not glob across the source host's global projects directory. That crosses workspace boundaries and reads private chats from unrelated projects.

Survey recent agent conversations within that scope for recurring patterns. Use multiple independent workers across authorized slices of recent history, such as the last 2-4 weeks split into 3 slices, only when exposed and authorized. Assign distinct slices under the assignment contract and inspect each result. Otherwise mine sequentially as reduced capability, without claiming independence. Each slice mining subagent reads transcripts from the workspace-scoped path the parent provides, looks for the signals below, and returns a short structured list of patterns it saw with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped. Label evidence strength and cite pointers in the findings and draft review. Distinguish repeated observed behavior, a direct user statement, an inference and an unresolved contradiction. Do not silently elevate a weak signal.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Use the exposed structured user-question operation when available. Otherwise ask concise chat questions and declare that reduced binding.

Prefer one or two questions with 4-6 options each and multiple selections for categories when the tool supports them. Adapt to the documented option and selection limits without pretending unsupported flags exist. Start broad ("Which areas matter most?"), then follow up on selected areas with specific options. After the structured rounds, one free-form chat question catches anything the options missed.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The [poteto-mode](../poteto-mode/SKILL.md) skill shows the shape. Read it for granularity. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Use the exposed `create-skill` companion, or the declared reduced authoring fallback, to prepare the draft. Placement:

- Path: preserve an existing mode skill's category. For a new mode, use `<project-skill-root>/<handle>/<handle>-mode/SKILL.md` when the repo has an established personal category for that handle. Otherwise use the discovered host project skill location, or its personal location if the user chooses it. Changing personal or global configuration requires explicit authorization.
- Handle: the user's first name or chosen identifier.
- Frontmatter `description`: trigger on their name + `/<handle>-mode` + "work in their style", not on generic keywords like "write code" or "review PR".
- Frontmatter formatting: follow `create-skill`'s YAML rules. Keep `description` as one YAML scalar. Quote it or use `description: >-` with indented continuation lines when punctuation or wrapping requires it.
- Frontmatter `disable-model-invocation: true` by default. Opt out only if the user explicitly wants their mode to apply on every turn.

### 5. Iterate on prose

Apply the **unslop** skill and `create-skill`'s writing guidelines to every line.

Show the draft to the user and take feedback before editing the destination. Preserve uncontradicted sections and show the evidence strength and unresolved gaps beside proposed changes. Draft approval authorizes only the agreed scope, not shipping or remote actions. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

The source landing contract is a worktree off main, a commit and a PR, never a direct push to main. Prepare the approved local change in an authorized worktree when available. Commit, push and PR creation each require their own authorization and observed tooling. Without those grants, return the local draft or reviewed diff and state the shipping gate. Do not create remotes, schedule runs, install tools or change personal settings incidentally.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A `-mode` skill is subjective output. A `create-skill`-style test/iterate benchmark loop isn't useful here. Vibe-check with the user: does it read like them? Did it miss anything? Then follow the separate landing gates.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill (not working conventions): `create-skill` alone, no mining required.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.

