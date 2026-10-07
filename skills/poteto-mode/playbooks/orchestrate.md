### Orchestrate

Read [poteto-mode](../SKILL.md), [capabilities](../../../references/host-capabilities.md), [model roles](../../../references/model-roles.md), [assignment contract](../../../references/orchestration-contract.md), [workflow ownership](../../../references/workflow-ownership.md), and the [poteto role prompt](../../../references/agent-prompts/poteto-agent.md) in full. This playbook responds to "run this whole project" and "own this migration until it lands". Aliases do not register host commands. Read applied principles and routed skills before dependent work. Use [arena](../../arena/SKILL.md), [figure-it-out](../../figure-it-out/SKILL.md), [show-me-your-work](../../show-me-your-work/SKILL.md), [separate shared state](../../principle-separate-before-serializing-shared-state/SKILL.md), and [encode lessons](../../principle-encode-lessons-in-structure/SKILL.md) where the steps call for them. Apply [unslop](../../unslop/SKILL.md) to briefs and reports.

A program needs observed independent worker operations, isolated ownership, execution, persistence and result inspection. Without workers, authorized sequential work is reduced capability and cannot satisfy a required independent review or standing program. Without execution or writable persistence, block helper-dependent work and offer a scoped read-only handoff. Missing wake or remote placement means foreground operation only. Recurring wakes need explicit scheduling authorization. No unattended continuity is implied. Commits, pushes, PR creation, merges, messages, deployments, deletion and setup each retain their applicable permission gates. Gate defaults never grant permission by silence.

The companion wake mechanism is a host capability, not a bundled loop skill. Pending caller paths are `playbooks/autonomous-run.md` and `playbooks/babysit.md`. Stop dependent routes that need those instructions until they exist. The embedded small-task collapse in Frame remains usable without the Autonomous run document. Never install missing companions implicitly.

**You own the program, never the code. Author briefs, drain the queue, keep the frontier green, decide.** For a whole project handed to one standing coordinator chat: multi-day, many stacked PRs, dozens to hundreds of subagents, the human checking in twice a day instead of every five minutes. One task driven to a predicate is Autonomous run. One ambitious run needing a bespoke workflow is figure-it-out. Route here when the work outlives any single agent. Work one agent could finish inside the session's budget is not a program.

Ceremony must scale with the program. On cheap near-identical units, collapse it as each section directs.

The following rules govern the program.

- Completions are queue events, not interrupts.
- Every spawn and every resume carries the standing orders verbatim.
- The brief is the product. A vague brief fails quietly, because a worker cannot ask you a question.

#### Roles and placement

- **Coordinator (this chat).** Local. Frames, authors briefs, drains the inbox, owns the human report, makes judgment calls. It never authors or edits code. Conflicted merges, restacks, and code changes are always tasks. Mechanically landing a verified unit (fast-forward or clean cherry-pick of a worker's commit, then push) is bookkeeping the coordinator may do itself on repos where local git is cheap. Queueing finished work behind an idle stacker is how a deadline harvests nothing. Bind spawn, follow-up, wait, result inspection and stop to exposed authorized operations. State reads and writes go through the bookkeeping helper at drain points. Most compact outputs are bounded summaries; inbox drain returns all pointers, status returns three lines, and `--json` returns complete rows. The CLI never spawns, waits, or wakes anything.
- **Sub-coordinator.** Always local, durable, one per track, and only when the program exceeds what one coordinator's drains can manage. A track the coordinator can drain itself needs no middle layer. Each nested layer re-pays a full orientation preamble, and a blocking sub-coordinator hides its children while the parent idles. Owns its track's units and boards, authors its workers' briefs, spawns its own workers and verifiers only when nesting and isolation are exposed and observed. Depth 3 is the desired ceiling, not a portable runtime guarantee. Rolls up aggregates at wave boundaries. Never forwards raw child reports. Cap in-flight children at what one drain can process, roughly ten, as a rolling window. Never as blocking batches, which cost the slowest child of every batch.
- **Worker / verifier.** Prefer remote workers when exposed and authorized. Local-only verification, this run's accessible transcripts, simulators, local IDE state and local auth require a suitable local binding. Discover control-ui and control-cli companions rather than assuming them. Remote workers cannot be assumed to read the local store, so inline required context or use paths confirmed readable by that worker. Prefer fewer, broader workers. One writer per worktree or branch (principle-separate-before-serializing-shared-state). Prefer a verifier on a different observed model family. Inherit the parent selection unless explicit supported selection is observed. Unknown actual models leave diversity unverified; an unavailable required family blocks that gate.

Depth stays at coordinator, track, worker. Author the track decomposition per project (build, landing, and verification are common cuts, not a required shape). Hard-coded swarm trees were tried and parked as too rigid.

#### Store layout

Choose an explicitly authorized task-owned writable `orchestrate/<project-slug>/` outside the package tree. Every file has exactly one writer. Owners publish facts, readers aggregate at read time. Use `bun --no-install <package-root>/skills/poteto-mode/scripts/orch/orch.ts --store <owned-store>`, written below as `orch`. `ORCH_STORE` is the alternative explicit binding. Plain TSV and JSON stay readable without the CLI.

- `preferences.md` is the standing-orders register: numbered lines, one constraint each (model policy, stack shape and count, verification bar, forbidden paths, escalation policy). Paste it verbatim into every spawn and every resume. Directives decay across resumes, and each dropped one costs a human turn. When you catch yourself restating an instruction, append the line before you act (principle-encode-lessons-in-structure).
- `overview.md` is the durable PR and issue DB. Append. Never rewrite wholesale per event.
- `units.tsv` has one row per unit: id, track, state, branch, PR, head SHA, brief path. Update rows in place.
- `frontier.json` is the computed merge frontier, per Stack safety.
- `ledger.tsv` is the verification ledger, per Verification.
- `inbox/` holds completion pointers. `gates.md` parks human gates (question, options, default on no answer).
- `decisions.tsv` is the trail via the show-me-your-work skill.
- `status.md` is derived from `units.tsv` and `ledger.tsv` at each drain, never hand-maintained. Regenerate it from the tables instead of narrating events into it.


#### Helper contract

Read [orch CLI](../scripts/orch/orch.ts), [store](../scripts/orch/store.ts), [tests](../scripts/orch/orch.test.ts), [bootstrap](../scripts/bootstrap.ts), [manifest](../scripts/package.json) and [lock](../scripts/bun.lock). The CLI requires the exact pinned dependencies in a separately authorized writable copy. The operative package has no installed dependencies; the tested helper snapshot is evidence for that snapshot only. No automatic install occurs. Read `docs/testing/helper-setup.md` as historical setup context only. Its unreconciled-lock and unavailable-snapshot statements are stale. Any future setup needs fresh explicit authorization for an exact writable copy, registry, disabled lifecycle scripts and task-owned cache under Herd. Never run its unqualified installation examples. Missing dependencies block CLI execution.

Use these actual commands through the explicit `orch` binding:

- `init`; `standing add <line>`; `standing show --json`. Compact standing output truncates after four rows, so use JSON or read preferences.md to obtain every standing order.
- `unit add <id> --track <track> --brief <path>`; `unit set <id> --state <state> --branch <branch> --pr <number> --sha <full-head-sha>`; `unit get <id>`; `unit list --json`.
- `ledger record <pr> <full-head-sha> <verdict> --evidence <path> --verifier <identity>`; `ledger check <pr> <full-head-sha>`; `ledger summary`. A missing exact key returns NOT-VERIFIED and exit 2. Usage or runtime failure returns exit 1; success returns 0.
- `inbox push <agent> <unit> <status> --report <path>`; `inbox drain --peek --json`; `inbox drain --json`; `inbox count`. Peek before drain, persist that receipt to an owned artifact and read it back. Capture the complete actual drain output to another owned receipt and verify readback before classifying pointers. Drain removes the queued pointers; arrivals between peek and drain can change the actual batch. If the receipt is lost or interruption makes consumption uncertain, reconcile actual artifacts before retrying or updating rows.
- `gate park <id> --question <question> --options <options> --default <answer>`; `gate list --json`; `gate resolve <id> --answer <answer>`. Resolve permission gates only from actual authorization.
- `frontier set --repo <stack-owner-clone>`, optionally `--prs <bottom-to-top-numbers>`; `frontier show --json`; `status`. Frontier discovery runs local git and gt inspection against that clone. Missing gt metadata, malformed output or pin mismatch is an error, never guessed frontier state.

The helper does not spawn, wait, wake, enforce worker ownership, validate full revision syntax for unit or ledger input, inspect evidence paths, enforce terminal states or verify permissions. Keep immutable assignments and append-only attempts separately under the assignment contract. Match identity, input revision, full current head SHA, artifacts and observed method before accepting results. Ledger counts include historical revisions; filter against the current unit and frontier heads before counting verified completions. A done unit string, ledger label or open-gate count proves no worker completion or authorization. Coordinator-owned bookkeeping may record worker facts; give each worker separate result and receipt paths. Atomic rename is not proof of crash durability or safe adversarial concurrent access.

#### The brief

Your prompts to agents are your only product, and a sloppy brief compounds into slop across the whole tree. Every spawn carries all of it. A field you cannot fill is a unit you have not scoped yet.

```
GOAL         one sentence, the outcome, executable by a stranger with no chat access
SCOPE        paths this unit may write; paths it may not; its exclusive worktree or branch
CONTEXT      pointers to files and PRs; upstream reports pasted in full when this unit
             depends on them, because workers cannot see siblings
ACCEPTANCE   checkable criteria, one per line
VERIFY       exact commands or the control-skill path, plus known gotchas
TIMEBOX      rough cap on runtime; on expiry, return partial findings and stop rather than run on
FORBIDDEN    no gt, no rebase, no force-push, no fixes outside scope, plus unit-specific bans
REPORT       status, branch, head SHA, PRs, verdict, what you actually ran, deviations,
             suggested follow-ups
STANDING     <preferences.md pasted verbatim>
```

Size the brief to the unit. A one-command unit gets the template collapsed to a paragraph that still names goal, scope, the verify command, and the report shape. A 4KB scaffold around a two-line edit costs more to write and obey than the edit. A verified readable local standing-orders path may supply the exact text. Paste it verbatim for remote spawns and every resume. Never replace it with a summary.

A sub-coordinator brief adds its track boundary and unit list, its spawn budget with supported remote placement and the local exception list, the drain protocol, and the rollup format (per child: name, status, PR, head SHA, verdict, one line, plus track status and frontier delta).

A dependency is a context relay, not just ordering. Undeclared upstream context makes the worker guess. Missing fields are a refuse-to-spawn condition. Audit one sampled worker brief per sub-coordinator per wave, concurrently with the wave it samples, never as a gate in front of it. A failing brief stops that track and fixes the sub-coordinator's instructions, not just the worker, because brief quality decays late in a run. Never resume-chain a brief. Respawn fresh with consolidated scope.

#### Steps

1. **Frame.** State the done predicate as something countable ("all 126 units merged, each verified at each current full head SHA with `unit-test-verified` or better"). Quantify scope: units, rough effort, expected stacks, and the wall-clock budget. If one agent could finish inside that budget, stop here and run Autonomous run instead. Collapsing must not depend on another document being present. It means do the work directly in this session, plain workers where they help, verification inline, landing as you go, and none of the store, register, or pilot machinery below. Schedule landing against the budget. By roughly 70% of it, stop spawning and land what is verified. Name the tracks per project. A contested decomposition or one-way door goes through the arena skill before the pilot. Present the framing once. Reversible prep proceeds without waiting.
2. **Initialize the runtime.** Check the helper prerequisites, then run `orch init`. Initialization creates bookkeeping files, not dependencies or workers. Open the trail via the show-me-your-work skill, write the standing orders before any spawn, and seed `frontier.json` from existing PRs with `orch frontier set --repo <repo-dir>`.
3. **Pilot.** Push one unit through the whole path: brief, worker, verification, stack entry, ledger row, merge. The pilot exists to falsify the brief template, the verify recipe, and the unit size while that costs one agent instead of fifty. Fix the contract from pilot evidence before any fan-out. Scale the pilot to the unit. On programs of near-identical cheap units, the first unit is the pilot, run as a normal unit with its verify command inline, and fan-out starts the moment it lands. The dedicated pilot pipeline (separate verifier agent, audit gate) is for expensive or novel unit shapes, not for clone-units where a serialized pilot has nothing to falsify.
4. **Scale.** Spawn a rolling window of workers up to the in-flight cap, refilling as children finish. Blocking batches pay the slowest child of every batch. Spawn track sub-coordinators only past the one-drain threshold in Roles. Recompute ready work after each drain. Relay upstream reports into downstream briefs. Keep sibling communication upward only. The sampled brief audit runs alongside the wave it samples and stops the next refill on failure, not the current one.
5. **Drain.** Run the queue discipline below at every drain point.
6. **Land.** Landing is continuous, never a terminal phase. Integration starts with the first verified unit and runs alongside the remaining waves. On heavy repos the stacker is a standing role from wave one, integrating as units verify. On repos where local git is cheap, the coordinator lands verified units itself per Roles. Keep the frontier green before upper-stack work. Stack safety governs. Advance `frontier.json` only on merge or reported new head SHAs.
7. **Close.** Drain the final inbox, reconcile every spawned agent to a terminal row (done, abandoned, zombie-reconciled), confirm the predicate on the real artifact, confirm every landed PR has a verdict for its current head SHA, audit the trail per show-me-your-work including its cross-model review, encode recurring corrections into `preferences.md` or the brief template. Leave the store intact. It is the postmortem.

#### Queue and drain

- On a completion notification, run `orch inbox push <agent> <unit> <status> [--report PATH]` and return to what you were doing. Never deep-review inline. A completion that needs review becomes a verifier unit. Never review a diff inside a drain.
- Drain in batches at four points: the end of a critical section, a track rollup, a frontier watcher wake (arm it through an exposed authorized wake binding, with a long heartbeat fallback when explicitly authorized), and before a human report. Begin each batch with the peek-and-receipt protocol above, then `orch inbox drain --json`. Preserve completion notifications that arrive during drain for the next batch. A concurrent helper writer can fail on the store lock; keep that pointer externally and enqueue it at the next safe boundary instead of treating it as saved.
- Critical sections you finish first: authoring a brief, a stack operation, a conflict decision, writing a gate, updating ledger or frontier.
- Each drain classifies every pointer (landed, needs-verify, failed, zombie, noise), writes the resulting rows through `orch unit add`, `orch unit set`, and `orch ledger record`, runs `orch status`, then spawns the next wave in one message.
- Account for every spawned child at its track's rollup: arrived, respawned, or its scope explicitly absorbed. Silently redoing a missing child's work hides both the wasted spend and the coverage gap its result existed to close.
- A drain turn ends with the three lines from `orch status`: counts against the states, what changed, gates open. Detail lives in `status.md`. The full reply contract applies at checkpoints and close.

#### Stack safety

- The frontier is a computed object, never narrative. Recompute `frontier.json` from `gt` after every merge and stack mutation because GitHub base refs drift mid-restack while gt tracking is authoritative: ordered PR list, branch names, head SHAs, a generation number, the lowest unmerged PR. Resolve it where gt knows the stack, normally the stacker's clone. A checkout whose gt metadata never saw the submits reports no PRs and the command errors rather than guessing.
- Exactly one stacker per stack may run `gt`, serialized within its stack. Record the holder in the standing orders. Prefer remote restacks when supported and authorized. Missing remote placement remains a limit; never silently substitute local heavy work.
- Workers never rebase and never run `gt`. Babysitters follow `playbooks/babysit.md`, one per stack, scoped to one immutable frontier generation. They report conflicts to the stacker rather than restacking.
- PR closes and retargets go through the stacker only. Closing a base PR orphans every chain above it. Merges and stack surgery are units with briefs like any other.
- One retro watcher follows merged PRs for reverts, post-merge CI breaks, and orphaned follow-ups.

#### Verification

Scale verification to the unit. When VERIFY is a single cheap command, the worker runs it and reports the output, and the coordinator spot-checks receipts. A dedicated verifier agent (on a different model family than the worker) is for units whose verification is expensive, judgment-laden, or high-blast-radius. A verifier agent whose entire product would be rerunning one command is ceremony, not verification.

Write ledger rows with `orch ledger record`. Check the current PR and head SHA with `orch ledger check`. `ledger.tsv`, one row per verdict, keyed by PR number plus head SHA: `live-ui-verified | unit-test-verified | type-check-only | verifier-blocked | verifier-failed`. CI green is an input to a verdict, not a verdict. Behavioral work needs better than `type-check-only`. `verifier-blocked` is not a pass. Respawn when the environment heals. `verifier-failed` gets a fix unit, not a re-verify. A worker may self-report. The coordinator inspects the method evidence and lets a verifier override it on the same key. The helper replaces a row on that key regardless of role; callers must enforce precedence and preserve attempt history separately. A new head SHA voids the row, so re-verify after restack. The ledger answers "was this verified", not memory and not the transcript.

A unit is not done until its output is externalized the moment it lands, never batched to the end of the run. An authorized worker pushes its branch, the designated ledger owner records the inspected verifier result, and receipts land in the store. Without push permission, externalization is limited to the authorized durable artifact and landing remains pending. Work that exists only on one VM when that VM dies was never done.

#### Liveness and failure

- Never resume an agent to check on it. A follow-up can restart an idle worker; inspect its actual state before use. Probe read-only: the ledger, `units.tsv`, `gh`, pushed branches, the worker's observed status through the exposed inspection binding. Transcript mtime is not liveness.
- A silent death gets a synthetic postmortem row in the inbox (unit, failure mode, last evidence, options). Replan on evidence as it arrives. Never wait for full quiescence.
- Retry by mode: cap-hit or oom, respawn with smaller scope. Network-drop, retry as-is. Tool-error, retry on a different model. Unknown, retry once. Two retries, then abandon the unit and replan around it. Missing required SHA or method evidence uses the stricter assignment limit of one inspected retry. A changed scope or input revision gets a new assignment ID linked to its predecessor. Never retry denied permissions or unknown external outcomes into success.
- A zombie that returns hours late reconciles against the current frontier and ledger before anything is accepted. Salvage unique findings through a fresh unit, never a blind merge.
- When continued spawning would produce garbage tree-wide (bad upstream output, broken acceptance, dead infra), write a stop line at the top of the standing orders, let in-flight work finish, fix the cause, clear it.
- Bound your own infra retries the same way you bound a child's. After a few consecutive tool aborts, stop retrying. Write a terminal handoff to durable state (what is done, where it lives, the exact command to resume) and end the run.
- After a host restart, inspect worker state. Do not infer that local agents died or remote work survived. Re-read the standing orders and `units.tsv`, recompute the frontier, reattach surviving remote work by inspected PR and branch plus immutable assignment identity rather than stale agent id, respawn one sub-coordinator per track from its stored brief plus current state, drain, resume. A dead holder does not authorize takeover. `orch` rejects a stale lock until ownership review. Use `--force` only after explicit reviewed takeover permission; it can also steal a live lock.

#### Escalation

Reaches the human, batched into the status page rather than per item: irreversible actions (force-push to shared branches, deploys, deletions, closing someone else's PR), genuine product or preference calls no experiment settles, a standing order that contradicts observed reality, a program-level dead end that survived a replan. Park each as a `gates.md` entry before asking, and route work around it.

Never reaches the human: frontier nudges, restack mechanics, retries, CI flake triage, review-thread triage, format fixes, scope the brief already forbids (refuse and continue), and "should I keep going". Act and log within existing authorization. Park any missing permission instead of assuming it.

Mid-run discoveries fix only what blocks the frontier. Everything else parks in follow-ups. At this fan-out a small scope leak multiplies into PRs nobody asked for.

**Reply:** at checkpoints and close: the predicate and the count against it from `units.tsv` and `ledger.tsv`, tracks and what each landed, the frontier (PR list plus SHAs), verdicts summary, what was abandoned and why, gates awaiting the human (the only asks), the store path, and the trail path. Numbers from the tables, not narrative. Include PR links.
