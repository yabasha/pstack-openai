# codex: contiguous-verified-stack

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "contiguous-verified-stack",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-07.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Task Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
