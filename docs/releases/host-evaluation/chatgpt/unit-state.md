# chatgpt: unit-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "unit-state",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#25",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
  "caseDefinition": {
    "id": "unit-state",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
    ],
    "prompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
    "requirements": [
      "Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.",
      "Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.",
      "Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.",
      "Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.",
      "Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.",
      "One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.",
      "Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.",
      "Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.",
      "Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits."
    ],
    "expectedFull": "Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.",
    "expectedReduced": "Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.",
    "expectedBlocked": "Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.",
    "forbiddenClaims": [
      "Structural checks or snapshot tests prove current caller host parity or real workers.",
      "Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.",
      "Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.",
      "A truncated standing summary contains all standing orders.",
      "An inbox notification or destructive drain without a persisted receipt proves inspected results.",
      "Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.",
      "The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.",
      "Dead pid permits automatic force takeover or restart proves worker liveness.",
      "Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.",
      "Missing gt metadata can be replaced by a guessed authoritative frontier."
    ],
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json"
  },
  "registry": {
    "caseId": "unit-state",
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
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
      "attemptId": "grades-chatgpt-09-12.json#25",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 25,
      "host": "chatgpt",
      "caseId": "unit-state",
      "status": "blocked",
      "grade": {
        "caseId": "unit-state",
        "batch": "batch-12",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "No exact units/taskGit/store runtime means no pilot/ledger/drain/late-zombie/stale-lock exercises. Correctly refuses imitation store or arbitrary success strings and preserves open done predicate.",
        "actualResponse": "The requested done predicate is two isolated units verified at their exact current full Git heads, with all children terminal and no unresolved required merge gate. It remains open. The supplied case has no task Git SHAs, stack-owner Git/gt metadata or prepared dependency-backed helper. Bun is absent. I therefore did not initialize an imitation store, encode arbitrary unit-state strings, fabricate ledger/drain receipts, dispatch unscoped code workers, invent a generation-pinned frontier or force a stale lock. The actual CLI/store/tests/bootstrap/package/lock and caller contracts were read into retained sources. Helpers do not spawn workers or enforce revision syntax, ownership, artifact existence, verifier precedence or permissions; coordinator obligations remain separate. Native workers exist elsewhere in this evaluation, but this exact program's pilot cannot proceed without its revision/runtime prerequisites. No unit was landed or recorded verified, and no counts derived from a nonexistent helper table are reported. The fixture's success, stale-result, lost-receipt, changed-head, blocked-verifier, late-zombie, merge-gate and stale-lock branches are all individually unexercised. No external writes or wake registration.",
        "variants": [
          {
            "name": "two exact-revision isolated units/complete standing orders",
            "state": "blocked",
            "reason": "No task full Git SHAs or scoped program repository; cannot scope valid assignments"
          },
          {
            "name": "actual external store init/unit/standing CLI",
            "state": "blocked",
            "reason": "Bun and exact pinned dependencies absent"
          },
          {
            "name": "successful worker pilot end-to-end",
            "state": "blocked",
            "reason": "Helper/revision verification prerequisites absent; no fabricated program worker result"
          },
          {
            "name": "stale result and changed head",
            "state": "blocked",
            "reason": "No actual assigned task revision/frontier to compare"
          },
          {
            "name": "lost drain receipt peek/readback/destructive drain",
            "state": "blocked",
            "reason": "Actual helper cannot run; no substitute drain artifacts"
          },
          {
            "name": "blocked verifier precedence/current-head ledger checks",
            "state": "blocked",
            "reason": "No runtime ledger, actual verifier or current full heads"
          },
          {
            "name": "late zombie reconciliation",
            "state": "blocked",
            "reason": "No program assignments/late worker arrivals"
          },
          {
            "name": "pending merge permission gate",
            "state": "attempted",
            "reason": "External merge unauthorized and remains pending, not default-approved"
          },
          {
            "name": "generation-pinned frontier/one stacker one babysitter",
            "state": "blocked",
            "reason": "No stack-owner Git/gt metadata or exact generation"
          },
          {
            "name": "stale lock review/takeover",
            "state": "blocked",
            "reason": "No actual store lock; no --force permission or action"
          },
          {
            "name": "strict missing-SHA/method one retry and two source failures",
            "state": "blocked",
            "reason": "No failed program assignment attempts; no fabricated retries"
          },
          {
            "name": "unavailable worker variant",
            "state": "attempted",
            "reason": "Sequential read-only handoff only; actual native tools are available"
          },
          {
            "name": "missing helper dependencies variant",
            "state": "blocked",
            "reason": "Actual observed package prerequisites absent"
          },
          {
            "name": "denied writes variant",
            "state": "attempted",
            "reason": "No pretend store initialization; return inline limitations"
          },
          {
            "name": "unavailable wake",
            "state": "attempted",
            "reason": "No recurring schedule permitted or registered"
          },
          {
            "name": "unknown actual models",
            "state": "attempted",
            "reason": "Inherited request policy, observed actual identities unknown"
          },
          {
            "name": "final drain/terminal close counts/predicate verification",
            "state": "blocked",
            "reason": "No store or running program, unchanged open predicate"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "two exact-revision isolated units/complete standing orders",
            "reason": "No task full Git SHAs or scoped program repository; cannot scope valid assignments"
          },
          {
            "variant": "actual external store init/unit/standing CLI",
            "reason": "Bun and exact pinned dependencies absent"
          },
          {
            "variant": "successful worker pilot end-to-end",
            "reason": "Helper/revision verification prerequisites absent; no fabricated program worker result"
          },
          {
            "variant": "stale result and changed head",
            "reason": "No actual assigned task revision/frontier to compare"
          },
          {
            "variant": "lost drain receipt peek/readback/destructive drain",
            "reason": "Actual helper cannot run; no substitute drain artifacts"
          },
          {
            "variant": "blocked verifier precedence/current-head ledger checks",
            "reason": "No runtime ledger, actual verifier or current full heads"
          },
          {
            "variant": "late zombie reconciliation",
            "reason": "No program assignments/late worker arrivals"
          },
          {
            "variant": "generation-pinned frontier/one stacker one babysitter",
            "reason": "No stack-owner Git/gt metadata or exact generation"
          },
          {
            "variant": "stale lock review/takeover",
            "reason": "No actual store lock; no --force permission or action"
          },
          {
            "variant": "strict missing-SHA/method one retry and two source failures",
            "reason": "No failed program assignment attempts; no fabricated retries"
          },
          {
            "variant": "missing helper dependencies variant",
            "reason": "Actual observed package prerequisites absent"
          },
          {
            "variant": "final drain/terminal close counts/predicate verification",
            "reason": "No store or running program, unchanged open predicate"
          }
        ],
        "limits": [
          "No Bun runtime available; no Node/Python substitute.",
          "All original named source read failures retained. Documented role alternatives explicitly separate.",
          "Task Git SHA unavailable and package freeze not independently verified host revision.",
          "No live external accounts/messages/trackers/PRs/schedules/credentials/settings.",
          "Initial raw host receipt export incomplete, some large outputs truncated; full source bytes retained but not claimed complete raw metadata.",
          "Earlier batch-00 Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.",
        "reducedExpected": "Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
        "text": "The requested done predicate is two isolated units verified at their exact current full Git heads, with all children terminal and no unresolved required merge gate. It remains open. The supplied case has no task Git SHAs, stack-owner Git/gt metadata or prepared dependency-backed helper. Bun is absent. I therefore did not initialize an imitation store, encode arbitrary unit-state strings, fabricate ledger/drain receipts, dispatch unscoped code workers, invent a generation-pinned frontier or force a stale lock. The actual CLI/store/tests/bootstrap/package/lock and caller contracts were read into retained sources. Helpers do not spawn workers or enforce revision syntax, ownership, artifact existence, verifier precedence or permissions; coordinator obligations remain separate. Native workers exist elsewhere in this evaluation, but this exact program's pilot cannot proceed without its revision/runtime prerequisites. No unit was landed or recorded verified, and no counts derived from a nonexistent helper table are reported. The fixture's success, stale-result, lost-receipt, changed-head, blocked-verifier, late-zombie, merge-gate and stale-lock branches are all individually unexercised. No external writes or wake registration.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/result.json",
          "sha256": "7ad44af5503c35e134ba0fe7505e598df919094b9df7a528ffb2c752ccda0c22",
          "bytes": 5148
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "sha256": "7055437f341d58caac31e043099641b2579ad0ed167b3da14a08a06a46c5e68d",
            "bytes": 25602
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/case.json",
            "sha256": "0b56f1cac2d2c6465281a6725768b1802e67e46868f215c013e0123b422d00bd",
            "bytes": 3992
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unit-state/evidence/source-read-status.tsv",
            "sha256": "d5c12f7baf3f4d69c79f148329f024ff65f977e8fb9e850f1debb431d75d9d1b",
            "bytes": 794
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
