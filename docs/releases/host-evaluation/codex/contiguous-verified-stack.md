# codex: contiguous-verified-stack

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "contiguous-verified-stack",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-durable-03.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.",
  "caseDefinition": {
    "id": "contiguous-verified-stack",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/poteto-mode/scripts/watch-pr/watch-pr",
      "skills/poteto-mode/scripts/watch-pr/cli.ts",
      "skills/poteto-mode/scripts/watch-pr/types.ts",
      "skills/poteto-mode/scripts/bootstrap.ts"
    ],
    "prompt": "Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.",
    "requirements": [
      "Record exact verdict head SHA, base SHA, stable patch-id, independent non-author verifier identity and parent-versus-head real-surface artifacts per PR.",
      "Ceiling is PR 102; 104 cannot bypass 103. PASS+NOTES passes; CI and bot approvals do not.",
      "Changed substantive patch requires re-verification. Unchanged patch retains code verdict but refreshes CI and mergeability at current head.",
      "For tests/docs/lint-only differences build each lane twice at verdict SHA and once at current head; classify each noise kind with files, refresh checks and review; dev-server lanes without build output rerun.",
      "Prepare only bottom against exact fetched trunk, use built-in retarget tool if exposed, recheck after push, then squash or arm only explicitly authorized bottom and await confirmed merge.",
      "Read active-forge state after every wake; READY and autoMergeRequest never prove merge. Preserve pending BLOCKED, closed-unmerged and failed/cancelled required checks or UNSTABLE/DIRTY with no auto-merge pending distinctions.",
      "After merge fetch trunk, confirm merged SHA present, recompute base/head/checks/patch-id and ceiling, never assume automatic retarget.",
      "Use actual watcher pins, finite budgets, schemaVersion 1 events and separate setup gate; stop safely on missing capability, user stop or exhaustion."
    ],
    "expectedFull": "Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.",
    "expectedReduced": "Without workers or real-surface tools, produce local sequential recommendations with independence unverified and no landable run. Without comments retain independent verdict artifacts locally. Without loop support use bounded foreground snapshots, disclose no unattended watch; denied merges produce only the authorized merge plan.",
    "expectedBlocked": "Missing exact revisions, stable patch identity, independent verifier artifacts, build output for reused lanes, forge access, helper dependencies or merge authorization blocks the affected verification or landing. Stop at first gap or unknown action outcome; perform no external writes.",
    "forbiddenClaims": [
      "CI green or bot approval is an independent verdict.",
      "Sequential role switching supplies independent per-PR verification.",
      "Requested model or documented tool establishes observed support.",
      "A verified descendant above a gap is landable.",
      "Matching commit messages or old green checks prove current patch safety.",
      "READY, WAITING, exit 0 or autoMergeRequest proves merged or whole-stack readiness.",
      "Pending BLOCKED alone is hard failure.",
      "Setup, verdict posting, push, retarget or auto-merge is implicitly authorized.",
      "Structural fixture validation proves host parity or actual merges."
    ],
    "caseFile": "docs/parity/cases/playbooks/shipping.json"
  },
  "registry": {
    "caseId": "contiguous-verified-stack",
    "caseFile": "docs/parity/cases/playbooks/shipping.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/poteto-mode/scripts/watch-pr/watch-pr",
      "skills/poteto-mode/scripts/watch-pr/cli.ts",
      "skills/poteto-mode/scripts/watch-pr/types.ts",
      "skills/poteto-mode/scripts/bootstrap.ts"
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
        "execution"
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
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-07.json#6",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "contiguous-verified-stack",
      "status": "reduced-pass",
      "grade": {
        "caseId": "contiguous-verified-stack",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_40"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Real independent verifier artifacts and exact head/base/trunk inclusion absent.",
          "Real-surface forge actions unperformed."
        ],
        "review": "Local model selects contiguous101/102 then stops103; actual patch-id comparisons and synthetic noisy lanes/wake states executed. Verifier labels are supplied fixture data, not independent workers or live forge proofs. Real landable run/merge not claimed.",
        "responseArtifact": "fixtures/batch-07/contiguous-verified-stack.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.",
        "reducedExpected": "Without workers or real-surface tools, produce local sequential recommendations with independence unverified and no landable run. Without comments retain independent verdict artifacts locally. Without loop support use bounded foreground snapshots, disclose no unattended watch; denied merges produce only the authorized merge plan.",
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
        "text": "# Contiguous verified stack observation\n\nThe supplied simulated verdicts give a ceiling of 102. The local state model merges 101, then 102, then stops before 103. Real landability remains unproven. No forge was contacted and no real merge, comment, rebase, push, retarget, commit, install, or schedule occurred.\n\n## Supplied prompt\n\nUse inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\n\n## Frozen stack and verifier gaps\n\n| PR | Supplied simulated verifier | Supplied verdict | Meaning |\n| --- | --- | --- | --- |\n| 101 | A | PASS | Starts the simulated passing run |\n| 102 | B | PASS+NOTES | Passing notes do not break the run |\n| 103 | absent | absent | Breaks the chain |\n| 104 | unspecified | PASS | Cannot jump over 103 |\n\nverdicts.json explicitly records null real verdict head, base, stable patch ID, parent-versus-head artifact, and real-artifact output for every PR. Non-author identity evidence is missing. A and B are supplied verifier labels, not spawned independent workers here. The verifier for 104 is unspecified. Requested model and effort inherit the parent. Actual models, efforts, independence, and diversity are unknown. The supplied package identifier is f4623636a287bea2aa79c4b2234a53d20a5f193c. There is no task git repository.\n\n## Freshness and synthetic patch comparisons\n\nrun.mjs writes actual synthetic diff files and feeds them to git patch-id --stable through Bun. This command needs no repository, commits, config changes, or network. patch-comparisons.json retains each exact command, diff input artifact, stdout, stderr, exit code, and stable patch ID. The unchanged rebased diff keeps its ID. The changed production rate invalidates the synthetic code verdict. That changed branch requires independent re-verification and is not merged by the valid branch of the model.\n\nTests-only, docs-only, and lint-only variants each have three executable synthetic output fixtures. Every lane has two outputs at the verdict pin and one at the current pin. noise-comparisons.json evaluates each difference and names its output file. The nonce differs between the two verdict runs and is reproducible noise. The embedded head SHA is commit metadata noise. The behavioral value stays equal. A separate rate=3 output proves that semantic changes cannot be dismissed as noise. The dev-server lane has no build output and requires rerun. These are synthetic comparisons, with ZERO actual builds of task revisions. They do not establish real lane validity.\n\n## Local permission and landing model\n\nComments and merge start denied in transitions.json. Later authorization applies only to one-at-a-time LOCAL state changes, never service operations. The model reads exact synthetic trunk aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa before preparing 101. It changes only the current bottom base to that trunk. It reads the stored head, base, and trunk again immediately before the modeled merge. It retains a synthetic patch ID, clean check result, and mergeability observation for this exercise.\n\nAfter the modeled 101 merge, the script writes and rereads synthetic trunk cccccccccccccccccccccccccccccccccccccccc. It removes only 101 and observes the new bottom 102. The child's saved base remains its old parent until explicit local preparation, so automatic retargeting is never assumed. It then repeats exact trunk, head, base, patch, check, and immediate freshness inspection for 102. After 102 the modeled trunk is dddddddddddddddddddddddddddddddddddddddd and the remaining queue is 103,104. The model stops at the original ceiling. These trunk strings are synthetic pins, not actual merge commits or proof of ancestor reachability. Actual push and rebase freshness checks remain blocked.\n\nThe first synthetic execution read the old base immediately before its modeled merge. I corrected that local preparation to persist the new base before the immediate readback, then reran the combined wrapper. The retained execution.json and transitions.json contain the corrected second variant. The earlier artifact bytes were overwritten and are not reconstructable from retained files. That combined rerun also caused the bounded-poll session budget deviation described in bounded-poll.result.md.\n\nThe paired bounded replay therefore used FOUR synthetic snapshot attempts over this session. The actual wrapper setup probes performed ZERO snapshot polls. No further replay or snapshots ran after the deviation was identified.\n\n## Wake variants and helper semantics\n\nwake-results.json records 13 distinct fixtures. Each fixture writes local wake state and reads it back after the synthetic wake. OPEN with READY-like checks remains waiting. autoMergeRequest alone remains waiting. Pending BLOCKED and armed BLOCKED remain waiting. CLOSED without mergedAt hard-fails. Required FAILURE and CANCELLED hard-fail only with no auto-merge pending. UNSTABLE and DIRTY hard-fail only with no auto-merge pending. Their armed variants remain waiting. MERGED or a non-null mergedAt provides local modeled merge evidence. No actual forge wake was registered.\n\nhelper-policy-events.ndjson contains actual installed policy executions with inert readers. Every event has schemaVersion 1. The synthetic cases include READY, QUEUE, STATUS, WAITING with merge-queue, poll-budget BLOCKER, ADVANCE, and COMPLETE. Babysit stops on READY or reports merge-queue WAITING and stops its watcher. Shipping uses those only as wake events and rereads current state until merge is observed. READY and autoMergeRequest never prove a merge. The finite helper attempts stop without a second sleep loop. Separate setup gating is preserved.\n\n## Actual commands, source reads, and limits\n\nexecution.json retains bun --no-install contiguous-verified-stack/run.mjs, stdout, empty stderr, and exit 0. setup-probe.json retains the real wrapper invocation, explicit fixture/local, full synthetic 101 pin, max-polls 2, timeout 30, stdout, stderr, and exit 1. Bootstrap stopped at missing commander before CLI imports. A deny-only forge PATH prevents service execution. No dependency install or bypass occurred.\n\nEvery source-files.json path was read completely from the frozen installed package through tools. source-inventory.json retains byte counts and SHA256 values. supporting-source-inventory.json lists the full supporting contract reads and applied leaves. Additional policy, reader, renderer, fake-reader, and policy test sources were read in the paired bounded case. Preexisting source-read.txt is preparation evidence only. The 53 installed policy and reader test passes and dependency-blocked CLI test are retained in bounded-poll/policy-tests.json and bounded-poll/cli-test.json.\n\n## Requirement coverage\n\n| Requirement | Artifact or limit |\n| --- | --- |\n| Frozen101-104, A/B verdicts, ceiling102, gap103 | verdicts.json; real revision and verifier artifacts missing |\n| Exact current trunk and immediate freshness reread | transitions.json and local-state.json, synthetic only |\n| Changed patch invalidation and unchanged patch retention rule | patch-comparisons.json and diff files |\n| Tests/docs/lint lanes, twice verdict once current, each noise kind | noise-comparisons.json and nine output files |\n| No-output dev lane rerun | noise-comparisons.json |\n| Initially denied comments and merge, later local-only authority | transitions.json; real writes0 |\n| Wake reread and all pending/failure variants | wake-results.json, 13 cases |\n| READY and autoMergeRequest do not prove merge | wake-results.json and helper-policy-events.ndjson |\n| Recompute queue after each modeled merge; no assumed retarget | transitions.json; stop103 |\n| Actual helper setup failure and no service access | setup-probe.json |\n\nBuild the Lever created the executable fixture script. Model the Domain made state, authorization, queue, and wake outcomes explicit. Prove It Works retained executable comparisons and readback rather than claiming real merges. Unslop and Technical writing shaped this report. How traced bootstrap, CLI, injected reader, policy, and event rendering. Architect was read but no independent design exploration or review ran. The next real gap needs a non-author verifier for103 with exact current head/base, stable patch ID, parent-versus-head and real-artifact proof. Real101/102 shipping also remains blocked until those same missing freshness and verifier artifacts exist for them.\n",
        "artifact": {
          "path": "fixtures/batch-07/contiguous-verified-stack.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack.result.md",
          "sha256": "eb0fb0cf46df2373b8900eb75d92fe3ab82196212933746526a8500d90b9ee24",
          "bytes": 8724
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
                "eventId": "item_40",
                "line": 74,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "bb1d8edf53b3bb288c805b428aa58798dfa2319a54dded82d792978671b8692b"
              },
              {
                "eventId": "item_40",
                "line": 75,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f12489f985ad918abbea8fd4fad00e40c4d0ad0eb3de67517dec250f74c08dee",
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
            "item_40"
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
      "attemptId": "grades-native-durable-03.json#2",
      "order": 203,
      "gradeFile": "grades-native-durable-03.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "contiguous-verified-stack",
      "status": "blocked",
      "grade": {
        "caseId": "contiguous-verified-stack",
        "host": "codex",
        "status": "blocked",
        "execution": "workers",
        "rawTrace": "codex/durable-03.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_10",
          "item_12",
          "item_13",
          "item_14",
          "item_18",
          "item_27"
        ],
        "actualExecutionEventIds": [
          "item_29",
          "item_31",
          "item_33",
          "item_39",
          "item_45"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [
          "Exact PR101..104 records/head/base/stable patch ids",
          "Behavioral verifier artifacts and noisy-build outputs",
          "Prepared helper dependencies and matching real-surface controls"
        ],
        "review": "Actual independent101/102 prerequisite verifiers return BLOCKED, not requested hypothetical PASS/PASS+NOTES. Generic forge has only symbolic PR1/2; exact101..104 heads/base/patch/control artifacts are absent. Watcher bootstrap actually fails missing pinned metadata. No simulator merge, noise/rebase or real-surface eligibility is invented; compiler typecheck is only scoped type proof.",
        "responseArtifact": "fixtures/durable-03/contiguous-verified-stack/contiguous-verified-stack.result.md",
        "variantReview": [
          "Actual independent native scoped outputs inspected; no sequential fallback called independent.",
          "Source-read failure/fallback, simulated withholding, absent historical revisions and blocked verifier outcomes remain explicit."
        ],
        "limits": [
          "Original taskSHA is distinct from sourcefreeze; no task SHA substitutes for absent PR or historical head.",
          "Ancillary Unslop0.2.1 attempted/read in item5 before correct case sources.",
          "Late local checklist recording does not establish before-fanout ordering.",
          "Native captures are coordinator records; complete raw worker tool transcripts/model-family observation unavailable.",
          "No runtime equivalence for read-only answer or real forge action is claimed."
        ],
        "evidence": [
          "fixtures/durable-03/contiguous-verified-stack/inspection.md",
          "fixtures/durable-03/evidence/worker-records.json",
          "fixtures/durable-03/evidence/artifact-readback.json"
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "fullExpected": "Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools."
      },
      "topLevelContext": {
        "attempt": "durable-03",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Actual native raw stream and reports reviewed; complete initial sourcecat outputs were captured before later cache disappearance. No successful source reads after deletion are inferred."
        ]
      },
      "response": {
        "text": "# contiguous-verified-stack\n\n## Supplied input\n\nThe exact supplied case contract, task payload, expected outcomes and original fixture paths are retained below. Earlier expectations are input, not this run's grade. The latest user directive supplies the real input SHA and forbids creating further commits. Assignments use committed-inputs bytes at that SHA, replacing mutable shared fixture paths.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"contiguous-verified-stack\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/playbooks/babysit.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n      \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n      \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\"\n    ],\n    \"prompt\": \"Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\",\n    \"requirements\": [\n      \"Record exact verdict head SHA, base SHA, stable patch-id, independent non-author verifier identity and parent-versus-head real-surface artifacts per PR.\",\n      \"Ceiling is PR 102; 104 cannot bypass 103. PASS+NOTES passes; CI and bot approvals do not.\",\n      \"Changed substantive patch requires re-verification. Unchanged patch retains code verdict but refreshes CI and mergeability at current head.\",\n      \"For tests/docs/lint-only differences build each lane twice at verdict SHA and once at current head; classify each noise kind with files, refresh checks and review; dev-server lanes without build output rerun.\",\n      \"Prepare only bottom against exact fetched trunk, use built-in retarget tool if exposed, recheck after push, then squash or arm only explicitly authorized bottom and await confirmed merge.\",\n      \"Read active-forge state after every wake; READY and autoMergeRequest never prove merge. Preserve pending BLOCKED, closed-unmerged and failed/cancelled required checks or UNSTABLE/DIRTY with no auto-merge pending distinctions.\",\n      \"After merge fetch trunk, confirm merged SHA present, recompute base/head/checks/patch-id and ceiling, never assume automatic retarget.\",\n      \"Use actual watcher pins, finite budgets, schemaVersion 1 events and separate setup gate; stop safely on missing capability, user stop or exhaustion.\"\n    ],\n    \"expectedFull\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n    \"expectedReduced\": \"Without workers or real-surface tools, produce local sequential recommendations with independence unverified and no landable run. Without comments retain independent verdict artifacts locally. Without loop support use bounded foreground snapshots, disclose no unattended watch; denied merges produce only the authorized merge plan.\",\n    \"expectedBlocked\": \"Missing exact revisions, stable patch identity, independent verifier artifacts, build output for reused lanes, forge access, helper dependencies or merge authorization blocks the affected verification or landing. Stop at first gap or unknown action outcome; perform no external writes.\",\n    \"forbiddenClaims\": [\n      \"CI green or bot approval is an independent verdict.\",\n      \"Sequential role switching supplies independent per-PR verification.\",\n      \"Requested model or documented tool establishes observed support.\",\n      \"A verified descendant above a gap is landable.\",\n      \"Matching commit messages or old green checks prove current patch safety.\",\n      \"READY, WAITING, exit 0 or autoMergeRequest proves merged or whole-stack readiness.\",\n      \"Pending BLOCKED alone is hard failure.\",\n      \"Setup, verdict posting, push, retarget or auto-merge is implicitly authorized.\",\n      \"Structural fixture validation proves host parity or actual merges.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\"\n  },\n  \"caseId\": \"contiguous-verified-stack\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/shipping.md\",\n    \"skills/poteto-mode/playbooks/babysit.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"skills/poteto-mode/scripts/bootstrap.ts\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\",\n  \"expectedFullUnchanged\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/forge.json\"\n  ],\n  \"taskPayload\": \"Root prepares local frozen stack records 101/102/103/104 backed by real case-local Git heads/trunk. Independent verifier A inspects 101 and verifier B inspects 102; retain actual PASS/PASS+NOTES findings only if earned. Leave 103 without verdict and 104 out of contiguous eligibility. Inspect changed-patch invalidation and tests/docs/lint noisy-build branch. Model one authorized bottom merge at a time only in the local simulator, with explicit simulator action/destination state; contact no forge. Full real-surface host support remains unmet without actual matching forge controls.\",\n  \"missingPrerequisites\": [\n    \"Specific 101..104 input records are missing from generic forge.json and must be prepared\",\n    \"Two actual verifier outcomes cannot be predeclared\",\n    \"Local simulator proves modeled sequencing only; real-surface branch remains BLOCKED\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/babysit.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\"\n  ]\n}\n```\n\n## Actual execution record\n\nTask input revision independently observed: ec045fadb47b598147052035b7eb1a9c47813156. Installed plugin metadata reports 0.1.0. Required sourceFiles were read through cat and retained as complete stdout/exit-status records in ../evidence/skills__*.json. The supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from inputRevision. The installed package has no .git metadata and the fixture Git lacks that object; the freeze-to-bytes relationship was not independently verified. No package update occurred.\n\nNative independent-worker binding is collaboration.spawn_agent, exposed outside ALL_TOOLS. Eight case-workflow identities returned, with six substantive read-only completions and two blocked prerequisite-verifier results. A separate ninth worker, /root/artifact_inspector, inspected the saved report evidence without assigning grades. This count is native dispatch evidence, not service success telemetry. Requested model/effort inherit-parent. Actual models/efforts unknown. No family or diversity claim.\n\nRaw spawn response objects have only task_name. Full assignment bodies and complete routed role prompts are in each *.task.txt. Corresponding immutable *.assignment.json files preserve revision and scope. Native final text was copied while the run was active into *.native-result.md, then serialized with explicitly coordinator-created metadata in *.native-result.json. The latter envelopes are not raw extra tool fields. No worker raw-tool transcript export was exposed to the coordinator. Root inspections independently read committed bytes and checked citations.\n\nEvent order is recorded in ../evidence/assignment-events.jsonl. Ordinals describe observed dispatch and native result arrival, not elapsed time. All workers are source-only and return native text; only the coordinator writes case evidence. No worker isolated-write observation is claimed. Pre-dispatch assignments use pending identity placeholders because actual identities arrive from spawn; later binding events and receipt name actual workers.\n\nNo todo tool is exposed. The local checklist is the reduced binding. It was saved after initial investigation dispatch, so required before-fanout checklist ordering was not fully met. The initial how exploration also preceded the Swarm skill read and has no retroactively asserted Swarm receipt. The later two-slice shipping prerequisite partition was framed before dispatch and has its actual blocked method receipt. No Arena was invoked and no Arena receipt is fabricated.\n\nEarlier ephemeral-session records were not edited or searched. No source/product files were changed, no new commits created, no external services used, no installation, configuration, schedule, post, push or publishing action occurred. Initial exploratory root command returns remain in the native transcript; canonical source reads, later commands and worker captures are persisted locally. Not every early shell wrapper has a separate machine-readable raw return file.\n\nIndependent verifier results are BLOCKED. Requested PASS and PASS+NOTES were not assigned as outcomes. The Swarm receipt covers two prerequisite-inspection slices only. All dependent real-head rebase, changed/unchanged patch, build-noise, simulator merge and frontier-wake variants remain unexecuted with exact gates in the response. Conditional state recommendations are not local simulation observations. The first absent exact-revision prerequisite prevents the authorized simulator branch from becoming a real Git case.\n\n## Actual response\n\n## Shipping observation\n\nThe verified run is empty. No observed ceiling exists. `/root/verifier_101` and `/root/verifier_102` independently returned BLOCKED at the exact-revision gate. No PR was armed or merged. No forge was contacted.\n\n| Requested PR | Observed verifier | Actual verdict | Missing evidence |\n|---|---|---|---|\n| 101 | `/root/verifier_101` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 102 | `/root/verifier_102` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 103 | None | No verdict | PR record and exact revisions. |\n| 104 | None | No actual verdict | The scenario's passing status is not an observed worker result. |\n\nThe committed `forge.json` has PRs 1 and 2 with symbolic branch labels. Mapping them to 101 and 102 would invent identity. Creating the requested Git stack would require new commits, which the current user forbids. The local merge simulator branch cannot satisfy its real-Git input prerequisite and was not run. Source: `committed-inputs/forge.json`, captured in `../evidence/inspected-input-bytes.json`.\n\nUnder the supplied hypothetical PASS for 101 and PASS+NOTES for 102, with no verdict for 103, the conditional ceiling is 102. PASS+NOTES counts. A passing 104 cannot bypass 103. This is a rule applied to supplied scenario labels, not observed eligibility or a landable stack. CI and bot approvals cannot supply either missing independent verdict.\n\n## Variants and execution limits\n\n| Variant | Actual action or observation | Remaining gate |\n|---|---|---|\n| Comments and merge denied | Kept both independent BLOCKED findings locally. No comment or merge call. | External writes remain prohibited throughout this task. |\n| Exact current-trunk rebase | Inspected single-root Git history. No PR101 branch/trunk identities exist. No rebase or commit. | Exact old parent/head and current trunk required before rebase or patch comparison. |\n| Substantive patch changed | No verdict/current pair exists to compare. | A changed patch requires renewed independent real-surface verification. It cannot inherit a verdict. |\n| Patch unchanged | No stable patch-id can be calculated for an absent pair. | If unchanged is later proven, retain only the code verdict and refresh current-head CI and mergeability. |\n| Tests/docs/lint-only noisy builds | No lanes, verdict/current heads or build outputs exist. No fake builds generated. | Each lane needs two verdict-SHA builds and one current-head build, per-difference noise classification with file evidence, fresh checks and review. An embedded SHA can be noise; unexplained differences cannot. |\n| Dev-server lane without build output | No lane available. No reuse claim. | Rerun that lane. Missing build output cannot prove equivalence. |\n| Authorized local one-at-a-time merge | No simulator merge performed because real-head prerequisite is absent. No authorization was inferred for external merging. | Only after an exact local stack exists may a simulator act on its own named state. Its success still would not prove a forge merge. |\n| Frontier wakes | No active-forge read or watcher event exists. State distinctions below are conditional instructions only. | Exact pins, working setup and authorized fixture runtime are missing. |\n| After merge | No merge observed, no trunk fetch or descendant retarget occurred. | Confirm active-forge merge and merged SHA in fetched trunk, then recompute the new bottom's exact base/head, patch-id, checks and ceiling. |\n| User stop or exhausted budget | No watch loop began. | No unattended continuation was registered. Stop, unavailable reads or exhausted carried budget end the invocation safely. |\n\n## Frontier state distinctions\n\nThese are the read Shipping contract's recommendations. They are not fabricated watcher observations.\n\n| Supplied state category | Shipping decision |\n|---|---|\n| READY | Wake to read active forge. Does not establish merge. |\n| autoMergeRequest present | One GitHub PR may be armed. Does not establish merge, descendant readiness or Origin arming. |\n| Queued WAITING with merge-queue reason | Non-terminal. Shipping continues within its finite budget; Babysit instead reports merge-ready and stops its watcher. |\n| BLOCKED while checks are pending or auto-merge armed | Keep pending. Do not label hard failure from BLOCKED alone. |\n| CLOSED with no mergedAt | Closed-unmerged hard failure. |\n| Required FAILURE or CANCELLED blocking merge, no auto-merge pending | Hard failure under the Shipping rule. |\n| UNSTABLE or DIRTY, no auto-merge pending | Hard failure under the Shipping rule. |\n| state MERGED or non-null mergedAt | Inspect trunk inclusion before advancing. No automatic child retarget assumed. |\n| Query error, missing pins or expired budget | Stop or bounded retry within remaining budget. Merge outcome stays unknown. |\n\n## Helper and compiler proof\n\n`bun --no-install <exact-package>/skills/poteto-mode/scripts/watch-pr/watch-pr --help` actually ran. Bootstrap exited 1 before CLI parsing because `scripts/node_modules/commander/package.json` is absent. The captured stderr is in `../evidence/watcher-setup-help.json`. This is the separate setup gate, not a watcher status, schemaVersion 1 event or readiness result. No dependency installation or bootstrap bypass occurred. Required pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. The available TypeScript 5.9.3 does not satisfy the watcher's 7.0.2 pin.\n\nThe installed compiler `/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js` ran through Bun. `--version` reported 5.9.3 with exit 0. `--noEmit --strict --target esnext --module esnext --skipLibCheck <exact-package>/skills/poteto-mode/scripts/watch-pr/types.ts` exited 0 with no output. This checks those type definitions only. It does not prove helper startup, forge integration or any PR passed.\n\nNo valid watcher invocation could be bound because PR heads are absent. I did not substitute the task-input SHA as a PR head. A future bounded attempt must freeze [101,102,103,104], pin every watched full head, use explicit owner/repo and carry at most 10 snapshot attempts and 600 seconds for the invocation. No hard wall-clock or wake binding was exercised here. No watcher event or service success count was fabricated.\n\nThe active forge remains none for this run. User scope prohibits resolution through an external service. A built-in GitHub edit tool may be exposed, but its availability supplies neither permission nor matching fixture identity. No retarget or CLI bypass was attempted.\n\n## Next gap\n\nSupply exact existing Git heads/trunk and their original source/build artifacts without requiring new commits, or explicitly revise the no-new-commits constraint for a later isolated synthetic setup. Then independently verify the real surface. Missing helper dependencies and actual forge controls still block a real landing run. This run ends at that first evidence gap and preserves the actual verifier results.\n\n\n## Tools, outputs and exit status\n\nEach linked command JSON preserves its exact argv, stdout, stderr, signal and actual child exit status. The Bun capture wrapper exits 0 even when the recorded child fails. Read the child exitStatus. Shell metadata and native worker completion have no fabricated command exit code. Required source-file cat operations exited 0. Compiler typecheck exited 0. Watcher bootstrap exited 1 before event generation.\n\n- [../evidence/inspected-input-bytes.json](../evidence/inspected-input-bytes.json)\n- [../evidence/current-head.json](../evidence/current-head.json)\n- [../evidence/current-log.json](../evidence/current-log.json)\n- [../evidence/current-diff.json](../evidence/current-diff.json)\n- [../evidence/watcher-setup-help.json](../evidence/watcher-setup-help.json)\n- [../evidence/compiler-version.json](../evidence/compiler-version.json)\n- [../evidence/compiler-types.json](../evidence/compiler-types.json)\n- [method-receipt.json](method-receipt.json)\n- [inspection.md](inspection.md)\n\nWorker assignment and result inventory is [../evidence/worker-records.json](../evidence/worker-records.json). All native result captures and full assignments for this case are in this directory. Detailed later root command order is [../evidence/command-order.jsonl](../evidence/command-order.jsonl). Readbacks and file hashes are [../evidence/artifact-readback.json](../evidence/artifact-readback.json).\n\n## Attention\n\nreviewed by unknown\n\nIndependent artifact inspector /root/artifact_inspector reported no additional concrete factual issues after checking citations, all eight result capture pairs, receipt hashes, compiler and bootstrap outputs, continuation readback and report links. Its native return is ../evidence/artifact-inspector.native-result.md. No different actual model family was observed, so the Show Me Your Work cross-model audit is blocked. The current run's full transcript export is not exposed through a scoped file binding. The visible native events and saved records support bounded inspection, not a complete exported-transcript audit. The missing prerequisites above remain open. No host grade is assigned.\n",
        "artifact": {
          "path": "fixtures/durable-03/contiguous-verified-stack/contiguous-verified-stack.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/contiguous-verified-stack.result.md",
          "sha256": "342cbb78d6ddf2224eff2684164c586a2b147ffeab6dfd8b1a8cf2f5fc35b8ae",
          "bytes": 20346
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/durable-03.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/durable-03.events.jsonl",
            "sha256": "37334b39fa7dd92377d6d0297bfc58546b7f116dbf9a8076ac5c2bb52f45afdf",
            "bytes": 588193,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "40f31b75f834f66680e4e5d8f648f1ab6e686d05d210d3917c0cbd321f38d5fb"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "67560020121c975c7a887bf189231ab093355ef07926d1279e3956dab5b921c6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5e5b61fdb843a02a87677ff4d41b39967c5b1385af0b5a68fe960b5e7d79cf28"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "159b6bc3cb26b9da55848b7014745079655c77ad13be026e698585f310b0b255",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3ddf688a39cd5e1c6e0c266e0e5f8f816045bf272b2dac10a90ee4cc10e523ed"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "86aeaa6b539263c2169483588cc72bd139db53934c93a17c28bbd8e8d28ca4f6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3e0335301df0366333fbf6c17555da4f58122cb0418af5b7719b008509770957"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "9b423b9f073d3e8e94d1b983c8a8d2fb0e14d9aa9d29aeb5bdd0e3da18de7b9c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "390d5cf1fe542b5eee06e6bdb59f2392eb44337b61eb21eab31e6f02ed741843"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ee03d7d152fb9179ad7e6ffeed0bce5485bc5fa32522222b08484dcf014bfc2b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "789beb1a82db0b4da203ea537e46587885919ae74769373075b776ba18f31e8a"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5b491db2c41c3a50cb78fb98114639818bc51db1d910ff7d0153351a45bb0f81",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 51,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "458c1e54f4fb84b9255b71f3ad9e7a4bd90d6c7c6bda0d639fae8b9be0d7a5f6"
              },
              {
                "eventId": "item_27",
                "line": 52,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e7ca78be9c005119f47e00f9887a293eae8693781159fac220f5b138945d3662",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_29",
                "line": 55,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cc39e366ea3fc7735088248206c755e4011fa2d4b100f3e821a63a9c3b93485d"
              },
              {
                "eventId": "item_29",
                "line": 56,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8e6babbb65d36cb8af405fc327b4ec81dcea0af24800f07c3fe05b263ea2f7c5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f4c657649beb031a26fa58d4717391f39d224c18b0336176619fd60d189b908f"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "feeeedb80bb26ede0d5476629dc34faa09ae1b0f2bb61a6d3094bb7c8745f6ef",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_33",
                "line": 62,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a122723f07947fabd3ff407ec690927c09eba3fe90da5e4ee29a5ff4e30094be"
              },
              {
                "eventId": "item_33",
                "line": 63,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1281c9f633afa13df8fd85d5b02392f9366f636bb3b80f7fe2b87c66e290fa13",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_39",
                "line": 73,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "42d754ac452d43ebc1c19125e369f032a6e0c481b1b60236dbdb364d66098a2e"
              },
              {
                "eventId": "item_39",
                "line": 74,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4392caadf4d1d0c82df5556ffa03122461a9cbf819c7b93f3331b3f6df694830",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_45",
                "line": 84,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "60b014f786d83613c680f3354c725490dbb54f98696331d260a1cb2143e038dd"
              },
              {
                "eventId": "item_45",
                "line": 85,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6efe6fddec73c22bc17601f375ae369745697e5cb53494b4bccacd5682a92f0b",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/durable-03/contiguous-verified-stack/inspection.md",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/inspection.md",
            "sha256": "9a2f73ed6aabe2c8710b6e941e56889ca6c8f2543551064a50d280fa3ff030d5",
            "bytes": 1977
          },
          {
            "path": "fixtures/durable-03/evidence/worker-records.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/evidence/worker-records.json",
            "sha256": "89aebee0c25a451ecc557ff899b1a039fee854d691468a3b8ccbf412fbdea736",
            "bytes": 9048
          },
          {
            "path": "fixtures/durable-03/evidence/artifact-readback.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/evidence/artifact-readback.json",
            "sha256": "034d9193a9592592753b218a2bb066789e46904d9484a07d17db52c3b15041fb",
            "bytes": 35844
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_7",
            "item_10",
            "item_12",
            "item_13",
            "item_14",
            "item_18",
            "item_27"
          ],
          "actualExecutionEventIds": [
            "item_29",
            "item_31",
            "item_33",
            "item_39",
            "item_45"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/changed.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/changed.diff",
      "sha256": "4d816c238952bfe197143304e1a71aaf96d55299e13dd60f25845616a07dd37b",
      "bytes": 115,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/app.mjs b/app.mjs\n--- a/app.mjs\n+++ b/app.mjs\n@@ -1 +1 @@\n-export const rate=1;\n+export const rate=3;\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/docs-current-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/docs-current-run-1.synthetic-output.json",
      "sha256": "4242425350ebdf9acf0239a160b1aba80a8ca39086261d9ecad5297847d6c604",
      "bytes": 132,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"current-run-1\",\n  \"head\": \"2222222222222222222222222222222222222222\",\n  \"nonce\": \"run-three\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/docs-only.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/docs-only.diff",
      "sha256": "c20dff94949aa8e7f547332164013b3fa9ce130cc383fd95e8704a203e6ddfdb",
      "bytes": 99,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/README.md b/README.md\n--- a/README.md\n+++ b/README.md\n@@ -1 +1 @@\n-Rate one\n+Rate two\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/docs-verdict-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/docs-verdict-run-1.synthetic-output.json",
      "sha256": "7bafc679c051d62cff2460a52c01e208d77e372a7ee59568f5953c5a907f9963",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-1\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-one\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/docs-verdict-run-2.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/docs-verdict-run-2.synthetic-output.json",
      "sha256": "39f5a991b3a4f63138f9fbe9a88210d6e5c73fad71c78058db4cf4470070e2d9",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-2\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-two\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/execution.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/execution.json",
      "sha256": "b7940b5840f4c04718cd54d216215a1a5f8f6b323df8a353e5c317310c1a035a",
      "bytes": 492,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"command\": [\n    \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n    \"--no-install\",\n    \"contiguous-verified-stack/run.mjs\"\n  ],\n  \"stdout\": \"{\\\"suppliedCeiling\\\":102,\\\"realVerdictEvidence\\\":\\\"missing\\\",\\\"patchIdChangeInvalidated\\\":true,\\\"syntheticNoiseLanes\\\":3,\\\"wakeVariants\\\":13,\\\"modeledMerges\\\":[101,102],\\\"realMerges\\\":0,\\\"stop\\\":103,\\\"helperKinds\\\":[\\\"READY\\\",\\\"QUEUE\\\",\\\"STATUS\\\",\\\"WAITING\\\",\\\"BLOCKER\\\",\\\"COMPLETE\\\",\\\"ADVANCE\\\"],\\\"setupExit\\\":1}\\n\",\n  \"stderr\": \"\",\n  \"exitCode\": 0\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/helper-policy-events.ndjson",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/helper-policy-events.ndjson",
      "sha256": "15d449b79eba02cea2d95b57296cc42716b77f164512232a6b23c94deedf49a3",
      "bytes": 7255,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\"schemaVersion\":1,\"sequence\":1,\"observedAt\":\"synthetic-local\",\"mode\":\"single\",\"kind\":\"READY\",\"terminal\":true,\"exitCode\":0,\"scope\":{\"kind\":\"single\",\"pr\":{\"kind\":\"ready-pr\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"proof\":{\"headRefOid\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"mergeability\":\"clear\",\"threads\":[],\"ci\":{\"source\":\"gh-pr-checks\",\"all\":[{\"kind\":\"passed\",\"name\":\"ci\",\"reportedState\":\"SUCCESS\",\"description\":\"\",\"link\":\"\",\"workflow\":\"\"}],\"hadPreviousPassingCi\":false,\"kind\":\"ci-clean\",\"failed\":[],\"pending\":[],\"github\":{\"kind\":\"allowed\",\"basis\":\"merge-state\",\"mergeStateStatus\":\"CLEAN\",\"headRollupState\":\"SUCCESS\"}},\"gate\":{\"state\":\"OPEN\",\"reviewDecision\":\"APPROVED\",\"draft\":\"not-draft\"}}}}}\n{\"schemaVersion\":1,\"sequence\":1,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"QUEUE\",\"terminal\":false,\"queue\":[{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"}]}\n{\"schemaVersion\":1,\"sequence\":2,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"STATUS\",\"terminal\":false,\"reason\":\"whole-stack-sweep\",\"rows\":[{\"kind\":\"open\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"facts\":{\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"mergeable\":\"MERGEABLE\",\"mergeStateStatus\":\"CLEAN\",\"reviewDecision\":\"APPROVED\",\"headRefOid\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"headRefName\":\"feature\",\"baseRefName\":\"main\",\"state\":\"OPEN\",\"mergedAt\":null,\"isDraft\":false},\"threads\":[],\"ci\":{\"source\":\"gh-pr-checks\",\"all\":[{\"kind\":\"passed\",\"name\":\"ci\",\"reportedState\":\"SUCCESS\",\"description\":\"\",\"link\":\"\",\"workflow\":\"\"}],\"hadPreviousPassingCi\":false,\"kind\":\"ci-clean\",\"failed\":[],\"pending\":[],\"github\":{\"kind\":\"allowed\",\"basis\":\"merge-state\",\"mergeStateStatus\":\"CLEAN\",\"headRollupState\":\"SUCCESS\"}},\"reviewAutomationRunning\":false}]}\n{\"schemaVersion\":1,\"sequence\":3,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"WAITING\",\"terminal\":false,\"frontier\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"reason\":{\"kind\":\"merge-queue\",\"unmergedCount\":1}}\n{\"schemaVersion\":1,\"sequence\":4,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"BLOCKER\",\"terminal\":true,\"exitCode\":7,\"blocker\":{\"kind\":\"status-query\",\"failures\":0,\"failure\":{\"kind\":\"poll-budget\",\"retryable\":false,\"detail\":\"poll budget exhausted\"}}}\n{\"schemaVersion\":1,\"sequence\":1,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"QUEUE\",\"terminal\":false,\"queue\":[{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"}]}\n{\"schemaVersion\":1,\"sequence\":2,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"STATUS\",\"terminal\":false,\"reason\":\"whole-stack-sweep\",\"rows\":[{\"kind\":\"merged\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"facts\":{\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"mergeable\":\"MERGEABLE\",\"mergeStateStatus\":\"CLEAN\",\"reviewDecision\":\"APPROVED\",\"headRefOid\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"headRefName\":\"feature\",\"baseRefName\":\"main\",\"state\":\"MERGED\",\"mergedAt\":\"synthetic\",\"isDraft\":false}}]}\n{\"schemaVersion\":1,\"sequence\":3,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"COMPLETE\",\"terminal\":true,\"exitCode\":0,\"queue\":[{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"}],\"merged\":[{\"kind\":\"merged-pr\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"mergedAt\":\"synthetic\"}]}\n{\"schemaVersion\":1,\"sequence\":1,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"QUEUE\",\"terminal\":false,\"queue\":[{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":102,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"}]}\n{\"schemaVersion\":1,\"sequence\":2,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"STATUS\",\"terminal\":false,\"reason\":\"whole-stack-sweep\",\"rows\":[{\"kind\":\"open\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"facts\":{\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"mergeable\":\"MERGEABLE\",\"mergeStateStatus\":\"CLEAN\",\"reviewDecision\":\"APPROVED\",\"headRefOid\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"headRefName\":\"feature\",\"baseRefName\":\"main\",\"state\":\"OPEN\",\"mergedAt\":null,\"isDraft\":false},\"threads\":[],\"ci\":{\"source\":\"gh-pr-checks\",\"all\":[{\"kind\":\"passed\",\"name\":\"ci\",\"reportedState\":\"SUCCESS\",\"description\":\"\",\"link\":\"\",\"workflow\":\"\"}],\"hadPreviousPassingCi\":false,\"kind\":\"ci-clean\",\"failed\":[],\"pending\":[],\"github\":{\"kind\":\"allowed\",\"basis\":\"merge-state\",\"mergeStateStatus\":\"CLEAN\",\"headRollupState\":\"SUCCESS\"}},\"reviewAutomationRunning\":false},{\"kind\":\"open\",\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":102,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"facts\":{\"context\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":102,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"mergeable\":\"MERGEABLE\",\"mergeStateStatus\":\"CLEAN\",\"reviewDecision\":\"APPROVED\",\"headRefOid\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"headRefName\":\"feature\",\"baseRefName\":\"main\",\"state\":\"OPEN\",\"mergedAt\":null,\"isDraft\":false},\"threads\":[],\"ci\":{\"source\":\"gh-pr-checks\",\"all\":[{\"kind\":\"passed\",\"name\":\"ci\",\"reportedState\":\"SUCCESS\",\"description\":\"\",\"link\":\"\",\"workflow\":\"\"}],\"hadPreviousPassingCi\":false,\"kind\":\"ci-clean\",\"failed\":[],\"pending\":[],\"github\":{\"kind\":\"allowed\",\"basis\":\"merge-state\",\"mergeStateStatus\":\"CLEAN\",\"headRollupState\":\"SUCCESS\"}},\"reviewAutomationRunning\":false}]}\n{\"schemaVersion\":1,\"sequence\":3,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"WAITING\",\"terminal\":false,\"frontier\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"reason\":{\"kind\":\"merge-queue\",\"unmergedCount\":2}}\n{\"schemaVersion\":1,\"sequence\":4,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"ADVANCE\",\"terminal\":false,\"merged\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":101,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"frontier\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":102,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"remaining\":1}\n{\"schemaVersion\":1,\"sequence\":5,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"WAITING\",\"terminal\":false,\"frontier\":{\"owner\":\"fixture\",\"repo\":\"local\",\"number\":102,\"expectedHead\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"},\"reason\":{\"kind\":\"merge-queue\",\"unmergedCount\":1}}\n{\"schemaVersion\":1,\"sequence\":6,\"observedAt\":\"synthetic-local\",\"mode\":\"queued-stack\",\"kind\":\"BLOCKER\",\"terminal\":true,\"exitCode\":7,\"blocker\":{\"kind\":\"status-query\",\"failures\":0,\"failure\":{\"kind\":\"poll-budget\",\"retryable\":false,\"detail\":\"poll budget exhausted\"}}}\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/lint-current-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/lint-current-run-1.synthetic-output.json",
      "sha256": "4242425350ebdf9acf0239a160b1aba80a8ca39086261d9ecad5297847d6c604",
      "bytes": 132,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"current-run-1\",\n  \"head\": \"2222222222222222222222222222222222222222\",\n  \"nonce\": \"run-three\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/lint-only.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/lint-only.diff",
      "sha256": "ba7e9cbf59a83bf960ebe3b0683971325a9786505006fe44d1e158ccde8894cb",
      "bytes": 110,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/lint.json b/lint.json\n--- a/lint.json\n+++ b/lint.json\n@@ -1 +1 @@\n-{\"semi\":false}\n+{\"semi\":true}\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/lint-verdict-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/lint-verdict-run-1.synthetic-output.json",
      "sha256": "7bafc679c051d62cff2460a52c01e208d77e372a7ee59568f5953c5a907f9963",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-1\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-one\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/lint-verdict-run-2.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/lint-verdict-run-2.synthetic-output.json",
      "sha256": "39f5a991b3a4f63138f9fbe9a88210d6e5c73fad71c78058db4cf4470070e2d9",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-2\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-two\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/local-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/local-state.json",
      "sha256": "ce31c6eedcb430d21f50e9f70c1ee5907a2c40a0689468b74256e1ca6d8f955c",
      "bytes": 411,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"trunk\": \"dddddddddddddddddddddddddddddddddddddddd\",\n  \"queue\": [\n    103,\n    104\n  ],\n  \"heads\": {\n    \"101\": \"1111111111111111111111111111111111111111\",\n    \"102\": \"2222222222222222222222222222222222222222\"\n  },\n  \"bases\": {\n    \"101\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n    \"102\": \"cccccccccccccccccccccccccccccccccccccccc\"\n  },\n  \"observedMerged\": [\n    101,\n    102\n  ]\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/noise-comparisons.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/noise-comparisons.json",
      "sha256": "200f62d8e67a3916f054caa439e5998f14dd6cda5469b67af536aecc614a2d2e",
      "bytes": 2897,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"actualBuildsRun\": 0,\n  \"method\": \"Executable synthetic output fixtures only, not builds of real revisions\",\n  \"comparisons\": [\n    {\n      \"lane\": \"tests\",\n      \"changedPaths\": [\n        \"app.test.mjs\"\n      ],\n      \"outputs\": [\n        \"tests-verdict-run-1.synthetic-output.json\",\n        \"tests-verdict-run-2.synthetic-output.json\",\n        \"tests-current-run-1.synthetic-output.json\"\n      ],\n      \"differences\": [\n        {\n          \"field\": \"nonce\",\n          \"file\": \"tests synthetic output\",\n          \"judgment\": \"noise reproduced in both verdict runs\"\n        },\n        {\n          \"field\": \"head\",\n          \"file\": \"tests synthetic output\",\n          \"judgment\": \"embedded commit SHA noise\"\n        },\n        {\n          \"field\": \"behavior\",\n          \"file\": \"tests synthetic output\",\n          \"judgment\": \"unchanged\"\n        }\n      ],\n      \"result\": \"synthetic comparison permits retain lane only after fresh checks and change review\"\n    },\n    {\n      \"lane\": \"docs\",\n      \"changedPaths\": [\n        \"README.md\"\n      ],\n      \"outputs\": [\n        \"docs-verdict-run-1.synthetic-output.json\",\n        \"docs-verdict-run-2.synthetic-output.json\",\n        \"docs-current-run-1.synthetic-output.json\"\n      ],\n      \"differences\": [\n        {\n          \"field\": \"nonce\",\n          \"file\": \"docs synthetic output\",\n          \"judgment\": \"noise reproduced in both verdict runs\"\n        },\n        {\n          \"field\": \"head\",\n          \"file\": \"docs synthetic output\",\n          \"judgment\": \"embedded commit SHA noise\"\n        },\n        {\n          \"field\": \"behavior\",\n          \"file\": \"docs synthetic output\",\n          \"judgment\": \"unchanged\"\n        }\n      ],\n      \"result\": \"synthetic comparison permits retain lane only after fresh checks and change review\"\n    },\n    {\n      \"lane\": \"lint\",\n      \"changedPaths\": [\n        \"lint.json\"\n      ],\n      \"outputs\": [\n        \"lint-verdict-run-1.synthetic-output.json\",\n        \"lint-verdict-run-2.synthetic-output.json\",\n        \"lint-current-run-1.synthetic-output.json\"\n      ],\n      \"differences\": [\n        {\n          \"field\": \"nonce\",\n          \"file\": \"lint synthetic output\",\n          \"judgment\": \"noise reproduced in both verdict runs\"\n        },\n        {\n          \"field\": \"head\",\n          \"file\": \"lint synthetic output\",\n          \"judgment\": \"embedded commit SHA noise\"\n        },\n        {\n          \"field\": \"behavior\",\n          \"file\": \"lint synthetic output\",\n          \"judgment\": \"unchanged\"\n        }\n      ],\n      \"result\": \"synthetic comparison permits retain lane only after fresh checks and change review\"\n    }\n  ],\n  \"semanticDifference\": \"rate=3 is not old-run noise; invalidate and re-verify\",\n  \"devServerLane\": {\n    \"buildOutput\": null,\n    \"decision\": \"rerun required; cannot retain\"\n  },\n  \"actualPushFreshness\": \"blocked; no push authorized or attempted\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/patch-comparisons.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/patch-comparisons.json",
      "sha256": "905d7a0ca72e11a6066dd6de43f3afcec085c77d3c72c5ada9bd171abbbb8e61",
      "bytes": 2441,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"records\": [\n    {\n      \"label\": \"verdict\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"verdict.diff\",\n      \"stdout\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30\"\n    },\n    {\n      \"label\": \"same-rebased\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"same-rebased.diff\",\n      \"stdout\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30\"\n    },\n    {\n      \"label\": \"changed\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"changed.diff\",\n      \"stdout\": \"a92baed88d582066ca181a523f6322bbeea41653 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"a92baed88d582066ca181a523f6322bbeea41653\"\n    },\n    {\n      \"label\": \"tests-only\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"tests-only.diff\",\n      \"stdout\": \"705dba924e9effa5fa394c5c31ccf00f8e430ffd 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"705dba924e9effa5fa394c5c31ccf00f8e430ffd\"\n    },\n    {\n      \"label\": \"docs-only\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"docs-only.diff\",\n      \"stdout\": \"b4326ee24a4c63ba6791e18bbce038311c3fdc9f 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"b4326ee24a4c63ba6791e18bbce038311c3fdc9f\"\n    },\n    {\n      \"label\": \"lint-only\",\n      \"command\": [\n        \"git\",\n        \"patch-id\",\n        \"--stable\"\n      ],\n      \"stdinArtifact\": \"lint-only.diff\",\n      \"stdout\": \"e1a54b7f86a417eb9767024cb17a4415ea068610 0000000000000000000000000000000000000000\\n\",\n      \"stderr\": \"\",\n      \"exitCode\": 0,\n      \"id\": \"e1a54b7f86a417eb9767024cb17a4415ea068610\"\n    }\n  ],\n  \"changedPatch\": \"invalidates code verdict; independent re-verification required\",\n  \"unchangedPatch\": \"retain code verdict only; fresh current-head CI and mergeability still required\",\n  \"noGitRepositoryCreated\": true\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/prompt.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/prompt.txt",
      "sha256": "caa8c25d11e3281f47acedaab256c9fea19a2549a6fad9cda8f60815c8d94916",
      "bytes": 410,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/run.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/run.mjs",
      "sha256": "321f028b1a878009562fde40bf1c8ac16f8d13b3ad4451972f434bec0e9c542c",
      "bytes": 12228,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "import {mkdir,copyFile,readFile,writeFile} from 'node:fs/promises';\nimport assert from 'node:assert/strict';\nconst root=import.meta.dir;\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nawait mkdir(`${root}/inputs`,{recursive:true});\nawait copyFile(`${root}/../../shared/forge.json`,`${root}/inputs/forge.json`);\nconst source=JSON.parse(await readFile(`${root}/source-files.json`,'utf8'));\nconst inventory=[];\nfor(const path of source){const bytes=await readFile(`${pkg}/${path}`);inventory.push({path,bytes:bytes.length,sha256:new Bun.CryptoHasher('sha256').update(bytes).digest('hex')});}\nawait writeFile(`${root}/source-inventory.json`,JSON.stringify(inventory,null,2));\nconst args=['--no-install',`${pkg}/skills/poteto-mode/scripts/watch-pr/watch-pr`,'--owner','fixture','--repo','local','--queued-stack','--stack-prs','101','--head',`101=${'1'.repeat(40)}`,'--max-polls','2','--timeout','30'];\nconst probe=Bun.spawnSync([process.execPath,...args],{cwd:pkg,env:{...process.env,PATH:`${root}/../bounded-poll/deny-bin`,BUN_CONFIG_NO_AUTO_INSTALL:'1'}});\nawait writeFile(`${root}/setup-probe.json`,JSON.stringify({command:[process.execPath,...args],cwd:pkg,stdout:probe.stdout.toString(),stderr:probe.stderr.toString(),exitCode:probe.exitCode,guard:'Deny-only PATH; bootstrap retained, no installation or bypass'},null,2));\nassert.match(probe.stderr.toString(),/Helper setup required/);assert.doesNotMatch(probe.stderr.toString(),/FORGE EXECUTION DENIED/);\nconst supplied=[{pr:101,verifier:'A',verdict:'PASS'},{pr:102,verifier:'B',verdict:'PASS+NOTES'},{pr:103,verifier:null,verdict:null},{pr:104,verifier:'unspecified supplied verifier',verdict:'PASS'}];\nconst ceiling=supplied.findIndex(x=>!['PASS','PASS+NOTES'].includes(x.verdict));\nassert.equal(supplied[ceiling-1].pr,102);\nawait writeFile(`${root}/verdicts.json`,JSON.stringify({synthetic:true,source:'Supplied simulated verifier statements; no actual independent verifiers ran here',ceiling:102,chainGap:103,rows:supplied.map(x=>({...x,nonAuthorIdentityEvidence:'missing',verdictHead:null,verdictBase:null,stablePatchId:null,parentVsHeadArtifact:null,realSurfaceArtifact:null,actualModel:'unknown',actualEffort:'unknown'})),realLandableRun:'unproven'},null,2));\nconst patch=(path,before,after)=>`diff --git a/${path} b/${path}\\n--- a/${path}\\n+++ b/${path}\\n@@ -1 +1 @@\\n-${before}\\n+${after}\\n`;\nconst original=patch('app.mjs','export const rate=1;','export const rate=2;');\nconst changed=patch('app.mjs','export const rate=1;','export const rate=3;');\nconst patchRecords=[];\nfor(const [label,diff] of [['verdict',original],['same-rebased',original],['changed',changed],['tests-only',patch('app.test.mjs','expect(rate).toBe(1);','expect(rate).toBe(2);')],['docs-only',patch('README.md','Rate one','Rate two')],['lint-only',patch('lint.json','{\"semi\":false}','{\"semi\":true}')]]){\n  await writeFile(`${root}/${label}.diff`,diff);\n  const run=Bun.spawnSync(['git','patch-id','--stable'],{stdin:Buffer.from(diff),cwd:root});\n  assert.equal(run.exitCode,0);const id=run.stdout.toString().trim().split(' ')[0];assert.match(id,/^[a-f0-9]{40}$/);\n  patchRecords.push({label,command:['git','patch-id','--stable'],stdinArtifact:`${label}.diff`,stdout:run.stdout.toString(),stderr:run.stderr.toString(),exitCode:run.exitCode,id});\n}\nassert.equal(patchRecords[0].id,patchRecords[1].id);assert.notEqual(patchRecords[0].id,patchRecords[2].id);\nawait writeFile(`${root}/patch-comparisons.json`,JSON.stringify({synthetic:true,records:patchRecords,changedPatch:'invalidates code verdict; independent re-verification required',unchangedPatch:'retain code verdict only; fresh current-head CI and mergeability still required',noGitRepositoryCreated:true},null,2));\nconst comparisons=[];\nfor(const lane of ['tests','docs','lint']){\n  const outputs=[{label:'verdict-run-1',head:'1'.repeat(40),nonce:'run-one',behavior:'rate=2'},{label:'verdict-run-2',head:'1'.repeat(40),nonce:'run-two',behavior:'rate=2'},{label:'current-run-1',head:'2'.repeat(40),nonce:'run-three',behavior:'rate=2'}];\n  for(const out of outputs) await writeFile(`${root}/${lane}-${out.label}.synthetic-output.json`,JSON.stringify(out,null,2));\n  assert.notEqual(outputs[0].nonce,outputs[1].nonce);assert.equal(outputs[0].behavior,outputs[2].behavior);\n  comparisons.push({lane,changedPaths:[lane==='tests'?'app.test.mjs':lane==='docs'?'README.md':'lint.json'],outputs:outputs.map(o=>`${lane}-${o.label}.synthetic-output.json`),differences:[{field:'nonce',file:`${lane} synthetic output`,judgment:'noise reproduced in both verdict runs'},{field:'head',file:`${lane} synthetic output`,judgment:'embedded commit SHA noise'},{field:'behavior',file:`${lane} synthetic output`,judgment:'unchanged'}],result:'synthetic comparison permits retain lane only after fresh checks and change review'});\n}\nconst bad={...JSON.parse(await readFile(`${root}/tests-current-run-1.synthetic-output.json`,'utf8')),behavior:'rate=3'};\nawait writeFile(`${root}/semantic-change.synthetic-output.json`,JSON.stringify(bad,null,2));assert.notEqual(bad.behavior,'rate=2');\nawait writeFile(`${root}/noise-comparisons.json`,JSON.stringify({synthetic:true,actualBuildsRun:0,method:'Executable synthetic output fixtures only, not builds of real revisions',comparisons,semanticDifference:'rate=3 is not old-run noise; invalidate and re-verify',devServerLane:{buildOutput:null,decision:'rerun required; cannot retain'},actualPushFreshness:'blocked; no push authorized or attempted'},null,2));\nconst classify=s=>s.state==='MERGED'||s.mergedAt!==null?'merged':s.state==='CLOSED'?'hard-fail':!s.autoMergeRequest&&s.required.some(x=>['FAILURE','CANCELLED'].includes(x))?'hard-fail':!s.autoMergeRequest&&['UNSTABLE','DIRTY'].includes(s.mergeStateStatus)?'hard-fail':'waiting';\nconst wakes=[\n  ['ready-open',{state:'OPEN',mergedAt:null,mergeStateStatus:'CLEAN',autoMergeRequest:null,required:['SUCCESS']},'waiting'],\n  ['pending-blocked',{state:'OPEN',mergedAt:null,mergeStateStatus:'BLOCKED',autoMergeRequest:null,required:['PENDING']},'waiting'],\n  ['armed-blocked',{state:'OPEN',mergedAt:null,mergeStateStatus:'BLOCKED',autoMergeRequest:{enabled:true},required:['PENDING']},'waiting'],\n  ['closed-unmerged',{state:'CLOSED',mergedAt:null,mergeStateStatus:'CLEAN',autoMergeRequest:null,required:['SUCCESS']},'hard-fail'],\n  ...['FAILURE','CANCELLED'].flatMap(c=>[[`required-${c}`,{state:'OPEN',mergedAt:null,mergeStateStatus:'BLOCKED',autoMergeRequest:null,required:[c]},'hard-fail'],[`armed-${c}`,{state:'OPEN',mergedAt:null,mergeStateStatus:'BLOCKED',autoMergeRequest:{enabled:true},required:[c]},'waiting']]),\n  ...['UNSTABLE','DIRTY'].flatMap(s=>[[s,{state:'OPEN',mergedAt:null,mergeStateStatus:s,autoMergeRequest:null,required:['SUCCESS']},'hard-fail'],[`armed-${s}`,{state:'OPEN',mergedAt:null,mergeStateStatus:s,autoMergeRequest:{enabled:true},required:['PENDING']},'waiting']]),\n  ['merged',{state:'MERGED',mergedAt:'synthetic-observation',mergeStateStatus:'CLEAN',autoMergeRequest:null,required:['SUCCESS']},'merged']\n];\nconst wakeResults=[];\nfor(const [label,state,expected] of wakes){await writeFile(`${root}/wake-state.json`,JSON.stringify(state));const reread=JSON.parse(await readFile(`${root}/wake-state.json`,'utf8'));const result=classify(reread);assert.equal(result,expected);wakeResults.push({label,wake:'synthetic fixture event only',stateAfterWake:reread,result,reRead:true});}\nawait writeFile(`${root}/wake-results.json`,JSON.stringify({synthetic:true,results:wakeResults,helperBudget:'finite synthetic exercises, no real watcher service loop',readyDoesNotMeanMerged:true,autoMergeRequestDoesNotMeanMerged:true},null,2));\nconst transitions=[];let localAuthorized=false;let queue=[101,102,103,104];let trunk='a'.repeat(40);\ntransitions.push({action:'comment',authorization:'denied',performed:false},{action:'merge101',authorization:'denied',performed:false});\nlocalAuthorized=true;\nawait writeFile(`${root}/local-state.json`,JSON.stringify({synthetic:true,trunk,queue,heads:{101:'1'.repeat(40),102:'2'.repeat(40)},bases:{101:trunk,102:'1'.repeat(40)}}));\nfor(const pr of [101,102]){\n  const before=JSON.parse(await readFile(`${root}/local-state.json`,'utf8'));assert.equal(before.queue[0],pr);assert(localAuthorized);\n  const freshHead=before.heads[pr];const exactTrunk=before.trunk;\n  const prepared={...before,bases:{...before.bases,[pr]:exactTrunk}};\n  await writeFile(`${root}/local-state.json`,JSON.stringify(prepared,null,2));\n  const immediate=JSON.parse(await readFile(`${root}/local-state.json`,'utf8'));\n  assert.equal(immediate.heads[pr],freshHead);assert.equal(immediate.bases[pr],exactTrunk);assert.equal(immediate.trunk,exactTrunk);\n  transitions.push({action:`prepare-${pr}`,synthetic:true,exactTrunk,head:freshHead,baseBefore:before.bases[pr],baseAfter:exactTrunk,rebase:'local metadata model only; no git rebase',patchId:patchRecords[0].id,proof:'synthetic rule exercise only',freshCI:'synthetic success',freshMergeability:'synthetic clear',immediateReread:{head:immediate.heads[pr],base:immediate.bases[pr],trunk:immediate.trunk}});\n  trunk=pr===101?'c'.repeat(40):'d'.repeat(40);queue=before.queue.slice(1);\n  const after={...before,trunk,queue,observedMerged:[...(before.observedMerged??[]),pr],bases:{...before.bases,[pr]:exactTrunk}};\n  await writeFile(`${root}/local-state.json`,JSON.stringify(after,null,2));\n  const reread=JSON.parse(await readFile(`${root}/local-state.json`,'utf8'));\n  transitions.push({action:`local-model-merge-${pr}`,authorization:'local simulation only',externalOperation:false,observedLocalState:reread,newCeiling:queue[0]===102?102:null,nextBottom:queue[0],nextMetadata:'base/head/checks/patch-id must be recomputed; child retarget not assumed',mergedSHAOnTrunk:'synthetic trunk state only; no remote reachability evidence'});\n}\nassert.deepEqual(queue,[103,104]);\nawait writeFile(`${root}/transitions.json`,JSON.stringify({synthetic:true,initialCeiling:102,transitions,stoppedAt:103,realMerges:0,realComments:0,realRebases:0,remaining:[103,104],next:'Independent non-author verdict for 103 with exact current revisions, stable patch-id and parent-v-head artifacts; refresh all 104 proof too'},null,2));\nconst {runSimple,runQueued}=await import(`${pkg}/skills/poteto-mode/scripts/watch-pr/policy.ts`);\nconst {fakeReader}=await import(`${pkg}/skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts`);\nconst ctx={owner:'fixture',repo:'local',number:101,expectedHead:'a'.repeat(40)};\nconst helperEvents=[];let now=0;\nconst options={maxPolls:2,timeout:30,interval:1,sweepInterval:300,maxQueryErrors:1,allowDraft:false};\nconst clock={now:()=>now,observedAt:()=> 'synthetic-local',sleep:async s=>{now+=s;}};\nconst ready=await runSimple({contexts:[ctx],mode:'single',statusOnly:false,options,dependencies:{reader:fakeReader(),clock,emit:e=>helperEvents.push(e)}});assert.equal(ready.kind,'READY');helperEvents.push(ready);\nconst q=await runQueued({contexts:[ctx],options,dependencies:{reader:fakeReader(),clock,emit:e=>helperEvents.push(e)}});assert.equal(q.blocker.failure.kind,'poll-budget');helperEvents.push(q);\nconst complete=await runQueued({contexts:[ctx],options,dependencies:{reader:fakeReader({facts:{state:'MERGED',mergedAt:'synthetic'}}),clock,emit:e=>helperEvents.push(e)}});assert.equal(complete.kind,'COMPLETE');helperEvents.push(complete);\nlet reads=0;const base=fakeReader();\nconst second={...ctx,number:102};\nconst adv=await runQueued({contexts:[ctx,second],options:{...options,maxPolls:5},dependencies:{reader:{...base,pullRequest:async c=>{const f=await base.pullRequest(c);if(c.number===101&&++reads>2)return {...f,state:'MERGED',mergedAt:'synthetic'};return f;}},clock,emit:e=>helperEvents.push(e)}});helperEvents.push(adv);assert(helperEvents.some(e=>e.kind==='ADVANCE'));\nassert(helperEvents.every(e=>e.schemaVersion===1));\nawait writeFile(`${root}/helper-policy-events.ndjson`,helperEvents.map(e=>JSON.stringify(e)).join('\\n')+'\\n');\nconsole.log(JSON.stringify({suppliedCeiling:102,realVerdictEvidence:'missing',patchIdChangeInvalidated:true,syntheticNoiseLanes:3,wakeVariants:wakeResults.length,modeledMerges:[101,102],realMerges:0,stop:103,helperKinds:[...new Set(helperEvents.map(e=>e.kind))],setupExit:probe.exitCode}));\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/same-rebased.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/same-rebased.diff",
      "sha256": "7a0dbecdd4425c2415b5d3c97d0a5070cc1d15db87ce56e3757c84d29b7328a5",
      "bytes": 115,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/app.mjs b/app.mjs\n--- a/app.mjs\n+++ b/app.mjs\n@@ -1 +1 @@\n-export const rate=1;\n+export const rate=2;\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/semantic-change.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/semantic-change.synthetic-output.json",
      "sha256": "3bc0e8a294e554c78028f576aaf7de5a362d5d6992ff05e999a87801adae8a01",
      "bytes": 132,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"current-run-1\",\n  \"head\": \"2222222222222222222222222222222222222222\",\n  \"nonce\": \"run-three\",\n  \"behavior\": \"rate=3\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/setup-probe.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/setup-probe.json",
      "sha256": "04c34cb1c6231b37afaa82a3b6fcf4de0008fc940f6536c85a746827d3692af5",
      "bytes": 1908,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"command\": [\n    \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"--owner\",\n    \"fixture\",\n    \"--repo\",\n    \"local\",\n    \"--queued-stack\",\n    \"--stack-prs\",\n    \"101\",\n    \"--head\",\n    \"101=1111111111111111111111111111111111111111\",\n    \"--max-polls\",\n    \"2\",\n    \"--timeout\",\n    \"30\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"stdout\": \"\",\n  \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr:4:1\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n  \"exitCode\": 1,\n  \"guard\": \"Deny-only PATH; bootstrap retained, no installation or bypass\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/source-files.json",
      "sha256": "43ad2f097e2e3326a0d309b527e79b8fb3134ba2cd20fbda31658d94a9234d42",
      "bytes": 336,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "[\n  \"skills/poteto-mode/playbooks/shipping.md\",\n  \"skills/poteto-mode/playbooks/babysit.md\",\n  \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n  \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n  \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n  \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n  \"skills/poteto-mode/scripts/bootstrap.ts\"\n]"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/source-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/source-inventory.json",
      "sha256": "48af0e76dfe9f591839ec4bd5d670fc4191d50900011e466b47e75fc63529f46",
      "bytes": 1170,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "[\n  {\n    \"path\": \"skills/poteto-mode/playbooks/shipping.md\",\n    \"bytes\": 8873,\n    \"sha256\": \"94bb986b545617ed6123fa76efd5a5ceac73601e232bde929aad357fba1ece9b\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/playbooks/babysit.md\",\n    \"bytes\": 13631,\n    \"sha256\": \"85883ceae3e4485fb00ed77b9337a48148bd0263ef045a6dc496761b7fa8fa39\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"bytes\": 8516,\n    \"sha256\": \"4198f32b22cf1d8ff367deee1dbfea805e6eecdd7ff1da3409ae7c0b07fb1c59\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"bytes\": 227,\n    \"sha256\": \"5d30c476658fe73baa013aeab37d4c88302f1d4ad9ab7f8407d97ac982ee6e8d\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"bytes\": 8271,\n    \"sha256\": \"af2dd3a1f2da4af5680954a69f16e2a5a41bafea13c52267a7c99a083436a878\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"bytes\": 12700,\n    \"sha256\": \"951ba0fc933b215757c6a1eeca6b71801eb52247eb97a24bb9d585a6d301f834\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/scripts/bootstrap.ts\",\n    \"bytes\": 1353,\n    \"sha256\": \"307cdd435542b6adb719e885b08028fbb0a1467a6dcfbb1297392af475abe03f\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/supporting-source-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/supporting-source-inventory.json",
      "sha256": "26a6503446c7db75cb3da322ead1b9d0eb24e28417b3abff45e6957c3c3e9e1b",
      "bytes": 2042,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "[\n  {\n    \"path\": \"references/host-capabilities.md\",\n    \"bytes\": 7155,\n    \"sha256\": \"f0f09ce28b6feca4d72694d5687204dc074aa58dade9a0ab59656da3bfa1bd20\"\n  },\n  {\n    \"path\": \"references/workflow-ownership.md\",\n    \"bytes\": 1265,\n    \"sha256\": \"50644b3a9a3dfd5651382eaca1d3a2728af0b3157d6d66b730930370a64bb03c\"\n  },\n  {\n    \"path\": \"references/model-roles.md\",\n    \"bytes\": 2869,\n    \"sha256\": \"c86696b6c568b7db80a7e339856986e64482ce6a418bb91946ce3a3b772f79a1\"\n  },\n  {\n    \"path\": \"references/orchestration-contract.md\",\n    \"bytes\": 6273,\n    \"sha256\": \"5dd740ad66d992df252754d189d0dc207900023372392a0db4309b85eb5e4ec5\"\n  },\n  {\n    \"path\": \"references/agent-prompts/poteto-agent.md\",\n    \"bytes\": 1221,\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/SKILL.md\",\n    \"bytes\": 32329,\n    \"sha256\": \"cb03eedb91cea96b570af30a7af317c6aae6a47a321cff2e82af656141ab0f14\"\n  },\n  {\n    \"path\": \"skills/unslop/SKILL.md\",\n    \"bytes\": 6015,\n    \"sha256\": \"195411d320b5b328f9f642baf59757ed19aaf0931c0838740e0aca273d538dc1\"\n  },\n  {\n    \"path\": \"skills/technical-writing/SKILL.md\",\n    \"bytes\": 10591,\n    \"sha256\": \"409a010a405d3ea3e4c2386e2a5ce5fa7cc64dffd8304feb99282a5e099564f6\"\n  },\n  {\n    \"path\": \"skills/principle-prove-it-works/SKILL.md\",\n    \"bytes\": 1814,\n    \"sha256\": \"a78cfdebd9dccfba5f6d69bbd74379924769d769e4b3e2f514846fc7bdd56edc\"\n  },\n  {\n    \"path\": \"skills/principle-build-the-lever/SKILL.md\",\n    \"bytes\": 3644,\n    \"sha256\": \"483e5d66b0ec7fcbf98fe7175c20d60109f6a35c3c7fc8cc34771f42fee20083\"\n  },\n  {\n    \"path\": \"skills/principle-model-the-domain/SKILL.md\",\n    \"bytes\": 2663,\n    \"sha256\": \"05c073621ec18b442ecd7487dc6136bddb6a842f2bd537cb73567de7088a6b0e\"\n  },\n  {\n    \"path\": \"skills/how/SKILL.md\",\n    \"bytes\": 4092,\n    \"sha256\": \"bca7b43af6d6d0089d20edb2ec2178d681d589357c20ea345eddbf81ce87f7e8\"\n  },\n  {\n    \"path\": \"skills/architect/SKILL.md\",\n    \"bytes\": 7555,\n    \"sha256\": \"af93988bb4eec01a50f1caf71fd196a01f5affd56d2dcb36fe70d1735fa28f78\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/tests-current-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/tests-current-run-1.synthetic-output.json",
      "sha256": "4242425350ebdf9acf0239a160b1aba80a8ca39086261d9ecad5297847d6c604",
      "bytes": 132,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"current-run-1\",\n  \"head\": \"2222222222222222222222222222222222222222\",\n  \"nonce\": \"run-three\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/tests-only.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/tests-only.diff",
      "sha256": "0a070b66ca6e8270348acdc29df52dfd706bb048c879825acf830c8818865cdd",
      "bytes": 137,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/app.test.mjs b/app.test.mjs\n--- a/app.test.mjs\n+++ b/app.test.mjs\n@@ -1 +1 @@\n-expect(rate).toBe(1);\n+expect(rate).toBe(2);\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/tests-verdict-run-1.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/tests-verdict-run-1.synthetic-output.json",
      "sha256": "7bafc679c051d62cff2460a52c01e208d77e372a7ee59568f5953c5a907f9963",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-1\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-one\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/tests-verdict-run-2.synthetic-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/tests-verdict-run-2.synthetic-output.json",
      "sha256": "39f5a991b3a4f63138f9fbe9a88210d6e5c73fad71c78058db4cf4470070e2d9",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"label\": \"verdict-run-2\",\n  \"head\": \"1111111111111111111111111111111111111111\",\n  \"nonce\": \"run-two\",\n  \"behavior\": \"rate=2\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/todo.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/todo.md",
      "sha256": "11501ae90ac0411dcfefd4f5066dbd847724eab93c8c3705c24c0a4db897a562",
      "bytes": 7814,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "1. **Resolve the forge, then verify every PR independently.** GitHub CLI (`gh`) is the default. If `command -v origin` succeeds and Origin can resolve the repository, use `origin pr ...` for PR view, watch, edit, and merge operations. Otherwise stay on `gh` and record the fallback. Never require Graphite (`gt`). One subagent per PR, not batched, each an independently spawned worker through an observed host binding, each exercising the real surface with the matching exposed and authorized control skill against exact parent versus head revisions. The upstream examples `control-ui` and `control-cli` are external skills, not bundled bindings. Missing control capability leaves real-surface verification blocked. Use inherited model roles unless current supported selection and actual results are observed. Each returns `PASS`, `PASS+NOTES` or `FAIL`, with verifier identity, exact revisions and method artifacts, and posts that verdict on its own PR when comment authorization exists. Otherwise retain the verdict locally and report that posting is blocked. A missing worker permits local sequential recommendations as reduced capability, never an independent verdict or a landable run. Safe means a verdict from an agent that did not write the code. CI green is not a verdict, and an approving bot review is not a verdict.\n2. **Land only the contiguous verified run rooted at the bottom.** Walk up from the lowest unmerged PR and stop at the first one without a passing verdict, where both `PASS` and `PASS+NOTES` pass. A verified PR sitting above an unverified one is not landable. Report the ceiling as a PR number and say what breaks the chain.\n3. **Re-check that each verdict still describes the patch.** Record the verdict head SHA, base SHA, and stable `git patch-id` of that PR's base-to-head diff. A rebase or base retarget rewrites SHAs and can silently invalidate a verdict without touching a check. Before landing a PR, read and record its current exact head SHA and base SHA, resolve the base-to-head diff at those revisions, and compare the recorded patch-id with its current base-to-head patch-id. Re-read the head and base immediately before the authorized merge or arm action. If either moved since the freshness check, stop and repeat that check. When the two patches differ only in tests, docs, or lint config, build what each lane ran. Build it twice at the verdict SHA and once at the current head. A difference is noise if the two builds at the verdict SHA also show it, or if it is an embedded commit SHA. Judge each difference, not each file, and report each kind of noise with its files. If only noise differs, that lane's result stays valid, and checks and a review of the change run fresh. Do not reuse a lane result from a dev server or from anything else with no build output. Rerun that lane. Re-verify anything else when the patch changed. When it did not, keep the code verdict but re-run mergeability and CI at the current head. Never use matching commit messages or a green check from an older SHA as a substitute.\n4. **Prepare only the bottom PR.** Fetch current trunk. Rebase the lowest verified branch onto the exact trunk tip when needed, push it, and retarget only that PR to trunk through an exposed built-in PR tool when present, as required by [opening a PR](opening-a-pr.md). Without that tool use `origin pr edit <pr> --base <trunk>` or `gh pr edit <pr> --base <trunk>`. Re-run step 3 after the push. Do not retarget, arm, or merge descendants yet.\n5. **Land one PR at a time.** If the bottom PR is mergeable now, squash it with `origin pr merge <pr> --squash` or `gh pr merge <pr> --squash`. If requirements are still running and the user asked for merge-when-ready, arm only that PR with `origin pr merge <pr> --squash --auto` or `gh pr merge <pr> --squash --auto`. Origin's `--auto` is Origin merge-when-ready. GitHub's `--auto` is GitHub auto-merge. Wait for that PR to merge before preparing the next one.\n6. **Do not read GitHub `autoMergeRequest` as stack readiness.** At most it says GitHub auto-merge was requested for one GitHub PR. It does not prove Origin merge-when-ready is armed, that a descendant is queued, that a patch verdict is current, or that the contiguous stack is safe. Confirm the active forge's state for the current bottom PR, and say that the state is unknown if the active forge cannot report it.\n7. **Recompute after every merge.** Fetch trunk, confirm the merged SHA is present, drop the merged PR from the frozen bottom-to-top list, and inspect the new bottom PR's base, head, checks, and patch-id. A host may retarget a child automatically, but do not assume it did. Repeat steps 3 through 6 for that one PR. Independent work stays outside this chain and ships on its own.\n8. **Watch the current frontier until it merges or fails. Do not mutate the queue around it.** With Origin, use `origin pr view <pr> --checks --comments` and `origin pr checks <pr> --watch`, then re-read the PR until it reports merged or blocked. With GitHub, use the read-only [watcher](../scripts/watch-pr/watch-pr) from the package root as `bun --no-install skills/poteto-mode/scripts/watch-pr/watch-pr --owner <owner> --repo <repo> --queued-stack --stack-prs <bottom> --head <bottom=full-40-character-head> --max-polls <remaining-count> --timeout <remaining-seconds>` only as an event wake and poll `gh pr view <pr> --json state,mergedAt,mergeStateStatus,statusCheckRollup,autoMergeRequest` after each wake, ignoring `READY` until `mergedAt` is non-null or `state` is `MERGED`. Only then run step 7. Hard-fail only when `state` is `CLOSED` with no `mergedAt`, a required check concludes `FAILURE` or `CANCELLED` and blocks merge after auto-merge is no longer pending, or `mergeStateStatus` is `UNSTABLE` or `DIRTY` with no auto-merge pending. `BLOCKED` while checks are pending or auto-merge is armed is not failure. Do not use Babysit's queued `WAITING`/`merge-queue` stop condition here. Hold the watch through the observed authorized loop or wake binding within the declared budget. Do not add a second sleep loop. The watcher emits NDJSON schemaVersion 1 events. Inspect kind, terminal and reason, never exit 0 alone. Queued mode emits non-terminal `WAITING` with `reason.kind` equal to `merge-queue`, not `READY`. Terminal helper blockers or budget exhaustion require inspection of the active forge, not an invented merged or hard-failed state. The [bootstrap](../scripts/bootstrap.ts) checks pinned dependencies and fails setup-required; never install or bypass it. [Helper setup](../../../docs/testing/helper-setup.md) is separately authorized. For Origin, use a finite bound and an observed stop binding for check watching, or bounded view snapshots when an unbounded watch cannot be stopped. Report each merge and the new ceiling. If the queue stalls, diagnose before mutating.\n9. **Stop at the ceiling.** When the verified run is merged, report what landed, what the next unverified PR is, and what verifying it would take. Extending the run is a new pass through step 1.\n\n\n## Local disposition\n\n- Completed source reads, authorized fixture copy, local policy proof, setup probe, and report readback.\n- Live forge steps skipped because services and external writes are denied.\n- Independent real-artifact shipping verification remains blocked.\n\n## Throughput checkpoint\n\n- Blocking first steps. Read all named frozen sources and preserve authorization boundaries before execution.\n- Independent workstreams. These two case directories have one assigned owner. No nested workers ran.\n- Shared mutable state. The shared fixture directory remains read-only. Each case has its own copied inputs and evidence.\n- Smallest safe decomposition. One local owner executes deterministic synthetic fixtures. No real forge or repository exists for this task.\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/transitions.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/transitions.json",
      "sha256": "34c37ff8359a7499a3a99e4735c0856886de98e0f187a93eb44c6290a1682877",
      "bytes": 3965,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"initialCeiling\": 102,\n  \"transitions\": [\n    {\n      \"action\": \"comment\",\n      \"authorization\": \"denied\",\n      \"performed\": false\n    },\n    {\n      \"action\": \"merge101\",\n      \"authorization\": \"denied\",\n      \"performed\": false\n    },\n    {\n      \"action\": \"prepare-101\",\n      \"synthetic\": true,\n      \"exactTrunk\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n      \"head\": \"1111111111111111111111111111111111111111\",\n      \"baseBefore\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n      \"baseAfter\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n      \"rebase\": \"local metadata model only; no git rebase\",\n      \"patchId\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30\",\n      \"proof\": \"synthetic rule exercise only\",\n      \"freshCI\": \"synthetic success\",\n      \"freshMergeability\": \"synthetic clear\",\n      \"immediateReread\": {\n        \"head\": \"1111111111111111111111111111111111111111\",\n        \"base\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n        \"trunk\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"\n      }\n    },\n    {\n      \"action\": \"local-model-merge-101\",\n      \"authorization\": \"local simulation only\",\n      \"externalOperation\": false,\n      \"observedLocalState\": {\n        \"synthetic\": true,\n        \"trunk\": \"cccccccccccccccccccccccccccccccccccccccc\",\n        \"queue\": [\n          102,\n          103,\n          104\n        ],\n        \"heads\": {\n          \"101\": \"1111111111111111111111111111111111111111\",\n          \"102\": \"2222222222222222222222222222222222222222\"\n        },\n        \"bases\": {\n          \"101\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n          \"102\": \"1111111111111111111111111111111111111111\"\n        },\n        \"observedMerged\": [\n          101\n        ]\n      },\n      \"newCeiling\": 102,\n      \"nextBottom\": 102,\n      \"nextMetadata\": \"base/head/checks/patch-id must be recomputed; child retarget not assumed\",\n      \"mergedSHAOnTrunk\": \"synthetic trunk state only; no remote reachability evidence\"\n    },\n    {\n      \"action\": \"prepare-102\",\n      \"synthetic\": true,\n      \"exactTrunk\": \"cccccccccccccccccccccccccccccccccccccccc\",\n      \"head\": \"2222222222222222222222222222222222222222\",\n      \"baseBefore\": \"1111111111111111111111111111111111111111\",\n      \"baseAfter\": \"cccccccccccccccccccccccccccccccccccccccc\",\n      \"rebase\": \"local metadata model only; no git rebase\",\n      \"patchId\": \"1ac7a8abb7fc24c6bdcb795557dff96d025a4b30\",\n      \"proof\": \"synthetic rule exercise only\",\n      \"freshCI\": \"synthetic success\",\n      \"freshMergeability\": \"synthetic clear\",\n      \"immediateReread\": {\n        \"head\": \"2222222222222222222222222222222222222222\",\n        \"base\": \"cccccccccccccccccccccccccccccccccccccccc\",\n        \"trunk\": \"cccccccccccccccccccccccccccccccccccccccc\"\n      }\n    },\n    {\n      \"action\": \"local-model-merge-102\",\n      \"authorization\": \"local simulation only\",\n      \"externalOperation\": false,\n      \"observedLocalState\": {\n        \"synthetic\": true,\n        \"trunk\": \"dddddddddddddddddddddddddddddddddddddddd\",\n        \"queue\": [\n          103,\n          104\n        ],\n        \"heads\": {\n          \"101\": \"1111111111111111111111111111111111111111\",\n          \"102\": \"2222222222222222222222222222222222222222\"\n        },\n        \"bases\": {\n          \"101\": \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\n          \"102\": \"cccccccccccccccccccccccccccccccccccccccc\"\n        },\n        \"observedMerged\": [\n          101,\n          102\n        ]\n      },\n      \"newCeiling\": null,\n      \"nextBottom\": 103,\n      \"nextMetadata\": \"base/head/checks/patch-id must be recomputed; child retarget not assumed\",\n      \"mergedSHAOnTrunk\": \"synthetic trunk state only; no remote reachability evidence\"\n    }\n  ],\n  \"stoppedAt\": 103,\n  \"realMerges\": 0,\n  \"realComments\": 0,\n  \"realRebases\": 0,\n  \"remaining\": [\n    103,\n    104\n  ],\n  \"next\": \"Independent non-author verdict for 103 with exact current revisions, stable patch-id and parent-v-head artifacts; refresh all 104 proof too\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/verdict.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/verdict.diff",
      "sha256": "7a0dbecdd4425c2415b5d3c97d0a5070cc1d15db87ce56e3757c84d29b7328a5",
      "bytes": 115,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "diff --git a/app.mjs b/app.mjs\n--- a/app.mjs\n+++ b/app.mjs\n@@ -1 +1 @@\n-export const rate=1;\n+export const rate=2;\n"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/verdicts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/verdicts.json",
      "sha256": "9a4521737d6abe079327f523fd8a4607849fcc289f10df3f48c9046a8252a5ab",
      "bytes": 1606,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"source\": \"Supplied simulated verifier statements; no actual independent verifiers ran here\",\n  \"ceiling\": 102,\n  \"chainGap\": 103,\n  \"rows\": [\n    {\n      \"pr\": 101,\n      \"verifier\": \"A\",\n      \"verdict\": \"PASS\",\n      \"nonAuthorIdentityEvidence\": \"missing\",\n      \"verdictHead\": null,\n      \"verdictBase\": null,\n      \"stablePatchId\": null,\n      \"parentVsHeadArtifact\": null,\n      \"realSurfaceArtifact\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\"\n    },\n    {\n      \"pr\": 102,\n      \"verifier\": \"B\",\n      \"verdict\": \"PASS+NOTES\",\n      \"nonAuthorIdentityEvidence\": \"missing\",\n      \"verdictHead\": null,\n      \"verdictBase\": null,\n      \"stablePatchId\": null,\n      \"parentVsHeadArtifact\": null,\n      \"realSurfaceArtifact\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\"\n    },\n    {\n      \"pr\": 103,\n      \"verifier\": null,\n      \"verdict\": null,\n      \"nonAuthorIdentityEvidence\": \"missing\",\n      \"verdictHead\": null,\n      \"verdictBase\": null,\n      \"stablePatchId\": null,\n      \"parentVsHeadArtifact\": null,\n      \"realSurfaceArtifact\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\"\n    },\n    {\n      \"pr\": 104,\n      \"verifier\": \"unspecified supplied verifier\",\n      \"verdict\": \"PASS\",\n      \"nonAuthorIdentityEvidence\": \"missing\",\n      \"verdictHead\": null,\n      \"verdictBase\": null,\n      \"stablePatchId\": null,\n      \"parentVsHeadArtifact\": null,\n      \"realSurfaceArtifact\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\"\n    }\n  ],\n  \"realLandableRun\": \"unproven\"\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/wake-results.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/wake-results.json",
      "sha256": "87782adc04c8dbdb76747500d02579d67087ff73d2ea2a67b9e568e3f579b26c",
      "bytes": 4932,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\n  \"synthetic\": true,\n  \"results\": [\n    {\n      \"label\": \"ready-open\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"CLEAN\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"SUCCESS\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"pending-blocked\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"PENDING\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"armed-blocked\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": {\n          \"enabled\": true\n        },\n        \"required\": [\n          \"PENDING\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"closed-unmerged\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"CLOSED\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"CLEAN\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"SUCCESS\"\n        ]\n      },\n      \"result\": \"hard-fail\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"required-FAILURE\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"FAILURE\"\n        ]\n      },\n      \"result\": \"hard-fail\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"armed-FAILURE\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": {\n          \"enabled\": true\n        },\n        \"required\": [\n          \"FAILURE\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"required-CANCELLED\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"CANCELLED\"\n        ]\n      },\n      \"result\": \"hard-fail\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"armed-CANCELLED\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"BLOCKED\",\n        \"autoMergeRequest\": {\n          \"enabled\": true\n        },\n        \"required\": [\n          \"CANCELLED\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"UNSTABLE\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"UNSTABLE\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"SUCCESS\"\n        ]\n      },\n      \"result\": \"hard-fail\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"armed-UNSTABLE\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"UNSTABLE\",\n        \"autoMergeRequest\": {\n          \"enabled\": true\n        },\n        \"required\": [\n          \"PENDING\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"DIRTY\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"DIRTY\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"SUCCESS\"\n        ]\n      },\n      \"result\": \"hard-fail\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"armed-DIRTY\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"OPEN\",\n        \"mergedAt\": null,\n        \"mergeStateStatus\": \"DIRTY\",\n        \"autoMergeRequest\": {\n          \"enabled\": true\n        },\n        \"required\": [\n          \"PENDING\"\n        ]\n      },\n      \"result\": \"waiting\",\n      \"reRead\": true\n    },\n    {\n      \"label\": \"merged\",\n      \"wake\": \"synthetic fixture event only\",\n      \"stateAfterWake\": {\n        \"state\": \"MERGED\",\n        \"mergedAt\": \"synthetic-observation\",\n        \"mergeStateStatus\": \"CLEAN\",\n        \"autoMergeRequest\": null,\n        \"required\": [\n          \"SUCCESS\"\n        ]\n      },\n      \"result\": \"merged\",\n      \"reRead\": true\n    }\n  ],\n  \"helperBudget\": \"finite synthetic exercises, no real watcher service loop\",\n  \"readyDoesNotMeanMerged\": true,\n  \"autoMergeRequestDoesNotMeanMerged\": true\n}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/wake-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack/wake-state.json",
      "sha256": "fd17db27512851b18c26fbba1e1941d7af7642c2d0de958547df10818c73c88e",
      "bytes": 127,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "{\"state\":\"MERGED\",\"mergedAt\":\"synthetic-observation\",\"mergeStateStatus\":\"CLEAN\",\"autoMergeRequest\":null,\"required\":[\"SUCCESS\"]}"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/contiguous-verified-stack.result.md",
      "sha256": "eb0fb0cf46df2373b8900eb75d92fe3ab82196212933746526a8500d90b9ee24",
      "bytes": 8724,
      "owners": [
        "grades-native-07.json#6"
      ],
      "text": "# Contiguous verified stack observation\n\nThe supplied simulated verdicts give a ceiling of 102. The local state model merges 101, then 102, then stops before 103. Real landability remains unproven. No forge was contacted and no real merge, comment, rebase, push, retarget, commit, install, or schedule occurred.\n\n## Supplied prompt\n\nUse inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\n\n## Frozen stack and verifier gaps\n\n| PR | Supplied simulated verifier | Supplied verdict | Meaning |\n| --- | --- | --- | --- |\n| 101 | A | PASS | Starts the simulated passing run |\n| 102 | B | PASS+NOTES | Passing notes do not break the run |\n| 103 | absent | absent | Breaks the chain |\n| 104 | unspecified | PASS | Cannot jump over 103 |\n\nverdicts.json explicitly records null real verdict head, base, stable patch ID, parent-versus-head artifact, and real-artifact output for every PR. Non-author identity evidence is missing. A and B are supplied verifier labels, not spawned independent workers here. The verifier for 104 is unspecified. Requested model and effort inherit the parent. Actual models, efforts, independence, and diversity are unknown. The supplied package identifier is f4623636a287bea2aa79c4b2234a53d20a5f193c. There is no task git repository.\n\n## Freshness and synthetic patch comparisons\n\nrun.mjs writes actual synthetic diff files and feeds them to git patch-id --stable through Bun. This command needs no repository, commits, config changes, or network. patch-comparisons.json retains each exact command, diff input artifact, stdout, stderr, exit code, and stable patch ID. The unchanged rebased diff keeps its ID. The changed production rate invalidates the synthetic code verdict. That changed branch requires independent re-verification and is not merged by the valid branch of the model.\n\nTests-only, docs-only, and lint-only variants each have three executable synthetic output fixtures. Every lane has two outputs at the verdict pin and one at the current pin. noise-comparisons.json evaluates each difference and names its output file. The nonce differs between the two verdict runs and is reproducible noise. The embedded head SHA is commit metadata noise. The behavioral value stays equal. A separate rate=3 output proves that semantic changes cannot be dismissed as noise. The dev-server lane has no build output and requires rerun. These are synthetic comparisons, with ZERO actual builds of task revisions. They do not establish real lane validity.\n\n## Local permission and landing model\n\nComments and merge start denied in transitions.json. Later authorization applies only to one-at-a-time LOCAL state changes, never service operations. The model reads exact synthetic trunk aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa before preparing 101. It changes only the current bottom base to that trunk. It reads the stored head, base, and trunk again immediately before the modeled merge. It retains a synthetic patch ID, clean check result, and mergeability observation for this exercise.\n\nAfter the modeled 101 merge, the script writes and rereads synthetic trunk cccccccccccccccccccccccccccccccccccccccc. It removes only 101 and observes the new bottom 102. The child's saved base remains its old parent until explicit local preparation, so automatic retargeting is never assumed. It then repeats exact trunk, head, base, patch, check, and immediate freshness inspection for 102. After 102 the modeled trunk is dddddddddddddddddddddddddddddddddddddddd and the remaining queue is 103,104. The model stops at the original ceiling. These trunk strings are synthetic pins, not actual merge commits or proof of ancestor reachability. Actual push and rebase freshness checks remain blocked.\n\nThe first synthetic execution read the old base immediately before its modeled merge. I corrected that local preparation to persist the new base before the immediate readback, then reran the combined wrapper. The retained execution.json and transitions.json contain the corrected second variant. The earlier artifact bytes were overwritten and are not reconstructable from retained files. That combined rerun also caused the bounded-poll session budget deviation described in bounded-poll.result.md.\n\nThe paired bounded replay therefore used FOUR synthetic snapshot attempts over this session. The actual wrapper setup probes performed ZERO snapshot polls. No further replay or snapshots ran after the deviation was identified.\n\n## Wake variants and helper semantics\n\nwake-results.json records 13 distinct fixtures. Each fixture writes local wake state and reads it back after the synthetic wake. OPEN with READY-like checks remains waiting. autoMergeRequest alone remains waiting. Pending BLOCKED and armed BLOCKED remain waiting. CLOSED without mergedAt hard-fails. Required FAILURE and CANCELLED hard-fail only with no auto-merge pending. UNSTABLE and DIRTY hard-fail only with no auto-merge pending. Their armed variants remain waiting. MERGED or a non-null mergedAt provides local modeled merge evidence. No actual forge wake was registered.\n\nhelper-policy-events.ndjson contains actual installed policy executions with inert readers. Every event has schemaVersion 1. The synthetic cases include READY, QUEUE, STATUS, WAITING with merge-queue, poll-budget BLOCKER, ADVANCE, and COMPLETE. Babysit stops on READY or reports merge-queue WAITING and stops its watcher. Shipping uses those only as wake events and rereads current state until merge is observed. READY and autoMergeRequest never prove a merge. The finite helper attempts stop without a second sleep loop. Separate setup gating is preserved.\n\n## Actual commands, source reads, and limits\n\nexecution.json retains bun --no-install contiguous-verified-stack/run.mjs, stdout, empty stderr, and exit 0. setup-probe.json retains the real wrapper invocation, explicit fixture/local, full synthetic 101 pin, max-polls 2, timeout 30, stdout, stderr, and exit 1. Bootstrap stopped at missing commander before CLI imports. A deny-only forge PATH prevents service execution. No dependency install or bypass occurred.\n\nEvery source-files.json path was read completely from the frozen installed package through tools. source-inventory.json retains byte counts and SHA256 values. supporting-source-inventory.json lists the full supporting contract reads and applied leaves. Additional policy, reader, renderer, fake-reader, and policy test sources were read in the paired bounded case. Preexisting source-read.txt is preparation evidence only. The 53 installed policy and reader test passes and dependency-blocked CLI test are retained in bounded-poll/policy-tests.json and bounded-poll/cli-test.json.\n\n## Requirement coverage\n\n| Requirement | Artifact or limit |\n| --- | --- |\n| Frozen101-104, A/B verdicts, ceiling102, gap103 | verdicts.json; real revision and verifier artifacts missing |\n| Exact current trunk and immediate freshness reread | transitions.json and local-state.json, synthetic only |\n| Changed patch invalidation and unchanged patch retention rule | patch-comparisons.json and diff files |\n| Tests/docs/lint lanes, twice verdict once current, each noise kind | noise-comparisons.json and nine output files |\n| No-output dev lane rerun | noise-comparisons.json |\n| Initially denied comments and merge, later local-only authority | transitions.json; real writes0 |\n| Wake reread and all pending/failure variants | wake-results.json, 13 cases |\n| READY and autoMergeRequest do not prove merge | wake-results.json and helper-policy-events.ndjson |\n| Recompute queue after each modeled merge; no assumed retarget | transitions.json; stop103 |\n| Actual helper setup failure and no service access | setup-probe.json |\n\nBuild the Lever created the executable fixture script. Model the Domain made state, authorization, queue, and wake outcomes explicit. Prove It Works retained executable comparisons and readback rather than claiming real merges. Unslop and Technical writing shaped this report. How traced bootstrap, CLI, injected reader, policy, and event rendering. Architect was read but no independent design exploration or review ran. The next real gap needs a non-author verifier for103 with exact current head/base, stable patch ID, parent-versus-head and real-artifact proof. Real101/102 shipping also remains blocked until those same missing freshness and verifier artifacts exist for them.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/contiguous-verified-stack.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/contiguous-verified-stack.result.md",
      "sha256": "342cbb78d6ddf2224eff2684164c586a2b147ffeab6dfd8b1a8cf2f5fc35b8ae",
      "bytes": 20346,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "# contiguous-verified-stack\n\n## Supplied input\n\nThe exact supplied case contract, task payload, expected outcomes and original fixture paths are retained below. Earlier expectations are input, not this run's grade. The latest user directive supplies the real input SHA and forbids creating further commits. Assignments use committed-inputs bytes at that SHA, replacing mutable shared fixture paths.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"contiguous-verified-stack\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/playbooks/babysit.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n      \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n      \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\"\n    ],\n    \"prompt\": \"Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\",\n    \"requirements\": [\n      \"Record exact verdict head SHA, base SHA, stable patch-id, independent non-author verifier identity and parent-versus-head real-surface artifacts per PR.\",\n      \"Ceiling is PR 102; 104 cannot bypass 103. PASS+NOTES passes; CI and bot approvals do not.\",\n      \"Changed substantive patch requires re-verification. Unchanged patch retains code verdict but refreshes CI and mergeability at current head.\",\n      \"For tests/docs/lint-only differences build each lane twice at verdict SHA and once at current head; classify each noise kind with files, refresh checks and review; dev-server lanes without build output rerun.\",\n      \"Prepare only bottom against exact fetched trunk, use built-in retarget tool if exposed, recheck after push, then squash or arm only explicitly authorized bottom and await confirmed merge.\",\n      \"Read active-forge state after every wake; READY and autoMergeRequest never prove merge. Preserve pending BLOCKED, closed-unmerged and failed/cancelled required checks or UNSTABLE/DIRTY with no auto-merge pending distinctions.\",\n      \"After merge fetch trunk, confirm merged SHA present, recompute base/head/checks/patch-id and ceiling, never assume automatic retarget.\",\n      \"Use actual watcher pins, finite budgets, schemaVersion 1 events and separate setup gate; stop safely on missing capability, user stop or exhaustion.\"\n    ],\n    \"expectedFull\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n    \"expectedReduced\": \"Without workers or real-surface tools, produce local sequential recommendations with independence unverified and no landable run. Without comments retain independent verdict artifacts locally. Without loop support use bounded foreground snapshots, disclose no unattended watch; denied merges produce only the authorized merge plan.\",\n    \"expectedBlocked\": \"Missing exact revisions, stable patch identity, independent verifier artifacts, build output for reused lanes, forge access, helper dependencies or merge authorization blocks the affected verification or landing. Stop at first gap or unknown action outcome; perform no external writes.\",\n    \"forbiddenClaims\": [\n      \"CI green or bot approval is an independent verdict.\",\n      \"Sequential role switching supplies independent per-PR verification.\",\n      \"Requested model or documented tool establishes observed support.\",\n      \"A verified descendant above a gap is landable.\",\n      \"Matching commit messages or old green checks prove current patch safety.\",\n      \"READY, WAITING, exit 0 or autoMergeRequest proves merged or whole-stack readiness.\",\n      \"Pending BLOCKED alone is hard failure.\",\n      \"Setup, verdict posting, push, retarget or auto-merge is implicitly authorized.\",\n      \"Structural fixture validation proves host parity or actual merges.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\"\n  },\n  \"caseId\": \"contiguous-verified-stack\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/shipping.md\",\n    \"skills/poteto-mode/playbooks/babysit.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"skills/poteto-mode/scripts/bootstrap.ts\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\",\n  \"expectedFullUnchanged\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/forge.json\"\n  ],\n  \"taskPayload\": \"Root prepares local frozen stack records 101/102/103/104 backed by real case-local Git heads/trunk. Independent verifier A inspects 101 and verifier B inspects 102; retain actual PASS/PASS+NOTES findings only if earned. Leave 103 without verdict and 104 out of contiguous eligibility. Inspect changed-patch invalidation and tests/docs/lint noisy-build branch. Model one authorized bottom merge at a time only in the local simulator, with explicit simulator action/destination state; contact no forge. Full real-surface host support remains unmet without actual matching forge controls.\",\n  \"missingPrerequisites\": [\n    \"Specific 101..104 input records are missing from generic forge.json and must be prepared\",\n    \"Two actual verifier outcomes cannot be predeclared\",\n    \"Local simulator proves modeled sequencing only; real-surface branch remains BLOCKED\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/babysit.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\"\n  ]\n}\n```\n\n## Actual execution record\n\nTask input revision independently observed: ec045fadb47b598147052035b7eb1a9c47813156. Installed plugin metadata reports 0.1.0. Required sourceFiles were read through cat and retained as complete stdout/exit-status records in ../evidence/skills__*.json. The supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from inputRevision. The installed package has no .git metadata and the fixture Git lacks that object; the freeze-to-bytes relationship was not independently verified. No package update occurred.\n\nNative independent-worker binding is collaboration.spawn_agent, exposed outside ALL_TOOLS. Eight case-workflow identities returned, with six substantive read-only completions and two blocked prerequisite-verifier results. A separate ninth worker, /root/artifact_inspector, inspected the saved report evidence without assigning grades. This count is native dispatch evidence, not service success telemetry. Requested model/effort inherit-parent. Actual models/efforts unknown. No family or diversity claim.\n\nRaw spawn response objects have only task_name. Full assignment bodies and complete routed role prompts are in each *.task.txt. Corresponding immutable *.assignment.json files preserve revision and scope. Native final text was copied while the run was active into *.native-result.md, then serialized with explicitly coordinator-created metadata in *.native-result.json. The latter envelopes are not raw extra tool fields. No worker raw-tool transcript export was exposed to the coordinator. Root inspections independently read committed bytes and checked citations.\n\nEvent order is recorded in ../evidence/assignment-events.jsonl. Ordinals describe observed dispatch and native result arrival, not elapsed time. All workers are source-only and return native text; only the coordinator writes case evidence. No worker isolated-write observation is claimed. Pre-dispatch assignments use pending identity placeholders because actual identities arrive from spawn; later binding events and receipt name actual workers.\n\nNo todo tool is exposed. The local checklist is the reduced binding. It was saved after initial investigation dispatch, so required before-fanout checklist ordering was not fully met. The initial how exploration also preceded the Swarm skill read and has no retroactively asserted Swarm receipt. The later two-slice shipping prerequisite partition was framed before dispatch and has its actual blocked method receipt. No Arena was invoked and no Arena receipt is fabricated.\n\nEarlier ephemeral-session records were not edited or searched. No source/product files were changed, no new commits created, no external services used, no installation, configuration, schedule, post, push or publishing action occurred. Initial exploratory root command returns remain in the native transcript; canonical source reads, later commands and worker captures are persisted locally. Not every early shell wrapper has a separate machine-readable raw return file.\n\nIndependent verifier results are BLOCKED. Requested PASS and PASS+NOTES were not assigned as outcomes. The Swarm receipt covers two prerequisite-inspection slices only. All dependent real-head rebase, changed/unchanged patch, build-noise, simulator merge and frontier-wake variants remain unexecuted with exact gates in the response. Conditional state recommendations are not local simulation observations. The first absent exact-revision prerequisite prevents the authorized simulator branch from becoming a real Git case.\n\n## Actual response\n\n## Shipping observation\n\nThe verified run is empty. No observed ceiling exists. `/root/verifier_101` and `/root/verifier_102` independently returned BLOCKED at the exact-revision gate. No PR was armed or merged. No forge was contacted.\n\n| Requested PR | Observed verifier | Actual verdict | Missing evidence |\n|---|---|---|---|\n| 101 | `/root/verifier_101` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 102 | `/root/verifier_102` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 103 | None | No verdict | PR record and exact revisions. |\n| 104 | None | No actual verdict | The scenario's passing status is not an observed worker result. |\n\nThe committed `forge.json` has PRs 1 and 2 with symbolic branch labels. Mapping them to 101 and 102 would invent identity. Creating the requested Git stack would require new commits, which the current user forbids. The local merge simulator branch cannot satisfy its real-Git input prerequisite and was not run. Source: `committed-inputs/forge.json`, captured in `../evidence/inspected-input-bytes.json`.\n\nUnder the supplied hypothetical PASS for 101 and PASS+NOTES for 102, with no verdict for 103, the conditional ceiling is 102. PASS+NOTES counts. A passing 104 cannot bypass 103. This is a rule applied to supplied scenario labels, not observed eligibility or a landable stack. CI and bot approvals cannot supply either missing independent verdict.\n\n## Variants and execution limits\n\n| Variant | Actual action or observation | Remaining gate |\n|---|---|---|\n| Comments and merge denied | Kept both independent BLOCKED findings locally. No comment or merge call. | External writes remain prohibited throughout this task. |\n| Exact current-trunk rebase | Inspected single-root Git history. No PR101 branch/trunk identities exist. No rebase or commit. | Exact old parent/head and current trunk required before rebase or patch comparison. |\n| Substantive patch changed | No verdict/current pair exists to compare. | A changed patch requires renewed independent real-surface verification. It cannot inherit a verdict. |\n| Patch unchanged | No stable patch-id can be calculated for an absent pair. | If unchanged is later proven, retain only the code verdict and refresh current-head CI and mergeability. |\n| Tests/docs/lint-only noisy builds | No lanes, verdict/current heads or build outputs exist. No fake builds generated. | Each lane needs two verdict-SHA builds and one current-head build, per-difference noise classification with file evidence, fresh checks and review. An embedded SHA can be noise; unexplained differences cannot. |\n| Dev-server lane without build output | No lane available. No reuse claim. | Rerun that lane. Missing build output cannot prove equivalence. |\n| Authorized local one-at-a-time merge | No simulator merge performed because real-head prerequisite is absent. No authorization was inferred for external merging. | Only after an exact local stack exists may a simulator act on its own named state. Its success still would not prove a forge merge. |\n| Frontier wakes | No active-forge read or watcher event exists. State distinctions below are conditional instructions only. | Exact pins, working setup and authorized fixture runtime are missing. |\n| After merge | No merge observed, no trunk fetch or descendant retarget occurred. | Confirm active-forge merge and merged SHA in fetched trunk, then recompute the new bottom's exact base/head, patch-id, checks and ceiling. |\n| User stop or exhausted budget | No watch loop began. | No unattended continuation was registered. Stop, unavailable reads or exhausted carried budget end the invocation safely. |\n\n## Frontier state distinctions\n\nThese are the read Shipping contract's recommendations. They are not fabricated watcher observations.\n\n| Supplied state category | Shipping decision |\n|---|---|\n| READY | Wake to read active forge. Does not establish merge. |\n| autoMergeRequest present | One GitHub PR may be armed. Does not establish merge, descendant readiness or Origin arming. |\n| Queued WAITING with merge-queue reason | Non-terminal. Shipping continues within its finite budget; Babysit instead reports merge-ready and stops its watcher. |\n| BLOCKED while checks are pending or auto-merge armed | Keep pending. Do not label hard failure from BLOCKED alone. |\n| CLOSED with no mergedAt | Closed-unmerged hard failure. |\n| Required FAILURE or CANCELLED blocking merge, no auto-merge pending | Hard failure under the Shipping rule. |\n| UNSTABLE or DIRTY, no auto-merge pending | Hard failure under the Shipping rule. |\n| state MERGED or non-null mergedAt | Inspect trunk inclusion before advancing. No automatic child retarget assumed. |\n| Query error, missing pins or expired budget | Stop or bounded retry within remaining budget. Merge outcome stays unknown. |\n\n## Helper and compiler proof\n\n`bun --no-install <exact-package>/skills/poteto-mode/scripts/watch-pr/watch-pr --help` actually ran. Bootstrap exited 1 before CLI parsing because `scripts/node_modules/commander/package.json` is absent. The captured stderr is in `../evidence/watcher-setup-help.json`. This is the separate setup gate, not a watcher status, schemaVersion 1 event or readiness result. No dependency installation or bootstrap bypass occurred. Required pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. The available TypeScript 5.9.3 does not satisfy the watcher's 7.0.2 pin.\n\nThe installed compiler `/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js` ran through Bun. `--version` reported 5.9.3 with exit 0. `--noEmit --strict --target esnext --module esnext --skipLibCheck <exact-package>/skills/poteto-mode/scripts/watch-pr/types.ts` exited 0 with no output. This checks those type definitions only. It does not prove helper startup, forge integration or any PR passed.\n\nNo valid watcher invocation could be bound because PR heads are absent. I did not substitute the task-input SHA as a PR head. A future bounded attempt must freeze [101,102,103,104], pin every watched full head, use explicit owner/repo and carry at most 10 snapshot attempts and 600 seconds for the invocation. No hard wall-clock or wake binding was exercised here. No watcher event or service success count was fabricated.\n\nThe active forge remains none for this run. User scope prohibits resolution through an external service. A built-in GitHub edit tool may be exposed, but its availability supplies neither permission nor matching fixture identity. No retarget or CLI bypass was attempted.\n\n## Next gap\n\nSupply exact existing Git heads/trunk and their original source/build artifacts without requiring new commits, or explicitly revise the no-new-commits constraint for a later isolated synthetic setup. Then independently verify the real surface. Missing helper dependencies and actual forge controls still block a real landing run. This run ends at that first evidence gap and preserves the actual verifier results.\n\n\n## Tools, outputs and exit status\n\nEach linked command JSON preserves its exact argv, stdout, stderr, signal and actual child exit status. The Bun capture wrapper exits 0 even when the recorded child fails. Read the child exitStatus. Shell metadata and native worker completion have no fabricated command exit code. Required source-file cat operations exited 0. Compiler typecheck exited 0. Watcher bootstrap exited 1 before event generation.\n\n- [../evidence/inspected-input-bytes.json](../evidence/inspected-input-bytes.json)\n- [../evidence/current-head.json](../evidence/current-head.json)\n- [../evidence/current-log.json](../evidence/current-log.json)\n- [../evidence/current-diff.json](../evidence/current-diff.json)\n- [../evidence/watcher-setup-help.json](../evidence/watcher-setup-help.json)\n- [../evidence/compiler-version.json](../evidence/compiler-version.json)\n- [../evidence/compiler-types.json](../evidence/compiler-types.json)\n- [method-receipt.json](method-receipt.json)\n- [inspection.md](inspection.md)\n\nWorker assignment and result inventory is [../evidence/worker-records.json](../evidence/worker-records.json). All native result captures and full assignments for this case are in this directory. Detailed later root command order is [../evidence/command-order.jsonl](../evidence/command-order.jsonl). Readbacks and file hashes are [../evidence/artifact-readback.json](../evidence/artifact-readback.json).\n\n## Attention\n\nreviewed by unknown\n\nIndependent artifact inspector /root/artifact_inspector reported no additional concrete factual issues after checking citations, all eight result capture pairs, receipt hashes, compiler and bootstrap outputs, continuation readback and report links. Its native return is ../evidence/artifact-inspector.native-result.md. No different actual model family was observed, so the Show Me Your Work cross-model audit is blocked. The current run's full transcript export is not exposed through a scoped file binding. The visible native events and saved records support bounded inspection, not a complete exported-transcript audit. The missing prerequisites above remain open. No host grade is assigned.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/checklist.md",
      "sha256": "9c3a12f27c7d84330ed9e2ba71e1f899c0ab40dbbae78a20150118d3f10e8c90",
      "bytes": 7444,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "Reduced local checklist binding. Saved after initial dispatch; no before-dispatch ordering claim. Steps below are copied verbatim from the exact installed contract.\n\n1. **Resolve the forge, then verify every PR independently.** GitHub CLI (`gh`) is the default. If `command -v origin` succeeds and Origin can resolve the repository, use `origin pr ...` for PR view, watch, edit, and merge operations. Otherwise stay on `gh` and record the fallback. Never require Graphite (`gt`). One subagent per PR, not batched, each an independently spawned worker through an observed host binding, each exercising the real surface with the matching exposed and authorized control skill against exact parent versus head revisions. The upstream examples `control-ui` and `control-cli` are external skills, not bundled bindings. Missing control capability leaves real-surface verification blocked. Use inherited model roles unless current supported selection and actual results are observed. Each returns `PASS`, `PASS+NOTES` or `FAIL`, with verifier identity, exact revisions and method artifacts, and posts that verdict on its own PR when comment authorization exists. Otherwise retain the verdict locally and report that posting is blocked. A missing worker permits local sequential recommendations as reduced capability, never an independent verdict or a landable run. Safe means a verdict from an agent that did not write the code. CI green is not a verdict, and an approving bot review is not a verdict.\n\n2. **Land only the contiguous verified run rooted at the bottom.** Walk up from the lowest unmerged PR and stop at the first one without a passing verdict, where both `PASS` and `PASS+NOTES` pass. A verified PR sitting above an unverified one is not landable. Report the ceiling as a PR number and say what breaks the chain.\n\n3. **Re-check that each verdict still describes the patch.** Record the verdict head SHA, base SHA, and stable `git patch-id` of that PR's base-to-head diff. A rebase or base retarget rewrites SHAs and can silently invalidate a verdict without touching a check. Before landing a PR, read and record its current exact head SHA and base SHA, resolve the base-to-head diff at those revisions, and compare the recorded patch-id with its current base-to-head patch-id. Re-read the head and base immediately before the authorized merge or arm action. If either moved since the freshness check, stop and repeat that check. When the two patches differ only in tests, docs, or lint config, build what each lane ran. Build it twice at the verdict SHA and once at the current head. A difference is noise if the two builds at the verdict SHA also show it, or if it is an embedded commit SHA. Judge each difference, not each file, and report each kind of noise with its files. If only noise differs, that lane's result stays valid, and checks and a review of the change run fresh. Do not reuse a lane result from a dev server or from anything else with no build output. Rerun that lane. Re-verify anything else when the patch changed. When it did not, keep the code verdict but re-run mergeability and CI at the current head. Never use matching commit messages or a green check from an older SHA as a substitute.\n\n4. **Prepare only the bottom PR.** Fetch current trunk. Rebase the lowest verified branch onto the exact trunk tip when needed, push it, and retarget only that PR to trunk through an exposed built-in PR tool when present, as required by [opening a PR](opening-a-pr.md). Without that tool use `origin pr edit <pr> --base <trunk>` or `gh pr edit <pr> --base <trunk>`. Re-run step 3 after the push. Do not retarget, arm, or merge descendants yet.\n\n5. **Land one PR at a time.** If the bottom PR is mergeable now, squash it with `origin pr merge <pr> --squash` or `gh pr merge <pr> --squash`. If requirements are still running and the user asked for merge-when-ready, arm only that PR with `origin pr merge <pr> --squash --auto` or `gh pr merge <pr> --squash --auto`. Origin's `--auto` is Origin merge-when-ready. GitHub's `--auto` is GitHub auto-merge. Wait for that PR to merge before preparing the next one.\n\n6. **Do not read GitHub `autoMergeRequest` as stack readiness.** At most it says GitHub auto-merge was requested for one GitHub PR. It does not prove Origin merge-when-ready is armed, that a descendant is queued, that a patch verdict is current, or that the contiguous stack is safe. Confirm the active forge's state for the current bottom PR, and say that the state is unknown if the active forge cannot report it.\n\n7. **Recompute after every merge.** Fetch trunk, confirm the merged SHA is present, drop the merged PR from the frozen bottom-to-top list, and inspect the new bottom PR's base, head, checks, and patch-id. A host may retarget a child automatically, but do not assume it did. Repeat steps 3 through 6 for that one PR. Independent work stays outside this chain and ships on its own.\n\n8. **Watch the current frontier until it merges or fails. Do not mutate the queue around it.** With Origin, use `origin pr view <pr> --checks --comments` and `origin pr checks <pr> --watch`, then re-read the PR until it reports merged or blocked. With GitHub, use the read-only [watcher](../scripts/watch-pr/watch-pr) from the package root as `bun --no-install skills/poteto-mode/scripts/watch-pr/watch-pr --owner <owner> --repo <repo> --queued-stack --stack-prs <bottom> --head <bottom=full-40-character-head> --max-polls <remaining-count> --timeout <remaining-seconds>` only as an event wake and poll `gh pr view <pr> --json state,mergedAt,mergeStateStatus,statusCheckRollup,autoMergeRequest` after each wake, ignoring `READY` until `mergedAt` is non-null or `state` is `MERGED`. Only then run step 7. Hard-fail only when `state` is `CLOSED` with no `mergedAt`, a required check concludes `FAILURE` or `CANCELLED` and blocks merge after auto-merge is no longer pending, or `mergeStateStatus` is `UNSTABLE` or `DIRTY` with no auto-merge pending. `BLOCKED` while checks are pending or auto-merge is armed is not failure. Do not use Babysit's queued `WAITING`/`merge-queue` stop condition here. Hold the watch through the observed authorized loop or wake binding within the declared budget. Do not add a second sleep loop. The watcher emits NDJSON schemaVersion 1 events. Inspect kind, terminal and reason, never exit 0 alone. Queued mode emits non-terminal `WAITING` with `reason.kind` equal to `merge-queue`, not `READY`. Terminal helper blockers or budget exhaustion require inspection of the active forge, not an invented merged or hard-failed state. The [bootstrap](../scripts/bootstrap.ts) checks pinned dependencies and fails setup-required; never install or bypass it. [Helper setup](../../../docs/testing/helper-setup.md) is separately authorized. For Origin, use a finite bound and an observed stop binding for check watching, or bounded view snapshots when an unbounded watch cannot be stopped. Report each merge and the new ceiling. If the queue stalls, diagnose before mutating.\n\n9. **Stop at the ceiling.** When the verified run is merged, report what landed, what the next unverified PR is, and what verifying it would take. Extending the run is a new pass through step 1.\n\nDisposition\n\nIndependent prerequisite verifier results inspected. Shipping steps 2 through 9 remain blocked at missing exact revisions. Conditional recommendations do not substitute for runtime. Watcher setup failure preserved.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/inspection.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/inspection.md",
      "sha256": "9a2f73ed6aabe2c8710b6e941e56889ca6c8f2543551064a50d280fa3ff030d5",
      "bytes": 1977,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "The coordinator inspected both complete native verifier findings and reread the committed forge source. Assignment IDs, input SHA, sample count, sample definition and method order match. Worker `/root/verifier_101` inspected the exact blob; `/root/verifier_102` inspected the same committed source and its fields. Neither authored the seed. Both returned BLOCKED, and neither result was promoted to PASS or PASS+NOTES.\n\nThe fixture contains only PRs 1 and 2. It has no records 101..104, no exact trunk tip for that stack, no verdict head/base SHAs, no stable patch IDs and no parent-versus-head build or control artifacts. The input revision identifies the fixture repository only. It is not a PR101 or PR102 head.\n\nThe receipt records a two-slice prerequisite-inspection partition. It does not claim successful real-surface shipping verification. Both shipping slices remain gaps. Initial how explorers used the how route before the Swarm contract was read. That earlier batch is recorded as routed exploration and is not retroactively claimed as a compliant Swarm run.\n\nUnknown actual models leave diversity unverified. Worker assignments initially used a pending identity placeholder because spawn identities are returned only after dispatch. Spawn-return events bind the observed identities. Coordinator capture owns persisted native results; workers did not write output files. This is a disclosed departure from a strict pre-known worker output-owner field, not an isolated-write observation.\n\nRaw spawn returns contain only task_name. Native completion text was copied into Markdown captures while this run was active, then wrapped in coordinator-created JSON envelopes. The envelopes are capture metadata, not additional raw fields returned by collaboration. No hidden runtime model, telemetry, timing or tool-call trace is invented. The current transcript retains actual worker tool calls; the coordinator does not claim a separate worker raw-tool export was exposed.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/method-receipt.json",
      "sha256": "c3d014e20ef97bcecd7508bd32da15f5e2296af6e9c890970f90a9e8699f1099",
      "bytes": 4636,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"swarm\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageCommitObservation\": \"supplied freeze; installed tree lacks Git metadata; no independent commit match claimed\",\n  \"assignments\": [\n    {\n      \"id\": \"verifier-101\",\n      \"workerId\": \"/root/verifier_101\",\n      \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n      \"outputOwner\": \"/root/verifier_101\",\n      \"outputPath\": \"contiguous-verified-stack/verifier-101.native-result.md\",\n      \"role\": \"poteto-agent independent non-author PR verifier\",\n      \"status\": \"blocked\",\n      \"startedOrder\": 13,\n      \"completedOrder\": 15,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"requestedEffort\": \"inherit-parent\",\n      \"actualEffort\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n        \"order\": [\n          \"read source bytes\",\n          \"check identity and exact revisions\",\n          \"check surface artifacts\",\n          \"return blocked or evidence\"\n        ]\n      },\n      \"taskArtifact\": \"contiguous-verified-stack/verifier-101.task.txt\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n        \"order\": [\n          \"read source bytes\",\n          \"check identity and exact revisions\",\n          \"check surface artifacts\",\n          \"return blocked or evidence\"\n        ]\n      },\n      \"outputSha256\": \"97493e469139a8a1c86684e2a1ad7ddc8c889937b7058f6c96ac3c3a9c65d345\",\n      \"spawnReturnArtifact\": \"contiguous-verified-stack/verifier-101.spawn-return.json\",\n      \"nativeResultArtifact\": \"contiguous-verified-stack/verifier-101.native-result.json\"\n    },\n    {\n      \"id\": \"verifier-102\",\n      \"workerId\": \"/root/verifier_102\",\n      \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n      \"outputOwner\": \"/root/verifier_102\",\n      \"outputPath\": \"contiguous-verified-stack/verifier-102.native-result.md\",\n      \"role\": \"poteto-agent independent non-author PR verifier\",\n      \"status\": \"blocked\",\n      \"startedOrder\": 14,\n      \"completedOrder\": 16,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"requestedEffort\": \"inherit-parent\",\n      \"actualEffort\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n        \"order\": [\n          \"read source bytes\",\n          \"check identity and exact revisions\",\n          \"check surface artifacts\",\n          \"return blocked or evidence\"\n        ]\n      },\n      \"taskArtifact\": \"contiguous-verified-stack/verifier-102.task.txt\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n        \"order\": [\n          \"read source bytes\",\n          \"check identity and exact revisions\",\n          \"check surface artifacts\",\n          \"return blocked or evidence\"\n        ]\n      },\n      \"outputSha256\": \"16713517c69863a5d139826a4bca26daa70e61754a30e6b2aa67cdd8e201fed5\",\n      \"spawnReturnArtifact\": \"contiguous-verified-stack/verifier-102.spawn-return.json\",\n      \"nativeResultArtifact\": \"contiguous-verified-stack/verifier-102.native-result.json\"\n    }\n  ],\n  \"reviewArtifact\": \"contiguous-verified-stack/inspection.md\",\n  \"reviewedBy\": \"/root\",\n  \"declaredOrder\": [\n    \"verifier-101\",\n    \"verifier-102\"\n  ],\n  \"declaredOrderArtifact\": \"contiguous-verified-stack/swarm-frame.md\",\n  \"partition\": {\n    \"requiredSlices\": [\n      \"101\",\n      \"102\"\n    ],\n    \"results\": {\n      \"101\": \"verifier-101\",\n      \"102\": \"verifier-102\"\n    },\n    \"gaps\": [\n      \"101 shipping verification blocked: absent exact revisions and surface artifacts\",\n      \"102 shipping verification blocked: absent exact revisions and surface artifacts\"\n    ]\n  },\n  \"race\": null,\n  \"cancelled\": [],\n  \"quarantined\": [],\n  \"failureExercises\": [],\n  \"limits\": [\n    \"prerequisite inspection only\",\n    \"no real-surface verification\",\n    \"no passing verifier verdicts\",\n    \"no model diversity observation\",\n    \"no isolated worker writes; native outputs captured by coordinator\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/response.md",
      "sha256": "7e90ce2cdb1ff4b1499ffe8c62607f36f06a76feaf60f9d9da206ac6b782905f",
      "bytes": 7035,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "## Shipping observation\n\nThe verified run is empty. No observed ceiling exists. `/root/verifier_101` and `/root/verifier_102` independently returned BLOCKED at the exact-revision gate. No PR was armed or merged. No forge was contacted.\n\n| Requested PR | Observed verifier | Actual verdict | Missing evidence |\n|---|---|---|---|\n| 101 | `/root/verifier_101` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 102 | `/root/verifier_102` | BLOCKED | PR record, exact base/head, stable patch-id and parent/head control artifacts. |\n| 103 | None | No verdict | PR record and exact revisions. |\n| 104 | None | No actual verdict | The scenario's passing status is not an observed worker result. |\n\nThe committed `forge.json` has PRs 1 and 2 with symbolic branch labels. Mapping them to 101 and 102 would invent identity. Creating the requested Git stack would require new commits, which the current user forbids. The local merge simulator branch cannot satisfy its real-Git input prerequisite and was not run. Source: `committed-inputs/forge.json`, captured in `../evidence/inspected-input-bytes.json`.\n\nUnder the supplied hypothetical PASS for 101 and PASS+NOTES for 102, with no verdict for 103, the conditional ceiling is 102. PASS+NOTES counts. A passing 104 cannot bypass 103. This is a rule applied to supplied scenario labels, not observed eligibility or a landable stack. CI and bot approvals cannot supply either missing independent verdict.\n\n## Variants and execution limits\n\n| Variant | Actual action or observation | Remaining gate |\n|---|---|---|\n| Comments and merge denied | Kept both independent BLOCKED findings locally. No comment or merge call. | External writes remain prohibited throughout this task. |\n| Exact current-trunk rebase | Inspected single-root Git history. No PR101 branch/trunk identities exist. No rebase or commit. | Exact old parent/head and current trunk required before rebase or patch comparison. |\n| Substantive patch changed | No verdict/current pair exists to compare. | A changed patch requires renewed independent real-surface verification. It cannot inherit a verdict. |\n| Patch unchanged | No stable patch-id can be calculated for an absent pair. | If unchanged is later proven, retain only the code verdict and refresh current-head CI and mergeability. |\n| Tests/docs/lint-only noisy builds | No lanes, verdict/current heads or build outputs exist. No fake builds generated. | Each lane needs two verdict-SHA builds and one current-head build, per-difference noise classification with file evidence, fresh checks and review. An embedded SHA can be noise; unexplained differences cannot. |\n| Dev-server lane without build output | No lane available. No reuse claim. | Rerun that lane. Missing build output cannot prove equivalence. |\n| Authorized local one-at-a-time merge | No simulator merge performed because real-head prerequisite is absent. No authorization was inferred for external merging. | Only after an exact local stack exists may a simulator act on its own named state. Its success still would not prove a forge merge. |\n| Frontier wakes | No active-forge read or watcher event exists. State distinctions below are conditional instructions only. | Exact pins, working setup and authorized fixture runtime are missing. |\n| After merge | No merge observed, no trunk fetch or descendant retarget occurred. | Confirm active-forge merge and merged SHA in fetched trunk, then recompute the new bottom's exact base/head, patch-id, checks and ceiling. |\n| User stop or exhausted budget | No watch loop began. | No unattended continuation was registered. Stop, unavailable reads or exhausted carried budget end the invocation safely. |\n\n## Frontier state distinctions\n\nThese are the read Shipping contract's recommendations. They are not fabricated watcher observations.\n\n| Supplied state category | Shipping decision |\n|---|---|\n| READY | Wake to read active forge. Does not establish merge. |\n| autoMergeRequest present | One GitHub PR may be armed. Does not establish merge, descendant readiness or Origin arming. |\n| Queued WAITING with merge-queue reason | Non-terminal. Shipping continues within its finite budget; Babysit instead reports merge-ready and stops its watcher. |\n| BLOCKED while checks are pending or auto-merge armed | Keep pending. Do not label hard failure from BLOCKED alone. |\n| CLOSED with no mergedAt | Closed-unmerged hard failure. |\n| Required FAILURE or CANCELLED blocking merge, no auto-merge pending | Hard failure under the Shipping rule. |\n| UNSTABLE or DIRTY, no auto-merge pending | Hard failure under the Shipping rule. |\n| state MERGED or non-null mergedAt | Inspect trunk inclusion before advancing. No automatic child retarget assumed. |\n| Query error, missing pins or expired budget | Stop or bounded retry within remaining budget. Merge outcome stays unknown. |\n\n## Helper and compiler proof\n\n`bun --no-install <exact-package>/skills/poteto-mode/scripts/watch-pr/watch-pr --help` actually ran. Bootstrap exited 1 before CLI parsing because `scripts/node_modules/commander/package.json` is absent. The captured stderr is in `../evidence/watcher-setup-help.json`. This is the separate setup gate, not a watcher status, schemaVersion 1 event or readiness result. No dependency installation or bootstrap bypass occurred. Required pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. The available TypeScript 5.9.3 does not satisfy the watcher's 7.0.2 pin.\n\nThe installed compiler `/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js` ran through Bun. `--version` reported 5.9.3 with exit 0. `--noEmit --strict --target esnext --module esnext --skipLibCheck <exact-package>/skills/poteto-mode/scripts/watch-pr/types.ts` exited 0 with no output. This checks those type definitions only. It does not prove helper startup, forge integration or any PR passed.\n\nNo valid watcher invocation could be bound because PR heads are absent. I did not substitute the task-input SHA as a PR head. A future bounded attempt must freeze [101,102,103,104], pin every watched full head, use explicit owner/repo and carry at most 10 snapshot attempts and 600 seconds for the invocation. No hard wall-clock or wake binding was exercised here. No watcher event or service success count was fabricated.\n\nThe active forge remains none for this run. User scope prohibits resolution through an external service. A built-in GitHub edit tool may be exposed, but its availability supplies neither permission nor matching fixture identity. No retarget or CLI bypass was attempted.\n\n## Next gap\n\nSupply exact existing Git heads/trunk and their original source/build artifacts without requiring new commits, or explicitly revise the no-new-commits constraint for a later isolated synthetic setup. Then independently verify the real surface. Missing helper dependencies and actual forge controls still block a real landing run. This run ends at that first evidence gap and preserves the actual verifier results.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/save-receipt.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/save-receipt.mjs",
      "sha256": "35d97cab23724e9c07005137de645b408c5188be9fa9660ecadc0c242ee64365",
      "bytes": 1292,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "import{readFileSync,writeFileSync}from'node:fs';\nconst assignments=JSON.parse(readFileSync('evidence/worker-records.json','utf8')).filter(x=>x.id.startsWith('verifier-'));\nconst r={schemaVersion:1,kind:'swarm',inputRevision:'ec045fadb47b598147052035b7eb1a9c47813156',packageCommit:'f4623636a287bea2aa79c4b2234a53d20a5f193c',packageCommitObservation:'supplied freeze; installed tree lacks Git metadata; no independent commit match claimed',assignments,reviewArtifact:'contiguous-verified-stack/inspection.md',reviewedBy:'/root',declaredOrder:['verifier-101','verifier-102'],declaredOrderArtifact:'contiguous-verified-stack/swarm-frame.md',partition:{requiredSlices:['101','102'],results:{'101':'verifier-101','102':'verifier-102'},gaps:['101 shipping verification blocked: absent exact revisions and surface artifacts','102 shipping verification blocked: absent exact revisions and surface artifacts']},race:null,cancelled:[],quarantined:[],failureExercises:[],limits:['prerequisite inspection only','no real-surface verification','no passing verifier verdicts','no model diversity observation','no isolated worker writes; native outputs captured by coordinator']};\nwriteFileSync('contiguous-verified-stack/method-receipt.json',JSON.stringify(r,null,2));console.log(JSON.stringify(r,null,2));\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/supplied-input.json",
      "sha256": "ac8210f55b619f7ce12ce936d46cc7f5de165c6af0352e6633c5623810818ca5",
      "bytes": 7170,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"contract\": {\n    \"id\": \"contiguous-verified-stack\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/playbooks/babysit.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n      \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n      \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\"\n    ],\n    \"prompt\": \"Use inert local fixtures for a frozen stack 101,102,103,104. Independent verifier A passes 101 and verifier B returns PASS+NOTES for 102; 103 lacks a verdict and 104 passes. Rebase 101 to exact current trunk, include a changed patch and a tests/docs/lint-only patch with noisy builds, deny comments and merge first, then model authorized one-at-a-time merging and frontier wake states. Do not contact a forge.\",\n    \"requirements\": [\n      \"Record exact verdict head SHA, base SHA, stable patch-id, independent non-author verifier identity and parent-versus-head real-surface artifacts per PR.\",\n      \"Ceiling is PR 102; 104 cannot bypass 103. PASS+NOTES passes; CI and bot approvals do not.\",\n      \"Changed substantive patch requires re-verification. Unchanged patch retains code verdict but refreshes CI and mergeability at current head.\",\n      \"For tests/docs/lint-only differences build each lane twice at verdict SHA and once at current head; classify each noise kind with files, refresh checks and review; dev-server lanes without build output rerun.\",\n      \"Prepare only bottom against exact fetched trunk, use built-in retarget tool if exposed, recheck after push, then squash or arm only explicitly authorized bottom and await confirmed merge.\",\n      \"Read active-forge state after every wake; READY and autoMergeRequest never prove merge. Preserve pending BLOCKED, closed-unmerged and failed/cancelled required checks or UNSTABLE/DIRTY with no auto-merge pending distinctions.\",\n      \"After merge fetch trunk, confirm merged SHA present, recompute base/head/checks/patch-id and ceiling, never assume automatic retarget.\",\n      \"Use actual watcher pins, finite budgets, schemaVersion 1 events and separate setup gate; stop safely on missing capability, user stop or exhaustion.\"\n    ],\n    \"expectedFull\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n    \"expectedReduced\": \"Without workers or real-surface tools, produce local sequential recommendations with independence unverified and no landable run. Without comments retain independent verdict artifacts locally. Without loop support use bounded foreground snapshots, disclose no unattended watch; denied merges produce only the authorized merge plan.\",\n    \"expectedBlocked\": \"Missing exact revisions, stable patch identity, independent verifier artifacts, build output for reused lanes, forge access, helper dependencies or merge authorization blocks the affected verification or landing. Stop at first gap or unknown action outcome; perform no external writes.\",\n    \"forbiddenClaims\": [\n      \"CI green or bot approval is an independent verdict.\",\n      \"Sequential role switching supplies independent per-PR verification.\",\n      \"Requested model or documented tool establishes observed support.\",\n      \"A verified descendant above a gap is landable.\",\n      \"Matching commit messages or old green checks prove current patch safety.\",\n      \"READY, WAITING, exit 0 or autoMergeRequest proves merged or whole-stack readiness.\",\n      \"Pending BLOCKED alone is hard failure.\",\n      \"Setup, verdict posting, push, retarget or auto-merge is implicitly authorized.\",\n      \"Structural fixture validation proves host parity or actual merges.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\"\n  },\n  \"caseId\": \"contiguous-verified-stack\",\n  \"baselineBatch\": \"batch-07\",\n  \"baselineState\": \"active-or-not-yet-finished\",\n  \"baselineGrade\": null,\n  \"selectionReason\": \"Registry pass requires workers\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/shipping.md\",\n    \"skills/poteto-mode/playbooks/babysit.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"skills/poteto-mode/scripts/bootstrap.ts\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/shipping.json\",\n  \"expectedFullUnchanged\": \"Fixture observation selects only contiguous 101 and 102, preserves independent verdict artifacts, invalidates changed patches, applies build-noise procedure, and models exactly one authorized bottom merge at a time with active-forge confirmation and trunk inclusion before advancement. Actual host full support additionally requires observed workers and real-surface tools.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/forge.json\"\n  ],\n  \"taskPayload\": \"Root prepares local frozen stack records 101/102/103/104 backed by real case-local Git heads/trunk. Independent verifier A inspects 101 and verifier B inspects 102; retain actual PASS/PASS+NOTES findings only if earned. Leave 103 without verdict and 104 out of contiguous eligibility. Inspect changed-patch invalidation and tests/docs/lint noisy-build branch. Model one authorized bottom merge at a time only in the local simulator, with explicit simulator action/destination state; contact no forge. Full real-surface host support remains unmet without actual matching forge controls.\",\n  \"missingPrerequisites\": [\n    \"Specific 101..104 input records are missing from generic forge.json and must be prepared\",\n    \"Two actual verifier outcomes cannot be predeclared\",\n    \"Local simulator proves modeled sequencing only; real-surface branch remains BLOCKED\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/babysit.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/cli.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/types.ts\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\"\n  ]\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/swarm-frame.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/swarm-frame.md",
      "sha256": "e11bd8b58d53c7e21bdeba2507dd0711e210ab652d04affeadc00185aa7c8c37",
      "bytes": 1142,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "1. Frame\n2. Fan out\n3. Aggregate\n4. Report\n\nDone predicate: two independently inspected prerequisite reports for PR 101 and 102, not invented passing verdicts. Partition with N=2, required slices [101,102], declared dispatch order [verifier-101,verifier-102]. No race, no Arena. Each method has one sample: inspect the committed forge fixture and check for exact parent/head and surface artifacts; order source bytes, identity, prerequisites, verdict. Real verification is blocked if exact revisions are absent. User prohibits new commits and all external services. Each worker returns native text; coordinator alone writes captures in distinct paths. Input revision ec045fadb47b598147052035b7eb1a9c47813156. Actual model unknown, requested inherit-parent.\n\nThroughput checkpoint\n- Blocking first steps. Read shipping, gate sources and permission before dispatch.\n- Independent workstreams. PR 101 and PR 102 prerequisite inspections, separate native outputs.\n- Shared mutable state. None for read-only workers; coordinator owns captures.\n- Smallest safe decomposition. Two workers for two distinct requested independent verifier identities.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-101.assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.assignment.json",
      "sha256": "8f8c0694ebcc71f47f9a0bdae8b4d7e75f859a37239b54ed3401886b8615d425",
      "bytes": 1354,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"id\": \"verifier-101\",\n  \"scope\": \"Inspect PR 101 verification prerequisites using ONLY committed-inputs/forge.json at inputRevision. It has PRs 1/2, no 101..104 and no full SHA heads. Do not map those records or invent source commits. Independently confirm gap. Exact PR base/head are absent; stop verification at that gate. Return BLOCKED unless real evidence exists. No predeclared PASS or PASS+NOTES.\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"role\": \"poteto-agent independent non-author PR verifier\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.md\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/supplied-input.json\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  },\n  \"resultMethodRequired\": true\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.json",
      "sha256": "94ceb6138c1dadea8f0e083a4d0688433e53b69b2ad91cd4adf4758b868dd7af",
      "bytes": 1773,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"messageType\": \"FINAL_ANSWER\",\n  \"taskName\": \"/root\",\n  \"sender\": \"/root/verifier_101\",\n  \"payload\": \"BLOCKED.\\n\\nAssignment `verifier-101`. Worker `/root/verifier_101`. InputRevision `ec045fadb47b598147052035b7eb1a9c47813156`.\\n\\nI independently read `committed-inputs/forge.json` using `git show` at that revision. Git resolved its blob as `deeeace8830b688700c402b82f1af325b2510416`.\\n\\nThe source contains PRs 1 and 2 only. Their base/head values are branch labels. PR 101, its exact base/head SHAs, stable patch identity, and real-surface verification artifacts are absent. Those records cannot establish PR 101’s identity or verification.\\n\\n```json\\n{\\n  \\\"assignmentId\\\": \\\"verifier-101\\\",\\n  \\\"inputRevision\\\": \\\"ec045fadb47b598147052035b7eb1a9c47813156\\\",\\n  \\\"terminalStatus\\\": \\\"blocked\\\",\\n  \\\"verdict\\\": \\\"BLOCKED\\\",\\n  \\\"requestedModel\\\": \\\"inherit-parent\\\",\\n  \\\"actualModel\\\": \\\"unknown\\\",\\n  \\\"requestedEffort\\\": \\\"inherit-parent\\\",\\n  \\\"actualEffort\\\": \\\"unknown\\\",\\n  \\\"resultMethod\\\": {\\n    \\\"sampleCount\\\": 1,\\n    \\\"sampleDefinition\\\": \\\"one committed source prerequisite inspection; not a real-surface lane\\\",\\n    \\\"order\\\": [\\n      \\\"read source bytes\\\",\\n      \\\"check identity and exact revisions\\\",\\n      \\\"check surface artifacts\\\",\\n      \\\"return blocked or evidence\\\"\\n    ]\\n  }\\n}\\n```\\n\\nProve It Works required direct source inspection and prevented substituting fixture checks for a passing verdict. Unslop shaped this report. No writes, builds, commits, network operations, configuration changes, or nested delegation occurred.\\n\\nPR 101 remains the verification gap. Exact base/head revisions, the corresponding diff and stable patch-id, and authorized real-surface evidence are required before verification can proceed.\\n\"\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.md",
      "sha256": "97493e469139a8a1c86684e2a1ad7ddc8c889937b7058f6c96ac3c3a9c65d345",
      "bytes": 1580,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "BLOCKED.\n\nAssignment `verifier-101`. Worker `/root/verifier_101`. InputRevision `ec045fadb47b598147052035b7eb1a9c47813156`.\n\nI independently read `committed-inputs/forge.json` using `git show` at that revision. Git resolved its blob as `deeeace8830b688700c402b82f1af325b2510416`.\n\nThe source contains PRs 1 and 2 only. Their base/head values are branch labels. PR 101, its exact base/head SHAs, stable patch identity, and real-surface verification artifacts are absent. Those records cannot establish PR 101’s identity or verification.\n\n```json\n{\n  \"assignmentId\": \"verifier-101\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"terminalStatus\": \"blocked\",\n  \"verdict\": \"BLOCKED\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  }\n}\n```\n\nProve It Works required direct source inspection and prevented substituting fixture checks for a passing verdict. Unslop shaped this report. No writes, builds, commits, network operations, configuration changes, or nested delegation occurred.\n\nPR 101 remains the verification gap. Exact base/head revisions, the corresponding diff and stable patch-id, and authorized real-surface evidence are required before verification can proceed.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-101.spawn-return.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.spawn-return.json",
      "sha256": "73df4a035f6d21c38cfcaa6e8ec78c48f348442ba1930d029b82f36a217d7ae7",
      "bytes": 34,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\"task_name\":\"/root/verifier_101\"}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-101.task.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.task.txt",
      "sha256": "13a39e15fea4fd0ba5a7e813737b7b5c3622da59eea33445b6902597b90a2fc9",
      "bytes": 2958,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"id\": \"verifier-101\",\n  \"scope\": \"Inspect PR 101 verification prerequisites using ONLY committed-inputs/forge.json at inputRevision. It has PRs 1/2, no 101..104 and no full SHA heads. Do not map those records or invent source commits. Independently confirm gap. Exact PR base/head are absent; stop verification at that gate. Return BLOCKED unless real evidence exists. No predeclared PASS or PASS+NOTES.\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"role\": \"poteto-agent independent non-author PR verifier\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-101.native-result.md\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/supplied-input.json\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  },\n  \"resultMethodRequired\": true\n}\n\nFull role prompt\n# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\n\nRead complete shipping contract at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md. Read-only, no source or output writes, builds, commits, configuration, network or nested workers. Coordinator captures result. Return assignment id, inputRevision and resultMethod matching method above.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-102.assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.assignment.json",
      "sha256": "799ee0f80e53ff2a89040b7e0446ffe61e3cfa72f95d7f878aa2d685a8c707f7",
      "bytes": 1354,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"id\": \"verifier-102\",\n  \"scope\": \"Inspect PR 102 verification prerequisites using ONLY committed-inputs/forge.json at inputRevision. It has PRs 1/2, no 101..104 and no full SHA heads. Do not map those records or invent source commits. Independently confirm gap. Exact PR base/head are absent; stop verification at that gate. Return BLOCKED unless real evidence exists. No predeclared PASS or PASS+NOTES.\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"role\": \"poteto-agent independent non-author PR verifier\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.md\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/supplied-input.json\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  },\n  \"resultMethodRequired\": true\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.json",
      "sha256": "dec5d1fe8caf2c16d009a87ca8125494eed6df3cac977ccca06654f4235232ca",
      "bytes": 1523,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"messageType\": \"FINAL_ANSWER\",\n  \"taskName\": \"/root\",\n  \"sender\": \"/root/verifier_102\",\n  \"payload\": \"BLOCKED for PR 102.\\n\\nAssignment `verifier-102`. Worker `/root/verifier_102`.\\nInputRevision `ec045fadb47b598147052035b7eb1a9c47813156`.\\nRequested model `inherit-parent`. Actual model `unknown`.\\n\\nI inspected `committed-inputs/forge.json` through `git show` at the exact input revision, then checked its fields with Bun.\\n\\nThe source contains only PRs 1 and 2. PR 102 is absent. Their base/head values are symbolic names, not full commit SHAs. The source supplies no PR 102 stable patch identity or real-surface artifacts. I stopped at the exact-revisions gate. No passing verification or landing authorization follows.\\n\\n```json\\n{\\n  \\\"assignmentId\\\": \\\"verifier-102\\\",\\n  \\\"inputRevision\\\": \\\"ec045fadb47b598147052035b7eb1a9c47813156\\\",\\n  \\\"resultMethod\\\": {\\n    \\\"sampleCount\\\": 1,\\n    \\\"sampleDefinition\\\": \\\"one committed source prerequisite inspection; not a real-surface lane\\\",\\n    \\\"order\\\": [\\n      \\\"read source bytes\\\",\\n      \\\"check identity and exact revisions\\\",\\n      \\\"check surface artifacts\\\",\\n      \\\"return blocked or evidence\\\"\\n    ]\\n  },\\n  \\\"verdict\\\": \\\"BLOCKED\\\"\\n}\\n```\\n\\nProve It Works shaped the decision to inspect committed bytes directly and withhold a passing verdict. Poteto mode, Shipping, and Unslop were read and applied. No writes, builds, commits, configuration changes, network calls, or nested delegation occurred. Coordinator owns native result capture.\\n\"\n}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.md",
      "sha256": "16713517c69863a5d139826a4bca26daa70e61754a30e6b2aa67cdd8e201fed5",
      "bytes": 1355,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "BLOCKED for PR 102.\n\nAssignment `verifier-102`. Worker `/root/verifier_102`.\nInputRevision `ec045fadb47b598147052035b7eb1a9c47813156`.\nRequested model `inherit-parent`. Actual model `unknown`.\n\nI inspected `committed-inputs/forge.json` through `git show` at the exact input revision, then checked its fields with Bun.\n\nThe source contains only PRs 1 and 2. PR 102 is absent. Their base/head values are symbolic names, not full commit SHAs. The source supplies no PR 102 stable patch identity or real-surface artifacts. I stopped at the exact-revisions gate. No passing verification or landing authorization follows.\n\n```json\n{\n  \"assignmentId\": \"verifier-102\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  },\n  \"verdict\": \"BLOCKED\"\n}\n```\n\nProve It Works shaped the decision to inspect committed bytes directly and withhold a passing verdict. Poteto mode, Shipping, and Unslop were read and applied. No writes, builds, commits, configuration changes, network calls, or nested delegation occurred. Coordinator owns native result capture.\n"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-102.spawn-return.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.spawn-return.json",
      "sha256": "6981aaa094557c2b52c69c70e5e6fce74aa334dcb68cbd741294bf628a398fab",
      "bytes": 34,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\"task_name\":\"/root/verifier_102\"}"
    },
    {
      "path": "fixtures/durable-03/contiguous-verified-stack/verifier-102.task.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.task.txt",
      "sha256": "887bf3562c68777ed146d93f08f94d21bb3789558b6e377a78fdd811c6b7043c",
      "bytes": 2958,
      "owners": [
        "grades-native-durable-03.json#2"
      ],
      "text": "{\n  \"id\": \"verifier-102\",\n  \"scope\": \"Inspect PR 102 verification prerequisites using ONLY committed-inputs/forge.json at inputRevision. It has PRs 1/2, no 101..104 and no full SHA heads. Do not map those records or invent source commits. Independently confirm gap. Exact PR base/head are absent; stop verification at that gate. Return BLOCKED unless real evidence exists. No predeclared PASS or PASS+NOTES.\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"role\": \"poteto-agent independent non-author PR verifier\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/verifier-102.native-result.md\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/contiguous-verified-stack/supplied-input.json\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one committed source prerequisite inspection; not a real-surface lane\",\n    \"order\": [\n      \"read source bytes\",\n      \"check identity and exact revisions\",\n      \"check surface artifacts\",\n      \"return blocked or evidence\"\n    ]\n  },\n  \"resultMethodRequired\": true\n}\n\nFull role prompt\n# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\n\nRead complete shipping contract at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md. Read-only, no source or output writes, builds, commits, configuration, network or nested workers. Coordinator captures result. Return assignment id, inputRevision and resultMethod matching method above.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/inputs",
      "owner": "grades-native-07.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/source-read.txt",
      "owner": "grades-native-07.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/inputs",
      "owner": "grades-native-07.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/contiguous-verified-stack/source-read.txt",
      "owner": "grades-native-07.json#6",
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
