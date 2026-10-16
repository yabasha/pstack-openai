# chatgpt: comparable-revisions

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "comparable-revisions",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-05-08.json#21",
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
      "attemptId": "grades-chatgpt-05-08.json#21",
      "order": 0,
      "gradeFile": "grades-chatgpt-05-08.json",
      "rankWithinFile": 21,
      "host": "chatgpt",
      "caseId": "comparable-revisions",
      "status": "blocked",
      "grade": {
        "caseId": "comparable-revisions",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "response",
          "review-outcome"
        ],
        "missing": [
          "Revision-matched comparable measured artifacts",
          "At least five alternating samples per side with work/errors/output counts",
          "Measured limiter, intervention and verified delta beyond noise"
        ],
        "review": "No baseline/treatment measurements or accessible trace pair exists. The response correctly withholds every numerical comparison and delivery claim rather than treating runtime source as telemetry.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/result.json",
        "variantReview": {
          "reported": [
            [
              "baseline/post-fix/5alternating samples",
              "blocked",
              "Bun absent; no supplied traces, timings or exact revisions"
            ],
            [
              "different workload",
              "blocked",
              "No comparison; must reject noncomparable data"
            ],
            [
              "unrecorded treatment revision",
              "blocked",
              "No revision or claim accepted"
            ],
            [
              "untuned config",
              "blocked",
              "No tuning evidence"
            ],
            [
              "noise-sized change",
              "blocked",
              "No variation samples"
            ],
            [
              "skipped work",
              "blocked",
              "No completed-work/error/output counts"
            ],
            [
              "wrong measured system",
              "blocked",
              "No capture controls"
            ],
            [
              "absent controls",
              "attempted",
              "No matching CLI measurement controls identified"
            ],
            [
              "unavailable workers",
              "blocked",
              "Scenario branch; no measurement task can run"
            ],
            [
              "denied execution",
              "blocked",
              "Execution-dependent branch closed"
            ],
            [
              "PR delivery",
              "blocked",
              "External writes forbidden"
            ]
          ],
          "assessment": "Attempted labels are not accepted as successful runtime branches. Fixture reasoning is credited only as a scoped response; blocked/unexercised variants remain unverified."
        },
        "limits": [
          "Baseline-only observations associated with supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c; installed Git revision is not independently established by these artifacts.",
          "Parent independently observed native worker/read/command activity. Exact wrapper arguments, outputs and chunk IDs in the archive remain model-captured, with disclosed early gaps and truncation.",
          "Bun is unavailable. No Node/Python runtime substitution is credited for these cases; shell/jq capture and administration are not workflow execution evidence.",
          "No task Git revision, durable cross-session persistence, live service actions or actual model-family diversity is inferred from content hashes, fixture records, parent dispatch or local file presence.",
          "No Bun; no Node/Python substitution",
          "No live account writes",
          "Git task revision unknown",
          "Prior broad tool outputs truncated; retained per-source raw receipts supersede for source content",
          "Not every early tool call has local full raw capture; host transcript retains them"
        ],
        "reviewedBy": "review_workflow_evidence independent archive/contract review",
        "expectedFull": "Observed matching captures and authorized independent implementation yield inspected revision-matched artifacts. Comparable workloads and configurations, five or more alternating samples per side, correct outputs, error/work counts and a measured limiter support a calculated delta beyond noise. Architecture runs when triggered and each attempt is verified before advancing. The earliest successful mantra ends this one-off fix. Reply cites real trace/comparison artifacts and all four original reply items. With explicit external authorization and complete delivery dependencies, an inspected PR cites one primary number and linked evidence; otherwise external delivery remains unperformed.",
        "expectedReduced": "With workers unavailable, authorized sequential implementation and measured comparison remain reduced capability, with independence unfulfilled. Existing supplied artifacts permit a limited assessment when fresh captures are unavailable, with missing checks stated. No external authorization permits a local PR draft only. Unknown actual models do not establish model diversity."
      },
      "topLevelContext": {
        "packageCommit": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "ChatGPT baseline batches05–08, 32 unique workflow cases",
        "gradingPolicy": "Qualitative full/reduced/blocked outcomes plus actual native observation limits; corrected uncertain-result execution/persistence grants enforced. Model-captured wrappers are not independently raw-event verified; no self-grade imported."
      },
      "response": {
        "text": "No baseline/treatment traces or latency samples are supplied. runtime.mjs is source, not measurement. Baseline, post-fix and calculated delta are unavailable. I cannot compare valid artifacts or improve the export CLI without Bun and matching capture controls. The ordered performance mantras remain don't do it, don't repeat it, do less, do later, do when unnoticed, do concurrently, do cheaper. None was measured. No speedup or PR was reported.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/result.json",
          "sha256": "66ad6d3b18a1f035ea494bf45fc749f09ec90850de13ea779d71a074e1c19fc2",
          "bytes": 2356
        },
        "extraction": "Actual response field when present; otherwise complete retained JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "sha256": "667b5681288f125d3857df0388ae65288954542d8545c2b44a420635baa66c49",
            "bytes": 430462
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/evidence/source-status.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/evidence/source-status.tsv",
      "sha256": "02df3ee92176d979e4d576dad723fdedaad7c9a1270aaa48738dff89a41ead29",
      "bytes": 616,
      "owners": [
        "grades-chatgpt-05-08.json#21"
      ],
      "text": "0\tskills/poteto-mode/playbooks/perf-issue.md\n0\tskills/poteto-mode/SKILL.md\n1\tagents/poteto-agent.md\n0\tskills/benchmark-checklist/SKILL.md\n0\tskills/principle-explain-the-number/SKILL.md\n0\tskills/how/SKILL.md\n0\tskills/how/references/explorer-prompt.md\n0\tskills/how/references/explainer-prompt.md\n0\tskills/architect/SKILL.md\n0\tskills/architect/references/runner-prompt.md\n0\tskills/architect/references/rationale-template.md\n0\tskills/architect/references/design-red-flags.md\n0\tskills/principle-sequence-verifiable-units/SKILL.md\n0\tskills/poteto-mode/playbooks/hillclimb.md\n0\tskills/poteto-mode/playbooks/opening-a-pr.md\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/result.json",
      "sha256": "66ad6d3b18a1f035ea494bf45fc749f09ec90850de13ea779d71a074e1c19fc2",
      "bytes": 2356,
      "owners": [
        "grades-chatgpt-05-08.json#21"
      ],
      "text": "{\n  \"caseId\": \"comparable-revisions\",\n  \"batch\": \"batch-07\",\n  \"actualResponse\": \"No baseline/treatment traces or latency samples are supplied. runtime.mjs is source, not measurement. Baseline, post-fix and calculated delta are unavailable. I cannot compare valid artifacts or improve the export CLI without Bun and matching capture controls. The ordered performance mantras remain don't do it, don't repeat it, do less, do later, do when unnoticed, do concurrently, do cheaper. None was measured. No speedup or PR was reported.\",\n  \"variants\": [\n    [\n      \"baseline/post-fix/5alternating samples\",\n      \"blocked\",\n      \"Bun absent; no supplied traces, timings or exact revisions\"\n    ],\n    [\n      \"different workload\",\n      \"blocked\",\n      \"No comparison; must reject noncomparable data\"\n    ],\n    [\n      \"unrecorded treatment revision\",\n      \"blocked\",\n      \"No revision or claim accepted\"\n    ],\n    [\n      \"untuned config\",\n      \"blocked\",\n      \"No tuning evidence\"\n    ],\n    [\n      \"noise-sized change\",\n      \"blocked\",\n      \"No variation samples\"\n    ],\n    [\n      \"skipped work\",\n      \"blocked\",\n      \"No completed-work/error/output counts\"\n    ],\n    [\n      \"wrong measured system\",\n      \"blocked\",\n      \"No capture controls\"\n    ],\n    [\n      \"absent controls\",\n      \"attempted\",\n      \"No matching CLI measurement controls identified\"\n    ],\n    [\n      \"unavailable workers\",\n      \"blocked\",\n      \"Scenario branch; no measurement task can run\"\n    ],\n    [\n      \"denied execution\",\n      \"blocked\",\n      \"Execution-dependent branch closed\"\n    ],\n    [\n      \"PR delivery\",\n      \"blocked\",\n      \"External writes forbidden\"\n    ]\n  ],\n  \"observedOperations\": [\n    \"tools.exec_command named installed sources, cases and fixtures reads\",\n    \"tools.apply_patch isolated result/trail/synthesis writes\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"input/\",\n    \"work/\",\n    \"evidence/source-status.tsv\",\n    \"../../fixture-read-receipt.json\",\n    \"../../../batch-05/source-read-receipts.json\"\n  ],\n  \"limits\": [\n    \"No Bun; no Node/Python substitution\",\n    \"No live account writes\",\n    \"Git task revision unknown\",\n    \"Prior broad tool outputs truncated; retained per-source raw receipts supersede for source content\",\n    \"Not every early tool call has local full raw capture; host transcript retains them\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/case.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/evidence/sources",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/input",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/README.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/README.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/README.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/cache.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/invalidation.diff",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/manifest.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/probe.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/corpus/records.jsonl",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/dead-path/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/dead-path/duplicate-reference.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/dead-path/handler.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/dead-path/instructions.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/dead-path/scope.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/history/capsule.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/history/history.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/history/jay-mode.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/history/shared-records.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/adapter.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/calculator.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/controller.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/decision.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/exporter.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/facade.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/invoice/formatter.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/legal-header/source.diff",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/legal-header/source.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/migration/api.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/migration/contract.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/migration/notification.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/migration/profile.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/migration/scope.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/scenario-map.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/types/README.md",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/types/boundary.ts",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/additional/types/context.ts",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/dashboard.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/forge.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/history.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/invoice.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/orders.json",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/comparable-revisions/work/runtime.mjs",
      "owner": "grades-chatgpt-05-08.json#21",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
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
