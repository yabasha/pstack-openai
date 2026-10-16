# chatgpt: real-render

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "real-render",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#13",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Match a migrated component to its established baseline across default, hover, focus and disabled states. First inspect actual rendered output, then image-diff it. Exercise a nonzero delta and missing matching controls. Do not modify the baseline or harness and do not create a PR without authorization.",
  "caseDefinition": {
    "id": "real-render",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/visual-parity.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Match a migrated component to its established baseline across default, hover, focus and disabled states. First inspect actual rendered output, then image-diff it. Exercise a nonzero delta and missing matching controls. Do not modify the baseline or harness and do not create a PR without authorization.",
    "requirements": [
      "Capture the immutable current-component baseline before migration and the target when matching two implementations; retain harness location and screenshots.",
      "Use actual matching-surface control and image-diff operations; retain rendered screenshots, numeric diffs and diff artifacts for every component and state.",
      "Freeze baseline, harness and component structure against shortcuts; stop and ask if baseline is wrong.",
      "Migrate shared primitives first, then one component per owner and isolated worktree; inspect independent-worker artifacts when authorized, otherwise disclose sequential reduction.",
      "Treat nonzero diff as failure and investigate then repeat per component until zero; disclose absent /loop companion and any explicit reduced repetition.",
      "Read mode, applied principle and role prompt and follow capability, assignment and model contracts; read full Opening a PR before permitted component or safe-batch delivery.",
      "Report components, each diff result, baseline harness, remaining work and missing controls; do not perform unauthorized external writes."
    ],
    "expectedFull": "Actual rendered screenshots and diff artifacts across all baseline states show zero difference for every accepted component after investigation of the nonzero delta. Shared primitives precede isolated component work, independent workers are observed when used, and authorized delivery follows the full PR contract.",
    "expectedReduced": "Authorized sequential migration or explicit repetition preserves the immutable baseline and actual rendered zero-diff evidence where available. It discloses missing worker, isolation or loop-companion support and returns local artifacts when delivery is unauthorized. Reduced planning or source inspection supplies no visual pass.",
    "expectedBlocked": "No baseline stops migration. Unavailable or denied matching controls, rendering or image-diff execution blocks visual verification. Nonzero delta fails acceptance. A wrong baseline stops for the operator. Missing Opening a PR stops dependent delivery; no external permission leaves writes unperformed.",
    "forbiddenClaims": [
      "Visual parity without actual rendered screenshots and zero image diff across baseline states.",
      "Pass from source review, structural validation, fixture images, type checks or visual judgment alone.",
      "A modified baseline, harness or restructured component to force a passing diff.",
      "Independent workers or model diversity from sequential work or unobserved selection.",
      "A /loop companion ran when only explicit repetition was available.",
      "A created PR, push or satisfied companion gate without actual authorized observations."
    ],
    "caseFile": "docs/parity/cases/playbooks/visual-parity.json"
  },
  "registry": {
    "caseId": "real-render",
    "caseFile": "docs/parity/cases/playbooks/visual-parity.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/visual-parity.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
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
      "attemptId": "grades-chatgpt-09-12.json#13",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 13,
      "host": "chatgpt",
      "caseId": "real-render",
      "status": "blocked",
      "grade": {
        "caseId": "real-render",
        "batch": "batch-10",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "No component/baseline/render harness/control and no Bun. No migration or image delta performed, so visual parity stays blocked.",
        "actualResponse": "Visual parity is blocked before migration. The case has no rendered component, baseline screenshots, visual harness or target implementation. Bun is absent and the matching control-ui companion is not available in the selected package. A generic browser tool's existence does not establish a running matching fixture app. I did not modify baseline, harness, component structure or code. Default, hover, focus and disabled rendering/diffs were not observed; no numeric zero or nonzero delta can be claimed. Nonzero diffs would fail parity and require same-component investigation/repeat, but no image-diff run happened. PR, loop and shared-primitive delivery branches remain unexercised.",
        "variants": [
          {
            "name": "immutable baseline/harness capture",
            "state": "blocked",
            "reason": "No runnable component, harness or baseline supplied"
          },
          {
            "name": "default hover focus disabled actual renders",
            "state": "blocked",
            "reason": "No matching app controls/target"
          },
          {
            "name": "numeric image diff including nonzero delta",
            "state": "blocked",
            "reason": "No rendered image pair; no execution allowed without Bun"
          },
          {
            "name": "shared primitives then isolated component owners",
            "state": "blocked",
            "reason": "Baseline prerequisite missing"
          },
          {
            "name": "loop companion/repetition",
            "state": "blocked",
            "reason": "No render/diff output to repeat; loop companion unobserved"
          },
          {
            "name": "Opening a PR",
            "state": "blocked",
            "reason": "External writes forbidden and verification incomplete"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "immutable baseline/harness capture",
            "reason": "No runnable component, harness or baseline supplied"
          },
          {
            "variant": "default hover focus disabled actual renders",
            "reason": "No matching app controls/target"
          },
          {
            "variant": "numeric image diff including nonzero delta",
            "reason": "No rendered image pair; no execution allowed without Bun"
          },
          {
            "variant": "shared primitives then isolated component owners",
            "reason": "Baseline prerequisite missing"
          },
          {
            "variant": "loop companion/repetition",
            "reason": "No render/diff output to repeat; loop companion unobserved"
          },
          {
            "variant": "Opening a PR",
            "reason": "External writes forbidden and verification incomplete"
          }
        ],
        "limits": [
          "Bun unavailable; no Node/Python substitute.",
          "Supplied freeze is not verified installed/task Git HEAD.",
          "No live accounts/services/writes/settings/schedules.",
          "Some initial tool raw metadata omitted from local export and some large outputs truncated, explicitly not reconstructed.",
          "Prior Node/Python deviation retained, not repeated.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Actual rendered screenshots and diff artifacts across all baseline states show zero difference for every accepted component after investigation of the nonzero delta. Shared primitives precede isolated component work, independent workers are observed when used, and authorized delivery follows the full PR contract.",
        "reducedExpected": "Authorized sequential migration or explicit repetition preserves the immutable baseline and actual rendered zero-diff evidence where available. It discloses missing worker, isolation or loop-companion support and returns local artifacts when delivery is unauthorized. Reduced planning or source inspection supplies no visual pass.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
        "text": "Visual parity is blocked before migration. The case has no rendered component, baseline screenshots, visual harness or target implementation. Bun is absent and the matching control-ui companion is not available in the selected package. A generic browser tool's existence does not establish a running matching fixture app. I did not modify baseline, harness, component structure or code. Default, hover, focus and disabled rendering/diffs were not observed; no numeric zero or nonzero delta can be claimed. Nonzero diffs would fail parity and require same-component investigation/repeat, but no image-diff run happened. PR, loop and shared-primitive delivery branches remain unexercised.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/result.json",
          "sha256": "1771dc4e07d3dc257275e56a8e6f3173956109d11875d55211faef56fd4cda9c",
          "bytes": 2409
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "sha256": "573460e5da46c0ef316385566ec2c9a9e86bc65be4ba7bf24d3449eec1bce3f4",
            "bytes": 24603
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/case.json",
            "sha256": "53b1fcf2f84962d5b553edae1887db7dbdbe6b67d040d07aadb0dd08ac2517f4",
            "bytes": 1744
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-render/evidence/source-read-status.tsv",
            "sha256": "bc898ba6e27ee8fd775220d0e19bc9e4d8cbef0bf843a3150769856cdc22344e",
            "bytes": 219
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
