# chatgpt: stale-feature-map

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "stale-feature-map",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#18",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
      "attemptId": "grades-chatgpt-09-12.json#18",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 18,
      "host": "chatgpt",
      "caseId": "stale-feature-map",
      "status": "blocked",
      "grade": {
        "caseId": "stale-feature-map",
        "batch": "batch-11",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "No verification map/features/app target, so all-source/live correction/re-drive impossible. Preserves unresolved async entitlement contract rather than silently deleting requirement.",
        "actualResponse": "Blocked at target discovery. No actual verify skill, feature-map index or feature files are supplied in this case. The Notes examples elsewhere in the installed package are illustrative and cannot substitute for this app. The changed contract says saving now needs entitlement and completes asynchronously. That requires both entitlement branches, pending/completed/error observation and persisted second-view proof; a screenshot cannot replace them. I did not silently delete the old immediate-save requirement or edit product code. Source wave, every-feature live pass, harness correction re-drive and shipped corrections remain unexercised because the target and runnable app contract are missing. No branch or PR created.",
        "variants": [
          {
            "name": "locate actual verification target/index/features",
            "state": "blocked",
            "reason": "No target supplied or discoverable within case fixture"
          },
          {
            "name": "one independent source reader per feature",
            "state": "blocked",
            "reason": "No actual feature files to assign"
          },
          {
            "name": "entitlement required/denied and async save completion",
            "state": "blocked",
            "reason": "No changed runnable source/user controls"
          },
          {
            "name": "index hygiene and churn sweep",
            "state": "blocked",
            "reason": "No target map/repository change history"
          },
          {
            "name": "live every-feature doctor/reset/proof survives cleanup",
            "state": "blocked",
            "reason": "Bun absent and no runnable app/driver"
          },
          {
            "name": "doc drift vs product regression triage",
            "state": "attempted",
            "reason": "Preserve old requirement and classify as unresolved contract change"
          },
          {
            "name": "harness correction re-drive",
            "state": "blocked",
            "reason": "No harness target or live proof"
          },
          {
            "name": "shipping corrections",
            "state": "blocked",
            "reason": "Explicitly unauthorized branch/PR delivery"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "locate actual verification target/index/features",
            "reason": "No target supplied or discoverable within case fixture"
          },
          {
            "variant": "one independent source reader per feature",
            "reason": "No actual feature files to assign"
          },
          {
            "variant": "entitlement required/denied and async save completion",
            "reason": "No changed runnable source/user controls"
          },
          {
            "variant": "index hygiene and churn sweep",
            "reason": "No target map/repository change history"
          },
          {
            "variant": "live every-feature doctor/reset/proof survives cleanup",
            "reason": "Bun absent and no runnable app/driver"
          },
          {
            "variant": "harness correction re-drive",
            "reason": "No harness target or live proof"
          },
          {
            "variant": "shipping corrections",
            "reason": "Explicitly unauthorized branch/PR delivery"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python runtime substitute.",
          "No live accounts/services/external writes/schedules/global settings.",
          "Task Git revision absent; supplied sourceFreeze is not verified host Git HEAD.",
          "Early raw metadata export incomplete; truncated outputs retained as returned, not reconstructed.",
          "Prior Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Locate the existing target and reconcile its index. Assign one read-only reader per feature, inspect every returned source summary and citation, merge recipes and check churn for missing source-backed features. The coordinator drives every feature according to the target launch model. Doctor before first and fresh-session drives and after failures; reset wedged UI state. Preserve and check evidence after cleanup, clean failed-drive residue and perform final teardown after re-proofs. Classify confirmed contract change as doc drift, broken product behavior as a product gap, and working behavior unreachable by the harness as a harness gap. Record the entitlement and attempted route for verified-unreachable, repair missing prerequisites and re-drive harness fixes. Re-read changed files and produce at most one authorized PR of proven corrections, or report clean or blocked honestly.",
        "reducedExpected": "Without independent workers, one coordinator may read every feature serially as reduced capability, retaining all source and live coverage standards. Without shipping authorization, retain proven corrections for local review and report blocked shipping; do not create a branch or PR. Without execution or app-driving, provide source findings and pending live recipes, mark live verification not-run and outcome blocked. Read-only permissions permit recommendations only, with denied writes explicit.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-09-12.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ]
      },
      "topLevelContext": {
        "scope": "Actual ChatGPT Work remaining batches09..12,30cases",
        "gradingNotes": [
          "Independent outcome review of retained actual responses/variants/source artifacts, not exported selfgrades.",
          "Native UI aggregate reads/commands/worker activity supplied by parent; exact model-captured logs treated with explicit provenance gaps.",
          "No proxy programs/fixture verdicts count as actual service or worker results.",
          "Missing taskGit and unavailable Bun remain required-method blockers; tools themselves not declared absent.",
          "All named requested variants must be addressed before full. No full awarded in this set.",
          "Old original source path failures retained; documented fallback source reads not automatically rejected.",
          "history-evidence is included because actual cloud batch09 contains it; do not count duplicate historical case twice when aggregating target coverage."
        ]
      },
      "response": {
        "text": "Blocked at target discovery. No actual verify skill, feature-map index or feature files are supplied in this case. The Notes examples elsewhere in the installed package are illustrative and cannot substitute for this app. The changed contract says saving now needs entitlement and completes asynchronously. That requires both entitlement branches, pending/completed/error observation and persisted second-view proof; a screenshot cannot replace them. I did not silently delete the old immediate-save requirement or edit product code. Source wave, every-feature live pass, harness correction re-drive and shipped corrections remain unexercised because the target and runnable app contract are missing. No branch or PR created.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/result.json",
          "sha256": "85187020380598105058d574c22ac48e48f0a3e3c8237f7eda8ba88debadec01",
          "bytes": 2808
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
        "retainedEvidence": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "sha256": "a0f4eb6e5baaded49263375472ed1d7b945b1aa4459538f99c6abf2f46b3ebf5",
            "bytes": 28398
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/case.json",
            "sha256": "9492f0ff4cc9c57ef1adcd9160205619f2043249f48327a453d30b2a24423c85",
            "bytes": 753
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/stale-feature-map/evidence/source-read-status.tsv",
            "sha256": "9f18b3e818cd738e1a8c9a6654b2bda8c1e60e73557fc2d63f9e8a69fdd97c8b",
            "bytes": 46
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-09-12.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [],
  "skippedManifest": [],
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
