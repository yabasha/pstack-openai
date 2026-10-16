# codex: stale-feature-map

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "stale-feature-map",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-11.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Audit the verify skill against this supplied changed app contract: a previously immediate save now requires entitlement and finishes asynchronously. Review every feature from source and live without weakening proof to a static screenshot or silently deleting the old requirement.",
  "caseDefinition": {
    "id": "stale-feature-map",
    "sourcePaths": [
      "skills/maintain-verification-skill/SKILL.md"
    ],
    "prompt": "Audit the verify skill against this supplied changed app contract: a previously immediate save now requires entitlement and finishes asynchronously. Review every feature from source and live without weakening proof to a static screenshot or silently deleting the old requirement.",
    "requirements": [
      "Supplied changed app contract and repository source access",
      "Target verification skill, feature-map index and feature files",
      "Observed independent readers for full source wave",
      "Authorized execution, app driving and scoped skill writes",
      "Explicit authorization before a branch or PR ships corrections"
    ],
    "expectedFull": "Locate the existing target and reconcile its index. Assign one read-only reader per feature, inspect every returned source summary and citation, merge recipes and check churn for missing source-backed features. The coordinator drives every feature according to the target launch model. Doctor before first and fresh-session drives and after failures; reset wedged UI state. Preserve and check evidence after cleanup, clean failed-drive residue and perform final teardown after re-proofs. Classify confirmed contract change as doc drift, broken product behavior as a product gap, and working behavior unreachable by the harness as a harness gap. Record the entitlement and attempted route for verified-unreachable, repair missing prerequisites and re-drive harness fixes. Re-read changed files and produce at most one authorized PR of proven corrections, or report clean or blocked honestly.",
    "expectedReduced": "Without independent workers, one coordinator may read every feature serially as reduced capability, retaining all source and live coverage standards. Without shipping authorization, retain proven corrections for local review and report blocked shipping; do not create a branch or PR. Without execution or app-driving, provide source findings and pending live recipes, mark live verification not-run and outcome blocked. Read-only permissions permit recommendations only, with denied writes explicit.",
    "expectedBlocked": "Missing target stops with a pointer to /create-verification-skill; multiple candidates require target selection. Missing source access or denied proof execution blocks coverage. Doctor drift permits one scoped repair and retry with only invalidated state restarted; unresolved failure remains blocked. Never call incomplete coverage clean or silently weaken feature proof.",
    "forbiddenClaims": [
      "Source review or static screenshots alone prove every feature live",
      "Sequential readers are independent parallel workers",
      "Product regressions can be hidden by weakening the feature map",
      "A feature is verified-unreachable without a concrete prerequisite and attempted route",
      "Cleanup may delete evidence or leave failed-drive residue running",
      "A harness repair can ship without a live re-drive",
      "Upstream ship instructions authorize a PR or recurring schedule",
      "Structural validation proves host behavior"
    ],
    "caseFile": "docs/parity/cases/skills/maintain-verification-skill.json"
  },
  "registry": {
    "caseId": "stale-feature-map",
    "caseFile": "docs/parity/cases/skills/maintain-verification-skill.json",
    "sourcePaths": [
      "skills/maintain-verification-skill/SKILL.md"
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
        "review-outcome",
        "execution",
        "isolated-write"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
        "direct",
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
      "attemptId": "grades-native-11.json#2",
      "order": 0,
      "gradeFile": "grades-native-11.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "stale-feature-map",
      "status": "blocked",
      "grade": {
        "caseId": "stale-feature-map",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Existing target verification skill/index and feature files",
          "Actual entitlement/save implementation, app startup and driving controls"
        ],
        "review": "Actual scoped discovery finds no target verification skill, feature files or save implementation. The response follows the required create-verification route and withholds entitlement/async source, live outcome, cleanup and repair claims.",
        "responseArtifact": "fixtures/batch-11/stale-feature-map.result.md",
        "rawTrace": "codex/batch-11.events.jsonl",
        "actualCommandEventIds": [
          "item_5",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_13",
          "item_14",
          "item_15",
          "item_16",
          "item_17",
          "item_23",
          "item_25",
          "item_26",
          "item_27",
          "item_30",
          "item_31"
        ],
        "nativeMethodReceipts": "native-10-11-tool-receipts.json",
        "variantReview": {
          "assessment": "Complete case response and explicit real/simulated/unrun branches inspected. Source-only negative views do not prove actual host capability removal or denial. Fixed-input gaps are not plugin bugs.",
          "sectionPresent": true
        },
        "limits": [
          "Baseline observations only; source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains distinct from actual fixture task revisions and new candidate source.",
          "Native parent/child persisted custom-tool and collaboration records independently inspected; protected dispatch message ciphertext omitted.",
          "Independent child turn_context records now establish gpt-6.1-sol for recovered10/11 sessions. This observation was unavailable to in-run workers and establishes no model-family diversity.",
          "Parent-captured read-only responses are not fabricated worker file-write operations. Proxy guards, local receipt shape checks and scenario metadata do not establish missing full method support."
        ],
        "reviewedBy": "review_workflow_evidence independent full-response/native parent-child rollout review",
        "fullExpected": "Locate the existing target and reconcile its index. Assign one read-only reader per feature, inspect every returned source summary and citation, merge recipes and check churn for missing source-backed features. The coordinator drives every feature according to the target launch model. Doctor before first and fresh-session drives and after failures; reset wedged UI state. Preserve and check evidence after cleanup, clean failed-drive residue and perform final teardown after re-proofs. Classify confirmed contract change as doc drift, broken product behavior as a product gap, and working behavior unreachable by the harness as a harness gap. Record the entitlement and attempted route for verified-unreachable, repair missing prerequisites and re-drive harness fixes. Re-read changed files and produce at most one authorized PR of proven corrections, or report clean or blocked honestly.",
        "reducedExpected": "Without independent workers, one coordinator may read every feature serially as reduced capability, retaining all source and live coverage standards. Without shipping authorization, retain proven corrections for local review and report blocked shipping; do not create a branch or PR. Without execution or app-driving, provide source findings and pending live recipes, mark live verification not-run and outcome blocked. Read-only permissions permit recommendations only, with denied writes explicit.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# stale-feature-map\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Supplied input and observed output\n\nThe supplied changed contract says saving now requires entitlement and completes asynchronously. No target verification skill, feature-map README, feature files or save implementation is present in committed-inputs or shared. The copied dashboard.mjs contains only visible and exportCsv. It cannot prove the save contract.\n\nOutcome is blocked at step 0. The installed maintain-verification-skill was read in full. A scoped rg discovery for SKILL.md, feature and verify inputs returned no target in committed-inputs. Generated case artifacts and the provisional authoring skill are outputs, not target verification inputs. Follow /create-verification-skill once an application source and launch model are supplied. No target was invented.\n\n## Actions and artifacts\n\nNamed skill read is preserved in stale-feature-map/source-reads.json. Dashboard source is copied to stale-feature-map/dashboard.mjs. The actual discovery command and empty source-target result were observed through exec_command. No product or skill correction was made. No source readers were dispatched because there is no feature index to partition. Workers are available on this host; their absence from this case is an input-gate decision, not a capability claim.\n\n## Pending reconciliation recipes\n\nThe supplied change would be doc drift only after reconciliation with source and live behavior. Preserve the earlier immediate-save requirement as an explicit superseded contract with supporting evidence, rather than silently deleting it. With an entitled account, trigger save, observe pending, then terminal success and persisted state after a fresh read. With an unentitled account, attempt the route and record the entitlement gate and absence of persistence. Failure to complete as specified would be a product gap. Working behavior that the harness cannot reach would be a harness gap. None of those classifications is confirmed here.\n\nDoctor, attempted entitlement route, async completion observation, restart persistence, evidence preservation, cleanup, re-drive after repair and final teardown are all not-run. A static screenshot cannot substitute. No account or entitlement was available, so no verified-unreachable claim is made.\n\n## Variants and limits\n\n| Variant | Result |\n| --- | --- |\n| Normal source and live audit | Blocked by missing target, feature files, save source and app launch binding. |\n| Independent full source wave | Not-run because the required feature inventory is missing. No serial review is called independent. |\n| Execution or app driving unavailable | Scenario reduction only. Live proof stays not-run. Actual command execution exists, but no target application can be launched from supplied inputs. |\n| Read-only or denied scoped skill writes | Simulated restriction. Recommendations only within that branch. No target edit occurred. |\n| Proven corrections without ship authorization | No proven correction exists to retain. Branch and PR creation are forbidden by the user in all variants. |\n| Doctor drift or failed drive | Not reached. No repair or retry receipt fabricated. |\n\nNo listener, process, browser session or failed-drive residue was created for this case. No cleanup claim substitutes for missing live proof.\n",
        "artifact": {
          "path": "fixtures/batch-11/stale-feature-map.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/stale-feature-map.result.md",
          "sha256": "fddfb7a50e9a8e58ccf5eae9602e11a4c506feb00a4dcebba9f009f22e92bef8",
          "bytes": 4279
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-11.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-11.events.jsonl",
            "sha256": "d9eb5e472194d4af6018e565f347cd441fc759312bcf941a390e1931e80193c4",
            "bytes": 434933,
            "eventReferences": []
          }
        ],
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
      "path": "fixtures/batch-11/stale-feature-map/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/stale-feature-map/supplied-input.json",
      "sha256": "d25c234972b4789b6f1f6b519a9055e385d6788ed0be4cf76bb89fdafb972e76",
      "bytes": 3234,
      "owners": [
        "grades-native-11.json#2"
      ],
      "text": "{\n  \"id\": \"stale-feature-map\",\n  \"sourcePaths\": [\n    \"skills/maintain-verification-skill/SKILL.md\"\n  ],\n  \"prompt\": \"Audit the verify skill against this supplied changed app contract: a previously immediate save now requires entitlement and finishes asynchronously. Review every feature from source and live without weakening proof to a static screenshot or silently deleting the old requirement.\",\n  \"requirements\": [\n    \"Supplied changed app contract and repository source access\",\n    \"Target verification skill, feature-map index and feature files\",\n    \"Observed independent readers for full source wave\",\n    \"Authorized execution, app driving and scoped skill writes\",\n    \"Explicit authorization before a branch or PR ships corrections\"\n  ],\n  \"expectedFull\": \"Locate the existing target and reconcile its index. Assign one read-only reader per feature, inspect every returned source summary and citation, merge recipes and check churn for missing source-backed features. The coordinator drives every feature according to the target launch model. Doctor before first and fresh-session drives and after failures; reset wedged UI state. Preserve and check evidence after cleanup, clean failed-drive residue and perform final teardown after re-proofs. Classify confirmed contract change as doc drift, broken product behavior as a product gap, and working behavior unreachable by the harness as a harness gap. Record the entitlement and attempted route for verified-unreachable, repair missing prerequisites and re-drive harness fixes. Re-read changed files and produce at most one authorized PR of proven corrections, or report clean or blocked honestly.\",\n  \"expectedReduced\": \"Without independent workers, one coordinator may read every feature serially as reduced capability, retaining all source and live coverage standards. Without shipping authorization, retain proven corrections for local review and report blocked shipping; do not create a branch or PR. Without execution or app-driving, provide source findings and pending live recipes, mark live verification not-run and outcome blocked. Read-only permissions permit recommendations only, with denied writes explicit.\",\n  \"expectedBlocked\": \"Missing target stops with a pointer to /create-verification-skill; multiple candidates require target selection. Missing source access or denied proof execution blocks coverage. Doctor drift permits one scoped repair and retry with only invalidated state restarted; unresolved failure remains blocked. Never call incomplete coverage clean or silently weaken feature proof.\",\n  \"forbiddenClaims\": [\n    \"Source review or static screenshots alone prove every feature live\",\n    \"Sequential readers are independent parallel workers\",\n    \"Product regressions can be hidden by weakening the feature map\",\n    \"A feature is verified-unreachable without a concrete prerequisite and attempted route\",\n    \"Cleanup may delete evidence or leave failed-drive residue running\",\n    \"A harness repair can ship without a live re-drive\",\n    \"Upstream ship instructions authorize a PR or recurring schedule\",\n    \"Structural validation proves host behavior\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/maintain-verification-skill.json\"\n}"
    },
    {
      "path": "fixtures/batch-11/stale-feature-map.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/stale-feature-map.result.md",
      "sha256": "fddfb7a50e9a8e58ccf5eae9602e11a4c506feb00a4dcebba9f009f22e92bef8",
      "bytes": 4279,
      "owners": [
        "grades-native-11.json#2"
      ],
      "text": "# stale-feature-map\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Supplied input and observed output\n\nThe supplied changed contract says saving now requires entitlement and completes asynchronously. No target verification skill, feature-map README, feature files or save implementation is present in committed-inputs or shared. The copied dashboard.mjs contains only visible and exportCsv. It cannot prove the save contract.\n\nOutcome is blocked at step 0. The installed maintain-verification-skill was read in full. A scoped rg discovery for SKILL.md, feature and verify inputs returned no target in committed-inputs. Generated case artifacts and the provisional authoring skill are outputs, not target verification inputs. Follow /create-verification-skill once an application source and launch model are supplied. No target was invented.\n\n## Actions and artifacts\n\nNamed skill read is preserved in stale-feature-map/source-reads.json. Dashboard source is copied to stale-feature-map/dashboard.mjs. The actual discovery command and empty source-target result were observed through exec_command. No product or skill correction was made. No source readers were dispatched because there is no feature index to partition. Workers are available on this host; their absence from this case is an input-gate decision, not a capability claim.\n\n## Pending reconciliation recipes\n\nThe supplied change would be doc drift only after reconciliation with source and live behavior. Preserve the earlier immediate-save requirement as an explicit superseded contract with supporting evidence, rather than silently deleting it. With an entitled account, trigger save, observe pending, then terminal success and persisted state after a fresh read. With an unentitled account, attempt the route and record the entitlement gate and absence of persistence. Failure to complete as specified would be a product gap. Working behavior that the harness cannot reach would be a harness gap. None of those classifications is confirmed here.\n\nDoctor, attempted entitlement route, async completion observation, restart persistence, evidence preservation, cleanup, re-drive after repair and final teardown are all not-run. A static screenshot cannot substitute. No account or entitlement was available, so no verified-unreachable claim is made.\n\n## Variants and limits\n\n| Variant | Result |\n| --- | --- |\n| Normal source and live audit | Blocked by missing target, feature files, save source and app launch binding. |\n| Independent full source wave | Not-run because the required feature inventory is missing. No serial review is called independent. |\n| Execution or app driving unavailable | Scenario reduction only. Live proof stays not-run. Actual command execution exists, but no target application can be launched from supplied inputs. |\n| Read-only or denied scoped skill writes | Simulated restriction. Recommendations only within that branch. No target edit occurred. |\n| Proven corrections without ship authorization | No proven correction exists to retain. Branch and PR creation are forbidden by the user in all variants. |\n| Doctor drift or failed drive | Not reached. No repair or retry receipt fabricated. |\n\nNo listener, process, browser session or failed-drive residue was created for this case. No cleanup claim substitutes for missing live proof.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-11/stale-feature-map/dashboard.mjs",
      "owner": "grades-native-11.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-11/stale-feature-map/source-reads.json",
      "owner": "grades-native-11.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/stale-feature-map/dashboard.mjs",
      "owner": "grades-native-11.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-11/stale-feature-map/source-reads.json",
      "owner": "grades-native-11.json#2",
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
