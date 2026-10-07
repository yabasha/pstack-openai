# pstack for personal ChatGPT and Codex

Date: 2026-10-07
Status: design for user review. No implementation or installation is authorized by this document.

## Purpose and agreed scope

Create one standalone plugin for the user's personal ChatGPT and Codex environments. Preserve the full pstack baseline before adding personal customizations. The baseline includes all 51 root skills, all 24 principles, and the support files that make the workflows work.

The repository is `/Users/digital-hawk/Herd/pstack-openai`. This design stage contains a README and this spec. It does not fork the entire Cursor plugins monorepo, create a remote, install a plugin, change settings, add dependencies, or implement a runtime. Written-spec approval permits a later implementation plan. The user must review that plan and select execution before implementation begins.

Full coverage means every upstream workflow has an accounted-for purpose, instructions, dependencies, and acceptance evidence. It does not mean every host can execute every workflow. Runtime parity needs actual workers, execution, history, integrations, and permissions. A missing capability remains visible even when a useful reduced workflow exists.

## Source lineage and verified baseline

The canonical source is [Cursor pstack at the pinned commit](https://github.com/cursor/plugins/tree/df581122cde17e6e27686b5a448bde23e4ad4318/pstack). Its `.cursor-plugin/plugin.json` reports `0.15.15`. The exact monorepo commit is `df581122cde17e6e27686b5a448bde23e4ad4318`. Only the `pstack/` subtree is in scope. This spec's counts refer to that revision, not to a claim that today's moving `main` is unchanged.

[FetchUpstream's comparison port](https://github.com/FetchUpstream/pstack-plugin/tree/ba2205db1f83295154e31abc762f533954f581bb) reports `0.2.0` at `ba2205db1f83295154e31abc762f533954f581bb`. Its 26 root skills include six adapted workflows: `how`, `why`, `teach`, `architect`, `blast-radius`, and `recall`. Its README deliberately excludes much of the autonomous orchestration. Use its distinction between evidence and unproven runtime claims as a fallback reference. Do not treat its smaller inventory or older skill text as the canonical baseline.

Source archives fetched by exact commit were inspected without running their code. The canonical subtree contains 164 regular files, including hidden files. Of these, 51 are `skills/*/SKILL.md`; the other 113 include three nested Benny skill files. Those three operational files are not extra registered root skills. The appendices enumerate every file.

The source confirms that arena creates competing artifacts and a later cross-judge, swarm partitions or races workers, and poteto-mode routes coordination through skills and playbooks. Its orchestration includes Bun scripts, worktree auditing, GitHub review watching, and local state. These are implementation concerns, not instructions that can be ported by renaming Cursor tools.

## Alternatives and selected design

A curated conversational subset would be smaller but would omit the orchestration the user requested. A monorepo fork would preserve unrelated plugins and couple updates to irrelevant changes. The selected approach extracts the pstack subtree into a standalone package and keeps one set of adapted skills for both hosts.

Host differences belong in shared capability references and explicit workflow branches. Separate ChatGPT and Codex copies would drift during updates. A shared package lets a reviewer compare one adaptation against one upstream file, while each host has its own verification result.

## Package boundaries and proposed source layout

The future package uses root `plugin.json` with the Agent Plugins schema `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Portable identity stays at the root. OpenAI presentation metadata belongs in `extensions.com.openai.interface`. Root `skills/` is the shared entry point. Manifest references start with `./` and stay inside the package. These choices follow [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).

There is no default MCP server, app mapping, lifecycle hook, or compatibility overlay. Optional integrations are declared only when implemented and verified. The extension object replaces the compatibility overlay rather than merging with it. A second manifest therefore needs a demonstrated compatibility reason.

The proposed layout describes future files. None of these runtime files exist in this design repository:

```text
pstack-openai/
	plugin.json
	README.md
	LICENSE
	NOTICE.md
	UPSTREAM.md
	skills/<upstream-name>/SKILL.md
	skills/<upstream-name>/references, playbooks, scripts
	references/host-capabilities.md
	references/orchestration-contract.md
	references/workflow-ownership.md
	references/model-roles.md
	references/agent-prompts/<upstream-agent>.md
	automations/benny/
	assets/
	docs/guide/
	docs/parity/inventory.json
	docs/parity/evidence/
	docs/superpowers/specs/
```

Keep existing reference and playbook paths where possible. Adapt references together with callers. Move Cursor agent definitions to portable prompt references instead of claiming that their frontmatter registers custom OpenAI agents. Benny stays an optional operational pack outside registered skills. Documentation and images remain accounted for even when a host cannot render them.

The future inventory has one record per source file. Each record contains upstream path, commit, SHA-256, destination path or explicit non-runtime disposition, adaptation rationale, dependent references, and license provenance. It records adaptation status separately from ChatGPT and Codex verification status. Evidence includes the tested package version, host, date, available tools, permissions, input, observed output, and remaining limits.

Allowed adaptation states are `pending`, `unchanged-reviewed`, `adapted-reviewed`, and `reference-only-reviewed`. Verification states are `not-run`, `pass`, `reduced-pass`, `blocked`, and `fail`. A blocked execution is never a full pass. Every source file starts pending with host verification not-run. Source inspection proves an inventory entry exists, not that its port works.

## Capabilities determine execution

The host capability record distinguishes documented support, tools exposed in the active session, and a successful operation. A tool name in a skill is not evidence of availability. Before execution, the coordinator checks the tools required for that branch and reports missing access once.

The shared contract describes operations such as spawn, follow up, wait, inspect result, stop, read file, write isolated output, retrieve scoped history, and run a command. Each branch binds an operation to a callable host tool. It never invents a `Task` tool or translates unsupported parameters into an untested promise.

[OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) describes delegation in ChatGPT Work and Codex, inherited models and permissions, and local custom-agent configuration. This does not establish that every personal ChatGPT conversation exposes workers. Local `.codex/agents/*.toml` configuration is not portable plugin configuration. Package prompts can define a role without installing that role into host settings.

The design treats ordinary ChatGPT without workers or local execution as a constrained host. A ChatGPT session with workers still needs accessible artifacts and tools for the requested task. Codex needs writable workspace access, execution, and applicable approval for local changes. Cloud and local workers are not interchangeable when data exists only on the user's computer.

Unavailable execution produces analysis, a proposed test, or a blocked result. It never produces a fabricated test outcome. Missing files produce a request for the needed source or a bounded evidence gap. Plugin cache files are source material, not a durable writable store.

## Orchestration retains its original purpose

### Arena preserves competition and cross-review

Frame the artifact and rubric, give each candidate the same task, and allocate separate output locations. Candidates do not see the selection rubric if upstream separates that information. After candidates finish, a fresh judge sees the candidates and rubric. The parent reads all surviving candidates, selects a base, records disagreements, grafts useful parts, and verifies the result.

Prefer different available model families when the host supports selecting them. Record the requested and actual model only when the host provides evidence. Distinct workers on an inherited model are legitimate workers, but they do not prove model diversity. Unsupported model selection falls back to an available inherited model with an explicit disclosure. Do not substitute guessed OpenAI names for Cursor defaults.

One failed candidate can leave a reduced contest. If fewer than two artifacts survive, report that competition was not completed. If there is no fresh judge, report that cross-review was not completed. The parent can still examine alternatives, but must label a sequential fallback as reduced capability. Multiple passes in one context are not independent workers.

### Swarm preserves partitioning and aggregation

Declare coverage slices or the race rule before launch. Worker briefs include the goal, exact input revision, output ownership, done predicate, method, and evidence contract. Limit concurrency to the host's observed capacity. Queue remaining workers instead of assuming unlimited cloud concurrency.

Workers return `PASS`, `ISSUES`, or `BLOCKED`, with evidence and gaps. Missing required revisions or measurement methods invalidate the result. Preserve upstream's single retry for that omission, then record a gap. A worker dropout does not satisfy a required coverage slice. A race can still select a survivor under its declared rule, with the dropout disclosed.

### Poteto-mode preserves coordination

Keep its skill routing, principle selection, throughput checkpoint, playbooks, decision trail, verification, and review posture. Read the leaf principle before citing it as a reason for a decision. Fresh workers receive the full relevant mode instructions and role prompt. Do not rely on a Cursor-only agent type to provide that context.

Adapt every playbook, including autonomous runs, multi-phase work, pauses, session pickup, PR watching, shipping, and cleanup. A foreground turn cannot promise to work after it ends. Persistence needs a real host scheduling or durable execution facility, explicit setup, and an observable status. Without that facility, produce a saved continuation brief and mark persistent execution unavailable.

GitHub checking requires actual repository access. Draft PR creation, comments, merge, push, deployment, and messages require the user's authorization and host permissions for the action. Broad autonomy language in upstream mode instructions does not override either. Never poll indefinitely or merge because a summary says checks are green. Verify the precise revision, review verdict, and authorized target.

### Worker state and writes have clear ownership

The coordinator owns integration and the final status. Each worker owns one output directory or worktree and cannot edit the shared baseline or another worker's files. If isolation is unavailable, writers run sequentially. Read-only workers can run concurrently when access allows it.

Each assignment records its ID, input revision, scope, output location, actual role, and terminal result. Failed or stopped workers keep their artifacts for inspection. Resumption verifies the assignment and revision before reusing a worker. Retries cannot replay external writes without checking whether they already happened. Cleanup removes only coordinator-owned artifacts after their evidence is saved.

## History, reflection, and customization

`recall` uses the supplied state capsule first when it is complete. Otherwise, it locks topic, workspace, and time range before reading accessible history. It uses a host history tool or an explicitly supplied transcript, not guessed Cursor or Codex transcript paths. Related repositories and connectors need real access. Separate remembered decisions from current Git or ticket state and cite each source. An inaccessible history corpus remains an explicit gap.

`reflect` uses the active transcript when accessible, otherwise a digest labelled as a digest. Preserve the judgment, tooling, divergent, and synthesis roles. Without workers, run labelled sequential lenses. Present accepted, rejected, and backlog findings before applying durable skill edits. Upstream explicitly requires approval for accepted edits. External backlog filing also needs user authorization and an available integration.

`automate-me` captures working preferences in a personal mode skill. It is not the scheduler. Preserve existing user preferences, scope history mining, distinguish repeated evidence from a single correction, and use a supported authoring and validation workflow. Show the draft before durable changes. Do not create a remote or PR by default for a personal local edit.

Personal customization begins only after the entire baseline inventory has reviewed dispositions and each host has evidence for supported behavior or explicit blocks. It lives in a separate personal mode or customization document with its own changelog. It must not silently remove upstream workflows, alter principle meanings, or change baseline defaults during adaptation.

## Workflow ownership and the proposed ambiguity default

Explicit pstack invocation owns pstack orchestration. Explicit Superpowers invocation owns Superpowers orchestration and its design and implementation gates. The other package can supply a leaf writing or verification skill without taking over the coordinator.

Decision D1 proposes that an unqualified task keeps the already active workflow. With no active workflow, use host defaults and do not activate either orchestration mode automatically. If both are explicitly requested, clarify ownership before launching workers or changing artifacts. This avoids overlapping coordinators and conflicting completion rules. D1 needs the user's review.

Host and user instructions retain priority. No skill can authorize reading unrelated private history, sending a message, widening the sandbox, or skipping an explicit user review gate.

## Dependencies and optional integrations

The instructions-only branches need no external runtime dependencies. Execution branches can need Git, a shell, a language runtime, browser control, repository APIs, or connectors. Discover requirements from the actual playbook and report them before setup. Do not install tools as a hidden prerequisite of invoking a skill.

The upstream poteto tools declare Bun, `commander` at `14.0.0`, and development dependencies `bun-types` and `typescript` at `latest`. Retain their inventory and license provenance, but review their code and lockfile before deciding whether to port, replace, or keep them as reference-only. If a helper is required for full parity, its reference-only disposition must block that runtime claim. A future implementation plan must resolve those dispositions and pin supported dependencies. No scripts are executed in this stage.

Inventory unresolved cross-package references as dependencies too. Cursor built-ins and cursor-team-kit skills such as `create-skill`, `deslop`, `control-cli`, and `control-ui` do not become available through a string replacement. Bind each to an available equivalent with the same proof obligations, or mark the affected branch blocked. ChatGPT conversational analysis cannot satisfy a requirement to drive a real app.

`make-bot-ui` depends on a webhook system, a server-side secret flow, and networking. Keep the skill and its purpose, but leave execution blocked until the user chooses a supported webhook provider and explicitly sets it up. Do not guess routine APIs, accept secrets in chat, install Tailscale, or open a network listener automatically. Secret values stay outside the package and logs.

Benny requires a configured report channel, tracker, repository, control adapter, feature map, and supported automation trigger. Preserve immutable thread coordinates, existing-fix verification, bounded fix attempts, draft-only PRs, and fail-closed behavior. Its nested skills remain operational instructions. Connector reads, messages, tickets, and scheduled actions need actual grants. Neither Benny nor any optional integration is a credential requirement for the base plugin.

Hooks are optional and outside the baseline's required execution path. Current packaging docs limit hook distribution to manual Codex desktop installations and require trust review. Web installation does not deploy local scripts. A hook-free shared package preserves personal-host portability. Any later hook requires its own host evidence and user-reviewed setup.

## Safe updates, versioning, and rollback

`UPSTREAM.md` records source URL, subtree, version, commit, archive digest, import date, and comparison-port provenance. The inventory stores original file hashes. No update follows a moving branch without choosing and recording a new commit.

An update compares the previous upstream snapshot, the proposed upstream snapshot, and the current adapted file. New, removed, renamed, and changed files all require reviewed dispositions. Adaptation notes remain separate from source hashes so an upstream copy cannot erase host constraints or personal changes. An unexplained upstream deletion blocks the update.

Run reference validation, capability checks, license checks, and affected behavioral cases before accepting an update. Recheck both hosts when shared instructions change. Review tool, model, history, and permission assumptions even if the upstream change looks like prose. Personal customization changes do not enter an upstream update by accident.

The port has its own semantic version, starting with a proposed `0.1.0` candidate after implementation, independent of upstream `0.15.15`. A major change changes workflow contracts or removes supported behavior. A minor change adds reviewed coverage. A patch fixes prose or behavior without changing the contract. Release notes name the upstream pin, adaptation changes, host evidence, and blocks.

A release is immutable and identifies a known package commit. Rollback restores that release and its inventory together, then verifies the installed copy's version in each host. Local plugin caches may need explicit refresh. Runtime state, user configuration, secrets, and external automations do not revert merely because package files revert. Migrations therefore need backups and a separate rollback contract before they exist. No global settings or cache files change during this design stage.

## Behavioral acceptance design

The following cases are proposed tests, not tests already run. Execute them in personal ChatGPT and Codex after implementation. Record the exact package commit, host mode, capabilities, permissions, and artifacts for each case. Run both an available-capability case and a missing-capability case where the host permits them.

| Case | Required observation |
| --- | --- |
| Package discovery | Both hosts discover all 51 root skills with valid names and descriptions. The three Benny operational skills are not registered root skills. |
| Inventory closure | Every one of the 164 baseline files has a destination or reviewed disposition, an original hash, and separate host statuses. |
| Arena | At least two isolated candidates finish before a fresh cross-judge runs. The synthesis records rubric scores, base, grafts, dropouts, and real verification. |
| Swarm | Disjoint slices return evidence against the exact input. A missing slice remains a gap. Race selection follows the declared rule. |
| Poteto-mode | A fresh worker receives mode and leaf references, uses the applicable playbook, and returns evidence for its done predicate. |
| Missing worker tools | The result says reduced capability or blocked. It never names invented workers or claims independent review. |
| Model limits | An unavailable model uses a supported disclosed fallback. Inherited workers never imply cross-family diversity. |
| Worker failure | A dropout preserves artifacts, records incomplete coverage, and does not cause false success. Invalid revision evidence receives at most the defined retry. |
| Concurrent writes | Two writers receive separate outputs. If isolation fails, writes serialize. Integration cannot overwrite another worker's work without review. |
| Missing execution | ChatGPT without a shell proposes checks and marks runtime claims unproven. Codex denied execution reports the denied step. |
| Broken references | Missing files, renamed leaves, and unresolved external skills block package acceptance or the affected branch. No silent skip produces full parity. |
| Cursor remnants | Scan operative instructions for `Task`, `AskQuestion`, Cursor paths, model slugs, routine tools, settings writes, and cloud parameters. Every match has an explicit adapted binding or source-only explanation. |
| Recall privacy | Only the declared workspace, topic, and window are searched. Missing history or connectors appears as a gap. Current state is checked independently. |
| Reflect approval | A digest stays labelled. Findings are shown before durable edits. No ticket or message is sent without authorization. |
| Automate me | Existing preferences survive. The user reviews the draft. No scheduling or remote creation occurs as a side effect. |
| Optional setup | Missing webhook, tracker, secret, control adapter, or feature map blocks only the dependent workflow. No credential is requested for ordinary skills. |
| Ownership | Explicit pstack and explicit Superpowers each retain coordination. An ambiguous task follows the reviewed D1 default. |
| Persistent work | Without a scheduler, the turn saves a continuation brief rather than promising future work. With one, status and failures are observable. |
| Completion evidence | An intentionally failing test or inaccessible artifact produces fail or blocked. A plausible worker summary alone cannot produce pass. |
| Update and rollback | A fixture upstream change preserves an adaptation, detects a deleted reference, retains notices, and restores package plus inventory to the prior release. |

Each principle also needs a scenario that demonstrates its choice, not just successful loading. The 27 non-principle skills need input and output cases that preserve their individual upstream contracts. Reference prompts, all 23 poteto playbooks, scripts, and Benny operational files need caller-level checks. A release can claim full workflow coverage only when these records close. Its runtime support report must still distinguish full, reduced, and blocked execution per host.

## Remaining review decisions

D1 is the workflow ambiguity default described above. The recommendation is to retain an active workflow and otherwise use host defaults.

D2 is the runtime parity claim for the first release. The recommendation is full inventory and workflow coverage with explicit per-host capability limits. Do not delay honest reduced branches or call them full orchestration.

D3 is the future helper disposition. The recommendation is to preserve every helper in the inventory and let the implementation plan select reviewed ports or replacements. No reference-only helper can support a claim that its runtime behavior works.

No user decision is needed to create a remote, install dependencies, or change settings now, because those actions are outside this stage. The next review is this written spec. Implementation planning waits for approval.

## Design-stage checks and limits

The destination was absent before creation. Parent directories had no applicable `AGENTS.md`; local `.agents/skills` was checked. Superpowers brainstorming and pstack technical-writing and unslop were read. Pinned archives, manifests, inventories, orchestration instructions, history workflows, agent prompts, license files, and comparison-port scope were inspected. Official packaging and subagent documentation was read on 2026-10-07.

Self-review covers placeholders, scope, ownership conflicts, source counts, status semantics, capability claims, local links, and prose. It does not certify the future plugin. No behavioral acceptance test above has run. This repository is documentation only.

## Appendix A: complete root skill inventory

Each row represents `skills/<name>/SKILL.md`. Source presence is verified. Port adaptation is pending and both host verification results are not-run for every row. Comparison-port presence does not imply equivalence.

| Upstream skill | Kind | Comparison port | Adaptation | ChatGPT | Codex |
| --- | --- | --- | --- | --- | --- |
| `architect` | workflow | adapted | pending | not-run | not-run |
| `arena` | workflow | absent | pending | not-run | not-run |
| `automate-me` | workflow | absent | pending | not-run | not-run |
| `benchmark-checklist` | workflow | absent | pending | not-run | not-run |
| `blast-radius` | workflow | adapted | pending | not-run | not-run |
| `bro` | workflow | included | pending | not-run | not-run |
| `correct` | workflow | absent | pending | not-run | not-run |
| `create-verification-skill` | workflow | absent | pending | not-run | not-run |
| `figure-it-out` | workflow | absent | pending | not-run | not-run |
| `how` | workflow | adapted | pending | not-run | not-run |
| `interrogate` | workflow | absent | pending | not-run | not-run |
| `maintain-verification-skill` | workflow | absent | pending | not-run | not-run |
| `make-bot-ui` | workflow | absent | pending | not-run | not-run |
| `no-comments` | workflow | absent | pending | not-run | not-run |
| `poteto-help` | workflow | absent | pending | not-run | not-run |
| `poteto-mode` | workflow | absent | pending | not-run | not-run |
| `principle-attack-the-premise` | principle | absent | pending | not-run | not-run |
| `principle-boundary-discipline` | principle | included | pending | not-run | not-run |
| `principle-build-the-lever` | principle | included | pending | not-run | not-run |
| `principle-encode-lessons-in-structure` | principle | included | pending | not-run | not-run |
| `principle-exhaust-the-design-space` | principle | included | pending | not-run | not-run |
| `principle-experience-first` | principle | included | pending | not-run | not-run |
| `principle-explain-the-number` | principle | absent | pending | not-run | not-run |
| `principle-fix-root-causes` | principle | included | pending | not-run | not-run |
| `principle-foundational-thinking` | principle | included | pending | not-run | not-run |
| `principle-guard-the-context-window` | principle | absent | pending | not-run | not-run |
| `principle-laziness-protocol` | principle | absent | pending | not-run | not-run |
| `principle-make-operations-idempotent` | principle | included | pending | not-run | not-run |
| `principle-migrate-callers-then-delete-legacy-apis` | principle | included | pending | not-run | not-run |
| `principle-minimize-reader-load` | principle | included | pending | not-run | not-run |
| `principle-model-the-domain` | principle | included | pending | not-run | not-run |
| `principle-never-block-on-the-human` | principle | absent | pending | not-run | not-run |
| `principle-outcome-oriented-execution` | principle | absent | pending | not-run | not-run |
| `principle-prove-it-works` | principle | included | pending | not-run | not-run |
| `principle-redesign-from-first-principles` | principle | included | pending | not-run | not-run |
| `principle-separate-before-serializing-shared-state` | principle | included | pending | not-run | not-run |
| `principle-sequence-verifiable-units` | principle | absent | pending | not-run | not-run |
| `principle-subtract-before-you-add` | principle | included | pending | not-run | not-run |
| `principle-test-behavior-not-implementation` | principle | absent | pending | not-run | not-run |
| `principle-type-system-discipline` | principle | included | pending | not-run | not-run |
| `recall` | workflow | adapted | pending | not-run | not-run |
| `reflect` | workflow | absent | pending | not-run | not-run |
| `setup-pstack` | workflow | absent | pending | not-run | not-run |
| `show-me-your-work` | workflow | absent | pending | not-run | not-run |
| `swarm` | workflow | absent | pending | not-run | not-run |
| `tdd` | workflow | absent | pending | not-run | not-run |
| `teach` | workflow | adapted | pending | not-run | not-run |
| `technical-writing` | workflow | included | pending | not-run | not-run |
| `typescript-best-practices` | workflow | included | pending | not-run | not-run |
| `unslop` | workflow | included | pending | not-run | not-run |
| `why` | workflow | adapted | pending | not-run | not-run |

## Appendix B: complete support-file inventory

These 113 paths are relative to canonical `pstack/`. Every path has source presence verified, adaptation pending, and ChatGPT and Codex verification not-run. Inclusion here accounts for the file without copying or executing it. Runtime helpers require reviewed disposition before any parity claim.

- `.cursor-plugin/plugin.json`
- `.gitignore`
- `LICENSE`
- `README.md`
- `agents/comment-sicko.md`
- `agents/poteto-agent.md`
- `assets/logo.png`
- `automations/benny/FOR_AGENTS.md`
- `automations/benny/README.md`
- `automations/benny/skills/reproduce-and-fix-issues/SKILL.md`
- `automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md`
- `automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md`
- `automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md`
- `automations/benny/skills/setup-benny/SKILL.md`
- `automations/benny/skills/triage-issue-reports/SKILL.md`
- `automations/benny/skills/triage-issue-reports/references/routing.example.md`
- `automations/benny/templates/configuration.example.yaml`
- `automations/benny/templates/reproduce-automation-prompt.md`
- `automations/benny/templates/triage-automation-prompt.md`
- `docs/guide/01-setup.md`
- `docs/guide/02-poteto-mode.md`
- `docs/guide/03-understand.md`
- `docs/guide/04-design.md`
- `docs/guide/05-build-and-clean.md`
- `docs/guide/06-verify-and-ship.md`
- `docs/guide/07-overnight.md`
- `docs/guide/08-principles.md`
- `docs/guide/09-make-it-yours.md`
- `docs/guide/10-recipes-and-pitfalls.md`
- `docs/guide/README.md`
- `docs/guide/images/design.jpg`
- `docs/guide/images/overnight.jpg`
- `docs/guide/images/recipes.jpg`
- `docs/guide/images/router.jpg`
- `docs/guide/images/understanding.jpg`
- `docs/guide/images/verification.jpg`
- `skills/architect/references/design-red-flags.md`
- `skills/architect/references/rationale-template.md`
- `skills/architect/references/runner-prompt.md`
- `skills/create-verification-skill/references/feature-map-example/README.md`
- `skills/create-verification-skill/references/feature-map-example/create-note.md`
- `skills/create-verification-skill/references/feature-map-example/search.md`
- `skills/how/references/explainer-prompt.md`
- `skills/how/references/explorer-prompt.md`
- `skills/interrogate/references/code-quality-review.md`
- `skills/interrogate/references/lead-judgment.md`
- `skills/interrogate/references/reviewer-prompt.md`
- `skills/interrogate/references/rubric.md`
- `skills/poteto-help/references/prompting.md`
- `skills/poteto-help/references/recipes.md`
- `skills/poteto-mode/playbooks/authoring-a-skill.md`
- `skills/poteto-mode/playbooks/autonomous-run.md`
- `skills/poteto-mode/playbooks/autopilot-full.md`
- `skills/poteto-mode/playbooks/autopilot-stack.md`
- `skills/poteto-mode/playbooks/babysit.md`
- `skills/poteto-mode/playbooks/bug-fix.md`
- `skills/poteto-mode/playbooks/eval.md`
- `skills/poteto-mode/playbooks/feature.md`
- `skills/poteto-mode/playbooks/hillclimb.md`
- `skills/poteto-mode/playbooks/investigation.md`
- `skills/poteto-mode/playbooks/multi-phase-plan.md`
- `skills/poteto-mode/playbooks/opening-a-pr.md`
- `skills/poteto-mode/playbooks/orchestrate.md`
- `skills/poteto-mode/playbooks/pause-safely.md`
- `skills/poteto-mode/playbooks/perf-issue.md`
- `skills/poteto-mode/playbooks/prototype.md`
- `skills/poteto-mode/playbooks/refactoring.md`
- `skills/poteto-mode/playbooks/runtime-forensics.md`
- `skills/poteto-mode/playbooks/session-pickup.md`
- `skills/poteto-mode/playbooks/shipping.md`
- `skills/poteto-mode/playbooks/trace-forensics.md`
- `skills/poteto-mode/playbooks/visual-parity.md`
- `skills/poteto-mode/playbooks/worktree-cleanup.md`
- `skills/poteto-mode/references/bugbot-triage.md`
- `skills/poteto-mode/scripts/bootstrap.ts`
- `skills/poteto-mode/scripts/bun.lock`
- `skills/poteto-mode/scripts/check-plan.mjs`
- `skills/poteto-mode/scripts/orch/orch.test.ts`
- `skills/poteto-mode/scripts/orch/orch.ts`
- `skills/poteto-mode/scripts/orch/store.ts`
- `skills/poteto-mode/scripts/package.json`
- `skills/poteto-mode/scripts/watch-pr/cli.test.ts`
- `skills/poteto-mode/scripts/watch-pr/cli.ts`
- `skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts`
- `skills/poteto-mode/scripts/watch-pr/github.test.ts`
- `skills/poteto-mode/scripts/watch-pr/github.ts`
- `skills/poteto-mode/scripts/watch-pr/policy.test.ts`
- `skills/poteto-mode/scripts/watch-pr/policy.ts`
- `skills/poteto-mode/scripts/watch-pr/render.ts`
- `skills/poteto-mode/scripts/watch-pr/tsconfig.json`
- `skills/poteto-mode/scripts/watch-pr/types.compile.ts`
- `skills/poteto-mode/scripts/watch-pr/types.ts`
- `skills/poteto-mode/scripts/watch-pr/watch-pr`
- `skills/poteto-mode/scripts/worktree-audit.sh`
- `skills/reflect/references/divergent-reviewer.md`
- `skills/reflect/references/judgment-reviewer.md`
- `skills/reflect/references/synthesizer.md`
- `skills/reflect/references/tooling-reviewer.md`
- `skills/show-me-your-work/references/decision-log-template.tsv`
- `skills/show-me-your-work/scripts/log.sh`
- `skills/typescript-best-practices/references/patterns.md`
- `skills/why/references/epistemics.md`
- `skills/why/references/investigator-prompt.md`
- `skills/why/references/source-playbook.md`
- `skills/why/references/sources/code-archaeology.md`
- `skills/why/references/sources/databricks.md`
- `skills/why/references/sources/datadog.md`
- `skills/why/references/sources/incident-postmortem.md`
- `skills/why/references/sources/linear.md`
- `skills/why/references/sources/notion.md`
- `skills/why/references/sources/sentry.md`
- `skills/why/references/sources/slack.md`
- `skills/why/references/synthesizer-prompt.md`

## Appendix C: license and notices

The canonical license is MIT with `Copyright (c) 2026 Lauren Tan`. The comparison port retains the same license and has its own `NOTICE.md`. The implementation must keep the upstream copyright, full permission notice, and disclaimer in `LICENSE`. Record copied or adapted portions and exact lineage in `NOTICE.md`. If comparison-port text or assets are reused, preserve its applicable notices too. New authorship never replaces upstream attribution. This is an unofficial port, with no implied endorsement by Cursor, Lauren Tan, FetchUpstream, or OpenAI.

No runtime source or assets were copied into this design repository. The full upstream MIT notice is retained below for the source inventory and any adapted design descriptions.

```text
MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Appendix D: reproducible source inspection

The inspected archive digests are SHA-256:

- `upstream.tar.gz`: `7e76b77c76fca022e17483cdaba0f3efa583043d98ac604d59a20bc22bf5091f`
- `port.tar.gz`: `4bbbb50a4f97abb85554610870cb7bac68bfb00c3e629813eb27b605f9b66812`

A reviewer can fetch the same archives by exact commit, extract them outside the package, and repeat this read-only inventory check. `base` points at the extracted canonical `pstack/` subtree:

```python
from pathlib import Path
base = Path("plugins-df581122cde17e6e27686b5a448bde23e4ad4318/pstack")
files = sorted(p.relative_to(base) for p in base.rglob("*") if p.is_file())
skills = sorted((base / "skills").glob("*/SKILL.md"))
assert len(files) == 164
assert len(skills) == 51
assert sum(p.parent.name.startswith("principle-") for p in skills) == 24
print("\n".join(str(p) for p in files))
```

The archive endpoints are [canonical source archive](https://codeload.github.com/cursor/plugins/tar.gz/df581122cde17e6e27686b5a448bde23e4ad4318) and [comparison-port archive](https://codeload.github.com/FetchUpstream/pstack-plugin/tar.gz/ba2205db1f83295154e31abc762f533954f581bb). Downloading these archives does not install either plugin.
