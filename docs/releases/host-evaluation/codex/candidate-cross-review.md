# codex: candidate-cross-review

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "candidate-cross-review",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-durable-02.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.",
  "caseDefinition": {
    "id": "candidate-cross-review",
    "sourcePaths": [
      "skills/arena/SKILL.md"
    ],
    "prompt": "Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.",
    "requirements": [
      "At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.",
      "Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.",
      "Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.",
      "Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.",
      "Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.",
      "One survivor means incomplete competition, never a full arena pass."
    ],
    "expectedFull": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.",
    "expectedReduced": "Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.",
    "expectedBlocked": "Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.",
    "forbiddenClaims": [
      "Sequential role switching proves independent candidates or independent review.",
      "Requested model names prove actual model diversity.",
      "A judge begins while candidates still write.",
      "One survivor establishes full competition.",
      "Structural validation or a case definition establishes host pass.",
      "The rubric is supplied to candidates.",
      "Upstream autonomy permits external writes or implicit setup."
    ],
    "caseFile": "docs/parity/cases/skills/arena.json"
  },
  "registry": {
    "caseId": "candidate-cross-review",
    "caseFile": "docs/parity/cases/skills/arena.json",
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
      "attemptId": "grades-native-07.json#4",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "candidate-cross-review",
      "status": "reduced-pass",
      "grade": {
        "caseId": "candidate-cross-review",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_25",
          "item_26",
          "item_27",
          "item_31"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Exact taskGit revision/structured assignment-method receipt absent.",
          "Actual observed model diversity unknown."
        ],
        "review": "Two real isolated candidates finish, later fresh readonly judge compares complete outputs; parent selects B and runs7tests26assertions. Dropout and unavailable-worker limits retained. Required exact Git revision and full structured method receipt absent, so method cannot fully pass merely because artifacts/tests exist.",
        "responseArtifact": "fixtures/batch-07/candidate-cross-review.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.",
        "reducedExpected": "Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-07.json",
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
        "text": "# candidate-cross-review\n\n## Supplied input\n\nArena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\n\nThe installed source is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md. It and its required contracts and principle leaves were read through actual file tools. Package freeze supplied is f4623636a287bea2aa79c4b2234a53d20a5f193c. Only package 0.1.0 was used.\n\nConcrete cache requirement comes from the copied prepared fixture: retain ready values through the actual deferred disposal callback, release after reporting, and prevent old lifetimes deleting or overwriting replacements. Fixture data is not evidence of any service contact.\n\n## Actual output\n\nSelected candidate B, generation-owned handles. Its keyed cache exposes the newest generation; old handles keep their own value until released. Identity checks protect replacement and deletion. The selected implementation is candidate-cross-review/selected. Parent verification passed seven tests with 26 assertions, using the unchanged pinned local disposer.\n\nCandidate A uses shared counted leases and first-value-wins until all owners release. It fixes callback lifetime but changes the original per-mount replacement behavior. Candidate B is the stronger base for the supplied source. No material code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. The parent removed an obvious factory description comment while adapting B. The complete synthesis and rejections are in synthesis.md.\n\n## Observed method and artifacts\n\nNative candidates /root/cache_candidate_a and /root/cache_candidate_b wrote distinct authorized directories. The parent read both full implementations, callers, tests, rationales and verification artifacts. Both completed before /root/cache_judge was spawned as a fresh readonly judge. The judge returned scores and a base recommendation before selection and integration. It did not write candidate files.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Retention and finally cleanup | 2 | 2 |\n| Original fresh replacement behavior | 0 | 2 |\n| Stale lifetime safety | 2 | 2 |\n| Ownership/API tradeoffs | 2 | 2 |\n| Lifecycle coverage | 1 | 2 |\n\nThese are candidate scores, not evaluation grades. The parent agrees with the judge after inspecting the code. Its intermediate arithmetic said B=9; the displayed criteria total B=10. judge.md retains that correction. The fresh-replacement criterion is grounded in original cache.put and caller.mount, though more specific than the short task summary.\n\nCandidate A observed baseline failure exit 1 and six passing tests. Candidate B observed baseline failure exit 1 and seven passing tests. selected/cache.test.mjs was actually rerun by the parent. Original command arguments, stdout, stderr and exit codes are preserved in candidate verification.json files and synthesis-verification.json.\n\nRequested models and efforts for candidates were inherit-parent. Judge requested gpt-6-luna/high using current exposed tool documentation. All actual model and effort observations remain unknown. Requesting different selections proves no diversity. No aliases were supplied and no model selection rejection was observed. An earlier unrelated full-history forge worker dispatch failed with invalid thread-store/no rollout; fresh fork-none dispatch worked. Neither result is a model rejection.\n\n## Variants and limits\n\nThe normal two-candidate native-worker branch completed with a fresh judge. Task Git SHA is absent because the fixture root has no Git repository. Per-file digests identify copied inputs, but exact input-SHA assignment acceptance remains blocked. The package freeze is not substituted for task revision. No complete valid structured Arena method receipt or full Arena claim is made.\n\nThere are framing deviations. The rubric was written after candidate dispatch. The same substantive task and source grounding were used, but candidate wrapper wording differed. Immutable assignment records were not all persisted before dispatch. These limits remain explicit instead of retroactively rewriting dispatch history.\n\nDropout branch was an actual new worker /root/candidate_dropout, assignment cache-dropout-1. It required an exact task SHA, observed git rev-parse HEAD exit 128, and returned BLOCKED with no implementation. dropout/receipt.json preserves that result. It ran after the original competition as a separate negative variant, not an invented third competitor in the original ordering. With only candidate A retained as the survivor in that variant, competition is incomplete. The selected B artifact is not used to relabel that one-survivor variant as complete.\n\nUnavailable-worker branch was simulated, not enforced by this host. With worker calls deliberately omitted, the parent can compare the two shapes sequentially, but that leaves candidate independence, fresh independent judging and model diversity unmet. It does not produce a second full Arena result. The actual host did expose and successfully run workers in the normal branch.\n\nNo external service, configuration change, dependency install, commit, push, PR, message to others, publishing or schedule was performed. Worker messages were internal assignment/result operations only.\n",
        "artifact": {
          "path": "fixtures/batch-07/candidate-cross-review.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review.result.md",
          "sha256": "b0273bc111b69dae91a9157ff85a6e99a40c41c2e557ea76afe87d14e28cb986",
          "bytes": 5499
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-07.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-07.events.jsonl",
            "sha256": "26078a6d01730e84b6d57421e843541eb5b82f4c8b0cdd0b167ecf6636bbc630",
            "bytes": 636607,
            "eventReferences": [
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9c7e49e193d7e6fc52fd5690dadc8cb1c7dd9e7b66ad9c98a27361e9e40d31f5"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0b4bd71add486f8096424ea4384d9d00a84ea374bb3ef05e77fa7ec6a667fb9c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "650f5e9b7f40c3edf201a414197dd4b743093ff3cf4839c72768cbb308032037"
              },
              {
                "eventId": "item_25",
                "line": 48,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "faee36f0b43167185f291a747e52e89664840ada51b3d51dbfce4e914b671164",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_26",
                "line": 49,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "35e8ec07685b6e5df8a857303502e100e801a7aacd17ff9b13552d2c751a5698"
              },
              {
                "eventId": "item_26",
                "line": 50,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7261d690fa4bb9f801845f567d4eb161f7afba53bf59288f7467fb999cdbb907",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 51,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9bbd7c142dcb2190315310f1211e77d686156092c519bdf1ae8bcfcb911c12ec"
              },
              {
                "eventId": "item_27",
                "line": 52,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c3aa727b5bf17acd21d05aa984a11c6e2dd240b849c8ee06a075389096bc67b0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3d414913782b0e95aaf45c305c1fdca1f3ea5abcdce2891e23d7fb14a293978f"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "71440977a8a877d92807af16b9a2f0fa68b61440a86f9814aa56a5169107323d",
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
            "item_8",
            "item_25",
            "item_26",
            "item_27",
            "item_31"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-07.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    },
    {
      "attemptId": "grades-native-durable-02.json#2",
      "order": 202,
      "gradeFile": "grades-native-durable-02.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "candidate-cross-review",
      "status": "pass",
      "grade": {
        "caseId": "candidate-cross-review",
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
          "item_52",
          "item_53",
          "item_54",
          "item_58",
          "item_60",
          "item_72",
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
        "review": "Two real main candidates finish and are inspected before a fresh read-only judge sees rubric/paths; parent reads, selectsA, coherently grafts independent overlap/remount coverage and runs actual synthesis/graft probes. Native activity metadata confirms distinct threads. Separate thread-cap rejection, actual injected dropout exit7 and one surviving candidate remain incomplete competition; they do not erase the successful main trial or become a false full failure-trial competition.",
        "responseArtifact": "fixtures/durable-02/candidate-cross-review.result.md",
        "variantReview": [
          "Main independent candidate/terminal-inspection/fresh-judge/synthesis sequence supported by actual native order and inspected code, not receipt schema alone.",
          "Actual capacity rejection and failure injection retained as separate incomplete one-survivor trial."
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
          "fixtures/durable-02/candidate-cross-review/parent-check-a.json",
          "fixtures/durable-02/candidate-cross-review/parent-check-b.json",
          "fixtures/durable-02/candidate-cross-review/verification.json",
          "fixtures/durable-02/candidate-cross-review/graft-verification.json",
          "fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json",
          "fixtures/durable-02/candidate-cross-review/method-receipt.json",
          "fixtures/durable-02/evidence/native/index.json",
          "fixtures/durable-02/evidence/observed-order.json",
          "fixtures/durable-02/evidence/freeze-comparison.json",
          "fixtures/durable-02/evidence/final-source-availability.json"
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "fullExpected": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note."
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
        "text": "# candidate-cross-review\n\nRan a new two-worker cache competition, rather than reusing the walkthrough candidates. Parent inspected every terminal artifact and reran both probes before a fresh read-only judge. Both selected lifecycle-owned A. Parent adapted B coverage for both same-key teardown orders, kept A distinct-value lifetime test, and rejected the map plumbing and immediate invalidation policy. Synthesis and graft probes exited 0. Separate unavailable-worker and dropout trials are documented below.\n\n## Supplied input\n\nThe complete supplied case is retained at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/supplied-input.json. Original fixture paths in that case were not used as mutable sources. Assignments used committed-inputs/ at verified task revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze is separately f4623636a287bea2aa79c4b2234a53d20a5f193c, version 0.1.0.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"candidate-cross-review\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\",\n    \"requirements\": [\n      \"At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.\",\n      \"Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.\",\n      \"Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.\",\n      \"Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.\",\n      \"Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.\",\n      \"One survivor means incomplete competition, never a full arena pass.\"\n    ],\n    \"expectedFull\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n    \"expectedReduced\": \"Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.\",\n    \"expectedBlocked\": \"Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.\",\n    \"forbiddenClaims\": [\n      \"Sequential role switching proves independent candidates or independent review.\",\n      \"Requested model names prove actual model diversity.\",\n      \"A judge begins while candidates still write.\",\n      \"One survivor establishes full competition.\",\n      \"Structural validation or a case definition establishes host pass.\",\n      \"The rubric is supplied to candidates.\",\n      \"Upstream autonomy permits external writes or implicit setup.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/arena.json\"\n  },\n  \"caseId\": \"candidate-cross-review\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/arena.json\",\n  \"expectedFullUnchanged\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Arena the same local cache lifecycle task with at least two completed isolated candidates and rationales before a fresh read-only judge sees the labelled paths and parent rubric. Parent reads every candidate and records base/grafts/rejections/convergence and actual verification. Exercise candidate dropout as an additional separate trial; one survivor is incomplete competition, never full arena. Preserve unavailable-worker trial separately.\",\n  \"missingPrerequisites\": [\n    \"Two completed candidates and genuinely fresh judge\",\n    \"Explicit separate dropout trial with real terminal state\",\n    \"Root-created exact task SHA and evidence note\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}\n```\n\n## Actual response and integration\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/evidence-note.md\n\nParent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/1/2/1 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B removes the singleton but retains a caller-owned mutable map and coordination API. It also invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's coverage of both same-key teardown orders into overlap.mjs, also checking remount before old disposal completes, without importing B's immediate invalidation or uncaught exception policy. Retained A's stronger distinct-value lifetime test. A's completion promise provides an observable rejection channel. No implementation-code graft is needed from B because the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge/result.md\n\nAssignment: `candidate-cross-review-judge`  \nInput SHA: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nVerdict: **Choose A as the maintainable base.**\n\n| Criterion | A | B | Assessment |\n|---|---:|---:|---|\n| Original mounted value observed before invalidation | 2 | 1 | A delays invalidation until disposal settles. B observes its captured original value **after** synchronous invalidation. |\n| No shared mutable map; overlapping ownership protected | 2 | 1 | A isolates entries completely. B removes the global singleton and guards deletion by identity, but retains a mutable map shared between mounts using one cache. |\n| Repeat teardown and throwing report have deterministic cleanup | 2 | 2 | A returns the same completion promise and clears in `finally`, including async rejection. B invalidates before reporting and guards repeated teardown; synchronous report errors remain uncaught microtask exceptions by explicit design. |\n| Caller clarity and extension cost | 2 | 1 | A offers one lifecycle abstraction with observable completion. B requires cache plumbing plus `put/get/invalidate`, identity ownership, and a separate disposal boundary. |\n| **Total** | **8/8** | **5/8** | |\n\nA satisfies the literal ordering requirement. Its completion promise makes success, failure, and cleanup observable without depending on scheduling timing. The documented limitations are real: a never-settling report retains the entry, and awaiting its own teardown creates a dependency cycle.\n\nB is a valid captured-value design for a weaker requirement: disposal retains access despite cache invalidation. Its identity guard prevents an older mount from deleting a newer entry. It does not satisfy disposal-before-invalidation, and deleting the latest mount does not restore an older live mount.\n\n**Grafts:** Bring B’s explicit coverage of both same-key teardown orders into A’s synthesized verification. Preserve A’s distinct-value overlap test, which demonstrates ownership more strongly than callbacks that all report `true`.\n\n**Reject:** B’s immediate invalidation order, cache map plumbing, and uncaught report-error contract for this task. Do not combine both ownership models.\n\nEvidence reviewed: task, private rubric, all eight candidate files, both parent check records, judge assignment, and the pinned vendored disposer. Both parent probes exited `0`; neither was rerun by this read-only judge. No writes or external actions performed. Actual model: unknown.\n\n## Variants\n\nMain competition remains separate.\n\nUnavailable-worker trial: collaboration.spawn_agent rejected trial_unavailable with agent thread limit reached. No worker identity or artifact exists for that assignment. The availability failure is observed, not a simulated decision. No fallback model was selected.\n\nDropout trial: native trial_dropout executed a real Bun command with exit 7 and returned blocked assignment cross-dropout. It produced failure.json only, no candidate. Native worker thread completed its failure report; task assignment is blocked. No stop/cancellation was requested or claimed.\n\nIndependent trial_survivor produced an inspected proposal, implementation and rationale with matching full input revision. Parent reran its real vendor probe with exit 0. Exactly one candidate survived. Competition remains incomplete; no judge, competitive base pick, graft or trial synthesis is claimed. Failure output is excluded from main and survivor integration. No retry was attempted. See raw native thread captures and failure.json.\n\n\n## Native assignments and observations\n\n```json\n[\n  {\n    \"worker\": \"cross_a\",\n    \"workerId\": \"/root/cross_a\",\n    \"threadId\": \"01a143da-66c0-74d2-b055-c089062b2c60\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-35-49-01a143da-66c0-74d2-b055-c089062b2c60.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_a.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_a-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"cross_b\",\n    \"workerId\": \"/root/cross_b\",\n    \"threadId\": \"01a143db-01a5-7190-ba4d-4d283f32a093\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-36-28-01a143db-01a5-7190-ba4d-4d283f32a093.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_b.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_b-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"cross_judge\",\n    \"workerId\": \"/root/cross_judge\",\n    \"threadId\": \"01a143dd-1646-7b60-824b-165c988c5a5b\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-38-45-01a143dd-1646-7b60-824b-165c988c5a5b.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_judge.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_judge-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"trial_dropout\",\n    \"workerId\": \"/root/trial_dropout\",\n    \"threadId\": \"01a143de-0d27-79f1-83f8-983c664db936\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-39-48-01a143de-0d27-79f1-83f8-983c664db936.jsonl\",\n    \"rawArtifact\": \"evidence/native/trial_dropout.jsonl\",\n    \"finalArtifact\": \"evidence/native/trial_dropout-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"trial_survivor\",\n    \"workerId\": \"/root/trial_survivor\",\n    \"threadId\": \"01a143de-755f-72a1-8441-2109dfba66be\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-40-14-01a143de-755f-72a1-8441-2109dfba66be.jsonl\",\n    \"rawArtifact\": \"evidence/native/trial_survivor.jsonl\",\n    \"finalArtifact\": \"evidence/native/trial_survivor-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  }\n]\n```\n\nEach main candidate received its case task.md plus dispatch-a.txt or dispatch-b.txt and the exact revision. Boundary dispatches embed the complete architect runner prompt. Candidate rubric was held in the parent file and not included in fork_turns:none assignments. Judges were fresh threads after terminal inspection. Exact native calls, returned objects, worker command outputs, terminal returns and encrypted inter-agent messages are retained while this session runs in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/native/root.jsonl and the named worker JSONL files. Method receipt, append-only assignment-events, task files, inspected output snapshots and artifact hashes are in the case directory. Global integer ordering is derived from actual timestamped dispatch calls and task_complete events, retaining each source ordinal in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/observed-order.json. It is event ordering, not synthetic timing telemetry.\n\nAll requested models/efforts inherited the parent. Native turn_context records independently identify observed gpt-6.1-sol with medium effort for these workers. Their self-reports said unknown because those workers did not have that observation. Distinct threads establish native worker identities; the identical observed model does not establish model diversity. No model aliases were invoked or model selection rejection invented.\n\n## Actual command outputs and exit status\n\nThese are raw captured command objects for the case, rather than service success counters. Nested commands and initial failed attempts also remain in native raw tool outputs. rg exit 1 with empty output means no match for the recorded query.\n\n```json\n[\n  {\n    \"path\": \"candidate-cross-review/parent-check-a.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/candidates/a/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/trials/dropout/failure.json\",\n    \"assignmentId\": \"cross-dropout\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"outputOwner\": \"/root/trial_dropout\",\n    \"terminalStatus\": \"blocked\",\n    \"authorizedFailureInjection\": true,\n    \"retryCount\": 0,\n    \"candidateProduced\": false,\n    \"eligibleForIntegration\": false,\n    \"argv\": [\n      \"bun\",\n      \"-e\",\n      \"console.log(\\\"injected candidate failure\\\"); process.exit(7)\"\n    ],\n    \"command\": \"bun -e 'console.log(\\\"injected candidate failure\\\"); process.exit(7)'\",\n    \"output\": \"injected candidate failure\\n\",\n    \"exitCode\": 7,\n    \"rawCommandResult\": {\n      \"chunk_id\": \"17876f\",\n      \"wall_time_seconds\": 0.000005375,\n      \"exit_code\": 7,\n      \"original_token_count\": 7,\n      \"output\": \"injected candidate failure\\n\"\n    }\n  },\n  {\n    \"path\": \"candidate-cross-review/trials/survivor-parent-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/trials/survivor/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"Baseline reproduced deferred read failure against committed vendor.\\nPASS: vendor pin, lifecycle read through completion, invalidation, repeated teardown, same-key overlap, sync and async report errors.\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/graft-verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/synthesis/overlap.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS graft: remount before old deferred disposal completes\\nPASS graft: both same-key teardown orders\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/synthesis/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/parent-check-b.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/candidates/b/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"baseline reproduced deferred TypeError using exact committed modules\\nPASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Permissions, package provenance and limits\n\nThe user authorized native isolated workers, local writes, persistence and command execution in this root. No external services/actions, installation, configuration, commits, pushes, schedules or publishing were performed. No approval was inferred from source narratives. A local Markdown checklist substitutes for an absent todo tool. The session exposes no direct skill-invocation API; complete loaded workflows were executed inline. Catalog entries and source reads are kept distinct from registered invocation discovery.\n\nInstalled package has no Git metadata. A separate readable source Git repository contains the requested freeze. The comparison of all 726 tracked source paths found all installed and byte-identical except plugin.json author/developer metadata. Operative skills, references, README and linked walkthrough match the freeze. See /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/freeze-comparison.json. Do not describe the entire installed package as byte-identical or transfer a prior host result to this run.\n\nIsolation uses distinct local directories and one assigned writer, not Git worktrees or an OS-enforced worker-specific filesystem boundary. Initial cache ownership reservations used pending seat owners before native IDs were returned; original reservation records remain, and resolved native owners are recorded in receipt/events. This is an assignment-contract documentation limit. Method/resultMethod objects in receipts are coordinator normalization of observed one-artifact attempts and workflow order; original worker results declare the string arena. They are not a claim that workers returned structured sample metadata. Main dispatches occurred as separate native calls; they were not one atomic multi-spawn call.\n\nRaw inter-agent payloads are encrypted by the host in durable history. They are retained exactly; no decryption is claimed. Main task/dispatch files preserve the full readable assigned work and exact SHA. Initial source evidence copies serialized Buffers as JSON; those copies were corrected from actual installed bytes after the problem was observed. Workers that encountered this read the real installed or frozen Git files instead. Native history preserves the earlier failed reads and coordinator script error.\n\nPersistence is an observed current-session write/readback. It does not establish unattended recovery or a later-session reload. No structural validator result is used as a host behavioral conclusion. Earlier ephemeral-session failures remain untouched.\n\n## Independent outcome inspection\n\nRead-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery.\n\n### Corrections and final source availability\n\nIndependent reviewer findings retained verbatim in each outcome-review.md. Corrections after review: candidate-stage workflow status in boundary synthesis was replaced with completed status and a separate completion-status.md; full-source-legacy-scan.json now covers every implementation TypeScript file. Assignment event terminal label is now terminal-completed, distinguishing completion from later parent inspection shown in raw history. Earlier event files are preserved in native command outputs.\n\nInstalled 0.1.0 orchestration-contract path was available during initial source reads and full byte comparison, but existsSync now returns false. No package update or deletion was performed by this task. Cause is unknown. Final-source-availability.json preserves that observation. Review used the archived byte-matched source copy. No current installed-discovery claim follows.\n\nThe selected cross-review implementation does not promise synchronous disposer-scheduling failure recovery. The exact pinned vendor queues a microtask; report failures are separately covered. No new implementation change was warranted for an unrequested dependency behavior.\n\n\n## Artifacts\n\nComplete paths and SHA-256 digests: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/artifact-manifest.json. Primary receipt: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/method-receipt.json. Actual synthesis: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis.\n",
        "artifact": {
          "path": "fixtures/durable-02/candidate-cross-review.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review.result.md",
          "sha256": "a56f539bd6cc119865e55a5ddf0176bffb4dc71e1adc765ed8b3877d16a7856a",
          "bytes": 30873
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
                "eventId": "item_52",
                "line": 100,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ad33d790d3b65157cd78ba60a47250f8e0bd3c32c8c51e9be9c0b31da35d67e8"
              },
              {
                "eventId": "item_52",
                "line": 101,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2acfd16a116697b91ef7c5f3287a26ab16426df6e11555d56e4322b3219e501a",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_53",
                "line": 102,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6d0b00301fcf8ce28feba31dc28563c0a9c44ff3b9af8a7478b5d1a96aa8ec82"
              },
              {
                "eventId": "item_53",
                "line": 103,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b3834bde0a306a8f0c34135ad9d6fd49faed2f035c0f9e35594db17e97580cd1",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_54",
                "line": 104,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e75c14b2abb622205685afaf8aa8df7bb8348ceab72e0d1466f3a175fbf782da"
              },
              {
                "eventId": "item_54",
                "line": 105,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d6cd3427879c5e8fad30f0f6570378d46bad3508799f90b428da262ea3c39c22",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_58",
                "line": 111,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c8306cf8a7ed89771a8b13f0020686a8501a1350dce1e9fb64ac307983bd1690"
              },
              {
                "eventId": "item_58",
                "line": 112,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d25b8f752c444a96685bc757f6e0b30adcbf5e2407336e1b8a55056e71d87e68",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_60",
                "line": 115,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "81cfcbd0f7882b740d36036b2422703970ec778e440139bd837113cd51b4fe24"
              },
              {
                "eventId": "item_60",
                "line": 116,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7de005686e8ef569f25a9ac1e94d9eff82bf53f45e52af0f736034aa1d3941ab",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_72",
                "line": 138,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4e46d7c036485d7612f0793f16429caf32a492d7e45151c7354fce8a6c42829d"
              },
              {
                "eventId": "item_72",
                "line": 139,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "19d9ba0b532a4bae42966c5d50cf477a38af3b44f8615b4431f7d2bc9eae4be4",
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
            "path": "fixtures/durable-02/candidate-cross-review/parent-check-a.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-a.json",
            "sha256": "639694cc8fb31dba8e68c69aef80495fe1fd98607341898bef6bbcb3c712f417",
            "bytes": 572
          },
          {
            "path": "fixtures/durable-02/candidate-cross-review/parent-check-b.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-b.json",
            "sha256": "ff2a7ebe3982ac6ec5d4540babb2816518bedf76afcdca5692ba86dade7a1298",
            "bytes": 417
          },
          {
            "path": "fixtures/durable-02/candidate-cross-review/verification.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/verification.json",
            "sha256": "b49a15680b59de0f7d0b2035607fb7e27a03d5b08e6b5d9debebdf14d9c02a20",
            "bytes": 569
          },
          {
            "path": "fixtures/durable-02/candidate-cross-review/graft-verification.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/graft-verification.json",
            "sha256": "0495e8e3b89ad80eb54a1a4c9fc008c670106389093ec005e1911bf576bffc9a",
            "bytes": 326
          },
          {
            "path": "fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json",
            "sha256": "830ba79f479b42fa53f0cc74e81ab54dc1605248fb52dd53b42f416a5ff1070b",
            "bytes": 735
          },
          {
            "path": "fixtures/durable-02/candidate-cross-review/method-receipt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/method-receipt.json",
            "sha256": "60fb1c197d18aa57588b01a4884a2d6a257441892dcce844b7596a888127c6c9",
            "bytes": 5846
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
            "item_52",
            "item_53",
            "item_54",
            "item_58",
            "item_60",
            "item_72",
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
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/README.md",
      "sha256": "bce6ca314730b60a78520358702c99e55882b9d9b3cf6320bf5f2c45a3392568",
      "bytes": 2970,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# Candidate A\n\nThe caller acquires one lease per mount and releases it only after the vendored deferred disposal callback reports. The release runs in `finally`, including when reporting throws. Multiple mounts of one key share the current entry. Each lease releases at most once, and deletion checks entry identity.\n\nCaller usage is the design boundary:\n\n```js\nconst lease = acquire(key, { ready: true });\n// Inside the disposer's callback:\ntry { report(lease.value.ready); }\nfinally { lease.release(); }\n```\n\nThe cache exports `acquire` and `get`. `acquire` returns the value and a release capability tied to that entry. `get` preserves ordinary cache reads but does not acquire a lease. There is no public `put`, `invalidate`, replacement, or reference-count mutation. The caller cannot publish a stale deferred write. A fresh generation can start once the previous generation has no owners, and a repeated old release cannot remove it. For one key, the first value wins until all leases release. Later acquire calls do not overwrite it.\n\n`mount` remains the caller's only export. Its returned unmount function is idempotent, so repeated cleanup cannot queue duplicate reports. Reading the lease inside disposal also avoids accidentally reporting a different generation's value.\n\nRejected alternatives:\n\n- Restoring `setTimeout` relies on scheduler ordering and leaves cache lifetime detached from the callback that needs the value.\n- Deleting immediately and guarding `get(key)?.ready` avoids a throw but loses the required ready report.\n- A captured value with immediate cache invalidation reports correctly but violates retention through reporting.\n- A compare-and-delete token without lease counting lets one unmount evict an entry another active mount still needs.\n- Public replace and invalidate operations require extra lifecycle rules. This fixture has no replacement caller, so the API prevents replacement while an entry has owners.\n\nThe supplied after-state probe fails with a TypeError under Bun. The six candidate tests use the actual copied pinned disposer and pass. They cover retention during reporting, overlapping mounts, stale release after a new generation, repeated unmount, a mount created during reporting, and report failure with cleanup. `verification.json` records exact commands, outputs, and exit codes.\n\nThe supported callback contract is synchronous reporting, matching the fixture. An asynchronous report that returns a promise would need a separate decision about whether its settlement owns the lease. There is no claim about any public dependency or other disposer implementation. No service, installation, commit, or configuration change was performed.\n\nAssignment `cache-a-1` uses package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`. `input-digest.json` records every copied input hash and their aggregate content digest. Requested model and effort are inherited; actual values are unobserved. No parent rubric was supplied.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/artifacts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/artifacts.json",
      "sha256": "1f263ff783d4a887bc2a75c8d50b44084bd3a08dd27385340707e252b6c02277",
      "bytes": 1073,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"artifacts\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"bce6ca314730b60a78520358702c99e55882b9d9b3cf6320bf5f2c45a3392568\"\n    },\n    {\n      \"path\": \"assignment.json\",\n      \"sha256\": \"34e394a7c317b30b50cd43f56d94262adc4e70e1f196838d9afff55e159dee29\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"eecd30f1c41ceef55ddf6c107ca356ed688f77938ea764a9a0facedac3b430f2\"\n    },\n    {\n      \"path\": \"cache.test.mjs\",\n      \"sha256\": \"6ab47769367dd5f73c00fdc994edb2b6a31f3af08bcae2616d91137881b608c9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"7900387370c14152237da8e8f1a180d2d2bfa75488ec28209e2eb04ece9db157\"\n    },\n    {\n      \"path\": \"input-digest.json\",\n      \"sha256\": \"74fc9c5db9764d63293a8955431320090757af201f4ca55fa33b173824ad40c3\"\n    },\n    {\n      \"path\": \"throw-probe.mjs\",\n      \"sha256\": \"59f873ebb286c111eef407560023c422c53148bc7e7d4bc60249c4f9cdb523f4\"\n    },\n    {\n      \"path\": \"verification.json\",\n      \"sha256\": \"e7fe060b62479ccf778abe3e0c67aef803e587f41f3b163f8e3385051d572872\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/assignment.json",
      "sha256": "34e394a7c317b30b50cd43f56d94262adc4e70e1f196838d9afff55e159dee29",
      "bytes": 468,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"workerId\": \"/root/cache_candidate_a\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"inputContentSha256\": \"1573556b38b3867e89399540f97bfd6a490b7a3e6c4942f5b98700b7c2da35f7\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"role\": \"candidate\",\n  \"rubricProvided\": false,\n  \"outputPath\": \"candidate-cross-review/candidate-a\"\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/cache.mjs",
      "sha256": "eecd30f1c41ceef55ddf6c107ca356ed688f77938ea764a9a0facedac3b430f2",
      "bytes": 656,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "const entries = new Map();\n\n// Acquire synchronously. Mounts of the same key share its current value.\nexport function acquire(key, value) {\n  let entry = entries.get(key);\n  if (!entry) {\n    entry = { value, leases: 0 };\n    entries.set(key, entry);\n  }\n  entry.leases++;\n  let released = false;\n  return {\n    value: entry.value,\n    release() {\n      if (released) return;\n      released = true;\n      if (--entry.leases === 0 && entries.get(key) === entry) {\n        entries.delete(key);\n      }\n    },\n  };\n}\n\n// A read never acquires ownership. Teardown reads through its lease instead.\nexport function get(key) {\n  return entries.get(key)?.value;\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/cache.test.mjs",
      "sha256": "6ab47769367dd5f73c00fdc994edb2b6a31f3af08bcae2616d91137881b608c9",
      "bytes": 2702,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { acquire, get } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\ntest('entry survives unmount until the actual deferred report returns', async () => {\n  const observed = [];\n  const unmount = mount('lifetime', ready => {\n    observed.push(ready);\n    expect(get('lifetime').ready).toBe(true);\n  });\n  unmount();\n  expect(get('lifetime').ready).toBe(true);\n  expect(observed).toEqual([]);\n  await Promise.resolve();\n  expect(observed).toEqual([true]);\n  expect(get('lifetime')).toBeUndefined();\n});\n\ntest('overlapping mounts retain the same entry until both reports finish', async () => {\n  const reports = [];\n  const first = mount('overlap', ready => reports.push(['first', ready]));\n  const original = get('overlap');\n  first();\n  const second = mount('overlap', ready => reports.push(['second', ready]));\n  expect(get('overlap')).toBe(original);\n  await Promise.resolve();\n  expect(reports).toEqual([['first', true]]);\n  expect(get('overlap')).toBe(original);\n  second();\n  await Promise.resolve();\n  expect(reports).toEqual([['first', true], ['second', true]]);\n  expect(get('overlap')).toBeUndefined();\n});\n\ntest('a stale release cannot delete or replace a fresh generation', () => {\n  const old = acquire('generation', { ready: true, generation: 1 });\n  old.release();\n  const replacement = acquire('generation', { ready: true, generation: 2 });\n  old.release();\n  expect(get('generation')).toBe(replacement.value);\n  expect(get('generation').generation).toBe(2);\n  replacement.release();\n  expect(get('generation')).toBeUndefined();\n});\n\ntest('repeated unmount queues only one report and cannot release another mount', async () => {\n  let count = 0;\n  const first = mount('repeat', () => count++);\n  const second = mount('repeat', () => count++);\n  first();\n  first();\n  await Promise.resolve();\n  expect(count).toBe(1);\n  expect(get('repeat').ready).toBe(true);\n  second();\n  await Promise.resolve();\n  expect(count).toBe(2);\n  expect(get('repeat')).toBeUndefined();\n});\n\ntest('a mount created within reporting remains alive after the old release', async () => {\n  let next;\n  const first = mount('reentrant', () => {\n    next = mount('reentrant', () => {});\n  });\n  first();\n  await Promise.resolve();\n  expect(get('reentrant').ready).toBe(true);\n  next();\n  await Promise.resolve();\n  expect(get('reentrant')).toBeUndefined();\n});\n\ntest('a throwing report releases the cache through the real disposer', () => {\n  const result = Bun.spawnSync([process.execPath, 'throw-probe.mjs'], {\n    cwd: import.meta.dir,\n  });\n  expect(result.exitCode).toBe(0);\n  expect(result.stdout.toString()).toContain('report failed; cache released');\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/caller.mjs",
      "sha256": "7900387370c14152237da8e8f1a180d2d2bfa75488ec28209e2eb04ece9db157",
      "bytes": 455,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './input/vendor/disposer-v1.mjs';\nimport { acquire } from './cache.mjs';\n\nexport function mount(key, report) {\n  const lease = acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(lease.value.ready);\n    } finally {\n      lease.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/input-digest.json",
      "sha256": "74fc9c5db9764d63293a8955431320090757af201f4ca55fa33b173824ad40c3",
      "bytes": 1095,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"algorithm\": \"sha256 of sorted relative-path file digest manifest, lines sha256 two spaces path newline\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    }\n  ],\n  \"digest\": \"1573556b38b3867e89399540f97bfd6a490b7a3e6c4942f5b98700b7c2da35f7\"\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/throw-probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/throw-probe.mjs",
      "sha256": "59f873ebb286c111eef407560023c422c53148bc7e7d4bc60249c4f9cdb523f4",
      "bytes": 452,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { mount } from './caller.mjs';\nimport { get } from './cache.mjs';\n\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throws', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 0));\nif (caught?.message !== 'report failed' || get('throws') !== undefined) {\n  throw new Error('Report error or cache cleanup was lost');\n}\nconsole.log('report failed; cache released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/verification.json",
      "sha256": "e7fe060b62479ccf778abe3e0c67aef803e587f41f3b163f8e3385051d572872",
      "bytes": 1220,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"results\": [\n    {\n      \"name\": \"baseline\",\n      \"command\": [\n        \"bun\",\n        \"candidate-cross-review/candidate-a/input/probe.mjs\"\n      ],\n      \"exitCode\": 1,\n      \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"name\": \"candidate\",\n      \"command\": [\n        \"bun\",\n        \"test\",\n        \"candidate-cross-review/candidate-a/cache.test.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n      \"stderr\": \"\\ncandidate-cross-review/candidate-a/cache.test.mjs:\\n(pass) entry survives unmount until the actual deferred report returns [0.21ms]\\n(pass) overlapping mounts retain the same entry until both reports finish [0.07ms]\\n(pass) a stale release cannot delete or replace a fresh generation [0.02ms]\\n(pass) repeated unmount queues only one report and cannot release another mount [0.05ms]\\n(pass) a mount created within reporting remains alive after the old release [0.04ms]\\n(pass) a throwing report releases the cache through the real disposer [11.60ms]\\n\\n 6 pass\\n 0 fail\\n 21 expect() calls\\nRan 6 tests across 1 file. [18.00ms]\\n\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/README.md",
      "sha256": "5a23a05f777224b13db2a26059017c01a7550a481221aa94938dd98cbf2df7b3",
      "bytes": 4803,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# Cache candidate B\n\nUse a mount-owned cache handle. The disposer reads that handle before releasing it.\n\n```js\nimport { mount } from './implementation/caller.mjs';\nimport { cache } from './implementation/cache.mjs';\n\nconst unmount = mount('panel', ready => console.log(ready));\nunmount();\nconsole.log(cache.get('panel').ready); // true until the disposal microtask runs\nawait new Promise(resolve => queueMicrotask(resolve));\nconsole.log(cache.get('panel')); // undefined\n```\n\nThe complete caller is in `implementation/caller.mjs`. Its unmount callback schedules the exact supplied vendored disposer once. Inside the disposal callback, `report(entry.read().ready)` runs before `entry.release()`. A `finally` releases the entry even if reporting throws. It does not catch or suppress the reporting error.\n\n## Cache API\n\n`implementation/cache.mjs` exports `createCache()` for an independent cache and the shared `cache` used by `mount`.\n\n| Operation | Contract |\n| --- | --- |\n| `cache.acquire(key, initialValue)` | Installs a new current entry and returns its owning handle. Superseded handles retain their own value until released. |\n| `cache.get(key)` | Returns the current value, or `undefined` when no current entry exists. |\n| `handle.read()` | Returns this handle's value, even after another mount replaces the key. Throws after release. |\n| `handle.replace(nextValue)` | Updates only while this handle is current and unreleased. Returns `false` for stale or released handles. |\n| `handle.release()` | Drops this handle's value. Deletes the keyed entry only if this handle still owns it. Returns `false` after the first release. |\n\nFor asynchronous producers, acquire before starting work and publish through that same handle:\n\n```js\nconst entry = cache.acquire('panel', { ready: true });\nconst result = await loadPanel();\nif (!entry.replace({ ready: true, result })) {\n  // Another mount replaced this generation, or this mount already released it.\n}\n```\n\nThis is a replacement of the original `put/get/invalidate` contract. Migrate mount ownership and producer writes together. A stale producer must retain its handle rather than call `acquire` again when work completes.\n\n## Why this shape\n\nThe original caller disposes asynchronously and invalidates synchronously. Its callback subsequently reads `undefined.ready`. Delaying invalidation with a timer repairs that one ordering but leaves a key-reuse race. An older timer can delete a newer mount's entry.\n\nA handle separates a mount's retained value from whichever mount currently owns the key. Entry identity checks protect both writes and deletion. Deleting a current entry never reveals an older generation. If a newer mount unmounts first, an older live mount can still report its own ready value, but key lookup remains empty until a later mount acquires the key.\n\nThe public key lookup deliberately returns only the current generation. Disposal must read its own handle. A key lookup inside old teardown cannot identify which mount it belongs to.\n\nI considered these alternatives:\n\n- Moving `invalidate(key)` into the disposal callback fixes the missing value but still allows old teardown to delete a replacement.\n- Comparing values during invalidation protects deletion but does not stop stale reads or late producer writes. Dedicated handles make all three operations use the same ownership check.\n- Keeping a set of all generations in the cache would expose more bookkeeping than callers need. Each mount's handle already retains its generation, and release clears its value.\n- A reference count would keep a shared entry alive but would conflate replacement with shared ownership. This fixture creates a fresh ready entry on every mount.\n\nValues remain ordinary JavaScript references. Callers should use `replace` rather than mutate retained objects. Reporting is synchronous, as in the supplied caller. The cache releases after `report` returns or throws; it does not await a returned promise. If a disposer never invokes its callback, its handle remains retained. The local pinned disposer always queues that callback in a microtask.\n\n## Verification\n\nRun `bun test candidate-cross-review/candidate-b/implementation/cache.test.mjs` from the fixture root.\n\nSeven tests cover retention during reporting, final release, old and new mount teardown in both orders, rejected stale producer writes, duplicate unmount/release, reentrant mounting during reporting, and release after a reporter throws. The last case runs in a subprocess so an uncaught reporting error cannot interfere with the test runner.\n\nThe original copied probe fails with `TypeError` under Bun. The candidate uses the unchanged vendored dependency bytes. These checks establish behavior for the exact local fixture only. They make no claim about a public dependency.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.mjs",
      "sha256": "aff32bea0c029542adca1c7f652e3c49087ccf6f6f934a15ae654faaf75a5547",
      "bytes": 920,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "/** A keyed cache whose handles own one generation until release. */\nexport function createCache() {\n  const current = new Map();\n\n  return {\n    get(key) { return current.get(key)?.value; },\n    acquire(key, initialValue) {\n      const entry = { value: initialValue };\n      let released = false;\n      current.set(key, entry);\n\n      return {\n        read() {\n          if (released) throw new Error('Cache handle already released');\n          return entry.value;\n        },\n        replace(nextValue) {\n          if (released || current.get(key) !== entry) return false;\n          entry.value = nextValue;\n          return true;\n        },\n        release() {\n          if (released) return false;\n          released = true;\n          if (current.get(key) === entry) current.delete(key);\n          entry.value = undefined;\n          return true;\n        },\n      };\n    },\n  };\n}\n\nexport const cache = createCache();\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.test.mjs",
      "sha256": "b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0",
      "bytes": 3768,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { describe, expect, test } from 'bun:test';\nimport { createCache, cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst flushDisposal = () => new Promise(resolve => queueMicrotask(resolve));\n\ndescribe('ownership and deferred disposal', () => {\n  test('retains ready through reporting and releases after reporting', async () => {\n    const observed = [];\n    const unmount = mount('single', ready => {\n      observed.push([ready, cache.get('single')?.ready]);\n    });\n    unmount();\n    expect(cache.get('single')).toEqual({ ready: true });\n    expect(observed).toEqual([]);\n    await flushDisposal();\n    expect(observed).toEqual([[true, true]]);\n    expect(cache.get('single')).toBeUndefined();\n  });\n\n  test('old callback reads its own ready value and cannot delete a replacement', async () => {\n    const observed = [];\n    const stopOld = mount('reused', ready => observed.push(['old', ready]));\n    stopOld();\n    const stopNew = mount('reused', ready => observed.push(['new', ready]));\n    await flushDisposal();\n    expect(observed).toEqual([['old', true]]);\n    expect(cache.get('reused')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(observed).toEqual([['old', true], ['new', true]]);\n    expect(cache.get('reused')).toBeUndefined();\n  });\n\n  test('replacement unmounting first still leaves old handle readable', async () => {\n    const observed = [];\n    const stopOld = mount('reverse', ready => observed.push(['old', ready]));\n    const stopNew = mount('reverse', ready => observed.push(['new', ready]));\n    stopNew();\n    stopOld();\n    await flushDisposal();\n    expect(observed).toEqual([['new', true], ['old', true]]);\n    expect(cache.get('reverse')).toBeUndefined();\n  });\n\n  test('a stale asynchronous producer cannot overwrite a replacement', () => {\n    const local = createCache();\n    const old = local.acquire('key', { ready: true, id: 'old' });\n    const replacement = local.acquire('key', { ready: true, id: 'new' });\n    expect(old.replace({ ready: false, id: 'late-old' })).toBe(false);\n    expect(old.read()).toEqual({ ready: true, id: 'old' });\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    old.release();\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    expect(replacement.replace({ ready: false, id: 'updated-new' })).toBe(true);\n    expect(local.get('key')).toEqual({ ready: false, id: 'updated-new' });\n    replacement.release();\n    expect(local.get('key')).toBeUndefined();\n  });\n\n  test('unmount and release are idempotent', async () => {\n    let count = 0;\n    const stop = mount('duplicate', () => count++);\n    stop(); stop();\n    await flushDisposal();\n    stop();\n    await flushDisposal();\n    expect(count).toBe(1);\n    const local = createCache();\n    const handle = local.acquire('key', 1);\n    expect(handle.release()).toBe(true);\n    expect(handle.release()).toBe(false);\n    expect(handle.replace(2)).toBe(false);\n    expect(() => handle.read()).toThrow('already released');\n  });\n\n  test('report may synchronously mount a replacement without old release deleting it', async () => {\n    let stopNew;\n    const stopOld = mount('reentrant', () => {\n      stopNew = mount('reentrant', () => {});\n    });\n    stopOld();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toBeUndefined();\n  });\n\n  test('a throwing reporter still releases its entry', () => {\n    const result = Bun.spawnSync([process.execPath, new URL('./throwing-reporter.mjs', import.meta.url).pathname]);\n    expect(result.exitCode).toBe(0);\n    expect(result.stdout.toString()).toContain('throw observed; entry released');\n  });\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/caller.mjs",
      "sha256": "8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34",
      "bytes": 454,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './vendor/disposer-v1.mjs';\nimport { cache } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = cache.acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(entry.read().ready);\n    } finally {\n      entry.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/throwing-reporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/throwing-reporter.mjs",
      "sha256": "9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc",
      "bytes": 410,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throw', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 5));\nif (caught?.message !== 'report failed' || cache.get('throw') !== undefined) process.exit(1);\nconsole.log('throw observed; entry released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/input-digest.json",
      "sha256": "d39add47ed04ef0102dec4155c4f5c0496f3ecea1ca486147e15bd3a7911be48",
      "bytes": 1071,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"algorithm\": \"sha256 of JSON.stringify(sorted array of path and sha256 records)\",\n  \"digest\": \"0c36430ae8b0398d1853696b1fed0cb0a7aadb2b785a6d8e954376516b50080e\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/output-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/output-digest.json",
      "sha256": "42dc97cb373c5daa2ab60e77c6f4b1b2168516b8ba675b474508f2fbf5152b78",
      "bytes": 2299,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-b-1\",\n  \"outputSha256\": \"7408ca18cce4dddf132899f4d11aefade59021d9d1b11c9eb16d9090e28f7b62\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"5a23a05f777224b13db2a26059017c01a7550a481221aa94938dd98cbf2df7b3\"\n    },\n    {\n      \"path\": \"implementation/cache.mjs\",\n      \"sha256\": \"aff32bea0c029542adca1c7f652e3c49087ccf6f6f934a15ae654faaf75a5547\"\n    },\n    {\n      \"path\": \"implementation/cache.test.mjs\",\n      \"sha256\": \"b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0\"\n    },\n    {\n      \"path\": \"implementation/caller.mjs\",\n      \"sha256\": \"8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34\"\n    },\n    {\n      \"path\": \"implementation/throwing-reporter.mjs\",\n      \"sha256\": \"9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc\"\n    },\n    {\n      \"path\": \"implementation/vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    },\n    {\n      \"path\": \"input-digest.json\",\n      \"sha256\": \"d39add47ed04ef0102dec4155c4f5c0496f3ecea1ca486147e15bd3a7911be48\"\n    },\n    {\n      \"path\": \"input/README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"input/cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"input/caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"input/invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"input/manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"input/probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"input/vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    },\n    {\n      \"path\": \"task-input.md\",\n      \"sha256\": \"d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b\"\n    },\n    {\n      \"path\": \"verification.json\",\n      \"sha256\": \"23c13584548c4edaf3719c5f85d8deac8012fad0b30cc383113381687412eaab\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/task-input.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/task-input.md",
      "sha256": "d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b",
      "bytes": 720,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Produce isolated candidate B for the local cache API from ../shared/additional/cache.\nThe cache must retain its ready entry until the deferred disposer reports on unmount, then release the entry. Stale concurrent mounts must not overwrite or delete replacements.\nDeliver the whole API with caller-first usage, implementation, rationale naming alternatives, and meaningful tests. Preserve a source copy in input. Write only candidate-cross-review/candidate-b. Do not use live services, install, commit, or change configuration. Run scripts with Bun.\nAssignment: cache-b-1. Requested model and effort: inherit-parent. Actual model and effort: unknown.\nInstruction package freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/verification.json",
      "sha256": "23c13584548c4edaf3719c5f85d8deac8012fad0b30cc383113381687412eaab",
      "bytes": 3165,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-b-1\",\n  \"role\": \"candidate\",\n  \"outputPath\": \"candidate-cross-review/candidate-b\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"inputRevision\": \"unknown; fixture root has no Git repository\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"taskInputSha256\": \"d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b\",\n  \"fixtureInputSha256\": \"0c36430ae8b0398d1853696b1fed0cb0a7aadb2b785a6d8e954376516b50080e\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one independently generated API candidate, verified against the pinned local disposer\",\n    \"order\": 1\n  },\n  \"tests\": [\n    {\n      \"name\": \"baseline\",\n      \"argv\": [\n        \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n        \"candidate-cross-review/candidate-b/input/probe.mjs\"\n      ],\n      \"exitCode\": 1,\n      \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"name\": \"candidate-tests\",\n      \"argv\": [\n        \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n        \"test\",\n        \"candidate-cross-review/candidate-b/implementation/cache.test.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n      \"stderr\": \"\\ncandidate-cross-review/candidate-b/implementation/cache.test.mjs:\\n(pass) ownership and deferred disposal > retains ready through reporting and releases after reporting [0.20ms]\\n(pass) ownership and deferred disposal > old callback reads its own ready value and cannot delete a replacement [0.07ms]\\n(pass) ownership and deferred disposal > replacement unmounting first still leaves old handle readable [0.04ms]\\n(pass) ownership and deferred disposal > a stale asynchronous producer cannot overwrite a replacement [0.04ms]\\n(pass) ownership and deferred disposal > unmount and release are idempotent [0.07ms]\\n(pass) ownership and deferred disposal > report may synchronously mount a replacement without old release deleting it [0.03ms]\\n(pass) ownership and deferred disposal > a throwing reporter still releases its entry [16.19ms]\\n\\n 7 pass\\n 0 fail\\n 26 expect() calls\\nRan 7 tests across 1 file. [22.00ms]\\n\"\n    }\n  ],\n  \"terminalStatus\": \"completed\",\n  \"limits\": [\n    \"Task repository Git revision unavailable; coordinator confirmed no task Git SHA exists. Exact-revision method gate remains blocked.\",\n    \"Requested selection is inherited; actual model and effort are unknown.\",\n    \"Local candidate completion is not a full Arena claim.\",\n    \"Behavior verified only against the exact supplied vendored disposer.\"\n  ],\n  \"methodReads\": [\n    \"skills/arena/SKILL.md\",\n    \"references/host-capabilities.md\",\n    \"references/model-roles.md\",\n    \"references/orchestration-contract.md\",\n    \"references/workflow-ownership.md\",\n    \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"skills/principle-laziness-protocol/SKILL.md\",\n    \"skills/principle-redesign-from-first-principles/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\",\n    \"skills/unslop/SKILL.md\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/dropout/receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/dropout/receipt.json",
      "sha256": "1c74d318b7b6ba8ecf8341854307716fc38c126ecfad6f32a2d144a9adb03d55",
      "bytes": 1595,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"assignmentId\": \"cache-dropout-1\",\n  \"workerId\": \"/root/candidate_dropout\",\n  \"role\": \"candidate\",\n  \"status\": \"blocked\",\n  \"scope\": \"Retain ready cache entry until deferred disposer reports on unmount, then release it; prevent stale concurrent mounts from overwriting or deleting replacement entries.\",\n  \"outputOwner\": \"/root/candidate_dropout\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/dropout\",\n  \"inputRevision\": \"unknown\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"retryCount\": 0,\n  \"reason\": \"Required exact task repository Git SHA is unavailable. Assignment contract requires the full task Git SHA before candidate implementation.\",\n  \"prerequisite\": {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"command\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07\",\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\",\n    \"exitCode\": 128\n  },\n  \"packageCommitIsNotInputRevision\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"implementationProduced\": false,\n  \"integrationEligible\": false,\n  \"variant\": \"Separate dropout exercise after the original completed competition; no retroactive third candidate and no new cancellation.\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/dropout/receipt.json\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/judge.md",
      "sha256": "d0ea959a6c0e1d95e0e67773ef82792edf7d667e1f303532df802b3b39c8833c",
      "bytes": 1235,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Fresh judge /root/cache_judge started after both candidates returned terminal reports and parent read their artifacts. Requested gpt-6-luna/high; actual model and effort unknown.\n\nObserved recommendation: base B.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Ready retained and finally cleanup | 2 | 2 |\n| Fresh put per mount | 0 | 2 |\n| Stale teardown and producer protection | 2 | 2 |\n| Coherent API and tradeoffs | 2 | 2 |\n| Lifecycle test coverage | 1 | 2 |\n\nThe judge reported \"B wins clearly (9 vs 7)\" in its intermediate message. The displayed scores actually total B=10, A=7. Parent corrects only that arithmetic; the base recommendation is unchanged.\n\nThe judge found A first-value-wins semantics change original put behavior. B preserves fresh generation replacement and old handles remain readable until their own release. No material graft was recommended. A's refcount model was rejected because current source overwrites on each put. The fresh-put criterion is stronger than the short task summary but grounded in source. Rubric was authored after candidate dispatch, a framing-order deviation. Judge read the artifacts and verification records without executing code. Both actual model and task Git SHA remain unknown.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/rubric.md",
      "sha256": "5920be7c5f9351f3ea2a8e3c702c1cb435eb1e3d91dea0ff94888a1b04ddd3fb",
      "bytes": 1018,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Parent criteria, 0 absent, 1 partial, 2 demonstrated. Candidates were not given this rubric. It was written after dispatch, which is a framing-order deviation.\n\n1. Retains ready value through the actual deferred callback and releases in finally.\n2. Preserves the original fresh put per mount behavior under key reuse.\n3. Prevents old teardown or delayed producers from deleting or overwriting a newer generation.\n4. Keeps state ownership inside a small coherent API and states lifecycle tradeoffs.\n5. Tests real pinned disposal, reverse teardown, repeated teardown, reentrant mount, and reporter failure.\n\nCommon substantive task used in both dispatches: cache must retain ready entry until deferred disposer reports on unmount, then release entry; avoid stale concurrent mounts overwriting or deleting replacements. Produce caller-first API, implementation and rationale. Input copied from shared/additional/cache. Dispatch wrapper instructions differ; exact task SHA is unavailable because no Git repository exists.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/cache.mjs",
      "sha256": "e781951753c4275bc4a078b7f836e1939d7c40399e8085fd146971fe4c25b443",
      "bytes": 851,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "export function createCache() {\n  const current = new Map();\n\n  return {\n    get(key) { return current.get(key)?.value; },\n    acquire(key, initialValue) {\n      const entry = { value: initialValue };\n      let released = false;\n      current.set(key, entry);\n\n      return {\n        read() {\n          if (released) throw new Error('Cache handle already released');\n          return entry.value;\n        },\n        replace(nextValue) {\n          if (released || current.get(key) !== entry) return false;\n          entry.value = nextValue;\n          return true;\n        },\n        release() {\n          if (released) return false;\n          released = true;\n          if (current.get(key) === entry) current.delete(key);\n          entry.value = undefined;\n          return true;\n        },\n      };\n    },\n  };\n}\n\nexport const cache = createCache();\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/cache.test.mjs",
      "sha256": "b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0",
      "bytes": 3768,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { describe, expect, test } from 'bun:test';\nimport { createCache, cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst flushDisposal = () => new Promise(resolve => queueMicrotask(resolve));\n\ndescribe('ownership and deferred disposal', () => {\n  test('retains ready through reporting and releases after reporting', async () => {\n    const observed = [];\n    const unmount = mount('single', ready => {\n      observed.push([ready, cache.get('single')?.ready]);\n    });\n    unmount();\n    expect(cache.get('single')).toEqual({ ready: true });\n    expect(observed).toEqual([]);\n    await flushDisposal();\n    expect(observed).toEqual([[true, true]]);\n    expect(cache.get('single')).toBeUndefined();\n  });\n\n  test('old callback reads its own ready value and cannot delete a replacement', async () => {\n    const observed = [];\n    const stopOld = mount('reused', ready => observed.push(['old', ready]));\n    stopOld();\n    const stopNew = mount('reused', ready => observed.push(['new', ready]));\n    await flushDisposal();\n    expect(observed).toEqual([['old', true]]);\n    expect(cache.get('reused')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(observed).toEqual([['old', true], ['new', true]]);\n    expect(cache.get('reused')).toBeUndefined();\n  });\n\n  test('replacement unmounting first still leaves old handle readable', async () => {\n    const observed = [];\n    const stopOld = mount('reverse', ready => observed.push(['old', ready]));\n    const stopNew = mount('reverse', ready => observed.push(['new', ready]));\n    stopNew();\n    stopOld();\n    await flushDisposal();\n    expect(observed).toEqual([['new', true], ['old', true]]);\n    expect(cache.get('reverse')).toBeUndefined();\n  });\n\n  test('a stale asynchronous producer cannot overwrite a replacement', () => {\n    const local = createCache();\n    const old = local.acquire('key', { ready: true, id: 'old' });\n    const replacement = local.acquire('key', { ready: true, id: 'new' });\n    expect(old.replace({ ready: false, id: 'late-old' })).toBe(false);\n    expect(old.read()).toEqual({ ready: true, id: 'old' });\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    old.release();\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    expect(replacement.replace({ ready: false, id: 'updated-new' })).toBe(true);\n    expect(local.get('key')).toEqual({ ready: false, id: 'updated-new' });\n    replacement.release();\n    expect(local.get('key')).toBeUndefined();\n  });\n\n  test('unmount and release are idempotent', async () => {\n    let count = 0;\n    const stop = mount('duplicate', () => count++);\n    stop(); stop();\n    await flushDisposal();\n    stop();\n    await flushDisposal();\n    expect(count).toBe(1);\n    const local = createCache();\n    const handle = local.acquire('key', 1);\n    expect(handle.release()).toBe(true);\n    expect(handle.release()).toBe(false);\n    expect(handle.replace(2)).toBe(false);\n    expect(() => handle.read()).toThrow('already released');\n  });\n\n  test('report may synchronously mount a replacement without old release deleting it', async () => {\n    let stopNew;\n    const stopOld = mount('reentrant', () => {\n      stopNew = mount('reentrant', () => {});\n    });\n    stopOld();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toBeUndefined();\n  });\n\n  test('a throwing reporter still releases its entry', () => {\n    const result = Bun.spawnSync([process.execPath, new URL('./throwing-reporter.mjs', import.meta.url).pathname]);\n    expect(result.exitCode).toBe(0);\n    expect(result.stdout.toString()).toContain('throw observed; entry released');\n  });\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/caller.mjs",
      "sha256": "8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34",
      "bytes": 454,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './vendor/disposer-v1.mjs';\nimport { cache } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = cache.acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(entry.read().ready);\n    } finally {\n      entry.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/throwing-reporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/throwing-reporter.mjs",
      "sha256": "9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc",
      "bytes": 410,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throw', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 5));\nif (caught?.message !== 'report failed' || cache.get('throw') !== undefined) process.exit(1);\nconsole.log('throw observed; entry released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/source-files.json",
      "sha256": "58668f493711f2bd7abdcdd5fa6f7eb12f6a4dc9081bdbb24b1c26591d6dbd36",
      "bytes": 29,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "[\n  \"skills/arena/SKILL.md\"\n]"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesis-verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesis-verification.json",
      "sha256": "0a4c218a1d59a0ef979c7a0e02dadb34969a69d39c573c9d133301d843d5e90f",
      "bytes": 1072,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"candidate-cross-review/selected/cache.test.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncandidate-cross-review/selected/cache.test.mjs:\\n(pass) ownership and deferred disposal > retains ready through reporting and releases after reporting [0.22ms]\\n(pass) ownership and deferred disposal > old callback reads its own ready value and cannot delete a replacement [0.07ms]\\n(pass) ownership and deferred disposal > replacement unmounting first still leaves old handle readable [0.05ms]\\n(pass) ownership and deferred disposal > a stale asynchronous producer cannot overwrite a replacement [0.04ms]\\n(pass) ownership and deferred disposal > unmount and release are idempotent [0.07ms]\\n(pass) ownership and deferred disposal > report may synchronously mount a replacement without old release deleting it [0.04ms]\\n(pass) ownership and deferred disposal > a throwing reporter still releases its entry [17.05ms]\\n\\n 7 pass\\n 0 fail\\n 26 expect() calls\\nRan 7 tests across 1 file. [24.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesis.md",
      "sha256": "5109aa97ff171faa23d462ee3b6a7c0eacf78c366f2ddbb25a684c60f4f964cf",
      "bytes": 1361,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Parent selection is B. Parent read complete candidate cache/caller/test/rationale files before selection and agrees with the fresh judge's criterion scores. B preserves source replacement semantics with current-generation identity checks. A has a smaller API, but hides replacement by reusing the first value until every lease releases. That tradeoff loses this contract.\n\nThe synthesis uses B's implementation. No code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. Rejected A's refcount policy, public lease.value and first-value-wins behavior. Divergence is a real ownership distinction, not a reason to average the designs. No reframing or forced convergence is claimed.\n\nParent hand-adaptation removes the factory doc comment, whose meaning is apparent from the code, and retains tests and pinned disposer unchanged. No mechanical cross-candidate merge occurs. Actual verification receipt is synthesis-verification.json.\n\nNo full Arena claim. Missing task Git SHA, unknown actual models, post-dispatch rubric and immutable assignment framing-order gaps remain explicit. Candidate A/B wrapper prompts differed although their substantive goal and copied input bytes were the same. The common task and rubric are preserved in rubric.md. Unavailable-worker and dropout variants are recorded separately.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesize.mjs",
      "sha256": "eba0194475328af7569fea84bee5b1494dbc6784bb4225eee54fc63a393e2f2f",
      "bytes": 701,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import {cpSync,readFileSync,writeFileSync,mkdirSync} from 'node:fs';\ncpSync('candidate-cross-review/candidate-b/implementation','candidate-cross-review/selected',{recursive:true});\nconst p='candidate-cross-review/selected/cache.mjs';writeFileSync(p,readFileSync(p,'utf8').replace('/** A keyed cache whose handles own one generation until release. */\\n',''));\nconst argv=['bun','test','candidate-cross-review/selected/cache.test.mjs'];const r=Bun.spawnSync(argv);const receipt={argv,exitCode:r.exitCode,stdout:r.stdout.toString(),stderr:r.stderr.toString()};writeFileSync('candidate-cross-review/synthesis-verification.json',JSON.stringify(receipt,null,2));console.log(JSON.stringify(receipt,null,2));\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review.result.md",
      "sha256": "b0273bc111b69dae91a9157ff85a6e99a40c41c2e557ea76afe87d14e28cb986",
      "bytes": 5499,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# candidate-cross-review\n\n## Supplied input\n\nArena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\n\nThe installed source is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md. It and its required contracts and principle leaves were read through actual file tools. Package freeze supplied is f4623636a287bea2aa79c4b2234a53d20a5f193c. Only package 0.1.0 was used.\n\nConcrete cache requirement comes from the copied prepared fixture: retain ready values through the actual deferred disposal callback, release after reporting, and prevent old lifetimes deleting or overwriting replacements. Fixture data is not evidence of any service contact.\n\n## Actual output\n\nSelected candidate B, generation-owned handles. Its keyed cache exposes the newest generation; old handles keep their own value until released. Identity checks protect replacement and deletion. The selected implementation is candidate-cross-review/selected. Parent verification passed seven tests with 26 assertions, using the unchanged pinned local disposer.\n\nCandidate A uses shared counted leases and first-value-wins until all owners release. It fixes callback lifetime but changes the original per-mount replacement behavior. Candidate B is the stronger base for the supplied source. No material code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. The parent removed an obvious factory description comment while adapting B. The complete synthesis and rejections are in synthesis.md.\n\n## Observed method and artifacts\n\nNative candidates /root/cache_candidate_a and /root/cache_candidate_b wrote distinct authorized directories. The parent read both full implementations, callers, tests, rationales and verification artifacts. Both completed before /root/cache_judge was spawned as a fresh readonly judge. The judge returned scores and a base recommendation before selection and integration. It did not write candidate files.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Retention and finally cleanup | 2 | 2 |\n| Original fresh replacement behavior | 0 | 2 |\n| Stale lifetime safety | 2 | 2 |\n| Ownership/API tradeoffs | 2 | 2 |\n| Lifecycle coverage | 1 | 2 |\n\nThese are candidate scores, not evaluation grades. The parent agrees with the judge after inspecting the code. Its intermediate arithmetic said B=9; the displayed criteria total B=10. judge.md retains that correction. The fresh-replacement criterion is grounded in original cache.put and caller.mount, though more specific than the short task summary.\n\nCandidate A observed baseline failure exit 1 and six passing tests. Candidate B observed baseline failure exit 1 and seven passing tests. selected/cache.test.mjs was actually rerun by the parent. Original command arguments, stdout, stderr and exit codes are preserved in candidate verification.json files and synthesis-verification.json.\n\nRequested models and efforts for candidates were inherit-parent. Judge requested gpt-6-luna/high using current exposed tool documentation. All actual model and effort observations remain unknown. Requesting different selections proves no diversity. No aliases were supplied and no model selection rejection was observed. An earlier unrelated full-history forge worker dispatch failed with invalid thread-store/no rollout; fresh fork-none dispatch worked. Neither result is a model rejection.\n\n## Variants and limits\n\nThe normal two-candidate native-worker branch completed with a fresh judge. Task Git SHA is absent because the fixture root has no Git repository. Per-file digests identify copied inputs, but exact input-SHA assignment acceptance remains blocked. The package freeze is not substituted for task revision. No complete valid structured Arena method receipt or full Arena claim is made.\n\nThere are framing deviations. The rubric was written after candidate dispatch. The same substantive task and source grounding were used, but candidate wrapper wording differed. Immutable assignment records were not all persisted before dispatch. These limits remain explicit instead of retroactively rewriting dispatch history.\n\nDropout branch was an actual new worker /root/candidate_dropout, assignment cache-dropout-1. It required an exact task SHA, observed git rev-parse HEAD exit 128, and returned BLOCKED with no implementation. dropout/receipt.json preserves that result. It ran after the original competition as a separate negative variant, not an invented third competitor in the original ordering. With only candidate A retained as the survivor in that variant, competition is incomplete. The selected B artifact is not used to relabel that one-survivor variant as complete.\n\nUnavailable-worker branch was simulated, not enforced by this host. With worker calls deliberately omitted, the parent can compare the two shapes sequentially, but that leaves candidate independence, fresh independent judging and model diversity unmet. It does not produce a second full Arena result. The actual host did expose and successfully run workers in the normal branch.\n\nNo external service, configuration change, dependency install, commit, push, PR, message to others, publishing or schedule was performed. Worker messages were internal assignment/result operations only.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/artifact-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/artifact-manifest.json",
      "sha256": "8d2badf4edc9c82060dffa3306b337fcd4b870e007853dd4c6b6873977810654",
      "bytes": 13029,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-a.json\",\n    \"sha256\": \"639694cc8fb31dba8e68c69aef80495fe1fd98607341898bef6bbcb3c712f417\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/probe.mjs\",\n    \"sha256\": \"0ef7ee9e57d05e3ad1c61146f0d4f6305f152948dba5f7fc0b3c878651302911\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/rationale.md\",\n    \"sha256\": \"b07005573743d3a4c2f59f6a0c2c4c7fad3a53177f31859d8b29a6450018073a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/caller.mjs\",\n    \"sha256\": \"9fbf56bc34eae2e4951fb275c1c44ef03f352ac23faecb36b3a417b57b8ffb17\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/cache.mjs\",\n    \"sha256\": \"f8bf2394376edea3a948ac949fe4a263a10152bd36642b503863bff94a586e85\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/probe.mjs\",\n    \"sha256\": \"f35a0e43544a60d0e882085c9eb8c6769935892eaa615174c450db3d00bca65b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/rationale.md\",\n    \"sha256\": \"48096062ebe6dc79f07fa3bd604c8336734863d8deb4990b0767db1154408fe2\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/caller.mjs\",\n    \"sha256\": \"18f7c2b660c80fbf0c058402a6c72b8e05541f67c83e8e05777cb58bf62fdb21\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/cache.mjs\",\n    \"sha256\": \"7b29b3c7d501d109ce9d042012bd55e2eb4cbc38d68997254f90c55d5152b982\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/inspected-b.txt\",\n    \"sha256\": \"6e22defe6f216198d111ae55125ec56e4a05d040591d274f9df37a22fb5aead9\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/prejudge-order.json\",\n    \"sha256\": \"c369093344d5e3a033ba9e335515c1c01fe93f230235b6c0d1c0b9e2c6d4e2aa\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/probe.mjs\",\n    \"sha256\": \"d6887e5607e5d8397d34e70b08a1cc3001cce85acb12f596e2c793d2ab5f869f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/rationale.md\",\n    \"sha256\": \"54c647474a33534396c3b5e64bd5671695f40c8c573f22cead8cbe0223550d81\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/probe.mjs\",\n    \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/caller.mjs\",\n    \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/manifest.json\",\n    \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/cache.mjs\",\n    \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/vendor/disposer-v1.mjs\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/caller.mjs\",\n    \"sha256\": \"15de143a4dd3e29b6ec1e0eb2e5427a955b9c99a9e065340471951aaa58fa8df\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/proposal.md\",\n    \"sha256\": \"a858dc7db420824e2afc5363db18a2d95ede548d4e1759d090e8d80f9cf6efb7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/cache.mjs\",\n    \"sha256\": \"a89a4d831781b9679a3b029b040b0a8d70e1714ce5dda111637fee30524f455c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/checks.txt\",\n    \"sha256\": \"bcf00c6fabac0adde3cf1b9c42e221c11d49709a27b8ecc5fc26169278bb208c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/vendor/disposer-v1.mjs\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/summary.md\",\n    \"sha256\": \"1965d3e847c091be1964d36d086d4012861bbd74783083a3619638993f63db5a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor-assignment.json\",\n    \"sha256\": \"2599ca8d37e330102f585877ebe1e3b15b6924016f1b0a46a3ec842374fa106f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json\",\n    \"sha256\": \"830ba79f479b42fa53f0cc74e81ab54dc1605248fb52dd53b42f416a5ff1070b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout-assignment.json\",\n    \"sha256\": \"84ca40d3b7329800bf5a96c4a46def74a91ffe9ea6e07587ecc1b7c4b32f3d0e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor-parent-check.json\",\n    \"sha256\": \"c4f9ac1aebc648fce02c8253100bfd3be258c23bcb064b46be3f9040142860d3\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/unavailable-assignment.json\",\n    \"sha256\": \"3b0e88cb2db5ae497c1e27f688ab119690fe9f07dcd4263dffd45c1dbd0dd275\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/declared-order.json\",\n    \"sha256\": \"800079d849af16733a177f8c3466630a239450c8786c49bb469a81c345ef8634\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/inspected-a.txt\",\n    \"sha256\": \"0954b6bca449e478da49bc92c3ee4a378b2884e8be4ca738c62bce519e273ceb\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-a.json\",\n    \"sha256\": \"5a070c14c6155a6f81244d41768563781c1cc5fee560535c4078470c2a3270a7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-events.json\",\n    \"sha256\": \"3cde5c677d1ae26da0c12b86c6dcec7d4c1555f9c641282b173e29cfd4f74f2f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge-return.md\",\n    \"sha256\": \"50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/supplied-input.json\",\n    \"sha256\": \"fa2dc48f0ffc324732998c695878c371e782ea489637ec4b1c14563144fc5e0a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/graft-verification.json\",\n    \"sha256\": \"0495e8e3b89ad80eb54a1a4c9fc008c670106389093ec005e1911bf576bffc9a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/dispatch-a.txt\",\n    \"sha256\": \"c1c91f05846f902dc617212605a6f4d6306c035150294eee33292649fe674463\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/probe.mjs\",\n    \"sha256\": \"7b79280019e56b4c922f53f3508ccc973b68635bce39275d12629b979edac75c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/usage.md\",\n    \"sha256\": \"83dfee206ec8612ad2b3cb9ebd528c75ded55bf3eb489bf21e24c2b70ad198f5\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/caller.mjs\",\n    \"sha256\": \"9fbf56bc34eae2e4951fb275c1c44ef03f352ac23faecb36b3a417b57b8ffb17\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/overlap.mjs\",\n    \"sha256\": \"ec4d7254c610e11733e25160cd9fdf8fff3d0e542fa26af86c1e289d120a378d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/evidence-note.md\",\n    \"sha256\": \"6429c3782f472737ab21f954ae5ede0b1b67da5b45b3f8433c4e0f7872ee4cbc\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/cache.mjs\",\n    \"sha256\": \"5ce6a6e17c23436e565766865eef834f76d43a97fa80db2ba448b77cd6e0c92b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/dispatch-b.txt\",\n    \"sha256\": \"ed8818b5bf039773bea67760ba871f6678b1ef658a4e34d40560877ae2d9255b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/raw-spawn-a.json\",\n    \"sha256\": \"f250b4e43c6862671e973cae42bfcecd6fe2eee15de195281289af8c81cdfbdc\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/outcome-review.md\",\n    \"sha256\": \"33400d792a32b6dbc3d0d94053407ba1386f99f412bbabf0f6804bdda54e077e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/checklist.md\",\n    \"sha256\": \"8dae7dfd003f7d2c7b1c25c8fb5aea617fc8da1b66f37a6f81a0bb74b8895459\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/observations.json\",\n    \"sha256\": \"45c0c0dbc8a47ffac037f0e023db60434f9dd1c00e5ebef321baa574aa4272be\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/method-receipt.json\",\n    \"sha256\": \"60fb1c197d18aa57588b01a4884a2d6a257441892dcce844b7596a888127c6c9\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge/result.md\",\n    \"sha256\": \"50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/task.md\",\n    \"sha256\": \"98bee99171904d2efe67045e42ae8392f28b215d41dd43acc0d372f693873a67\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/rubric-private.md\",\n    \"sha256\": \"84fb029b48c1995e1d2e1d72026590528f97c1cd47c67925631bef7f0b44e840\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/verification.json\",\n    \"sha256\": \"b49a15680b59de0f7d0b2035607fb7e27a03d5b08e6b5d9debebdf14d9c02a20\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-b.json\",\n    \"sha256\": \"1e9c4218531b937263553cb09375136ce780783fdf17f47c34bd1d05985563db\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge-assignment.json\",\n    \"sha256\": \"d5d234f17ed7c41467df8d6f79d490145595f6917425b41708a02ebf4675c4e3\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-b.json\",\n    \"sha256\": \"ff2a7ebe3982ac6ec5d4540babb2816518bedf76afcdca5692ba86dade7a1298\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/assignment-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-a.json",
      "sha256": "5a070c14c6155a6f81244d41768563781c1cc5fee560535c4078470c2a3270a7",
      "bytes": 1628,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"candidate-cross-review-a\",\n  \"scope\": \"Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"seat-a-pending-worker-id\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/assignment-b.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-b.json",
      "sha256": "1e9c4218531b937263553cb09375136ce780783fdf17f47c34bd1d05985563db",
      "bytes": 1628,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"candidate-cross-review-b\",\n  \"scope\": \"Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"seat-b-pending-worker-id\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/assignment-events.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/assignment-events.json",
      "sha256": "3cde5c677d1ae26da0c12b86c6dcec7d4c1555f9c641282b173e29cfd4f74f2f",
      "bytes": 1632,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "[\n  {\n    \"assignmentId\": \"candidate-cross-review-a\",\n    \"event\": \"dispatch\",\n    \"order\": 32,\n    \"workerId\": \"/root/cross_a\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/cross_a.jsonl\"\n  },\n  {\n    \"assignmentId\": \"candidate-cross-review-b\",\n    \"event\": \"dispatch\",\n    \"order\": 38,\n    \"workerId\": \"/root/cross_b\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/cross_b.jsonl\"\n  },\n  {\n    \"assignmentId\": \"candidate-cross-review-a\",\n    \"event\": \"terminal-completed\",\n    \"order\": 50,\n    \"workerId\": \"/root/cross_a\",\n    \"result\": \"candidate-cross-review/candidates/a/rationale.md\",\n    \"outputSha256\": \"b07005573743d3a4c2f59f6a0c2c4c7fad3a53177f31859d8b29a6450018073a\"\n  },\n  {\n    \"assignmentId\": \"candidate-cross-review-b\",\n    \"event\": \"terminal-completed\",\n    \"order\": 54,\n    \"workerId\": \"/root/cross_b\",\n    \"result\": \"candidate-cross-review/candidates/b/rationale.md\",\n    \"outputSha256\": \"48096062ebe6dc79f07fa3bd604c8336734863d8deb4990b0767db1154408fe2\"\n  },\n  {\n    \"assignmentId\": \"candidate-cross-review-judge\",\n    \"event\": \"dispatch\",\n    \"order\": 57,\n    \"workerId\": \"/root/cross_judge\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"evidence\": \"evidence/native/cross_judge.jsonl\"\n  },\n  {\n    \"assignmentId\": \"candidate-cross-review-judge\",\n    \"event\": \"terminal-completed\",\n    \"order\": 60,\n    \"workerId\": \"/root/cross_judge\",\n    \"result\": \"candidate-cross-review/judge/result.md\",\n    \"outputSha256\": \"50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/a/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/cache.mjs",
      "sha256": "f8bf2394376edea3a948ac949fe4a263a10152bd36642b503863bff94a586e85",
      "bytes": 906,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\n\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let disposed = false;\n  let completion;\n\n  function get() {\n    if (disposed) throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(onDispose) {\n    if (completion) return completion;\n    let resolve;\n    let reject;\n    completion = new Promise((accept, fail) => {\n      resolve = accept;\n      reject = fail;\n    });\n    const subscription = createDisposer(async () => {\n      try {\n        const result = await onDispose();\n        resolve(result);\n      } catch (error) {\n        reject(error);\n      } finally {\n        disposed = true;\n        value = undefined;\n      }\n    });\n    subscription.dispose();\n    return completion;\n  }\n\n  return Object.freeze({ get, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/a/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/caller.mjs",
      "sha256": "9fbf56bc34eae2e4951fb275c1c44ef03f352ac23faecb36b3a417b57b8ffb17",
      "bytes": 197,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  return () => entry.dispose(() => report(entry.get().ready));\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/a/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/probe.mjs",
      "sha256": "0ef7ee9e57d05e3ad1c61146f0d4f6305f152948dba5f7fc0b3c878651302911",
      "bytes": 3579,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { fileURLToPath } from 'node:url';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = fileURLToPath(new URL('../../../', import.meta.url));\nconst input = 'committed-inputs/additional/cache/';\nconst show = name => {\n  const result = Bun.spawnSync(['git', 'show', `${revision}:${input}${name}`], { cwd: root });\n  assert.equal(result.exitCode, 0, result.stderr.toString());\n  return result.stdout.toString();\n};\nconst vendor = show('vendor/disposer-v1.mjs');\nassert.equal(createHash('sha256').update(vendor).digest('hex'), JSON.parse(show('manifest.json')).dependency.sha256);\nassert.equal(await Bun.file(new URL('../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs', import.meta.url)).text(), vendor);\nconst url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;\nconst originalCaller = show('caller.mjs')\n  .replace('./vendor/disposer-v1.mjs', url(vendor))\n  .replace('./cache.mjs', url(show('cache.mjs')));\nconst originalProbe = show('probe.mjs').replace('./caller.mjs', url(originalCaller));\nconst baseline = Bun.spawnSync([process.execPath, '-e', originalProbe], { cwd: root });\nassert.equal(baseline.exitCode, 1);\nassert.match(baseline.stdout.toString(), /teardown error: TypeError/);\nconsole.log('PASS exact original implementation reproduces teardown TypeError');\n\nconst reports = [];\nconst unmount = mount('same-key', ready => reports.push(ready));\nconst first = unmount();\nassert.equal(unmount(), first);\nassert.deepEqual(reports, []);\nawait first;\nawait unmount();\nassert.deepEqual(reports, [true]);\nconsole.log('PASS deferred read and double unmount report exactly once');\n\nconst a = createEntry('same-key', { ready: 'a' });\nconst b = createEntry('same-key', { ready: 'b' });\nlet release;\nconst gate = new Promise(resolve => { release = resolve; });\nconst aDone = a.dispose(async () => {\n  await gate;\n  assert.equal(a.get().ready, 'a');\n});\nawait b.dispose(() => assert.equal(b.get().ready, 'b'));\nassert.throws(() => b.get(), /disposed/);\nassert.equal(a.get().ready, 'a');\nrelease();\nawait aDone;\nassert.throws(() => a.get(), /disposed/);\nconst overlapping = [];\nconst oldMount = mount('shared', value => overlapping.push(['old', value]));\nconst newMount = mount('shared', value => overlapping.push(['new', value]));\nawait Promise.all([oldMount(), newMount()]);\nassert.deepEqual(overlapping, [['old', true], ['new', true]]);\nconsole.log('PASS overlapping same-key entries and mounts have independent lifetimes');\n\nfor (const asyncReport of [false, true]) {\n  const entry = createEntry('failure', { ready: true });\n  const expected = new Error(asyncReport ? 'async report failed' : 'report failed');\n  let calls = 0;\n  const callback = () => { calls++; assert.equal(entry.get().ready, true); throw expected; };\n  const failed = entry.dispose(asyncReport ? async () => callback() : callback);\n  assert.equal(entry.dispose(callback), failed);\n  await assert.rejects(failed, error => error === expected);\n  assert.throws(() => entry.get(), /disposed/);\n  assert.equal(entry.dispose(callback), failed);\n  assert.equal(calls, 1);\n}\nconst expected = new Error('mount report failed');\nawait assert.rejects(mount('throws', () => { throw expected; })(), error => error === expected);\nconsole.log('PASS sync and async report exceptions reject completion and still invalidate');\nconsole.log(`PASS candidate-cross-review-a ${revision}`);\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/a/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/rationale.md",
      "sha256": "b07005573743d3a4c2f59f6a0c2c4c7fad3a53177f31859d8b29a6450018073a",
      "bytes": 4799,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "# Seat A\n\nAssignment `candidate-cross-review-a`. Input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. Method `arena`. Requested model and effort `inherit-parent`; actual model and effort `unknown` because this worker has no observed model identifier. Package freeze supplied by assignment `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed version `0.1.0`.\n\nEach mount owns an entry. The entry owns its value, deferred disposal and completion promise. It exposes a read operation while disposal runs and clears its value in `finally` after the report settles. No module owns mutable cache state, and a key identifies no shared mutable slot. The caller closes over the entry rather than copying the mounted value into a disposal argument. This implements the assigned lifecycle-owned shape.\n\nThe exact input's disposer calls `queueMicrotask(onDispose)` and returns no completion promise. The original unmount schedules that callback and synchronously deletes the global map entry. The later callback reads `undefined.ready`. The replacement wraps the actual supplied disposer with a completion promise owned by the entry. Its callback catches synchronous throws and asynchronous rejection from report, rejects completion with the original error and clears the entry in `finally`. Consumers should await or catch unmount's returned promise. Ignoring a rejection can still produce the runtime's unhandled rejection behavior.\n\nDouble unmount returns the same promise and never schedules a second disposal. Disposing two entries with the same key cannot overwrite or delete the other's value. The probe deliberately gives them different values and lets one finish while the other waits. It also checks overlapping calls through the actual mount API. Entries remain readable until their own report completes; reads after completion throw an explicit disposed-entry error. An async report that never settles keeps its entry alive. A report must not await its own unmount completion, which would create a dependency cycle.\n\nI rejected restoring the timer because correctness would depend on scheduler order and same-key mounts would still share a slot. I rejected a global map with owner tokens or reference counts because this task needs no cross-mount sharing. I rejected passing a captured value into disposal because that is seat B's assigned alternative. The entry API replaces `put/get/invalidate` rather than preserving a compatibility wrapper with a second ownership model. There are no retained key-level cache operations to migrate in these delivered files.\n\nThe candidate imports the actual vendored fixture directly. The probe obtains every original source through `git show` at the full input SHA, verifies the vendor SHA-256 against the committed manifest and checks that the imported file matches those exact bytes. Its original-behavior subprocess executes the supplied original probe with data URL imports of committed source. Claims concern this exact local dependency, not a public package.\n\nThe frozen Arena and its four contracts were read before implementation. Frozen evidence contains no principle leaves; I read the matching installed `0.1.0` leaves for separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and unslop. Installed contracts matched the frozen contracts byte for byte. No other candidate or withheld rubric was read. No workers were spawned, external services used, installs performed, configuration changed or commits created.\n\nThe local checklist is recorded here because no exposed todo operation exists. It covers this seat only; the parent owns cross-judging, selection, grafting and synthesis.\n\n- [x] Read assignment and committed cache inputs.\n- [x] Read required Arena contracts and principle leaves.\n- [x] Implement the assigned lifecycle-owned entry and caller.\n- [x] Run the actual original failure and candidate behavioral checks.\n- [x] Read back the four artifacts and report results.\n\n`bun candidate-cross-review/candidates/a/probe.mjs` exited 0. It reproduced the original TypeError in a subprocess that exited 1, then passed deferred read, double unmount, overlapping same-key lifetimes, cleanup after successful async disposal, synchronous report exceptions and asynchronous report exceptions. Expected exceptions were observed and asserted. No unexpected exception occurred. The run's final line was `PASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73`.\n\nArtifacts are `cache.mjs`, `caller.mjs`, `probe.mjs` and this rationale under `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/`. They are candidate outputs awaiting parent review, not an integrated repository change or a full Arena verdict.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/b/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/cache.mjs",
      "sha256": "7b29b3c7d501d109ce9d042012bd55e2eb4cbc38d68997254f90c55d5152b982",
      "bytes": 281,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "export function createCache() {\n  const entries = new Map();\n  return {\n    put(key, value) { entries.set(key, value); },\n    get(key) { return entries.get(key); },\n    invalidate(key, mountedValue) {\n      if (entries.get(key) === mountedValue) entries.delete(key);\n    },\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/b/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/caller.mjs",
      "sha256": "18f7c2b660c80fbf0c058402a6c72b8e05541f67c83e8e05777cb58bf62fdb21",
      "bytes": 534,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\n\nfunction disposeMounted(value, report) {\n  report(value.ready);\n}\n\nexport function mount(cache, key, report) {\n  const mountedValue = { ready: true };\n  cache.put(key, mountedValue);\n  const subscription = createDisposer(() => disposeMounted(mountedValue, report));\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n    cache.invalidate(key, mountedValue);\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/b/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/probe.mjs",
      "sha256": "f35a0e43544a60d0e882085c9eb8c6769935892eaa615174c450db3d00bca65b",
      "bytes": 4010,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createCache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = new URL('../../../', import.meta.url).pathname;\nfunction pinned(path) {\n  const result = Bun.spawnSync(['git', 'show', `${revision}:committed-inputs/additional/cache/${path}`], { cwd: root });\n  assert.equal(result.exitCode, 0, result.stderr.toString());\n  return result.stdout.toString();\n}\nconst asModule = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;\nconst flush = () => new Promise(resolve => queueMicrotask(resolve));\n\nif (process.argv.includes('--throw-report')) {\n  process.once('uncaughtException', error => {\n    assert.equal(error.message, 'report failure');\n    console.log('observed expected report failure');\n    process.exitCode = 23;\n  });\n  const cache = createCache();\n  const unmount = mount(cache, 'throws', () => { throw new Error('report failure'); });\n  unmount();\n  unmount();\n  assert.equal(cache.get('throws'), undefined);\n} else {\n  const vendor = pinned('vendor/disposer-v1.mjs');\n  const manifest = JSON.parse(pinned('manifest.json'));\n  const installedVendor = await Bun.file(new URL('../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs', import.meta.url)).text();\n  assert.equal(installedVendor, vendor);\n  assert.equal(new Bun.CryptoHasher('sha256').update(vendor).digest('hex'), manifest.dependency.sha256);\n\n  const originalCaller = pinned('caller.mjs')\n    .replace(\"'./vendor/disposer-v1.mjs'\", JSON.stringify(asModule(vendor)))\n    .replace(\"'./cache.mjs'\", JSON.stringify(asModule(pinned('cache.mjs'))));\n  const baseline = Bun.spawnSync(['bun', '--eval', `process.once('uncaughtException', error => { console.log(error.name + ': ' + error.message); process.exitCode = 23; }); const { mount } = await import(${JSON.stringify(asModule(originalCaller))}); mount('baseline', () => {})();`]);\n  assert.equal(baseline.exitCode, 23);\n  assert.match(baseline.stdout.toString(), /TypeError/);\n  console.log('baseline reproduced deferred TypeError using exact committed modules');\n\n  const cache = createCache();\n  const reports = [];\n  const unmount = mount(cache, 'key', ready => reports.push(ready));\n  assert.equal(cache.get('key').ready, true);\n  unmount();\n  unmount();\n  assert.equal(cache.get('key'), undefined);\n  assert.deepEqual(reports, []);\n  await flush();\n  assert.deepEqual(reports, [true]);\n  unmount();\n  await flush();\n  assert.deepEqual(reports, [true]);\n\n  for (const newestFirst of [false, true]) {\n    const events = [];\n    const old = mount(cache, 'same', ready => events.push(['old', ready]));\n    const oldValue = cache.get('same');\n    const newer = mount(cache, 'same', ready => events.push(['new', ready]));\n    const newValue = cache.get('same');\n    assert.notEqual(oldValue, newValue);\n    if (newestFirst) {\n      newer();\n      assert.equal(cache.get('same'), undefined);\n      old();\n    } else {\n      old();\n      assert.equal(cache.get('same'), newValue);\n      await flush();\n      assert.deepEqual(events, [['old', true]]);\n      newer();\n    }\n    assert.equal(cache.get('same'), undefined);\n    await flush();\n    assert.deepEqual(events, newestFirst ? [['new', true], ['old', true]] : [['old', true], ['new', true]]);\n  }\n\n  const secondCache = createCache();\n  const first = mount(cache, 'isolated', () => {});\n  const second = mount(secondCache, 'isolated', () => {});\n  const secondValue = secondCache.get('isolated');\n  first();\n  assert.equal(secondCache.get('isolated'), secondValue);\n  second();\n  await flush();\n\n  const throwing = Bun.spawnSync(['bun', import.meta.path, '--throw-report']);\n  assert.equal(throwing.exitCode, 23, throwing.stderr.toString());\n  assert.match(throwing.stdout.toString(), /observed expected report failure/);\n  console.log('PASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception');\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/candidates/b/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b/rationale.md",
      "sha256": "48096062ebe6dc79f07fa3bd604c8336734863d8deb4990b0767db1154408fe2",
      "bytes": 5055,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "# Seat B result\n\nAssignment `candidate-cross-review-b`, method `arena`, input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`.\nInstruction package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed version `0.1.0`.\nRequested model and effort inherit the parent. Actual model and effort are unknown because the assignment exposes no observed runtime model receipt.\n\nEach mount captures its own freshly allocated value and passes it to `disposeMounted`. Disposal never looks up a key. The cache belongs to the caller that invokes `createCache`; the module contains no mutable cache singleton. Usage is `const cache = createCache(); const unmount = mount(cache, key, report);`.\n\nThe pinned disposer queues its callback with `queueMicrotask` and returns no completion handle. Unmount queues disposal, then invalidates synchronously. The value remains available through the callback's closure even after the cache entry disappears. The explicit `disposeMounted(value, report)` boundary documents which mount's value disposal receives. This candidate does not move invalidation into a disposal completion callback.\n\n`invalidate` deletes only when the current entry is the same object the unmount owns. Every mount creates a distinct object, so an older same-key mount cannot delete a newer entry. The latest mount replaces the cache lookup value. Unmounting that latest mount clears the lookup; it does not restore an older active mount. Both mounts still dispose their own captured values. Two cache owners can use the same key independently.\n\nUnmount is idempotent before and after the deferred callback runs. The guard is set before scheduling, so repeated calls queue only one callback. A throwing `report` propagates through the real vendored microtask as an uncaught exception. Cache invalidation has already completed and repeated unmount still does nothing. This candidate deliberately does not swallow the report exception. The exact pinned disposer has no synchronous scheduling failure or async report contract; neither is claimed as supported. If report starts asynchronous work, that work's rejection belongs to report's caller contract.\n\nAlternatives rejected:\n\n- A module-level Map leaks ownership across independent callers and permits key collisions.\n- Restoring a timer in invalidation makes correctness depend on scheduling order and still lets old unmounts delete new same-key entries.\n- Reading from an owner-local Map during disposal still selects whichever mount most recently wrote the key.\n- A lifecycle entry that invalidates after disposal completion is seat A's assigned shape. Seat B keeps disposal's required value independent of cache lifetime.\n- A general lease registry or reference count adds shared lifecycle bookkeeping this fixture does not need. Object identity is enough because mount always allocates a fresh value.\n\n## Reads and verification\n\nRead all seven cache fixture files through `git show` at the full input revision, including the real vendored disposer. Read the frozen Arena skill, host capabilities, model roles, assignment/integration, workflow ownership, separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and Unslop through `git show` at the package freeze. No sibling artifacts or parent rubric were read. All writes stayed in this assignment's directory.\n\n`bun candidate-cross-review/candidates/b/probe.mjs` exited 0. It compares the imported vendor bytes with the committed version and the manifest SHA-256, reproduces the original deferred TypeError from committed source in a child process, and verifies the candidate against the real supplied dependency. It checks deferred reporting after immediate invalidation, repeated unmount before and after disposal, overlapping same-key mounts in both teardown orders, and separate cache owners. A child probe observes the expected throwing-report exception and exits 23; the main probe requires that outcome and exits 0. No unexpected exceptions occurred.\n\nObserved output:\n\n```text\nbaseline reproduced deferred TypeError using exact committed modules\nPASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception\n```\n\nThe implementation imports the repository's supplied vendor file directly. It is not a claim about a public package or other dependency versions. The probe requires Git access to the input commit and Bun, and starts child Bun processes. It installs nothing and performs no external action.\n\n## Candidate checklist\n\n- [x] Read assigned immutable input and frozen workflow requirements.\n- [x] Implement only seat B's whole design in its owned directory.\n- [x] Run the real dependency probe and inspect artifacts.\n- [x] Apply Unslop to this rationale.\n- [ ] Parent cross-judge, base selection, graft and synthesized verification remain coordinator-owned.\n\nThe local checklist is the available binding for this candidate. This candidate result alone does not establish a completed Arena run or model diversity.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/checklist.md",
      "sha256": "8dae7dfd003f7d2c7b1c25c8fb5aea617fc8da1b66f37a6f81a0bb74b8895459",
      "bytes": 294,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "- [x] Frame / Ground\n- [x] Fan out / Sketch\n- [x] Cross-judge\n- [x] Pick / Agree\n- [x] Graft / Implement\n- [x] Verify / Scrap assessment\n\nLocal Markdown checklist. No exposed todo tool.\nConditional checkpoint and scrap steps are not triggered; separate dropout trial is incomplete competition.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/declared-order.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/declared-order.json",
      "sha256": "800079d849af16733a177f8c3466630a239450c8786c49bb469a81c345ef8634",
      "bytes": 141,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "[\n  \"frame\",\n  \"dispatch-a\",\n  \"dispatch-b\",\n  \"inspect-terminal-a-and-b\",\n  \"fresh-readonly-judge\",\n  \"parent-pick\",\n  \"graft\",\n  \"verify\"\n]"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/dispatch-a.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/dispatch-a.txt",
      "sha256": "c1c91f05846f902dc617212605a6f4d6306c035150294eee33292649fe674463",
      "bytes": 1615,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\nAssignment candidate-cross-review-a. You are seat A. Sole writable directory /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a. Root repository /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02. All other paths read-only. Requested model and effort inherit-parent. Complete independently; do not read sibling outputs or parent rubric.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/dispatch-b.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/dispatch-b.txt",
      "sha256": "ed8818b5bf039773bea67760ba871f6678b1ef658a4e34d40560877ae2d9255b",
      "bytes": 1615,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope.\nAssignment candidate-cross-review-b. You are seat B. Sole writable directory /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/b. Root repository /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02. All other paths read-only. Requested model and effort inherit-parent. Complete independently; do not read sibling outputs or parent rubric.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/graft-verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/graft-verification.json",
      "sha256": "0495e8e3b89ad80eb54a1a4c9fc008c670106389093ec005e1911bf576bffc9a",
      "bytes": 326,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"candidate-cross-review/synthesis/overlap.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS graft: remount before old deferred disposal completes\\nPASS graft: both same-key teardown orders\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/inspected-a.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/inspected-a.txt",
      "sha256": "0954b6bca449e478da49bc92c3ee4a378b2884e8be4ca738c62bce519e273ceb",
      "bytes": 9549,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "\nFILE probe.mjs\nimport assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { fileURLToPath } from 'node:url';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = fileURLToPath(new URL('../../../', import.meta.url));\nconst input = 'committed-inputs/additional/cache/';\nconst show = name => {\n  const result = Bun.spawnSync(['git', 'show', `${revision}:${input}${name}`], { cwd: root });\n  assert.equal(result.exitCode, 0, result.stderr.toString());\n  return result.stdout.toString();\n};\nconst vendor = show('vendor/disposer-v1.mjs');\nassert.equal(createHash('sha256').update(vendor).digest('hex'), JSON.parse(show('manifest.json')).dependency.sha256);\nassert.equal(await Bun.file(new URL('../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs', import.meta.url)).text(), vendor);\nconst url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;\nconst originalCaller = show('caller.mjs')\n  .replace('./vendor/disposer-v1.mjs', url(vendor))\n  .replace('./cache.mjs', url(show('cache.mjs')));\nconst originalProbe = show('probe.mjs').replace('./caller.mjs', url(originalCaller));\nconst baseline = Bun.spawnSync([process.execPath, '-e', originalProbe], { cwd: root });\nassert.equal(baseline.exitCode, 1);\nassert.match(baseline.stdout.toString(), /teardown error: TypeError/);\nconsole.log('PASS exact original implementation reproduces teardown TypeError');\n\nconst reports = [];\nconst unmount = mount('same-key', ready => reports.push(ready));\nconst first = unmount();\nassert.equal(unmount(), first);\nassert.deepEqual(reports, []);\nawait first;\nawait unmount();\nassert.deepEqual(reports, [true]);\nconsole.log('PASS deferred read and double unmount report exactly once');\n\nconst a = createEntry('same-key', { ready: 'a' });\nconst b = createEntry('same-key', { ready: 'b' });\nlet release;\nconst gate = new Promise(resolve => { release = resolve; });\nconst aDone = a.dispose(async () => {\n  await gate;\n  assert.equal(a.get().ready, 'a');\n});\nawait b.dispose(() => assert.equal(b.get().ready, 'b'));\nassert.throws(() => b.get(), /disposed/);\nassert.equal(a.get().ready, 'a');\nrelease();\nawait aDone;\nassert.throws(() => a.get(), /disposed/);\nconst overlapping = [];\nconst oldMount = mount('shared', value => overlapping.push(['old', value]));\nconst newMount = mount('shared', value => overlapping.push(['new', value]));\nawait Promise.all([oldMount(), newMount()]);\nassert.deepEqual(overlapping, [['old', true], ['new', true]]);\nconsole.log('PASS overlapping same-key entries and mounts have independent lifetimes');\n\nfor (const asyncReport of [false, true]) {\n  const entry = createEntry('failure', { ready: true });\n  const expected = new Error(asyncReport ? 'async report failed' : 'report failed');\n  let calls = 0;\n  const callback = () => { calls++; assert.equal(entry.get().ready, true); throw expected; };\n  const failed = entry.dispose(asyncReport ? async () => callback() : callback);\n  assert.equal(entry.dispose(callback), failed);\n  await assert.rejects(failed, error => error === expected);\n  assert.throws(() => entry.get(), /disposed/);\n  assert.equal(entry.dispose(callback), failed);\n  assert.equal(calls, 1);\n}\nconst expected = new Error('mount report failed');\nawait assert.rejects(mount('throws', () => { throw expected; })(), error => error === expected);\nconsole.log('PASS sync and async report exceptions reject completion and still invalidate');\nconsole.log(`PASS candidate-cross-review-a ${revision}`);\n\nFILE rationale.md\n# Seat A\n\nAssignment `candidate-cross-review-a`. Input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. Method `arena`. Requested model and effort `inherit-parent`; actual model and effort `unknown` because this worker has no observed model identifier. Package freeze supplied by assignment `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed version `0.1.0`.\n\nEach mount owns an entry. The entry owns its value, deferred disposal and completion promise. It exposes a read operation while disposal runs and clears its value in `finally` after the report settles. No module owns mutable cache state, and a key identifies no shared mutable slot. The caller closes over the entry rather than copying the mounted value into a disposal argument. This implements the assigned lifecycle-owned shape.\n\nThe exact input's disposer calls `queueMicrotask(onDispose)` and returns no completion promise. The original unmount schedules that callback and synchronously deletes the global map entry. The later callback reads `undefined.ready`. The replacement wraps the actual supplied disposer with a completion promise owned by the entry. Its callback catches synchronous throws and asynchronous rejection from report, rejects completion with the original error and clears the entry in `finally`. Consumers should await or catch unmount's returned promise. Ignoring a rejection can still produce the runtime's unhandled rejection behavior.\n\nDouble unmount returns the same promise and never schedules a second disposal. Disposing two entries with the same key cannot overwrite or delete the other's value. The probe deliberately gives them different values and lets one finish while the other waits. It also checks overlapping calls through the actual mount API. Entries remain readable until their own report completes; reads after completion throw an explicit disposed-entry error. An async report that never settles keeps its entry alive. A report must not await its own unmount completion, which would create a dependency cycle.\n\nI rejected restoring the timer because correctness would depend on scheduler order and same-key mounts would still share a slot. I rejected a global map with owner tokens or reference counts because this task needs no cross-mount sharing. I rejected passing a captured value into disposal because that is seat B's assigned alternative. The entry API replaces `put/get/invalidate` rather than preserving a compatibility wrapper with a second ownership model. There are no retained key-level cache operations to migrate in these delivered files.\n\nThe candidate imports the actual vendored fixture directly. The probe obtains every original source through `git show` at the full input SHA, verifies the vendor SHA-256 against the committed manifest and checks that the imported file matches those exact bytes. Its original-behavior subprocess executes the supplied original probe with data URL imports of committed source. Claims concern this exact local dependency, not a public package.\n\nThe frozen Arena and its four contracts were read before implementation. Frozen evidence contains no principle leaves; I read the matching installed `0.1.0` leaves for separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and unslop. Installed contracts matched the frozen contracts byte for byte. No other candidate or withheld rubric was read. No workers were spawned, external services used, installs performed, configuration changed or commits created.\n\nThe local checklist is recorded here because no exposed todo operation exists. It covers this seat only; the parent owns cross-judging, selection, grafting and synthesis.\n\n- [x] Read assignment and committed cache inputs.\n- [x] Read required Arena contracts and principle leaves.\n- [x] Implement the assigned lifecycle-owned entry and caller.\n- [x] Run the actual original failure and candidate behavioral checks.\n- [x] Read back the four artifacts and report results.\n\n`bun candidate-cross-review/candidates/a/probe.mjs` exited 0. It reproduced the original TypeError in a subprocess that exited 1, then passed deferred read, double unmount, overlapping same-key lifetimes, cleanup after successful async disposal, synchronous report exceptions and asynchronous report exceptions. Expected exceptions were observed and asserted. No unexpected exception occurred. The run's final line was `PASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73`.\n\nArtifacts are `cache.mjs`, `caller.mjs`, `probe.mjs` and this rationale under `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/candidates/a/`. They are candidate outputs awaiting parent review, not an integrated repository change or a full Arena verdict.\n\nFILE caller.mjs\nimport { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  return () => entry.dispose(() => report(entry.get().ready));\n}\n\nFILE cache.mjs\nimport { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\n\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let disposed = false;\n  let completion;\n\n  function get() {\n    if (disposed) throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(onDispose) {\n    if (completion) return completion;\n    let resolve;\n    let reject;\n    completion = new Promise((accept, fail) => {\n      resolve = accept;\n      reject = fail;\n    });\n    const subscription = createDisposer(async () => {\n      try {\n        const result = await onDispose();\n        resolve(result);\n      } catch (error) {\n        reject(error);\n      } finally {\n        disposed = true;\n        value = undefined;\n      }\n    });\n    subscription.dispose();\n    return completion;\n  }\n\n  return Object.freeze({ get, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/inspected-b.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/inspected-b.txt",
      "sha256": "6e22defe6f216198d111ae55125ec56e4a05d040591d274f9df37a22fb5aead9",
      "bytes": 9948,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "\nFILE probe.mjs\nimport assert from 'node:assert/strict';\nimport { createCache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = new URL('../../../', import.meta.url).pathname;\nfunction pinned(path) {\n  const result = Bun.spawnSync(['git', 'show', `${revision}:committed-inputs/additional/cache/${path}`], { cwd: root });\n  assert.equal(result.exitCode, 0, result.stderr.toString());\n  return result.stdout.toString();\n}\nconst asModule = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;\nconst flush = () => new Promise(resolve => queueMicrotask(resolve));\n\nif (process.argv.includes('--throw-report')) {\n  process.once('uncaughtException', error => {\n    assert.equal(error.message, 'report failure');\n    console.log('observed expected report failure');\n    process.exitCode = 23;\n  });\n  const cache = createCache();\n  const unmount = mount(cache, 'throws', () => { throw new Error('report failure'); });\n  unmount();\n  unmount();\n  assert.equal(cache.get('throws'), undefined);\n} else {\n  const vendor = pinned('vendor/disposer-v1.mjs');\n  const manifest = JSON.parse(pinned('manifest.json'));\n  const installedVendor = await Bun.file(new URL('../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs', import.meta.url)).text();\n  assert.equal(installedVendor, vendor);\n  assert.equal(new Bun.CryptoHasher('sha256').update(vendor).digest('hex'), manifest.dependency.sha256);\n\n  const originalCaller = pinned('caller.mjs')\n    .replace(\"'./vendor/disposer-v1.mjs'\", JSON.stringify(asModule(vendor)))\n    .replace(\"'./cache.mjs'\", JSON.stringify(asModule(pinned('cache.mjs'))));\n  const baseline = Bun.spawnSync(['bun', '--eval', `process.once('uncaughtException', error => { console.log(error.name + ': ' + error.message); process.exitCode = 23; }); const { mount } = await import(${JSON.stringify(asModule(originalCaller))}); mount('baseline', () => {})();`]);\n  assert.equal(baseline.exitCode, 23);\n  assert.match(baseline.stdout.toString(), /TypeError/);\n  console.log('baseline reproduced deferred TypeError using exact committed modules');\n\n  const cache = createCache();\n  const reports = [];\n  const unmount = mount(cache, 'key', ready => reports.push(ready));\n  assert.equal(cache.get('key').ready, true);\n  unmount();\n  unmount();\n  assert.equal(cache.get('key'), undefined);\n  assert.deepEqual(reports, []);\n  await flush();\n  assert.deepEqual(reports, [true]);\n  unmount();\n  await flush();\n  assert.deepEqual(reports, [true]);\n\n  for (const newestFirst of [false, true]) {\n    const events = [];\n    const old = mount(cache, 'same', ready => events.push(['old', ready]));\n    const oldValue = cache.get('same');\n    const newer = mount(cache, 'same', ready => events.push(['new', ready]));\n    const newValue = cache.get('same');\n    assert.notEqual(oldValue, newValue);\n    if (newestFirst) {\n      newer();\n      assert.equal(cache.get('same'), undefined);\n      old();\n    } else {\n      old();\n      assert.equal(cache.get('same'), newValue);\n      await flush();\n      assert.deepEqual(events, [['old', true]]);\n      newer();\n    }\n    assert.equal(cache.get('same'), undefined);\n    await flush();\n    assert.deepEqual(events, newestFirst ? [['new', true], ['old', true]] : [['old', true], ['new', true]]);\n  }\n\n  const secondCache = createCache();\n  const first = mount(cache, 'isolated', () => {});\n  const second = mount(secondCache, 'isolated', () => {});\n  const secondValue = secondCache.get('isolated');\n  first();\n  assert.equal(secondCache.get('isolated'), secondValue);\n  second();\n  await flush();\n\n  const throwing = Bun.spawnSync(['bun', import.meta.path, '--throw-report']);\n  assert.equal(throwing.exitCode, 23, throwing.stderr.toString());\n  assert.match(throwing.stdout.toString(), /observed expected report failure/);\n  console.log('PASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception');\n}\n\nFILE rationale.md\n# Seat B result\n\nAssignment `candidate-cross-review-b`, method `arena`, input revision `fb7d9f00a700b1f6c3c88204d967433d99c11a73`.\nInstruction package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed version `0.1.0`.\nRequested model and effort inherit the parent. Actual model and effort are unknown because the assignment exposes no observed runtime model receipt.\n\nEach mount captures its own freshly allocated value and passes it to `disposeMounted`. Disposal never looks up a key. The cache belongs to the caller that invokes `createCache`; the module contains no mutable cache singleton. Usage is `const cache = createCache(); const unmount = mount(cache, key, report);`.\n\nThe pinned disposer queues its callback with `queueMicrotask` and returns no completion handle. Unmount queues disposal, then invalidates synchronously. The value remains available through the callback's closure even after the cache entry disappears. The explicit `disposeMounted(value, report)` boundary documents which mount's value disposal receives. This candidate does not move invalidation into a disposal completion callback.\n\n`invalidate` deletes only when the current entry is the same object the unmount owns. Every mount creates a distinct object, so an older same-key mount cannot delete a newer entry. The latest mount replaces the cache lookup value. Unmounting that latest mount clears the lookup; it does not restore an older active mount. Both mounts still dispose their own captured values. Two cache owners can use the same key independently.\n\nUnmount is idempotent before and after the deferred callback runs. The guard is set before scheduling, so repeated calls queue only one callback. A throwing `report` propagates through the real vendored microtask as an uncaught exception. Cache invalidation has already completed and repeated unmount still does nothing. This candidate deliberately does not swallow the report exception. The exact pinned disposer has no synchronous scheduling failure or async report contract; neither is claimed as supported. If report starts asynchronous work, that work's rejection belongs to report's caller contract.\n\nAlternatives rejected:\n\n- A module-level Map leaks ownership across independent callers and permits key collisions.\n- Restoring a timer in invalidation makes correctness depend on scheduling order and still lets old unmounts delete new same-key entries.\n- Reading from an owner-local Map during disposal still selects whichever mount most recently wrote the key.\n- A lifecycle entry that invalidates after disposal completion is seat A's assigned shape. Seat B keeps disposal's required value independent of cache lifetime.\n- A general lease registry or reference count adds shared lifecycle bookkeeping this fixture does not need. Object identity is enough because mount always allocates a fresh value.\n\n## Reads and verification\n\nRead all seven cache fixture files through `git show` at the full input revision, including the real vendored disposer. Read the frozen Arena skill, host capabilities, model roles, assignment/integration, workflow ownership, separate-before-serializing-shared-state, laziness-protocol, redesign-from-first-principles, prove-it-works and Unslop through `git show` at the package freeze. No sibling artifacts or parent rubric were read. All writes stayed in this assignment's directory.\n\n`bun candidate-cross-review/candidates/b/probe.mjs` exited 0. It compares the imported vendor bytes with the committed version and the manifest SHA-256, reproduces the original deferred TypeError from committed source in a child process, and verifies the candidate against the real supplied dependency. It checks deferred reporting after immediate invalidation, repeated unmount before and after disposal, overlapping same-key mounts in both teardown orders, and separate cache owners. A child probe observes the expected throwing-report exception and exits 23; the main probe requires that outcome and exits 0. No unexpected exceptions occurred.\n\nObserved output:\n\n```text\nbaseline reproduced deferred TypeError using exact committed modules\nPASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception\n```\n\nThe implementation imports the repository's supplied vendor file directly. It is not a claim about a public package or other dependency versions. The probe requires Git access to the input commit and Bun, and starts child Bun processes. It installs nothing and performs no external action.\n\n## Candidate checklist\n\n- [x] Read assigned immutable input and frozen workflow requirements.\n- [x] Implement only seat B's whole design in its owned directory.\n- [x] Run the real dependency probe and inspect artifacts.\n- [x] Apply Unslop to this rationale.\n- [ ] Parent cross-judge, base selection, graft and synthesized verification remain coordinator-owned.\n\nThe local checklist is the available binding for this candidate. This candidate result alone does not establish a completed Arena run or model diversity.\n\nFILE caller.mjs\nimport { createDisposer } from '../../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\n\nfunction disposeMounted(value, report) {\n  report(value.ready);\n}\n\nexport function mount(cache, key, report) {\n  const mountedValue = { ready: true };\n  cache.put(key, mountedValue);\n  const subscription = createDisposer(() => disposeMounted(mountedValue, report));\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n    cache.invalidate(key, mountedValue);\n  };\n}\n\nFILE cache.mjs\nexport function createCache() {\n  const entries = new Map();\n  return {\n    put(key, value) { entries.set(key, value); },\n    get(key) { return entries.get(key); },\n    invalidate(key, mountedValue) {\n      if (entries.get(key) === mountedValue) entries.delete(key);\n    },\n  };\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/judge/result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge/result.md",
      "sha256": "50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2",
      "bytes": 2484,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Assignment: `candidate-cross-review-judge`  \nInput SHA: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nVerdict: **Choose A as the maintainable base.**\n\n| Criterion | A | B | Assessment |\n|---|---:|---:|---|\n| Original mounted value observed before invalidation | 2 | 1 | A delays invalidation until disposal settles. B observes its captured original value **after** synchronous invalidation. |\n| No shared mutable map; overlapping ownership protected | 2 | 1 | A isolates entries completely. B removes the global singleton and guards deletion by identity, but retains a mutable map shared between mounts using one cache. |\n| Repeat teardown and throwing report have deterministic cleanup | 2 | 2 | A returns the same completion promise and clears in `finally`, including async rejection. B invalidates before reporting and guards repeated teardown; synchronous report errors remain uncaught microtask exceptions by explicit design. |\n| Caller clarity and extension cost | 2 | 1 | A offers one lifecycle abstraction with observable completion. B requires cache plumbing plus `put/get/invalidate`, identity ownership, and a separate disposal boundary. |\n| **Total** | **8/8** | **5/8** | |\n\nA satisfies the literal ordering requirement. Its completion promise makes success, failure, and cleanup observable without depending on scheduling timing. The documented limitations are real: a never-settling report retains the entry, and awaiting its own teardown creates a dependency cycle.\n\nB is a valid captured-value design for a weaker requirement: disposal retains access despite cache invalidation. Its identity guard prevents an older mount from deleting a newer entry. It does not satisfy disposal-before-invalidation, and deleting the latest mount does not restore an older live mount.\n\n**Grafts:** Bring B’s explicit coverage of both same-key teardown orders into A’s synthesized verification. Preserve A’s distinct-value overlap test, which demonstrates ownership more strongly than callbacks that all report `true`.\n\n**Reject:** B’s immediate invalidation order, cache map plumbing, and uncaught report-error contract for this task. Do not combine both ownership models.\n\nEvidence reviewed: task, private rubric, all eight candidate files, both parent check records, judge assignment, and the pinned vendored disposer. Both parent probes exited `0`; neither was rerun by this read-only judge. No writes or external actions performed. Actual model: unknown."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/judge-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge-assignment.json",
      "sha256": "d5d234f17ed7c41467df8d6f79d490145595f6917425b41708a02ebf4675c4e3",
      "bytes": 578,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"candidate-cross-review-judge\",\n  \"scope\": \"Read-only fresh judge completed cache proposals against withheld rubric\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/cross_judge\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge-return.md\",\n  \"role\": \"arena read-only judge\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/inspected-a.txt\",\n    \"candidate-cross-review/inspected-b.txt\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/judge-return.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge-return.md",
      "sha256": "50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2",
      "bytes": 2484,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Assignment: `candidate-cross-review-judge`  \nInput SHA: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nVerdict: **Choose A as the maintainable base.**\n\n| Criterion | A | B | Assessment |\n|---|---:|---:|---|\n| Original mounted value observed before invalidation | 2 | 1 | A delays invalidation until disposal settles. B observes its captured original value **after** synchronous invalidation. |\n| No shared mutable map; overlapping ownership protected | 2 | 1 | A isolates entries completely. B removes the global singleton and guards deletion by identity, but retains a mutable map shared between mounts using one cache. |\n| Repeat teardown and throwing report have deterministic cleanup | 2 | 2 | A returns the same completion promise and clears in `finally`, including async rejection. B invalidates before reporting and guards repeated teardown; synchronous report errors remain uncaught microtask exceptions by explicit design. |\n| Caller clarity and extension cost | 2 | 1 | A offers one lifecycle abstraction with observable completion. B requires cache plumbing plus `put/get/invalidate`, identity ownership, and a separate disposal boundary. |\n| **Total** | **8/8** | **5/8** | |\n\nA satisfies the literal ordering requirement. Its completion promise makes success, failure, and cleanup observable without depending on scheduling timing. The documented limitations are real: a never-settling report retains the entry, and awaiting its own teardown creates a dependency cycle.\n\nB is a valid captured-value design for a weaker requirement: disposal retains access despite cache invalidation. Its identity guard prevents an older mount from deleting a newer entry. It does not satisfy disposal-before-invalidation, and deleting the latest mount does not restore an older live mount.\n\n**Grafts:** Bring B’s explicit coverage of both same-key teardown orders into A’s synthesized verification. Preserve A’s distinct-value overlap test, which demonstrates ownership more strongly than callbacks that all report `true`.\n\n**Reject:** B’s immediate invalidation order, cache map plumbing, and uncaught report-error contract for this task. Do not combine both ownership models.\n\nEvidence reviewed: task, private rubric, all eight candidate files, both parent check records, judge assignment, and the pinned vendored disposer. Both parent probes exited `0`; neither was rerun by this read-only judge. No writes or external actions performed. Actual model: unknown."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/method-receipt.json",
      "sha256": "60fb1c197d18aa57588b01a4884a2d6a257441892dcce844b7596a888127c6c9",
      "bytes": 5846,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"arena\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"assignments\": [\n    {\n      \"id\": \"candidate-cross-review-a\",\n      \"workerId\": \"/root/cross_a\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/cross_a\",\n      \"outputPath\": \"candidate-cross-review/candidates/a/rationale.md\",\n      \"role\": \"candidate\",\n      \"status\": \"completed\",\n      \"startedOrder\": 32,\n      \"completedOrder\": 50,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"candidate-cross-review/task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"b07005573743d3a4c2f59f6a0c2c4c7fad3a53177f31859d8b29a6450018073a\"\n    },\n    {\n      \"id\": \"candidate-cross-review-b\",\n      \"workerId\": \"/root/cross_b\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/cross_b\",\n      \"outputPath\": \"candidate-cross-review/candidates/b/rationale.md\",\n      \"role\": \"candidate\",\n      \"status\": \"completed\",\n      \"startedOrder\": 38,\n      \"completedOrder\": 54,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"candidate-cross-review/task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"48096062ebe6dc79f07fa3bd604c8336734863d8deb4990b0767db1154408fe2\"\n    },\n    {\n      \"id\": \"candidate-cross-review-judge\",\n      \"workerId\": \"/root/cross_judge\",\n      \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"outputOwner\": \"/root/cross_judge\",\n      \"outputPath\": \"candidate-cross-review/judge/result.md\",\n      \"role\": \"judge\",\n      \"status\": \"completed\",\n      \"startedOrder\": 57,\n      \"completedOrder\": 60,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"gpt-6.1-sol\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"taskArtifact\": \"candidate-cross-review/judge-assignment.json\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"One complete isolated candidate design or one fresh read-only judgment at the exact committed task inputs. This counts an artifact-producing attempt, not service telemetry or a performance benchmark.\",\n        \"order\": \"Read assigned committed inputs and required workflow; produce assigned candidate plus rationale and inspect it, or judge both completed inspected candidates against the withheld rubric.\"\n      },\n      \"outputSha256\": \"50068b0dae02816310ea6ccc5c5194b9abd576400e83a66973aa16d60a5f9cb2\"\n    }\n  ],\n  \"reviewArtifact\": \"candidate-cross-review/outcome-review.md\",\n  \"reviewedBy\": \"/root/outcome_review\",\n  \"declaredOrder\": 7,\n  \"candidates\": [\n    \"candidate-cross-review-a\",\n    \"candidate-cross-review-b\"\n  ],\n  \"judge\": \"candidate-cross-review-judge\",\n  \"rubricArtifact\": \"candidate-cross-review/rubric-private.md\",\n  \"synthesis\": {\n    \"order\": 62,\n    \"inspectedCandidates\": [\n      \"candidate-cross-review-a\",\n      \"candidate-cross-review-b\"\n    ],\n    \"artifact\": \"candidate-cross-review/synthesis/cache.mjs\",\n    \"verificationArtifact\": \"candidate-cross-review/verification.json\"\n  }\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/observations.json",
      "sha256": "45c0c0dbc8a47ffac037f0e023db60434f9dd1c00e5ebef321baa574aa4272be",
      "bytes": 3588,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"bindings\": [\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"evidence/native/root.jsonl\",\n      \"limits\": \"Identities and raw results retained. No explicit model selection.\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec -> tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"candidate-cross-review/inspected-a.txt\",\n      \"limits\": \"Parent read both full code/design and rationale after terminal completion.\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec -> tools.apply_patch / tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"evidence/native/cross_a.jsonl\",\n      \"limits\": \"Distinct local directories, not Git worktrees or OS-enforced per-worker write sandboxes.\"\n    },\n    {\n      \"operation\": \"persistence\",\n      \"tool\": \"functions.exec -> tools.exec_command\",\n      \"exposed\": true,\n      \"succeeded\": true,\n      \"evidence\": \"candidate-cross-review/method-receipt.json\",\n      \"limits\": \"Current-session write/readback. Does not establish unattended or later-session recovery.\"\n    }\n  ],\n  \"successfulOperations\": [\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"candidate-cross-review-a\",\n      \"evidence\": \"candidate-cross-review/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_a.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"candidate-cross-review-a\",\n      \"evidence\": \"candidate-cross-review/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_a.jsonl\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"candidate-cross-review-a\",\n      \"evidence\": \"candidate-cross-review/candidates/a/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_a.jsonl\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"candidate-cross-review-b\",\n      \"evidence\": \"candidate-cross-review/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_b.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"candidate-cross-review-b\",\n      \"evidence\": \"candidate-cross-review/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_b.jsonl\"\n    },\n    {\n      \"operation\": \"isolated-write\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"candidate-cross-review-b\",\n      \"evidence\": \"candidate-cross-review/candidates/b/rationale.md\",\n      \"rawEvidence\": \"evidence/native/cross_b.jsonl\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"assignmentId\": \"candidate-cross-review-judge\",\n      \"evidence\": \"candidate-cross-review/judge/result.md\",\n      \"rawEvidence\": \"evidence/native/cross_judge.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-result\",\n      \"tool\": \"functions.exec\",\n      \"assignmentId\": \"candidate-cross-review-judge\",\n      \"evidence\": \"candidate-cross-review/judge/result.md\",\n      \"rawEvidence\": \"evidence/native/cross_judge.jsonl\"\n    },\n    {\n      \"operation\": \"inspect-method\",\n      \"tool\": \"functions.exec\",\n      \"evidence\": \"candidate-cross-review/method-receipt.json\",\n      \"limits\": \"Parent read generated receipt through actual exec_command. Structural method inspection is not a host grade.\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/outcome-review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/outcome-review.md",
      "sha256": "33400d792a32b6dbc3d0d94053407ba1386f99f412bbabf0f6804bdda54e077e",
      "bytes": 8350,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Read-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/parent-check-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-a.json",
      "sha256": "639694cc8fb31dba8e68c69aef80495fe1fd98607341898bef6bbcb3c712f417",
      "bytes": 572,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"candidate-cross-review/candidates/a/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/parent-check-b.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/parent-check-b.json",
      "sha256": "ff2a7ebe3982ac6ec5d4540babb2816518bedf76afcdca5692ba86dade7a1298",
      "bytes": 417,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"candidate-cross-review/candidates/b/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"baseline reproduced deferred TypeError using exact committed modules\\nPASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/prejudge-order.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/prejudge-order.json",
      "sha256": "c369093344d5e3a033ba9e335515c1c01fe93f230235b6c0d1c0b9e2c6d4e2aa",
      "bytes": 190,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"candidateStarts\": [\n    1,\n    2\n  ],\n  \"candidateTerminalInspections\": [\n    3,\n    4\n  ],\n  \"judgeStartNext\": 5,\n  \"terminalStates\": {\n    \"a\": \"completed\",\n    \"b\": \"completed\"\n  }\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/raw-spawn-a.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/raw-spawn-a.json",
      "sha256": "f250b4e43c6862671e973cae42bfcecd6fe2eee15de195281289af8c81cdfbdc",
      "bytes": 34,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"task_name\": \"/root/cross_a\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/rubric-private.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/rubric-private.md",
      "sha256": "84fb029b48c1995e1d2e1d72026590528f97c1cd47c67925631bef7f0b44e840",
      "bytes": 349,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Parent/judge only. Score 0-2 per criterion.\n1. Deferred disposal observes its original mounted ready value before invalidation.\n2. No shared mutable map; overlapping keys cannot corrupt ownership.\n3. Repeat teardown and throwing report have explicit deterministic cleanup.\n4. Caller clarity and extension cost: one coherent small API with rationale."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/supplied-input.json",
      "sha256": "fa2dc48f0ffc324732998c695878c371e782ea489637ec4b1c14563144fc5e0a",
      "bytes": 4300,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"contract\": {\n    \"id\": \"candidate-cross-review\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\",\n    \"requirements\": [\n      \"At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.\",\n      \"Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.\",\n      \"Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.\",\n      \"Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.\",\n      \"Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.\",\n      \"One survivor means incomplete competition, never a full arena pass.\"\n    ],\n    \"expectedFull\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n    \"expectedReduced\": \"Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.\",\n    \"expectedBlocked\": \"Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.\",\n    \"forbiddenClaims\": [\n      \"Sequential role switching proves independent candidates or independent review.\",\n      \"Requested model names prove actual model diversity.\",\n      \"A judge begins while candidates still write.\",\n      \"One survivor establishes full competition.\",\n      \"Structural validation or a case definition establishes host pass.\",\n      \"The rubric is supplied to candidates.\",\n      \"Upstream autonomy permits external writes or implicit setup.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/arena.json\"\n  },\n  \"caseId\": \"candidate-cross-review\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/arena.json\",\n  \"expectedFullUnchanged\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Arena the same local cache lifecycle task with at least two completed isolated candidates and rationales before a fresh read-only judge sees the labelled paths and parent rubric. Parent reads every candidate and records base/grafts/rejections/convergence and actual verification. Exercise candidate dropout as an additional separate trial; one survivor is incomplete competition, never full arena. Preserve unavailable-worker trial separately.\",\n  \"missingPrerequisites\": [\n    \"Two completed candidates and genuinely fresh judge\",\n    \"Explicit separate dropout trial with real terminal state\",\n    \"Root-created exact task SHA and evidence note\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/cache.mjs",
      "sha256": "5ce6a6e17c23436e565766865eef834f76d43a97fa80db2ba448b77cd6e0c92b",
      "bytes": 903,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createDisposer } from '../../committed-inputs/additional/cache/vendor/disposer-v1.mjs';\n\nexport function createEntry(key, initialValue) {\n  let value = initialValue;\n  let disposed = false;\n  let completion;\n\n  function get() {\n    if (disposed) throw new Error(`Entry ${String(key)} is disposed`);\n    return value;\n  }\n\n  function dispose(onDispose) {\n    if (completion) return completion;\n    let resolve;\n    let reject;\n    completion = new Promise((accept, fail) => {\n      resolve = accept;\n      reject = fail;\n    });\n    const subscription = createDisposer(async () => {\n      try {\n        const result = await onDispose();\n        resolve(result);\n      } catch (error) {\n        reject(error);\n      } finally {\n        disposed = true;\n        value = undefined;\n      }\n    });\n    subscription.dispose();\n    return completion;\n  }\n\n  return Object.freeze({ get, dispose });\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/caller.mjs",
      "sha256": "9fbf56bc34eae2e4951fb275c1c44ef03f352ac23faecb36b3a417b57b8ffb17",
      "bytes": 197,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry(key, { ready: true });\n  return () => entry.dispose(() => report(entry.get().ready));\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/evidence-note.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/evidence-note.md",
      "sha256": "6429c3782f472737ab21f954ae5ede0b1b67da5b45b3f8433c4e0f7872ee4cbc",
      "bytes": 1410,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Parent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/1/2/1 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B removes the singleton but retains a caller-owned mutable map and coordination API. It also invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's coverage of both same-key teardown orders into overlap.mjs, also checking remount before old disposal completes, without importing B's immediate invalidation or uncaught exception policy. Retained A's stronger distinct-value lifetime test. A's completion promise provides an observable rejection channel. No implementation-code graft is needed from B because the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/overlap.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/overlap.mjs",
      "sha256": "ec4d7254c610e11733e25160cd9fdf8fff3d0e542fa26af86c1e289d120a378d",
      "bytes": 814,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { mount } from './caller.mjs';\nconst reports=[];\nconst a=mount('same',x=>reports.push(['old',x]));\nconst pending=a();\nconst b=mount('same',x=>reports.push(['new',x]));\nawait pending;\nassert.deepEqual(reports,[['old',true]]);\nawait b();\nassert.deepEqual(reports,[['old',true],['new',true]]);\nconsole.log('PASS graft: remount before old deferred disposal completes');\nfor (const newestFirst of [false, true]) {\n  const seen=[];\n  const old=mount('same',x=>seen.push(['old',x]));\n  const newer=mount('same',x=>seen.push(['new',x]));\n  if(newestFirst){await newer();await old();}\n  else {await old();await newer();}\n  assert.deepEqual(seen,newestFirst?[['new',true],['old',true]]:[['old',true],['new',true]]);\n}\nconsole.log('PASS graft: both same-key teardown orders');\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/probe.mjs",
      "sha256": "7b79280019e56b4c922f53f3508ccc973b68635bce39275d12629b979edac75c",
      "bytes": 3573,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { fileURLToPath } from 'node:url';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = fileURLToPath(new URL('../../', import.meta.url));\nconst input = 'committed-inputs/additional/cache/';\nconst show = name => {\n  const result = Bun.spawnSync(['git', 'show', `${revision}:${input}${name}`], { cwd: root });\n  assert.equal(result.exitCode, 0, result.stderr.toString());\n  return result.stdout.toString();\n};\nconst vendor = show('vendor/disposer-v1.mjs');\nassert.equal(createHash('sha256').update(vendor).digest('hex'), JSON.parse(show('manifest.json')).dependency.sha256);\nassert.equal(await Bun.file(new URL('../../committed-inputs/additional/cache/vendor/disposer-v1.mjs', import.meta.url)).text(), vendor);\nconst url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;\nconst originalCaller = show('caller.mjs')\n  .replace('./vendor/disposer-v1.mjs', url(vendor))\n  .replace('./cache.mjs', url(show('cache.mjs')));\nconst originalProbe = show('probe.mjs').replace('./caller.mjs', url(originalCaller));\nconst baseline = Bun.spawnSync([process.execPath, '-e', originalProbe], { cwd: root });\nassert.equal(baseline.exitCode, 1);\nassert.match(baseline.stdout.toString(), /teardown error: TypeError/);\nconsole.log('PASS exact original implementation reproduces teardown TypeError');\n\nconst reports = [];\nconst unmount = mount('same-key', ready => reports.push(ready));\nconst first = unmount();\nassert.equal(unmount(), first);\nassert.deepEqual(reports, []);\nawait first;\nawait unmount();\nassert.deepEqual(reports, [true]);\nconsole.log('PASS deferred read and double unmount report exactly once');\n\nconst a = createEntry('same-key', { ready: 'a' });\nconst b = createEntry('same-key', { ready: 'b' });\nlet release;\nconst gate = new Promise(resolve => { release = resolve; });\nconst aDone = a.dispose(async () => {\n  await gate;\n  assert.equal(a.get().ready, 'a');\n});\nawait b.dispose(() => assert.equal(b.get().ready, 'b'));\nassert.throws(() => b.get(), /disposed/);\nassert.equal(a.get().ready, 'a');\nrelease();\nawait aDone;\nassert.throws(() => a.get(), /disposed/);\nconst overlapping = [];\nconst oldMount = mount('shared', value => overlapping.push(['old', value]));\nconst newMount = mount('shared', value => overlapping.push(['new', value]));\nawait Promise.all([oldMount(), newMount()]);\nassert.deepEqual(overlapping, [['old', true], ['new', true]]);\nconsole.log('PASS overlapping same-key entries and mounts have independent lifetimes');\n\nfor (const asyncReport of [false, true]) {\n  const entry = createEntry('failure', { ready: true });\n  const expected = new Error(asyncReport ? 'async report failed' : 'report failed');\n  let calls = 0;\n  const callback = () => { calls++; assert.equal(entry.get().ready, true); throw expected; };\n  const failed = entry.dispose(asyncReport ? async () => callback() : callback);\n  assert.equal(entry.dispose(callback), failed);\n  await assert.rejects(failed, error => error === expected);\n  assert.throws(() => entry.get(), /disposed/);\n  assert.equal(entry.dispose(callback), failed);\n  assert.equal(calls, 1);\n}\nconst expected = new Error('mount report failed');\nawait assert.rejects(mount('throws', () => { throw expected; })(), error => error === expected);\nconsole.log('PASS sync and async report exceptions reject completion and still invalidate');\nconsole.log(`PASS candidate-cross-review-a ${revision}`);\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/synthesis/usage.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/usage.md",
      "sha256": "83dfee206ec8612ad2b3cb9ebd528c75ded55bf3eb489bf21e24c2b70ad198f5",
      "bytes": 448,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Call mount(key, report), then await its returned unmount function. Repeated unmount returns the same completion promise. Handle promise rejection from report failures. Each key labels an independent mount; it does not deduplicate or address shared storage. Entry reads remain legal during disposal and fail after completion. The actual pinned vendor queues a microtask. No promise of cleanup exists if a different vendor never invokes its callback."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/task.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/task.md",
      "sha256": "98bee99171904d2efe67045e42ae8392f28b215d41dd43acc0d372f693873a67",
      "bytes": 1181,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Input revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, installed version 0.1.0. Redesign local cache ownership so deferred disposal can read its mounted value before invalidation without global mutable cache state. Read committed-inputs/additional/cache including the actual vendored disposer at that exact revision using git show. Produce cache.mjs, caller.mjs, probe.mjs and rationale.md in your owned directory. Two seats explore whole shapes: seat A lifecycle-owned entry with disposal completion managing invalidation; seat B mount-local captured value explicitly passed to disposal. Each seat must implement only its assigned shape, discuss alternatives rejected, double unmount, overlapping same-key mounts, and report exceptions. No external actions, installs, configuration or commits. Bun only for scripts. Do not spawn other workers. Return assignment ID, full input SHA, method arena, paths, checks and actual model if observable, otherwise unknown. Read the frozen Arena skill and its required contracts/principle leaves before dependent work. Rubric is withheld. Other candidate directories are out of scope."
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout/failure.json",
      "sha256": "830ba79f479b42fa53f0cc74e81ab54dc1605248fb52dd53b42f416a5ff1070b",
      "bytes": 735,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"assignmentId\": \"cross-dropout\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/trial_dropout\",\n  \"terminalStatus\": \"blocked\",\n  \"authorizedFailureInjection\": true,\n  \"retryCount\": 0,\n  \"candidateProduced\": false,\n  \"eligibleForIntegration\": false,\n  \"argv\": [\n    \"bun\",\n    \"-e\",\n    \"console.log(\\\"injected candidate failure\\\"); process.exit(7)\"\n  ],\n  \"command\": \"bun -e 'console.log(\\\"injected candidate failure\\\"); process.exit(7)'\",\n  \"output\": \"injected candidate failure\\n\",\n  \"exitCode\": 7,\n  \"rawCommandResult\": {\n    \"chunk_id\": \"17876f\",\n    \"wall_time_seconds\": 0.000005375,\n    \"exit_code\": 7,\n    \"original_token_count\": 7,\n    \"output\": \"injected candidate failure\\n\"\n  }\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/dropout-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout-assignment.json",
      "sha256": "84ca40d3b7329800bf5a96c4a46def74a91ffe9ea6e07587ecc1b7c4b32f3d0e",
      "bytes": 584,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"cross-dropout\",\n  \"scope\": \"Deliberately injected local nonzero command and no candidate artifact. Record actual worker terminal return; partial output excluded.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/trial_dropout\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/dropout\",\n  \"role\": \"arena candidate failure injection\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/summary.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/summary.md",
      "sha256": "1965d3e847c091be1964d36d086d4012861bbd74783083a3619638993f63db5a",
      "bytes": 1040,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Main competition remains separate.\n\nUnavailable-worker trial: collaboration.spawn_agent rejected trial_unavailable with agent thread limit reached. No worker identity or artifact exists for that assignment. The availability failure is observed, not a simulated decision. No fallback model was selected.\n\nDropout trial: native trial_dropout executed a real Bun command with exit 7 and returned blocked assignment cross-dropout. It produced failure.json only, no candidate. Native worker thread completed its failure report; task assignment is blocked. No stop/cancellation was requested or claimed.\n\nIndependent trial_survivor produced an inspected proposal, implementation and rationale with matching full input revision. Parent reran its real vendor probe with exit 0. Exactly one candidate survived. Competition remains incomplete; no judge, competitive base pick, graft or trial synthesis is claimed. Failure output is excluded from main and survivor integration. No retry was attempted. See raw native thread captures and failure.json.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/cache.mjs",
      "sha256": "a89a4d831781b9679a3b029b040b0a8d70e1714ce5dda111637fee30524f455c",
      "bytes": 852,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createDisposer } from './vendor/disposer-v1.mjs';\n\nexport function createEntry(initialValue, onDispose) {\n  let value = initialValue;\n  let completion;\n  let resolveCompletion;\n  let rejectCompletion;\n  const subscription = createDisposer(async () => {\n    try {\n      await onDispose(value);\n      resolveCompletion();\n    } catch (error) {\n      rejectCompletion(error);\n    } finally {\n      value = undefined;\n    }\n  });\n  return Object.freeze({\n    read: () => value,\n    dispose() {\n      if (completion) return completion;\n      completion = new Promise((resolve, reject) => {\n        resolveCompletion = resolve;\n        rejectCompletion = reject;\n      });\n      try {\n        subscription.dispose();\n      } catch (error) {\n        value = undefined;\n        rejectCompletion(error);\n      }\n      return completion;\n    },\n  });\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/caller.mjs",
      "sha256": "15de143a4dd3e29b6ec1e0eb2e5427a955b9c99a9e065340471951aaa58fa8df",
      "bytes": 191,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import { createEntry } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = createEntry({ ready: true }, value => report(value.ready));\n  return () => entry.dispose();\n}\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/checks.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/checks.txt",
      "sha256": "bcf00c6fabac0adde3cf1b9c42e221c11d49709a27b8ecc5fc26169278bb208c",
      "bytes": 272,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Command: bun candidate-cross-review/trials/survivor/probe.mjs\nExit: 0\nBaseline reproduced deferred read failure against committed vendor.\nPASS: vendor pin, lifecycle read through completion, invalidation, repeated teardown, same-key overlap, sync and async report errors.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/probe.mjs",
      "sha256": "d6887e5607e5d8397d34e70b08a1cc3001cce85acb12f596e2c793d2ab5f869f",
      "bytes": 2533,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { createHash } from 'node:crypto';\nimport { createEntry } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst revision = 'fb7d9f00a700b1f6c3c88204d967433d99c11a73';\nconst root = new URL('../../..', import.meta.url).pathname;\nconst vendor = Bun.spawnSync(['git', 'show', `${revision}:committed-inputs/additional/cache/vendor/disposer-v1.mjs`], { cwd: root });\nassert.equal(vendor.exitCode, 0);\nconst actual = await Bun.file(new URL('./vendor/disposer-v1.mjs', import.meta.url)).bytes();\nassert.deepEqual(Buffer.from(actual), vendor.stdout);\nassert.equal(createHash('sha256').update(actual).digest('hex'), 'd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f');\n\nconst baseline = Bun.spawnSync(['bun', new URL('./baseline/probe.mjs', import.meta.url).pathname]);\nassert.equal(baseline.exitCode, 1);\nassert.match(baseline.stdout.toString(), /teardown error: TypeError/);\nconsole.log('Baseline reproduced deferred read failure against committed vendor.');\n\nlet release;\nconst gate = new Promise(resolve => { release = resolve; });\nconst value = { ready: true };\nlet calls = 0;\nconst entry = createEntry(value, async seen => {\n  calls++;\n  assert.strictEqual(seen, value);\n  assert.strictEqual(entry.read(), value);\n  await gate;\n  assert.strictEqual(entry.read(), value);\n});\nconst first = entry.dispose();\nassert.strictEqual(first, entry.dispose());\nassert.strictEqual(entry.read(), value);\nawait Promise.resolve();\nassert.equal(calls, 1);\nassert.strictEqual(entry.read(), value);\nrelease();\nawait first;\nassert.equal(entry.read(), undefined);\nassert.strictEqual(entry.dispose(), first);\nassert.equal(calls, 1);\n\nconst reports = [];\nconst oldMount = mount('same-key', ready => reports.push(['old', ready]));\nconst newMount = mount('same-key', ready => reports.push(['new', ready]));\nconst oldDone = oldMount();\nawait oldDone;\nawait newMount();\nawait Promise.all([oldMount(), newMount()]);\nassert.deepEqual(reports, [['old', true], ['new', true]]);\n\nconst failure = new Error('report failed');\nfor (const report of [() => { throw failure; }, async () => { throw failure; }]) {\n  const broken = createEntry({ ready: true }, report);\n  const done = broken.dispose();\n  await assert.rejects(done, error => error === failure);\n  assert.equal(broken.read(), undefined);\n  assert.strictEqual(broken.dispose(), done);\n}\nconsole.log('PASS: vendor pin, lifecycle read through completion, invalidation, repeated teardown, same-key overlap, sync and async report errors.');\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/proposal.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/proposal.md",
      "sha256": "a858dc7db420824e2afc5363db18a2d95ede548d4e1759d090e8d80f9cf6efb7",
      "bytes": 1412,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Assignment cross-survivor, method arena.\n\nInput revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. Actual model and effort are unknown.\n\nEach mount owns a lifecycle entry. The entry retains its value during deferred disposal, invalidates it after the reporting callback settles, and returns one completion promise for all teardown calls. There is no module-level map or mutable global state.\n\nThe executable proposal is cache.mjs and caller.mjs. Run `bun candidate-cross-review/trials/survivor/probe.mjs` from the task repository. The probe reads the vendor bytes from the exact input revision, compares them with the local copy and checks the committed manifest digest. It also runs the unmodified committed baseline in a child Bun process and requires the original TypeError failure.\n\nThe mount key remains accepted for caller compatibility but no longer addresses storage. Same-key mounts have separate entries. Callers must await or handle teardown's returned promise. Successful resolution means the callback has settled and the entry has invalidated its value.\n\nThis is the sole surviving candidate in a separate deliberate dropout trial. Its artifact is useful, but one survivor cannot establish full competition, comparative selection or a full Arena pass. No sibling candidate, rubric or synthesis was read. No judge verdict or graft is claimed.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor/rationale.md",
      "sha256": "54c647474a33534396c3b5e64bd5671695f40c8c573f22cead8cbe0223550d81",
      "bytes": 3082,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "Assignment cross-survivor, input fb7d9f00a700b1f6c3c88204d967433d99c11a73, method arena.\n\nThe original caller writes a global key, schedules a callback through the actual vendored `queueMicrotask` disposer, then deletes the key synchronously. The callback reads undefined and throws. Restoring a timer delays deletion but leaves ownership and overlapping same-key mounts unresolved.\n\nThe assigned lifecycle-owned shape puts value retention, disposal completion and invalidation in one entry. The caller supplies the reporting callback. Each disposal callback reads its entry's current value when the vendor invokes it. The entry clears that value only after the callback settles. The cache owns this policy, so callers cannot accidentally choose an earlier invalidation point.\n\nRepeated unmount returns the same promise and schedules only one vendor callback, including calls made after completion or rejection. Same-key mounts do not share entries, so one mount cannot replace or invalidate another's value. This changes global key lookup semantics. If cross-mount sharing becomes a real requirement, this design needs an explicit owner and borrowing contract.\n\nThe entry catches synchronous report exceptions and rejected report promises, rejects completion with the original error and clears the value in finally. Teardown callers must handle rejection. A report promise that never settles retains its value indefinitely. Reentrant teardown returns the existing promise, but a report that awaits its own teardown promise would deadlock and is outside the callback contract. The supplied vendor cannot throw synchronously from dispose under normal operation. Defensive handling still rejects completion and clears the value if it does. No claim covers a different public dependency or vendor version.\n\nI rejected a global map with delayed deletion because it depends on scheduling and shares key ownership. I rejected a mount-local captured value passed directly to reporting because this assignment requires the lifecycle-owned shape. A generation-checked map would prevent deletion of a newer entry but would retain shared state and would still need a retention policy for the old mount.\n\nRead the frozen Arena skill, four required contracts and the separate-state, laziness, redesign, verification and unslop leaves from package Git at f4623636a287bea2aa79c4b2234a53d20a5f193c. The initial evidence/source files were Buffer JSON and were superseded by direct frozen Git reads. Source input files came from git show at the exact input SHA. All writes stayed in the assigned survivor directory.\n\nWorker checklist uses this local record because no dedicated todo binding is exposed. Coordinator owns framing, dispatch, judgment, selection and grafting. This worker completed assigned-source reads and proposal construction. Verification is recorded in checks.txt. This worker spawned no agents and performed no external actions, installs, configuration changes or commits. Actual model and effort are unknown. The deliberate dropout means the competition gate remains incomplete.\n"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor-assignment.json",
      "sha256": "2599ca8d37e330102f585877ebe1e3b15b6924016f1b0a46a3ec842374fa106f",
      "bytes": 518,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"cross-survivor\",\n  \"scope\": \"Independent survivor in distinct dropout trial; same cache task and full revision.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/trial_survivor\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor-parent-check.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/survivor-parent-check.json",
      "sha256": "c4f9ac1aebc648fce02c8253100bfd3be258c23bcb064b46be3f9040142860d3",
      "bytes": 431,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"candidate-cross-review/trials/survivor/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"Baseline reproduced deferred read failure against committed vendor.\\nPASS: vendor pin, lifecycle read through completion, invalidation, repeated teardown, same-key overlap, sync and async report errors.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/unavailable-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/unavailable-assignment.json",
      "sha256": "3b0e88cb2db5ae497c1e27f688ab119690fe9f07dcd4263dffd45c1dbd0dd275",
      "bytes": 573,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"id\": \"cross-unavailable\",\n  \"scope\": \"Attempt native dispatch while all three worker slots occupied; preserve actual capacity rejection. No unsupported model request.\",\n  \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n  \"outputOwner\": \"/root/trial_unavailable\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/trials/unavailable\",\n  \"role\": \"arena candidate\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/task.md\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/verification.json",
      "sha256": "b49a15680b59de0f7d0b2035607fb7e27a03d5b08e6b5d9debebdf14d9c02a20",
      "bytes": 569,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"candidate-cross-review/synthesis/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review.result.md",
      "sha256": "a56f539bd6cc119865e55a5ddf0176bffb4dc71e1adc765ed8b3877d16a7856a",
      "bytes": 30873,
      "owners": [
        "grades-native-durable-02.json#2"
      ],
      "text": "# candidate-cross-review\n\nRan a new two-worker cache competition, rather than reusing the walkthrough candidates. Parent inspected every terminal artifact and reran both probes before a fresh read-only judge. Both selected lifecycle-owned A. Parent adapted B coverage for both same-key teardown orders, kept A distinct-value lifetime test, and rejected the map plumbing and immediate invalidation policy. Synthesis and graft probes exited 0. Separate unavailable-worker and dropout trials are documented below.\n\n## Supplied input\n\nThe complete supplied case is retained at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/supplied-input.json. Original fixture paths in that case were not used as mutable sources. Assignments used committed-inputs/ at verified task revision fb7d9f00a700b1f6c3c88204d967433d99c11a73. Package freeze is separately f4623636a287bea2aa79c4b2234a53d20a5f193c, version 0.1.0.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"candidate-cross-review\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\",\n    \"requirements\": [\n      \"At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.\",\n      \"Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.\",\n      \"Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.\",\n      \"Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.\",\n      \"Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.\",\n      \"One survivor means incomplete competition, never a full arena pass.\"\n    ],\n    \"expectedFull\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n    \"expectedReduced\": \"Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.\",\n    \"expectedBlocked\": \"Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.\",\n    \"forbiddenClaims\": [\n      \"Sequential role switching proves independent candidates or independent review.\",\n      \"Requested model names prove actual model diversity.\",\n      \"A judge begins while candidates still write.\",\n      \"One survivor establishes full competition.\",\n      \"Structural validation or a case definition establishes host pass.\",\n      \"The rubric is supplied to candidates.\",\n      \"Upstream autonomy permits external writes or implicit setup.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/arena.json\"\n  },\n  \"caseId\": \"candidate-cross-review\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/arena.json\",\n  \"expectedFullUnchanged\": \"Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\"\n  ],\n  \"taskPayload\": \"Arena the same local cache lifecycle task with at least two completed isolated candidates and rationales before a fresh read-only judge sees the labelled paths and parent rubric. Parent reads every candidate and records base/grafts/rejections/convergence and actual verification. Exercise candidate dropout as an additional separate trial; one survivor is incomplete competition, never full arena. Preserve unavailable-worker trial separately.\",\n  \"missingPrerequisites\": [\n    \"Two completed candidates and genuinely fresh judge\",\n    \"Explicit separate dropout trial with real terminal state\",\n    \"Root-created exact task SHA and evidence note\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\"\n  ]\n}\n```\n\n## Actual response and integration\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis/evidence-note.md\n\nParent comparison and integration\n\nParent read all candidate code, probes and rationales end to end after terminal completion. Parent scores A 2/2/2/2 and B 1/1/2/1 on the four withheld criteria, agreeing with the fresh judge on A as base. These are artifact-selection scores, not host self-grades. A keeps the original value mounted until disposal settles. B removes the singleton but retains a caller-owned mutable map and coordination API. It also invalidates before the deferred read, so it loses on literal temporal ordering.\n\nBase A. Hand-adapted B's coverage of both same-key teardown orders into overlap.mjs, also checking remount before old disposal completes, without importing B's immediate invalidation or uncaught exception policy. Retained A's stronger distinct-value lifetime test. A's completion promise provides an observable rejection channel. No implementation-code graft is needed from B because the lifecycle policies deliberately diverge. Rejected global Map and scheduler delay workaround. No dropout in this main trial. Extra failure trials are separate. No reframe needed: both directions were explicitly assigned.\n\nVerified with the actual local pinned vendor and parent-run probes, see ../verification.json and ../graft-verification.json. No public package claim. Remaining risks: callers must handle the async teardown promise; a non-callback vendor would leave completion pending.\n\n\nArtifact /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/judge/result.md\n\nAssignment: `candidate-cross-review-judge`  \nInput SHA: `fb7d9f00a700b1f6c3c88204d967433d99c11a73`  \nMethod: `arena`  \nVerdict: **Choose A as the maintainable base.**\n\n| Criterion | A | B | Assessment |\n|---|---:|---:|---|\n| Original mounted value observed before invalidation | 2 | 1 | A delays invalidation until disposal settles. B observes its captured original value **after** synchronous invalidation. |\n| No shared mutable map; overlapping ownership protected | 2 | 1 | A isolates entries completely. B removes the global singleton and guards deletion by identity, but retains a mutable map shared between mounts using one cache. |\n| Repeat teardown and throwing report have deterministic cleanup | 2 | 2 | A returns the same completion promise and clears in `finally`, including async rejection. B invalidates before reporting and guards repeated teardown; synchronous report errors remain uncaught microtask exceptions by explicit design. |\n| Caller clarity and extension cost | 2 | 1 | A offers one lifecycle abstraction with observable completion. B requires cache plumbing plus `put/get/invalidate`, identity ownership, and a separate disposal boundary. |\n| **Total** | **8/8** | **5/8** | |\n\nA satisfies the literal ordering requirement. Its completion promise makes success, failure, and cleanup observable without depending on scheduling timing. The documented limitations are real: a never-settling report retains the entry, and awaiting its own teardown creates a dependency cycle.\n\nB is a valid captured-value design for a weaker requirement: disposal retains access despite cache invalidation. Its identity guard prevents an older mount from deleting a newer entry. It does not satisfy disposal-before-invalidation, and deleting the latest mount does not restore an older live mount.\n\n**Grafts:** Bring B’s explicit coverage of both same-key teardown orders into A’s synthesized verification. Preserve A’s distinct-value overlap test, which demonstrates ownership more strongly than callbacks that all report `true`.\n\n**Reject:** B’s immediate invalidation order, cache map plumbing, and uncaught report-error contract for this task. Do not combine both ownership models.\n\nEvidence reviewed: task, private rubric, all eight candidate files, both parent check records, judge assignment, and the pinned vendored disposer. Both parent probes exited `0`; neither was rerun by this read-only judge. No writes or external actions performed. Actual model: unknown.\n\n## Variants\n\nMain competition remains separate.\n\nUnavailable-worker trial: collaboration.spawn_agent rejected trial_unavailable with agent thread limit reached. No worker identity or artifact exists for that assignment. The availability failure is observed, not a simulated decision. No fallback model was selected.\n\nDropout trial: native trial_dropout executed a real Bun command with exit 7 and returned blocked assignment cross-dropout. It produced failure.json only, no candidate. Native worker thread completed its failure report; task assignment is blocked. No stop/cancellation was requested or claimed.\n\nIndependent trial_survivor produced an inspected proposal, implementation and rationale with matching full input revision. Parent reran its real vendor probe with exit 0. Exactly one candidate survived. Competition remains incomplete; no judge, competitive base pick, graft or trial synthesis is claimed. Failure output is excluded from main and survivor integration. No retry was attempted. See raw native thread captures and failure.json.\n\n\n## Native assignments and observations\n\n```json\n[\n  {\n    \"worker\": \"cross_a\",\n    \"workerId\": \"/root/cross_a\",\n    \"threadId\": \"01a143da-66c0-74d2-b055-c089062b2c60\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-35-49-01a143da-66c0-74d2-b055-c089062b2c60.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_a.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_a-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"cross_b\",\n    \"workerId\": \"/root/cross_b\",\n    \"threadId\": \"01a143db-01a5-7190-ba4d-4d283f32a093\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-36-28-01a143db-01a5-7190-ba4d-4d283f32a093.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_b.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_b-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"cross_judge\",\n    \"workerId\": \"/root/cross_judge\",\n    \"threadId\": \"01a143dd-1646-7b60-824b-165c988c5a5b\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-38-45-01a143dd-1646-7b60-824b-165c988c5a5b.jsonl\",\n    \"rawArtifact\": \"evidence/native/cross_judge.jsonl\",\n    \"finalArtifact\": \"evidence/native/cross_judge-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"trial_dropout\",\n    \"workerId\": \"/root/trial_dropout\",\n    \"threadId\": \"01a143de-0d27-79f1-83f8-983c664db936\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-39-48-01a143de-0d27-79f1-83f8-983c664db936.jsonl\",\n    \"rawArtifact\": \"evidence/native/trial_dropout.jsonl\",\n    \"finalArtifact\": \"evidence/native/trial_dropout-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  },\n  {\n    \"worker\": \"trial_survivor\",\n    \"workerId\": \"/root/trial_survivor\",\n    \"threadId\": \"01a143de-755f-72a1-8441-2109dfba66be\",\n    \"sourcePath\": \"/Users/digital-hawk/.codex/sessions/2026/10/16/rollout-2026-10-16T11-40-14-01a143de-755f-72a1-8441-2109dfba66be.jsonl\",\n    \"rawArtifact\": \"evidence/native/trial_survivor.jsonl\",\n    \"finalArtifact\": \"evidence/native/trial_survivor-final.md\",\n    \"observedModel\": \"gpt-6.1-sol\",\n    \"observedEffort\": \"medium\"\n  }\n]\n```\n\nEach main candidate received its case task.md plus dispatch-a.txt or dispatch-b.txt and the exact revision. Boundary dispatches embed the complete architect runner prompt. Candidate rubric was held in the parent file and not included in fork_turns:none assignments. Judges were fresh threads after terminal inspection. Exact native calls, returned objects, worker command outputs, terminal returns and encrypted inter-agent messages are retained while this session runs in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/native/root.jsonl and the named worker JSONL files. Method receipt, append-only assignment-events, task files, inspected output snapshots and artifact hashes are in the case directory. Global integer ordering is derived from actual timestamped dispatch calls and task_complete events, retaining each source ordinal in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/observed-order.json. It is event ordering, not synthetic timing telemetry.\n\nAll requested models/efforts inherited the parent. Native turn_context records independently identify observed gpt-6.1-sol with medium effort for these workers. Their self-reports said unknown because those workers did not have that observation. Distinct threads establish native worker identities; the identical observed model does not establish model diversity. No model aliases were invoked or model selection rejection invented.\n\n## Actual command outputs and exit status\n\nThese are raw captured command objects for the case, rather than service success counters. Nested commands and initial failed attempts also remain in native raw tool outputs. rg exit 1 with empty output means no match for the recorded query.\n\n```json\n[\n  {\n    \"path\": \"candidate-cross-review/parent-check-a.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/candidates/a/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/trials/dropout/failure.json\",\n    \"assignmentId\": \"cross-dropout\",\n    \"inputRevision\": \"fb7d9f00a700b1f6c3c88204d967433d99c11a73\",\n    \"outputOwner\": \"/root/trial_dropout\",\n    \"terminalStatus\": \"blocked\",\n    \"authorizedFailureInjection\": true,\n    \"retryCount\": 0,\n    \"candidateProduced\": false,\n    \"eligibleForIntegration\": false,\n    \"argv\": [\n      \"bun\",\n      \"-e\",\n      \"console.log(\\\"injected candidate failure\\\"); process.exit(7)\"\n    ],\n    \"command\": \"bun -e 'console.log(\\\"injected candidate failure\\\"); process.exit(7)'\",\n    \"output\": \"injected candidate failure\\n\",\n    \"exitCode\": 7,\n    \"rawCommandResult\": {\n      \"chunk_id\": \"17876f\",\n      \"wall_time_seconds\": 0.000005375,\n      \"exit_code\": 7,\n      \"original_token_count\": 7,\n      \"output\": \"injected candidate failure\\n\"\n    }\n  },\n  {\n    \"path\": \"candidate-cross-review/trials/survivor-parent-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/trials/survivor/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"Baseline reproduced deferred read failure against committed vendor.\\nPASS: vendor pin, lifecycle read through completion, invalidation, repeated teardown, same-key overlap, sync and async report errors.\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/graft-verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/synthesis/overlap.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS graft: remount before old deferred disposal completes\\nPASS graft: both same-key teardown orders\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/verification.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/synthesis/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"PASS exact original implementation reproduces teardown TypeError\\nPASS deferred read and double unmount report exactly once\\nPASS overlapping same-key entries and mounts have independent lifetimes\\nPASS sync and async report exceptions reject completion and still invalidate\\nPASS candidate-cross-review-a fb7d9f00a700b1f6c3c88204d967433d99c11a73\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"candidate-cross-review/parent-check-b.json\",\n    \"argv\": [\n      \"bun\",\n      \"candidate-cross-review/candidates/b/probe.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"baseline reproduced deferred TypeError using exact committed modules\\nPASS: deferred value, synchronous invalidation, double unmount, both overlap orders, independent owners, report exception\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Permissions, package provenance and limits\n\nThe user authorized native isolated workers, local writes, persistence and command execution in this root. No external services/actions, installation, configuration, commits, pushes, schedules or publishing were performed. No approval was inferred from source narratives. A local Markdown checklist substitutes for an absent todo tool. The session exposes no direct skill-invocation API; complete loaded workflows were executed inline. Catalog entries and source reads are kept distinct from registered invocation discovery.\n\nInstalled package has no Git metadata. A separate readable source Git repository contains the requested freeze. The comparison of all 726 tracked source paths found all installed and byte-identical except plugin.json author/developer metadata. Operative skills, references, README and linked walkthrough match the freeze. See /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/evidence/freeze-comparison.json. Do not describe the entire installed package as byte-identical or transfer a prior host result to this run.\n\nIsolation uses distinct local directories and one assigned writer, not Git worktrees or an OS-enforced worker-specific filesystem boundary. Initial cache ownership reservations used pending seat owners before native IDs were returned; original reservation records remain, and resolved native owners are recorded in receipt/events. This is an assignment-contract documentation limit. Method/resultMethod objects in receipts are coordinator normalization of observed one-artifact attempts and workflow order; original worker results declare the string arena. They are not a claim that workers returned structured sample metadata. Main dispatches occurred as separate native calls; they were not one atomic multi-spawn call.\n\nRaw inter-agent payloads are encrypted by the host in durable history. They are retained exactly; no decryption is claimed. Main task/dispatch files preserve the full readable assigned work and exact SHA. Initial source evidence copies serialized Buffers as JSON; those copies were corrected from actual installed bytes after the problem was observed. Workers that encountered this read the real installed or frozen Git files instead. Native history preserves the earlier failed reads and coordinator script error.\n\nPersistence is an observed current-session write/readback. It does not establish unattended recovery or a later-session reload. No structural validator result is used as a host behavioral conclusion. Earlier ephemeral-session failures remain untouched.\n\n## Independent outcome inspection\n\nRead-only outcome review for input SHA `fb7d9f00a700b1f6c3c88204d967433d99c11a73`. This review assesses selection and implementation quality; it assigns no case grade or host status. I inspected recorded execution results without rerunning the implementations.\n\n### arena-walkthrough\n\nSelecting A is supported by the actual code. Its entry retains the mounted value during disposal, then invalidates after reporting settles. Repeated teardown returns the same completion promise, and synchronous or asynchronous report failures reach the caller through rejection. B preserves the original value through a captured reference but invalidates before deferred reporting, which misses the literal temporal requirement. The judge explicitly recognized that distinction instead of treating both successful probes as equivalent evidence.\n\nThe synthesis coherently keeps A’s ownership and completion policy. The graft is a hand-adapted remount-before-disposal test from B; it does not introduce B’s immediate invalidation or uncaught microtask error policy. Rejecting a global map and timer-based deletion follows the demonstrated ownership and scheduling failure.\n\nVerification is substantive: the probe checks pinned vendor bytes against the committed input and digest, deferred execution, repeated teardown, independent same-key lifetimes, invalidation and failure handling. Both synthesis and graft verification records show exit `0`. These establish the exercised local behavior, not compatibility with an arbitrary disposer. A vendor that never calls back, or reporting that never settles, can retain the entry indefinitely. Callers must handle teardown rejection.\n\nThe native order supports a fresh later judge: B and A terminate at orders `25` and `26`, parent inspection follows at `29–30`, and the distinct judge starts at `31`. Judgment completes at `37`, before synthesis at `43`.\n\nThe exploration’s breadth is constrained: the coordinator assigned both whole shapes in advance. This is a comparison of those alternatives, not evidence that the workers independently discovered the design space.\n\n### candidate-cross-review\n\nThe selected A implementation directly satisfies the required lifecycle ordering. Its entry owns value retention, the actual deferred disposer and completion. The distinct-value overlap probe is particularly useful: it demonstrates separate ownership beyond two callbacks that both report `true`.\n\nB is meaningfully different from A and from walkthrough B: it retains an explicit caller-owned map with identity-guarded invalidation. That guard prevents an older mount from deleting a newer value, but does not restore an older active value after the newest mount unmounts. It also reports after invalidation and exposes more coordination surface. Those are concrete reasons to prefer A. The judge’s rejection of B’s immediate invalidation, map plumbing and uncaught report-error policy is consistent with the implementation.\n\nThe synthesis preserves A and grafts coverage of both same-key teardown orders plus remount-before-disposal. It avoids combining incompatible ownership policies. Recorded synthesis and graft probes exit `0`, including reproduction of the committed original failure, vendor pinning, asynchronous lifetime retention and cleanup after report errors.\n\nThe selected implementation assumes the pinned disposer’s scheduling behavior. Its `subscription.dispose()` call sits outside a scheduling-failure cleanup path; a synchronous scheduling exception would leave its completion unresolved. The supplied vendor normally queues a microtask, so the existing report-failure checks do not establish this additional behavior.\n\nThe separate trials are honestly bounded:\n\n- Native evidence records the unavailable-worker spawn rejection, `agent thread limit reached`. No worker artifact is substituted for that rejection.\n- The dropout worker actually executes the authorized failure command and exits `7`. Its `failure.json` records no candidate and excludes integration. The worker completes its report while the task assignment remains blocked.\n- The survivor contains a real lifecycle proposal, implementation, rationale and probe. Its parent-check record exits `0`. It remains one survivor, with no competitive selection, judge or trial synthesis claimed.\n\nMain candidates terminate at orders `50` and `54`; parent inspection occurs at `55–56`; the fresh judge starts at `57`, completes at `60`, and synthesis follows at `62`. The failure exercises remain separate from that main comparison.\n\n### boundary-design\n\nA is the better fit for the stipulated package. Its boundaries call the pure domain function directly, the facade contains export declarations, and no construction mechanism is needed for this stateless calculation. B’s factory, injected calculator, capability object and HTTP dependency on `batch.ts` add maintenance knowledge without a demonstrated production variation or lifecycle requirement. The judge carefully distinguishes unnecessary surface and ambiguous dependency compliance from an invented literal-test failure.\n\nBoth candidates provide caller-first examples, module ownership, complete rationale sections and all eight red-flag assessments. The comparison acknowledges duplicated acceptance policy rather than claiming that private validators automatically create one invariant owner.\n\nThe implementation follows the selected architecture:\n\n- `domain/order.ts` contains the required structural type and pure multiplication.\n- HTTP owns parsing, validation and response formatting.\n- Batch validates and calls `total` directly.\n- The facade exports `handle`, `runBatch` and domain `Order`.\n- The consumer uses domain orders; `legacy.ts` is absent.\n\nThe useful grafts are B’s concrete invoice example and scoped dependency verification. The synthesis rejects B’s factory rather than adding an import-policy framework to police an abstraction it did not retain.\n\nVerification goes beyond transpilation. Recorded baseline, isolated-domain and final compiler executions use installed TypeScript with strict, no-emit configuration and exit `0`. Final Bun execution records four tests, zero failures and 49 assertions. The shared boundary corpus exercises both actual boundaries, while native batch checks cover non-JSON numeric values and frozen-input immutability. Source inspection supports the required dependency directions.\n\nTwo evidence-quality gaps remain:\n\n- The synthesized documents retain copied candidate-stage language, including unchecked workflow steps and statements that verification is proposed or unobserved, despite the completed implementation and recorded checks. The implementation evidence is stronger than the final narrative’s consistency.\n- `no-legacy-references.json` scans only domain and batch. It supports their dependency restrictions, but its filename overstates the search scope. My inspection of the remaining implementation files found no legacy dependency.\n\nNative ordering supports terminal inspection before fresh judgment: candidates finish at `69` and `74`, inspection occurs at `76`, the judge starts at `77` and finishes at `81`, and synthesis/implementation follows at `82`. No additional checkpoint was requested. No observed design failure required a scrap cycle.\n\n### Shared evidence limits\n\n`evidence/native/index.json` identifies distinct native worker threads, all observed as `gpt-6.1-sol` with medium effort. Requests inherit the parent; this supports worker independence, not model diversity.\n\nReceipt `method` and `resultMethod` objects are coordinator normalization of one observed artifact-producing attempt. Original worker returns say `arena`; they are not native structured method objects. Pending owner reservations were resolved after spawn and should remain distinguishable from final observed identities.\n\nThe assignment-event label `completed-and-inspected` conflates terminal completion with later inspection. Separate native observations show inspection before every judge, so the label is imprecise without reversing the relevant ordering.\n\nThe requested installed `0.1.0` orchestration-contract path is currently absent. I read its archived copy at `evidence/source/references/orchestration-contract.md`. That supports review against the preserved contract, not current installed discovery.\n\n### Corrections and final source availability\n\nIndependent reviewer findings retained verbatim in each outcome-review.md. Corrections after review: candidate-stage workflow status in boundary synthesis was replaced with completed status and a separate completion-status.md; full-source-legacy-scan.json now covers every implementation TypeScript file. Assignment event terminal label is now terminal-completed, distinguishing completion from later parent inspection shown in raw history. Earlier event files are preserved in native command outputs.\n\nInstalled 0.1.0 orchestration-contract path was available during initial source reads and full byte comparison, but existsSync now returns false. No package update or deletion was performed by this task. Cause is unknown. Final-source-availability.json preserves that observation. Review used the archived byte-matched source copy. No current installed-discovery claim follows.\n\nThe selected cross-review implementation does not promise synchronous disposer-scheduling failure recovery. The exact pinned vendor queues a microtask; report failures are separately covered. No new implementation change was warranted for an unrequested dependency behavior.\n\n\n## Artifacts\n\nComplete paths and SHA-256 digests: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/artifact-manifest.json. Primary receipt: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/method-receipt.json. Actual synthesis: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-02/candidate-cross-review/synthesis.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-read.txt",
      "owner": "grades-native-07.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-read.txt",
      "owner": "grades-native-07.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/cache.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/caller.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/manifest.json",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/probe.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/vendor/disposer-v1.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/vendor/disposer-v1.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/cache.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/caller.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/manifest.json",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/probe.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/baseline/vendor/disposer-v1.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/durable-02/candidate-cross-review/trials/survivor/vendor/disposer-v1.mjs",
      "owner": "grades-native-durable-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
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
