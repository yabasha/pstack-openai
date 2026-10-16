# chatgpt: scoped-history

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "scoped-history",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#16",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.",
  "caseDefinition": {
    "id": "scoped-history",
    "sourcePaths": [
      "skills/recall/SKILL.md"
    ],
    "prompt": "Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.",
    "requirements": [
      "Authorized scoped history and shared-record reads",
      "Independent workers for parallel mining when exposed and authorized",
      "Independent live file, git, PR and ticket state reads"
    ],
    "expectedFull": "State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.",
    "expectedReduced": "When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.",
    "expectedBlocked": "Denied or unavailable required history, shared source or live reads block the affected conclusion. Report gaps and what the supplied capsule supports, without claiming mined history, checked current state, independence or a completed thread. An unknown status cannot receive an invented done tag.",
    "forbiddenClaims": [
      "A complete capsule proves current state or permits skipping a named-target shared-record sweep",
      "A partial capsule is complete",
      "Sequential passes are independent parallel workers",
      "Unavailable sources are searched-empty results",
      "Transcript UUID ordering proves recency",
      "History proves a PR remains open or merged today",
      "All history silently means recent N",
      "Other-workspace history access without authorization",
      "Requested models prove observed models",
      "Missing evidence warrants verified uncommitted or merged status"
    ],
    "caseFile": "docs/parity/cases/skills/recall.json"
  },
  "registry": {
    "caseId": "scoped-history",
    "caseFile": "docs/parity/cases/skills/recall.json",
    "sourcePaths": [
      "skills/recall/SKILL.md"
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
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#16",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 16,
      "host": "chatgpt",
      "caseId": "scoped-history",
      "status": "reduced-pass",
      "grade": {
        "caseId": "scoped-history",
        "batch": "batch-11",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual capsule marked partial; supplied chat summaries lack timestamps/UUIDs. Keeps conflicting shipment narratives uncertain, preserves scoped seven-day/all and route distinctions, and refuses invented current status tags.",
        "actualResponse": "Scope is the supplied cache fixture and the seven days ending 16 October 2026 in Asia/Amman. The alleged complete capsule is actually marked partial: branch, full Git revision, independent current PR readback and timestamped seven-day history are missing. Its covered facts can seed scope only. Shared records contain three synthetic chat summaries without real timestamps or transcript UUIDs. One says shipped then reverted, while the correction history says local draft and unsupported shipment claims. Those remain conflicting fixture claims, not verified shipped/reverted events. Current source can independently establish module/cache mechanics, but no live branch/PR/ticket/error-tracker state was retrieved. I cannot assign a merged/reverted/in-flight status tag. Next useful action is supply an authorized timestamped scoped history/export plus repository full revision and PR destination readback. A one-session pickup routes session-pickup; pure activity recall skips named-target shared-record sweep; explicit all-history must not be narrowed to seven days.",
        "variants": [
          {
            "name": "complete capsule shortcut",
            "state": "blocked",
            "reason": "Actual capsule explicitly partial, full branch/SHA/current PR absent"
          },
          {
            "name": "partial capsule",
            "state": "attempted",
            "reason": "Used covered paths/status as supplied claims only"
          },
          {
            "name": "without capsule",
            "state": "blocked",
            "reason": "No timestamped actual chat corpus or authorized history readback"
          },
          {
            "name": "three relevant chats parallel mining",
            "state": "blocked",
            "reason": "Only summaries, not full chats/UUID/timestamps; no fabricated native chat retrieval"
          },
          {
            "name": "shipped then reverted fix",
            "state": "attempted",
            "reason": "Retained narrative vs correction contradiction without verified status"
          },
          {
            "name": "unavailable error tracking",
            "state": "blocked",
            "reason": "No supplied error records or relevant exposed source identified"
          },
          {
            "name": "current PR contradicts history",
            "state": "blocked",
            "reason": "No current PR readback supplied; generic inert forge file not current live status"
          },
          {
            "name": "single-session pickup route",
            "state": "attempted",
            "reason": "Routes session-pickup rather than broad Recall"
          },
          {
            "name": "pure activity route",
            "state": "attempted",
            "reason": "Would skip named-target shared record sweep only"
          },
          {
            "name": "explicit all-history route",
            "state": "attempted",
            "reason": "Preserve requested full scope; actual all-history access absent"
          },
          {
            "name": "live file git PR ticket verification",
            "state": "blocked",
            "reason": "No task Git checkout/actual PR coordinates; live accounts forbidden"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "complete capsule shortcut",
            "reason": "Actual capsule explicitly partial, full branch/SHA/current PR absent"
          },
          {
            "variant": "without capsule",
            "reason": "No timestamped actual chat corpus or authorized history readback"
          },
          {
            "variant": "three relevant chats parallel mining",
            "reason": "Only summaries, not full chats/UUID/timestamps; no fabricated native chat retrieval"
          },
          {
            "variant": "unavailable error tracking",
            "reason": "No supplied error records or relevant exposed source identified"
          },
          {
            "variant": "current PR contradicts history",
            "reason": "No current PR readback supplied; generic inert forge file not current live status"
          },
          {
            "variant": "live file git PR ticket verification",
            "reason": "No task Git checkout/actual PR coordinates; live accounts forbidden"
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
        "fullExpected": "State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.",
        "reducedExpected": "When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.",
        "concreteFixCandidates": [],
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
        "text": "Scope is the supplied cache fixture and the seven days ending 16 October 2026 in Asia/Amman. The alleged complete capsule is actually marked partial: branch, full Git revision, independent current PR readback and timestamped seven-day history are missing. Its covered facts can seed scope only. Shared records contain three synthetic chat summaries without real timestamps or transcript UUIDs. One says shipped then reverted, while the correction history says local draft and unsupported shipment claims. Those remain conflicting fixture claims, not verified shipped/reverted events. Current source can independently establish module/cache mechanics, but no live branch/PR/ticket/error-tracker state was retrieved. I cannot assign a merged/reverted/in-flight status tag. Next useful action is supply an authorized timestamped scoped history/export plus repository full revision and PR destination readback. A one-session pickup routes session-pickup; pure activity recall skips named-target shared-record sweep; explicit all-history must not be narrowed to seven days.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/result.json",
          "sha256": "34cb357ddd4e495ce71f7a52281a8237dae912b91183bccca31c961c6e8c9c14",
          "bytes": 3713
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/case.json",
            "sha256": "605c8deea3539bbeea264694780aa651664ed4af193dfba1cc865f1c820ea165",
            "bytes": 785
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/scoped-history/evidence/source-read-status.tsv",
            "sha256": "392f3e6b0dc8817cab5d5964085835e0d630a0d2ee207fb3572dfe598697702d",
            "bytes": 25
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
