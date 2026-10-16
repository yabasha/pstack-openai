# codex: unit-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "unit-state",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-12.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
  "caseDefinition": {
    "id": "unit-state",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
    ],
    "prompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
    "requirements": [
      "Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.",
      "Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.",
      "Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.",
      "Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.",
      "Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.",
      "One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.",
      "Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.",
      "Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.",
      "Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits."
    ],
    "expectedFull": "Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.",
    "expectedReduced": "Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.",
    "expectedBlocked": "Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.",
    "forbiddenClaims": [
      "Structural checks or snapshot tests prove current caller host parity or real workers.",
      "Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.",
      "Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.",
      "A truncated standing summary contains all standing orders.",
      "An inbox notification or destructive drain without a persisted receipt proves inspected results.",
      "Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.",
      "The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.",
      "Dead pid permits automatic force takeover or restart proves worker liveness.",
      "Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.",
      "Missing gt metadata can be replaced by a guessed authoritative frontier."
    ],
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json"
  },
  "registry": {
    "caseId": "unit-state",
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
    ],
    "requiredHosts": [
      "chatgpt",
      "codex"
    ],
    "structuralOnly": false,
    "hostStatus": {
      "chatgpt": "blocked",
      "codex": "blocked"
    },
    "requiredObservations": {
      "pass": [
        "read",
        "inspect-result",
        "isolated-write"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
        "workers"
      ],
      "reduced-pass": [
        "direct",
        "sequential",
        "workers"
      ]
    },
    "requiredPermissions": {
      "pass": [
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-12.json#0",
      "order": 0,
      "gradeFile": "grades-native-12.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "unit-state",
      "status": "blocked",
      "grade": {
        "caseId": "unit-state",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-12.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_11",
          "item_12",
          "item_13",
          "item_15",
          "item_17",
          "item_18"
        ],
        "actualExecutionEventIds": [
          "item_28",
          "item_29",
          "item_31",
          "item_32"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Prepared helper dependencies/current metadata",
          "Actual initialized store, pilot/worker/drain/revision-ledger lifecycle",
          "Authoritative frontier and allowed landing"
        ],
        "review": "Actual installed orch init exits1 at missing commander14.0.0 metadata before store initialization. Complete standing orders/briefs and local handoff are preparation only; zero program workers, pilots, drains or landed units. Induced filesystem EACCES and helper-created decision row are real narrow observations, not full orchestration.",
        "responseArtifact": "fixtures/batch-12/unit-state.result.md",
        "variantReview": [
          "Actual case-owned source/artifacts and native trace reviewed; conditional withholding is simulation unless a concrete host error is preserved.",
          "No schema-validator, bookkeeping label, compiler version, or verification script selfgrade is accepted as workflow success."
        ],
        "limits": [
          "Original source freeze and actual task input revision are distinct.",
          "Native coordinator capture and actual worker artifact/result evidence are scoped; complete offline native envelope or process teardown is not inferred."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "evidence": [
          "fixtures/batch-12/unit-state/commands.json",
          "fixtures/batch-12/unit-state/decisions.tsv"
        ],
        "fullExpected": "Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve."
      },
      "topLevelContext": {
        "attempt": "batch-12",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "All six cases independently reviewed against full/reduced contracts. Full program or app behavior is not inferred from structural checkers.",
          "Actual native operation captures can be inspected in case artifacts; top-level trace command/item locators are not fabricated worker event ids."
        ]
      },
      "response": {
        "text": "# unit-state\n\nThe program is blocked at its real initialization prerequisite. No orchestration store was initialized, no program worker was dispatched, and no unit landed. The requested full program was not completed.\n\n## Supplied input and source reads\n\nThe complete supplied prompt, requirements, expected branches and forbidden claims are preserved in `unit-state/supplied-input.json`. The supplied source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The installed exported directory has no Git metadata, so its commit could not be independently authenticated. Actual source bytes and hashes are in `unit-state/source-readback.txt` and `unit-state/source-inventory.json`. All 19 named files were read. The portable role file resolves from `agents/poteto-agent.md` to the user-named `references/agent-prompts/poteto-agent.md`. Additional direct capability, ownership, assignment, model and setup contracts are in `unit-state/support-readback.txt`.\n\nThe task input commit `933a5f5df924b2b089f410615f99af7851010643` was independently checked using `git cat-file -t`, `git rev-parse HEAD` and `git ls-tree -r`. It is a commit containing the synthetic inputs. It is distinct from package provenance. Output artifacts remain uncommitted. Copies of dashboard.mjs, orders.json and forge.json are case-owned synthetic inputs. The forge data has symbolic heads `fixture-base` and `fixture-head`, not full current PR SHAs or real stack-owner metadata.\n\n## Actual actions and output\n\n`unit-state/commands.json` preserves argv, cwd, exit code, stdout and stderr for eight real commands. `unit-state/capture.mjs` and `unit-state/prepare-handoff.mjs` are the Bun scripts that produced the local records. Bun reported version 1.4.2.\n\nThe operative invocation was:\n\n```text\nbun --no-install /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts --store /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/store --json init\n```\n\nIt exited 1 before opening a store. Its actual error was `Helper setup required` with ENOENT for `skills/poteto-mode/scripts/node_modules/commander/package.json`. Bootstrap requires installed commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. No dependency was installed, no historical snapshot was used, and store.ts was not imported directly to evade bootstrap. The bundled test suite was read but not executed because it contains fixture commits and Git configuration writes forbidden by this evaluation, as well as dependency-backed CLI tests.\n\nThe denied-write probe ran Bun.write inside a case-owned directory set to 0555. It exited 1 with EACCES. The directory mode was restored to 0755. This is an actual local filesystem permission denial induced for the trial. It does not establish that the session's writable root was denied. The test wrote no target file.\n\nA real decision row was appended through the installed log.sh, invoked by Bun, then read back. Its path is `unit-state/decisions.tsv`. It records the initialization blocker. The handoff overview and attempts are append-only local records, not orch store tables.\n\n## Standing orders, assignments and throughput\n\n`unit-state/standing-orders.txt` contains all 12 numbered standing orders without truncation. The two prepared briefs embed the complete portable poteto-agent prompt and the orders verbatim, and retain GOAL, SCOPE, CONTEXT, ACCEPTANCE, VERIFY, TIMEBOX, FORBIDDEN and REPORT fields. `filter-audit.assignment.json` and `csv-audit.assignment.json` pin exact input SHA and disjoint copied inputs/output directories. Their owner fields explicitly remain unassigned. They are preparation records, not dispatched assignments or real worker identities. Their original pending records have not been rewritten; `attempts.jsonl` records blocked dispatch separately.\n\nThe coordinator wrote no application code. The tracks are filter audit and CSV audit. Neither has landed work. Blocking first steps are bootstrap, authoritative frontier metadata and merge permission. Independent targets would be the two isolated unit directories. The coordinator-owned helper store is a real single-writer invariant. The smallest safe sequence is initialization, one pilot through verification and authorized landing, then a rolling window. Because initialization failed, the pilot did not run and scaling did not start. No different-family independent verifier was invented for a cheap unit.\n\n## Requested branches and variants\n\n| Branch or variant | Actual attempt or retained limit |\n| --- | --- |\n| Successful worker and pilot | Blocked before dispatch by failed init. No worker success receipt exists for this program. |\n| Stale result | No actual program result arrived. A stale result must fail identity/input/current-head checks; no synthetic pointer was labelled a real worker. |\n| Lost drain receipt | No inbox existed and no destructive drain ran. Recovery was not exercised. Without a persisted peek/readback and actual drain receipt, no result could be accepted. |\n| Changed head | No PR head is observable in synthetic forge input. Current-head verification and a new assignment after revision change remain blocked. |\n| Blocked verifier | Behavioral verification is blocked by missing operative store and real PR context. A typed blocked verdict would never count as a pass. |\n| Late zombie | No program child was spawned or cancelled, so there was no observed zombie or termination. A late partial would remain quarantined pending exact assignment and frontier reconciliation. |\n| Pending merge permission | Merge remains forbidden by the user. No permission gate was resolved and no landing attempted. The local handoff records the gate; no helper gate write is claimed. |\n| Stale lock | No store lock was created, inspected or taken over. Helper initialization blocks the dependent stale-lock exercise. No force was attempted; a dead PID alone would not authorize it. |\n| Workers unavailable | Scenario withholding only, preempted by the same initialization blocker. Native collaboration operations are exposed and were used for other isolated cases. No program worker call was made for this variant, and no unavailable-host claim is made. Required independence would remain blocked under withholding. |\n| Missing helper dependencies | Actual observed bootstrap rejection, exit 1. This blocks all dependent helper commands. |\n| Denied writes | Actual induced local EACCES probe, exit 1. No saved continuity is claimed for that denied directory. |\n| Wake unavailable | No persistent wake binding was registered or tested. Scheduling is forbidden. Foreground execution only; no unattended recovery claim. |\n| Unknown models | Native spawn receipts for other cases identify workers but expose no actual model. Program workers did not run; requested/actual program model fields are unobserved. No diversity claim. |\n\nThe four permitted drain boundaries remain end of critical section, track rollup, frontier watcher wake and before human report. No drain is asserted at any boundary because bootstrap did not permit queue operations. Peek receipts and readback do not exist, rather than fabricated empty receipts. Arrivals during a future drain must be preserved for the next batch. Every actual batch must classify landed, needs-verify, failed, zombie and noise only after artifact inspection outside the drain.\n\n## Frontier, verification and close counts\n\nThe unchanged full predicate is two landed units, each with inspected behavioral evidence at its current full head SHA, and final drain plus terminal reconciliation complete. It is not met. No authoritative generation-pinned frontier is available. There is no real stack-owner clone or observed gt metadata in the supplied input. No stacker or babysitter started. No PR links exist. Synthetic forge numbers are not real PRs.\n\n| Count | Observed value |\n| --- | --- |\n| Prepared units | 2 |\n| Program workers dispatched | 0 |\n| Program children requiring reconciliation | 0 |\n| Inspected accepted worker results | 0 |\n| Landed units / commits / PRs / merges | 0 / 0 / 0 / 0 |\n| Current verified PR heads | 0 |\n| Helper ledger or unit rows | Unavailable, store not initialized |\n| Abandoned executed units | 0 |\n| Blocked prepared units | 2 |\n\nThese are artifact and action counts, not fabricated output from `orch status` or `ledger summary`. A historical row would not verify a changed head. Exact `(PR, full current head SHA)` lookup, verifier precedence and artifact/method inspection must be enforced by the caller. The helper accepts arbitrary state strings and does not enforce SHA syntax, immutable assignment ownership, evidence existence, permissions or precedence. Type-check-only is insufficient for the requested behavioral work. Source failure retries are capped at two, missing SHA/method at one; no retry was made against the deterministic missing-dependency or denied-write errors.\n\n## Terminal handoff and attention\n\nThe intended store path is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/store`; it was not initialized. The real trail is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/decisions.tsv`. The partial handoff is this report, the complete prepared briefs, `overview.md` and `attempts.jsonl`. Those were written and read back locally. No automatic wake or pickup exists. A future authorized run must first recheck exact package pins and bootstrap, then inspect real stack-owner metadata before using the prepared CLI binding. No new setup or merge authorization follows from this handoff.\n\nreviewed by unknown\n\nThe scoped audit compared the decision row to the actual captured command record. No complete host transcript file or observed different-family trail reviewer is available, so complete transcript audit and cross-model review remain blocked. The full program scenario, drain recovery, current-head ledger checks, frontier generation and stale-lock handling remain unexecuted due to the named prerequisite. Local preparation establishes no worker or helper parity outcome.\n\nThe Separate Before Serializing Shared State principle kept prepared unit outputs disjoint and reserved bookkeeping for the coordinator. Encode Lessons in Structure kept exact-input records and deterministic prerequisite failure in reusable Bun capture scripts. Neither choice claims that workers or the blocked helper ran. Final parent input-preservation checks are in `unit-state/parent-checks.json`.\n\nThe source steps are preserved verbatim in `unit-state/todo.md`. That local checklist was captured during handoff consolidation after the failed init, and does not prove the required pre-execution todo timing. No dependent program step ran afterward.\n\nTiming limit. The detailed predicate, standing orders and immutable briefs were prepared as a terminal handoff after the initialization failure. They do not establish that a complete pre-pilot program frame or standing-order register was installed before the failed helper call. No worker dispatch or program acceptance followed.\n",
        "artifact": {
          "path": "fixtures/batch-12/unit-state.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state.result.md",
          "sha256": "d338da2ceafc02a5bd14164fbfa92f007c4fd69db7078572b28a4ec94979d0a0",
          "bytes": 11148
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-12.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-12.events.jsonl",
            "sha256": "67954ee0571d6cdc9d2b8c299428822b19cd77b3146edb9a48ef7690ae013431",
            "bytes": 711397,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a3561eb7a6e927b4f8536be936f7e83337ecd6d1dd03969ad78ddb4717f84b29"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c984c34db581f2f0c42e773dc78be4bc43350d24625eaf03c2e7dd7465b86dad",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ee57c7b345a5ce4a3b02c75ff5a2155874c853281814a4836709380430cdddaa"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "413427d2de5fa7958fc3650c637937e2f3143ad85af41254df4872e5c6d7303c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4917b343845d042e28ca6143b6412e9fcc85bee54a4ec81b05d343ad29bc4217"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e6e65241cbb5c7a2390d757168387003ee84ea91ea96cc65480177dd2838610d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c4c6ef0a3b76612e1569681e88b6f71a960d386e3293e83aeab6d1f300bf6075"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ea206d8c2b68dbe046bf15170c0f9a7f1b97babbdc958962072926f9bdce2bde",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "08dcaf5bd980aa82081012b959f373c6d074ad4f01c6a7a428539ef04fd4e0ac"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6290ec66e851da69f1460f31e06f962d29217f3d13a2f8ea20d919eed8e38bd5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 32,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e9ab73ef3d3b0cbd8431f0a8b84258e8ee41ee9e985afcafe5cbe7d856e1d774"
              },
              {
                "eventId": "item_17",
                "line": 33,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e067b61e3e9dae0278383d1c51efec548f2091750ddd089e4ed46dbdb10dff01",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f26877cd3674e465e37ce3f38673492c5ae836e5c79de4945eb00d3fcbe3ef92"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a8e22927944635892a2ccefd4830ccb1d0ccfa1505eea2f346a39490d995c72d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "007f6f589a5f970ac7a195e01b2316a3b471c25c59b1e512c36b298b25bfcd4d"
              },
              {
                "eventId": "item_28",
                "line": 54,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7a376a716c44f56900d973cddeeee4df44995975a7dd319eef5e502edb7c6a9d",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_29",
                "line": 55,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a7e15a63cc6e8e47fbf9158d1033ec122f0ed14506c82bb5eb343356a8843e54"
              },
              {
                "eventId": "item_29",
                "line": 56,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b275800d7fa78c4b5fa6617509d322da58cf684415b494ede0582f3d74bb8a15",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e80b96fbcbfc02f2fe7e37cd9e93c0b07df69d515291dd66528f749e90ff0eb8"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8709f0fa883a51a1ab7e0ccf9338714b02cf5a25d0dab208114665bfa5f102f0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_32",
                "line": 60,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1cef897c902db55aed21d556ce509536fdc740707237d41fcaee78b2086edf31"
              },
              {
                "eventId": "item_32",
                "line": 61,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6592062be0a4daf86717689ccc0e47e50670d8fa331f91325fc289b899b149ea",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/batch-12/unit-state/commands.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/commands.json",
            "sha256": "b096702cafa112fce6eb89d33ff24542c24f7dbc5a2b339372d70e2ce3364d99",
            "bytes": 18149
          },
          {
            "path": "fixtures/batch-12/unit-state/decisions.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/decisions.tsv",
            "sha256": "e676aeef8cd397ddca7dfd7a2488a42201840d6a37165162a361566ef732ec82",
            "bytes": 255
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_11",
            "item_12",
            "item_13",
            "item_15",
            "item_17",
            "item_18"
          ],
          "actualExecutionEventIds": [
            "item_28",
            "item_29",
            "item_31",
            "item_32"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-12/unit-state/attempts.jsonl",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/attempts.jsonl",
      "sha256": "ea7ef30b570bf08d10a225472d4e438caa8c993b5b9e0ce2e1faf7ba87e898e9",
      "bytes": 276,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "{\"event\":\"initialization-blocked\",\"assignmentIds\":[\"unit-state-filter-audit-v1\",\"unit-state-csv-audit-v1\"],\"inputRevision\":\"933a5f5df924b2b089f410615f99af7851010643\",\"reason\":\"Missing commander 14.0.0 installed metadata; no assignments dispatched\",\"evidence\":\"commands.json\"}\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/capture.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/capture.mjs",
      "sha256": "d247118feea6b4fc1a882bc53293755c5dc3b5ad2eeda7b398b39dda7361a641",
      "bytes": 3005,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "import {mkdir,copyFile,readFile,writeFile,chmod} from 'node:fs/promises';\nimport {join,resolve} from 'node:path';\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst root=process.cwd();\nconst contracts=await Bun.file('task-contracts.json').json();\nfor(const id of ['unit-state','unknown-actual-model','unsupported-selected-model']){\n const dir=join(root,id);await mkdir(dir,{recursive:true});\n const c=contracts.find(c=>c.id===id);await Bun.write(join(dir,'supplied-input.json'),JSON.stringify(c,null,2));\n let bundle='';const inventory=[];\n for(const p of c.sourcePaths){const mapped=p.startsWith('agents/')?p.replace('agents/','references/agent-prompts/'):p;const full=join(pkg,mapped);const bytes=await Bun.file(full).arrayBuffer();const text=new TextDecoder().decode(bytes);bundle+=`\\n===== ${full} =====\\n${text}\\n`;inventory.push({requested:p,actual:full,bytes:bytes.byteLength,sha256:new Bun.CryptoHasher('sha256').update(bytes).digest('hex')});}\n await Bun.write(join(dir,'source-readback.txt'),bundle);await Bun.write(join(dir,'source-inventory.json'),JSON.stringify(inventory,null,2));\n}\nconst commands=[];\nasync function run(argv,cwd=root){const p=Bun.spawnSync(argv,{cwd,env:{...process.env,BUN_CONFIG_NO_AUTO_INSTALL:'1'}});const r={argv,cwd,exitCode:p.exitCode,stdout:p.stdout.toString(),stderr:p.stderr.toString()};commands.push(r);await Bun.write(join(root,'unit-state','commands.json'),JSON.stringify(commands,null,2));return r;}\nawait run(['git','rev-parse','HEAD']);await run(['git','cat-file','-t','933a5f5df924b2b089f410615f99af7851010643']);await run(['git','ls-tree','-r','933a5f5df924b2b089f410615f99af7851010643','committed-inputs/']);\nawait run(['git','-C',pkg,'rev-parse','HEAD']);await run(['bun','--version']);\nconst store=join(root,'unit-state','store');const cli=join(pkg,'skills/poteto-mode/scripts/orch/orch.ts');\nawait run(['bun','--no-install',cli,'--store',store,'--json','init']);\nfor(const p of ['orders.json','dashboard.mjs','forge.json'])await copyFile(join(root,'committed-inputs',p),join(root,'unit-state',p));\nconst denied=join(root,'unit-state','denied-write');await mkdir(denied,{recursive:true});await chmod(denied,0o555);\ntry{await run(['bun','--no-install','-e','await Bun.write(process.argv[1], \"probe\")',join(denied,'probe.txt')]);}finally{await chmod(denied,0o755);}\nconst log=join(root,'unit-state','decisions.tsv');\nawait run(['bun','--no-install','-e','const r=Bun.spawnSync(process.argv.slice(1));process.stdout.write(r.stdout);process.stderr.write(r.stderr);process.exit(r.exitCode) ','bash',join(pkg,'skills/show-me-your-work/scripts/log.sh'),log,'frame','Stop helper dependent operations','Bootstrap rejects missing installed metadata',join(root,'unit-state','commands.json'),'blocked']);\nconsole.log(JSON.stringify({commands:commands.length,init:commands.find(c=>c.argv.includes('init')),denied:commands.find(c=>c.argv.includes(join(denied,'probe.txt'))),log:await readFile(log,'utf8')},null,2));\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/commands.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/commands.json",
      "sha256": "b096702cafa112fce6eb89d33ff24542c24f7dbc5a2b339372d70e2ce3364d99",
      "bytes": 18149,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "[\n  {\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 0,\n    \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"git\",\n      \"cat-file\",\n      \"-t\",\n      \"933a5f5df924b2b089f410615f99af7851010643\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 0,\n    \"stdout\": \"commit\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"git\",\n      \"ls-tree\",\n      \"-r\",\n      \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"committed-inputs/\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 0,\n    \"stdout\": \"100644 blob 7b2943d8f74232b5f67dec8de8f163493defba64\\tcommitted-inputs/README.md\\n100644 blob 9a1d5902c9655a7514ee1d8c6bd7ec965f5d9ae0\\tcommitted-inputs/additional-v2/README.md\\n100644 blob c546a33ca727df67fa23c6bf05a054c134b849d6\\tcommitted-inputs/additional-v2/caller-migration/api.mjs\\n100644 blob 9202640ebda45cf335880590ded13be807b5a380\\tcommitted-inputs/additional-v2/caller-migration/contract.test.mjs\\n100644 blob 10c90faeea94a7268d23d3a6c3b692d1ede634ce\\tcommitted-inputs/additional-v2/caller-migration/notification.mjs\\n100644 blob 9c60cc1638be88a3720bcbfe21ed859ebfbba4d5\\tcommitted-inputs/additional-v2/caller-migration/package.json\\n100644 blob 18528bf331a1909fe505c698a3b232106f948315\\tcommitted-inputs/additional-v2/caller-migration/profile.mjs\\n100644 blob 1459965b78833643a93cc3e47a6f828be8ac44ae\\tcommitted-inputs/additional-v2/caller-migration/scope.md\\n100644 blob f71f6cc59bc2bebfb64aca2255e3a41b1e0f5735\\tcommitted-inputs/additional-v2/dead-path/acceptance.json\\n100644 blob c4895bb4ac56b16b91d9a7b3e6fffb3064de702c\\tcommitted-inputs/additional-v2/dead-path/caller.mjs\\n100644 blob 2c487986f7d4383207933af197c25f0ae2400a4e\\tcommitted-inputs/additional-v2/dead-path/contract.test.mjs\\n100644 blob 19545b94e9904dffebe205d1591adf959e8a2061\\tcommitted-inputs/additional-v2/dead-path/duplicate-reference.md\\n100644 blob c0ad602a382b72eb13c0f3226e38eab9c4b8722e\\tcommitted-inputs/additional-v2/dead-path/handler.mjs\\n100644 blob 82270bff3a61f39676f8f8bfcc4e0c27e3e9bb56\\tcommitted-inputs/additional-v2/dead-path/instructions.md\\n100644 blob 0ca4d77dec291e417921bddc272efd206b756a36\\tcommitted-inputs/additional-v2/dead-path/scope.md\\n100644 blob fac140dcd4dd7a027375bd80f41a602d9844c175\\tcommitted-inputs/additional-v2/empty-function/acceptance.json\\n100644 blob 97fbf2c075a68fa2c5786122fc0c283968df8b72\\tcommitted-inputs/additional-v2/empty-function/contracts.test-d.ts\\n100644 blob 9ee56f1090a4b3ad3bb799e0f56e8faa0172e1c3\\tcommitted-inputs/additional-v2/empty-function/fixture-data.mjs\\n100644 blob 0e740b6ac8a80714da33f2a7290eac98b5171b9e\\tcommitted-inputs/additional-v2/empty-function/subject.mjs\\n100644 blob 6da54f9bd65cfce177783a4e5a3063354157d725\\tcommitted-inputs/additional-v2/empty-function/table-relations.test.mjs\\n100644 blob 1050af5dc0a3e23925f52db501cf875bc60ca8bb\\tcommitted-inputs/additional-v2/empty-function/types.ts\\n100644 blob cda40a8b4dd4ae37903caece4686d4042f8cffc6\\tcommitted-inputs/additional-v2/empty-function/weak.test.mjs\\n100644 blob 405578c6fa7703d83ba933b7dd42b726586f4ae1\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js\\n100644 blob 9b6a918a979d9021b48678f9f3d9eecdd7c88a89\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js\\n100644 blob 4fe83ea691a4c0b38e4b3c73e40fc13ce692ef36\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js\\n100644 blob a1f80ae82de510e389502484641f4fffa790a55b\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js\\n100644 blob 72453a759d8835485c8dc4b88fa401ffcf70e9c3\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js\\n100644 blob 7aae764c3870ba299beb14645ef1b2354ec40454\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js\\n100644 blob 88d1eb3d9c937bb8799d29736c7afec44826c4c8\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js\\n100644 blob e7a7c29356624b97ee6c73cc58fae51abc54018f\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js\\n100644 blob 32f74320895732c83921744ea81e810a0115adb1\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js\\n100644 blob 8665c638230c1bb64f08b176a03e7e1b5422d724\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js\\n100644 blob 5525d077d948d1b4fb550e061d8171e60e9de7b1\\tcommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js\\n100644 blob bcb280c32c881b1c0b74d1fc5cf2664a2d6b8c8e\\tcommitted-inputs/additional-v2/preparation-checks.json\\n100644 blob 1c0500eec0401982665cb541864ff6320b67c9e8\\tcommitted-inputs/additional-v2/scenario-map.json\\n100644 blob 9c66f2ff411e3699601530033f897588a4a272e0\\tcommitted-inputs/additional-v3/README.md\\n100644 blob cedfeef97f795ae0b2950b87c4674c9f12ff81c2\\tcommitted-inputs/additional-v3/installed-compiler-paths.json\\n100644 blob f76345a7b16132c0288357608bea53fe11ae2f6f\\tcommitted-inputs/additional-v3/invalid-input/adapter.ts\\n100644 blob 46f0d86bc6af38ba0950084e6e41aa1df8df73a6\\tcommitted-inputs/additional-v3/invalid-input/boundary.test.mjs\\n100644 blob f260814422fbba355c848a5f0d86088724ae557b\\tcommitted-inputs/additional-v3/invalid-input/domain.ts\\n100644 blob 5cc88b4f95cc0a74307141192afa3ac49e06a39f\\tcommitted-inputs/additional-v3/invalid-input/internal-caller.ts\\n100644 blob 930ef47f2ee92bfe8802f81a10ac165b11924485\\tcommitted-inputs/additional-v3/invalid-input/internal-guards.test.mjs\\n100644 blob 5ee9c3a6139991b5af3914ffb43d2d0478ffe758\\tcommitted-inputs/additional-v3/invalid-input/scope.md\\n100644 blob 11ea7d3f87832ad0549684e91783759853bdc20f\\tcommitted-inputs/additional-v3/invalid-input/tsconfig.json\\n100644 blob c6781743d40033376ef0e63e9892777d256abc0a\\tcommitted-inputs/additional-v3/migration-end-state/consumer.ts\\n100644 blob cc3771e12457657bd4c8cf2465b99b9502b045af\\tcommitted-inputs/additional-v3/migration-end-state/contract.test.mjs\\n100644 blob 5f4abb242a3f9f33b1b4e6a45590e953f6320703\\tcommitted-inputs/additional-v3/migration-end-state/index.ts\\n100644 blob 56eed2d7c3470af0b36d9e4828f0412555714a9a\\tcommitted-inputs/additional-v3/migration-end-state/legacy.ts\\n100644 blob bf7b333fe000950f989a236727bb10ba1834a848\\tcommitted-inputs/additional-v3/migration-end-state/target.md\\n100644 blob 11ea7d3f87832ad0549684e91783759853bdc20f\\tcommitted-inputs/additional-v3/migration-end-state/tsconfig.json\\n100644 blob 0a33272d8003f1577be62764807ad74ca322a8da\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js\\n100644 blob dd90c43cb93fd8c6a954e960a0c7682afca4f6f2\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js\\n100644 blob c10806768f631f145607c93c12fb6355a04970cc\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js\\n100644 blob 78e00ad7233515a71f3ee9cd1795473e64bb9dc4\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js\\n100644 blob bc7342c6c7a18e64473d7ffbf316b73e8f91bace\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js\\n100644 blob 5d700a68e64c8d59687b50efe7b34bed579c0025\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js\\n100644 blob a422f40c227cb74e9bae71b0410123fd7f1b69b0\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js\\n100644 blob 2cd9a9386244db9b80a3866aa1fa67eb3d4b719d\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js\\n100644 blob 2cd9a9386244db9b80a3866aa1fa67eb3d4b719d\\tcommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js\\n100644 blob 9457425c207c290a27d187980cc688c7913d6c87\\tcommitted-inputs/additional-v3/preparation-checks.json\\n100644 blob 16a37ab7a12f88b28dfa30813a63ae6d9976f8f4\\tcommitted-inputs/additional-v3/repeatable-change/manifests/admin/audit.json\\n100644 blob 40f2b70aa0c28fe7249ddad0d6c7d3dc5b4b9649\\tcommitted-inputs/additional-v3/repeatable-change/manifests/admin/team.json\\n100644 blob 481a14f2c9dabdf7c773a4319ac507b73c0cca1f\\tcommitted-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json\\n100644 blob cfb4ee9a9c7e05a6a27bd4fead1ac4a132114587\\tcommitted-inputs/additional-v3/repeatable-change/manifests/core/export.json\\n100644 blob 4be751bf4ca2c5022e0b7a94c2df3f476682965f\\tcommitted-inputs/additional-v3/repeatable-change/manifests/core/search.json\\n100644 blob b920892479eb5f0a538711cae59b7079aa62a512\\tcommitted-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json\\n100644 blob 5475af1af2735ec07911da417b1e3bdfb058eb2d\\tcommitted-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json\\n100644 blob 427346635cb318aa6e157a53243f71dc5b6dd643\\tcommitted-inputs/additional-v3/repeatable-change/notes.txt\\n100644 blob b24fce39ed6ae22ea80150dfd3945f0cee82845d\\tcommitted-inputs/additional-v3/repeatable-change/scope.md\\n100644 blob c903b7d1d9b2cb036d3da59ff740e886f1079e43\\tcommitted-inputs/additional-v3/scenario-map.json\\n100644 blob 0c23547554f3f2ee0469e02252aeb952e67ecef3\\tcommitted-inputs/additional/README.md\\n100644 blob fa3a9c1e97b92414d641b5e2d1a0612cdaf0c0d5\\tcommitted-inputs/additional/cache/README.md\\n100644 blob fe42ffc8e5297a7768dacddf2ef2e5e9f0361a53\\tcommitted-inputs/additional/cache/cache.mjs\\n100644 blob 574c28047d03b1ef6b8a71c20d808cbb600e3d16\\tcommitted-inputs/additional/cache/caller.mjs\\n100644 blob 8d5541ae98204e3ebb75df3d67e294246bd3afce\\tcommitted-inputs/additional/cache/invalidation.diff\\n100644 blob 5cf6cf1070314209c53799865c1509decf46a79c\\tcommitted-inputs/additional/cache/manifest.json\\n100644 blob a16b46c08c9139572727d1ed1c6962ad64532cde\\tcommitted-inputs/additional/cache/probe.mjs\\n100644 blob 5792df7c0cc883eec6101eac64c2bd49095700e2\\tcommitted-inputs/additional/cache/vendor/disposer-v1.mjs\\n100644 blob db8b8e8684bd11aa501d47470b47ec3840185306\\tcommitted-inputs/additional/corpus/records.jsonl\\n100644 blob c4895bb4ac56b16b91d9a7b3e6fffb3064de702c\\tcommitted-inputs/additional/dead-path/caller.mjs\\n100644 blob 19545b94e9904dffebe205d1591adf959e8a2061\\tcommitted-inputs/additional/dead-path/duplicate-reference.md\\n100644 blob c0ad602a382b72eb13c0f3226e38eab9c4b8722e\\tcommitted-inputs/additional/dead-path/handler.mjs\\n100644 blob 82270bff3a61f39676f8f8bfcc4e0c27e3e9bb56\\tcommitted-inputs/additional/dead-path/instructions.md\\n100644 blob 5a9bc364c691dfdbd29d17dc59dbafbcc2323999\\tcommitted-inputs/additional/dead-path/scope.md\\n100644 blob f8437955da056bd300a92c4e8c54a6035ad6d010\\tcommitted-inputs/additional/history/capsule.json\\n100644 blob f65473bc56e0513fa8a6d2e9989205fb504b0ad9\\tcommitted-inputs/additional/history/history.json\\n100644 blob d56a276fa6706ad0062e4cd9d1982a79c5dc6c88\\tcommitted-inputs/additional/history/jay-mode.md\\n100644 blob 59c8308e9dc7d919c949db50fbc0e666d28686c3\\tcommitted-inputs/additional/history/shared-records.json\\n100644 blob fbe5afd39493585d8ebc7c13f52f322159af2a2b\\tcommitted-inputs/additional/invoice/adapter.mjs\\n100644 blob 165f88df3f98fde1286768d02e51fd48cc97aeff\\tcommitted-inputs/additional/invoice/calculator.mjs\\n100644 blob bc0cb0f5dc3825b6989d584ca7f72a0a9d5ce699\\tcommitted-inputs/additional/invoice/controller.mjs\\n100644 blob 474538b9c93322a7053089ff2681649480c648f6\\tcommitted-inputs/additional/invoice/decision.md\\n100644 blob 1a5880627909c36081aa9379097a389a5a63f9fd\\tcommitted-inputs/additional/invoice/exporter.mjs\\n100644 blob e865728e3cadd004eca2acf7f9c10b66c9f97c51\\tcommitted-inputs/additional/invoice/facade.mjs\\n100644 blob 5b61f9ec23eb2a05bd3872f499212e2720da7e19\\tcommitted-inputs/additional/invoice/formatter.mjs\\n100644 blob b0ee61462a20feb5ddfd1074643cb332ebb26300\\tcommitted-inputs/additional/legal-header/source.diff\\n100644 blob d1c045adfd2b14622977192f72b682c0ca615ff5\\tcommitted-inputs/additional/legal-header/source.mjs\\n100644 blob c546a33ca727df67fa23c6bf05a054c134b849d6\\tcommitted-inputs/additional/migration/api.mjs\\n100644 blob 7fd32e388b0d2176c7ea92e119485fec1ae7d9d9\\tcommitted-inputs/additional/migration/contract.mjs\\n100644 blob 10c90faeea94a7268d23d3a6c3b692d1ede634ce\\tcommitted-inputs/additional/migration/notification.mjs\\n100644 blob 18528bf331a1909fe505c698a3b232106f948315\\tcommitted-inputs/additional/migration/profile.mjs\\n100644 blob 75ea417837bc5c894fbb6985592a11980cdc1b94\\tcommitted-inputs/additional/migration/scope.md\\n100644 blob 31fba05d22dd3c0842d7ec3de8324d9484099e2e\\tcommitted-inputs/additional/scenario-map.json\\n100644 blob 0cf58510e3ef5b223758c1eb208562aff569a450\\tcommitted-inputs/additional/types/README.md\\n100644 blob 66d916fb34e1d541fb5eaa4b8bb9d814660ac061\\tcommitted-inputs/additional/types/boundary.ts\\n100644 blob 1bc455938d149a5a73454723bb793e8045eb709e\\tcommitted-inputs/additional/types/context.ts\\n100644 blob 92e482b756144714545be37621de0998854ca753\\tcommitted-inputs/dashboard.mjs\\n100644 blob deeeace8830b688700c402b82f1af325b2510416\\tcommitted-inputs/forge.json\\n100644 blob 21d29ba76826ac4aaa9c62fecf8257c6c706d831\\tcommitted-inputs/history.json\\n100644 blob 411a960069aea2da2bc8fba961e4b563cfe794f1\\tcommitted-inputs/invoice.mjs\\n100644 blob 43dcd6eeb8a720a091045ba106a0a88082fda50f\\tcommitted-inputs/orders.json\\n100644 blob d851a9820a91b07413c281389c430a9b177438a8\\tcommitted-inputs/runtime.mjs\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"git\",\n      \"-C\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts\",\n      \"--store\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/store\",\n      \"--json\",\n      \"init\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts:20:1\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"await Bun.write(process.argv[1], \\\"probe\\\")\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/denied-write/probe.txt\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"1 | await Bun.write(process.argv[1], \\\"probe\\\")\\n              ^\\nEACCES: permission denied, open '/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/denied-write/probe.txt'\\n    path: \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/denied-write/probe.txt\\\",\\n syscall: \\\"open\\\",\\n   errno: -13,\\n    code: \\\"EACCES\\\"\\n\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/[eval]:1:11\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"const r=Bun.spawnSync(process.argv.slice(1));process.stdout.write(r.stdout);process.stderr.write(r.stderr);process.exit(r.exitCode) \",\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/decisions.tsv\",\n      \"frame\",\n      \"Stop helper dependent operations\",\n      \"Bootstrap rejects missing installed metadata\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/commands.json\",\n      \"blocked\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12\",\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/unit-state/csv-audit.assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/csv-audit.assignment.json",
      "sha256": "da232876997386764fee038fc5275572f691d9eb9af3b6474cdb9ba5d8f2ad8c",
      "bytes": 527,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "{\n  \"id\": \"unit-state-csv-audit-v1\",\n  \"scope\": [\n    \"Read copied dashboard.mjs and orders.json; produce audit.json only\"\n  ],\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"outputOwner\": \"unassigned-csv-audit\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/csv-audit\",\n  \"role\": \"poteto-agent\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"dispatch\": \"blocked before spawn by helper initialization\"\n}"
    },
    {
      "path": "fixtures/batch-12/unit-state/csv-audit.brief.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/csv-audit.brief.md",
      "sha256": "c6d67e542e01e6312a8e999092bed7fa3d7d02b19010e414a854b42b74487f5c",
      "bytes": 3581,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\nGOAL         Inspect csv-audit behavior in the committed fixture without editing application code.\nSCOPE        Only /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/csv-audit/audit.json may be written; no other files or shared store.\nCONTEXT      Input 933a5f5df924b2b089f410615f99af7851010643; copied dashboard.mjs and orders.json in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/csv-audit. Package freeze supplied f4623636a287bea2aa79c4b2234a53d20a5f193c, not authenticated by installed tree.\nACCEPTANCE   Include exact input revision, actual inspected literal values and method.\nVERIFY       bun --no-install -e with dynamic import of copied module and fixture JSON; retain actual command and result.\nTIMEBOX      One foreground inspection, stop on prerequisite error.\nFORBIDDEN    No gt, rebase, commits, config, installs, live services, external writes or out-of-scope fixes.\nREPORT       Assignment id; worker id if observed; input SHA; head SHA; no PR; artifacts; actual commands; verdict; deviations; follow-ups.\nSTANDING\n1. Use only the installed pstack-openai 0.1.0 root and case-owned fixture inputs.\n2. Read full mode and applicable direct contracts before dependent work.\n3. Input revision is 933a5f5df924b2b089f410615f99af7851010643; reject any assignment result at another revision.\n4. Write only the immutable assignment's isolated output path; coordinator alone owns bookkeeping.\n5. No commits, git configuration changes, gt, rebase, push, PR, merge, external messages, installs or schedules.\n6. Requested model and effort remain separate from observed values; unexposed values are unknown.\n7. Return identity, exact revision, artifacts and actual method outputs; no inferred completion from labels.\n8. Keep stale, cancelled, late and partial results quarantined; salvage needs a fresh assignment.\n9. No remote placement, nesting, background wake, independent verifier or different-family claims without observations.\n10. Missing SHA or method permits one inspected retry; source failures permit at most two; denied operations never retry into success.\n11. Stop tree-wide refills on invalid upstream input; preserve a terminal handoff.\n12. No stacker or babysitter starts until real stack-owner metadata and a pinned frontier generation exist.\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/decisions.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/decisions.tsv",
      "sha256": "e676aeef8cd397ddca7dfd7a2488a42201840d6a37165162a361566ef732ec82",
      "bytes": 255,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T08:25:12Z\tframe\tStop helper dependent operations\tBootstrap rejects missing installed metadata\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/commands.json\tblocked\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/filter-audit.assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/filter-audit.assignment.json",
      "sha256": "ec982e9d74cadc9aef44a20ff951fb95c5225ad2c9c708e16c74a19633d2d98a",
      "bytes": 536,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "{\n  \"id\": \"unit-state-filter-audit-v1\",\n  \"scope\": [\n    \"Read copied dashboard.mjs and orders.json; produce audit.json only\"\n  ],\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"outputOwner\": \"unassigned-filter-audit\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/filter-audit\",\n  \"role\": \"poteto-agent\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"dispatch\": \"blocked before spawn by helper initialization\"\n}"
    },
    {
      "path": "fixtures/batch-12/unit-state/filter-audit.brief.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/filter-audit.brief.md",
      "sha256": "e955fa501aa24719e67f4a6ef9dbd92776317e14533e800386fc5a089de2036a",
      "bytes": 3590,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\nGOAL         Inspect filter-audit behavior in the committed fixture without editing application code.\nSCOPE        Only /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/filter-audit/audit.json may be written; no other files or shared store.\nCONTEXT      Input 933a5f5df924b2b089f410615f99af7851010643; copied dashboard.mjs and orders.json in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/units/filter-audit. Package freeze supplied f4623636a287bea2aa79c4b2234a53d20a5f193c, not authenticated by installed tree.\nACCEPTANCE   Include exact input revision, actual inspected literal values and method.\nVERIFY       bun --no-install -e with dynamic import of copied module and fixture JSON; retain actual command and result.\nTIMEBOX      One foreground inspection, stop on prerequisite error.\nFORBIDDEN    No gt, rebase, commits, config, installs, live services, external writes or out-of-scope fixes.\nREPORT       Assignment id; worker id if observed; input SHA; head SHA; no PR; artifacts; actual commands; verdict; deviations; follow-ups.\nSTANDING\n1. Use only the installed pstack-openai 0.1.0 root and case-owned fixture inputs.\n2. Read full mode and applicable direct contracts before dependent work.\n3. Input revision is 933a5f5df924b2b089f410615f99af7851010643; reject any assignment result at another revision.\n4. Write only the immutable assignment's isolated output path; coordinator alone owns bookkeeping.\n5. No commits, git configuration changes, gt, rebase, push, PR, merge, external messages, installs or schedules.\n6. Requested model and effort remain separate from observed values; unexposed values are unknown.\n7. Return identity, exact revision, artifacts and actual method outputs; no inferred completion from labels.\n8. Keep stale, cancelled, late and partial results quarantined; salvage needs a fresh assignment.\n9. No remote placement, nesting, background wake, independent verifier or different-family claims without observations.\n10. Missing SHA or method permits one inspected retry; source failures permit at most two; denied operations never retry into success.\n11. Stop tree-wide refills on invalid upstream input; preserve a terminal handoff.\n12. No stacker or babysitter starts until real stack-owner metadata and a pinned frontier generation exist.\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/overview.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/overview.md",
      "sha256": "7c76b7a68b358460e449990a590cacad7894ad5d5deb70e83cd7bb3fcb1de0bf",
      "bytes": 400,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "# Append-only program overview\n\n1. Framed two inspection tracks at exact input revision. Full done predicate requires both units landed with current behavioral verdicts.\n2. Actual orch init failed setup-required before initialization. Store, pilot, scaling and landing are blocked.\n3. Input fixture forge.json has symbolic heads and no authoritative local gt metadata; do not manufacture a frontier.\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/parent-checks.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/parent-checks.json",
      "sha256": "e8cf757f3190cdc343a739cb8e3436d7cfb03c7356a75000f3b61be0672cd4f5",
      "bytes": 1183,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "{\n  \"checks\": [\n    {\n      \"argv\": [\n        \"git\",\n        \"diff\",\n        \"--exit-code\",\n        \"933a5f5df924b2b089f410615f99af7851010643\",\n        \"--\",\n        \"committed-inputs\",\n        \"task-contracts.json\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"\",\n      \"stderr\": \"\"\n    },\n    {\n      \"argv\": [\n        \"git\",\n        \"rev-parse\",\n        \"HEAD\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"files\": [\n    {\n      \"id\": \"unit-state\",\n      \"path\": \"unit-state.result.md\",\n      \"exists\": true,\n      \"bytes\": 10062\n    },\n    {\n      \"id\": \"units-and-proof\",\n      \"path\": \"units-and-proof.result.md\",\n      \"exists\": true,\n      \"bytes\": 10912\n    },\n    {\n      \"id\": \"unknown-actual-model\",\n      \"path\": \"unknown-actual-model.result.md\",\n      \"exists\": true,\n      \"bytes\": 3396\n    },\n    {\n      \"id\": \"unsupported-selected-model\",\n      \"path\": \"unsupported-selected-model.result.md\",\n      \"exists\": true,\n      \"bytes\": 4310\n    },\n    {\n      \"id\": \"dependency-readiness\",\n      \"path\": \"dependency-readiness.result.md\",\n      \"exists\": true,\n      \"bytes\": 9862\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/unit-state/prepare-handoff.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/prepare-handoff.mjs",
      "sha256": "471933c5bfae9a6f50312549deefcc19871eca329194775409b0baf05d5cb1cc",
      "bytes": 4521,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "import {join} from 'node:path';\nimport {mkdir,copyFile,readFile} from 'node:fs/promises';\nconst root=process.cwd(),dir=join(root,'unit-state'),pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst sha='933a5f5df924b2b089f410615f99af7851010643';\nconst orders=`1. Use only the installed pstack-openai 0.1.0 root and case-owned fixture inputs.\\n2. Read full mode and applicable direct contracts before dependent work.\\n3. Input revision is ${sha}; reject any assignment result at another revision.\\n4. Write only the immutable assignment's isolated output path; coordinator alone owns bookkeeping.\\n5. No commits, git configuration changes, gt, rebase, push, PR, merge, external messages, installs or schedules.\\n6. Requested model and effort remain separate from observed values; unexposed values are unknown.\\n7. Return identity, exact revision, artifacts and actual method outputs; no inferred completion from labels.\\n8. Keep stale, cancelled, late and partial results quarantined; salvage needs a fresh assignment.\\n9. No remote placement, nesting, background wake, independent verifier or different-family claims without observations.\\n10. Missing SHA or method permits one inspected retry; source failures permit at most two; denied operations never retry into success.\\n11. Stop tree-wide refills on invalid upstream input; preserve a terminal handoff.\\n12. No stacker or babysitter starts until real stack-owner metadata and a pinned frontier generation exist.\\n`;\nawait Bun.write(join(dir,'standing-orders.txt'),orders);\nconst fullRole=await Bun.file(join(pkg,'references/agent-prompts/poteto-agent.md')).text();\nfor(const [i,name]of ['filter-audit','csv-audit'].entries()){\n const out=join(dir,'units',name);await mkdir(out,{recursive:true});for(const p of ['orders.json','dashboard.mjs'])await copyFile(join(dir,p),join(out,p));\n const assignment={id:`unit-state-${name}-v1`,scope:['Read copied dashboard.mjs and orders.json; produce audit.json only'],inputRevision:sha,outputOwner:`unassigned-${name}`,isolatedOutputPath:out,role:'poteto-agent',retryCount:0,terminalStatus:'pending',evidenceLinks:[],dispatch:'blocked before spawn by helper initialization'};\n await Bun.write(join(dir,`${name}.assignment.json`),JSON.stringify(assignment,null,2));\n const brief=`${fullRole}\\nGOAL         Inspect ${name} behavior in the committed fixture without editing application code.\\nSCOPE        Only ${out}/audit.json may be written; no other files or shared store.\\nCONTEXT      Input ${sha}; copied dashboard.mjs and orders.json in ${out}. Package freeze supplied f4623636a287bea2aa79c4b2234a53d20a5f193c, not authenticated by installed tree.\\nACCEPTANCE   Include exact input revision, actual inspected literal values and method.\\nVERIFY       bun --no-install -e with dynamic import of copied module and fixture JSON; retain actual command and result.\\nTIMEBOX      One foreground inspection, stop on prerequisite error.\\nFORBIDDEN    No gt, rebase, commits, config, installs, live services, external writes or out-of-scope fixes.\\nREPORT       Assignment id; worker id if observed; input SHA; head SHA; no PR; artifacts; actual commands; verdict; deviations; follow-ups.\\nSTANDING\\n${orders}`;\n await Bun.write(join(dir,`${name}.brief.md`),brief);\n}\nconst support=['references/host-capabilities.md','references/model-roles.md','references/orchestration-contract.md','references/workflow-ownership.md','docs/testing/helper-setup.md'];\nlet bundle='';for(const p of support)bundle+=`\\n===== ${p} =====\\n${await Bun.file(join(pkg,p)).text()}\\n`;await Bun.write(join(dir,'support-readback.txt'),bundle);\nawait Bun.write(join(dir,'overview.md'),'# Append-only program overview\\n\\n1. Framed two inspection tracks at exact input revision. Full done predicate requires both units landed with current behavioral verdicts.\\n2. Actual orch init failed setup-required before initialization. Store, pilot, scaling and landing are blocked.\\n3. Input fixture forge.json has symbolic heads and no authoritative local gt metadata; do not manufacture a frontier.\\n');\nawait Bun.write(join(dir,'attempts.jsonl'),JSON.stringify({event:'initialization-blocked',assignmentIds:['unit-state-filter-audit-v1','unit-state-csv-audit-v1'],inputRevision:sha,reason:'Missing commander 14.0.0 installed metadata; no assignments dispatched',evidence:'commands.json'})+'\\n');\nconsole.log(await readFile(join(dir,'standing-orders.txt'),'utf8'));console.log(await readFile(join(dir,'attempts.jsonl'),'utf8'));\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/source-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/source-inventory.json",
      "sha256": "f733fedb5eb1da93350ffb3bbc2343667758c55bf0dbfefc1cba4fdc8025b449",
      "bytes": 5867,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "[\n  {\n    \"requested\": \"skills/poteto-mode/playbooks/orchestrate.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\",\n    \"bytes\": 24094,\n    \"sha256\": \"bd3d7d52f475effd6c0365125da3dccbef4c79a93be5cd0752a1bc71545e0adb\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\",\n    \"bytes\": 32329,\n    \"sha256\": \"cb03eedb91cea96b570af30a7af317c6aae6a47a321cff2e82af656141ab0f14\"\n  },\n  {\n    \"requested\": \"agents/poteto-agent.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\",\n    \"bytes\": 1221,\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/orch/orch.ts\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts\",\n    \"bytes\": 15539,\n    \"sha256\": \"be91b7bca8a6f100d23f97661e468997c1bf0adbd1a17c23b43fc7c19dfe60b3\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/orch/store.ts\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/store.ts\",\n    \"bytes\": 44659,\n    \"sha256\": \"09ecb0c39d20af47a281a0190e6d4182c3bda5da4937ff8f7c4f42ef21da2797\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/orch/orch.test.ts\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.test.ts\",\n    \"bytes\": 25179,\n    \"sha256\": \"8368ce0e099186d4c321891007de33dfd3668321dca97242efe80628e9d7fbf2\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/bootstrap.ts\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\",\n    \"bytes\": 1353,\n    \"sha256\": \"307cdd435542b6adb719e885b08028fbb0a1467a6dcfbb1297392af475abe03f\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/package.json\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/package.json\",\n    \"bytes\": 351,\n    \"sha256\": \"a49b034b183dcb5735ed948a91eaf76b7f24d6d9ba313704721ad1be7a5f434d\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/scripts/bun.lock\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bun.lock\",\n    \"bytes\": 6678,\n    \"sha256\": \"530b7fb6cba7f0b2a6cfc862dbcfe9020c333d45e7e0f448133006583ffdc1f2\"\n  },\n  {\n    \"requested\": \"skills/arena/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\",\n    \"bytes\": 7536,\n    \"sha256\": \"28ecec523bed9d58bc044fe5abc549fc18a7c9de8e5ee6a124f7331fb0200cad\"\n  },\n  {\n    \"requested\": \"skills/figure-it-out/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/figure-it-out/SKILL.md\",\n    \"bytes\": 5028,\n    \"sha256\": \"d139b438205b09e5ffa5e0af12ef61485965eab4e6322a5a23b97b98e220e33a\"\n  },\n  {\n    \"requested\": \"skills/show-me-your-work/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/SKILL.md\",\n    \"bytes\": 8456,\n    \"sha256\": \"3c4f05ffecc162b6ae376b7adcf4e7d030c8dfc65a7f26f8519f2c1544c3b98b\"\n  },\n  {\n    \"requested\": \"skills/show-me-your-work/scripts/log.sh\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"bytes\": 1717,\n    \"sha256\": \"fb47611cbb75ea17aa80cb4f8dbfc7978b8844450b0ce702961bdef65cbb1342\"\n  },\n  {\n    \"requested\": \"skills/show-me-your-work/references/decision-log-template.tsv\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/references/decision-log-template.tsv\",\n    \"bytes\": 38,\n    \"sha256\": \"6779378006a2f5225e8c06deb84f1d913fb532041ebbb6e50d94600bfe3f4b76\"\n  },\n  {\n    \"requested\": \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"bytes\": 2264,\n    \"sha256\": \"9ef714543b16665c68182e1b66beb22829fbc4b68e2ceb138db9858384c598ce\"\n  },\n  {\n    \"requested\": \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-encode-lessons-in-structure/SKILL.md\",\n    \"bytes\": 3348,\n    \"sha256\": \"aea2433d69ce9acefd75b825c0c60e1ee41934120c565e20046f88ab588f108d\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/playbooks/autonomous-run.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/autonomous-run.md\",\n    \"bytes\": 5428,\n    \"sha256\": \"d7a61255568f81fb8facddc8d8f5aaa710ce0407569175eccdf7dd050744ba1a\"\n  },\n  {\n    \"requested\": \"skills/poteto-mode/playbooks/babysit.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/babysit.md\",\n    \"bytes\": 13631,\n    \"sha256\": \"85883ceae3e4485fb00ed77b9337a48148bd0263ef045a6dc496761b7fa8fa39\"\n  },\n  {\n    \"requested\": \"skills/unslop/SKILL.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/unslop/SKILL.md\",\n    \"bytes\": 6015,\n    \"sha256\": \"195411d320b5b328f9f642baf59757ed19aaf0931c0838740e0aca273d538dc1\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/unit-state/standing-orders.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/standing-orders.txt",
      "sha256": "4351e8fa50d985ce1f56ac56d48ccdcb22e4304e50f3d5cf2e326e9f72816673",
      "bytes": 1231,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "1. Use only the installed pstack-openai 0.1.0 root and case-owned fixture inputs.\n2. Read full mode and applicable direct contracts before dependent work.\n3. Input revision is 933a5f5df924b2b089f410615f99af7851010643; reject any assignment result at another revision.\n4. Write only the immutable assignment's isolated output path; coordinator alone owns bookkeeping.\n5. No commits, git configuration changes, gt, rebase, push, PR, merge, external messages, installs or schedules.\n6. Requested model and effort remain separate from observed values; unexposed values are unknown.\n7. Return identity, exact revision, artifacts and actual method outputs; no inferred completion from labels.\n8. Keep stale, cancelled, late and partial results quarantined; salvage needs a fresh assignment.\n9. No remote placement, nesting, background wake, independent verifier or different-family claims without observations.\n10. Missing SHA or method permits one inspected retry; source failures permit at most two; denied operations never retry into success.\n11. Stop tree-wide refills on invalid upstream input; preserve a terminal handoff.\n12. No stacker or babysitter starts until real stack-owner metadata and a pinned frontier generation exist.\n"
    },
    {
      "path": "fixtures/batch-12/unit-state/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/supplied-input.json",
      "sha256": "09dd13188e9343271cf99a0eca2e74d1dfebf2d3c57f6629f6bb4ddd34f83ef2",
      "bytes": 6620,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "{\n  \"id\": \"unit-state\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/orchestrate.md\",\n    \"skills/poteto-mode/SKILL.md\",\n    \"agents/poteto-agent.md\",\n    \"skills/poteto-mode/scripts/orch/orch.ts\",\n    \"skills/poteto-mode/scripts/orch/store.ts\",\n    \"skills/poteto-mode/scripts/orch/orch.test.ts\",\n    \"skills/poteto-mode/scripts/bootstrap.ts\",\n    \"skills/poteto-mode/scripts/package.json\",\n    \"skills/poteto-mode/scripts/bun.lock\",\n    \"skills/arena/SKILL.md\",\n    \"skills/figure-it-out/SKILL.md\",\n    \"skills/show-me-your-work/SKILL.md\",\n    \"skills/show-me-your-work/scripts/log.sh\",\n    \"skills/show-me-your-work/references/decision-log-template.tsv\",\n    \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n    \"skills/poteto-mode/playbooks/autonomous-run.md\",\n    \"skills/poteto-mode/playbooks/babysit.md\",\n    \"skills/unslop/SKILL.md\"\n  ],\n  \"prompt\": \"Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.\",\n  \"requirements\": [\n    \"Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.\",\n    \"Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.\",\n    \"Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.\",\n    \"Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.\",\n    \"Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.\",\n    \"One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.\",\n    \"Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.\",\n    \"Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.\",\n    \"Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits.\"\n  ],\n  \"expectedFull\": \"Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.\",\n  \"expectedReduced\": \"Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.\",\n  \"expectedBlocked\": \"Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.\",\n  \"forbiddenClaims\": [\n    \"Structural checks or snapshot tests prove current caller host parity or real workers.\",\n    \"Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.\",\n    \"Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.\",\n    \"A truncated standing summary contains all standing orders.\",\n    \"An inbox notification or destructive drain without a persisted receipt proves inspected results.\",\n    \"Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.\",\n    \"The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.\",\n    \"Dead pid permits automatic force takeover or restart proves worker liveness.\",\n    \"Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.\",\n    \"Missing gt metadata can be replaced by a guessed authoritative frontier.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/orchestrate.json\"\n}"
    },
    {
      "path": "fixtures/batch-12/unit-state/todo.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/todo.md",
      "sha256": "de39c9da46e7e31368632b292f6f44b86ccc246a57d35f626096cdcb3a323f47",
      "bytes": 4047,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "# Orchestrate todo binding\n\nNo todo API is exposed. This authorized local Markdown file is the reduced binding. Steps below preserve the source text verbatim. This checklist was captured after the failed initialization during handoff consolidation, so it does not establish a pre-execution todo binding.\n\n\n1. **Frame.** State the done predicate as something countable (\"all 126 units merged, each verified at each current full head SHA with `unit-test-verified` or better\"). Quantify scope: units, rough effort, expected stacks, and the wall-clock budget. If one agent could finish inside that budget, stop here and run Autonomous run instead. Collapsing must not depend on another document being present. It means do the work directly in this session, plain workers where they help, verification inline, landing as you go, and none of the store, register, or pilot machinery below. Schedule landing against the budget. By roughly 70% of it, stop spawning and land what is verified. Name the tracks per project. A contested decomposition or one-way door goes through the arena skill before the pilot. Present the framing once. Reversible prep proceeds without waiting.\n2. **Initialize the runtime.** Check the helper prerequisites, then run `orch init`. Initialization creates bookkeeping files, not dependencies or workers. Open the trail via the show-me-your-work skill, write the standing orders before any spawn, and seed `frontier.json` from existing PRs with `orch frontier set --repo <repo-dir>`.\n3. **Pilot.** Push one unit through the whole path: brief, worker, verification, stack entry, ledger row, merge. The pilot exists to falsify the brief template, the verify recipe, and the unit size while that costs one agent instead of fifty. Fix the contract from pilot evidence before any fan-out. Scale the pilot to the unit. On programs of near-identical cheap units, the first unit is the pilot, run as a normal unit with its verify command inline, and fan-out starts the moment it lands. The dedicated pilot pipeline (separate verifier agent, audit gate) is for expensive or novel unit shapes, not for clone-units where a serialized pilot has nothing to falsify.\n4. **Scale.** Spawn a rolling window of workers up to the in-flight cap, refilling as children finish. Blocking batches pay the slowest child of every batch. Spawn track sub-coordinators only past the one-drain threshold in Roles. Recompute ready work after each drain. Relay upstream reports into downstream briefs. Keep sibling communication upward only. The sampled brief audit runs alongside the wave it samples and stops the next refill on failure, not the current one.\n5. **Drain.** Run the queue discipline below at every drain point.\n6. **Land.** Landing is continuous, never a terminal phase. Integration starts with the first verified unit and runs alongside the remaining waves. On heavy repos the stacker is a standing role from wave one, integrating as units verify. On repos where local git is cheap, the coordinator lands verified units itself per Roles. Keep the frontier green before upper-stack work. Stack safety governs. Advance `frontier.json` only on merge or reported new head SHAs.\n7. **Close.** Drain the final inbox, reconcile every spawned agent to a terminal row (done, abandoned, zombie-reconciled), confirm the predicate on the real artifact, confirm every landed PR has a verdict for its current head SHA, audit the trail per show-me-your-work including its cross-model review, encode recurring corrections into `preferences.md` or the brief template. Leave the store intact. It is the postmortem.\n\n\n## Actual state\n\n1. Frame recorded, predicate open.\n2. Initialization attempted, blocked by actual missing pinned dependency metadata.\n3. Pilot not run, initialization prerequisite failed and merge unauthorized.\n4. Scale not run, pilot prerequisite unmet.\n5. Drain not run, no operative helper or inbox.\n6. Land not run, no current verdict or authorization.\n7. Close not complete; terminal handoff saved with zero dispatched program children.\n"
    },
    {
      "path": "fixtures/batch-12/unit-state.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state.result.md",
      "sha256": "d338da2ceafc02a5bd14164fbfa92f007c4fd69db7078572b28a4ec94979d0a0",
      "bytes": 11148,
      "owners": [
        "grades-native-12.json#0"
      ],
      "text": "# unit-state\n\nThe program is blocked at its real initialization prerequisite. No orchestration store was initialized, no program worker was dispatched, and no unit landed. The requested full program was not completed.\n\n## Supplied input and source reads\n\nThe complete supplied prompt, requirements, expected branches and forbidden claims are preserved in `unit-state/supplied-input.json`. The supplied source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The installed exported directory has no Git metadata, so its commit could not be independently authenticated. Actual source bytes and hashes are in `unit-state/source-readback.txt` and `unit-state/source-inventory.json`. All 19 named files were read. The portable role file resolves from `agents/poteto-agent.md` to the user-named `references/agent-prompts/poteto-agent.md`. Additional direct capability, ownership, assignment, model and setup contracts are in `unit-state/support-readback.txt`.\n\nThe task input commit `933a5f5df924b2b089f410615f99af7851010643` was independently checked using `git cat-file -t`, `git rev-parse HEAD` and `git ls-tree -r`. It is a commit containing the synthetic inputs. It is distinct from package provenance. Output artifacts remain uncommitted. Copies of dashboard.mjs, orders.json and forge.json are case-owned synthetic inputs. The forge data has symbolic heads `fixture-base` and `fixture-head`, not full current PR SHAs or real stack-owner metadata.\n\n## Actual actions and output\n\n`unit-state/commands.json` preserves argv, cwd, exit code, stdout and stderr for eight real commands. `unit-state/capture.mjs` and `unit-state/prepare-handoff.mjs` are the Bun scripts that produced the local records. Bun reported version 1.4.2.\n\nThe operative invocation was:\n\n```text\nbun --no-install /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts --store /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/store --json init\n```\n\nIt exited 1 before opening a store. Its actual error was `Helper setup required` with ENOENT for `skills/poteto-mode/scripts/node_modules/commander/package.json`. Bootstrap requires installed commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. No dependency was installed, no historical snapshot was used, and store.ts was not imported directly to evade bootstrap. The bundled test suite was read but not executed because it contains fixture commits and Git configuration writes forbidden by this evaluation, as well as dependency-backed CLI tests.\n\nThe denied-write probe ran Bun.write inside a case-owned directory set to 0555. It exited 1 with EACCES. The directory mode was restored to 0755. This is an actual local filesystem permission denial induced for the trial. It does not establish that the session's writable root was denied. The test wrote no target file.\n\nA real decision row was appended through the installed log.sh, invoked by Bun, then read back. Its path is `unit-state/decisions.tsv`. It records the initialization blocker. The handoff overview and attempts are append-only local records, not orch store tables.\n\n## Standing orders, assignments and throughput\n\n`unit-state/standing-orders.txt` contains all 12 numbered standing orders without truncation. The two prepared briefs embed the complete portable poteto-agent prompt and the orders verbatim, and retain GOAL, SCOPE, CONTEXT, ACCEPTANCE, VERIFY, TIMEBOX, FORBIDDEN and REPORT fields. `filter-audit.assignment.json` and `csv-audit.assignment.json` pin exact input SHA and disjoint copied inputs/output directories. Their owner fields explicitly remain unassigned. They are preparation records, not dispatched assignments or real worker identities. Their original pending records have not been rewritten; `attempts.jsonl` records blocked dispatch separately.\n\nThe coordinator wrote no application code. The tracks are filter audit and CSV audit. Neither has landed work. Blocking first steps are bootstrap, authoritative frontier metadata and merge permission. Independent targets would be the two isolated unit directories. The coordinator-owned helper store is a real single-writer invariant. The smallest safe sequence is initialization, one pilot through verification and authorized landing, then a rolling window. Because initialization failed, the pilot did not run and scaling did not start. No different-family independent verifier was invented for a cheap unit.\n\n## Requested branches and variants\n\n| Branch or variant | Actual attempt or retained limit |\n| --- | --- |\n| Successful worker and pilot | Blocked before dispatch by failed init. No worker success receipt exists for this program. |\n| Stale result | No actual program result arrived. A stale result must fail identity/input/current-head checks; no synthetic pointer was labelled a real worker. |\n| Lost drain receipt | No inbox existed and no destructive drain ran. Recovery was not exercised. Without a persisted peek/readback and actual drain receipt, no result could be accepted. |\n| Changed head | No PR head is observable in synthetic forge input. Current-head verification and a new assignment after revision change remain blocked. |\n| Blocked verifier | Behavioral verification is blocked by missing operative store and real PR context. A typed blocked verdict would never count as a pass. |\n| Late zombie | No program child was spawned or cancelled, so there was no observed zombie or termination. A late partial would remain quarantined pending exact assignment and frontier reconciliation. |\n| Pending merge permission | Merge remains forbidden by the user. No permission gate was resolved and no landing attempted. The local handoff records the gate; no helper gate write is claimed. |\n| Stale lock | No store lock was created, inspected or taken over. Helper initialization blocks the dependent stale-lock exercise. No force was attempted; a dead PID alone would not authorize it. |\n| Workers unavailable | Scenario withholding only, preempted by the same initialization blocker. Native collaboration operations are exposed and were used for other isolated cases. No program worker call was made for this variant, and no unavailable-host claim is made. Required independence would remain blocked under withholding. |\n| Missing helper dependencies | Actual observed bootstrap rejection, exit 1. This blocks all dependent helper commands. |\n| Denied writes | Actual induced local EACCES probe, exit 1. No saved continuity is claimed for that denied directory. |\n| Wake unavailable | No persistent wake binding was registered or tested. Scheduling is forbidden. Foreground execution only; no unattended recovery claim. |\n| Unknown models | Native spawn receipts for other cases identify workers but expose no actual model. Program workers did not run; requested/actual program model fields are unobserved. No diversity claim. |\n\nThe four permitted drain boundaries remain end of critical section, track rollup, frontier watcher wake and before human report. No drain is asserted at any boundary because bootstrap did not permit queue operations. Peek receipts and readback do not exist, rather than fabricated empty receipts. Arrivals during a future drain must be preserved for the next batch. Every actual batch must classify landed, needs-verify, failed, zombie and noise only after artifact inspection outside the drain.\n\n## Frontier, verification and close counts\n\nThe unchanged full predicate is two landed units, each with inspected behavioral evidence at its current full head SHA, and final drain plus terminal reconciliation complete. It is not met. No authoritative generation-pinned frontier is available. There is no real stack-owner clone or observed gt metadata in the supplied input. No stacker or babysitter started. No PR links exist. Synthetic forge numbers are not real PRs.\n\n| Count | Observed value |\n| --- | --- |\n| Prepared units | 2 |\n| Program workers dispatched | 0 |\n| Program children requiring reconciliation | 0 |\n| Inspected accepted worker results | 0 |\n| Landed units / commits / PRs / merges | 0 / 0 / 0 / 0 |\n| Current verified PR heads | 0 |\n| Helper ledger or unit rows | Unavailable, store not initialized |\n| Abandoned executed units | 0 |\n| Blocked prepared units | 2 |\n\nThese are artifact and action counts, not fabricated output from `orch status` or `ledger summary`. A historical row would not verify a changed head. Exact `(PR, full current head SHA)` lookup, verifier precedence and artifact/method inspection must be enforced by the caller. The helper accepts arbitrary state strings and does not enforce SHA syntax, immutable assignment ownership, evidence existence, permissions or precedence. Type-check-only is insufficient for the requested behavioral work. Source failure retries are capped at two, missing SHA/method at one; no retry was made against the deterministic missing-dependency or denied-write errors.\n\n## Terminal handoff and attention\n\nThe intended store path is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/store`; it was not initialized. The real trail is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unit-state/decisions.tsv`. The partial handoff is this report, the complete prepared briefs, `overview.md` and `attempts.jsonl`. Those were written and read back locally. No automatic wake or pickup exists. A future authorized run must first recheck exact package pins and bootstrap, then inspect real stack-owner metadata before using the prepared CLI binding. No new setup or merge authorization follows from this handoff.\n\nreviewed by unknown\n\nThe scoped audit compared the decision row to the actual captured command record. No complete host transcript file or observed different-family trail reviewer is available, so complete transcript audit and cross-model review remain blocked. The full program scenario, drain recovery, current-head ledger checks, frontier generation and stale-lock handling remain unexecuted due to the named prerequisite. Local preparation establishes no worker or helper parity outcome.\n\nThe Separate Before Serializing Shared State principle kept prepared unit outputs disjoint and reserved bookkeeping for the coordinator. Encode Lessons in Structure kept exact-input records and deterministic prerequisite failure in reusable Bun capture scripts. Neither choice claims that workers or the blocked helper ran. Final parent input-preservation checks are in `unit-state/parent-checks.json`.\n\nThe source steps are preserved verbatim in `unit-state/todo.md`. That local checklist was captured during handoff consolidation after the failed init, and does not prove the required pre-execution todo timing. No dependent program step ran afterward.\n\nTiming limit. The detailed predicate, standing orders and immutable briefs were prepared as a terminal handoff after the initialization failure. They do not establish that a complete pre-pilot program frame or standing-order register was installed before the failed helper call. No worker dispatch or program acceptance followed.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-12/unit-state/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/forge.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/unit-state/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unit-state/source-readback.txt",
      "owner": "grades-native-12.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unit-state/support-readback.txt",
      "owner": "grades-native-12.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unit-state/units/csv-audit/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/units/csv-audit/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unit-state/units/filter-audit/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/units/filter-audit/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unit-state/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/forge.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/unit-state/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unit-state/source-readback.txt",
      "owner": "grades-native-12.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unit-state/support-readback.txt",
      "owner": "grades-native-12.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unit-state/units/csv-audit/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/units/csv-audit/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unit-state/units/filter-audit/dashboard.mjs",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unit-state/units/filter-audit/orders.json",
      "owner": "grades-native-12.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    }
  ],
  "globalLimits": [
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
