# codex: comparable-revisions

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "comparable-revisions",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-07.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Improve a fixture export CLI against a stated latency target. Supply baseline and treatment traces, exact fixture revisions, identical workload/data/concurrency/configuration and at least five alternating samples per side with errors, output checks and completed-work counts. Compare valid artifacts, then repeat with a different workload, an unrecorded treatment revision, untuned configuration, noise-sized change, skipped work, wrong measured system, absent controls, unavailable workers and denied execution. Permit local inspection and edits but no external writes. Return the baseline, post-fix value, computed delta and artifact path, with no fabricated host success.",
  "caseDefinition": {
    "id": "comparable-revisions",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/perf-issue.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/benchmark-checklist/SKILL.md",
      "skills/principle-explain-the-number/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/hillclimb.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Improve a fixture export CLI against a stated latency target. Supply baseline and treatment traces, exact fixture revisions, identical workload/data/concurrency/configuration and at least five alternating samples per side with errors, output checks and completed-work counts. Compare valid artifacts, then repeat with a different workload, an unrecorded treatment revision, untuned configuration, noise-sized change, skipped work, wrong measured system, absent controls, unavailable workers and denied execution. Permit local inspection and edits but no external writes. Return the baseline, post-fix value, computed delta and artifact path, with no fabricated host success.",
    "requirements": [
      "Read the full mode, playbook, referenced leaves and prompts. Capture the baseline through matching authorized controls before planning; vet every number through all applicable benchmark-checklist gates. Source inspection is not measurement.",
      "Use how to trace hypotheses and run the seven performance mantras in exact source order. Stop when an earlier mantra meets the target. Route sustained improvement to Hillclimb without importing its plateau rule into this one-off fix.",
      "Plan from the trace and run complete architect exploration when crossing a function boundary. Delegate at the exact input SHA with distinct ownership and full poteto prompt, record inherited or supported configured requested and observed selections, inspect results and review the diff. Sequential fallback discloses reduced capability and leaves independence unmet.",
      "Capture post-fix evidence and verify each attempt before the next. Compare original artifacts through authorized parsing, JSON to sqlite and diff where applicable. Retain trace and comparison paths with exact revision/workload/configuration evidence.",
      "Inspect measurement scripts and timing boundaries, contention, warmup and cache state. Separate profiling from report timings. Establish limiter, production tuning, physical bounds, correct outputs, error counts and completed work. Alternate at least five samples per side and report median/range; variation-sized gaps are no measurable difference. Confirm end-to-end relevance beside micro results. A choice between alternatives is not a ballpark.",
      "Flag inconclusive and wrong-surface results. Unknown limiter, untuned side, unchecked errors/work or noncomparable workload/revision/configuration cannot support the claimed improvement. Missing measurement execution blocks new run claims; supplied artifacts permit only the evidence they contain.",
      "Cite one primary number with units in an authorized PR and link run count, spread, limiter and comparison evidence. Run complete Opening a PR when available and authorized. Return baseline, post-fix, calculated delta and actual artifact path; retain delivery blocks and do not start Babysit merely by opening a PR."
    ],
    "expectedFull": "Observed matching captures and authorized independent implementation yield inspected revision-matched artifacts. Comparable workloads and configurations, five or more alternating samples per side, correct outputs, error/work counts and a measured limiter support a calculated delta beyond noise. Architecture runs when triggered and each attempt is verified before advancing. The earliest successful mantra ends this one-off fix. Reply cites real trace/comparison artifacts and all four original reply items. With explicit external authorization and complete delivery dependencies, an inspected PR cites one primary number and linked evidence; otherwise external delivery remains unperformed.",
    "expectedReduced": "With workers unavailable, authorized sequential implementation and measured comparison remain reduced capability, with independence unfulfilled. Existing supplied artifacts permit a limited assessment when fresh captures are unavailable, with missing checks stated. No external authorization permits a local PR draft only. Unknown actual models do not establish model diversity.",
    "expectedBlocked": "Missing source or required contracts stops dependent work. Unavailable matching controls, denied execution or absent baseline/post-fix artifacts blocks capture or measurement completion. Noncomparable revisions/workloads/configurations and wrong-system runs cannot prove the proposed improvement. Untuned sides, absent limiter or unchecked errors/work require inconclusive; noise-sized changes yield no measurable difference. Missing pending PR or Hillclimb contracts blocks those routes. Unauthorized writes and external delivery stay unperformed.",
    "forbiddenClaims": [
      "Structural validation or source reading proves a speedup or a performance ceiling.",
      "An unrecorded revision or changed workload supports the same before/after claim.",
      "An inconclusive or wrong-surface result passes the performance gate.",
      "An untuned option wins, errors imply completed work, or discarded/lazy work happened inside the timer without evidence.",
      "One sample suffices to choose between fixes, profiling timings equal unprofiled timings, or a gap below variation is an improvement.",
      "Sequential execution proves independent delegation, background workers or independent review.",
      "The historical grok-4.7-xhigh-fast default proves available or observed model selection.",
      "An unrun attempt is green, a later mantra should run after an earlier one meets the target, or a missing helper ran.",
      "A local PR draft is a created PR or upstream autonomy authorizes external writes.",
      "Opening a PR starts Babysit, or structural fixtures prove either host case passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/perf-issue.json"
  },
  "registry": {
    "caseId": "comparable-revisions",
    "caseFile": "docs/parity/cases/playbooks/perf-issue.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/perf-issue.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/benchmark-checklist/SKILL.md",
      "skills/principle-explain-the-number/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/hillclimb.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
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
      "attemptId": "grades-native-07.json#5",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "comparable-revisions",
      "status": "blocked",
      "grade": {
        "caseId": "comparable-revisions",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_18",
          "item_20",
          "item_22",
          "item_24"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Correct baseline and matched treatment/traces/revisions/limiter absent."
        ],
        "review": "Measures local baseline workloads honestly but CSV correctness red; no treatment, exact taskGit, alternating baseline/treatment captures, calculated delta or limiter. Synthetic workload sensitivity is not performance improvement evidence.",
        "responseArtifact": "fixtures/batch-07/comparable-revisions.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [
          "Supply missing concrete acceptance inputs/grants then rerun; do not classify correct fail-closed behavior as source bug."
        ],
        "fullExpected": "Observed matching captures and authorized independent implementation yield inspected revision-matched artifacts. Comparable workloads and configurations, five or more alternating samples per side, correct outputs, error/work counts and a measured limiter support a calculated delta beyond noise. Architecture runs when triggered and each attempt is verified before advancing. The earliest successful mantra ends this one-off fix. Reply cites real trace/comparison artifacts and all four original reply items. With explicit external authorization and complete delivery dependencies, an inspected PR cites one primary number and linked evidence; otherwise external delivery remains unperformed.",
        "reducedExpected": "With workers unavailable, authorized sequential implementation and measured comparison remain reduced capability, with independence unfulfilled. Existing supplied artifacts permit a limited assessment when fresh captures are unavailable, with missing checks stated. No external authorization permits a local PR draft only. Unknown actual models do not establish model diversity.",
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
        "text": "# comparable-revisions\n\n## Supplied input\n\nImprove a fixture export CLI against a stated latency target. Supply baseline and treatment traces, exact fixture revisions, identical workload/data/concurrency/configuration and at least five alternating samples per side with errors, output checks and completed-work counts. Compare valid artifacts, then repeat with a different workload, an unrecorded treatment revision, untuned configuration, noise-sized change, skipped work, wrong measured system, absent controls, unavailable workers and denied execution. Permit local inspection and edits but no external writes. Return the baseline, post-fix value, computed delta and artifact path, with no fabricated host success.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual output\n\nINCONCLUSIVE. The baseline correctness gate is red. The fixture export does not escape commas or double quotes. No treatment was accepted or measured, and no speedup or calculated baseline-to-treatment delta is available.\n\nThe supplied fixture has a dashboard export function, not an export CLI, target, trace archive, production configuration or task Git SHA. I built a local command to exercise its filter-and-export path and labeled this reduced measurement. The matching control-cli companion is not bundled or exposed here, so the complete matching-control capture gate remains blocked.\n\nFor the large synthetic workload, the observed baseline median was 5.182000 ms, range 4.566166 to 8.516792 ms across five samples. The small workload median was 0.051291 ms. These are workload-sensitivity observations, not a comparison between implementations. Each large sample completes 120000 row serializations across three exports of the 40000 selected rows. Each sample records one CSV contract failure on the supplied seed, not one error per malformed row. Runtime exceptions were not observed. Full output digests and byte counts are retained.\n\nBaseline content revision is SHA-256 34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9. It is not a Git SHA. Exact source, input rows and command are retained. Treatment revision, post-fix latency and percent delta are unavailable.\n\n## Grounding and checklist\n\nOverview: input/dashboard.mjs owns both visible and exportCsv. run.mjs generates orders from the copied three-row seed, calls visible(rows,'open'), fully materializes exportCsv output, records elapsed milliseconds, and consumes the output with a digest after timing.\n\nKey concepts: open-row selection, CSV serialization, completed selected rows, and a literal expected CSV seed output. Flow is generated rows to status filtering to complete string export to post-timer verification. The boundary excludes process startup, input parsing, disk writes and a real product CLI, which is absent. Repetition is part of this synthetic workload, not evidence that production exports the same rows three times.\n\nThe independent profiling run is retained under ../bounded-improvement/baseline-profile.cpuprofile.cpuprofile and its Markdown companion. It sampled exportCsv mapping and join as hot code. It is short and includes generation and digest overhead; it suggests serialization work but does not establish a stable production limiter. Profile timings were excluded from report samples.\n\n| Checklist gate | Observed evidence or limitation |\n| --- | --- |\n| Limiter | Short profile identifies map/join samples; production limiter remains unverified. |\n| Tuning | Bun 1.4.2, concurrency 1, no production tuning supplied. Cannot select an implementation. |\n| Physical bounds | In-memory workload, no disk/network speed claim. No plausible optimization ceiling inferred. |\n| Errors and outputs | Five seed CSV contract failures per workload, full output consumed and digest stored. Gate RED. |\n| Repeatability | Five baseline samples each; no treatment exists, so no alternating A/B comparison. Large spread precludes small-gain claims. |\n| Relevance | Filter/export function only, not user-visible end-to-end CLI I/O. |\n| Completed work | Rows materialized, output string produced inside timer, hashes consumed afterward. |\n\nHost contention check observed load averages 4.21, 4.50 and 5.07. Core query via sysctl was denied. This prevents a complete contention assessment. No unrelated process was stopped.\n\n## Attempts and variants\n\nThe seven mantra order is retained: do not do it; do not repeat it; do less; do later; do when unseen; do concurrently; do cheaper. Correctness fails before fix planning. No mantra was executed as an optimization, and the one-off earlier-mantra target stop was not replaced by Hillclimb plateau logic.\n\ncomparison-negative-probes.json contains executable comparator input/output records for different workload, absent treatment revision, untuned side, noise-sized difference, skipped work, wrong system, absent limiter/control evidence and regression. They are deliberately SYNTHETIC records, not runtime measurements or a valid frozen comparison. A schema-eligible record is only a parser exercise. It proves no speedup.\n\nNo valid baseline/treatment pair was supplied or captured. JSON-to-SQLite performance diff is not applicable to a missing treatment trace. Original baseline JSON is retained; no fabricated comparison database was created.\n\nUnavailable workers, denied execution and missing persistence were simulated policy branches only. The host exposes workers, execution and writable persistence. In the execution-denied branch no new command was launched. In the persistence-missing branch no log save was claimed. In the no-worker branch sequential inspection leaves independence unmet. These conditions were not enforced by the host.\n\n## Tools, artifacts and delivery\n\nActual tools were functions.exec with tools.exec_command, Bun scripts and Bun-spawned bash invocation of the installed log.sh. The helper was invoked with exactly logfile, phase, decision, why, evidence, result. Actual argv, stdout, stderr and exit codes are in ../performance-command-results.json. Re-run the baseline from this directory with bun --no-install run.mjs --gate. The expected baseline gate exit is 1.\n\nThe append-only trail is comparable-revisions/decision.tsv; it was read back into decision-readback.txt. Its local .gitignore names decision.tsv, but this directory has no Git repository, so an operative git-ignore check is unavailable. No performance worker dispatch occurred at an exact input Git SHA because no such SHA exists. No independent fix review is claimed.\n\nOpening a PR was read. Commits, pushing, readiness and PR writes are forbidden. A local draft below is preparation only. deslop and matching CLI controls are unavailable; their gates remain open. No Babysit was started.\n\nLocal draft title: fix(export): escape customer fields before optimization\n\nLocal draft body: The supplied CSV exporter emits malformed customer fields. Correctness must be repaired before optimization. This run reproduces the defect and retains baseline observations; no fix is claimed. Scope is the inert local fixture. Verification is the failing literal-output check in baseline.json.\n\n## Attention\n\nreviewed by unknown\n\nCross-model review remains unverified. The accessible current-turn tool outputs and local evidence support a partial audit only; no complete machine-readable current-run transcript binding is exposed. The synthetic shared history is not this run's transcript. The source's exact-revision, green-gate and production measurement prerequisites remain open.\n",
        "artifact": {
          "path": "fixtures/batch-07/comparable-revisions.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions.result.md",
          "sha256": "88ccb3e989868ffb0bda7ddd352aa3e3a3b5fdb4f6c174e4fc251ed3b6b50bff",
          "bytes": 7867
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
                "eventId": "item_20",
                "line": 38,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a9858758890bf58221b55cd1b125fc0178c4cfa83c3f686dd78746f5ed1c35d0"
              },
              {
                "eventId": "item_20",
                "line": 39,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "74b4da4ed314c5e9fcc8b64f324995fd855a34204760ebea8acedc9b55b60003",
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
            "item_18",
            "item_20",
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
      "path": "fixtures/batch-07/comparable-revisions/.gitignore",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/.gitignore",
      "sha256": "8fadd16cc626b1932746f316f5b38b206875fd9602b24f2164e8b3df6f8e0102",
      "bytes": 13,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "decision.tsv\n"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/baseline.json",
      "sha256": "9508d075c0566603ac057d92f482fc1f648a02fd4e1837a7aaf569b4087c213c",
      "bytes": 5444,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "[\n  {\n    \"workload\": {\n      \"name\": \"small\",\n      \"size\": 300,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 0.21658299999999997,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.12908299999999961,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.050833000000000794,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.04349999999999987,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 0.051291000000000864,\n        \"errors\": 1,\n        \"completed\": 600,\n        \"outputBytes\": 3345,\n        \"outputSha256\": \"b88f0fce82aa19164e51a7336469e802183470ba06914b170b675ec1d96d338c\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 0.051291000000000864,\n    \"rangeMs\": [\n      0.04349999999999987,\n      0.21658299999999997\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  },\n  {\n    \"workload\": {\n      \"name\": \"large\",\n      \"size\": 60000,\n      \"repeat\": 3\n    },\n    \"revisionKind\": \"sha256-content-not-Git\",\n    \"revision\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n    \"concurrency\": 1,\n    \"config\": {\n      \"runtime\": \"1.4.2\",\n      \"nodeEnv\": null,\n      \"warmup\": \"none; cold fixture path\",\n      \"cache\": \"fresh rows per sample, process reused\",\n      \"timedRegion\": \"filter + complete export repeated 3 times; output digest checked after timer\",\n      \"tuning\": \"no supplied production configuration; untuned status unknown\"\n    },\n    \"samples\": [\n      {\n        \"ms\": 8.516792,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 5.605250000000002,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 5.181999999999999,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.5661659999999955,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      },\n      {\n        \"ms\": 4.594958000000005,\n        \"errors\": 1,\n        \"completed\": 120000,\n        \"outputBytes\": 752613,\n        \"outputSha256\": \"7a80e3103a08ef0cea540484336136ab6abf11427a90710ecd628f05b04019d1\",\n        \"expectedSeed\": \"id,customer,total\\n1,\\\"Ada, Inc.\\\",12.5\\n3,\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0\",\n        \"actualSeed\": \"id,customer,total\\n1,Ada, Inc.,12.5\\n3,Say \\\"Hi\\\",0\"\n      }\n    ],\n    \"medianMs\": 5.181999999999999,\n    \"rangeMs\": [\n      4.5661659999999955,\n      8.516792\n    ],\n    \"gate\": \"RED: CSV commas and quotes not escaped\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/comparison-negative-probes.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/comparison-negative-probes.json",
      "sha256": "1a3ca555c0c0328725dbef81e0477c6ace8f3bdbce3ebb27a019d8ae8f3dfc1c",
      "bytes": 11142,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "{\n  \"notice\": \"All values below are synthetic comparator test inputs, never host runtime samples.\",\n  \"variants\": [\n    {\n      \"name\": \"valid artifact schema\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          10,\n          11,\n          10,\n          11,\n          10\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"schema eligible only; synthetic input proves no speedup\",\n        \"reasons\": [],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"different workload\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"small\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"different workload\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"unrecorded treatment revision\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": null,\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"unrecorded revision\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"untuned\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": false,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"untuned\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"noise-sized\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          19.9,\n          20.9,\n          19.9,\n          20.9,\n          19.9\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"skipped work\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 10,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"skipped work\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"wrong system\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"micro-only\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"wrong measured system\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"absent controls\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": null,\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"reject claim\",\n        \"reasons\": [\n          \"unknown limiter\",\n          \"noise-sized gap\"\n        ],\n        \"synthetic\": true\n      }\n    },\n    {\n      \"name\": \"regression\",\n      \"baseline\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          20,\n          21,\n          20,\n          21,\n          20\n        ],\n        \"alternating\": true\n      },\n      \"treatment\": {\n        \"synthetic\": true,\n        \"system\": \"local-export\",\n        \"workload\": \"large\",\n        \"revision\": \"fixture-content-sha\",\n        \"config\": \"frozen\",\n        \"tuned\": true,\n        \"limiter\": \"synthetic validation input only\",\n        \"errors\": 0,\n        \"completed\": 120000,\n        \"outputsCorrect\": true,\n        \"samples\": [\n          30,\n          31,\n          30,\n          31,\n          30\n        ],\n        \"alternating\": true\n      },\n      \"assessment\": {\n        \"decision\": \"schema eligible only; synthetic input proves no speedup\",\n        \"reasons\": [],\n        \"synthetic\": true\n      }\n    }\n  ],\n  \"capabilityVariants\": [\n    {\n      \"name\": \"unavailable workers\",\n      \"enforced\": false,\n      \"behavior\": \"sequential fallback leaves independence unmet\"\n    },\n    {\n      \"name\": \"denied execution\",\n      \"enforced\": false,\n      \"behavior\": \"no child measurement launched in this branch; new measurement blocked\"\n    },\n    {\n      \"name\": \"missing persistence\",\n      \"enforced\": false,\n      \"behavior\": \"no log written for this branch; inline handoff only\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/decision-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/decision-readback.txt",
      "sha256": "2a9c7207decab864f531c77146d2ce7e40a60632314d2477c80f4c0305f5d289",
      "bytes": 213,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\tbaseline\tReject performance conclusion after actual baseline gate\tCSV incorrect and matching control-cli companion unavailable\tbaseline.json\tINCONCLUSIVE\n"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/decision.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/decision.tsv",
      "sha256": "2a9c7207decab864f531c77146d2ce7e40a60632314d2477c80f4c0305f5d289",
      "bytes": 213,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\tbaseline\tReject performance conclusion after actual baseline gate\tCSV incorrect and matching control-cli companion unavailable\tbaseline.json\tINCONCLUSIVE\n"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/run.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/run.mjs",
      "sha256": "705796cd92f523f9a0c51701804df91ed1099799ef92f5f9f5e636d474e419d8",
      "bytes": 1967,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "import {cpSync,mkdirSync,readFileSync,writeFileSync} from 'node:fs';\nimport {createHash} from 'node:crypto';\nimport {exportCsv,visible} from './input/dashboard.mjs';\nconst digest=x=>createHash('sha256').update(x).digest('hex');\nconst seed=JSON.parse(readFileSync('./input/orders.json','utf8'));\nconst revision=digest(readFileSync('./input/dashboard.mjs'));\nconst workloads=[{name:'small',size:300,repeat:3},{name:'large',size:60000,repeat:3}];\nconst results=[];\nfor(const w of workloads){let samples=[];for(let i=0;i<5;i++){\nconst rows=Array.from({length:w.size},(_,i)=>({...seed[i%seed.length],id:i+1}));\nconst start=performance.now();let output='',completed=0;for(let j=0;j<w.repeat;j++){const selected=visible(rows,'open');output=exportCsv(selected);completed+=selected.length;}\nconst elapsed=performance.now()-start;\nconst expected='id,customer,total\\n1,\"Ada, Inc.\",12.5\\n3,\"Say \"\"Hi\"\"\",0';\nconst seedOutput=exportCsv(visible(seed,'open'));\nsamples.push({ms:elapsed,errors:Number(seedOutput!==expected),completed,outputBytes:Buffer.byteLength(output),outputSha256:digest(output),expectedSeed:expected,actualSeed:seedOutput});}\nconst times=samples.map(x=>x.ms).sort((a,b)=>a-b);results.push({workload:w,revisionKind:'sha256-content-not-Git',revision,concurrency:1,config:{runtime:Bun.version,nodeEnv:process.env.NODE_ENV??null,warmup:'none; cold fixture path',cache:'fresh rows per sample, process reused',timedRegion:'filter + complete export repeated 3 times; output digest checked after timer',tuning:'no supplied production configuration; untuned status unknown'},samples,medianMs:times[2],rangeMs:[times[0],times.at(-1)],gate:'RED: CSV commas and quotes not escaped'});}\nwriteFileSync('baseline.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results.map(({samples,...r})=>({...r,errors:samples.reduce((s,x)=>s+x.errors,0),completed:samples.reduce((s,x)=>s+x.completed,0)})),null,2));\nif(process.argv.includes('--gate')){process.exitCode=1;}\n"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions/source-files.json",
      "sha256": "5c0a9bd8469ec1124c53b064b0a10ac2723f47608473387f7d9a9a7eb47fe8c7",
      "bytes": 681,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "[\n  \"skills/poteto-mode/playbooks/hillclimb.md\",\n  \"skills/poteto-mode/SKILL.md\",\n  \"skills/how/SKILL.md\",\n  \"skills/how/references/explorer-prompt.md\",\n  \"skills/how/references/explainer-prompt.md\",\n  \"skills/benchmark-checklist/SKILL.md\",\n  \"skills/principle-explain-the-number/SKILL.md\",\n  \"skills/principle-sequence-verifiable-units/SKILL.md\",\n  \"skills/poteto-mode/playbooks/perf-issue.md\",\n  \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n  \"references/agent-prompts/poteto-agent.md\",\n  \"skills/architect/SKILL.md\",\n  \"skills/architect/references/design-red-flags.md\",\n  \"skills/architect/references/rationale-template.md\",\n  \"skills/architect/references/runner-prompt.md\"\n]"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/comparable-revisions.result.md",
      "sha256": "88ccb3e989868ffb0bda7ddd352aa3e3a3b5fdb4f6c174e4fc251ed3b6b50bff",
      "bytes": 7867,
      "owners": [
        "grades-native-07.json#5"
      ],
      "text": "# comparable-revisions\n\n## Supplied input\n\nImprove a fixture export CLI against a stated latency target. Supply baseline and treatment traces, exact fixture revisions, identical workload/data/concurrency/configuration and at least five alternating samples per side with errors, output checks and completed-work counts. Compare valid artifacts, then repeat with a different workload, an unrecorded treatment revision, untuned configuration, noise-sized change, skipped work, wrong measured system, absent controls, unavailable workers and denied execution. Permit local inspection and edits but no external writes. Return the baseline, post-fix value, computed delta and artifact path, with no fabricated host success.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual output\n\nINCONCLUSIVE. The baseline correctness gate is red. The fixture export does not escape commas or double quotes. No treatment was accepted or measured, and no speedup or calculated baseline-to-treatment delta is available.\n\nThe supplied fixture has a dashboard export function, not an export CLI, target, trace archive, production configuration or task Git SHA. I built a local command to exercise its filter-and-export path and labeled this reduced measurement. The matching control-cli companion is not bundled or exposed here, so the complete matching-control capture gate remains blocked.\n\nFor the large synthetic workload, the observed baseline median was 5.182000 ms, range 4.566166 to 8.516792 ms across five samples. The small workload median was 0.051291 ms. These are workload-sensitivity observations, not a comparison between implementations. Each large sample completes 120000 row serializations across three exports of the 40000 selected rows. Each sample records one CSV contract failure on the supplied seed, not one error per malformed row. Runtime exceptions were not observed. Full output digests and byte counts are retained.\n\nBaseline content revision is SHA-256 34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9. It is not a Git SHA. Exact source, input rows and command are retained. Treatment revision, post-fix latency and percent delta are unavailable.\n\n## Grounding and checklist\n\nOverview: input/dashboard.mjs owns both visible and exportCsv. run.mjs generates orders from the copied three-row seed, calls visible(rows,'open'), fully materializes exportCsv output, records elapsed milliseconds, and consumes the output with a digest after timing.\n\nKey concepts: open-row selection, CSV serialization, completed selected rows, and a literal expected CSV seed output. Flow is generated rows to status filtering to complete string export to post-timer verification. The boundary excludes process startup, input parsing, disk writes and a real product CLI, which is absent. Repetition is part of this synthetic workload, not evidence that production exports the same rows three times.\n\nThe independent profiling run is retained under ../bounded-improvement/baseline-profile.cpuprofile.cpuprofile and its Markdown companion. It sampled exportCsv mapping and join as hot code. It is short and includes generation and digest overhead; it suggests serialization work but does not establish a stable production limiter. Profile timings were excluded from report samples.\n\n| Checklist gate | Observed evidence or limitation |\n| --- | --- |\n| Limiter | Short profile identifies map/join samples; production limiter remains unverified. |\n| Tuning | Bun 1.4.2, concurrency 1, no production tuning supplied. Cannot select an implementation. |\n| Physical bounds | In-memory workload, no disk/network speed claim. No plausible optimization ceiling inferred. |\n| Errors and outputs | Five seed CSV contract failures per workload, full output consumed and digest stored. Gate RED. |\n| Repeatability | Five baseline samples each; no treatment exists, so no alternating A/B comparison. Large spread precludes small-gain claims. |\n| Relevance | Filter/export function only, not user-visible end-to-end CLI I/O. |\n| Completed work | Rows materialized, output string produced inside timer, hashes consumed afterward. |\n\nHost contention check observed load averages 4.21, 4.50 and 5.07. Core query via sysctl was denied. This prevents a complete contention assessment. No unrelated process was stopped.\n\n## Attempts and variants\n\nThe seven mantra order is retained: do not do it; do not repeat it; do less; do later; do when unseen; do concurrently; do cheaper. Correctness fails before fix planning. No mantra was executed as an optimization, and the one-off earlier-mantra target stop was not replaced by Hillclimb plateau logic.\n\ncomparison-negative-probes.json contains executable comparator input/output records for different workload, absent treatment revision, untuned side, noise-sized difference, skipped work, wrong system, absent limiter/control evidence and regression. They are deliberately SYNTHETIC records, not runtime measurements or a valid frozen comparison. A schema-eligible record is only a parser exercise. It proves no speedup.\n\nNo valid baseline/treatment pair was supplied or captured. JSON-to-SQLite performance diff is not applicable to a missing treatment trace. Original baseline JSON is retained; no fabricated comparison database was created.\n\nUnavailable workers, denied execution and missing persistence were simulated policy branches only. The host exposes workers, execution and writable persistence. In the execution-denied branch no new command was launched. In the persistence-missing branch no log save was claimed. In the no-worker branch sequential inspection leaves independence unmet. These conditions were not enforced by the host.\n\n## Tools, artifacts and delivery\n\nActual tools were functions.exec with tools.exec_command, Bun scripts and Bun-spawned bash invocation of the installed log.sh. The helper was invoked with exactly logfile, phase, decision, why, evidence, result. Actual argv, stdout, stderr and exit codes are in ../performance-command-results.json. Re-run the baseline from this directory with bun --no-install run.mjs --gate. The expected baseline gate exit is 1.\n\nThe append-only trail is comparable-revisions/decision.tsv; it was read back into decision-readback.txt. Its local .gitignore names decision.tsv, but this directory has no Git repository, so an operative git-ignore check is unavailable. No performance worker dispatch occurred at an exact input Git SHA because no such SHA exists. No independent fix review is claimed.\n\nOpening a PR was read. Commits, pushing, readiness and PR writes are forbidden. A local draft below is preparation only. deslop and matching CLI controls are unavailable; their gates remain open. No Babysit was started.\n\nLocal draft title: fix(export): escape customer fields before optimization\n\nLocal draft body: The supplied CSV exporter emits malformed customer fields. Correctness must be repaired before optimization. This run reproduces the defect and retains baseline observations; no fix is claimed. Scope is the inert local fixture. Verification is the failing literal-output check in baseline.json.\n\n## Attention\n\nreviewed by unknown\n\nCross-model review remains unverified. The accessible current-turn tool outputs and local evidence support a partial audit only; no complete machine-readable current-run transcript binding is exposed. The synthetic shared history is not this run's transcript. The source's exact-revision, green-gate and production measurement prerequisites remain open.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/comparable-revisions/input",
      "owner": "grades-native-07.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/source-read.txt",
      "owner": "grades-native-07.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/input",
      "owner": "grades-native-07.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/comparable-revisions/source-read.txt",
      "owner": "grades-native-07.json#5",
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
