# codex: arena-walkthrough

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "arena-walkthrough",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-durable-02.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.",
  "caseDefinition": {
    "id": "arena-walkthrough",
    "sourcePaths": [
      "skills/arena/SKILL.md"
    ],
    "prompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.",
      "Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge."
    ],
    "expectedFull": "Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.",
    "expectedReduced": "Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.",
    "expectedBlocked": "Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.",
    "forbiddenClaims": [
      "Links or direct source reads prove installed discovery.",
      "Sequential roles are independent workers.",
      "An isolated helper snapshot proves this candidate or host passed.",
      "A resolution file, owner marker or upstream autonomy grants approval.",
      "Apply automatically accepts an update or refreshes a host."
    ],
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json"
  },
  "registry": {
    "caseId": "arena-walkthrough",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
    "sourcePaths": [
      "skills/arena/SKILL.md"
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
        "inspect-result"
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
    },
    "requiredMethod": "arena"
  },
  "attempts": [
    {
      "attemptId": "grades-native-06.json#6",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "arena-walkthrough",
      "status": "reduced-pass",
      "grade": {
        "caseId": "arena-walkthrough",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_13",
          "item_20",
          "item_28",
          "item_33"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Exact task Git input revision absent.",
          "Pre-dispatch immutable assignment events/full structured receipt absent."
        ],
        "review": "Reads README→Arena and uses two actual fresh candidate outputs and later judge, then selects/grafts and inspects synthesis. Initial inherited launch failure followed successful fresh contexts, not absent tool. Missing taskSHA/pre-dispatch event method receipt prevents full despite useful native comparison.",
        "responseArtifact": "fixtures/batch-06/arena-walkthrough.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.",
        "reducedExpected": "Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-06.json",
            "reviewedBy": "grade_contract_audit independent reviewer"
          }
        ]
      },
      "topLevelContext": {
        "limits": [
          "Root command JSONL and retained child-produced artifacts inspected. Worker summary transcriptions are not signed raw method receipts.",
          "Inherited-context thread-store failure followed fresh-context success must not be described as absent worker tools.",
          "TaskGit SHA missing in these baseline fixtures remains distinct from package source freeze.",
          "No actual PR/service/scheduler behavior credited from local replay programs.",
          "No exitreceipt needed to infer batch completion here: actual native turn.completed and final response exist; paused outer orchestrator not counted as case failure."
        ]
      },
      "response": {
        "text": "# arena-walkthrough\n\n## Supplied input\n\n> Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\n\nNamed source files and exact copied source bytes are retained in [arena-walkthrough/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-manifest.json) and [arena-walkthrough/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Navigation, frame and capability decisions\n\nRead installed README. It links docs/workflows/arena.md and that destination exists and was fully read. Read Arena and its capability, model-role, assignment and ownership contracts plus applied leaves. Source reads establish navigation, not a registered /arena command or installed-discovery pass. Installed package is visibly listed in this host's skill catalog, but source invocation was manual and no host registration command was tested.\n\nA local six-phase checklist replaces an unavailable todo operation. task.md requests two Markdown cache API proposals. The parent-only rubric has five criteria, caller clarity, state ownership, teardown correctness, failure handling and extension cost. Candidates did not receive the rubric. Frozen fixture input-manifest.json hashes to7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43. No exact task Git SHA exists. This missing concrete prerequisite prevents a full assignment-contract run; isolated comparison proceeds with that explicit reduction.\n\n## Fan out and inspect\n\nCandidate A's inherited-context spawn failed with invalid thread-store/no rollout. The actual error is preserved in worker-events.json. A fresh fork_turns none attempt under arena-a-v1 retry1 returned /root/arena_a_retry and produced a/proposal.md. Candidate B, /root/arena_b under arena-b-v1 retry0, produced b/proposal.md. Their outputs are disjoint and both were read end to end. SHA256 values are4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e and366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b.\n\nWorker requests inherited model/effort. Observed model and effort are unknown. No cloud-placement or diversity claim. Actual workers wrote only their assigned proposals according to inspected files and returns; no OS-enforced per-worker sandbox is claimed. Append-only immutable pre-dispatch assignment events were not fully persisted before dispatch, so later coordinator event transcription is not a complete structured method receipt.\n\n## Cross-judge, pick and graft\n\nOnly after both terminal candidates and full artifacts were inspected, fresh read-only /root/arena_judge received candidates plus rubric. judge.md retains its result and independently checked artifact hashes. Parent criterion scores match the judge, A2/2/2/1/2 and B2/2/2/2/2. These are proposal comparison scores, not host case grades. Choose B because it defines closed-before-disposal and owned invalidation in finally. Graft A staged migration, optional-chaining warning and deferred-error policy. Reject scheduling-dependent lifetime, raw-key consumer invalidation, placeholders and unjustified reference counts. Both converge on generation handles; the graft keeps one model.\n\n## Verify and actual output\n\nsynthesis.md is the resulting cache API proposal; synthesis-note.md records base, grafts, rejections and inspection. verification.json retains hashes and bounded parent textual review aids. The parent reviewed the real caller/vendor path and reproduced after-state failure and before-state completion in command-results.json. API implementation and proposed future regression checks did not run. Prove It Works changed the verification from trusting worker summaries to reading artifacts and actual probe output. Separate Before Serializing Shared State changed candidate ownership to disjoint paths. Laziness Protocol rejected reference counting. Redesign From First Principles kept ownership coherent. Unslop was applied to synthesis prose.\n\nSix phases were exercised with native candidates and a fresh judge. Exact task Git SHA, observed model diversity and a full structured method receipt remain unmet. A source read or local text assertion is not evidence those gates passed. No dependency, settings, Git history or external action was changed.\n",
        "artifact": {
          "path": "fixtures/batch-06/arena-walkthrough.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough.result.md",
          "sha256": "a80484ae5850eccc0940c33b3bc99c0dd10574911c55635575e4f7ce0c58a13c",
          "bytes": 6019
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-06.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-06.events.jsonl",
            "sha256": "29e250d426d7f6e1853f71ccc210620bd85774dbbfaa2645ed41e80fe5d27d0b",
            "bytes": 497874,
            "eventReferences": [
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "067f64069a80d6bee7ae8fdc112f1eea7455c1a4f54059494a780082448eec31"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c12abe4f5d18352075fa27322540432154741adccfe652ee2aa9d4abbdb6f8d4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2e4adcfd8b33b29e8507ed6a18a5c3a631eab90e0ec6aac17ca8f441a2815f2b"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d334f54d4bfc726c80daf9c513ab237a570be5e8d9d1d48810140dcac6251519",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 52,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f95634a991bdf83a520d38029a33cffd5c0c1d25553b2c7b58c0de0780830db8"
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "897622be432f98a936806993bfadfeaf44ae238d2155a8b6f7be5292d6d44677",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_33",
                "line": 60,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "353993c230c9b434d1046ae45f631f6084edf7f0aca8dd85ebdec20b93d227ca"
              },
              {
                "eventId": "item_33",
                "line": 61,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8fa578ef231b70734b6c4fbaa3d3be0e900ac49b4552e533139f7f5a3ab426ff",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_13",
            "item_20",
            "item_28",
            "item_33"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-06.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    },
    {
      "attemptId": "grades-native-durable-02.json#0",
      "order": 202,
      "gradeFile": "grades-native-durable-02.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "arena-walkthrough",
      "status": "pass",
      "grade": {
        "caseId": "arena-walkthrough",
        "host": "codex",
        "status": "pass",
        "execution": "workers",
        "rawTrace": "codex/durable-02.events.jsonl",
        "actualReadEventIds": [
          "item_15",
          "item_19",
          "item_23",
          "item_24"
        ],
        "actualExecutionEventIds": [
          "item_32",
          "item_35",
          "item_41",
          "item_77",
          "item_105"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "isolated-write",
          "execution",
          "review-outcome"
        ],
        "missing": [],
        "review": "README-linked workflow and complete Arena phases run with two native isolated candidates/rationales, terminal parent inspection, fresh later judge and verified synthesis/graft. Parent rubric remains withheld from candidates. CandidateB passes its own broader probe but misses literal disposal-before-invalidation; judge and parent correctly preferA rather than treating probe exit0 as contract equivalence.",
        "responseArtifact": "fixtures/durable-02/arena-walkthrough.result.md",
        "variantReview": [
          "Main independent candidate/terminal-inspection/fresh-judge/synthesis sequence supported by actual native order and inspected code, not receipt schema alone."
        ],
        "limits": [
          "Operative source files were read and byte-compared to f462 before later cache disappearance. plugin.json author/developer metadata differed, so whole installed package is not asserted byte-identical.",
          "At final check requested global0.1.0 orchestration-contract path is absent. Archived earlier byte-matched source supports review only; no successful final installed discovery is invented.",
          "Original source-copy Buffer serialization/read failures and later actual-byte correction remain historical.",
          "All observed native workers use gpt-6.1-sol medium: independence is observed, model diversity is not.",
          "Encrypted inter-agent history does not prove plaintext equality; readable assignments and native ids/artifact order are separately retained.",
          "Pending logical owners before spawn, coordinator-normalized method/resultMethod metadata and corrected terminal-event labels are explicit documentation limits."
        ],
        "evidence": [
          "fixtures/durable-02/arena-walkthrough/parent-check-a.json",
          "fixtures/durable-02/arena-walkthrough/parent-check-b.json",
          "fixtures/durable-02/arena-walkthrough/verification.json",
          "fixtures/durable-02/arena-walkthrough/graft-verification.json",
          "fixtures/durable-02/arena-walkthrough/method-receipt.json",
          "fixtures/durable-02/evidence/native/index.json",
          "fixtures/durable-02/evidence/observed-order.json",
          "fixtures/durable-02/evidence/freeze-comparison.json",
          "fixtures/durable-02/evidence/final-source-availability.json"
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "fullExpected": "Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note."
      },
      "topLevelContext": {
        "attempt": "durable-02",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Independent source/actual implementation/probe/native-order inspection. Successful original source reads are distinct from real later cache-path absence.",
          "No whole installed-tree identity, current discovery, model diversity or release-readiness acceptance follows from case full outcome."
        ]
      },
      "response": {
        "text": "# arena-walkthrough\n\nFollowed installed README to docs/workflows/arena.md, read it and required contracts, then ran Frame, Fan out, Cross-judge, Pick, Graft and Verify. Two distinct native candidate workers completed isolated artifacts and rationales. Parent read both fully after terminal completion and reran both probes before spawning a fresh read-only judge. Both parent and judge selected lifecycle-owned A. Parent adapted B remount coverage and documented rejected immediate invalidation/error policy. Synthesis and graft probes exited 0.\n\n## Supplied input\n\nThe complete supplied case is retained at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/supplied-input.json. Original fixture paths in that case were not used as mutable sources. Assignments used committed-inputs/ at verified task revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze is separately f4623636a287bea2aa79c4b2234a53d20a5f193c, version 0.1.0.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"arena-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge.\"\n    ],\n    \"expectedFull\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n    \"expectedReduced\": \"Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\"\n  },\n  \"caseId\": \"arena-walkthrough\",\n  \"baselineBatch\": \"batch-06\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\",\n  \"expectedFullUnchanged\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Follow README to Arena. Task: redesign local cache ownership so disposal can read its mounted value before invalidation without leaking global mutable cache state. Two candidates must use structurally distinct shapes (e.g. lifecycle-owned entry vs explicit value passed to disposal), each in an isolated owned directory with rationale. Keep 3-6 criterion parent rubric hidden until a fresh read-only judge starts after both candidates finish. Parent reads both, chooses/grafts/rejects and verifies synthesis with an adjacent evidence note.\",\n  \"missingPrerequisites\": [\n    \"Exact case SHA and two isolated writable candidates\",\n    \"Fresh read-only cross-judge after inspected terminal candidates\",\n    \"No model-diversity claim without actual observation\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}\n```\n\n## Actual response and integration\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/evidence-note.md\n\nParent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/2/2/2 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B correctly isolates ownership but invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's remount-before-disposal test into overlap.mjs without importing B's immediate invalidation or uncaught exception policy. A's completion promise provides an observable rejection channel. No code graft is needed from B because ownership separation converges but the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra candidate-cross-review failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge/result.md\n\nAssignment: `arena-walkthrough-judge`  \nInput revision: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nObserved model: unknown\n\n| Rubric criterion | A | B |\n|---|---:|---:|\n| Deferred disposal observes original mounted ready value before invalidation | 2 | 1 |\n| No shared mutable map; overlapping keys cannot corrupt ownership | 2 | 2 |\n| Repeat teardown and throwing report have explicit deterministic cleanup | 2 | 2 |\n| Caller clarity and extension cost: coherent small API with rationale | 2 | 2 |\n| **Total** | **8/8** | **7/8** |\n\n**Recommend A as the maintainable base.** Its lifecycle entry retains the value while disposal runs, invalidates after reporting settles, and returns one completion promise for repeated teardown. Synchronous throws and asynchronous report rejection both invalidate and reject that promise.\n\nB satisfies the broader functional interpretation: deferred disposal receives its original mount’s value despite cache invalidation. It **does not satisfy the literal temporal requirement** that disposal read the value *before invalidation*: `cache.invalidate()` runs synchronously, and `reportDisposed(value, report)` runs in the later microtask. Its partial credit recognizes correct value ownership and reporting, not compliance with that ordering. This divergence follows the two assigned shapes and should remain explicit.\n\nConcrete integration choices:\n\n- **Graft B’s remount-before-disposal probe into A.** It explicitly checks an old mount disposing after a new same-key mount exists.\n- **Keep A’s completion and rejection contract.** Callers must await or handle unmount’s returned promise; that API change needs documentation.\n- **Reject B’s immediate invalidation for this literal requirement.**\n- **Reject B’s uncaught microtask exception policy as the base.** Cleanup is deterministic, but errors lack A’s caller-owned completion channel.\n- Keep both rationales’ ownership limitation: keys no longer provide shared caching or deduplication.\n\nI read the withheld rubric, task, every file in both candidate directories, both parent-check JSON outputs, and the pinned vendored disposer via `git show`. Both recorded parent checks exited `0`; their probes establish their respective contracts, so passing B’s probe does not establish the required temporal ordering. No writes or fresh executions were performed.\n\n## Variants\n\nTwo structurally distinct seats were exercised. No main-trial dropout occurred. Worker failure variants belong to the separate candidate-cross-review case.\n\n## Native assignments and observations\n\n```json\n[\n  {\n    \"worker\": \"walk_a\",\n    \"workerId\": \"/root/walk_a\",\n    \"threadId\": \"01a143d7-73b6-7720-a571-5e2721ab03eb\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-32-35-01a143d7-73b6-7720-a571-5e2721ab03eb.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_a.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_a-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"walk_b\",\n    \"workerId\": \"/root/walk_b\",\n    \"threadId\": \"01a143d7-86dc-7322-acfa-254c3911d921\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-32-40-01a143d7-86dc-7322-acfa-254c3911d921.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_b.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_b-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"walk_judge\",\n    \"workerId\": \"/root/walk_judge\",\n    \"threadId\": \"01a143da-50c2-7fb1-ba82-cd043be4d224\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-35-43-01a143da-50c2-7fb1-ba82-cd043be4d224.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_judge.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_judge-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  }\n]\n```\n\nEach main candidate received its case task.md plus dispatch-a.txt or dispatch-b.txt and the exact revision. Boundary dispatches embed the complete architect runner prompt. Candidate rubric was held in the parent file and not included in fork_turns:none assignments. Judges were fresh threads after terminal inspection. Exact native calls, returned objects, worker command outputs, terminal returns and encrypted inter-agent messages are retained while this session runs in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/native/root.jsonl and the named worker JSONL files. Method receipt, append-only assignment-events, task files, inspected output snapshots and artifact hashes are in the case directory. Global integer ordering is derived from actual timestamped dispatch calls and task_complete events, retaining each source ordinal in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/observed-order.json. It is event ordering, not synthetic timing telemetry.\n\nAll requested models/efforts inherited the parent. Native turn_context records independently identify observed gpt-6.1-sol with medium effort for these workers. Their self-reports said unknown because those workers did not have that observation. Distinct threads establish native worker identities; the identical observed model does not establish model diversity. No model aliases were invoked or model selection rejection invented.\n\n## Actual command outputs and exit status\n\nThese are raw captured command objects for the case, rather than service success counters. Nested commands and initial failed attempts also remain in native raw tool outputs. rg exit 1 with empty output means no match for the recorded query.\n\n```json\n[\n  {\n    \"path\": \"arena-walkthrough/parent-check-a.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/candidates/a/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/graft-verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/synthesis/overlap.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS graft: remount before old deferred disposal completes\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/baseline.json\",\n    \"argv\": [\n      \"bun\",\n      \"committed-inputs/additional/cache/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 1,\n    \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/synthesis/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/parent-check-b.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/candidates/b/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS actual vendored disposer matches input revision and manifest digest\\nPASS cache invalidation is synchronous and repeatable\\nPASS deferred report reads captured value, double unmount reports once\\nPASS overlapping same-key mounts and remount before disposal stay independent\\nPASS report exceptions remain observable as uncaught deferred exceptions\\nAll 5 checks passed\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Permissions, package provenance and limits\n\nThe user authorized native isolated workers, local writes, persistence and command execution in this root. No external services/actions, installation, configuration, commits, pushes, schedules or publishing were performed. No approval was inferred from source narratives. A local Markdown checklist substitutes for an absent todo tool. The session exposes no direct skill-invocation API; complete loaded workflows were executed inline. Catalog entries and source reads are kept distinct from registered invocation discovery.\n\nInstalled package has no Git metadata. A separate readable source Git repository contains the requested freeze. The comparison of all 726 tracked source paths found all installed and byte-identical except plugin.json author/developer metadata. Operative skills, references, README and linked walkthrough match the freeze. See /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/freeze-comparison.json. Do not describe the entire installed package as byte-identical or transfer a prior host result to this run.\n\nIsolation uses distinct local directories and one assigned writer, not Git worktrees or an OS-enforced worker-specific filesystem boundary. Initial cache ownership reservations used pending seat owners before native IDs were returned; original reservation records remain, and resolved native owners are recorded in receipt/events. This is an assignment-contract documentation limit. Method/resultMethod objects in receipts are coordinator normalization of observed one-artifact attempts and workflow order; original worker results declare the string arena. They are not a claim that workers returned structured sample metadata. Main dispatches occurred as separate native calls; they were not one atomic multi-spawn call.\n\nRaw inter-agent payloads are encrypted by the host in durable history. They are retained exactly; no decryption is claimed. Main task/dispatch files preserve the full readable assigned work and exact SHA. Initial source evidence copies serialized Buffers as JSON; those copies were corrected from actual installed bytes after the problem was observed. Workers that encountered this read the real installed or frozen Git files instead. Native history preserves the earlier failed reads and coordinator script error.\n\nPersistence is an observed current-session write/readback. It does not establish unattended recovery or a later-session reload. No structural validator result is used as a host behavioral conclusion. Earlier ephemeral-session failures remain untouched.\n\n## Independent outcome inspection\n\nRead-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery.\n\n### Corrections and final source availability\n\nIndependent reviewer findings retained verbatim in each outcome-review.md. Corrections after review: candidate-stage workflow status in boundary synthesis was replaced with completed status and a separate completion-status.md; full-source-legacy-scan.json now covers every implementation TypeScript file. Assignment event terminal label is now terminal-completed, distinguishing completion from later parent inspection shown in raw history. Earlier event files are preserved in native command outputs.\n\nInstalled 0.1.0 orchestration-contract path was available during initial source reads and full byte comparison, but existsSync now returns false. No package update or deletion was performed by this task. Cause is unknown. Final-source-availability.json preserves that observation. Review used the archived byte-matched source copy. No current installed-discovery claim follows.\n\nThe selected cross-review implementation does not promise synchronous disposer-scheduling failure recovery. The exact pinned vendor queues a microtask; report failures are separately covered. No new implementation change was warranted for an unrequested dependency behavior.\n\n\n## Artifacts\n\nComplete paths and SHA-256 digests: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/artifact-manifest.json. Primary receipt: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/method-receipt.json. Actual synthesis: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis.\n",
        "artifact": {
          "path": "fixtures/durable-02/arena-walkthrough.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough.result.md",
          "sha256": "b1a04c9a9c6da501e490b38cbe73b7ee2a1637d331031bbaaff0557e37828d6a",
          "bytes": 27386
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/durable-02.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/durable-02.events.jsonl",
            "sha256": "4d587cea58e0e80605c5e42c687becaa08b1b0c6ba1cf520b7077e87bfe10641",
            "bytes": 504691,
            "eventReferences": [
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "588886fe0e2259224e2d5db52dc5b23c89d25f6477da119cf5907af08c79aaa0"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "44bb2746c8224c924c9668d45e23ca206fcf9246422395a30f49c8a143c13d1a",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "06ae944e948f2ad7550b1d4c499702d6a137be61977142e0097599ca8d24b7f1"
              },
              {
                "eventId": "item_19",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4629f6fcb67fd68ba7671a5f6aead814ece1e73d3f0fb51b9a1259b6656362ea",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7d0b1ca6e203ca72ac56f650ccbf7c143424ef6b5b5e4e87d963ed502334b97a"
              },
              {
                "eventId": "item_23",
                "line": 45,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "decf6fef3eb5876dfd97c10cf3ab08bcd244b195292d034eb26adb6d2b27f8f0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_24",
                "line": 46,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ad97b3112a39b941624f0dbe4e552a77f8e11f78e07705d30f62d55614c7693f"
              },
              {
                "eventId": "item_24",
                "line": 47,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4bb678831035ea7f4407ae50ce07c4b79834477c4e4bf62240e889929d45f0eb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_32",
                "line": 61,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cbfe7caf81b42a0477ff50917fc11222f6fe71f5c5258a51a7c1f07925724fad"
              },
              {
                "eventId": "item_32",
                "line": 62,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a9c49dc41b27cc27631338155c0cab278d078f2d6e6ab79fd69aa3ad40bb31cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_35",
                "line": 67,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a38de2969b27712f66c68f0238e84290c2b89c43fb2bf24f7daf8c5c405af680"
              },
              {
                "eventId": "item_35",
                "line": 68,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "de5593e3ef33779886a1fc6774919f0ba032f32e32c6c38fefb6606095582de0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_41",
                "line": 78,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7ee6d604d16036d57ff55de0413d02a241324b63a99066504322f794f3c1560c"
              },
              {
                "eventId": "item_41",
                "line": 79,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "965c99c6f1567905a74cf3ee3abd9775f93b38710ff0cad2ec87db38fa940558",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_77",
                "line": 147,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4c3b73b78e8ff5dce8206af356514008bf8af8c37ea03cdc1abf4c8a9440019f"
              },
              {
                "eventId": "item_77",
                "line": 148,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b3cae2d20e308e963c8f1569b3ebdfe0f1090747892098f4e81beb1e4ed95151",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_105",
                "line": 201,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ddfdac77d6ea7202f9857404a12f1c1e37c4935daefbb29d0d37d62a2778b2c3"
              },
              {
                "eventId": "item_105",
                "line": 202,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "79d154a46c0418cc46ef047619568d9aca2a75224ad234b58eb27eabd5ff9bf7",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/durable-02/arena-walkthrough/parent-check-a.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-a.json",
            "sha256": "1a45ff25e244821df754c00447a111c01db9c0e3ae738b1c522b640b2c849443",
            "bytes": 350
          },
          {
            "path": "fixtures/durable-02/arena-walkthrough/parent-check-b.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-b.json",
            "sha256": "62b8a97800150e890cdd5fea25f20796b2245366fe9d3830cce49678af82591b",
            "bytes": 594
          },
          {
            "path": "fixtures/durable-02/arena-walkthrough/verification.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/verification.json",
            "sha256": "c608e79c0b8dff7ba701617c5c70e3b626c99483eb9e7806ea7a7429e832b24f",
            "bytes": 347
          },
          {
            "path": "fixtures/durable-02/arena-walkthrough/graft-verification.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/graft-verification.json",
            "sha256": "3fc1bfc990555065e263b8b0f27d69695a80b536297a37743a04fe71c65f966a",
            "bytes": 278
          },
          {
            "path": "fixtures/durable-02/arena-walkthrough/method-receipt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/method-receipt.json",
            "sha256": "4f3c38b3e073eab35d367debf71b45106939ce5bbd832069cabe1e8e142cd192",
            "bytes": 5748
          },
          {
            "path": "fixtures/durable-02/evidence/native/index.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/native/index.json",
            "sha256": "c48fa085251a6ecb7262ed26084fc7cdded8ad6062be964e5bba8a755bdf2d92",
            "bytes": 6746
          },
          {
            "path": "fixtures/durable-02/evidence/observed-order.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/observed-order.json",
            "sha256": "e4f72ce5fe13cbc61604699894be9d08b39883a8a7fa5f9c5fb35f76c732cc08",
            "bytes": 219577
          },
          {
            "path": "fixtures/durable-02/evidence/freeze-comparison.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/freeze-comparison.json",
            "sha256": "f81d39c71f6b664456d8c423d9975b79653b080f3b2ac5d845c9ea6801cae6a1",
            "bytes": 148499
          },
          {
            "path": "fixtures/durable-02/evidence/final-source-availability.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/final-source-availability.json",
            "sha256": "1b22307231d8a40f600eb459a61044670a1925c8c49082dd98d75e9d8ff9ec35",
            "bytes": 153
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_15",
            "item_19",
            "item_23",
            "item_24"
          ],
          "actualExecutionEventIds": [
            "item_32",
            "item_35",
            "item_41",
            "item_77",
            "item_105"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/arena-walkthrough/a/proposal.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/a/proposal.md",
      "sha256": "4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e",
      "bytes": 7313,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache ownership and teardown proposal\n\nRecommend synchronous invalidation, with teardown callbacks retaining the value they own. Add an entry handle returned by `put` so a consumer can remove only its own entry. A cache lookup is a point-in-time lookup, not a lifetime guarantee.\n\n## Observed failure\n\nThe supplied after-state deletes an entry synchronously. In `caller.mjs`, unmount calls `subscription.dispose()` and then `invalidate(key)`. The exact vendored disposer schedules `onDispose` with `queueMicrotask` and returns immediately. The callback therefore runs after deletion and `get(key).ready` dereferences undefined.\n\nI ran `bun arena-walkthrough/input/probe.mjs` against the supplied files. It exited 1 and printed:\n\n    teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\n\nThe removed timer previously deferred deletion until after the disposal microtask. That ordering explains why this caller depended on the old behavior. I did not execute a restored before-state, so that comparison is based on source inspection. The local vendor file SHA256 matches `manifest.json`: `d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f`. This evidence concerns fixture-v1 only and establishes no public package behavior.\n\n## Proposed API contract\n\n| Operation | Contract |\n| --- | --- |\n| `put(key, value)` | Replace the current lookup entry and return an owned entry handle. Each put creates a fresh identity, even for the same value. |\n| `get(key)` | Return the current value or undefined. Missing entries are ordinary misses. The result grants no guarantee about later lookups. |\n| `handle.value` | Retain the exact value passed to this put, independent of lookup replacement or invalidation. |\n| `handle.invalidate()` | Immediately remove the lookup entry only if this handle is still current for its key. Return whether removal occurred. Repeated calls are harmless. |\n| `invalidate(key)` | Immediately remove whatever entry currently occupies the key and return whether removal occurred. Reserve this operation for code intentionally invalidating the current entry regardless of owner. |\n\nThe cache owns lookup membership. The consumer owns its subscription and the value reference needed during teardown. Removing an entry does not dispose subscriptions or mutate the value. A handle retains its value while consumers retain the handle. This proposal assumes ordinary JavaScript values as in the fixture; resource disposal requires a separate contract.\n\nFor `mount`, retain the handle returned by `put`. The disposal callback reports `handle.value.ready` instead of performing `get(key).ready`. Unmount schedules disposal once and invalidates through that handle. Guard unmount so repeated calls cannot queue duplicate reports. The pinned disposer itself does not provide idempotence.\n\nThis also handles overlapping mounts using the same key. If mount A is replaced by mount B before A unmounts, A reports its own value and its handle cannot delete B. A raw key-based invalidation would still delete B after fixing the missing lookup alone.\n\nThe retained reference is not a deep snapshot. Mutations to that object remain visible. If consumers require the final value of another owner instead, that is a different requirement and needs an explicit handoff. The fixture supplies no such requirement.\n\n## Errors and completion\n\nDo not turn the failed lookup into an optional-chain expression. That would suppress the exception while changing the report from true to undefined.\n\nCache operations contain no user callbacks. A missing or replaced entry makes `handle.invalidate()` return false. Define this as a normal result, not an error. Value validation belongs with the caller that understands `ready`.\n\nA report callback can still throw. Under the supplied disposer, that exception escapes from a microtask; a try/catch around unmount cannot catch it. Catch and route report failures inside the deferred callback through the application's existing error policy, or explicitly document uncaught callback errors if that is the policy. Do not claim that unmount reports asynchronous errors synchronously.\n\nKeep unmount synchronous for this migration and document that it schedules teardown but does not signal its completion. The vendor supplies no completion promise. If a future consumer must await disposal, introduce an adapter that observes callback completion and rejection, then expose an explicit asynchronous teardown contract. Merely awaiting `dispose()` would not provide that guarantee.\n\n## Alternatives rejected\n\n| Alternative | Reason |\n| --- | --- |\n| Restore timer deletion permanently | It repairs this exact ordering but makes membership depend on scheduling. A pending deletion can also remove a replacement written under the same key. |\n| Delay deletion with `queueMicrotask` | It couples the cache to this disposer's current scheduling and does not protect later or nested asynchronous cleanup. |\n| Capture only the value and keep key-based invalidation | It fixes the demonstrated exception with a small caller change, but an old mount can still invalidate a newer mount. Use it only as an explicitly limited interim patch. |\n| Make the whole cache reference counted | It requires release discipline and leak handling that the supplied ordinary-value cache does not need. Retained handles already preserve the required callback value. |\n| Make every invalidation asynchronous | It expands the migration and still needs a definition of whose cleanup has completed. The cache does not own these subscriptions. |\n\n## Migration and acceptance checks\n\nFirst introduce entry handles without changing existing timer behavior, then migrate `mount` to retained values and owner-specific invalidation. Audit every caller for teardown-time `get` and overlapping key ownership before switching key-based invalidation to synchronous deletion. Deprecate unsafe consumer use of `invalidate(key)`, while keeping its deliberate current-entry semantics clear for administrative callers. Version or announce the timing change if callers outside this fixture consume the API.\n\nBefore implementation ships, verify actual behavior with the pinned vendor: normal unmount reports true exactly once after lookup removal; repeated unmount queues no extra report; external invalidation does not break disposal; A replaced by B can unmount without deleting B; a stale handle cannot remove a later put of the same object; report failures follow the documented policy. Keep the existing probe as evidence of the original failure. These proposed contracts and checks have not been implemented or validated here.\n\n## Assignment evidence and limits\n\nCandidate assignment: `arena-a-v1`, retry 1. This artifact is proposal-only and contains no implementation. The supplied package freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The supplied input manifest revision is SHA256 `7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43`; the manifest hashing convention was not supplied, so I do not claim to have independently reproduced that aggregate digest. No task Git SHA is available. The full Git input-revision gate remains reduced and this proposal cannot establish a full Arena method pass. The coordinator owns comparison, judgment and integration.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/b/proposal.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/b/proposal.md",
      "sha256": "366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b",
      "bytes": 7541,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache API proposal\n\nKeep cache invalidation synchronous and make teardown read the entry owned by its mount. Return an entry handle from put so an old mount can remove only its own generation. This separates lookup visibility from consumer lifetime without depending on event-loop delays.\n\n## Confirmed failure\n\nThe after-state invalidate deletes the Map entry immediately. The exact vendored createDisposer queues its callback with queueMicrotask and returns no completion signal. The caller invokes dispose, deletes the entry, then the queued callback evaluates get(key).ready against undefined. The diff alone hides that dependency.\n\nI ran bun arena-walkthrough/input/probe.mjs against the supplied files. It exited 1 with: teardown error: TypeError: undefined is not an object (evaluating get(key).ready). The vendor SHA-256 matches manifest.json: d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f. This establishes behavior for the local fixture-v1 implementation only. It establishes no public dependency behavior.\n\nThe removed setTimeout would place deletion after the queued microtask for this teardown. That ordering follows from the supplied code; I did not run a before-state comparison. Restoring it would preserve this narrow ordering but leave ownership ambiguous.\n\n## Proposed contract\n\n| Operation | Contract |\n| --- | --- |\n| put(key, value) | Replace the lookup entry and return a handle for that exact generation. |\n| get(key) | Return the current value, or undefined when absent. |\n| handle.value | Retain the supplied value reference for this consumer, even after replacement or invalidation. |\n| handle.invalidate() | Synchronously remove the key only if it still refers to this handle generation. Return whether removal occurred. Repeat calls are harmless. |\n| invalidate(key) | Synchronously remove the current lookup entry. Reserve this for a caller explicitly authorized to invalidate whichever generation is current. Return whether removal occurred. |\n\nA handle needs a unique internal identity. Comparing value equality is insufficient because callers can put the same object twice. The cache owns discoverability through get. Consumers own references they retain. Removing a lookup entry does not destroy its value, cancel a subscription, or invalidate an existing handle. The cache never invokes vendor disposal or owns consumer resource cleanup.\n\nThe consumer migration is conceptual, not an implementation in this proposal:\n\n1. Mount saves the handle returned by put.\n2. The disposal callback reports handle.value.ready rather than performing another lookup by key.\n3. Unmount calls subscription.dispose and calls handle.invalidate in a finally block. A local closed flag makes unmount idempotent before either action starts.\n\nThe retained object preserves reads of that particular object, including its later mutations. It does not promise a frozen snapshot. If two mounts use the same key, the older mount still reports its own value and cannot delete the newer mount when it closes. Explicit key-wide invalidation hides the entry from future lookups while retained consumers can finish cleanup.\n\n## Errors and completion\n\nA missing get returns undefined. Code that requires an entry must check it or keep an owned handle. Invalidation of an absent or replaced entry returns false, without throwing.\n\nIf dispose throws synchronously, finally still attempts owned invalidation and the original exception propagates. The closed flag prevents repeated disposal on another unmount call. The vendor provides no retry contract, so automatic disposal retries would be unsafe.\n\nErrors thrown by report inside the queued callback remain asynchronous errors under the existing consumer contract. A synchronous try/catch around unmount cannot catch them. Handle retention removes the missing-entry error, but does not suppress application callback failures. If the product requires error delivery through a promise, add a separate explicit completion/error adapter and define its callback semantics. Do not claim the current dispose method is awaitable.\n\nUnmount completion means disposal was requested and lookup ownership was released. It does not mean the queued report completed. Consumers that need stronger completion must use the separate adapter. A retained handle can prolong object lifetime, so consumers should release their subscription and handle references once their lifecycle finishes.\n\n## Alternatives considered\n\n| Alternative | Reason rejected for this proposal |\n| --- | --- |\n| Restore setTimeout deletion | Repairs this fixture ordering but delays lookup invalidation, and an old timer can delete a replacement entry. |\n| Queue deletion in a microtask | Relies on this vendor callback queue order and still lets stale owners delete new generations. |\n| Await subscription.dispose() | The supplied dispose returns undefined. Awaiting it establishes no general disposal completion contract. |\n| Change get to return a placeholder | Conceals missing entries and changes the meaning of ready. |\n| Retain only a captured value with the current key-based invalidate | Fixes the observed exception, but leaves overlapping mounts vulnerable to deleting a newer entry. |\n| Add reference counts and acquire/release leases | Useful if cache entries own destructible shared resources. The supplied cache holds plain values, so a generation handle is sufficient. |\n\n## Migration and verification plan\n\nFirst inspect all callers before changing put return values or enforcing handle ownership. Existing callers that ignore the new return can continue, but every consumer with delayed teardown must migrate before relying on synchronous invalidation. Document the lookup and lifetime contracts next to the exports. Update mount to keep its handle and remove its teardown lookup. Keep key-wide invalidation explicit for administrative invalidation use cases.\n\nBefore shipping an implementation, run the supplied real dependency probe and verify it reports disposed ready: true, then teardown completed with exit 0. Add behavioral checks for repeated unmount, old-unmount-after-replacement, two puts of the same object, invalidation before disposal, and report errors. Verify that synchronous invalidation hides lookup state before the queued callback while the callback still reads its retained value. These are proposed checks, not completed implementation tests.\n\n## Assignment evidence and limits\n\nThis artifact belongs to assignment arena-b-v1, candidate role, retryCount 0. Its only output is arena-walkthrough/b/proposal.md. I read task.md and every supplied input file. No implementation, external service, commit, installation, setting, or schedule was changed.\n\nThe coordinator supplied input manifest SHA-256 7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43 and package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The input task Git SHA is unavailable, so the full Git-revision assignment gate remains reduced. I have not substituted the package freeze for the task revision. The supplied manifest identifier is not the hash of the literal input/manifest.json file, whose observed SHA-256 is 5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29. I have not independently reconstructed the coordinator manifest algorithm.\n\nThe probe result and dependency hash above are observed command output. The proposed API and migration checks remain design work. No candidate comparison, independent judging, or full Arena completion is claimed by this artifact.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/checklist.md",
      "sha256": "5d87a149c9c9f496bca93211c6d84b9258c0b0df8d99baa9e3200fa317832554",
      "bytes": 211,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "- [x] Frame\n- [ ] Fan out\n- [ ] Cross-judge\n- [ ] Pick\n- [ ] Graft\n- [ ] Verify\nLocal checklist replaces unavailable todo operation. Exact repository Git SHA unavailable; manifest hashes identify fixture bytes.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/input-manifest.json",
      "sha256": "7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43",
      "bytes": 594,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "[[\"README.md\",\"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"],[\"cache.mjs\",\"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"],[\"caller.mjs\",\"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"],[\"invalidation.diff\",\"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"],[\"manifest.json\",\"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"],[\"probe.mjs\",\"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"],[\"vendor/disposer-v1.mjs\",\"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"]]"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/judge.md",
      "sha256": "e2b4d05c492ccaa99816a4e8a806a2df75f6b86bde50187b9baab8e74415f312",
      "bytes": 759,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Fresh worker /root/arena_judge, assignment arena-judge-v1. A hashes 4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e, B hashes 366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b. Scores caller clarity A2 B2; single state owner A2 B2; teardown correctness A2 B2; failure handling A1 B2; extension cost A2 B2. Choose B because closed-before-disposal and finally make synchronous failure explicit. Graft A staged migration and callback error guidance, optional chaining warning. Reject timer/microtask lifetime coupling, captured values with unrestricted invalidation, placeholders, reference counting. Proposed checks are unimplemented. Actual model/effort unknown. No task Git SHA. Coordinator transcription of returned judgment.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/rubric.md",
      "sha256": "a59d89d0e5b46cee7e128711a5e9485d939a77b1345b3762df61e2e1f91d8ce6",
      "bytes": 141,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Parent-only rubric. Score 0-2 each. Caller clarity; single state owner; teardown correctness; explicit failure handling; low extension cost.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/synthesis-note.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/synthesis-note.md",
      "sha256": "2ad624aea27df93d2dd341c56a59fa54ba3d4da4dfcb4ce853e58c8bb85f8935",
      "bytes": 1105,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Base B. Parent scores A 2/2/2/1/2 and B 2/2/2/2/2 on caller clarity, ownership, teardown, failures and extension cost. Fresh judge agrees. Both complete candidate artifacts were read before judging and reread for grafting. B contributes closed-before-disposal, finally and distinct generation identity. A contributes staged migration, optional-chaining warning and explicit deferred-error policy. Reject timing-based lifetime, key-only consumer deletion, placeholders and unnecessary reference counts. No terminal candidate dropout; A's initial spawn failed and its isolated retry completed.\n\nVerification is design review against real fixture and parent reproduction, not API implementation verification. command-results.json records after-state probe exit1 and restored before-state exit0. The synthesis addresses the demonstrated callback lifetime path and replacement ownership. Future behavioral checks remain proposals. No task Git SHA, model diversity, complete structured method receipt or installed-discovery pass is claimed. Manifest hashes and native worker identities are retained separately.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/synthesis.md",
      "sha256": "749432b24c38954ecb7702a67afc1b23010e4789bc88663c7612aa86bdf3f350",
      "bytes": 2607,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache API proposal\n\nRetain consumer values across synchronous cache invalidation. Return an identity-bound handle from put so an older consumer cannot remove a newer entry under the same key. The cache owns lookup membership. Each consumer owns its subscription and retained value.\n\n| Operation | Contract |\n|---|---|\n| put(key, value) | Replace lookup membership and return a fresh generation handle, even if the same value is inserted twice. |\n| get(key) | Return the current value or undefined for a miss. |\n| handle.value | Retain that generation's exact object reference, without promising a deep snapshot. |\n| handle.invalidate() | Remove membership only if this generation is still current, returning whether removal occurred. |\n| invalidate(key) | Remove whichever generation is current. Reserve for deliberate key-wide invalidation. |\n\nMount retains its handle. Its deferred callback reads handle.value.ready. Unmount marks itself closed before requesting disposal, then invalidates its own handle in finally. Repeated unmount does nothing. A synchronous disposal error propagates after owned invalidation. Asynchronous report errors follow an explicit application policy inside the deferred callback. The synchronous unmount return means teardown was requested, not that its callback finished.\n\nThe vendored dispose queues a microtask and returns undefined. Awaiting that return does not establish callback completion. The after-state probe throws because deletion precedes the deferred get(key).ready. Retention removes that dependency. Optional chaining would hide the broken contract and change the report value.\n\nIntroduce handles, migrate consumers, audit teardown-time lookups and overlapping mounts, then change existing key-wide invalidation timing. Publish or version this timing change only through a separately authorized delivery. No delivery occurred here.\n\nReject timer and microtask deferrals as a permanent lifetime contract. They couple correctness to scheduling and can remove replacement entries. Capturing only a value fixes the demonstrated exception but leaves stale key-wide deletion. Placeholder values hide missing data. Reference counting adds release and leak handling without evidence of destructible shared resources in this fixture.\n\nAn implementation must exercise successful deferred reporting after immediate lookup removal, repeated unmount, A replaced by B before A closes, two generations sharing one object, external invalidation before disposal, synchronous disposal errors and asynchronous report errors. No implementation or those future checks ran here.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/task.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/task.md",
      "sha256": "3fb521843cc17b61dd816a343036e322cbddf44d3a0ee5bb2cc49eb1d382641a",
      "bytes": 326,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Produce one Markdown proposal for a cache API using input/cache.mjs, caller.mjs, vendor/disposer-v1.mjs and README.md. Preserve consumer teardown correctness. Explain API ownership, errors, alternatives rejected and migration. No implementation or external actions. Input revision is SHA256 manifest, not an invented Git SHA.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/verification.json",
      "sha256": "b84d79259fd627401ac6acb9551958507a2f560c7ecb03c4cc40d487adb2ceda",
      "bytes": 399,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "{\n  \"kind\": \"parent design inspection; not implementation test\",\n  \"criteria\": {\n    \"callerClarity\": true,\n    \"stateOwnership\": true,\n    \"teardown\": true,\n    \"failureHandling\": true,\n    \"extensionCost\": true\n  },\n  \"candidateHashes\": {\n    \"a\": \"4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e\",\n    \"b\": \"366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b\"\n  }\n}"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough.result.md",
      "sha256": "a80484ae5850eccc0940c33b3bc99c0dd10574911c55635575e4f7ce0c58a13c",
      "bytes": 6019,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# arena-walkthrough\n\n## Supplied input\n\n> Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\n\nNamed source files and exact copied source bytes are retained in [arena-walkthrough/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-manifest.json) and [arena-walkthrough/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Navigation, frame and capability decisions\n\nRead installed README. It links docs/workflows/arena.md and that destination exists and was fully read. Read Arena and its capability, model-role, assignment and ownership contracts plus applied leaves. Source reads establish navigation, not a registered /arena command or installed-discovery pass. Installed package is visibly listed in this host's skill catalog, but source invocation was manual and no host registration command was tested.\n\nA local six-phase checklist replaces an unavailable todo operation. task.md requests two Markdown cache API proposals. The parent-only rubric has five criteria, caller clarity, state ownership, teardown correctness, failure handling and extension cost. Candidates did not receive the rubric. Frozen fixture input-manifest.json hashes to7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43. No exact task Git SHA exists. This missing concrete prerequisite prevents a full assignment-contract run; isolated comparison proceeds with that explicit reduction.\n\n## Fan out and inspect\n\nCandidate A's inherited-context spawn failed with invalid thread-store/no rollout. The actual error is preserved in worker-events.json. A fresh fork_turns none attempt under arena-a-v1 retry1 returned /root/arena_a_retry and produced a/proposal.md. Candidate B, /root/arena_b under arena-b-v1 retry0, produced b/proposal.md. Their outputs are disjoint and both were read end to end. SHA256 values are4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e and366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b.\n\nWorker requests inherited model/effort. Observed model and effort are unknown. No cloud-placement or diversity claim. Actual workers wrote only their assigned proposals according to inspected files and returns; no OS-enforced per-worker sandbox is claimed. Append-only immutable pre-dispatch assignment events were not fully persisted before dispatch, so later coordinator event transcription is not a complete structured method receipt.\n\n## Cross-judge, pick and graft\n\nOnly after both terminal candidates and full artifacts were inspected, fresh read-only /root/arena_judge received candidates plus rubric. judge.md retains its result and independently checked artifact hashes. Parent criterion scores match the judge, A2/2/2/1/2 and B2/2/2/2/2. These are proposal comparison scores, not host case grades. Choose B because it defines closed-before-disposal and owned invalidation in finally. Graft A staged migration, optional-chaining warning and deferred-error policy. Reject scheduling-dependent lifetime, raw-key consumer invalidation, placeholders and unjustified reference counts. Both converge on generation handles; the graft keeps one model.\n\n## Verify and actual output\n\nsynthesis.md is the resulting cache API proposal; synthesis-note.md records base, grafts, rejections and inspection. verification.json retains hashes and bounded parent textual review aids. The parent reviewed the real caller/vendor path and reproduced after-state failure and before-state completion in command-results.json. API implementation and proposed future regression checks did not run. Prove It Works changed the verification from trusting worker summaries to reading artifacts and actual probe output. Separate Before Serializing Shared State changed candidate ownership to disjoint paths. Laziness Protocol rejected reference counting. Redesign From First Principles kept ownership coherent. Unslop was applied to synthesis prose.\n\nSix phases were exercised with native candidates and a fresh judge. Exact task Git SHA, observed model diversity and a full structured method receipt remain unmet. A source read or local text assertion is not evidence those gates passed. No dependency, settings, Git history or external action was changed.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/artifact-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/artifact-manifest.json",
      "sha256": "bae84a8bd22760406349cca0bf31c2827d144af3312c7587f7ed6668e34ea21b",
      "bytes": 10076,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-a.json\",\n    \"sha256\": \"1a45ff25e244821df754c00447a111c01db9c0e3ae738b1c522b640b2c849443\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/probe.mjs\",\n    \"sha256\": \"5318c591adba35124261216c084209930f304f647206e71dd22651f5e2e24b62\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/verification.txt\",\n    \"sha256\": \"a217c58f09ec4aa6c30487d28fcd8fe99708b56817f64548c02e2aa33a1a2e09\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/rationale.md\",\n    \"sha256\": \"1d1b9e6b88c349df7e5fe1ebdb19ef9fd092f80ef9718a47ca5bafa0c402a578\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/caller.mjs\",\n    \"sha256\": \"11977f0cbb7984d932f1d08be6d201ef478413b8ad51e7648d69b8e433787c03\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/cache.mjs\",\n    \"sha256\": \"f23fd42b5a48fe7b0a825f3dffb207a53d4a2330b781337de03d315d7a0c38c4\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/probe.mjs\",\n    \"sha256\": \"0a7ac5803ed848836b25c063d38cce121f647cf92b6c718aec85cde345ec7ccf\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/rationale.md\",\n    \"sha256\": \"3490d018b721b94af532ba09b3764815ca4965a9873915252d866f20e2e225c0\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/check-output.txt\",\n    \"sha256\": \"e126ccdf445006282c4e4ecc9d9237fa29cee8416f5dae52580173599be4507b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/caller.mjs\",\n    \"sha256\": \"ccd8313ce544c2a3c021fd9e951240014c53865597a7a4fc09be02baa9f5fd50\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/cache.mjs\",\n    \"sha256\": \"91e23f5874e48fdcd96d0001fe9f50bb16182d6d7d2f1eb3ac53dc5a61144002\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/inspected-b.txt\",\n    \"sha256\": \"938fcd009eb6f2761a465df1bae7314eb69bbedabfb94885d02d4d30aceba924\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/prejudge-order.json\",\n    \"sha256\": \"c369093344d5e3a033ba9e335515c1c01fe93f230235b6c0d1c0b9e2c6d4e2aa\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/declared-order.json\",\n    \"sha256\": \"800079d849af16733a177f8c3466630a239450c8786c49bb469a81c345ef8634\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/inspected-a.txt\",\n    \"sha256\": \"ff19c53b2eb83d2a693d0ac941ee8326fc4179414d59253655ce5c217b06c560\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-a.json\",\n    \"sha256\": \"d78940929c787ac274aa99834ab9e1c78f345eb2a2f52a8dfa58b490dd789ae9\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-events.json\",\n    \"sha256\": \"22c94d7d26e3a08bdeea2f0c7e81b1f636104e1d0251411f4502ccf9166a010a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge-return.md\",\n    \"sha256\": \"9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/supplied-input.json\",\n    \"sha256\": \"8a7468842c1a9f6b261be11f918161f959f9953210ee4d8eb2750af412962f7f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/graft-verification.json\",\n    \"sha256\": \"3fc1bfc990555065e263b8b0f27d69695a80b536297a37743a04fe71c65f966a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-a.txt\",\n    \"sha256\": \"2fb5713501a1576ab558a69aa305f4d60b4ea4a8ccce209a1058cbc3fbed8272\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-b.json\",\n    \"sha256\": \"3338055db260447afe3362de98232345dc44f371e8533705d139722faa0eae07\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/probe.mjs\",\n    \"sha256\": \"7972e357f3d814cee41bb0d5ab89dc54738cfd8ea7e3d02c835cd07dfe4228e9\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/usage.md\",\n    \"sha256\": \"83dfee206ec8612ad2b3cb9ebd528c75ded55bf3eb489bf21e24c2b70ad198f5\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/caller.mjs\",\n    \"sha256\": \"d1c746e51c90c5d26733d55945332d636cd47bfa5ab0f5848386c5f05d3d520e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/overlap.mjs\",\n    \"sha256\": \"70a5a93086d5fd3c2ddd2e1b07b795d0f2b56bb66df3034040eed2e41484c350\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/evidence-note.md\",\n    \"sha256\": \"73902a46e3394a81c63b01ca9f8c46f7778664410a097a491cb766deb1d9da39\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/cache.mjs\",\n    \"sha256\": \"f23fd42b5a48fe7b0a825f3dffb207a53d4a2330b781337de03d315d7a0c38c4\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-b.txt\",\n    \"sha256\": \"6da362404a81da4b6f09ffb0b67716afd94388ce26ba45902cf18cb7e3dbeaa3\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-a.json\",\n    \"sha256\": \"e37a971ff6da34edb67541333e93856f173dcad0b6b88d9bb14bd1e67037d3c8\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/baseline.json\",\n    \"sha256\": \"e83b39b818d909b9553cfcc4cf285362948b62bb28b9fbd3ae1632c8f1d7e440\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/terminal-b.txt\",\n    \"sha256\": \"f506a383efedf09a3fe18cb3f5d5ffdba1c2931363b154650c949e5b926573ab\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/outcome-review.md\",\n    \"sha256\": \"33400d792a32b6dbc3d0d94053407ba1386f99f412bbabf0f6804bdda54e077e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-judge.json\",\n    \"sha256\": \"4b89fd7f0a10bfdb93748a3c4b5d85bf7d5839bdaca77a833cfd589032e40e7b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/checklist.md\",\n    \"sha256\": \"8dae7dfd003f7d2c7b1c25c8fb5aea617fc8da1b66f37a6f81a0bb74b8895459\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/observations.json\",\n    \"sha256\": \"36f7659bff2da3658293a632401d1bf7b790e06d4efa8e7386f9edbdf079ee03\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/method-receipt.json\",\n    \"sha256\": \"4f3c38b3e073eab35d367debf71b45106939ce5bbd832069cabe1e8e142cd192\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/spawn-order.json\",\n    \"sha256\": \"34f051e2e040105473d252856177484ad4f54d26a22f94c1eb60cb139670060f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge/result.md\",\n    \"sha256\": \"9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/task.md\",\n    \"sha256\": \"98bee99171904d2efe67045e42ae8392f28b215d41dd43acc0d372f693873a67\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/rubric-private.md\",\n    \"sha256\": \"84fb029b48c1995e1d2e1d72026590528f97c1cd47c67925631bef7f0b44e840\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/verification.json\",\n    \"sha256\": \"c608e79c0b8dff7ba701617c5c70e3b626c99483eb9e7806ea7a7429e832b24f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-b.json\",\n    \"sha256\": \"75710ac1793a7796a8b4c0b63892b8d6b4cf3306806778033d9ea04ee417fc6f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge-assignment.json\",\n    \"sha256\": \"be95c0023cf63431c54dac7e42ee35e26036e71a4f2bffb6f683f9a7aa796334\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-b.json\",\n    \"sha256\": \"62b8a97800150e890cdd5fea25f20796b2245366fe9d3830cce49678af82591b\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/assignment-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-a.json",
      "sha256": "d78940929c787ac274aa99834ab9e1c78f345eb2a2f52a8dfa58b490dd789ae9",
      "bytes": 1613,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"id\": \"arena-walkthrough-a\",\n  \"scope\": \"Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"seat-a-pending-worker-id\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"arena-walkthrough/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/assignment-b.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-b.json",
      "sha256": "75710ac1793a7796a8b4c0b63892b8d6b4cf3306806778033d9ea04ee417fc6f",
      "bytes": 1613,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"id\": \"arena-walkthrough-b\",\n  \"scope\": \"Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"seat-b-pending-worker-id\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"arena-walkthrough/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/assignment-events.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/assignment-events.json",
      "sha256": "22c94d7d26e3a08bdeea2f0c7e81b1f636104e1d0251411f4502ccf9166a010a",
      "bytes": 1576,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "[\n  {\n    \"assignmentId\": \"arena-walkthrough-a\",\n    \"event\": \"dispatch\",\n    \"order\": 8,\n    \"workerId\": \"/root/walk_a\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/walk_a.jsonl\"\n  },\n  {\n    \"assignmentId\": \"arena-walkthrough-b\",\n    \"event\": \"dispatch\",\n    \"order\": 9,\n    \"workerId\": \"/root/walk_b\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/walk_b.jsonl\"\n  },\n  {\n    \"assignmentId\": \"arena-walkthrough-b\",\n    \"event\": \"terminal-completed\",\n    \"order\": 25,\n    \"workerId\": \"/root/walk_b\",\n    \"result\": \"arena-walkthrough/candidates/b/rationale.md\",\n    \"outputSha256\": \"3490d018b721b94af532ba09b3764815ca4965a9873915252d866f20e2e225c0\"\n  },\n  {\n    \"assignmentId\": \"arena-walkthrough-a\",\n    \"event\": \"terminal-completed\",\n    \"order\": 26,\n    \"workerId\": \"/root/walk_a\",\n    \"result\": \"arena-walkthrough/candidates/a/rationale.md\",\n    \"outputSha256\": \"1d1b9e6b88c349df7e5fe1ebdb19ef9fd092f80ef9718a47ca5bafa0c402a578\"\n  },\n  {\n    \"assignmentId\": \"arena-walkthrough-judge\",\n    \"event\": \"dispatch\",\n    \"order\": 31,\n    \"workerId\": \"/root/walk_judge\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/walk_judge.jsonl\"\n  },\n  {\n    \"assignmentId\": \"arena-walkthrough-judge\",\n    \"event\": \"terminal-completed\",\n    \"order\": 37,\n    \"workerId\": \"/root/walk_judge\",\n    \"result\": \"arena-walkthrough/judge/result.md\",\n    \"outputSha256\": \"9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/baseline.json",
      "sha256": "e83b39b818d909b9553cfcc4cf285362948b62bb28b9fbd3ae1632c8f1d7e440",
      "bytes": 307,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"committed-inputs/additional/cache/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 1,\n  \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/a/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/cache.mjs",
      "sha256": "f23fd42b5a48fe7b0a825f3dffb207a53d4a2330b781337de03d315d7a0c38c4",
      "bytes": 1053,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "// Each mount owns one entry. Keys identify entries but never address shared storage.\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let state = 'mounted';\n  let completion;\n\n  function read() {\n    if (state === 'disposed') throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(startDisposal) {\n    if (completion) return completion;\n    state = 'disposing';\n    let resolveCompletion;\n    let rejectCompletion;\n    completion = new Promise((resolve, reject) => {\n      resolveCompletion = resolve;\n      rejectCompletion = reject;\n    });\n    function finish(error, failed) {\n      value = undefined;\n      state = 'disposed';\n      if (failed) rejectCompletion(error);\n      else resolveCompletion();\n    }\n    try {\n      Promise.resolve(startDisposal()).then(\n        () => finish(undefined, false),\n        error => finish(error, true),\n      );\n    } catch (error) {\n      finish(error, true);\n    }\n    return completion;\n  }\n\n  return Object.freeze({ read, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/a/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/caller.mjs",
      "sha256": "11977f0cbb7984d932f1d08be6d201ef478413b8ad51e7648d69b8e433787c03",
      "bytes": 699,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nimport { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  let resolveDisposal;\n  let rejectDisposal;\n  const disposed = new Promise((resolve, reject) => {\n    resolveDisposal = resolve;\n    rejectDisposal = reject;\n  });\n  const subscription = createDisposer(() => {\n    try {\n      Promise.resolve(report(entry.read().ready)).then(resolveDisposal, rejectDisposal);\n    } catch (error) {\n      rejectDisposal(error);\n    }\n  });\n  return () => entry.dispose(() => {\n    subscription.dispose();\n    return disposed;\n  });\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/a/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/probe.mjs",
      "sha256": "5318c591adba35124261216c084209930f304f647206e71dd22651f5e2e24b62",
      "bytes": 2877,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst source = 'committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nconst pinned = Bun.spawnSync(['git', 'show', `${revision}:${source}`]);\nassert.equal(pinned.exitCode, 0);\nconst live = await Bun.file(new URL(`../../../${source}`, import.meta.url)).arrayBuffer();\nassert.equal(Buffer.compare(Buffer.from(pinned.stdout), Buffer.from(live)), 0);\nassert.equal(createHash('sha256').update(Buffer.from(live)).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\n\nlet reports = 0;\nconst unmount = mount('key', ready => { assert.equal(ready, true); reports++; });\nconst completion = unmount();\nassert.equal(reports, 0, 'the pinned dependency defers its callback');\nassert.equal(unmount(), completion, 'double unmount returns the same completion');\nawait completion;\nassert.equal(reports, 1);\nassert.equal(unmount(), completion, 'unmount after completion remains idempotent');\n\nconst events = [];\nconst first = mount('same-key', ready => events.push(['first', ready]));\nconst second = mount('same-key', ready => events.push(['second', ready]));\nawait Promise.all([second(), first()]);\nassert.deepEqual(events, [['second', true], ['first', true]]);\n\nlet release;\nconst entry = createEntry('lifecycle', { owner: 'first' });\nconst pending = entry.dispose(() => new Promise(resolve => { release = resolve; }));\nassert.equal(entry.read().owner, 'first', 'disposing entries retain their value');\nconst other = createEntry('lifecycle', { owner: 'second' });\nrelease();\nawait pending;\nassert.throws(() => entry.read(), /disposed/);\nassert.equal(other.read().owner, 'second', 'same-key entries do not share state');\nawait other.dispose(() => undefined);\n\nconst reportError = new Error('report failure');\nawait assert.rejects(mount('throwing-report', () => { throw reportError; })(), error => error === reportError);\nawait assert.rejects(mount('rejecting-report', () => Promise.reject(reportError))(), error => error === reportError);\nconst failingEntry = createEntry('failure', { ready: true });\nconst failed = failingEntry.dispose(() => { throw reportError; });\nawait assert.rejects(failed, error => error === reportError);\nassert.throws(() => failingEntry.read(), /disposed/);\nassert.equal(failingEntry.dispose(() => assert.fail('must not restart')), failed);\nconst rejectingEntry = createEntry('rejection', 1);\nawait assert.rejects(rejectingEntry.dispose(() => Promise.reject(reportError)), error => error === reportError);\nassert.throws(() => rejectingEntry.read(), /disposed/);\nconsole.log('PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures');\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/a/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/rationale.md",
      "sha256": "1d1b9e6b88c349df7e5fe1ebdb19ef9fd092f80ef9718a47ca5bafa0c402a578",
      "bytes": 5126,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "# Seat A result\n\nAssignment ID: arena-walkthrough-a\nInput revision: fb7d9f00a700b1f6c3c88204d967433d99c11a73\nMethod: arena\nRequested model and effort: inherit-parent\nActual model and effort: unknown\nPackage freeze supplied by assignment: f4623636a287bea2aa79c4b2234a53d20a5f193c\nInstalled package version supplied by assignment: 0.1.0\n\nEach mount creates a lifecycle-owned entry. The entry retains its value through the disposing state and invalidates only after disposal completion settles. There is no module-level Map, shared key lookup, or global mutable cache. The report callback reads its entry at execution time. It does not receive a captured mount value as a disposal argument.\n\nThe original caller calls dispose, then deletes the key synchronously. The exact vendored disposer queues the callback with queueMicrotask. Its later get(key).ready therefore reads undefined. Retaining setTimeout deletion would change ordering but preserve global ownership and same-key interference.\n\ncache.mjs owns mounted, disposing, and disposed states. read remains legal during disposal and throws after disposal completes. dispose returns one cached promise, including when disposal fails. It invalidates on both successful and failed completion. A completion promise is allocated before starting disposal, so reentrant calls cannot start a second disposal.\n\ncaller.mjs adapts the actual vendored dependency, which provides no completion signal. Its callback settles a promise after report finishes. The entry observes that promise to decide when invalidation is safe. The dependency import points to the supplied vendor file, whose working bytes the probe compares with git show at the full input revision and with the manifest digest.\n\nDouble unmount returns the same promise and schedules exactly one vendor callback. Overlapping mounts with the same key own separate entries. Either may finish first without clearing or reading the other's value. The key is diagnostic identity, not a shared storage address. Independent mounts no longer deduplicate values; this fixture requires ownership isolation rather than shared caching.\n\nA synchronous report exception or rejected report promise rejects unmount's completion and still invalidates. The caller catches report exceptions inside the queued callback, so they do not escape as uncaught microtask exceptions. Consumers must await or handle the returned unmount promise. The entry also clears its value if starting disposal throws or returns a rejected promise. The pinned dependency always schedules its callback; an adapter for a dependency that never invokes it would need its own completion or cancellation policy. No timeout guesses completion here.\n\nAlternatives rejected:\n\n- A module-level Map with delayed deletion still allows same-key mounts to overwrite one another.\n- A per-controller Map would require generation ownership or reference counting to avoid the same problem and adds a lookup this caller does not need.\n- Seat B's captured mount value passed into disposal would also isolate mounts, but it is outside this seat's assigned shape.\n- queueMicrotask invalidation relies on scheduling order instead of disposal completion and would invalidate too early for asynchronous reporting.\n\n# Verification\n\nRan `bun arena-walkthrough/candidates/a/probe.mjs` with Bun 1.4.2. Exit status 0. The probe checks exact vendor bytes and digest, deferred callback execution, disposal-time reads, invalidation after completion, double unmount before and after completion, overlapping same-key mounts, synchronous report errors, asynchronous report rejection, disposal-start exceptions, and disposal-start rejection. It asserts rejection identity as well as final entry state.\n\nOne initial probe run failed because node:crypto update rejects ArrayBuffer. The probe now wraps the bytes in Buffer, and the rerun passes. This was a verification-code error, not a cache failure.\n\nRead installed Arena SKILL.md, host-capabilities.md, model-roles.md, orchestration-contract.md, workflow-ownership.md, and the five required leaves for separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works, and unslop. The installed 0.1.0 path has no Git metadata. After the coordinator supplied /Users/digital-hawk/Herd/pstack-openai-port, independently read all ten instruction files with git show at f4623636a287bea2aa79c4b2234a53d20a5f193c and compared them byte for byte with the installed copies. All matched. The coordinator reports an author metadata exception in plugin.json; that package metadata exception was not independently audited by this seat. Input cache files, README, diff, manifest, and vendored disposer were read with git show at the assignment revision. No installed discovery or public dependency claim follows from those source reads.\n\nWrites are confined to arena-walkthrough/candidates/a. No external services, installs, settings changes, commits, or child workers were used. This seat supplies one candidate, not a judgment or completed parent Arena synthesis. Sibling outputs and the withheld rubric were not read.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/a/verification.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a/verification.txt",
      "sha256": "a217c58f09ec4aa6c30487d28fcd8fe99708b56817f64548c02e2aa33a1a2e09",
      "bytes": 130,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/b/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/cache.mjs",
      "sha256": "91e23f5874e48fdcd96d0001fe9f50bb16182d6d7d2f1eb3ac53dc5a61144002",
      "bytes": 216,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "// Each mount owns one cache cell. No module-level mutable state.\nexport function createCache(value) {\n  let current = value;\n  return {\n    get: () => current,\n    invalidate: () => { current = undefined; },\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/b/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/caller.mjs",
      "sha256": "ccd8313ce544c2a3c021fd9e951240014c53865597a7a4fc09be02baa9f5fd50",
      "bytes": 745,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nimport { createCache } from './cache.mjs';\n\nfunction reportDisposed(value, report) {\n  report(value.ready);\n}\n\nexport function mount(key, report) {\n  // The key identifies the mount to callers; mounts do not share storage by key.\n  const cache = createCache({ ready: true });\n  let mountedValue = cache.get();\n  let unmounted = false;\n  const subscription = createDisposer(() => {\n    const value = mountedValue;\n    mountedValue = undefined;\n    reportDisposed(value, report);\n  });\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    try {\n      subscription.dispose();\n    } finally {\n      cache.invalidate();\n    }\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/b/check-output.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/check-output.txt",
      "sha256": "e126ccdf445006282c4e4ecc9d9237fa29cee8416f5dae52580173599be4507b",
      "bytes": 369,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "PASS actual vendored disposer matches input revision and manifest digest\nPASS cache invalidation is synchronous and repeatable\nPASS deferred report reads captured value, double unmount reports once\nPASS overlapping same-key mounts and remount before disposal stay independent\nPASS report exceptions remain observable as uncaught deferred exceptions\nAll 5 checks passed\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/b/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/probe.mjs",
      "sha256": "0a7ac5803ed848836b25c063d38cce121f647cf92b6c718aec85cde345ec7ccf",
      "bytes": 2881,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { fileURLToPath } from 'node:url';\nimport { createCache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nif (process.argv.includes('--report-error')) {\n  let caught;\n  process.once('uncaughtException', error => { caught = error; });\n  mount('throws', () => { throw new Error('report sentinel'); })();\n  await new Promise(resolve => setTimeout(resolve, 10));\n  assert.equal(caught?.message, 'report sentinel');\n  console.error('observed uncaught report sentinel');\n  process.exit(1);\n}\n\nconst root = fileURLToPath(new URL('../../../', import.meta.url));\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst vendorPath = 'committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nconst pinned = Bun.spawnSync(['git', 'show', `${revision}:${vendorPath}`], { cwd: root });\nassert.equal(pinned.exitCode, 0, pinned.stderr.toString());\nassert.deepEqual(new Uint8Array(await Bun.file(`${root}/${vendorPath}`).arrayBuffer()), new Uint8Array(pinned.stdout));\nassert.equal(new Bun.CryptoHasher('sha256').update(pinned.stdout).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\nconsole.log('PASS actual vendored disposer matches input revision and manifest digest');\n\nconst value = { ready: true };\nconst cell = createCache(value);\nassert.equal(cell.get(), value);\ncell.invalidate();\nassert.equal(cell.get(), undefined);\ncell.invalidate();\nassert.equal(cell.get(), undefined);\nconsole.log('PASS cache invalidation is synchronous and repeatable');\n\nconst calls = [];\nconst unmount = mount('single', ready => calls.push(ready));\nunmount();\nunmount();\nassert.deepEqual(calls, []);\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(calls, [true]);\nunmount();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(calls, [true]);\nconsole.log('PASS deferred report reads captured value, double unmount reports once');\n\nconst overlapping = [];\nconst a = mount('same-key', ready => overlapping.push(['a', ready]));\nconst b = mount('same-key', ready => overlapping.push(['b', ready]));\na();\nconst c = mount('same-key', ready => overlapping.push(['c', ready]));\nb();\na();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(overlapping, [['a', true], ['b', true]]);\nc();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(overlapping, [['a', true], ['b', true], ['c', true]]);\nconsole.log('PASS overlapping same-key mounts and remount before disposal stay independent');\n\nconst failure = Bun.spawnSync([process.execPath, fileURLToPath(import.meta.url), '--report-error']);\nassert.notEqual(failure.exitCode, 0);\nassert.match(failure.stderr.toString(), /observed uncaught report sentinel/);\nconsole.log('PASS report exceptions remain observable as uncaught deferred exceptions');\nconsole.log('All 5 checks passed');\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/candidates/b/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b/rationale.md",
      "sha256": "3490d018b721b94af532ba09b3764815ca4965a9873915252d866f20e2e225c0",
      "bytes": 4550,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "# Seat B: capture the mount's value\n\nAssignment `arena-walkthrough-b`, method `arena`, input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. Requested model and effort inherit the parent. Actual model and effort are unknown because this seat has no observed model identifier.\n\nEach mount creates its own cache cell, captures its mounted value, and explicitly passes that value to `reportDisposed(value, report)` when the pinned disposer invokes its deferred callback. Unmount invalidates the local cache synchronously. Disposal never consults the cache after invalidation. There is no module-level map, mutable singleton, scheduler workaround or shared state by key.\n\nThe external `mount(key, report)` call remains available. The key no longer selects shared storage. It is a caller label. This deliberate ownership change means overlapping mounts with equal keys own independent cells and values. Unmounting an older mount cannot delete a later mount's value. The fixture exposes no other cache consumers that require a shared key lookup. Such consumers would need an explicit ownership contract before migration; this candidate does not preserve a process-wide put/get/invalidate API.\n\nUnmount sets its guard before scheduling disposal, so repeated or reentrant unmounts schedule one callback. The deferred callback takes its captured value and clears its retained reference before invoking report. Clearing before report also releases that reference when report throws. Cache invalidation runs in finally if dispose itself throws. The pinned dispose only queues a microtask; no scheduling failure was injected into this exact dependency. If queuing did fail, unmount would throw and remain consumed, with no implicit retry.\n\nReport exceptions propagate out of the microtask, as in the supplied implementation. Unmount cannot catch a later callback exception and returns no completion promise. The probe uses a child process and an uncaughtException observer to verify that an intentional report error remains observable. It does not silently convert report failure into success. Unmount's local invalidation has already completed before report runs.\n\nI rejected delayed invalidation with setTimeout. It depends on relative scheduler timing and leaves shared same-key ownership unresolved. I rejected a global map with generation tokens or reference counts because independent mounts do not need shared mutation. I also rejected disposal-completion-owned invalidation for this seat. That is a valid different design, but it extends cache lifetime and requires a completion contract absent from the pinned disposer. Seat B has no reason to read a cache during disposal once the value is explicit.\n\nI read all seven cache fixture files with git show at the specified input revision, including the actual vendored disposer and its manifest. The supplied disposer uses queueMicrotask, so synchronous invalidation removes the map entry before its callback reads get(key).ready. The supplied after-state probe reproduced that TypeError with exit 1. The candidate imports that actual supplied vendor file. Its probe compares the imported file bytes against git show at the input revision and checks the manifest's SHA-256 before accepting the run. These conclusions apply to this exact local fixture, not a public dependency or unspecified disposer version.\n\nThe frozen Arena skill and its four contracts were read from the supplied evidence. The principle leaves were absent from that evidence subtree, so I read separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and unslop directly with git show from `/Users/digital-hawk/Herd/pstack-openai-port` at package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`. I applied Unslop to this rationale. This seat owns candidate output only; parent scoring, judging and integration remain outside this assignment.\n\nRun `bun arena-walkthrough/candidates/b/probe.mjs` from the repository root. Bun 1.4.2 passed all five checks: pinned vendor identity, synchronous repeatable invalidation, deferred capture and double unmount, overlapping same-key mounts with remount before disposal, and observable report exceptions. The first candidate probe run failed because its assertion assumed Bun would immediately terminate after an uncaught callback error. Bun continued to the timer. I corrected the observation method to capture the actual uncaught exception in a child; the implementation did not change. No remaining candidate check failures are known.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/checklist.md",
      "sha256": "8dae7dfd003f7d2c7b1c25c8fb5aea617fc8da1b66f37a6f81a0bb74b8895459",
      "bytes": 294,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "- [x] Frame / Ground\n- [x] Fan out / Sketch\n- [x] Cross-judge\n- [x] Pick / Agree\n- [x] Graft / Implement\n- [x] Verify / Scrap assessment\n\nLocal Markdown checklist. No exposed todo tool.\nConditional checkpoint and scrap steps are not triggered; separate dropout trial is incomplete competition.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/declared-order.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/declared-order.json",
      "sha256": "800079d849af16733a177f8c3466630a239450c8786c49bb469a81c345ef8634",
      "bytes": 141,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "[\n  \"frame\",\n  \"dispatch-a\",\n  \"dispatch-b\",\n  \"inspect-terminal-a-and-b\",\n  \"fresh-readonly-judge\",\n  \"parent-pick\",\n  \"graft\",\n  \"verify\"\n]"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/dispatch-a.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-a.txt",
      "sha256": "2fb5713501a1576ab558a69aa305f4d60b4ea4a8ccce209a1058cbc3fbed8272",
      "bytes": 1605,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\nAssignment arena-walkthrough-a. You are seat A. Sole writable directory /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/a. Root repository /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02. All other paths read-only. Requested model and effort inherit-parent. Complete independently; do not read sibling outputs or parent rubric.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/dispatch-b.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-b.txt",
      "sha256": "6da362404a81da4b6f09ffb0b67716afd94388ce26ba45902cf18cb7e3dbeaa3",
      "bytes": 1605,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\nAssignment arena-walkthrough-b. You are seat B. Sole writable directory /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/candidates/b. Root repository /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02. All other paths read-only. Requested model and effort inherit-parent. Complete independently; do not read sibling outputs or parent rubric.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/graft-verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/graft-verification.json",
      "sha256": "3fc1bfc990555065e263b8b0f27d69695a80b536297a37743a04fe71c65f966a",
      "bytes": 278,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"arena-walkthrough/synthesis/overlap.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS graft: remount before old deferred disposal completes\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/inspected-a.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/inspected-a.txt",
      "sha256": "ff19c53b2eb83d2a693d0ac941ee8326fc4179414d59253655ce5c217b06c560",
      "bytes": 9976,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "\nFILE probe.mjs\nimport assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst source = 'committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nconst pinned = Bun.spawnSync(['git', 'show', `${revision}:${source}`]);\nassert.equal(pinned.exitCode, 0);\nconst live = await Bun.file(new URL(`../../../${source}`, import.meta.url)).arrayBuffer();\nassert.equal(Buffer.compare(Buffer.from(pinned.stdout), Buffer.from(live)), 0);\nassert.equal(createHash('sha256').update(Buffer.from(live)).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\n\nlet reports = 0;\nconst unmount = mount('key', ready => { assert.equal(ready, true); reports++; });\nconst completion = unmount();\nassert.equal(reports, 0, 'the pinned dependency defers its callback');\nassert.equal(unmount(), completion, 'double unmount returns the same completion');\nawait completion;\nassert.equal(reports, 1);\nassert.equal(unmount(), completion, 'unmount after completion remains idempotent');\n\nconst events = [];\nconst first = mount('same-key', ready => events.push(['first', ready]));\nconst second = mount('same-key', ready => events.push(['second', ready]));\nawait Promise.all([second(), first()]);\nassert.deepEqual(events, [['second', true], ['first', true]]);\n\nlet release;\nconst entry = createEntry('lifecycle', { owner: 'first' });\nconst pending = entry.dispose(() => new Promise(resolve => { release = resolve; }));\nassert.equal(entry.read().owner, 'first', 'disposing entries retain their value');\nconst other = createEntry('lifecycle', { owner: 'second' });\nrelease();\nawait pending;\nassert.throws(() => entry.read(), /disposed/);\nassert.equal(other.read().owner, 'second', 'same-key entries do not share state');\nawait other.dispose(() => undefined);\n\nconst reportError = new Error('report failure');\nawait assert.rejects(mount('throwing-report', () => { throw reportError; })(), error => error === reportError);\nawait assert.rejects(mount('rejecting-report', () => Promise.reject(reportError))(), error => error === reportError);\nconst failingEntry = createEntry('failure', { ready: true });\nconst failed = failingEntry.dispose(() => { throw reportError; });\nawait assert.rejects(failed, error => error === reportError);\nassert.throws(() => failingEntry.read(), /disposed/);\nassert.equal(failingEntry.dispose(() => assert.fail('must not restart')), failed);\nconst rejectingEntry = createEntry('rejection', 1);\nawait assert.rejects(rejectingEntry.dispose(() => Promise.reject(reportError)), error => error === reportError);\nassert.throws(() => rejectingEntry.read(), /disposed/);\nconsole.log('PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures');\n\nFILE verification.txt\nPASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\n\nFILE rationale.md\n# Seat A result\n\nAssignment ID: arena-walkthrough-a\nInput revision: fb7d9f00a700b1f6c3c88204d967433d99c11a73\nMethod: arena\nRequested model and effort: inherit-parent\nActual model and effort: unknown\nPackage freeze supplied by assignment: f4623636a287bea2aa79c4b2234a53d20a5f193c\nInstalled package version supplied by assignment: 0.1.0\n\nEach mount creates a lifecycle-owned entry. The entry retains its value through the disposing state and invalidates only after disposal completion settles. There is no module-level Map, shared key lookup, or global mutable cache. The report callback reads its entry at execution time. It does not receive a captured mount value as a disposal argument.\n\nThe original caller calls dispose, then deletes the key synchronously. The exact vendored disposer queues the callback with queueMicrotask. Its later get(key).ready therefore reads undefined. Retaining setTimeout deletion would change ordering but preserve global ownership and same-key interference.\n\ncache.mjs owns mounted, disposing, and disposed states. read remains legal during disposal and throws after disposal completes. dispose returns one cached promise, including when disposal fails. It invalidates on both successful and failed completion. A completion promise is allocated before starting disposal, so reentrant calls cannot start a second disposal.\n\ncaller.mjs adapts the actual vendored dependency, which provides no completion signal. Its callback settles a promise after report finishes. The entry observes that promise to decide when invalidation is safe. The dependency import points to the supplied vendor file, whose working bytes the probe compares with git show at the full input revision and with the manifest digest.\n\nDouble unmount returns the same promise and schedules exactly one vendor callback. Overlapping mounts with the same key own separate entries. Either may finish first without clearing or reading the other's value. The key is diagnostic identity, not a shared storage address. Independent mounts no longer deduplicate values; this fixture requires ownership isolation rather than shared caching.\n\nA synchronous report exception or rejected report promise rejects unmount's completion and still invalidates. The caller catches report exceptions inside the queued callback, so they do not escape as uncaught microtask exceptions. Consumers must await or handle the returned unmount promise. The entry also clears its value if starting disposal throws or returns a rejected promise. The pinned dependency always schedules its callback; an adapter for a dependency that never invokes it would need its own completion or cancellation policy. No timeout guesses completion here.\n\nAlternatives rejected:\n\n- A module-level Map with delayed deletion still allows same-key mounts to overwrite one another.\n- A per-controller Map would require generation ownership or reference counting to avoid the same problem and adds a lookup this caller does not need.\n- Seat B's captured mount value passed into disposal would also isolate mounts, but it is outside this seat's assigned shape.\n- queueMicrotask invalidation relies on scheduling order instead of disposal completion and would invalidate too early for asynchronous reporting.\n\n# Verification\n\nRan `bun arena-walkthrough/candidates/a/probe.mjs` with Bun 1.4.2. Exit status 0. The probe checks exact vendor bytes and digest, deferred callback execution, disposal-time reads, invalidation after completion, double unmount before and after completion, overlapping same-key mounts, synchronous report errors, asynchronous report rejection, disposal-start exceptions, and disposal-start rejection. It asserts rejection identity as well as final entry state.\n\nOne initial probe run failed because node:crypto update rejects ArrayBuffer. The probe now wraps the bytes in Buffer, and the rerun passes. This was a verification-code error, not a cache failure.\n\nRead installed Arena SKILL.md, host-capabilities.md, model-roles.md, orchestration-contract.md, workflow-ownership.md, and the five required leaves for separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works, and unslop. The installed 0.1.0 path has no Git metadata. After the coordinator supplied /Users/digital-hawk/Herd/pstack-openai-port, independently read all ten instruction files with git show at f4623636a287bea2aa79c4b2234a53d20a5f193c and compared them byte for byte with the installed copies. All matched. The coordinator reports an author metadata exception in plugin.json; that package metadata exception was not independently audited by this seat. Input cache files, README, diff, manifest, and vendored disposer were read with git show at the assignment revision. No installed discovery or public dependency claim follows from those source reads.\n\nWrites are confined to arena-walkthrough/candidates/a. No external services, installs, settings changes, commits, or child workers were used. This seat supplies one candidate, not a judgment or completed parent Arena synthesis. Sibling outputs and the withheld rubric were not read.\n\nFILE caller.mjs\nimport { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nimport { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  let resolveDisposal;\n  let rejectDisposal;\n  const disposed = new Promise((resolve, reject) => {\n    resolveDisposal = resolve;\n    rejectDisposal = reject;\n  });\n  const subscription = createDisposer(() => {\n    try {\n      Promise.resolve(report(entry.read().ready)).then(resolveDisposal, rejectDisposal);\n    } catch (error) {\n      rejectDisposal(error);\n    }\n  });\n  return () => entry.dispose(() => {\n    subscription.dispose();\n    return disposed;\n  });\n}\n\nFILE cache.mjs\n// Each mount owns one entry. Keys identify entries but never address shared storage.\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let state = 'mounted';\n  let completion;\n\n  function read() {\n    if (state === 'disposed') throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(startDisposal) {\n    if (completion) return completion;\n    state = 'disposing';\n    let resolveCompletion;\n    let rejectCompletion;\n    completion = new Promise((resolve, reject) => {\n      resolveCompletion = resolve;\n      rejectCompletion = reject;\n    });\n    function finish(error, failed) {\n      value = undefined;\n      state = 'disposed';\n      if (failed) rejectCompletion(error);\n      else resolveCompletion();\n    }\n    try {\n      Promise.resolve(startDisposal()).then(\n        () => finish(undefined, false),\n        error => finish(error, true),\n      );\n    } catch (error) {\n      finish(error, true);\n    }\n    return completion;\n  }\n\n  return Object.freeze({ read, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/inspected-b.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/inspected-b.txt",
      "sha256": "938fcd009eb6f2761a465df1bae7314eb69bbedabfb94885d02d4d30aceba924",
      "bytes": 8852,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "\nFILE probe.mjs\nimport assert from 'node:assert/strict';\nimport { fileURLToPath } from 'node:url';\nimport { createCache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nif (process.argv.includes('--report-error')) {\n  let caught;\n  process.once('uncaughtException', error => { caught = error; });\n  mount('throws', () => { throw new Error('report sentinel'); })();\n  await new Promise(resolve => setTimeout(resolve, 10));\n  assert.equal(caught?.message, 'report sentinel');\n  console.error('observed uncaught report sentinel');\n  process.exit(1);\n}\n\nconst root = fileURLToPath(new URL('../../../', import.meta.url));\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst vendorPath = 'committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nconst pinned = Bun.spawnSync(['git', 'show', `${revision}:${vendorPath}`], { cwd: root });\nassert.equal(pinned.exitCode, 0, pinned.stderr.toString());\nassert.deepEqual(new Uint8Array(await Bun.file(`${root}/${vendorPath}`).arrayBuffer()), new Uint8Array(pinned.stdout));\nassert.equal(new Bun.CryptoHasher('sha256').update(pinned.stdout).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\nconsole.log('PASS actual vendored disposer matches input revision and manifest digest');\n\nconst value = { ready: true };\nconst cell = createCache(value);\nassert.equal(cell.get(), value);\ncell.invalidate();\nassert.equal(cell.get(), undefined);\ncell.invalidate();\nassert.equal(cell.get(), undefined);\nconsole.log('PASS cache invalidation is synchronous and repeatable');\n\nconst calls = [];\nconst unmount = mount('single', ready => calls.push(ready));\nunmount();\nunmount();\nassert.deepEqual(calls, []);\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(calls, [true]);\nunmount();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(calls, [true]);\nconsole.log('PASS deferred report reads captured value, double unmount reports once');\n\nconst overlapping = [];\nconst a = mount('same-key', ready => overlapping.push(['a', ready]));\nconst b = mount('same-key', ready => overlapping.push(['b', ready]));\na();\nconst c = mount('same-key', ready => overlapping.push(['c', ready]));\nb();\na();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(overlapping, [['a', true], ['b', true]]);\nc();\nawait new Promise(resolve => queueMicrotask(resolve));\nassert.deepEqual(overlapping, [['a', true], ['b', true], ['c', true]]);\nconsole.log('PASS overlapping same-key mounts and remount before disposal stay independent');\n\nconst failure = Bun.spawnSync([process.execPath, fileURLToPath(import.meta.url), '--report-error']);\nassert.notEqual(failure.exitCode, 0);\nassert.match(failure.stderr.toString(), /observed uncaught report sentinel/);\nconsole.log('PASS report exceptions remain observable as uncaught deferred exceptions');\nconsole.log('All 5 checks passed');\n\nFILE rationale.md\n# Seat B: capture the mount's value\n\nAssignment `arena-walkthrough-b`, method `arena`, input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. Requested model and effort inherit the parent. Actual model and effort are unknown because this seat has no observed model identifier.\n\nEach mount creates its own cache cell, captures its mounted value, and explicitly passes that value to `reportDisposed(value, report)` when the pinned disposer invokes its deferred callback. Unmount invalidates the local cache synchronously. Disposal never consults the cache after invalidation. There is no module-level map, mutable singleton, scheduler workaround or shared state by key.\n\nThe external `mount(key, report)` call remains available. The key no longer selects shared storage. It is a caller label. This deliberate ownership change means overlapping mounts with equal keys own independent cells and values. Unmounting an older mount cannot delete a later mount's value. The fixture exposes no other cache consumers that require a shared key lookup. Such consumers would need an explicit ownership contract before migration; this candidate does not preserve a process-wide put/get/invalidate API.\n\nUnmount sets its guard before scheduling disposal, so repeated or reentrant unmounts schedule one callback. The deferred callback takes its captured value and clears its retained reference before invoking report. Clearing before report also releases that reference when report throws. Cache invalidation runs in finally if dispose itself throws. The pinned dispose only queues a microtask; no scheduling failure was injected into this exact dependency. If queuing did fail, unmount would throw and remain consumed, with no implicit retry.\n\nReport exceptions propagate out of the microtask, as in the supplied implementation. Unmount cannot catch a later callback exception and returns no completion promise. The probe uses a child process and an uncaughtException observer to verify that an intentional report error remains observable. It does not silently convert report failure into success. Unmount's local invalidation has already completed before report runs.\n\nI rejected delayed invalidation with setTimeout. It depends on relative scheduler timing and leaves shared same-key ownership unresolved. I rejected a global map with generation tokens or reference counts because independent mounts do not need shared mutation. I also rejected disposal-completion-owned invalidation for this seat. That is a valid different design, but it extends cache lifetime and requires a completion contract absent from the pinned disposer. Seat B has no reason to read a cache during disposal once the value is explicit.\n\nI read all seven cache fixture files with git show at the specified input revision, including the actual vendored disposer and its manifest. The supplied disposer uses queueMicrotask, so synchronous invalidation removes the map entry before its callback reads get(key).ready. The supplied after-state probe reproduced that TypeError with exit 1. The candidate imports that actual supplied vendor file. Its probe compares the imported file bytes against git show at the input revision and checks the manifest's SHA-256 before accepting the run. These conclusions apply to this exact local fixture, not a public dependency or unspecified disposer version.\n\nThe frozen Arena skill and its four contracts were read from the supplied evidence. The principle leaves were absent from that evidence subtree, so I read separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and unslop directly with git show from `/Users/digital-hawk/Herd/pstack-openai-port` at package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`. I applied Unslop to this rationale. This seat owns candidate output only; parent scoring, judging and integration remain outside this assignment.\n\nRun `bun arena-walkthrough/candidates/b/probe.mjs` from the repository root. Bun 1.4.2 passed all five checks: pinned vendor identity, synchronous repeatable invalidation, deferred capture and double unmount, overlapping same-key mounts with remount before disposal, and observable report exceptions. The first candidate probe run failed because its assertion assumed Bun would immediately terminate after an uncaught callback error. Bun continued to the timer. I corrected the observation method to capture the actual uncaught exception in a child; the implementation did not change. No remaining candidate check failures are known.\n\nFILE check-output.txt\nPASS actual vendored disposer matches input revision and manifest digest\nPASS cache invalidation is synchronous and repeatable\nPASS deferred report reads captured value, double unmount reports once\nPASS overlapping same-key mounts and remount before disposal stay independent\nPASS report exceptions remain observable as uncaught deferred exceptions\nAll 5 checks passed\n\nFILE caller.mjs\nimport { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nimport { createCache } from './cache.mjs';\n\nfunction reportDisposed(value, report) {\n  report(value.ready);\n}\n\nexport function mount(key, report) {\n  // The key identifies the mount to callers; mounts do not share storage by key.\n  const cache = createCache({ ready: true });\n  let mountedValue = cache.get();\n  let unmounted = false;\n  const subscription = createDisposer(() => {\n    const value = mountedValue;\n    mountedValue = undefined;\n    reportDisposed(value, report);\n  });\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    try {\n      subscription.dispose();\n    } finally {\n      cache.invalidate();\n    }\n  };\n}\n\nFILE cache.mjs\n// Each mount owns one cache cell. No module-level mutable state.\nexport function createCache(value) {\n  let current = value;\n  return {\n    get: () => current,\n    invalidate: () => { current = undefined; },\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/judge/result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge/result.md",
      "sha256": "9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683",
      "bytes": 2383,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Assignment: `arena-walkthrough-judge`  \nInput revision: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nObserved model: unknown\n\n| Rubric criterion | A | B |\n|---|---:|---:|\n| Deferred disposal observes original mounted ready value before invalidation | 2 | 1 |\n| No shared mutable map; overlapping keys cannot corrupt ownership | 2 | 2 |\n| Repeat teardown and throwing report have explicit deterministic cleanup | 2 | 2 |\n| Caller clarity and extension cost: coherent small API with rationale | 2 | 2 |\n| **Total** | **8/8** | **7/8** |\n\n**Recommend A as the maintainable base.** Its lifecycle entry retains the value while disposal runs, invalidates after reporting settles, and returns one completion promise for repeated teardown. Synchronous throws and asynchronous report rejection both invalidate and reject that promise.\n\nB satisfies the broader functional interpretation: deferred disposal receives its original mount’s value despite cache invalidation. It **does not satisfy the literal temporal requirement** that disposal read the value *before invalidation*: `cache.invalidate()` runs synchronously, and `reportDisposed(value, report)` runs in the later microtask. Its partial credit recognizes correct value ownership and reporting, not compliance with that ordering. This divergence follows the two assigned shapes and should remain explicit.\n\nConcrete integration choices:\n\n- **Graft B’s remount-before-disposal probe into A.** It explicitly checks an old mount disposing after a new same-key mount exists.\n- **Keep A’s completion and rejection contract.** Callers must await or handle unmount’s returned promise; that API change needs documentation.\n- **Reject B’s immediate invalidation for this literal requirement.**\n- **Reject B’s uncaught microtask exception policy as the base.** Cleanup is deterministic, but errors lack A’s caller-owned completion channel.\n- Keep both rationales’ ownership limitation: keys no longer provide shared caching or deduplication.\n\nI read the withheld rubric, task, every file in both candidate directories, both parent-check JSON outputs, and the pinned vendored disposer via `git show`. Both recorded parent checks exited `0`; their probes establish their respective contracts, so passing B’s probe does not establish the required temporal ordering. No writes or fresh executions were performed."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/judge-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge-assignment.json",
      "sha256": "be95c0023cf63431c54dac7e42ee35e26036e71a4f2bffb6f683f9a7aa796334",
      "bytes": 557,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"id\": \"arena-walkthrough-judge\",\n  \"scope\": \"Read-only fresh judge completed cache proposals against withheld rubric\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/walk_judge\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge-return.md\",\n  \"role\": \"arena read-only judge\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"arena-walkthrough/inspected-a.txt\",\n    \"arena-walkthrough/inspected-b.txt\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/judge-return.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge-return.md",
      "sha256": "9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683",
      "bytes": 2383,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Assignment: `arena-walkthrough-judge`  \nInput revision: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nObserved model: unknown\n\n| Rubric criterion | A | B |\n|---|---:|---:|\n| Deferred disposal observes original mounted ready value before invalidation | 2 | 1 |\n| No shared mutable map; overlapping keys cannot corrupt ownership | 2 | 2 |\n| Repeat teardown and throwing report have explicit deterministic cleanup | 2 | 2 |\n| Caller clarity and extension cost: coherent small API with rationale | 2 | 2 |\n| **Total** | **8/8** | **7/8** |\n\n**Recommend A as the maintainable base.** Its lifecycle entry retains the value while disposal runs, invalidates after reporting settles, and returns one completion promise for repeated teardown. Synchronous throws and asynchronous report rejection both invalidate and reject that promise.\n\nB satisfies the broader functional interpretation: deferred disposal receives its original mount’s value despite cache invalidation. It **does not satisfy the literal temporal requirement** that disposal read the value *before invalidation*: `cache.invalidate()` runs synchronously, and `reportDisposed(value, report)` runs in the later microtask. Its partial credit recognizes correct value ownership and reporting, not compliance with that ordering. This divergence follows the two assigned shapes and should remain explicit.\n\nConcrete integration choices:\n\n- **Graft B’s remount-before-disposal probe into A.** It explicitly checks an old mount disposing after a new same-key mount exists.\n- **Keep A’s completion and rejection contract.** Callers must await or handle unmount’s returned promise; that API change needs documentation.\n- **Reject B’s immediate invalidation for this literal requirement.**\n- **Reject B’s uncaught microtask exception policy as the base.** Cleanup is deterministic, but errors lack A’s caller-owned completion channel.\n- Keep both rationales’ ownership limitation: keys no longer provide shared caching or deduplication.\n\nI read the withheld rubric, task, every file in both candidate directories, both parent-check JSON outputs, and the pinned vendored disposer via `git show`. Both recorded parent checks exited `0`; their probes establish their respective contracts, so passing B’s probe does not establish the required temporal ordering. No writes or fresh executions were performed."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/method-receipt.json",
      "sha256": "4f3c38b3e073eab35d367debf71b45106939ce5bbd832069cabe1e8e142cd192",
      "bytes": 5748,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"arena\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"assignments\": [\n    {\n      \"id\": \"arena-walkthrough-a\",\n      \"workerId\": \"/root/walk_a\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/walk_a\",\n      \"outputPath\": \"arena-walkthrough/candidates/a/rationale.md\",\n      \"role\": \"candidate\",\n      \"status\": \"completed\",\n      \"startedOrder\": 8,\n      \"completedOrder\": 26,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"arena-walkthrough/task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"1d1b9e6b88c349df7e5fe1ebdb19ef9fd092f80ef9718a47ca5bafa0c402a578\"\n    },\n    {\n      \"id\": \"arena-walkthrough-b\",\n      \"workerId\": \"/root/walk_b\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/walk_b\",\n      \"outputPath\": \"arena-walkthrough/candidates/b/rationale.md\",\n      \"role\": \"candidate\",\n      \"status\": \"completed\",\n      \"startedOrder\": 9,\n      \"completedOrder\": 25,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"arena-walkthrough/task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"3490d018b721b94af532ba09b3764815ca4965a9873915252d866f20e2e225c0\"\n    },\n    {\n      \"id\": \"arena-walkthrough-judge\",\n      \"workerId\": \"/root/walk_judge\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/walk_judge\",\n      \"outputPath\": \"arena-walkthrough/judge/result.md\",\n      \"role\": \"judge\",\n      \"status\": \"completed\",\n      \"startedOrder\": 31,\n      \"completedOrder\": 37,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"arena-walkthrough/judge-assignment.json\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"9ecb2c365c2275bea7ecca4f0a65fcb2f25a4c5390ea82ed9518f557a63a9683\"\n    }\n  ],\n  \"reviewArtifact\": \"arena-walkthrough/outcome-review.md\",\n  \"reviewedBy\": \"/root/outcome_review\",\n  \"declaredOrder\": 7,\n  \"candidates\": [\n    \"arena-walkthrough-a\",\n    \"arena-walkthrough-b\"\n  ],\n  \"judge\": \"arena-walkthrough-judge\",\n  \"rubricArtifact\": \"arena-walkthrough/rubric-private.md\",\n  \"synthesis\": {\n    \"order\": 43,\n    \"inspectedCandidates\": [\n      \"arena-walkthrough-a\",\n      \"arena-walkthrough-b\"\n    ],\n    \"artifact\": \"arena-walkthrough/synthesis/cache.mjs\",\n    \"verificationArtifact\": \"arena-walkthrough/verification.json\"\n  }\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/observations.json",
      "sha256": "36f7659bff2da3658293a632401d1bf7b790e06d4efa8e7386f9edbdf079ee03",
      "bytes": 3484,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"bindings\": [\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"evidence/native/root.jsonl\",\n      \"limits\": \"Identities and raw results retained. No explicit model selection.\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec -> tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"arena-walkthrough/inspected-a.txt\",\n      \"limits\": \"Parent read both full code/design and rationale after terminal completion.\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec -> tools.apply_patch / tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"evidence/native/walk_a.jsonl\",\n      \"limits\": \"Distinct local directories, not Git worktrees or OS-enforced per-worker write sandboxes.\"\n    },\n    {\n      \"operation\": \"persistence\",\n      \"tool\": \"functions.exec -> tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"arena-walkthrough/method-receipt.json\",\n      \"limits\": \"Current-session write/readback. Does not establish unattended or later-session recovery.\"\n    }\n  ],\n  \"successfulOperations\": [\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"arena-walkthrough-a\",\n      \"evidence\": \"arena-walkthrough/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_a.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"arena-walkthrough-a\",\n      \"evidence\": \"arena-walkthrough/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_a.jsonl\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"arena-walkthrough-a\",\n      \"evidence\": \"arena-walkthrough/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_a.jsonl\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"arena-walkthrough-b\",\n      \"evidence\": \"arena-walkthrough/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_b.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"arena-walkthrough-b\",\n      \"evidence\": \"arena-walkthrough/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_b.jsonl\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"arena-walkthrough-b\",\n      \"evidence\": \"arena-walkthrough/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/walk_b.jsonl\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"arena-walkthrough-judge\",\n      \"evidence\": \"arena-walkthrough/judge/result.md\",\n      \"rawEvidence\": \"evidence/native/walk_judge.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"arena-walkthrough-judge\",\n      \"evidence\": \"arena-walkthrough/judge/result.md\",\n      \"rawEvidence\": \"evidence/native/walk_judge.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-method\",\n      \"tool\": \"functions.exec\",\n      \"evidence\": \"arena-walkthrough/method-receipt.json\",\n      \"limits\": \"Parent read generated receipt through actual exec_command. Structural method inspection is not a host grade.\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/outcome-review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/outcome-review.md",
      "sha256": "33400d792a32b6dbc3d0d94053407ba1386f99f412bbabf0f6804bdda54e077e",
      "bytes": 8350,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Read-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/parent-check-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-a.json",
      "sha256": "1a45ff25e244821df754c00447a111c01db9c0e3ae738b1c522b640b2c849443",
      "bytes": 350,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"arena-walkthrough/candidates/a/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/parent-check-b.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/parent-check-b.json",
      "sha256": "62b8a97800150e890cdd5fea25f20796b2245366fe9d3830cce49678af82591b",
      "bytes": 594,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"arena-walkthrough/candidates/b/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS actual vendored disposer matches input revision and manifest digest\\nPASS cache invalidation is synchronous and repeatable\\nPASS deferred report reads captured value, double unmount reports once\\nPASS overlapping same-key mounts and remount before disposal stay independent\\nPASS report exceptions remain observable as uncaught deferred exceptions\\nAll 5 checks passed\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/prejudge-order.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/prejudge-order.json",
      "sha256": "c369093344d5e3a033ba9e335515c1c01fe93f230235b6c0d1c0b9e2c6d4e2aa",
      "bytes": 190,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"candidateStarts\": [\n    1,\n    2\n  ],\n  \"candidateTerminalInspections\": [\n    3,\n    4\n  ],\n  \"judgeStartNext\": 5,\n  \"terminalStates\": {\n    \"a\": \"completed\",\n    \"b\": \"completed\"\n  }\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/raw-spawn-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-a.json",
      "sha256": "e37a971ff6da34edb67541333e93856f173dcad0b6b88d9bb14bd1e67037d3c8",
      "bytes": 33,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"task_name\": \"/root/walk_a\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/raw-spawn-b.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-b.json",
      "sha256": "3338055db260447afe3362de98232345dc44f371e8533705d139722faa0eae07",
      "bytes": 33,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"task_name\": \"/root/walk_b\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/raw-spawn-judge.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/raw-spawn-judge.json",
      "sha256": "4b89fd7f0a10bfdb93748a3c4b5d85bf7d5839bdaca77a833cfd589032e40e7b",
      "bytes": 37,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"task_name\": \"/root/walk_judge\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/rubric-private.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/rubric-private.md",
      "sha256": "84fb029b48c1995e1d2e1d72026590528f97c1cd47c67925631bef7f0b44e840",
      "bytes": 349,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Parent/judge only. Score 0-2 per criterion.\n1. Deferred disposal observes its original mounted ready value before invalidation.\n2. No shared mutable map; overlapping keys cannot corrupt ownership.\n3. Repeat teardown and throwing report have explicit deterministic cleanup.\n4. Caller clarity and extension cost: one coherent small API with rationale."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/spawn-order.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/spawn-order.json",
      "sha256": "34f051e2e040105473d252856177484ad4f54d26a22f94c1eb60cb139670060f",
      "bytes": 1194,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "[\n  {\n    \"order\": 1,\n    \"tool\": \"collaboration.spawn_agent\",\n    \"task_name\": \"walk_a\",\n    \"fork_turns\": \"none\",\n    \"message\": \"Execute the full assignment in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-a.txt. Read it through actual tools first. Input Git revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Sole writes arena-walkthrough/candidates/a in that root. No other writes. No external services/install/config/commits. Bun scripts. You are independent Arena seat A. Return ID, revision, method, artifacts and checks.\"\n  },\n  {\n    \"order\": 2,\n    \"tool\": \"collaboration.spawn_agent\",\n    \"task_name\": \"walk_b\",\n    \"fork_turns\": \"none\",\n    \"message\": \"Execute the full assignment in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/dispatch-b.txt. Read it through actual tools first. Input Git revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Sole writes arena-walkthrough/candidates/b in that root. No other writes. No external services/install/config/commits. Bun scripts. You are independent Arena seat B. Return ID, revision, method, artifacts and checks.\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/supplied-input.json",
      "sha256": "8a7468842c1a9f6b261be11f918161f959f9953210ee4d8eb2750af412962f7f",
      "bytes": 4204,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"contract\": {\n    \"id\": \"arena-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge.\"\n    ],\n    \"expectedFull\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n    \"expectedReduced\": \"Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\"\n  },\n  \"caseId\": \"arena-walkthrough\",\n  \"baselineBatch\": \"batch-06\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\",\n  \"expectedFullUnchanged\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Follow README to Arena. Task: redesign local cache ownership so disposal can read its mounted value before invalidation without leaking global mutable cache state. Two candidates must use structurally distinct shapes (e.g. lifecycle-owned entry vs explicit value passed to disposal), each in an isolated owned directory with rationale. Keep 3-6 criterion parent rubric hidden until a fresh read-only judge starts after both candidates finish. Parent reads both, chooses/grafts/rejects and verifies synthesis with an adjacent evidence note.\",\n  \"missingPrerequisites\": [\n    \"Exact case SHA and two isolated writable candidates\",\n    \"Fresh read-only cross-judge after inspected terminal candidates\",\n    \"No model-diversity claim without actual observation\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/cache.mjs",
      "sha256": "f23fd42b5a48fe7b0a825f3dffb207a53d4a2330b781337de03d315d7a0c38c4",
      "bytes": 1053,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "// Each mount owns one entry. Keys identify entries but never address shared storage.\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let state = 'mounted';\n  let completion;\n\n  function read() {\n    if (state === 'disposed') throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(startDisposal) {\n    if (completion) return completion;\n    state = 'disposing';\n    let resolveCompletion;\n    let rejectCompletion;\n    completion = new Promise((resolve, reject) => {\n      resolveCompletion = resolve;\n      rejectCompletion = reject;\n    });\n    function finish(error, failed) {\n      value = undefined;\n      state = 'disposed';\n      if (failed) rejectCompletion(error);\n      else resolveCompletion();\n    }\n    try {\n      Promise.resolve(startDisposal()).then(\n        () => finish(undefined, false),\n        error => finish(error, true),\n      );\n    } catch (error) {\n      finish(error, true);\n    }\n    return completion;\n  }\n\n  return Object.freeze({ read, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/caller.mjs",
      "sha256": "d1c746e51c90c5d26733d55945332d636cd47bfa5ab0f5848386c5f05d3d520e",
      "bytes": 696,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import { createDisposer } from '../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nimport { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  let resolveDisposal;\n  let rejectDisposal;\n  const disposed = new Promise((resolve, reject) => {\n    resolveDisposal = resolve;\n    rejectDisposal = reject;\n  });\n  const subscription = createDisposer(() => {\n    try {\n      Promise.resolve(report(entry.read().ready)).then(resolveDisposal, rejectDisposal);\n    } catch (error) {\n      rejectDisposal(error);\n    }\n  });\n  return () => entry.dispose(() => {\n    subscription.dispose();\n    return disposed;\n  });\n}\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/evidence-note.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/evidence-note.md",
      "sha256": "73902a46e3394a81c63b01ca9f8c46f7778664410a097a491cb766deb1d9da39",
      "bytes": 1276,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Parent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/2/2/2 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B correctly isolates ownership but invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's remount-before-disposal test into overlap.mjs without importing B's immediate invalidation or uncaught exception policy. A's completion promise provides an observable rejection channel. No code graft is needed from B because ownership separation converges but the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra candidate-cross-review failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/overlap.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/overlap.mjs",
      "sha256": "70a5a93086d5fd3c2ddd2e1b07b795d0f2b56bb66df3034040eed2e41484c350",
      "bytes": 414,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { mount } from './caller.mjs';\nconst reports=[];\nconst a=mount('same',x=>reports.push(['old',x]));\nconst pending=a();\nconst b=mount('same',x=>reports.push(['new',x]));\nawait pending;\nassert.deepEqual(reports,[['old',true]]);\nawait b();\nassert.deepEqual(reports,[['old',true],['new',true]]);\nconsole.log('PASS graft: remount before old deferred disposal completes');\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/probe.mjs",
      "sha256": "7972e357f3d814cee41bb0d5ab89dc54738cfd8ea7e3d02c835cd07dfe4228e9",
      "bytes": 2874,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst source = 'committed-inputs/additional/cache/vendor/disposer-v1.mjs';\nconst pinned = Bun.spawnSync(['git', 'show', `${revision}:${source}`]);\nassert.equal(pinned.exitCode, 0);\nconst live = await Bun.file(new URL(`../../${source}`, import.meta.url)).arrayBuffer();\nassert.equal(Buffer.compare(Buffer.from(pinned.stdout), Buffer.from(live)), 0);\nassert.equal(createHash('sha256').update(Buffer.from(live)).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\n\nlet reports = 0;\nconst unmount = mount('key', ready => { assert.equal(ready, true); reports++; });\nconst completion = unmount();\nassert.equal(reports, 0, 'the pinned dependency defers its callback');\nassert.equal(unmount(), completion, 'double unmount returns the same completion');\nawait completion;\nassert.equal(reports, 1);\nassert.equal(unmount(), completion, 'unmount after completion remains idempotent');\n\nconst events = [];\nconst first = mount('same-key', ready => events.push(['first', ready]));\nconst second = mount('same-key', ready => events.push(['second', ready]));\nawait Promise.all([second(), first()]);\nassert.deepEqual(events, [['second', true], ['first', true]]);\n\nlet release;\nconst entry = createEntry('lifecycle', { owner: 'first' });\nconst pending = entry.dispose(() => new Promise(resolve => { release = resolve; }));\nassert.equal(entry.read().owner, 'first', 'disposing entries retain their value');\nconst other = createEntry('lifecycle', { owner: 'second' });\nrelease();\nawait pending;\nassert.throws(() => entry.read(), /disposed/);\nassert.equal(other.read().owner, 'second', 'same-key entries do not share state');\nawait other.dispose(() => undefined);\n\nconst reportError = new Error('report failure');\nawait assert.rejects(mount('throwing-report', () => { throw reportError; })(), error => error === reportError);\nawait assert.rejects(mount('rejecting-report', () => Promise.reject(reportError))(), error => error === reportError);\nconst failingEntry = createEntry('failure', { ready: true });\nconst failed = failingEntry.dispose(() => { throw reportError; });\nawait assert.rejects(failed, error => error === reportError);\nassert.throws(() => failingEntry.read(), /disposed/);\nassert.equal(failingEntry.dispose(() => assert.fail('must not restart')), failed);\nconst rejectingEntry = createEntry('rejection', 1);\nawait assert.rejects(rejectingEntry.dispose(() => Promise.reject(reportError)), error => error === reportError);\nassert.throws(() => rejectingEntry.read(), /disposed/);\nconsole.log('PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures');\n"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/synthesis/usage.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/usage.md",
      "sha256": "83dfee206ec8612ad2b3cb9ebd528c75ded55bf3eb489bf21e24c2b70ad198f5",
      "bytes": 448,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Call mount(key, report), then await its returned unmount function. Repeated unmount returns the same completion promise. Handle promise rejection from report failures. Each key labels an independent mount; it does not deduplicate or address shared storage. Entry reads remain legal during disposal and fail after completion. The actual pinned vendor queues a microtask. No promise of cleanup exists if a different vendor never invokes its callback."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/task.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/task.md",
      "sha256": "98bee99171904d2efe67045e42ae8392f28b215d41dd43acc0d372f693873a67",
      "bytes": 1181,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/terminal-b.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/terminal-b.txt",
      "sha256": "f506a383efedf09a3fe18cb3f5d5ffdba1c2931363b154650c949e5b926573ab",
      "bytes": 245,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "Completed arena-walkthrough-b. Input SHA fb7d9f00a700b1f6c3c88204d967433d99c11a73. Method arena, independent seat B. Actual model/effort unknown. See returned final in native durable history and candidate rationale/check-output for full details."
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/verification.json",
      "sha256": "c608e79c0b8dff7ba701617c5c70e3b626c99483eb9e7806ea7a7429e832b24f",
      "bytes": 347,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"arena-walkthrough/synthesis/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/arena-walkthrough.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough.result.md",
      "sha256": "b1a04c9a9c6da501e490b38cbe73b7ee2a1637d331031bbaaff0557e37828d6a",
      "bytes": 27386,
      "owners": [
        "grades-native-durable-02.json#0"
      ],
      "text": "# arena-walkthrough\n\nFollowed installed README to docs/workflows/arena.md, read it and required contracts, then ran Frame, Fan out, Cross-judge, Pick, Graft and Verify. Two distinct native candidate workers completed isolated artifacts and rationales. Parent read both fully after terminal completion and reran both probes before spawning a fresh read-only judge. Both parent and judge selected lifecycle-owned A. Parent adapted B remount coverage and documented rejected immediate invalidation/error policy. Synthesis and graft probes exited 0.\n\n## Supplied input\n\nThe complete supplied case is retained at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/supplied-input.json. Original fixture paths in that case were not used as mutable sources. Assignments used committed-inputs/ at verified task revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze is separately f4623636a287bea2aa79c4b2234a53d20a5f193c, version 0.1.0.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"arena-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge.\"\n    ],\n    \"expectedFull\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n    \"expectedReduced\": \"Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\"\n  },\n  \"caseId\": \"arena-walkthrough\",\n  \"baselineBatch\": \"batch-06\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\",\n  \"expectedFullUnchanged\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Follow README to Arena. Task: redesign local cache ownership so disposal can read its mounted value before invalidation without leaking global mutable cache state. Two candidates must use structurally distinct shapes (e.g. lifecycle-owned entry vs explicit value passed to disposal), each in an isolated owned directory with rationale. Keep 3-6 criterion parent rubric hidden until a fresh read-only judge starts after both candidates finish. Parent reads both, chooses/grafts/rejects and verifies synthesis with an adjacent evidence note.\",\n  \"missingPrerequisites\": [\n    \"Exact case SHA and two isolated writable candidates\",\n    \"Fresh read-only cross-judge after inspected terminal candidates\",\n    \"No model-diversity claim without actual observation\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}\n```\n\n## Actual response and integration\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis/evidence-note.md\n\nParent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/2/2/2 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B correctly isolates ownership but invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's remount-before-disposal test into overlap.mjs without importing B's immediate invalidation or uncaught exception policy. A's completion promise provides an observable rejection channel. No code graft is needed from B because ownership separation converges but the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra candidate-cross-review failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/judge/result.md\n\nAssignment: `arena-walkthrough-judge`  \nInput revision: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nObserved model: unknown\n\n| Rubric criterion | A | B |\n|---|---:|---:|\n| Deferred disposal observes original mounted ready value before invalidation | 2 | 1 |\n| No shared mutable map; overlapping keys cannot corrupt ownership | 2 | 2 |\n| Repeat teardown and throwing report have explicit deterministic cleanup | 2 | 2 |\n| Caller clarity and extension cost: coherent small API with rationale | 2 | 2 |\n| **Total** | **8/8** | **7/8** |\n\n**Recommend A as the maintainable base.** Its lifecycle entry retains the value while disposal runs, invalidates after reporting settles, and returns one completion promise for repeated teardown. Synchronous throws and asynchronous report rejection both invalidate and reject that promise.\n\nB satisfies the broader functional interpretation: deferred disposal receives its original mount’s value despite cache invalidation. It **does not satisfy the literal temporal requirement** that disposal read the value *before invalidation*: `cache.invalidate()` runs synchronously, and `reportDisposed(value, report)` runs in the later microtask. Its partial credit recognizes correct value ownership and reporting, not compliance with that ordering. This divergence follows the two assigned shapes and should remain explicit.\n\nConcrete integration choices:\n\n- **Graft B’s remount-before-disposal probe into A.** It explicitly checks an old mount disposing after a new same-key mount exists.\n- **Keep A’s completion and rejection contract.** Callers must await or handle unmount’s returned promise; that API change needs documentation.\n- **Reject B’s immediate invalidation for this literal requirement.**\n- **Reject B’s uncaught microtask exception policy as the base.** Cleanup is deterministic, but errors lack A’s caller-owned completion channel.\n- Keep both rationales’ ownership limitation: keys no longer provide shared caching or deduplication.\n\nI read the withheld rubric, task, every file in both candidate directories, both parent-check JSON outputs, and the pinned vendored disposer via `git show`. Both recorded parent checks exited `0`; their probes establish their respective contracts, so passing B’s probe does not establish the required temporal ordering. No writes or fresh executions were performed.\n\n## Variants\n\nTwo structurally distinct seats were exercised. No main-trial dropout occurred. Worker failure variants belong to the separate candidate-cross-review case.\n\n## Native assignments and observations\n\n```json\n[\n  {\n    \"worker\": \"walk_a\",\n    \"workerId\": \"/root/walk_a\",\n    \"threadId\": \"01a143d7-73b6-7720-a571-5e2721ab03eb\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-32-35-01a143d7-73b6-7720-a571-5e2721ab03eb.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_a.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_a-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"walk_b\",\n    \"workerId\": \"/root/walk_b\",\n    \"threadId\": \"01a143d7-86dc-7322-acfa-254c3911d921\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-32-40-01a143d7-86dc-7322-acfa-254c3911d921.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_b.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_b-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"walk_judge\",\n    \"workerId\": \"/root/walk_judge\",\n    \"threadId\": \"01a143da-50c2-7fb1-ba82-cd043be4d224\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-35-43-01a143da-50c2-7fb1-ba82-cd043be4d224.jsonl\",\n    \"rawArtifact\": \"evidence/native/walk_judge.jsonl\",\n    \"finalArtifact\": \"evidence/native/walk_judge-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  }\n]\n```\n\nEach main candidate received its case task.md plus dispatch-a.txt or dispatch-b.txt and the exact revision. Boundary dispatches embed the complete architect runner prompt. Candidate rubric was held in the parent file and not included in fork_turns:none assignments. Judges were fresh threads after terminal inspection. Exact native calls, returned objects, worker command outputs, terminal returns and encrypted inter-agent messages are retained while this session runs in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/native/root.jsonl and the named worker JSONL files. Method receipt, append-only assignment-events, task files, inspected output snapshots and artifact hashes are in the case directory. Global integer ordering is derived from actual timestamped dispatch calls and task_complete events, retaining each source ordinal in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/observed-order.json. It is event ordering, not synthetic timing telemetry.\n\nAll requested models/efforts inherited the parent. Native turn_context records independently identify observed gpt-6.1-sol with medium effort for these workers. Their self-reports said unknown because those workers did not have that observation. Distinct threads establish native worker identities; the identical observed model does not establish model diversity. No model aliases were invoked or model selection rejection invented.\n\n## Actual command outputs and exit status\n\nThese are raw captured command objects for the case, rather than service success counters. Nested commands and initial failed attempts also remain in native raw tool outputs. rg exit 1 with empty output means no match for the recorded query.\n\n```json\n[\n  {\n    \"path\": \"arena-walkthrough/parent-check-a.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/candidates/a/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/graft-verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/synthesis/overlap.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS graft: remount before old deferred disposal completes\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/baseline.json\",\n    \"argv\": [\n      \"bun\",\n      \"committed-inputs/additional/cache/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 1,\n    \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/synthesis/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS: pinned vendor bytes, deferred read, double unmount, overlapping mounts, invalidation, synchronous and asynchronous failures\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"arena-walkthrough/parent-check-b.json\",\n    \"argv\": [\n      \"bun\",\n      \"arena-walkthrough/candidates/b/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS actual vendored disposer matches input revision and manifest digest\\nPASS cache invalidation is synchronous and repeatable\\nPASS deferred report reads captured value, double unmount reports once\\nPASS overlapping same-key mounts and remount before disposal stay independent\\nPASS report exceptions remain observable as uncaught deferred exceptions\\nAll 5 checks passed\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Permissions, package provenance and limits\n\nThe user authorized native isolated workers, local writes, persistence and command execution in this root. No external services/actions, installation, configuration, commits, pushes, schedules or publishing were performed. No approval was inferred from source narratives. A local Markdown checklist substitutes for an absent todo tool. The session exposes no direct skill-invocation API; complete loaded workflows were executed inline. Catalog entries and source reads are kept distinct from registered invocation discovery.\n\nInstalled package has no Git metadata. A separate readable source Git repository contains the requested freeze. The comparison of all 726 tracked source paths found all installed and byte-identical except plugin.json author/developer metadata. Operative skills, references, README and linked walkthrough match the freeze. See /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/freeze-comparison.json. Do not describe the entire installed package as byte-identical or transfer a prior host result to this run.\n\nIsolation uses distinct local directories and one assigned writer, not Git worktrees or an OS-enforced worker-specific filesystem boundary. Initial cache ownership reservations used pending seat owners before native IDs were returned; original reservation records remain, and resolved native owners are recorded in receipt/events. This is an assignment-contract documentation limit. Method/resultMethod objects in receipts are coordinator normalization of observed one-artifact attempts and workflow order; original worker results declare the string arena. They are not a claim that workers returned structured sample metadata. Main dispatches occurred as separate native calls; they were not one atomic multi-spawn call.\n\nRaw inter-agent payloads are encrypted by the host in durable history. They are retained exactly; no decryption is claimed. Main task/dispatch files preserve the full readable assigned work and exact SHA. Initial source evidence copies serialized Buffers as JSON; those copies were corrected from actual installed bytes after the problem was observed. Workers that encountered this read the real installed or frozen Git files instead. Native history preserves the earlier failed reads and coordinator script error.\n\nPersistence is an observed current-session write/readback. It does not establish unattended recovery or a later-session reload. No structural validator result is used as a host behavioral conclusion. Earlier ephemeral-session failures remain untouched.\n\n## Independent outcome inspection\n\nRead-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery.\n\n### Corrections and final source availability\n\nIndependent reviewer findings retained verbatim in each outcome-review.md. Corrections after review: candidate-stage workflow status in boundary synthesis was replaced with completed status and a separate completion-status.md; full-source-legacy-scan.json now covers every implementation TypeScript file. Assignment event terminal label is now terminal-completed, distinguishing completion from later parent inspection shown in raw history. Earlier event files are preserved in native command outputs.\n\nInstalled 0.1.0 orchestration-contract path was available during initial source reads and full byte comparison, but existsSync now returns false. No package update or deletion was performed by this task. Cause is unknown. Final-source-availability.json preserves that observation. Review used the archived byte-matched source copy. No current installed-discovery claim follows.\n\nThe selected cross-review implementation does not promise synchronous disposer-scheduling failure recovery. The exact pinned vendor queues a microtask; report failures are separately covered. No new implementation change was warranted for an unrequested dependency behavior.\n\n\n## Artifacts\n\nComplete paths and SHA-256 digests: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/artifact-manifest.json. Primary receipt: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/method-receipt.json. Actual synthesis: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/arena-walkthrough/synthesis.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/arena-walkthrough/input",
      "owner": "grades-native-06.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-manifest.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-reads.txt",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input",
      "owner": "grades-native-06.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-manifest.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-reads.txt",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
  "globalLimits": [
    "Orchestrator receipt durations can include controller pauses; they are not inferred native case execution times or benchmark measurements.",
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
