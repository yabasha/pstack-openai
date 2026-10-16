# codex: bounded-improvement

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "bounded-improvement",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-07.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Hillclimb a fixture export latency using a fixed target and minimum iteration count. Supply contrasting realistic workloads, an exact baseline revision, a repeatable harness, error and completed-work counts, a green regression gate and candidate artifacts. Include an early lucky win, noise-sized improvement, changed workload, regression, plateau, worthwhile cheap remaining hypothesis and exhausted marginal ideas. Permit local measurement and edits but no commits, PR writes or recurring scheduling. Repeat with unavailable workers, denied execution and missing persistence. Compare every candidate using the same valid frozen metric and retain the stopping rule.",
  "caseDefinition": {
    "id": "bounded-improvement",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/hillclimb.md",
      "skills/poteto-mode/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/benchmark-checklist/SKILL.md",
      "skills/principle-explain-the-number/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-build-the-lever/SKILL.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/poteto-mode/playbooks/perf-issue.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "Hillclimb a fixture export latency using a fixed target and minimum iteration count. Supply contrasting realistic workloads, an exact baseline revision, a repeatable harness, error and completed-work counts, a green regression gate and candidate artifacts. Include an early lucky win, noise-sized improvement, changed workload, regression, plateau, worthwhile cheap remaining hypothesis and exhausted marginal ideas. Permit local measurement and edits but no commits, PR writes or recurring scheduling. Repeat with unavailable workers, denied execution and missing persistence. Compare every candidate using the same valid frozen metric and retain the stopping rule.",
    "requirements": [
      "Read the complete mode, playbook, how prompts, measurement and principle leaves, poteto role prompt and decision-log helper. Missing required reads stop dependent work.",
      "Reproduce the complaint across realistic workload dimensions. Agree one metric, direction, target and minimum attempt floor before attempts. Prove harness sensitivity with contrasting workloads, vet the checklist, freeze command/configuration, record baseline and green gate.",
      "Use exact revisions and comparable workloads. For performance comparisons alternate at least five runs per side, retain median/range, limiter, production tuning, outputs, error and completed-work counts. Source inspection and inconclusive comparisons cannot prove gains.",
      "Open gitignored decision.tsv through show-me-your-work and log.sh. Preserve append-only history, per-attempt id/hypothesis/change/before/after/delta/tests/verdict/note, read before attempts, readback persistence and transcript/review limits.",
      "Ground hypotheses in how. For performance use Perf issue mantra order without its earlier-success stop rule. Delegate tightly scoped revision-matched attempts with full role prompt, supported configured or inherited selection and inspected results. Isolate concurrent hypotheses and compare each to the same base; sequential fallback stays reduced.",
      "Measure and gate each single change before the next. Keep only changes past noise with green tests, revert failed candidates fully without touching unrelated work, and log every verdict. Commit each accepted fix only with permission and exact staging.",
      "Pivot after a plateau, combine near-misses only as a newly verified single hypothesis, prioritize correctness/simplicity, and do not abandon cheap remaining ideas. Stop at target plus floor, marginal cost or a surfaced dead end without relaxing the predicate. Wake scheduling borrows only Autonomous run mechanism and requires explicit authorization.",
      "Deliver accepted commits in order through complete Opening a PR only when authorized. Return metric/target, baseline/final/calculated percent, kept/reverted counts, each accepted fix, decision.tsv path and next idea, plus stop reason and Attention/review limits."
    ],
    "expectedFull": "Observed authorized independent candidates use the same sensitive frozen metric, comparable exact revisions/workloads and green regression gate. Every attempt has inspected evidence and an append-only log row. Regressions and noise-sized changes revert. A lucky win below the agreed iteration floor does not stop the loop, a plateau prompts new hypotheses, and cheap untried ideas remain actionable. The loop ends at the unchanged predicate or explicitly reports a marginal-cost stop or genuine dead end. Authorized commits and delivery preserve accepted order. The reply contains every original item and real artifacts.",
    "expectedReduced": "Authorized sequential attempts preserve the same measurement and stopping gates but leave independent delegation unsatisfied. No commit or external-write permission retains verified local work and a local PR draft only. No wake authorization means foreground execution. Supplied artifacts can support a limited assessment but cannot create missing runs. Unknown models, unavailable transcript audit or different-family review remain explicit limits.",
    "expectedBlocked": "Missing required source or pending companions blocks dependent routes. An unreproduced complaint requires repro repair before hillclimbing. An insensitive harness, missing green baseline, denied measurement execution, changed metric/workload, unchecked errors/work or missing artifacts prevents accepting a candidate. Missing persistence/helper execution blocks the required saved decision trail. An unavailable required model or independent-review capability stays blocked. Unavailable checks stop advancement; unauthorized commits, scheduling and external writes remain unperformed.",
    "forbiddenClaims": [
      "Structural validation proves a measured improvement or a host pass.",
      "A lucky early win meets the stopping predicate without the minimum attempts, or the target can be relaxed to claim success.",
      "Perf issue or Autonomous run stop rules replace Hillclimb stopping rules.",
      "A changed metric, workload or unrecorded revision is comparable, or noise-sized gains and regressions are kept.",
      "An insensitive harness, untuned run, unknown limiter or skipped work proves a win.",
      "Sequential attempts are independent workers or unknown requested models prove diversity.",
      "An unavailable helper ran, an unsaved log persisted, or missing transcript/reviewer access proves a complete audit.",
      "Upstream autonomy authorizes commits, scheduling, PR writes or installation.",
      "A local draft is a created PR, unrun tests are green, or opening a PR starts Babysit.",
      "A cost-based stop meets the target or a zero baseline supports a percent improvement."
    ],
    "caseFile": "docs/parity/cases/playbooks/hillclimb.json"
  },
  "registry": {
    "caseId": "bounded-improvement",
    "caseFile": "docs/parity/cases/playbooks/hillclimb.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/hillclimb.md",
      "skills/poteto-mode/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/benchmark-checklist/SKILL.md",
      "skills/principle-explain-the-number/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-build-the-lever/SKILL.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/poteto-mode/playbooks/perf-issue.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "agents/poteto-agent.md"
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
        "execution",
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
      "attemptId": "grades-native-07.json#1",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "bounded-improvement",
      "status": "blocked",
      "grade": {
        "caseId": "bounded-improvement",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_9",
          "item_10",
          "item_11",
          "item_12",
          "item_18",
          "item_22",
          "item_24"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Green baseline, exact target/iteration floor and comparable treatment/limiter evidence absent.",
          "Matching control companion/exact taskGit absent."
        ],
        "review": "Actual export baseline fails CSV correctness, so no candidate accepted or speed delta invented. Local function measurements with synthetic workloads do not replace target CLI/control traces/exact revision/iteration predicate. Correct stop preserves red correctness gate but hillclimb remains blocked.",
        "responseArtifact": "fixtures/batch-07/bounded-improvement.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [
          "Supply missing concrete acceptance inputs/grants then rerun; do not classify correct fail-closed behavior as source bug."
        ],
        "fullExpected": "Observed authorized independent candidates use the same sensitive frozen metric, comparable exact revisions/workloads and green regression gate. Every attempt has inspected evidence and an append-only log row. Regressions and noise-sized changes revert. A lucky win below the agreed iteration floor does not stop the loop, a plateau prompts new hypotheses, and cheap untried ideas remain actionable. The loop ends at the unchanged predicate or explicitly reports a marginal-cost stop or genuine dead end. Authorized commits and delivery preserve accepted order. The reply contains every original item and real artifacts.",
        "reducedExpected": "Authorized sequential attempts preserve the same measurement and stopping gates but leave independent delegation unsatisfied. No commit or external-write permission retains verified local work and a local PR draft only. No wake authorization means foreground execution. Supplied artifacts can support a limited assessment but cannot create missing runs. Unknown models, unavailable transcript audit or different-family review remain explicit limits.",
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
        "text": "# bounded-improvement\n\n## Supplied input\n\nHillclimb a fixture export latency using a fixed target and minimum iteration count. Supply contrasting realistic workloads, an exact baseline revision, a repeatable harness, error and completed-work counts, a green regression gate and candidate artifacts. Include an early lucky win, noise-sized improvement, changed workload, regression, plateau, worthwhile cheap remaining hypothesis and exhausted marginal ideas. Permit local measurement and edits but no commits, PR writes or recurring scheduling. Repeat with unavailable workers, denied execution and missing persistence. Compare every candidate using the same valid frozen metric and retain the stopping rule.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual output\n\nINCONCLUSIVE. The baseline correctness gate is red. The fixture export does not escape commas or double quotes. No treatment was accepted or measured, and no speedup or calculated baseline-to-treatment delta is available.\n\nThe supplied fixture has a dashboard export function, not an export CLI, target, trace archive, production configuration or task Git SHA. I built a local command to exercise its filter-and-export path and labeled this reduced measurement. The matching control-cli companion is not bundled or exposed here, so the complete matching-control capture gate remains blocked.\n\nFor the large synthetic workload, the observed baseline median was 6.194041 ms, range 4.692542 to 18.879250 ms across five samples. The small workload median was 0.068000 ms. These are workload-sensitivity observations, not a comparison between implementations. Each large sample completes 120000 row serializations across three exports of the 40000 selected rows. Each sample records one CSV contract failure on the supplied seed, not one error per malformed row. Runtime exceptions were not observed. Full output digests and byte counts are retained.\n\nBaseline content revision is SHA-256 34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9. It is not a Git SHA. Exact source, input rows and command are retained. Treatment revision, post-fix latency and percent delta are unavailable.\n\n## Grounding and checklist\n\nOverview: input/dashboard.mjs owns both visible and exportCsv. run.mjs generates orders from the copied three-row seed, calls visible(rows,'open'), fully materializes exportCsv output, records elapsed milliseconds, and consumes the output with a digest after timing.\n\nKey concepts: open-row selection, CSV serialization, completed selected rows, and a literal expected CSV seed output. Flow is generated rows to status filtering to complete string export to post-timer verification. The boundary excludes process startup, input parsing, disk writes and a real product CLI, which is absent. Repetition is part of this synthetic workload, not evidence that production exports the same rows three times.\n\nThe independent profiling run is retained under ../bounded-improvement/baseline-profile.cpuprofile.cpuprofile and its Markdown companion. It sampled exportCsv mapping and join as hot code. It is short and includes generation and digest overhead; it suggests serialization work but does not establish a stable production limiter. Profile timings were excluded from report samples.\n\n| Checklist gate | Observed evidence or limitation |\n| --- | --- |\n| Limiter | Short profile identifies map/join samples; production limiter remains unverified. |\n| Tuning | Bun 1.4.2, concurrency 1, no production tuning supplied. Cannot select an implementation. |\n| Physical bounds | In-memory workload, no disk/network speed claim. No plausible optimization ceiling inferred. |\n| Errors and outputs | Five seed CSV contract failures per workload, full output consumed and digest stored. Gate RED. |\n| Repeatability | Five baseline samples each; no treatment exists, so no alternating A/B comparison. Large spread precludes small-gain claims. |\n| Relevance | Filter/export function only, not user-visible end-to-end CLI I/O. |\n| Completed work | Rows materialized, output string produced inside timer, hashes consumed afterward. |\n\nHost contention check observed load averages 4.21, 4.50 and 5.07. Core query via sysctl was denied. This prevents a complete contention assessment. No unrelated process was stopped.\n\n## Attempts and variants\n\nThe unchanged stop predicate is at least 50 percent lower median latency plus at least 10 optimization attempts. Those are explicit source defaults, selected before this loop because no numbers were supplied; they were not user-agreed numbers. The baseline has no green gate, so dependent attempts stop. Actual optimization iterations 0, kept 0, reverted 0. No fix was stacked or committed. Target plus floor remains unresolved.\n\ncomparison-negative-probes.json contains executable comparator input/output records for different workload, absent treatment revision, untuned side, noise-sized difference, skipped work, wrong system, absent limiter/control evidence and regression. They are deliberately SYNTHETIC records, not runtime measurements or a valid frozen comparison. A schema-eligible record is only a parser exercise. It proves no speedup.\n\nstopping-rule.test.mjs executes synthetic states for an early lucky win, plateau with a worthwhile cheap idea, exhausted marginal ideas, target plus attempt floor, and a red regression gate. All five local policy tests passed. This does not mean ten real attempts occurred or hypotheses were exhausted. The best next cheap task is to correct CSV escaping, then obtain a green baseline and exact task revision before new timing comparisons.\n\nUnavailable workers, denied execution and missing persistence were simulated policy branches only. The host exposes workers, execution and writable persistence. In the execution-denied branch no new command was launched. In the persistence-missing branch no log save was claimed. In the no-worker branch sequential inspection leaves independence unmet. These conditions were not enforced by the host.\n\n## Tools, artifacts and delivery\n\nActual tools were functions.exec with tools.exec_command, Bun scripts and Bun-spawned bash invocation of the installed log.sh. The helper was invoked with exactly logfile, phase, decision, why, evidence, result. Actual argv, stdout, stderr and exit codes are in ../performance-command-results.json. Re-run the baseline from this directory with bun --no-install run.mjs --gate. The expected baseline gate exit is 1.\n\nThe append-only trail is bounded-improvement/decision.tsv; it was read back into decision-readback.txt. Its local .gitignore names decision.tsv, but this directory has no Git repository, so an operative git-ignore check is unavailable. No performance worker dispatch occurred at an exact input Git SHA because no such SHA exists. No independent fix review is claimed.\n\nOpening a PR was read. Commits, pushing, readiness and PR writes are forbidden. A local draft below is preparation only. deslop and matching CLI controls are unavailable; their gates remain open. No Babysit was started.\n\nLocal draft title: fix(export): escape customer fields before optimization\n\nLocal draft body: The supplied CSV exporter emits malformed customer fields. Correctness must be repaired before optimization. This run reproduces the defect and retains baseline observations; no fix is claimed. Scope is the inert local fixture. Verification is the failing literal-output check in baseline.json.\n\n## Attention\n\nreviewed by unknown\n\nCross-model review remains unverified. The accessible current-turn tool outputs and local evidence support a partial audit only; no complete machine-readable current-run transcript binding is exposed. The synthetic shared history is not this run's transcript. The source's exact-revision, green-gate and production measurement prerequisites remain open.\n",
        "artifact": {
          "path": "fixtures/batch-07/bounded-improvement.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement.result.md",
          "sha256": "bde2de48ed8d4692e0b585f6e09f776231436961bb555233f0db24f2b5da9401",
          "bytes": 8203
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
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1583aa6d4af4c3b46e71bfacaa0e4b5bc7b2050dc2076fbaa68327f0a73fc840"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "22bc8b3362b793f2c3865b8e7b5b465cc0f8042ae168a136d28c46640529903c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "dafc6d04936d05d466e755dd270b8264b254dbefacedd52aafd59c8748d55d42"
              },
              {
                "eventId": "item_10",
                "line": 20,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4737e0f01dbafadbbbac5713a3162fab133b7a41bf881dca4d20c62aba7da51f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "dd43d629da1996dd0bf654e06f2192b741e8d8cbb10d57458fb99f82795d5a6d"
              },
              {
                "eventId": "item_11",
                "line": 22,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7e173de2246c9d78e1a9c07da01b21ab397c109d5fa72cba93b2c54788e419c7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b7216fa5addff96e8623638f7324a98997792f4b0fb2961a81e6d95082cb5310"
              },
              {
                "eventId": "item_12",
                "line": 24,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8352a35dccc9ec57246bf150bdafb8b2003febb178d1ea0773edd5a92fc57992",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a00945eb89378e452d3f80edf9ae51c2594da02428a3eb8e652ba8a719046fae"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5f64a756ad409b64eb5817ff45fa83f69d833ce562b059fa3f2f05649865efc3",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d3a33df900d7b103bbf78e1ad77f3cf16cd5bde0e2a6e402c9a9b4b29f1a7f91"
              },
              {
                "eventId": "item_22",
                "line": 43,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "18b54cce2112f3ba4a8f61b78d5826a46f22049eb703842bd075aee2f6b0cadf",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_24",
                "line": 45,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d8501c72a47e3d120cb5da57a6fbf6f063545f9215d768b4a3bdea2341c6218a"
              },
              {
                "eventId": "item_24",
                "line": 46,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "42f34053d126c52417aff4adcbb4a481c8a8c6713a6e9691354049b392c29162",
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
            "item_9",
            "item_10",
            "item_11",
            "item_12",
            "item_18",
            "item_22",
            "item_24"
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
      "path": "fixtures/batch-07/bounded-improvement/.gitignore",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/.gitignore",
      "sha256": "8fadd16cc626b1932746f316f5b38b206875fd9602b24f2164e8b3df6f8e0102",
      "bytes": 13,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "decision.tsv\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/baseline-command.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/baseline-command.txt",
      "sha256": "61599c32e17a9c93b39e2f3a7fc520ac243217edbf4329dcee9a48b8c021ed3d",
      "bytes": 1606,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "[\n  {\n    \"workload\": {\n      \"name\": \"small\",\n      \"size\": 300,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"medianMs\": 0.06800000000000139,\n    \"rangeMs\": [\n      0.05383299999999913,\n      0.2241250000000008\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\",\n    \"errors\": 5,\n    \"completed\": 3000\n  },\n  {\n    \"workload\": {\n      \"name\": \"large\",\n      \"size\": 60000,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"medianMs\": 6.194040999999999,\n    \"rangeMs\": [\n      4.692541999999996,\n      18.87925\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\",\n    \"errors\": 5,\n    \"completed\": 600000\n  }\n]\nexit=1\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/baseline-profile.cpuprofile.cpuprofile",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/baseline-profile.cpuprofile.cpuprofile",
      "sha256": "d73fa286d62a31b4f6d4ce9deac898857108a9a0a98cbbf6685a5967daec1e3f",
      "bytes": 5907,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "{\"nodes\":[{\"id\":1,\"callFrame\":{\"functionName\":\"(root)\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[2,20]},{\"id\":2,\"callFrame\":{\"functionName\":\"node:crypto\",\"scriptId\":\"2\",\"url\":\"node:crypto\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[3]},{\"id\":3,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[4]},{\"id\":4,\"callFrame\":{\"functionName\":\"internal:streams/lazy_transform\",\"scriptId\":\"3\",\"url\":\"internal:streams/lazy_transform\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[5]},{\"id\":5,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":1,\"children\":[6]},{\"id\":6,\"callFrame\":{\"functionName\":\"internal:streams/transform\",\"scriptId\":\"4\",\"url\":\"internal:streams/transform\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[7]},{\"id\":7,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[8]},{\"id\":8,\"callFrame\":{\"functionName\":\"internal:streams/duplex\",\"scriptId\":\"5\",\"url\":\"internal:streams/duplex\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[9]},{\"id\":9,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[10]},{\"id\":10,\"callFrame\":{\"functionName\":\"internal:streams/readable\",\"scriptId\":\"6\",\"url\":\"internal:streams/readable\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[11]},{\"id\":11,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[12]},{\"id\":12,\"callFrame\":{\"functionName\":\"internal:streams/destroy\",\"scriptId\":\"7\",\"url\":\"internal:streams/destroy\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[13]},{\"id\":13,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[14]},{\"id\":14,\"callFrame\":{\"functionName\":\"internal:errors\",\"scriptId\":\"8\",\"url\":\"internal:errors\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[15]},{\"id\":15,\"callFrame\":{\"functionName\":\"anonymous\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[16]},{\"id\":16,\"callFrame\":{\"functionName\":\"internal:primordials\",\"scriptId\":\"9\",\"url\":\"internal:primordials\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[17]},{\"id\":17,\"callFrame\":{\"functionName\":\"makeSafe\",\"scriptId\":\"9\",\"url\":\"internal:primordials\",\"lineNumber\":28,\"columnNumber\":48},\"hitCount\":0,\"children\":[18]},{\"id\":18,\"callFrame\":{\"functionName\":\"bound call\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[19]},{\"id\":19,\"callFrame\":{\"functionName\":\"call\",\"scriptId\":\"10\",\"url\":\"\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":1,\"positionTicks\":[{\"line\":1,\"ticks\":1}]},{\"id\":20,\"callFrame\":{\"functionName\":\"(module)\",\"scriptId\":\"11\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs\",\"lineNumber\":0,\"columnNumber\":0},\"hitCount\":0,\"children\":[21,23,24,25,29,33]},{\"id\":21,\"callFrame\":{\"functionName\":\"readFileSync\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[22]},{\"id\":22,\"callFrame\":{\"functionName\":\"readFileSync\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":1},{\"id\":23,\"callFrame\":{\"functionName\":\"from\",\"scriptId\":\"10\",\"url\":\"\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":1,\"children\":[31],\"positionTicks\":[{\"line\":1,\"ticks\":1}]},{\"id\":24,\"callFrame\":{\"functionName\":\"filter\",\"scriptId\":\"10\",\"url\":\"\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":3,\"positionTicks\":[{\"line\":1,\"ticks\":3}]},{\"id\":25,\"callFrame\":{\"functionName\":\"exportCsv\",\"scriptId\":\"12\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs\",\"lineNumber\":1,\"columnNumber\":25},\"hitCount\":0,\"children\":[26,28]},{\"id\":26,\"callFrame\":{\"functionName\":\"map\",\"scriptId\":\"10\",\"url\":\"\",\"lineNumber\":0,\"columnNumber\":10},\"hitCount\":0,\"children\":[27]},{\"id\":27,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"12\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs\",\"lineNumber\":1,\"columnNumber\":74},\"hitCount\":10,\"positionTicks\":[{\"line\":2,\"ticks\":10}]},{\"id\":28,\"callFrame\":{\"functionName\":\"join\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":7},{\"id\":29,\"callFrame\":{\"functionName\":\"digest\",\"scriptId\":\"11\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs\",\"lineNumber\":3,\"columnNumber\":13},\"hitCount\":0,\"children\":[30]},{\"id\":30,\"callFrame\":{\"functionName\":\"update\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":2},{\"id\":31,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"11\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs\",\"lineNumber\":9,\"columnNumber\":38},\"hitCount\":0,\"children\":[32]},{\"id\":32,\"callFrame\":{\"functionName\":\"cloneObject\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":2},{\"id\":33,\"callFrame\":{\"functionName\":\"writeFileSync\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[34]},{\"id\":34,\"callFrame\":{\"functionName\":\"writeFileSync\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":1}],\"startTime\":1792137564607691,\"endTime\":1792137564651435.5,\"samples\":[5,19,22,23,24,27,28,27,24,27,30,27,27,27,28,24,28,27,28,32,27,27,27,30,32,28,28,28,34],\"timeDeltas\":[2734,1521,1385,1641,1234,1467,1318,1486,1619,1276,1826,1456,1760,1801,1114,1656,1436,1241,1574,1306,1175,1610,1763,1224,1404,1246,1671,1467,1323]}"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/baseline-profile.cpuprofile.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/baseline-profile.cpuprofile.md",
      "sha256": "05a1247e1d692d452f651bf55d67a16ed16b1429be9a81bad98ec1af4d501157",
      "bytes": 10134,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "# CPU Profile\n\n| Duration | Samples | Interval | Functions |\n|----------|---------|----------|----------|\n| 43.7ms | 29 | 1.0ms | 29 |\n\n**Top 10:** `(anonymous)` 34.3%, `join` 22.4%, `filter` 10.3%, `update` 6.9%, `anonymous` 6.2%, `cloneObject` 6.1%, `from` 3.7%, `call` 3.4%, `readFileSync` 3.1%, `writeFileSync` 3.0%\n\n## Hot Functions (Self Time)\n\n| Self% | Self | Total% | Total | Function | Location |\n|------:|-----:|-------:|------:|----------|----------|\n| 34.3% | 15.0ms | 34.3% | 15.0ms | `(anonymous)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs:2` |\n| 22.4% | 9.8ms | 22.4% | 9.8ms | `join` | `[native code]` |\n| 10.3% | 4.5ms | 10.3% | 4.5ms | `filter` | `[native code]` |\n| 6.9% | 3.0ms | 6.9% | 3.0ms | `update` | `[native code]` |\n| 6.2% | 2.7ms | 36.8% | 16.1ms | `anonymous` | `[native code]` |\n| 6.1% | 2.7ms | 6.1% | 2.7ms | `cloneObject` | `[native code]` |\n| 3.7% | 1.6ms | 9.9% | 4.3ms | `from` | `[native code]` |\n| 3.4% | 1.5ms | 3.4% | 1.5ms | `call` | `[native code]` |\n| 3.1% | 1.3ms | 6.3% | 2.7ms | `readFileSync` | `[native code]` |\n| 3.0% | 1.3ms | 6.0% | 2.6ms | `writeFileSync` | `[native code]` |\n\n## Call Tree (Total Time)\n\n| Total% | Total | Self% | Self | Function | Location |\n|-------:|------:|------:|-----:|----------|----------|\n| 67.1% | 29.3ms | 0.0% | 0us | `(module)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:11` |\n| 56.8% | 24.8ms | 0.0% | 0us | `exportCsv` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs:2` |\n| 36.8% | 16.1ms | 6.2% | 2.7ms | `anonymous` | `[native code]` |\n| 34.3% | 15.0ms | 0.0% | 0us | `map` | `[native code]` |\n| 34.3% | 15.0ms | 34.3% | 15.0ms | `(anonymous)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs:2` |\n| 22.4% | 9.8ms | 22.4% | 9.8ms | `join` | `[native code]` |\n| 10.3% | 4.5ms | 10.3% | 4.5ms | `filter` | `[native code]` |\n| 9.9% | 4.3ms | 3.7% | 1.6ms | `from` | `[native code]` |\n| 9.9% | 4.3ms | 0.0% | 0us | `(module)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:10` |\n| 9.7% | 4.2ms | 0.0% | 0us | `internal:streams/lazy_transform` | `internal:streams/lazy_transform:2` |\n| 9.7% | 4.2ms | 0.0% | 0us | `node:crypto` | `node:crypto:2` |\n| 6.9% | 3.0ms | 0.0% | 0us | `digest` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:4` |\n| 6.9% | 3.0ms | 0.0% | 0us | `(module)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:15` |\n| 6.9% | 3.0ms | 6.9% | 3.0ms | `update` | `[native code]` |\n| 6.3% | 2.7ms | 3.1% | 1.3ms | `readFileSync` | `[native code]` |\n| 6.1% | 2.7ms | 6.1% | 2.7ms | `cloneObject` | `[native code]` |\n| 6.1% | 2.7ms | 0.0% | 0us | `(anonymous)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:10` |\n| 6.0% | 2.6ms | 3.0% | 1.3ms | `writeFileSync` | `[native code]` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:primordials` | `internal:primordials:83` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:errors` | `internal:errors:2` |\n| 3.4% | 1.5ms | 3.4% | 1.5ms | `call` | `[native code]` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:streams/destroy` | `internal:streams/destroy:2` |\n| 3.4% | 1.5ms | 0.0% | 0us | `bound call` | `[native code]` |\n| 3.4% | 1.5ms | 0.0% | 0us | `makeSafe` | `internal:primordials:35` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:streams/readable` | `internal:streams/readable:2` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:streams/duplex` | `internal:streams/duplex:2` |\n| 3.4% | 1.5ms | 0.0% | 0us | `internal:streams/transform` | `internal:streams/transform:2` |\n| 3.1% | 1.3ms | 0.0% | 0us | `(module)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:5` |\n| 3.0% | 1.3ms | 0.0% | 0us | `(module)` | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:17` |\n\n## Function Details\n\n### `(anonymous)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs:2` | Self: 34.3% (15.0ms) | Total: 34.3% (15.0ms) | Samples: 10\n\n**Called by:**\n- `map` (10)\n\n### `join`\n`[native code]` | Self: 22.4% (9.8ms) | Total: 22.4% (9.8ms) | Samples: 7\n\n**Called by:**\n- `exportCsv` (7)\n\n### `filter`\n`[native code]` | Self: 10.3% (4.5ms) | Total: 10.3% (4.5ms) | Samples: 3\n\n**Called by:**\n- `(module)` (3)\n\n### `update`\n`[native code]` | Self: 6.9% (3.0ms) | Total: 6.9% (3.0ms) | Samples: 2\n\n**Called by:**\n- `digest` (2)\n\n### `anonymous`\n`[native code]` | Self: 6.2% (2.7ms) | Total: 36.8% (16.1ms) | Samples: 1\n\n**Called by:**\n- `node:crypto` (2)\n- `internal:streams/lazy_transform` (2)\n- `internal:streams/destroy` (1)\n- `internal:streams/readable` (1)\n- `internal:streams/duplex` (1)\n- `internal:streams/transform` (1)\n- `internal:errors` (1)\n\n**Calls:**\n- `internal:streams/lazy_transform` (2)\n- `internal:streams/destroy` (1)\n- `internal:streams/readable` (1)\n- `internal:streams/duplex` (1)\n- `internal:streams/transform` (1)\n- `internal:errors` (1)\n- `internal:primordials` (1)\n\n### `cloneObject`\n`[native code]` | Self: 6.1% (2.7ms) | Total: 6.1% (2.7ms) | Samples: 2\n\n**Called by:**\n- `(anonymous)` (2)\n\n### `from`\n`[native code]` | Self: 3.7% (1.6ms) | Total: 9.9% (4.3ms) | Samples: 1\n\n**Called by:**\n- `(module)` (3)\n\n**Calls:**\n- `(anonymous)` (2)\n\n### `call`\n`[native code]` | Self: 3.4% (1.5ms) | Total: 3.4% (1.5ms) | Samples: 1\n\n**Called by:**\n- `bound call` (1)\n\n### `readFileSync`\n`[native code]` | Self: 3.1% (1.3ms) | Total: 6.3% (2.7ms) | Samples: 1\n\n**Called by:**\n- `(module)` (1)\n- `readFileSync` (1)\n\n**Calls:**\n- `readFileSync` (1)\n\n### `writeFileSync`\n`[native code]` | Self: 3.0% (1.3ms) | Total: 6.0% (2.6ms) | Samples: 1\n\n**Called by:**\n- `writeFileSync` (1)\n- `(module)` (1)\n\n**Calls:**\n- `writeFileSync` (1)\n\n### `node:crypto`\n`node:crypto:2` | Self: 0.0% (0us) | Total: 9.7% (4.2ms) | Samples: 0\n\n**Calls:**\n- `anonymous` (2)\n\n### `internal:streams/lazy_transform`\n`internal:streams/lazy_transform:2` | Self: 0.0% (0us) | Total: 9.7% (4.2ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (2)\n\n**Calls:**\n- `anonymous` (2)\n\n### `internal:primordials`\n`internal:primordials:83` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `makeSafe` (1)\n\n### `(module)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:17` | Self: 0.0% (0us) | Total: 3.0% (1.3ms) | Samples: 0\n\n**Calls:**\n- `writeFileSync` (1)\n\n### `internal:streams/transform`\n`internal:streams/transform:2` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `anonymous` (1)\n\n### `(module)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:11` | Self: 0.0% (0us) | Total: 67.1% (29.3ms) | Samples: 0\n\n**Calls:**\n- `exportCsv` (17)\n- `filter` (3)\n\n### `(anonymous)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:10` | Self: 0.0% (0us) | Total: 6.1% (2.7ms) | Samples: 0\n\n**Called by:**\n- `from` (2)\n\n**Calls:**\n- `cloneObject` (2)\n\n### `internal:errors`\n`internal:errors:2` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `anonymous` (1)\n\n### `bound call`\n`[native code]` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `makeSafe` (1)\n\n**Calls:**\n- `call` (1)\n\n### `internal:streams/destroy`\n`internal:streams/destroy:2` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `anonymous` (1)\n\n### `(module)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:15` | Self: 0.0% (0us) | Total: 6.9% (3.0ms) | Samples: 0\n\n**Calls:**\n- `digest` (2)\n\n### `exportCsv`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs:2` | Self: 0.0% (0us) | Total: 56.8% (24.8ms) | Samples: 0\n\n**Called by:**\n- `(module)` (17)\n\n**Calls:**\n- `map` (10)\n- `join` (7)\n\n### `(module)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:5` | Self: 0.0% (0us) | Total: 3.1% (1.3ms) | Samples: 0\n\n**Calls:**\n- `readFileSync` (1)\n\n### `makeSafe`\n`internal:primordials:35` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `internal:primordials` (1)\n\n**Calls:**\n- `bound call` (1)\n\n### `map`\n`[native code]` | Self: 0.0% (0us) | Total: 34.3% (15.0ms) | Samples: 0\n\n**Called by:**\n- `exportCsv` (10)\n\n**Calls:**\n- `(anonymous)` (10)\n\n### `(module)`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:10` | Self: 0.0% (0us) | Total: 9.9% (4.3ms) | Samples: 0\n\n**Calls:**\n- `from` (3)\n\n### `internal:streams/duplex`\n`internal:streams/duplex:2` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `anonymous` (1)\n\n### `internal:streams/readable`\n`internal:streams/readable:2` | Self: 0.0% (0us) | Total: 3.4% (1.5ms) | Samples: 0\n\n**Called by:**\n- `anonymous` (1)\n\n**Calls:**\n- `anonymous` (1)\n\n### `digest`\n`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs:4` | Self: 0.0% (0us) | Total: 6.9% (3.0ms) | Samples: 0\n\n**Called by:**\n- `(module)` (2)\n\n**Calls:**\n- `update` (2)\n\n## Files\n\n| Self% | Self | File |\n|------:|-----:|------|\n| 65.6% | 28.6ms | `[native code]` |\n| 34.3% | 15.0ms | `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/input/dashboard.mjs` |\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/baseline.json",
      "sha256": "f29216173cb34d6967cfec811ceea0eec18d6257ee7a4f53adcf138d847deced",
      "bytes": 5438,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "[\n  {\n    \"workload\": {\n      \"name\": \"small\",\n      \"size\": 300,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 0.2241250000000008,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.12529199999999996,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.06800000000000139,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.05562499999999915,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.05383299999999913,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 0.06800000000000139,\n    \"rangeMs\": [\n      0.05383299999999913,\n      0.2241250000000008\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  },\n  {\n    \"workload\": {\n      \"name\": \"large\",\n      \"size\": 60000,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 18.87925,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 6.588666999999994,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 6.194040999999999,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 5.1137079999999955,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.692541999999996,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 6.194040999999999,\n    \"rangeMs\": [\n      4.692541999999996,\n      18.87925\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/comparison-negative-probes.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/comparison-negative-probes.json",
      "sha256": "1a3ca555c0c0328725dbef81e0477c6ace8f3bdbce3ebb27a019d8ae8f3dfc1c",
      "bytes": 11142,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "{\n  \"notice\": \"All values below are synthetic comparator test inputs, never host runtime samples.\",\n  \"variants\": [\n    {\n      \"name\": \"valid artifact schema\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          10,\n          11,\n          10,\n          11,\n          10\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"schema eligible only; synthetic input proves no speedup\",\n        \"reasons\": [],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"different workload\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"small\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"different workload\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"unrecorded treatment revision\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": null,\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"unrecorded revision\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"untuned\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": false,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"untuned\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"noise-sized\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          19.9,\n          20.9,\n          19.9,\n          20.9,\n          19.9\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"skipped work\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 10,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"skipped work\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"wrong system\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"micro-only\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"wrong measured system\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"absent controls\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": null,\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"unknown limiter\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"regression\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          30,\n          31,\n          30,\n          31,\n          30\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"schema eligible only; synthetic input proves no speedup\",\n        \"reasons\": [],\n        \"synthetic\": true\n      }\n    }\n  ],\n  \"capabilityVariants\": [\n    {\n      \"name\": \"unavailable workers\",\n      \"enforced\": false,\n      \"behavior\": \"sequential fallback leaves independence unmet\"\n    },\n    {\n      \"name\": \"denied execution\",\n      \"enforced\": false,\n      \"behavior\": \"no child measurement launched in this branch; new measurement blocked\"\n    },\n    {\n      \"name\": \"missing persistence\",\n      \"enforced\": false,\n      \"behavior\": \"no log written for this branch; inline handoff only\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/decision-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/decision-readback.txt",
      "sha256": "9607b4cfde3d7ad2652671421868944349d169b4986fda79ad32494497d99a87",
      "bytes": 583,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\tframe\tFreeze target at 50 percent lower latency and minimum 10 attempts\tNo numerical target or floor supplied; source defaults retained\tsource-read.txt\topen\n2026-10-16T07:59:24Z\tbaseline\tStop dependent hillclimb at red CSV gate\tCorrectness outranks a faster malformed export\tbaseline.json\t0 attempts; no accepted or reverted fixes\n2026-10-16T07:59:24Z\tvariants\tValidate rejection conditions using synthetic records\tNegative branches must not manufacture measurements\tcomparison-negative-probes.json\tno runtime gains claimed\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/decision.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/decision.tsv",
      "sha256": "9607b4cfde3d7ad2652671421868944349d169b4986fda79ad32494497d99a87",
      "bytes": 583,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\tframe\tFreeze target at 50 percent lower latency and minimum 10 attempts\tNo numerical target or floor supplied; source defaults retained\tsource-read.txt\topen\n2026-10-16T07:59:24Z\tbaseline\tStop dependent hillclimb at red CSV gate\tCorrectness outranks a faster malformed export\tbaseline.json\t0 attempts; no accepted or reverted fixes\n2026-10-16T07:59:24Z\tvariants\tValidate rejection conditions using synthetic records\tNegative branches must not manufacture measurements\tcomparison-negative-probes.json\tno runtime gains claimed\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/profile-run.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile-run.json",
      "sha256": "4e65b522ec586ef46dc03313844adfc0ea2391af47f0262961516270c61c7055",
      "bytes": 5459,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "[\n  {\n    \"workload\": {\n      \"name\": \"small\",\n      \"size\": 300,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 0.21283299999999983,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.13233299999999915,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.12599999999999945,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.13212500000000027,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.06079100000000004,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 0.13212500000000027,\n    \"rangeMs\": [\n      0.06079100000000004,\n      0.21283299999999983\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  },\n  {\n    \"workload\": {\n      \"name\": \"large\",\n      \"size\": 60000,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 8.987457999999998,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 5.372541999999999,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.677666000000002,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.7294160000000005,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.599249999999998,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 4.7294160000000005,\n    \"rangeMs\": [\n      4.599249999999998,\n      8.987457999999998\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/profile.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/profile.mjs",
      "sha256": "f1e367ba51cd60a8b189fd53d830861dc254bb08171e1e73d358da9d67c0e912",
      "bytes": 1970,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "import {cpSync,mkdirSync,readFileSync,writeFileSync} from 'node:fs';\nimport {createHash} from 'node:crypto';\nimport {exportCsv,visible} from './input/dashboard.mjs';\nconst digest=x=>createHash('sha256').update(x).digest('hex');\nconst seed=JSON.parse(readFileSync('./input/orders.json','utf8'));\nconst revision=digest(readFileSync('./input/dashboard.mjs'));\nconst workloads=[{name:'small',size:300,repeat:3},{name:'large',size:60000,repeat:3}];\nconst results=[];\nfor(const w of workloads){let samples=[];for(let i=0;i<5;i++){\nconst rows=Array.from({length:w.size},(_,i)=>({...seed[i%seed.length],id:i+1}));\nconst start=performance.now();let output='',completed=0;for(let j=0;j<w.repeat;j++){const selected=visible(rows,'open');output=exportCsv(selected);completed+=selected.length;}\nconst elapsed=performance.now()-start;\nconst expected='id,customer,total\\n1,\"Ada, Inc.\",12.5\\n3,\"Say \"\"Hi\"\"\",0';\nconst seedOutput=exportCsv(visible(seed,'open'));\nsamples.push({ms:elapsed,errors:Number(seedOutput!==expected),completed,outputBytes:Buffer.byteLength(output),outputSha256:digest(output),expectedSeed:expected,actualSeed:seedOutput});}\nconst times=samples.map(x=>x.ms).sort((a,b)=>a-b);results.push({workload:w,revisionKind:'sha256-content-not-Git',revision,concurrency:1,config:{runtime:Bun.version,nodeEnv:process.env.NODE_ENV??null,warmup:'none; cold fixture path',cache:'fresh rows per sample, process reused',timedRegion:'filter + complete export repeated 3 times; output digest checked after timer',tuning:'no supplied production configuration; untuned status unknown'},samples,medianMs:times[2],rangeMs:[times[0],times.at(-1)],gate:'RED: CSV commas and quotes not escaped'});}\nwriteFileSync('profile-run.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results.map(({samples,...r})=>({...r,errors:samples.reduce((s,x)=>s+x.errors,0),completed:samples.reduce((s,x)=>s+x.completed,0)})),null,2));\nif(process.argv.includes('--gate')){process.exitCode=1;}\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/run.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/run.mjs",
      "sha256": "705796cd92f523f9a0c51701804df91ed1099799ef92f5f9f5e636d474e419d8",
      "bytes": 1967,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "import {cpSync,mkdirSync,readFileSync,writeFileSync} from 'node:fs';\nimport {createHash} from 'node:crypto';\nimport {exportCsv,visible} from './input/dashboard.mjs';\nconst digest=x=>createHash('sha256').update(x).digest('hex');\nconst seed=JSON.parse(readFileSync('./input/orders.json','utf8'));\nconst revision=digest(readFileSync('./input/dashboard.mjs'));\nconst workloads=[{name:'small',size:300,repeat:3},{name:'large',size:60000,repeat:3}];\nconst results=[];\nfor(const w of workloads){let samples=[];for(let i=0;i<5;i++){\nconst rows=Array.from({length:w.size},(_,i)=>({...seed[i%seed.length],id:i+1}));\nconst start=performance.now();let output='',completed=0;for(let j=0;j<w.repeat;j++){const selected=visible(rows,'open');output=exportCsv(selected);completed+=selected.length;}\nconst elapsed=performance.now()-start;\nconst expected='id,customer,total\\n1,\"Ada, Inc.\",12.5\\n3,\"Say \"\"Hi\"\"\",0';\nconst seedOutput=exportCsv(visible(seed,'open'));\nsamples.push({ms:elapsed,errors:Number(seedOutput!==expected),completed,outputBytes:Buffer.byteLength(output),outputSha256:digest(output),expectedSeed:expected,actualSeed:seedOutput});}\nconst times=samples.map(x=>x.ms).sort((a,b)=>a-b);results.push({workload:w,revisionKind:'sha256-content-not-Git',revision,concurrency:1,config:{runtime:Bun.version,nodeEnv:process.env.NODE_ENV??null,warmup:'none; cold fixture path',cache:'fresh rows per sample, process reused',timedRegion:'filter + complete export repeated 3 times; output digest checked after timer',tuning:'no supplied production configuration; untuned status unknown'},samples,medianMs:times[2],rangeMs:[times[0],times.at(-1)],gate:'RED: CSV commas and quotes not escaped'});}\nwriteFileSync('baseline.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results.map(({samples,...r})=>({...r,errors:samples.reduce((s,x)=>s+x.errors,0),completed:samples.reduce((s,x)=>s+x.completed,0)})),null,2));\nif(process.argv.includes('--gate')){process.exitCode=1;}\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/source-files.json",
      "sha256": "56b287de1e7ede7d8e5c84d706e2af6ffaf43f153bc7de34d24bcafaf0b9aca4",
      "bytes": 965,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "[\n  \"skills/poteto-mode/playbooks/hillclimb.md\",\n  \"skills/poteto-mode/SKILL.md\",\n  \"skills/how/SKILL.md\",\n  \"skills/how/references/explorer-prompt.md\",\n  \"skills/how/references/explainer-prompt.md\",\n  \"skills/benchmark-checklist/SKILL.md\",\n  \"skills/principle-explain-the-number/SKILL.md\",\n  \"skills/show-me-your-work/SKILL.md\",\n  \"skills/show-me-your-work/scripts/log.sh\",\n  \"skills/show-me-your-work/references/decision-log-template.tsv\",\n  \"skills/principle-prove-it-works/SKILL.md\",\n  \"skills/principle-build-the-lever/SKILL.md\",\n  \"skills/principle-guard-the-context-window/SKILL.md\",\n  \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n  \"skills/principle-sequence-verifiable-units/SKILL.md\",\n  \"skills/principle-laziness-protocol/SKILL.md\",\n  \"skills/poteto-mode/playbooks/perf-issue.md\",\n  \"skills/poteto-mode/playbooks/autonomous-run.md\",\n  \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n  \"references/agent-prompts/poteto-agent.md\"\n]"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/stopping-rule-command.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/stopping-rule-command.txt",
      "sha256": "800e7a5000ade50bef38c8c08f9350c4be5a8e17ec1d89fb841250fada0eaf48",
      "bytes": 378,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nbounded-improvement/stopping-rule.test.mjs:\n(pass) a synthetic lucky win cannot waive floor [0.07ms]\n(pass) plateau does not discard cheap idea\n(pass) exhausted marginal ideas allow explicit cost stop\n(pass) target with floor ends loop\n(pass) regression gate blocks advancement\n\n 5 pass\n 0 fail\n 5 expect() calls\nRan 5 tests across 1 file. [6.00ms]\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/stopping-rule.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement/stopping-rule.test.mjs",
      "sha256": "2cea9dd89ea5f26c5f96102d0579a0485923577223e65aa308285de9406d85b5",
      "bytes": 1073,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "import {test,expect} from 'bun:test';\nconst decide=({attempts,improvement,cheapIdeas,remainingCostWorthwhile,green=true})=>!green?'block at gate':improvement>=50&&attempts>=10?'target plus floor':cheapIdeas?'continue cheap hypothesis':!remainingCostWorthwhile?'cost stop; predicate unresolved':'continue or pivot';\ntest('a synthetic lucky win cannot waive floor',()=>expect(decide({attempts:1,improvement:70,cheapIdeas:true})).toBe('continue cheap hypothesis'));\ntest('plateau does not discard cheap idea',()=>expect(decide({attempts:10,improvement:20,cheapIdeas:true})).toBe('continue cheap hypothesis'));\ntest('exhausted marginal ideas allow explicit cost stop',()=>expect(decide({attempts:10,improvement:20,cheapIdeas:false,remainingCostWorthwhile:false})).toBe('cost stop; predicate unresolved'));\ntest('target with floor ends loop',()=>expect(decide({attempts:10,improvement:51,cheapIdeas:false})).toBe('target plus floor'));\ntest('regression gate blocks advancement',()=>expect(decide({attempts:1,improvement:70,cheapIdeas:true,green:false})).toBe('block at gate'));\n"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/bounded-improvement.result.md",
      "sha256": "bde2de48ed8d4692e0b585f6e09f776231436961bb555233f0db24f2b5da9401",
      "bytes": 8203,
      "owners": [
        "grades-native-07.json#1"
      ],
      "text": "# bounded-improvement\n\n## Supplied input\n\nHillclimb a fixture export latency using a fixed target and minimum iteration count. Supply contrasting realistic workloads, an exact baseline revision, a repeatable harness, error and completed-work counts, a green regression gate and candidate artifacts. Include an early lucky win, noise-sized improvement, changed workload, regression, plateau, worthwhile cheap remaining hypothesis and exhausted marginal ideas. Permit local measurement and edits but no commits, PR writes or recurring scheduling. Repeat with unavailable workers, denied execution and missing persistence. Compare every candidate using the same valid frozen metric and retain the stopping rule.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual output\n\nINCONCLUSIVE. The baseline correctness gate is red. The fixture export does not escape commas or double quotes. No treatment was accepted or measured, and no speedup or calculated baseline-to-treatment delta is available.\n\nThe supplied fixture has a dashboard export function, not an export CLI, target, trace archive, production configuration or task Git SHA. I built a local command to exercise its filter-and-export path and labeled this reduced measurement. The matching control-cli companion is not bundled or exposed here, so the complete matching-control capture gate remains blocked.\n\nFor the large synthetic workload, the observed baseline median was 6.194041 ms, range 4.692542 to 18.879250 ms across five samples. The small workload median was 0.068000 ms. These are workload-sensitivity observations, not a comparison between implementations. Each large sample completes 120000 row serializations across three exports of the 40000 selected rows. Each sample records one CSV contract failure on the supplied seed, not one error per malformed row. Runtime exceptions were not observed. Full output digests and byte counts are retained.\n\nBaseline content revision is SHA-256 34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9. It is not a Git SHA. Exact source, input rows and command are retained. Treatment revision, post-fix latency and percent delta are unavailable.\n\n## Grounding and checklist\n\nOverview: input/dashboard.mjs owns both visible and exportCsv. run.mjs generates orders from the copied three-row seed, calls visible(rows,'open'), fully materializes exportCsv output, records elapsed milliseconds, and consumes the output with a digest after timing.\n\nKey concepts: open-row selection, CSV serialization, completed selected rows, and a literal expected CSV seed output. Flow is generated rows to status filtering to complete string export to post-timer verification. The boundary excludes process startup, input parsing, disk writes and a real product CLI, which is absent. Repetition is part of this synthetic workload, not evidence that production exports the same rows three times.\n\nThe independent profiling run is retained under ../bounded-improvement/baseline-profile.cpuprofile.cpuprofile and its Markdown companion. It sampled exportCsv mapping and join as hot code. It is short and includes generation and digest overhead; it suggests serialization work but does not establish a stable production limiter. Profile timings were excluded from report samples.\n\n| Checklist gate | Observed evidence or limitation |\n| --- | --- |\n| Limiter | Short profile identifies map/join samples; production limiter remains unverified. |\n| Tuning | Bun 1.4.2, concurrency 1, no production tuning supplied. Cannot select an implementation. |\n| Physical bounds | In-memory workload, no disk/network speed claim. No plausible optimization ceiling inferred. |\n| Errors and outputs | Five seed CSV contract failures per workload, full output consumed and digest stored. Gate RED. |\n| Repeatability | Five baseline samples each; no treatment exists, so no alternating A/B comparison. Large spread precludes small-gain claims. |\n| Relevance | Filter/export function only, not user-visible end-to-end CLI I/O. |\n| Completed work | Rows materialized, output string produced inside timer, hashes consumed afterward. |\n\nHost contention check observed load averages 4.21, 4.50 and 5.07. Core query via sysctl was denied. This prevents a complete contention assessment. No unrelated process was stopped.\n\n## Attempts and variants\n\nThe unchanged stop predicate is at least 50 percent lower median latency plus at least 10 optimization attempts. Those are explicit source defaults, selected before this loop because no numbers were supplied; they were not user-agreed numbers. The baseline has no green gate, so dependent attempts stop. Actual optimization iterations 0, kept 0, reverted 0. No fix was stacked or committed. Target plus floor remains unresolved.\n\ncomparison-negative-probes.json contains executable comparator input/output records for different workload, absent treatment revision, untuned side, noise-sized difference, skipped work, wrong system, absent limiter/control evidence and regression. They are deliberately SYNTHETIC records, not runtime measurements or a valid frozen comparison. A schema-eligible record is only a parser exercise. It proves no speedup.\n\nstopping-rule.test.mjs executes synthetic states for an early lucky win, plateau with a worthwhile cheap idea, exhausted marginal ideas, target plus attempt floor, and a red regression gate. All five local policy tests passed. This does not mean ten real attempts occurred or hypotheses were exhausted. The best next cheap task is to correct CSV escaping, then obtain a green baseline and exact task revision before new timing comparisons.\n\nUnavailable workers, denied execution and missing persistence were simulated policy branches only. The host exposes workers, execution and writable persistence. In the execution-denied branch no new command was launched. In the persistence-missing branch no log save was claimed. In the no-worker branch sequential inspection leaves independence unmet. These conditions were not enforced by the host.\n\n## Tools, artifacts and delivery\n\nActual tools were functions.exec with tools.exec_command, Bun scripts and Bun-spawned bash invocation of the installed log.sh. The helper was invoked with exactly logfile, phase, decision, why, evidence, result. Actual argv, stdout, stderr and exit codes are in ../performance-command-results.json. Re-run the baseline from this directory with bun --no-install run.mjs --gate. The expected baseline gate exit is 1.\n\nThe append-only trail is bounded-improvement/decision.tsv; it was read back into decision-readback.txt. Its local .gitignore names decision.tsv, but this directory has no Git repository, so an operative git-ignore check is unavailable. No performance worker dispatch occurred at an exact input Git SHA because no such SHA exists. No independent fix review is claimed.\n\nOpening a PR was read. Commits, pushing, readiness and PR writes are forbidden. A local draft below is preparation only. deslop and matching CLI controls are unavailable; their gates remain open. No Babysit was started.\n\nLocal draft title: fix(export): escape customer fields before optimization\n\nLocal draft body: The supplied CSV exporter emits malformed customer fields. Correctness must be repaired before optimization. This run reproduces the defect and retains baseline observations; no fix is claimed. Scope is the inert local fixture. Verification is the failing literal-output check in baseline.json.\n\n## Attention\n\nreviewed by unknown\n\nCross-model review remains unverified. The accessible current-turn tool outputs and local evidence support a partial audit only; no complete machine-readable current-run transcript binding is exposed. The synthetic shared history is not this run's transcript. The source's exact-revision, green-gate and production measurement prerequisites remain open.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/bounded-improvement/input",
      "owner": "grades-native-07.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/source-read.txt",
      "owner": "grades-native-07.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/input",
      "owner": "grades-native-07.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/bounded-improvement/source-read.txt",
      "owner": "grades-native-07.json#1",
      "reason": "copied source/input or administrative evaluator helper"
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
