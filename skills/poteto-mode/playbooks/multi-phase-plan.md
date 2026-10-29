### Multi-phase or multi-PR plan

Read [poteto-mode](../SKILL.md) in full. Preserve the active controller under [workflow ownership](../../../references/workflow-ownership.md). This is the pstack planning workflow, not a replacement for another controller's implementation plan. Read [session capabilities](../../../references/host-capabilities.md), [model roles](../../../references/model-roles.md), the full [poteto role prompt](../../../references/agent-prompts/poteto-agent.md), and [assignment and integration](../../../references/orchestration-contract.md). Record the steps verbatim in the exposed todo list or an authorized local checklist with that reduced binding disclosed.

**You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence.** The plan is the deliverable. Do not implement.

1. When the change is one or two files with an obvious approach, skip the plan. Say so and stop.
2. Settle open questions by prototype before you write. Run `playbooks/prototype.md` for each. Keep the branch, the SHA, and the screenshots for Appendix A. Ask the operator only about a product or preference call that no run can settle. Give options (the **never-block-on-the-human** principle skill).
3. Explore with authorized, exposed independent workers carrying the full poteto role prompt and mode read. Use inherited model roles unless explicit selection is supported and observed. Record assignment identity, input revision, owned paths, returned artifacts and actual model per the Subagents section. Without workers, explore sequentially as reduced capability and leave independence gates blocked (the **guard-the-context-window** principle skill). Each returns file pointers, conventions, test commands, and entry points. No inlined dumps.
4. Copy the skeleton below into the plan file and fill every placeholder. Unless the operator names a path, write the file under an explicitly authorized local `docs/` directory. If writes are denied, return the plan text and state that no file was saved. Keep every heading and every sub-block in the order shown. One section per PR. One PR is one change with its own evidence (the **sequence-verifiable-units** principle skill). Name the execution playbook in **How to read this**. Use Autopilot-full only when merging is authorized and Autopilot-stack when the operator lands the PRs. Pick between `playbooks/autopilot-full.md` and `playbooks/autopilot-stack.md` per the rule at the end of `playbooks/autopilot-stack.md`. A standing program takes `playbooks/orchestrate.md`.
5. Write under `/technical-writing` in full, then `/unslop`. The body is one Diátaxis mode, how-to. Appendices hold explanation and reference. Each heading states the task or the finding. No long dashes. No mid-sentence colons.
6. Run `bun --no-install <package-root>/skills/poteto-mode/scripts/check-plan.mjs <plan.md>` and fix every line it prints (the **encode-lessons-in-structure** principle skill).
7. Hand back. Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go, under the execution playbook the plan names.

**Verification.** Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability. Read the **prove-it-works** principle skill. That sentence is the verification rule. Every verification block opens with it. The live block is mandatory. The full source expectation is ten independent live lanes at the PR head through its control skill, per the **swarm** skill. Discover actual worker capacity and authorized controls first. Use inherited model roles unless explicit selection is supported and observed. Full live status requires observed independent workers and live control with capacity for the declared lanes. Missing capacity requires explicit reduced or blocked status, reason and evidence. Sequential lanes never prove independence or full source parity. Each lane is one box with a concrete scenario, the screenshot it saves, and its pass predicate. One lane is the **Regression lane against trunk.** It runs the same load-bearing scenario on trunk and head. If trunk does not have the feature, the lane records that fact and gates the behavior the diff adds plus the end state the user waits for instead of inventing a trunk result. The perf gate is dual-sided. Trunk and head must both produce the named metric. If trunk lacks the feature, also isolate the work the diff adds and set an absolute budget for that work plus the end-to-end state the user waits for. Do not claim a ratio between unlike scenarios. The perf block names the metric, the interleaved probe, the trunk baseline measured first, and the rule with the number that fails. If performance does not apply, retain the block and write ``Not applicable. Reason <scope reason>. Evidence `<scope artifact>`.`` without success boxes. A PR that changes an interaction is review-gated. The operator reviews it in chat with screenshots and a video before merge. A PR that changes no interaction writes ``**Review gate.** None. Interaction not applicable. Reason <scope reason>. Evidence `<scope artifact>`.`` and no boxes under it. When workers are unavailable, also record ``Reduced review. Reason <limit>. Evidence `<limit artifact>`.`` even for a None gate. When workers are available, record `Independent review available.` and name the independent reviewer and its evidence.

**Control skill.** Discover an available authorized control companion and its actual exposed tools before execution. The source companion names below identify required purposes, not portable installed capabilities. Pick it by surface. Browser, Electron, and web UIs use `control-ui` from `cursor-team-kit`. CLIs and TUIs use `control-cli` from `cursor-team-kit`. Native mobile uses whatever simulator-driving skill the repo has. A PR that touches two surfaces gets lanes on both. A surface with no control skill is a risk in Appendix C, and its live block still names how each lane drives it.

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `pstack/skills/poteto-mode/playbooks/<execution playbook>.md`. <Who merges, and which PR ids are the operator's items that stop at merge-ready.>

Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.

## Capabilities

Independent workers <available or unavailable>. Evidence `<artifact>`. Capacity <observed positive integer when available>.
Live control <available or unavailable>. Evidence `<artifact>`.
Scheduling <available or unavailable>. Evidence `<artifact>`.
Remote <available or unavailable>. Evidence `<artifact>`.
Model selection <available or unavailable>. Evidence `<artifact>`.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] Resolve the actual repository baseline once and record its ref and SHA. Read these from that baseline at program start. Re-read them at every tick. These example paths use the package-root prefix; resolve actual repository placement before running them. Do not fetch implicitly.
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/<execution playbook>.md`
  - [ ] `git show origin/main:pstack/skills/swarm/SKILL.md`
  - [ ] `git show origin/main:<control skill path>`
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:pstack/skills/<each other leaf skill the program uses>`
- [ ] On the operator's go, use an exposed authorized scheduler for the one-hour audit tick with the tick prompt below only after separate scheduling authorization. Record its identity and observed persistence. If unavailable or denied, record manual audit ticks as reduced capability. Do not claim unattended execution.
- [ ] Use this tick prompt, verbatim. "Re-read the execution playbook from trunk. Audit the operation against it and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then post a short status message to the operator in chat only when the audit found a tracked change that no earlier status message reported, such as a PR opened, a code-ready head, a round launched or closed, a verdict, a merge, a stuck agent and the action taken, a blocker added or cleared, or a decision only the operator can make. Name every such change and nothing else. Do not repeat a table, the merged list, or an unchanged blocker. If the audit found none, end the turn with no reply text. Either way, log this tick's row in your decision trail. The row names the items reported, or none."
- [ ] On the operator's hold or stand-down, send every owner a zero-writes order at once.

### Spawn owners

- [ ] Assign one owner per PR with the full lifecycle the execution playbook names through observed authorized independent-worker operations. Hold exact revision and disjoint write ownership. If unavailable, use a sequential owner as reduced capability and leave independent verdict gates blocked.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Authorize external PR operations, pushes, messages and merges separately before executing them. Resolve the forge once. Default to `gh`; if `command -v origin` succeeds and Origin can resolve the repository, use `origin pr` for every PR operation. Record any fallback to `gh`. Never require `gt`.
- [ ] Open the PR ready, never draft, per **Opening a PR**. Use the run's built-in PR tool when it has one, else `origin pr create --status open --base <base-branch>` or `gh pr create --base <base-branch>` according to the resolved forge. A stack child targets its parent branch.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Run `/deslop` before each commit and `/no-comments` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that merge base in fix rounds. Rebase again only at merge prep, on a `git merge-tree` conflict with trunk, or on a CI failure that comes from a change on trunk, or when a known concurrent change lands in the same files.

### Verdict and merge, for every PR

- [ ] Run a full swarm at code-ready and again only for new behavior, a redesign or a large new diff. A rebase, conflict resolution or minor fix gets a single independent verifier at the new head, with fresh current-head CI and a fresh applicable verdict. Run each full swarm per `pstack/skills/swarm/SKILL.md`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. Two or more audit lanes, each with its own focus, that read the diff and the receipts and distrust the PR body. The root audits the receipts in the merge-ready report before the verdict.
- [ ] Clean only when every required independent lane is `PASS` with inspected receipts at the exact head. Reduced or blocked lanes prevent a full clean verdict. Findings go back to the owner, including a defect that a lane filed as a note. A new head gets a fresh applicable verdict, except for results that stay valid under the patch-id rule in `playbooks/shipping.md`.
- [ ] <The merge or append rule from the execution playbook, with the patch-id rule from `playbooks/shipping.md`.>

### Boot recipe, for every live lane

Full isolation uses a separately authorized isolated environment per live lane at the PR head. Remote setup requires exposed tools and explicit setup authorization. If only local isolated execution is available, disclose the reduced remote binding. Drive through the available authorized control companion. Missing control blocks affected live claims.

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report.

## <Action as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability. Status <full, reduced, or blocked>. Lanes <declared count within observed capacity>. For reduced or blocked status add ``Reason <limit>. Evidence `<artifact>`.``. Keep ten lanes for the full source expectation when capacity supports it. If blocked declare zero lanes and keep unavailable scenarios in Appendix C. For a reduced run retain every omitted scenario and limit there. At the PR head, use the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run <the same load-bearing scenario> at trunk and head. If trunk lacks the feature, record that and gate <the behavior the diff adds plus the end state the user waits for>. Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>

**Review gate.** Interaction applicable. Independent review available. The operator reviews before merge. If workers are unavailable, replace the independent declaration with ``Reduced review. Reason <limit>. Evidence `<artifact>`.`` and leave the independence gate blocked.

- [ ] Independent reviewer audits the exact head and receipts. Save `<review artifact>`. Pass when no findings remain.
- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change on a lane VM. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] <The owner squash-merges its own PR, or the root appends it to the base-branch stack and the operator lands it bottom-up.>

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get `pstack/skills/how/SKILL.md` and `pstack/skills/interrogate/SKILL.md`. The trail per `pstack/skills/show-me-your-work/SKILL.md`.>
````

Checked live boxes additionally require ``Observed head `<40-character SHA>`. Evidence `<nonempty receipt path>`.``. The checker resolves that receipt relative to the plan directory. A checkbox alone proves nothing. The checker is read-only, takes exactly one positional plan path, exits 2 for usage or unreadable input, 1 for format problems, and 0 for structural success. It does not validate implementation or host behavior. Leave other controllers' plans unchanged.

Deferred execution dependencies include `shipping.md` and `autopilot-full.md`, `autopilot-stack.md`, `orchestrate.md`, `opening-a-pr.md`, and `../references/bugbot-triage.md`. Read their complete adapted contracts before dependent execution. Missing contracts block that work. This planning deliverable never authorizes execution, setup, scheduling or external writes.

**Reply:** the plan path, the PR ids with their dependencies and the review-gated set, what the prototypes proved and what stays unproven, and the check script's output.
