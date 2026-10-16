# codex: scoped-history

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "scoped-history",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-rerun-06.json#0",
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
      "attemptId": "grades-native-11.json#0",
      "order": 0,
      "gradeFile": "grades-native-11.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "scoped-history",
      "status": "fail",
      "grade": {
        "caseId": "scoped-history",
        "host": "codex",
        "status": "fail",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [
          "Exact topic/workspace/time declared before first history search (violated)",
          "Complete scoped chat transcripts, identifiers and real timestamps",
          "Exact target/current PR/action receipts for status claims"
        ],
        "review": "The response explicitly acknowledges initial fixture-history reads before formal scope/time-range capture. That violates the case requirement to establish topic/workspace/time before search; later independent source investigation and synthesis cannot retroactively repair ordering. Missing real transcripts and live status are separately retained, with no invented done tags.",
        "responseArtifact": "fixtures/batch-11/scoped-history.result.md",
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
          "item_31",
          "item_35",
          "item_42",
          "item_47"
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
        "fullExpected": "State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.",
        "reducedExpected": "When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.",
        "concreteFixCandidates": [
          "Rerun with topic/workspace/exact time scope declared before any history input read; source already requires this ordering."
        ]
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# scoped-history\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Scope and actual input\n\nCache invalidation teardown in this active disposable workspace only. Seven-day scope is 2026-10-09 11:16:00 through 2026-10-16 11:16:00 Asia/Amman, corresponding to 2026-10-09 08:16:00 through 2026-10-16 08:16:00 UTC. The end was observed through clock__curr_time. Initial fixture reads preceded formal scope capture, a sequencing limit. No unrelated history was read.\n\nCopied input/history, input/cache and input/forge.json from shared before any local changes. The actual capsule labels itself partial, has null fullGitRevision, no branch and no current PR observation. It is not the complete capsule described in the prompt. The three chat slices are synthetic digests with relativeOrder, not actual chats, UUIDs or modification timestamps. No full transcript was supplied.\n\n## Actual brief\n\n- The current cache fixture uses immediate deletion in cache.mjs:4. The caller schedules onDispose through disposer-v1.mjs:3, then immediately invalidates in caller.mjs:6. This is an observed source relationship, not a runtime result.\n- The supplied capsule describes a proposal only. The repository is on main at the input SHA with no remote. The tracked committed inputs have no diff. This does not establish deployed state.\n- The scoped Git log contains one fixture-seed commit at 2026-10-16T11:01:53+03:00. It contains no recorded shipped-and-reverted sequence.\n- fixture-chat-B says a fix shipped then reverted, but supplies no PR, commits or verified action. Error tracking and live PR state are unavailable.\n- No current PR contradiction can be verified. forge.json has two synthetic records, neither tied to the cache by a real repository or revision.\n\nThread status is blocked. None of the permitted tags is supported for a real cache thread. In particular, no invented [merged #N], [reverted #N] or [verified, uncommitted] tag is assigned.\n\nRecurring problems are the repeated unsupported shipped claims in fixture-event-04 and fixture-event-06, a reported but unverified shipped-then-reverted fix in fixture-chat-B, and the immediate-invalidation versus deferred-disposal ordering visible in source. The latter may lead to an undefined read in the queued callback, an inference from code rather than an executed reproduction.\n\nNext move is to obtain the scoped full transcripts with real timestamps and an exact cache PR or branch revision plus current destination readback.\n\n## Shared-record sweep\n\n| Category | Actual operation and result |\n| --- | --- |\n| Source control | Read local scoped log, blame and full file patch. One seed commit. No PR references. No remote configured. |\n| Ticket tracker | Supplied shared-records.json read. Synthetic retry ticket narrative is not cache ticket readback. Live source unavailable within this isolation. |\n| Long-form docs | Copied cache README and capsule read. No scoped real design record supplied. |\n| Team chat | Three supplied summary slices read. Full messages and timestamps unavailable. |\n| Infrastructure observability | No scoped supplied data or authorized live service. Unavailable, not searched-empty. |\n| Error tracking | Explicitly unavailable in supplied history. No search claimed. |\n| Product analytics | No scoped supplied data or authorized live service. Unavailable, not searched-empty. |\n\nThe why skill, epistemics, investigator and synthesizer templates and code-archaeology source playbook were read. A first attempted source-control.md path was absent; the actual code-archaeology.md was then read. The coordinator first made a bounded local source sweep. Then an actual independent why source-control investigator /root/cache_source repeated scoped file and Git checks, and a fresh /root/cache_synthesizer spot-checked citations and synthesized the inspected findings. Their read-only terminal results were inspected and captured in scoped-history/source-findings.md and scoped-history/synthesis.md. Immutable assignments were written and read before each dispatch. No independent mining of nonexistent full chats was dispatched. Source investigation and synthesis independence were observed; parallel chat mining and live PR or ticket verification were not. Model selection was inherited and actual models remain unknown.\n\n## Requested variants\n\n| Variant | Actual response and limits |\n| --- | --- |\n| Complete capsule | Required complete supplied input is absent. The shortcut cannot be exercised as an actual supplied-capsule run. With such input, mining is skipped while shared-record and live checks remain required. This is routing guidance, not a receipt. |\n| No capsule | Examined the limited synthetic history and chatSlices without using capsule completeness as a shortcut. Seven-day real history remains unavailable. |\n| Three chats | Read fixture-chat-A, B and C summaries. A concerns deferred invalidation, B reports shipped then reverted without proof, C reports microtask disposal. Goals, decisions, struggles, timestamps and artifacts are incomplete. Full per-chat schema is not recoverable and UUID citations are unavailable. Relative order is not recency. |\n| Partial capsule | Actual supplied variant. Covered paths were inspected. Missing history was retained as missing. |\n| Shipped then reverted | Narrative retained as unverified; local seed history does not prove either action. |\n| Unavailable error tracking | Actual supplied limitation respected. No searched-empty claim. |\n| Current PR contradicts history | No concrete current PR observation supplied or authorized live access. Contradiction branch is blocked, not invented. |\n| Single-session pickup | Routes to installed session-pickup.md, which was read. No scoped full prior session or pushed branch exists, so execution pickup is blocked. |\n| Pure activity recall | Shared-record sweep is skipped for that variant. The limited synthetic digest supports proposals and corrections only, not a seven-day activity report. |\n| Explicit all-history | All supplied scoped history is retained without a seven-day filter. Actual all-history is unavailable. No broad personal search performed. |\n| Habits or work summary | Habits route to automate-me. Human-readable work summary is a separate task. Neither was expanded into unauthorized durable personal edits. |\n\nNegative availability conditions were supplied scenario conditions, not host-enforced denials. Missing records are real. No source was fabricated to fill them.\n",
        "artifact": {
          "path": "fixtures/batch-11/scoped-history.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history.result.md",
          "sha256": "fec1bfb04704155565184e2310fc48242364c433e9a67bbe2d62af095ffc645e",
          "bytes": 7413
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
    },
    {
      "attemptId": "grades-native-rerun-06.json#0",
      "order": 106,
      "gradeFile": "grades-native-rerun-06.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "scoped-history",
      "status": "blocked",
      "grade": {
        "caseId": "scoped-history",
        "host": "codex",
        "status": "blocked",
        "execution": "workers",
        "rawTrace": "codex/rerun-06.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_7",
          "item_8",
          "item_9",
          "item_11",
          "item_12",
          "item_13"
        ],
        "actualExecutionEventIds": [
          "item_15",
          "item_16",
          "item_18",
          "item_19",
          "item_20",
          "item_22",
          "item_24",
          "item_26",
          "item_29",
          "item_30"
        ],
        "requiredObservationsMet": [
          "supplied-input",
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [
          "Requested exact installed0.1.0/f462 source path missing; available inspected package is0.1.1 reference only",
          "Actual cache implementation/current PR/ticket evidence and real timestamped chat transcripts/UUIDs",
          "Complete capsule, historical base/revert evidence and full required concurrent source/history roster"
        ],
        "review": "Raw item3 declares topic, workspace and exact seven-day window before every read, correcting baseline scope-order failure. Three fresh synthetic-chat investigators and scoped source investigators produce inspected limited findings. Missing0.1.0 is real after cache replacement;0.1.1 is explicitly reference-only, not silently accepted as originalfreeze. Supplied partial capsule, undated fictional chatids and unknown action cannot establish real history, implementation, shipping/revert or current PR state. Unknown threads remain untagged rather than inventing permitted done statuses. Actual Git assignment identity/readback and access-boundary preservation are useful observations; full frozen-workflow result remains blocked.",
        "responseArtifact": "fixtures/rerun-06/scoped-history.result.md",
        "evidence": [
          "fixtures/rerun-06/scoped-history.evidence/tool-returns.json",
          "fixtures/rerun-06/scoped-history.evidence/assignments.json",
          "fixtures/rerun-06/scoped-history.evidence/source-assignments.json",
          "fixtures/rerun-06/scoped-history.evidence/verification-return.json"
        ],
        "variantReview": [
          "All declared variants have separate evidence-limited responses; absent complete capsule, realPR contradiction, dated history and full transcript variants are blocked, not simulated successes.",
          "Pure activity variant omits target-specific shared sweep; explicit all-history keeps authorized supplied set without date filter.",
          "Initial scope precedes tool use. Earlier failed scope ordering remains preserved by original grade/rawtrace."
        ],
        "limits": [
          "Exact source-path absence after app cache replacement is real; no old-cache read is fabricated.",
          "Model/effort/family remain unknown from spawn receipts.",
          "Local result/tool-return captures are artifacts, not blanket independently verified extra native telemetry.",
          "No other-workspace cache path, actual accounts, unrelated private history or replay was accessed."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "priorAttempt": {
          "artifact": "grades-native-11.json",
          "status": "fail",
          "retained": true
        }
      },
      "topLevelContext": {
        "attempt": "rerun-06",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Actual native completed turn/source failure reviewed; no latest-best cherrypicking. Correct ordering does not repair unavailable requested source or target evidence."
        ]
      },
      "response": {
        "text": "# Scoped history observations\n\n- Topic: cache subsystem. Workspace: `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06`. Recent window: `2026-10-09T00:00:00+03:00` through `2026-10-16T00:00:00+03:00`, exactly seven days. The first assistant response declared these before any tool or read.\n- The requested installed `pstack-openai 0.1.0` path is missing. The inspected installed package identifies itself as `0.1.1`. Execution against freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` cannot be established. Its absence from this fixture's Git objects does not establish its absence elsewhere. The available version supplied reference instructions only.\n- Independently inspected fixture HEAD is `42fb97aed6a402f21cc42b220f1cdb8133cc326d`, branch `main`. The tracked tree has five input files, no cache implementation and no remote. These observations verify the fixture, not the cache change. See [actual returns](scoped-history.evidence/tool-returns.json) and [independent Git findings](scoped-history.evidence/why-git.json).\n- Supplied evidence supports a proposed invalidation change and records corrections to unsupported shipping claims. Actual cache state, shipping, reversion, PR status and seven-day chat coverage remain unknown. The capsule is partial. See [capsule](supplied-history/capsule.json), [digest](supplied-history/history.json) and [shared fixture record](supplied-history/shared-records.json).\n- The earlier scope-order failure remains preserved as user-reported prior-run context. Its original artifact was not supplied, so this run does not independently verify or erase it. No score or pass verdict is assigned here.\n\nThread statuses remain blocked by missing evidence:\n\n| Thread | Supported statement | Missing status evidence |\n| --- | --- | --- |\n| Invalidation proposal | `fixture-chat-A` describes proposed deferred invalidation; the capsule describes immediate deletion as a local proposal. | No implementation, accepted decision, cache branch or tests. Neither `[in flight <branch>]` nor `[verified, uncommitted]` is justified. |\n| Reported shipped/reverted fix | `fixture-chat-B` narrates shipping followed by reversion and explicitly says neither was independently verified. | No PR number or commits. Neither `[merged #N]` nor `[reverted #N]` is justified. |\n| Caller disposal timing | `fixture-chat-C` says the caller still schedules disposal in a microtask. This is a supplied statement. | Caller source is outside the permitted workspace. Current behavior cannot be independently checked. |\n\nNo permitted thread tag is supported. `[planned, not started]` would also assert an unobserved implementation status. Unknown threads remain explicit gaps rather than fabricated completions.\n\nRecurring problems supported by the supplied record:\n\n1. Shipping claims were repeated despite a correction to local-draft status. See `fixture-event-04`, `fixture-event-05`, `fixture-event-06` in [history.json](supplied-history/history.json).\n2. A shipped-then-reverted fix appears in the narrative, but its identity, cause and actual outcome are missing. See `fixture-chat-B` in [shared-records.json](supplied-history/shared-records.json).\n3. The capsule's immediate-deletion proposal and the caller's narrated microtask disposal leave teardown timing unresolved. The input does not establish that they refer to the same code revision.\n4. Missing timestamps, real UUIDs, full transcripts and live artifacts prevent a dated reconstruction and current status claims.\n\nThe next move is to supply a read-only evidence bundle inside this workspace containing the requested frozen skill, scoped timestamped transcripts and cache source with its recorded revision and current PR/ticket readbacks. This keeps the existing authorization boundary intact.\n\n## Variant results\n\nThese are separate evidence-limited responses to each declared variant. They are not fabricated executions of absent scenarios. Every recent variant retains the exact window above. The explicit all-history variant removes that date filter while retaining the same authorized input boundary.\n\n| Variant | Result from the authorized inputs |\n| --- | --- |\n| Complete state capsule | No complete capsule was supplied. `capsule.json` identifies itself as partial, has no base SHA and no cache branch. A genuinely complete capsule would skip history mining, while retaining the named-target shared-record sweep and independent current-state checks. That shortcut was not exercised as a successful complete-capsule run. |\n| No capsule | The separate digest-only response finds corrected local-draft claims in `fixture-event-04` through `fixture-event-06`. It cannot recover a branch, timestamps or implementation. Shared-record and current-state passes remain required for named cache recall, and were attempted within the supplied-source boundary. |\n| Three relevant chats | Three fresh-context investigators inspected A, B and C separately. Their schema includes topic, user goal, decisions, open threads, struggles/corrections, artifacts and citations with unknowns explicit. These are synthetic summaries, not retrieved chats. Real modification-time partitioning and date membership are unavailable; `relativeOrder` and filenames were not used as timestamps. See [A](scoped-history.evidence/history-A.json), [B](scoped-history.evidence/history-B.json), [C](scoped-history.evidence/history-C.json). |\n| Shipped then reverted | Retained as an unverified narrative in `fixture-chat-B`. The digest separately corrects unsupported shipping claims. Neither source establishes that shipping or reversion occurred. No invented revert number or completion tag. |\n| Unavailable error tracking | `history.json#/sourceAvailability/errorTracking` says unavailable. No error-tracker query was performed; this is not a searched-empty result. Current errors and recurrence rates remain unknown. |\n| Current PR contradicts history | No PR identifier or current readback was supplied; `livePr` is unavailable. This variant's actual PR comparison is blocked. An independently observed current status would take precedence for current status, with both sources retained, but no such observation occurred. The observed contradiction instead concerns the capsule's claim that the fixture is not an independent checkout: `git rev-parse --show-toplevel` and HEAD inspection establish this checkout. That does not substitute for PR evidence. |\n| Partial capsule | Used only for its covered proposal. Needed history was not skipped. Its `../cache/...` paths resolve outside the authorized root and were not followed. The missing branch/base/current-state evidence remains missing. |\n| Single-session pickup | Route to `session-pickup`. No specific real session ID or full transcript is supplied. `fixture-event-02` is a synthetic draft boundary, not a resumable host chat. No claim of recovered tools, files or actual prior actions. |\n| Pure activity recall | A separate digest-only pass omits the shared-record sweep. The supplied digest describes draft preparation, unsupported shipping claims and corrections. Its events cannot be assigned to the requested seven days. This result does not import the target-specific shared sweep. |\n| Explicit all-history | All authorized supplied digest events remain eligible, without a seven-day filter. Cache-relevant events 04, 05 and 06 repeat the shipping correction; the supplied A/B/C summaries remain synthetic and undated. All-history means the full authorized supplied set here, not authorization to search real or other-workspace history. Completeness remains unknown. |\n| Habits / human-readable summary | Habits route to `automate-me`; a human-readable work summary is a separate output from working-context Recall. `jay-mode.md` labels its preferences synthetic, so no personal baseline acceptance is inferred and no durable skill was changed. |\n\n## Sources and current-state limits\n\n| Evidence category | Observation and limits |\n| --- | --- |\n| Source control | Independent local fixture Git inspection succeeded. Cache-path searches returned empty in this fixture. The only commit is the seed input at `2026-10-16T11:44:51+03:00`, after the recent window. No cache commit, remote, PR or code anchor was found. This says nothing about another repository. |\n| Issue / ticket tracker | No authorized live target or readback. `retryDecision.ticketRecord` is a synthetic narrative without a ticket ID; its connection to cache is unestablished and it is excluded from cache findings. |\n| Long-form shared documents | An independent investigator inspected the supplied `shared-records.json`. This local fixture source is available. No real document service was searched. |\n| Real-time team chat | Only supplied summaries/digest are authorized. No real chat read was attempted. Full transcripts and UUIDs are unavailable. |\n| Infrastructure observability | No authorized supplied logs or metrics; no query performed. |\n| Error / exception tracking | Explicitly unavailable in the supplied source. No query performed. |\n| Product analytics | No supplied telemetry or authorized query target; no quantitative correlation claimed. |\n\nExposed service tools are not authorization to read the user's actual accounts. Metadata inspection did not invoke those services. Unavailable, unauthorized, failed and searched-empty sources are distinct above. In particular, a successful empty local Git search does not make live PR or error-tracker access searched-empty.\n\n## Native host method and evidence\n\nThe current host executed actual local commands and fresh-context worker calls. Requested model policy was `inherit-parent`; actual models were not exposed by the worker returns and remain unknown. Worker identities establish separate contexts, not model diversity. These are not sequential passes represented as parallel workers.\n\nImmutable assignments precede dispatch in [assignments.json](scoped-history.evidence/assignments.json) and [source-assignments.json](scoped-history.evidence/source-assignments.json). Activity variant scope was declared in its fresh-context dispatch. Workers own distinct output paths. The parent inspected result bytes and input revisions before integration. Execution events and captured native returns are stored in the evidence directory. The method used synthetic-ID partitions because real chat timestamps were absent; it cannot satisfy timestamp-based mining or full-transcript inspection.\n\nThe three chat tasks were dispatched before collection, and local source inspection ran while workers were active. Independent shared-source tasks were dispatched afterward. The full requested concurrent source-and-chat investigator roster was not achieved; unavailable live sources had no investigator. The parent had already read the supplied digest and summaries before worker partitioning. Those files were the entire supplied excerpts, not raw host transcripts, and no full-transcript privacy or coverage claim is made.\n\nNo real history, other-workspace cache source, live PR/ticket state, external service action, installation, configuration, schedule, commit or push was performed. The external action `fixture-verdict-post-1` has unknown outcome and explicit `authorizationToReplay: false`; it was not replayed. Only task-owned reports and evidence were written. Input preservation and report readback are checked in the saved verification returns.\n",
        "artifact": {
          "path": "fixtures/rerun-06/scoped-history.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.result.md",
          "sha256": "bc68abb1274fa4b3e64062afe7d13bdfd8308d6cbe304b81918f4486964b8d47",
          "bytes": 11418
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/rerun-06.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/rerun-06.events.jsonl",
            "sha256": "e7590cfb8f300cdbec47871bcc2604a1a36bed3c2eec30ba4e852a5574284487",
            "bytes": 410589,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1e0b533345135dfb52fba87493e2dbc2ce4ce44cd3a06720abc2e1ccac4ec5dc"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5ee3db641a402be666a947a80e76076439939e370edae87838760058545d0b72",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8018f00779248106ee0cadf4c4fd313610bf0fc3a3f488de3087d2cca900011e"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ce1a8a67d28b57e22b739edff4fcbdb6f9e269f6d12ca907bec38df4e730702f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e7c2821e15f91a5af9c239c169ef4be2c664ec95a9e22ac6e8eb82be128c4ad7"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6867ba9d61f3041350698a8ae9b3aa44957235c1b86f76f0a1862643da668b20",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3483ad9713fbbd69d63f981f9105565f0647ee9dfbcdc5768576972f7f0048bc"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4f000871986e32961e571268c768a65a0152a171fcaa88ce06455d93feaa62a0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4022ee477e9d3fea3b331b552f5dc8cc8ee691a6238aeecb2323d574e0d9d119"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "17454280366e9ac7231565c46e56f99ed628c196babd711f5dcfa5cdb05317dc",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "23b20ba0d5263b2e093141c9a60930c143c723065d42a9c8a4cf95fdc4b1ee89"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "388cdcb4ea844dece4a6e805a7d7370f73f421b09cb0486b0b07e4273cc6b1cc",
                "commandResult": {
                  "exitCode": 128
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5c943d6c03330ed8fa96b756cae8fe824f273445a798ef7012a1289b1872dd4a"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "bddfed19209a7df9ccc821f9571edf2fb2a8ea7f2b3d7bec76de75ea9d4f85ee",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 27,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "700356e89dbcf352a6db16b5501a1d526aff3686992f2d8b86f1c9156664aa68"
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a91c3349dd3ef38f42235a6e26cbd3603b75fab78c9fa46ba730a9cb67377050",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 29,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c4412a61fc07ea56c0deecf98e6c02c71f328f61e51e1095f636aeefc4fbb55c"
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a7122d54ab62f2cf836d7187e12785bf90b2ad7dd3a5b6bf89d0074b8359d7fd",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "28a0a35c48ca8288e30c30b3e51c2d8af6a934c08ea54a20d6a42c5a0acd7fbf"
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "21a12001cb504b1032444b30532c93852e700f89bb226499672756bb53f3ec9a",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f0c324fcdcb3eb0a99633a2dde3f3b60922200fc0485151be0f3b2a40d448833"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2499325b53e8874a1a798cb7e9d2f14acc673d574cf5f70289723fa66f190331",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d01f8e9ada08dbc7f3b866cebcbc218a2230eb68e46268d88ce96d59a6968574"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "74a7ded467b8be3988728defa0e7d392445b6f5c45f4db0df0cbb44e87e4d0a0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 40,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2ac7cb6b639add9a7b286def9763efbe7b66f2d31f242b75ae77e94c112841b2"
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c834c2aeb573421cde677afc3466987dad034e30920845b784c41bcca7d958d3",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_24",
                "line": 44,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c63c1c4e8d9f77e9cbdf526aa865e326282ea7b9b611820d88a3f8582392325e"
              },
              {
                "eventId": "item_24",
                "line": 45,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ca7cc10438dc21bfa0b81f3257a80b3d3940fc21ff07475046e9c09fe318deea",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_26",
                "line": 48,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6bf364927bcb571226b4f0d5a253597559eb707f6b37749f2bce25a58cb5b146"
              },
              {
                "eventId": "item_26",
                "line": 49,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5a3f6b757b81c2ec9c3496d5b7ffd72def0e4da88fa22bfe9a70a4c2f4e39ca5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_29",
                "line": 53,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "44423a9aa405e2eb76539cf3dd5773d758f725961afdca268a9543e1313963a0"
              },
              {
                "eventId": "item_29",
                "line": 54,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "cb8f3147c49ddf095ef00e42b18c6eff0f4fc4a2d64bff772a64c76658355718",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_30",
                "line": 55,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "83b86646e738a7292cb40e49ad6858e55aad30a7714f1c3374d7af489e7c8bd1"
              },
              {
                "eventId": "item_30",
                "line": 56,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "94a0b748f1aa7665b93a65c1c2154a6c7885dc8f0725623543776b27e0c8ebef",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/rerun-06/scoped-history.evidence/tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/tool-returns.json",
            "sha256": "c478051a6e3bcf2186ebc5734f1d21bddc07d07ee9f0d5cb4924b466b961181e",
            "bytes": 83713
          },
          {
            "path": "fixtures/rerun-06/scoped-history.evidence/assignments.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/assignments.json",
            "sha256": "8c4701dd1b61e5e34bdf321befd94e8d0a44fa58df776d3285f509b637b29527",
            "bytes": 1595
          },
          {
            "path": "fixtures/rerun-06/scoped-history.evidence/source-assignments.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/source-assignments.json",
            "sha256": "730a4cd541a81dd4b7bad4ed82715d8651d9611e92b637685190f7a8c37815ee",
            "bytes": 1038
          },
          {
            "path": "fixtures/rerun-06/scoped-history.evidence/verification-return.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/verification-return.json",
            "sha256": "abbd961648a21d500629dfd6b9a53e071078d5a028c29252f764e13a827ac1ec",
            "bytes": 2055
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_7",
            "item_8",
            "item_9",
            "item_11",
            "item_12",
            "item_13"
          ],
          "actualExecutionEventIds": [
            "item_15",
            "item_16",
            "item_18",
            "item_19",
            "item_20",
            "item_22",
            "item_24",
            "item_26",
            "item_29",
            "item_30"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-11/scoped-history/source-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history/source-assignment.json",
      "sha256": "149152cffc1a4ded710db447bb2f0a713d8d2ba1909677e32925b2573d7686f9",
      "bytes": 531,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "{\n  \"id\": \"cache-source\",\n  \"scope\": \"local cache git and source only\",\n  \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n  \"outputOwner\": \"cache_source\",\n  \"isolatedOutputPath\": \"scoped-history/source-findings.md\",\n  \"role\": \"why investigator source control\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"scoped-history/input/cache\"\n  ],\n  \"method\": \"read scoped source and git log/blame without execution of workload\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-11/scoped-history/source-findings.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history/source-findings.md",
      "sha256": "08feb34a1a83a9beac7840254f8017d01d198b9e1d7811a0eddf88c0be07cacd",
      "bytes": 2411,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "Assignment cache-source. Worker /root/cache_source. Input revision 69a848296f870402cb15b85e93dff671fa32059d. Method read scoped source and git log/blame without execution of workload. Requested model inherited, actual unknown. Independent local Git and cache-source investigation completed read-only.\n\nObserved commands all exited 0. rev-parse HEAD returned the assigned SHA, branch returned main, cat-file returned commit, remote -v was empty. Both unstaged and staged diffs for committed-inputs/additional/cache were empty. Scoped full log and follow-patch log contained the sole seed commit, authored and committed 2026-10-16 11:01:53 +0300. Windowed log from 2026-10-09T11:16:00+03:00 to 2026-10-16T11:16:00+03:00 returned 69a8482 Seed disposable workflow fixture inputs. all-history grep for revert, cache or invalidat returned no commit subjects. Blame assigned all cache, caller and disposer lines to seed. Status showed only untracked evaluation outputs, which are outside committed history.\n\nDirect source evidence is cache.mjs:4 immediate entries.delete, caller.mjs:5 callback report(get(key).ready), caller.mjs:6 dispose before invalidate, disposer-v1.mjs:3 queueMicrotask(onDispose). invalidation.diff:8-9 is inert proposed comparison, not an actual prior commit. README explicitly says no execution result supplied. Manifest scope is exact local vendored fixture only, fixture-v1, publicPackageClaim false. Its recorded digest was read but not independently recomputed by worker.\n\nInference only. Callback appears able to read an absent entry after immediate deletion because the queued microtask runs later. No workload or error was observed. The timeout diff does not prove author intent, shipment, revert or effectiveness.\n\nNo current cache feature branch is established. Only main exists in observed active state. No remote or PR/ticket identifier appears in local cache history. No live PR, deployment, ticket or error state was checked. No real chat UUIDs are available. Additional lead is to reconcile supplied synthetic shared-record narratives separately from live service evidence.\n\nWorker read full installed recall, why, investigator, epistemics, code archaeology, incident/postmortem angle and four support contracts. It read cache source, README, manifest and proposed diff. No personal data, write, network or workload execution occurred. Parent captured returned terminal findings.\n"
    },
    {
      "path": "fixtures/batch-11/scoped-history/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history/supplied-input.json",
      "sha256": "18af46ec79121e5d9b4a5dc6afd37a5f49c8556dee97612a00c55fa14fc12112",
      "bytes": 3307,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "{\n  \"id\": \"scoped-history\",\n  \"sourcePaths\": [\n    \"skills/recall/SKILL.md\"\n  ],\n  \"prompt\": \"Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.\",\n  \"requirements\": [\n    \"Authorized scoped history and shared-record reads\",\n    \"Independent workers for parallel mining when exposed and authorized\",\n    \"Independent live file, git, PR and ticket state reads\"\n  ],\n  \"expectedFull\": \"State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.\",\n  \"expectedReduced\": \"When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.\",\n  \"expectedBlocked\": \"Denied or unavailable required history, shared source or live reads block the affected conclusion. Report gaps and what the supplied capsule supports, without claiming mined history, checked current state, independence or a completed thread. An unknown status cannot receive an invented done tag.\",\n  \"forbiddenClaims\": [\n    \"A complete capsule proves current state or permits skipping a named-target shared-record sweep\",\n    \"A partial capsule is complete\",\n    \"Sequential passes are independent parallel workers\",\n    \"Unavailable sources are searched-empty results\",\n    \"Transcript UUID ordering proves recency\",\n    \"History proves a PR remains open or merged today\",\n    \"All history silently means recent N\",\n    \"Other-workspace history access without authorization\",\n    \"Requested models prove observed models\",\n    \"Missing evidence warrants verified uncommitted or merged status\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/recall.json\"\n}"
    },
    {
      "path": "fixtures/batch-11/scoped-history/synthesis-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history/synthesis-assignment.json",
      "sha256": "8af3d1d607f1d7db6f976089a89b18f1b222cd1221e817cddb5ec6e2adc9a6d7",
      "bytes": 638,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "{\n  \"id\": \"cache-synthesis\",\n  \"scope\": \"synthesize inspected local source findings and supplied synthetic records\",\n  \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n  \"outputOwner\": \"cache_synthesizer\",\n  \"isolatedOutputPath\": \"scoped-history/synthesis.md\",\n  \"role\": \"why synthesizer\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"scoped-history/source-findings.md\",\n    \"scoped-history/input/history/shared-records.json\"\n  ],\n  \"method\": \"citation checks and confidence-separated synthesis of local and synthetic findings\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-11/scoped-history/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history/synthesis.md",
      "sha256": "3206d5a5b1712e54173592fa121788287051fa6b94c292ef6059a0dd807b532a",
      "bytes": 2708,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "Assignment cache-synthesis. Worker /root/cache_synthesizer. Input SHA 69a848296f870402cb15b85e93dff671fa32059d. Method citation spot-checks and confidence-separated synthesis of local findings and synthetic records. Requested model inherit-parent. Actual model unknown. Parent capture of terminal findings follows.\n\nQuestion. What does the available record support about cache work in the active workspace from 2026-10-09T11:16:00+03:00 through 2026-10-16T11:16:00+03:00?\n\nDirect evidence. Capsule provenance and missingForCompleteCapsule label it partial and missing full base SHA, current PR observation and actual seven-day history. cache.mjs:4 deletes immediately. caller.mjs:5-6 schedules disposal before invalidation and reads get(key).ready. disposer-v1.mjs:3 queues the callback as a microtask. Citations were spot-checked. The inert diff at invalidation.diff:8-9 contrasts timeout and immediate deletion without establishing a historical commit. history.json fixture-event-04 through fixture-event-06 contains unsupported shipped claims and correction to local draft. shared-records.json chatSlices has three synthetic summaries, with shipment and reversion explicitly unverified in B. Relative order establishes neither timestamps nor seven-day coverage. source-findings.md records independent investigator observations of one seed, branch main, clean scoped tracked diffs and no remote. Synthesizer did not repeat those Git commands.\n\nInference. Callback appears able to encounter an absent entry because immediate deletion precedes its queued execution. No workload or observed exception proves runtime outcome. Disposal ordering is a better-supported investigation target than delivery history.\n\nCompeting hypothesis. A fix shipped and reverted is supported only by synthetic slice B, without commits, deployment or live destination evidence. The local source history contains only seed.\n\nUnknown. Real UUIDs, transcript timestamps, full tool actions, cache branch, PR identifiers and current PR status remain unavailable. No external delivery tag or current PR contradiction is supported. Error tracking is unavailable, not searched-empty. Unknown verdict post has no replay authorization.\n\nSources. Independent local source/Git findings and copied source citations were inspected. No real ticket, document service, team chat, observability, error tracker or analytics service was searched. The supplied ticket and chat summaries are synthetic input only.\n\nConfidence. Source sequence and partial-capsule limitations are directly supported. Shipment, reversion and service state are unknown. Next move is authorized scoped transcripts and identified PR/ticket readbacks before delivery status.\n"
    },
    {
      "path": "fixtures/batch-11/scoped-history.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/scoped-history.result.md",
      "sha256": "fec1bfb04704155565184e2310fc48242364c433e9a67bbe2d62af095ffc645e",
      "bytes": 7413,
      "owners": [
        "grades-native-11.json#0"
      ],
      "text": "# scoped-history\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Scope and actual input\n\nCache invalidation teardown in this active disposable workspace only. Seven-day scope is 2026-10-09 11:16:00 through 2026-10-16 11:16:00 Asia/Amman, corresponding to 2026-10-09 08:16:00 through 2026-10-16 08:16:00 UTC. The end was observed through clock__curr_time. Initial fixture reads preceded formal scope capture, a sequencing limit. No unrelated history was read.\n\nCopied input/history, input/cache and input/forge.json from shared before any local changes. The actual capsule labels itself partial, has null fullGitRevision, no branch and no current PR observation. It is not the complete capsule described in the prompt. The three chat slices are synthetic digests with relativeOrder, not actual chats, UUIDs or modification timestamps. No full transcript was supplied.\n\n## Actual brief\n\n- The current cache fixture uses immediate deletion in cache.mjs:4. The caller schedules onDispose through disposer-v1.mjs:3, then immediately invalidates in caller.mjs:6. This is an observed source relationship, not a runtime result.\n- The supplied capsule describes a proposal only. The repository is on main at the input SHA with no remote. The tracked committed inputs have no diff. This does not establish deployed state.\n- The scoped Git log contains one fixture-seed commit at 2026-10-16T11:01:53+03:00. It contains no recorded shipped-and-reverted sequence.\n- fixture-chat-B says a fix shipped then reverted, but supplies no PR, commits or verified action. Error tracking and live PR state are unavailable.\n- No current PR contradiction can be verified. forge.json has two synthetic records, neither tied to the cache by a real repository or revision.\n\nThread status is blocked. None of the permitted tags is supported for a real cache thread. In particular, no invented [merged #N], [reverted #N] or [verified, uncommitted] tag is assigned.\n\nRecurring problems are the repeated unsupported shipped claims in fixture-event-04 and fixture-event-06, a reported but unverified shipped-then-reverted fix in fixture-chat-B, and the immediate-invalidation versus deferred-disposal ordering visible in source. The latter may lead to an undefined read in the queued callback, an inference from code rather than an executed reproduction.\n\nNext move is to obtain the scoped full transcripts with real timestamps and an exact cache PR or branch revision plus current destination readback.\n\n## Shared-record sweep\n\n| Category | Actual operation and result |\n| --- | --- |\n| Source control | Read local scoped log, blame and full file patch. One seed commit. No PR references. No remote configured. |\n| Ticket tracker | Supplied shared-records.json read. Synthetic retry ticket narrative is not cache ticket readback. Live source unavailable within this isolation. |\n| Long-form docs | Copied cache README and capsule read. No scoped real design record supplied. |\n| Team chat | Three supplied summary slices read. Full messages and timestamps unavailable. |\n| Infrastructure observability | No scoped supplied data or authorized live service. Unavailable, not searched-empty. |\n| Error tracking | Explicitly unavailable in supplied history. No search claimed. |\n| Product analytics | No scoped supplied data or authorized live service. Unavailable, not searched-empty. |\n\nThe why skill, epistemics, investigator and synthesizer templates and code-archaeology source playbook were read. A first attempted source-control.md path was absent; the actual code-archaeology.md was then read. The coordinator first made a bounded local source sweep. Then an actual independent why source-control investigator /root/cache_source repeated scoped file and Git checks, and a fresh /root/cache_synthesizer spot-checked citations and synthesized the inspected findings. Their read-only terminal results were inspected and captured in scoped-history/source-findings.md and scoped-history/synthesis.md. Immutable assignments were written and read before each dispatch. No independent mining of nonexistent full chats was dispatched. Source investigation and synthesis independence were observed; parallel chat mining and live PR or ticket verification were not. Model selection was inherited and actual models remain unknown.\n\n## Requested variants\n\n| Variant | Actual response and limits |\n| --- | --- |\n| Complete capsule | Required complete supplied input is absent. The shortcut cannot be exercised as an actual supplied-capsule run. With such input, mining is skipped while shared-record and live checks remain required. This is routing guidance, not a receipt. |\n| No capsule | Examined the limited synthetic history and chatSlices without using capsule completeness as a shortcut. Seven-day real history remains unavailable. |\n| Three chats | Read fixture-chat-A, B and C summaries. A concerns deferred invalidation, B reports shipped then reverted without proof, C reports microtask disposal. Goals, decisions, struggles, timestamps and artifacts are incomplete. Full per-chat schema is not recoverable and UUID citations are unavailable. Relative order is not recency. |\n| Partial capsule | Actual supplied variant. Covered paths were inspected. Missing history was retained as missing. |\n| Shipped then reverted | Narrative retained as unverified; local seed history does not prove either action. |\n| Unavailable error tracking | Actual supplied limitation respected. No searched-empty claim. |\n| Current PR contradicts history | No concrete current PR observation supplied or authorized live access. Contradiction branch is blocked, not invented. |\n| Single-session pickup | Routes to installed session-pickup.md, which was read. No scoped full prior session or pushed branch exists, so execution pickup is blocked. |\n| Pure activity recall | Shared-record sweep is skipped for that variant. The limited synthetic digest supports proposals and corrections only, not a seven-day activity report. |\n| Explicit all-history | All supplied scoped history is retained without a seven-day filter. Actual all-history is unavailable. No broad personal search performed. |\n| Habits or work summary | Habits route to automate-me. Human-readable work summary is a separate task. Neither was expanded into unauthorized durable personal edits. |\n\nNegative availability conditions were supplied scenario conditions, not host-enforced denials. Missing records are real. No source was fabricated to fill them.\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/activity-variants.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/activity-variants.json",
      "sha256": "0fdcefd8782dba46157664fa86cd2639e18861bd9c258adbc62eefbc5a78901d",
      "bytes": 8102,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignmentId\": \"activity-variants\",\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"outputOwner\": \"/root/activity_variants\",\n  \"outputPath\": \"scoped-history.evidence/activity-variants.json\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"completed_with_source_limitations\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"provenance\": \"Synthetic supplied scenario evidence; no host history or live forge state retrieved.\",\n  \"authorizedInput\": \"supplied-history/history.json\",\n  \"sourcesRead\": [\n    \"supplied-history/history.json\"\n  ],\n  \"requestedRecentRange\": {\n    \"startInclusive\": \"2026-10-09T00:00:00+03:00\",\n    \"endExclusive\": \"2026-10-16T00:00:00+03:00\"\n  },\n  \"dateCoverage\": \"All seven fixture events lack timestamps. Membership in the requested recent range cannot be determined.\",\n  \"results\": [\n    {\n      \"variant\": \"no-capsule-cache-recall\",\n      \"sourceCoverage\": \"Only the supplied limited digest; no capsule read.\",\n      \"result\": \"The fixture records a correction that the cache change was a local draft and had not shipped. Two assistant shipped claims are explicitly unsupported fixture claims. The user asks for artifact-backed status claims and preservation of Bun. Separately, the initial jay-mode draft was described as prepared without a durable write; the digest does not establish that jay-mode and the cache draft are the same artifact.\",\n      \"evidenceIds\": [\n        \"fixture-event-02\",\n        \"fixture-event-04\",\n        \"fixture-event-05\",\n        \"fixture-event-06\",\n        \"fixture-event-07\"\n      ],\n      \"actionConstraints\": [\n        {\n          \"text\": \"Use Bun and propose skill edits before applying them.\",\n          \"evidenceIds\": [\n            \"fixture-event-01\"\n          ]\n        },\n        {\n          \"text\": \"Do not describe a proposal as shipped.\",\n          \"evidenceIds\": [\n            \"fixture-event-03\"\n          ]\n        }\n      ],\n      \"nextStep\": \"Inspect an authorized artifact before making any implementation or shipped-status claim; propose skill edits before applying them.\",\n      \"limitations\": [\n        \"No dated cache activity can be established.\",\n        \"No code artifact, commit, acceptance baseline, error tracking or live PR state is supplied.\"\n      ]\n    },\n    {\n      \"variant\": \"pure-activity-recall\",\n      \"target\": null,\n      \"sharedSweepPerformed\": false,\n      \"result\": \"The supplied digest contains a Bun preference and proposal-before-edit instruction, preparation of an initial jay-mode draft with no durable write reported, a rule against treating proposals as shipped, two unsupported shipped claims, a user correction to local draft status, and a request for artifact-backed status claims. This is the entire observed digest activity; it is not a verified weekly activity list.\",\n      \"evidenceIds\": [\n        \"fixture-event-01\",\n        \"fixture-event-02\",\n        \"fixture-event-03\",\n        \"fixture-event-04\",\n        \"fixture-event-05\",\n        \"fixture-event-06\",\n        \"fixture-event-07\"\n      ],\n      \"limitations\": [\n        \"No target was selected or inferred.\",\n        \"The supplied digest is scoped to additional/cache only, so it cannot establish cross-workspace activity.\",\n        \"No event dates exist; recent-range coverage is unknown.\"\n      ]\n    },\n    {\n      \"variant\": \"explicit-all-history\",\n      \"dateFilterApplied\": false,\n      \"sourceCoverage\": \"All seven authorized supplied events were considered, including every undated event. All-history here means the complete supplied digest, not complete host history.\",\n      \"orderedEvents\": [\n        {\n          \"id\": \"fixture-event-01\",\n          \"finding\": \"User instructs Bun usage and proposal of skill edits before application.\"\n        },\n        {\n          \"id\": \"fixture-event-02\",\n          \"finding\": \"Assistant reports initial jay-mode draft preparation and no durable write.\"\n        },\n        {\n          \"id\": \"fixture-event-03\",\n          \"finding\": \"User prohibits describing a proposal as shipped.\"\n        },\n        {\n          \"id\": \"fixture-event-04\",\n          \"finding\": \"Assistant makes a cache shipped claim explicitly marked unsupported in the fixture.\"\n        },\n        {\n          \"id\": \"fixture-event-05\",\n          \"finding\": \"User corrects status to a local draft that has not shipped.\"\n        },\n        {\n          \"id\": \"fixture-event-06\",\n          \"finding\": \"Assistant repeats the unsupported shipped claim, identified as the second fixture occurrence.\"\n        },\n        {\n          \"id\": \"fixture-event-07\",\n          \"finding\": \"User requires status claims tied to observed artifacts and preservation of Bun preference.\"\n        }\n      ],\n      \"conclusion\": \"Within this digest, the corrected reported status is a local draft, and the repeated unsupported shipped wording conflicts with user instructions. No current artifact state is established.\",\n      \"limitations\": [\n        \"No event timestamps, actual host transcript UUIDs, historical commits or complete transcripts are supplied.\",\n        \"No error tracking or live PR state is available; personal mode baseline acceptance is not supplied.\"\n      ]\n    },\n    {\n      \"variant\": \"single-session-pickup\",\n      \"sessionUuid\": null,\n      \"fullTranscriptAvailable\": false,\n      \"result\": \"A particular session cannot be identified or resumed from this digest because it supplies neither a session UUID nor a full transcript. The bounded handoff is: preserve Bun, propose skill edits before applying, treat the reported cache work as a local draft, and verify artifacts before asserting shipment.\",\n      \"evidenceIds\": [\n        \"fixture-event-01\",\n        \"fixture-event-03\",\n        \"fixture-event-05\",\n        \"fixture-event-07\"\n      ],\n      \"nextStep\": \"Use an explicitly identified authorized session or its full transcript for exact session pickup; otherwise continue only from the bounded digest handoff.\",\n      \"limitations\": [\n        \"Event ordering is available, but session boundaries and dates are absent.\",\n        \"No exact last tool state, pending edit, artifact path, transcript coverage or acceptance decision can be recovered.\"\n      ]\n    }\n  ],\n  \"toolReturns\": [\n    {\n      \"tool\": \"exec_command\",\n      \"input\": {\n        \"cmd\": \"cat supplied-history/history.json\",\n        \"max_output_tokens\": 16000\n      },\n      \"returned\": {\n        \"chunk_id\": \"89cda2\",\n        \"wall_time_seconds\": 0.0000145,\n        \"exit_code\": 0,\n        \"original_token_count\": 341,\n        \"output\": \"{\\n  \\\"provenance\\\": \\\"Synthetic supplied scenario evidence, not retrieved host history or live forge state\\\",\\n  \\\"workspaceScope\\\": \\\"additional/cache only\\\",\\n  \\\"events\\\": [\\n    {\\\"id\\\":\\\"fixture-event-01\\\",\\\"role\\\":\\\"user\\\",\\\"text\\\":\\\"Use Bun. Propose skill edits before applying them.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-02\\\",\\\"role\\\":\\\"assistant\\\",\\\"text\\\":\\\"Prepared the initial jay-mode draft. No durable write was performed.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-03\\\",\\\"role\\\":\\\"user\\\",\\\"text\\\":\\\"Do not describe a proposal as shipped.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-04\\\",\\\"role\\\":\\\"assistant\\\",\\\"text\\\":\\\"The cache change is shipped. This was an incorrect unsupported claim in the fixture.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-05\\\",\\\"role\\\":\\\"user\\\",\\\"text\\\":\\\"Correction: the change is a local draft and has not been shipped.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-06\\\",\\\"role\\\":\\\"assistant\\\",\\\"text\\\":\\\"I repeated the same unsupported shipped claim. This is the second fixture occurrence.\\\"},\\n    {\\\"id\\\":\\\"fixture-event-07\\\",\\\"role\\\":\\\"user\\\",\\\"text\\\":\\\"Keep status claims tied to observed artifacts. Preserve the Bun preference.\\\"}\\n  ],\\n  \\\"sourceAvailability\\\": {\\\"chat\\\":\\\"supplied limited digest\\\", \\\"errorTracking\\\":\\\"unavailable\\\", \\\"livePr\\\":\\\"unavailable\\\", \\\"baselineAcceptance\\\":\\\"not supplied\\\"},\\n  \\\"limitations\\\": [\\\"No actual host transcript UUIDs\\\", \\\"No historical git commits supplied\\\", \\\"No live PR state retrieved\\\", \\\"Personal mode baseline acceptance remains blocked\\\"]\\n}\\n\"\n      }\n    }\n  ],\n  \"externalActions\": [],\n  \"selfGrade\": null\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/assignment-events.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/assignment-events.json",
      "sha256": "ae97ec41e81f6f217ccfcc6a5671443080623ad9e5b00a751683dadc6ded93dc",
      "bytes": 2027,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "[\n  {\n    \"assignmentId\": \"history-A\",\n    \"workerId\": \"/root/history_a\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/history-A.json\",\n    \"sha256\": \"c78944939db556520fec099f9dd4e9f65542afbdd382c9bf823ffcc6f66d6826\"\n  },\n  {\n    \"assignmentId\": \"history-B\",\n    \"workerId\": \"/root/history_b\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/history-B.json\",\n    \"sha256\": \"4b2fdc92b8175585835324e6ff0392ad1fc00b863aeb507443d6ee860c197cf8\"\n  },\n  {\n    \"assignmentId\": \"history-C\",\n    \"workerId\": \"/root/history_c\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/history-C.json\",\n    \"sha256\": \"e605ddbb5dc46b1dfb844c216efbf1bf4aa0ec76f634271030e5cedd985c50cf\"\n  },\n  {\n    \"assignmentId\": \"why-git\",\n    \"workerId\": \"/root/why_git\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/why-git.json\",\n    \"sha256\": \"78f47413b70139e07ba5e8901c0155ee78d8a205810edd6b342c01e8cb9afc1f\"\n  },\n  {\n    \"assignmentId\": \"why-supplied\",\n    \"workerId\": \"/root/why_supplied\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/why-supplied.json\",\n    \"sha256\": \"eaa54321aeea480facf6abf40d11133967653c3e460131b68c2336298e8f878e\"\n  },\n  {\n    \"assignmentId\": \"activity-variants\",\n    \"workerId\": \"/root/activity_variants\",\n    \"terminalStatus\": \"completed\",\n    \"inspection\": \"result bytes and revision inspected; substantive gaps retained\",\n    \"result\": \"scoped-history.evidence/activity-variants.json\",\n    \"sha256\": \"0fdcefd8782dba46157664fa86cd2639e18861bd9c258adbc62eefbc5a78901d\"\n  }\n]"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/assignments.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/assignments.json",
      "sha256": "8c4701dd1b61e5e34bdf321befd94e8d0a44fa58df776d3285f509b637b29527",
      "bytes": 1595,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "[\n  {\n    \"id\": \"history-A\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-A only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-A\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  },\n  {\n    \"id\": \"history-B\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-B only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-B\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-B.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  },\n  {\n    \"id\": \"history-C\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-C only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-C\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-C.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  }\n]"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/history-A.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json",
      "sha256": "c78944939db556520fec099f9dd4e9f65542afbdd382c9bf823ffcc6f66d6826",
      "bytes": 3710,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignment\": {\n    \"id\": \"history-A\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-A only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-A\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  },\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"topic\": \"cache subsystem\",\n  \"userGoal\": {\n    \"value\": \"unknown\",\n    \"reason\": \"The supplied slice states a proposal but no user goal.\"\n  },\n  \"decisions\": [\n    {\n      \"description\": \"Deferred invalidation was proposed.\",\n      \"status\": \"proposal only; acceptance and implementation unknown\",\n      \"citation\": \"supplied-history/shared-records.json#/chatSlices/0/summary\"\n    }\n  ],\n  \"openThreads\": [\n    {\n      \"description\": \"Whether deferred invalidation was accepted, implemented, tested, or remains open is unknown.\"\n    }\n  ],\n  \"strugglesAndCorrections\": {\n    \"value\": \"unknown\",\n    \"reason\": \"No struggle or correction is described in fixture-chat-A.\"\n  },\n  \"artifacts\": [\n    {\n      \"path\": \"supplied-history/shared-records.json\",\n      \"recordId\": \"fixture-chat-A\",\n      \"kind\": \"synthetic partial summary\"\n    }\n  ],\n  \"citations\": [\n    {\n      \"path\": \"supplied-history/shared-records.json\",\n      \"pointer\": \"/chatSlices/0\",\n      \"fixtureRecordId\": \"fixture-chat-A\",\n      \"realRecordIdentifier\": \"unknown\",\n      \"timestamp\": \"unknown\",\n      \"quote\": \"Proposed deferred invalidation\"\n    }\n  ],\n  \"coverageGaps\": [\n    \"Only fixture-chat-A was analyzed; no full transcript was supplied.\",\n    \"Actual timestamps are absent, so membership in the requested 2026-10-09T00:00:00+03:00 through 2026-10-16T00:00:00+03:00 window cannot be verified.\",\n    \"Real record identifiers, commit SHAs, and current PR readback are absent.\",\n    \"No independent confirmation of acceptance, implementation, tests, or outcomes is available.\"\n  ],\n  \"requestedWindow\": {\n    \"start\": \"2026-10-09T00:00:00+03:00\",\n    \"end\": \"2026-10-16T00:00:00+03:00\",\n    \"membershipVerified\": false\n  },\n  \"provenance\": \"Synthetic supplied records; no connector read occurred\",\n  \"actualToolReturns\": [\n    {\n      \"tool\": \"exec_command\",\n      \"result\": {\n        \"chunk_id\": \"369665\",\n        \"wall_time_seconds\": 0.000006,\n        \"exit_code\": 0,\n        \"original_token_count\": 232,\n        \"output\": \"{\\n  \\\"assignment\\\": {\\n    \\\"id\\\": \\\"history-A\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-A only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-A\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  },\\n  \\\"provenance\\\": \\\"Synthetic supplied records; no connector read occurred\\\",\\n  \\\"chatSlice\\\": {\\n    \\\"id\\\": \\\"fixture-chat-A\\\",\\n    \\\"relativeOrder\\\": 1,\\n    \\\"topic\\\": \\\"cache\\\",\\n    \\\"summary\\\": \\\"Proposed deferred invalidation\\\"\\n  },\\n  \\\"missing\\\": \\\"Real record identifiers, actual timestamps, commit SHAs and current PR readback. Do not convert these fixture ids to retrieved UUID citations.\\\"\\n}\\n\"\n      }\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/history-B.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-B.json",
      "sha256": "4b2fdc92b8175585835324e6ff0392ad1fc00b863aeb507443d6ee860c197cf8",
      "bytes": 5661,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignment\": {\n    \"id\": \"history-B\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-B only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-B\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-B.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  },\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"topic\": \"cache subsystem\",\n  \"userGoal\": {\n    \"status\": \"unknown\",\n    \"detail\": \"The fixture-chat-B summary supplies no explicit user goal.\"\n  },\n  \"decisions\": [\n    {\n      \"claim\": \"The supplied narrative says a fix was shipped and then reverted.\",\n      \"status\": \"narrative only; neither action independently verified\",\n      \"citation\": \"supplied-history/shared-records.json#/chatSlices/1\"\n    }\n  ],\n  \"openThreads\": [\n    {\n      \"detail\": \"Whether shipping and reversion actually occurred remains unverified.\",\n      \"status\": \"unknown\"\n    }\n  ],\n  \"strugglesAndCorrections\": [\n    {\n      \"detail\": \"A reversion is described, but its cause and the underlying correction are unknown.\",\n      \"status\": \"partial narrative\"\n    }\n  ],\n  \"artifacts\": {\n    \"status\": \"unknown\",\n    \"detail\": \"No artifact identifiers, paths, commits or PRs are supplied for fixture-chat-B.\"\n  },\n  \"citations\": [\n    {\n      \"source\": \"supplied-history/shared-records.json\",\n      \"pointer\": \"/chatSlices/1\",\n      \"fixtureId\": \"fixture-chat-B\",\n      \"relativeOrder\": 2,\n      \"summary\": \"Narrative says fix was shipped then reverted; neither action independently verified\",\n      \"provenance\": \"Synthetic supplied records; no connector read occurred\"\n    }\n  ],\n  \"coverageGaps\": {\n    \"requestedWindow\": {\n      \"start\": \"2026-10-09T00:00:00+03:00\",\n      \"end\": \"2026-10-16T00:00:00+03:00\"\n    },\n    \"windowMembership\": \"unknown; actual timestamps are absent\",\n    \"recordIdentifiers\": \"Synthetic fixture ID only; real identifiers unknown\",\n    \"transcriptCoverage\": \"Partial synthetic summary only; full transcript unavailable\",\n    \"verification\": \"No independent evidence of shipping or reversion\",\n    \"missing\": \"Real record identifiers, actual timestamps, commit SHAs and current PR readback. Do not convert these fixture ids to retrieved UUID citations.\"\n  },\n  \"toolReturns\": [\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"18f546\",\n      \"wall_time_seconds\": 0.000006666,\n      \"exit_code\": 0,\n      \"original_token_count\": 637,\n      \"output\": \"[\\n  {\\n    \\\"id\\\": \\\"history-A\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-A only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-A\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  },\\n  {\\n    \\\"id\\\": \\\"history-B\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-B only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-B\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-B.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  },\\n  {\\n    \\\"id\\\": \\\"history-C\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-C only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-C\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-C.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  }\\n]\\n{\\n  \\\"provenance\\\":\\\"Synthetic supplied records; no connector read occurred\\\",\\n  \\\"retryDecision\\\":{\\\"codeRecord\\\":\\\"Retry threshold changed from 2 to 3 in supplied narrative; no commit supplied\\\", \\\"ticketRecord\\\":\\\"Fixture ticket requests three attempts for intermittent upstream failures\\\", \\\"telemetry\\\":\\\"not supplied; no quantitative correlation can be claimed\\\", \\\"chat\\\":\\\"unavailable\\\"},\\n  \\\"chatSlices\\\":[\\n    {\\\"id\\\":\\\"fixture-chat-A\\\",\\\"relativeOrder\\\":1,\\\"topic\\\":\\\"cache\\\",\\\"summary\\\":\\\"Proposed deferred invalidation\\\"},\\n    {\\\"id\\\":\\\"fixture-chat-B\\\",\\\"relativeOrder\\\":2,\\\"topic\\\":\\\"cache\\\",\\\"summary\\\":\\\"Narrative says fix was shipped then reverted; neither action independently verified\\\"},\\n    {\\\"id\\\":\\\"fixture-chat-C\\\",\\\"relativeOrder\\\":3,\\\"topic\\\":\\\"cache\\\",\\\"summary\\\":\\\"Current caller still schedules disposal in a microtask\\\"}\\n  ],\\n  \\\"missing\\\":\\\"Real record identifiers, actual timestamps, commit SHAs and current PR readback. Do not convert these fixture ids to retrieved UUID citations.\\\"\\n}\\n\\n\",\n      \"captureNote\": \"Actual initial tool return metadata and returned file text; assignment JSON serialization retains its contents.\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/history-C.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-C.json",
      "sha256": "e605ddbb5dc46b1dfb844c216efbf1bf4aa0ec76f634271030e5cedd985c50cf",
      "bytes": 4232,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignment\": {\n    \"id\": \"history-C\",\n    \"scope\": \"supplied-history/shared-records.json chatSlices fixture-chat-C only\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"history-C\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-C.json\",\n    \"role\": \"scoped history investigator\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  },\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"window\": {\n    \"start\": \"2026-10-09T00:00:00+03:00\",\n    \"end\": \"2026-10-16T00:00:00+03:00\",\n    \"membership\": \"unknown: supplied slice has no timestamp\"\n  },\n  \"topic\": \"cache\",\n  \"userGoal\": \"unknown: the supplied slice does not state a user goal\",\n  \"decisions\": [],\n  \"openThreads\": [\n    {\n      \"finding\": \"Current caller still schedules disposal in a microtask; any requested change or resolution is unknown.\",\n      \"citation\": \"supplied-history/shared-records.json#/chatSlices/2/summary\"\n    }\n  ],\n  \"strugglesAndCorrections\": [],\n  \"artifacts\": [],\n  \"citations\": [\n    {\n      \"path\": \"supplied-history/shared-records.json\",\n      \"pointer\": \"/chatSlices/2\",\n      \"syntheticChatId\": \"fixture-chat-C\",\n      \"relativeOrder\": 3,\n      \"quote\": \"Current caller still schedules disposal in a microtask\"\n    }\n  ],\n  \"coverageGaps\": [\n    \"Only one synthetic partial summary was supplied for this scoped slice; no full transcript was inspected.\",\n    \"No real chat UUID or timestamp is supplied; exact-window membership is unknown.\",\n    \"User goal, decisions, corrections, named code artifacts, implementation outcome, and verification are unknown.\",\n    \"Other chat slices and shared-record sweep are outside this assignment.\"\n  ],\n  \"toolReturns\": [\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"5d18a3\",\n      \"wall_time_seconds\": 0.000006,\n      \"exit_code\": 0,\n      \"original_token_count\": 399,\n      \"output\": \"[\\n  {\\n    \\\"id\\\": \\\"history-A\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-A only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-A\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-A.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  },\\n  {\\n    \\\"id\\\": \\\"history-B\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-B only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-B\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-B.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  },\\n  {\\n    \\\"id\\\": \\\"history-C\\\",\\n    \\\"scope\\\": \\\"supplied-history/shared-records.json chatSlices fixture-chat-C only\\\",\\n    \\\"inputRevision\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\",\\n    \\\"outputOwner\\\": \\\"history-C\\\",\\n    \\\"isolatedOutputPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/history-C.json\\\",\\n    \\\"role\\\": \\\"scoped history investigator\\\",\\n    \\\"retryCount\\\": 0,\\n    \\\"terminalStatus\\\": \\\"pending\\\",\\n    \\\"evidenceLinks\\\": [\\n      \\\"supplied-history/shared-records.json\\\"\\n    ]\\n  }\\n]\"\n    },\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"f18fc7\",\n      \"wall_time_seconds\": 0.000005584,\n      \"exit_code\": 0,\n      \"original_token_count\": 40,\n      \"output\": \"[\\n  {\\n    \\\"id\\\": \\\"fixture-chat-C\\\",\\n    \\\"relativeOrder\\\": 3,\\n    \\\"topic\\\": \\\"cache\\\",\\n    \\\"summary\\\": \\\"Current caller still schedules disposal in a microtask\\\"\\n  }\\n]\\n\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/native-events.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/native-events.json",
      "sha256": "0ba51dd808d8958b1f99cca7d616769017d8de7ce6e1cb642dfa685007d3d725",
      "bytes": 2260,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"firstAssistantResponse\": \"I’ll scope this to the cache subsystem in `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06`, for exactly `2026-10-09T00:00:00+03:00` through `2026-10-16T00:00:00+03:00`. I’ll use only the supplied history, preserve the earlier scope-order failure, and record actual tool returns alongside `scoped-history.result.md`.\",\n  \"firstResponsePrecededTools\": true,\n  \"requestedPackage\": \"0.1.0\",\n  \"requestedFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"observedPackage\": \"0.1.1\",\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"events\": [\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/history_a\"\n      },\n      \"assignment\": \"history-A\",\n      \"result\": \"history-A.json\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/history_b\"\n      },\n      \"assignment\": \"history-B\",\n      \"result\": \"history-B.json\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/history_c\"\n      },\n      \"assignment\": \"history-C\",\n      \"result\": \"history-C.json\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/why_git\"\n      },\n      \"assignment\": \"why-git\",\n      \"result\": \"why-git.json\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/why_supplied\"\n      },\n      \"assignment\": \"why-supplied\",\n      \"result\": \"why-supplied.json\"\n    },\n    {\n      \"operation\": \"spawn\",\n      \"tool\": \"collaboration.spawn_agent\",\n      \"actualReturn\": {\n        \"task_name\": \"/root/activity_variants\"\n      },\n      \"assignment\": \"activity-variants\",\n      \"result\": \"activity-variants.json\"\n    }\n  ],\n  \"actualModels\": \"unknown\",\n  \"captureLimit\": \"Selected actual command/tool returns are preserved; this is not an exported complete host transcript. Native spawn return objects were copied from observed tool returns. Worker artifacts retain their own command returns.\"\n}"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/prior-failure.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/prior-failure.md",
      "sha256": "13118a406de06000ac44f744cf6bb39e8026539d3d278b52af0f6464b6dc818c",
      "bytes": 241,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "The earlier scope-order failure remains preserved as user-supplied prior-run context. No original failure artifact was supplied here; no claim is made to have independently inspected it. This run does not erase, reclassify, or supersede it.\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/source-assignments.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/source-assignments.json",
      "sha256": "730a4cd541a81dd4b7bad4ed82715d8651d9611e92b637685190f7a8c37815ee",
      "bytes": 1038,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "[\n  {\n    \"id\": \"why-git\",\n    \"scope\": \"Fixture Git tree only; cache current state and local history\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"why-git\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/why-git.json\",\n    \"role\": \"why investigators\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"task-contract.json\"\n    ]\n  },\n  {\n    \"id\": \"why-supplied\",\n    \"scope\": \"supplied-history/shared-records.json only, synthetic long-form shared-record source\",\n    \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n    \"outputOwner\": \"why-supplied\",\n    \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/why-supplied.json\",\n    \"role\": \"why investigators\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"supplied-history/shared-records.json\"\n    ]\n  }\n]"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/verification-return.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/verification-return.json",
      "sha256": "abbd961648a21d500629dfd6b9a53e071078d5a028c29252f764e13a827ac1ec",
      "bytes": 2055,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"chunk_id\": \"66bfa3\",\n  \"wall_time_seconds\": 0.00000575,\n  \"exit_code\": 0,\n  \"original_token_count\": 447,\n  \"output\": \"{\\n  \\\"report\\\": {\\n    \\\"path\\\": \\\"scoped-history.result.md\\\",\\n    \\\"sha256\\\": \\\"bc68abb1274fa4b3e64062afe7d13bdfd8308d6cbe304b81918f4486964b8d47\\\",\\n    \\\"readbackBeginning\\\": \\\"# Scoped history observations\\\\n\\\\n- Topic: cache subsystem. Workspace: `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06`. Recent window: `2026-10-09T00:00:00+03:00` through `2026-10-16T00:00:00+03:00`, exactly seven days. The first assistant response declared these before any tool or read.\\\\n- The requested installed `pstack-openai 0.1.0` path is missing. The inspected installed package identifies itself as `0.1.1`. Execution against freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` cannot be established. I\\\",\\n    \\\"missingLinks\\\": []\\n  },\\n  \\\"parsedEvidenceFiles\\\": [\\n    \\\"scoped-history.evidence/activity-variants.json\\\",\\n    \\\"scoped-history.evidence/assignments.json\\\",\\n    \\\"scoped-history.evidence/assignment-events.json\\\",\\n    \\\"scoped-history.evidence/history-A.json\\\",\\n    \\\"scoped-history.evidence/tool-returns.json\\\",\\n    \\\"scoped-history.evidence/source-assignments.json\\\",\\n    \\\"scoped-history.evidence/native-events.json\\\",\\n    \\\"scoped-history.evidence/history-B.json\\\",\\n    \\\"scoped-history.evidence/why-git.json\\\",\\n    \\\"scoped-history.evidence/why-supplied.json\\\",\\n    \\\"scoped-history.evidence/history-C.json\\\"\\n  ],\\n  \\\"sourcePreservation\\\": {\\n    \\\"argv\\\": [\\n      \\\"git\\\",\\n      \\\"diff\\\",\\n      \\\"--exit-code\\\",\\n      \\\"HEAD\\\",\\n      \\\"--\\\",\\n      \\\"supplied-history\\\",\\n      \\\"task-contract.json\\\"\\n    ],\\n    \\\"exitCode\\\": 0,\\n    \\\"stdout\\\": \\\"\\\",\\n    \\\"stderr\\\": \\\"\\\"\\n  },\\n  \\\"head\\\": {\\n    \\\"exitCode\\\": 0,\\n    \\\"stdout\\\": \\\"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\\\n\\\",\\n    \\\"stderr\\\": \\\"\\\"\\n  },\\n  \\\"status\\\": {\\n    \\\"exitCode\\\": 0,\\n    \\\"stdout\\\": \\\"?? scoped-history.evidence/\\\\n?? scoped-history.result.md\\\\n\\\",\\n    \\\"stderr\\\": \\\"\\\"\\n  }\\n}\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/why-git.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/why-git.json",
      "sha256": "78f47413b70139e07ba5e8901c0155ee78d8a205810edd6b342c01e8cb9afc1f",
      "bytes": 4060,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignmentId\": \"why-git\",\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"role\": \"why investigators\",\n  \"terminalStatus\": \"completed\",\n  \"scope\": \"Fixture Git tree and local Git history only\",\n  \"range\": {\n    \"start\": \"2026-10-09T00:00:00+03:00\",\n    \"end\": \"2026-10-16T00:00:00+03:00\"\n  },\n  \"findings\": [\n    {\n      \"claim\": \"HEAD matches assigned revision and branch is main.\",\n      \"evidence\": [\n        \"git-1\",\n        \"git-2\"\n      ]\n    },\n    {\n      \"claim\": \"No Git remotes are configured in this fixture.\",\n      \"evidence\": [\n        \"git-3\"\n      ]\n    },\n    {\n      \"claim\": \"Tracked fixture tree contains only supplied-history source files and task-contract.json. It contains no cache implementation.\",\n      \"evidence\": [\n        \"git-4\",\n        \"git-5\"\n      ]\n    },\n    {\n      \"claim\": \"No local cache-path commits are returned in the requested date range or across all local refs.\",\n      \"evidence\": [\n        \"git-6\",\n        \"git-7\"\n      ]\n    },\n    {\n      \"claim\": \"All-ref local history returns one seed-input commit dated 2026-10-16T11:44:51+03:00, after the requested range end.\",\n      \"evidence\": [\n        \"git-8\"\n      ]\n    }\n  ],\n  \"gaps\": [\n    \"Git evidence cannot establish any cache subsystem implementation state, code change, design rationale, or actual engineering outcome.\",\n    \"A missing cache path in the fixture is not evidence that the separately referenced cache workspace is absent or unchanged.\",\n    \"Supplied-history contents were not read by this source-scoped assignment; another investigator owns that source.\",\n    \"No adjacent workspace, real chat, network, gh, Git config mutation, or commits were accessed or performed.\"\n  ],\n  \"evidence\": [\n    {\n      \"id\": \"git-1\",\n      \"command\": [\n        \"git\",\n        \"rev-parse\",\n        \"HEAD\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-2\",\n      \"command\": [\n        \"git\",\n        \"branch\",\n        \"--show-current\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"main\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-3\",\n      \"command\": [\n        \"git\",\n        \"remote\",\n        \"-v\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-4\",\n      \"command\": [\n        \"git\",\n        \"ls-tree\",\n        \"-r\",\n        \"--name-only\",\n        \"HEAD\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"supplied-history/capsule.json\\nsupplied-history/history.json\\nsupplied-history/jay-mode.md\\nsupplied-history/shared-records.json\\ntask-contract.json\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-5\",\n      \"command\": [\n        \"git\",\n        \"ls-tree\",\n        \"HEAD\",\n        \"cache\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-6\",\n      \"command\": [\n        \"git\",\n        \"log\",\n        \"--all\",\n        \"--date=iso-strict\",\n        \"--format=%H %ad %s\",\n        \"--since=2026-10-09T00:00:00+03:00\",\n        \"--until=2026-10-16T00:00:00+03:00\",\n        \"--\",\n        \"cache\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-7\",\n      \"command\": [\n        \"git\",\n        \"log\",\n        \"--all\",\n        \"--date=iso-strict\",\n        \"--format=%H %ad %s\",\n        \"--\",\n        \"cache\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-8\",\n      \"command\": [\n        \"git\",\n        \"log\",\n        \"--all\",\n        \"--date=iso-strict\",\n        \"--format=%H %ad %s\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d 2026-10-16T11:44:51+03:00 Seed scoped history evaluation inputs\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"id\": \"git-9\",\n      \"command\": [\n        \"git\",\n        \"status\",\n        \"--short\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"?? scoped-history.evidence/\\n\",\n      \"stderr\": \"\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/why-supplied.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/why-supplied.json",
      "sha256": "eaa54321aeea480facf6abf40d11133967653c3e460131b68c2336298e8f878e",
      "bytes": 7483,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "{\n  \"assignment\": \"why-supplied\",\n  \"role\": \"why investigators\",\n  \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"scope\": {\n    \"source\": \"supplied-history/shared-records.json\",\n    \"sourceKind\": \"synthetic supplied long-form shared-record source\",\n    \"topic\": \"cache\",\n    \"requestedRange\": {\n      \"from\": \"2026-10-09T00:00:00+03:00\",\n      \"through\": \"2026-10-16T00:00:00+03:00\"\n    },\n    \"rangeVerification\": \"Unknown: supplied records contain relative ordering but no actual timestamps\",\n    \"revisionVerification\": \"Revision is assignment metadata; no Git artifacts inspected by this investigator\"\n  },\n  \"provenance\": {\n    \"claim\": \"Synthetic supplied records; no connector read occurred\",\n    \"liveTrackerRead\": false,\n    \"independentArtifactVerification\": false\n  },\n  \"findings\": [\n    {\n      \"id\": \"cache-current-narrative\",\n      \"finding\": \"The latest relative-order cache slice says the current caller still schedules disposal in a microtask.\",\n      \"status\": \"supplied narrative only; current implementation not independently verified\",\n      \"citations\": [\n        {\n          \"path\": \"supplied-history/shared-records.json\",\n          \"pointer\": \"/chatSlices/2\",\n          \"recordId\": \"fixture-chat-C\",\n          \"relativeOrder\": 3\n        }\n      ]\n    },\n    {\n      \"id\": \"cache-proposal-narrative\",\n      \"finding\": \"The earliest cache slice proposes deferred invalidation.\",\n      \"status\": \"proposal only; implementation and outcome unknown\",\n      \"citations\": [\n        {\n          \"path\": \"supplied-history/shared-records.json\",\n          \"pointer\": \"/chatSlices/0\",\n          \"recordId\": \"fixture-chat-A\",\n          \"relativeOrder\": 1\n        }\n      ]\n    },\n    {\n      \"id\": \"cache-revert-narrative\",\n      \"finding\": \"The second cache slice says a fix was shipped and then reverted, explicitly stating neither action was independently verified.\",\n      \"status\": \"unverified shipped/reverted narrative; failed behavior and reason for reversal unspecified\",\n      \"citations\": [\n        {\n          \"path\": \"supplied-history/shared-records.json\",\n          \"pointer\": \"/chatSlices/1\",\n          \"recordId\": \"fixture-chat-B\",\n          \"relativeOrder\": 2\n        }\n      ]\n    },\n    {\n      \"id\": \"cache-recurring-symptoms-unknown\",\n      \"finding\": \"The supplied cache slices do not describe concrete recurring user-visible symptoms, reproduction steps, error messages, frequency, or telemetry. Persistence of microtask disposal is a narrative statement about behavior, insufficient to establish a recurring failure or causal explanation.\",\n      \"status\": \"unknown\",\n      \"citations\": [\n        {\n          \"path\": \"supplied-history/shared-records.json\",\n          \"pointer\": \"/chatSlices\"\n        }\n      ]\n    }\n  ],\n  \"excluded\": [\n    {\n      \"sourcePointer\": \"/retryDecision\",\n      \"relevance\": \"unknown\",\n      \"reason\": \"No demonstrated connection to the cache subsystem. Retry threshold and synthetic ticket narrative are excluded from cache conclusions; telemetry is not supplied and chat is unavailable.\"\n    }\n  ],\n  \"gaps\": [\n    \"No actual timestamps, so inclusion within the requested date range cannot be verified.\",\n    \"No real record identifiers, retrieved UUID citations, commit SHAs, or current PR readback supplied.\",\n    \"No live tracker, connector, repository implementation, commit, revert artifact, or deployment evidence inspected.\",\n    \"The record does not establish that the shipped/reverted fix was the deferred-invalidation proposal.\",\n    \"No stated reason for the revert, demonstrated failed fix, or recurring symptom evidence.\",\n    \"The assignment revision is supplied metadata and not independently verified here.\"\n  ],\n  \"citations\": [\n    {\n      \"path\": \"supplied-history/shared-records.json\",\n      \"pointer\": \"/provenance\"\n    },\n    {\n      \"path\": \"supplied-history/shared-records.json\",\n      \"pointer\": \"/missing\"\n    },\n    {\n      \"path\": \"scoped-history.evidence/source-assignments.json\",\n      \"pointer\": \"/1\"\n    }\n  ],\n  \"actualToolReturns\": [\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"32bf4c\",\n      \"exit_code\": 1,\n      \"output\": \"ENOENT: no such file or directory, open 'source-assignments.json'\\n    path: \\\"source-assignments.json\\\",\\n syscall: \\\"open\\\",\\n   errno: -2,\\n    code: \\\"ENOENT\\\"\\n\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n      \"note\": \"Initial relative assignment path read failed before records were read.\"\n    },\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"711b88\",\n      \"exit_code\": 1,\n      \"output\": \"ENOENT: no such file or directory, open 'source-assignments.json'\\n    path: \\\"source-assignments.json\\\",\\n syscall: \\\"open\\\",\\n   errno: -2,\\n    code: \\\"ENOENT\\\"\\n\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n      \"note\": \"Explicit fixture workdir did not resolve the incorrect assignment path.\"\n    },\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"f67fee\",\n      \"exit_code\": 1,\n      \"output\": \"ENOENT: no such file or directory, open 'source-assignments.json'\\n    path: \\\"source-assignments.json\\\",\\n syscall: \\\"open\\\",\\n   errno: -2,\\n    code: \\\"ENOENT\\\"\\n\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n      \"note\": \"Disabling login shell did not resolve the incorrect assignment path.\"\n    },\n    {\n      \"tool\": \"exec_command\",\n      \"chunk_id\": \"477b4d\",\n      \"exit_code\": 0,\n      \"returnedAssignment\": {\n        \"id\": \"why-supplied\",\n        \"scope\": \"supplied-history/shared-records.json only, synthetic long-form shared-record source\",\n        \"inputRevision\": \"42fb97aed6a402f21cc42b220f1cdb8133cc326d\",\n        \"outputOwner\": \"why-supplied\",\n        \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/why-supplied.json\",\n        \"role\": \"why investigators\",\n        \"retryCount\": 0,\n        \"terminalStatus\": \"pending\",\n        \"evidenceLinks\": [\n          \"supplied-history/shared-records.json\"\n        ]\n      },\n      \"returnedRecords\": {\n        \"provenance\": \"Synthetic supplied records; no connector read occurred\",\n        \"retryDecision\": {\n          \"codeRecord\": \"Retry threshold changed from 2 to 3 in supplied narrative; no commit supplied\",\n          \"ticketRecord\": \"Fixture ticket requests three attempts for intermittent upstream failures\",\n          \"telemetry\": \"not supplied; no quantitative correlation can be claimed\",\n          \"chat\": \"unavailable\"\n        },\n        \"chatSlices\": [\n          {\n            \"id\": \"fixture-chat-A\",\n            \"relativeOrder\": 1,\n            \"topic\": \"cache\",\n            \"summary\": \"Proposed deferred invalidation\"\n          },\n          {\n            \"id\": \"fixture-chat-B\",\n            \"relativeOrder\": 2,\n            \"topic\": \"cache\",\n            \"summary\": \"Narrative says fix was shipped then reverted; neither action independently verified\"\n          },\n          {\n            \"id\": \"fixture-chat-C\",\n            \"relativeOrder\": 3,\n            \"topic\": \"cache\",\n            \"summary\": \"Current caller still schedules disposal in a microtask\"\n          }\n        ],\n        \"missing\": \"Real record identifiers, actual timestamps, commit SHAs and current PR readback. Do not convert these fixture ids to retrieved UUID citations.\"\n      },\n      \"note\": \"Successful read used corrected absolute assignment path provided by parent; return also included sibling assignment metadata, which was not used for findings.\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.result.md",
      "sha256": "bc68abb1274fa4b3e64062afe7d13bdfd8308d6cbe304b81918f4486964b8d47",
      "bytes": 11418,
      "owners": [
        "grades-native-rerun-06.json#0"
      ],
      "text": "# Scoped history observations\n\n- Topic: cache subsystem. Workspace: `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06`. Recent window: `2026-10-09T00:00:00+03:00` through `2026-10-16T00:00:00+03:00`, exactly seven days. The first assistant response declared these before any tool or read.\n- The requested installed `pstack-openai 0.1.0` path is missing. The inspected installed package identifies itself as `0.1.1`. Execution against freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` cannot be established. Its absence from this fixture's Git objects does not establish its absence elsewhere. The available version supplied reference instructions only.\n- Independently inspected fixture HEAD is `42fb97aed6a402f21cc42b220f1cdb8133cc326d`, branch `main`. The tracked tree has five input files, no cache implementation and no remote. These observations verify the fixture, not the cache change. See [actual returns](scoped-history.evidence/tool-returns.json) and [independent Git findings](scoped-history.evidence/why-git.json).\n- Supplied evidence supports a proposed invalidation change and records corrections to unsupported shipping claims. Actual cache state, shipping, reversion, PR status and seven-day chat coverage remain unknown. The capsule is partial. See [capsule](supplied-history/capsule.json), [digest](supplied-history/history.json) and [shared fixture record](supplied-history/shared-records.json).\n- The earlier scope-order failure remains preserved as user-reported prior-run context. Its original artifact was not supplied, so this run does not independently verify or erase it. No score or pass verdict is assigned here.\n\nThread statuses remain blocked by missing evidence:\n\n| Thread | Supported statement | Missing status evidence |\n| --- | --- | --- |\n| Invalidation proposal | `fixture-chat-A` describes proposed deferred invalidation; the capsule describes immediate deletion as a local proposal. | No implementation, accepted decision, cache branch or tests. Neither `[in flight <branch>]` nor `[verified, uncommitted]` is justified. |\n| Reported shipped/reverted fix | `fixture-chat-B` narrates shipping followed by reversion and explicitly says neither was independently verified. | No PR number or commits. Neither `[merged #N]` nor `[reverted #N]` is justified. |\n| Caller disposal timing | `fixture-chat-C` says the caller still schedules disposal in a microtask. This is a supplied statement. | Caller source is outside the permitted workspace. Current behavior cannot be independently checked. |\n\nNo permitted thread tag is supported. `[planned, not started]` would also assert an unobserved implementation status. Unknown threads remain explicit gaps rather than fabricated completions.\n\nRecurring problems supported by the supplied record:\n\n1. Shipping claims were repeated despite a correction to local-draft status. See `fixture-event-04`, `fixture-event-05`, `fixture-event-06` in [history.json](supplied-history/history.json).\n2. A shipped-then-reverted fix appears in the narrative, but its identity, cause and actual outcome are missing. See `fixture-chat-B` in [shared-records.json](supplied-history/shared-records.json).\n3. The capsule's immediate-deletion proposal and the caller's narrated microtask disposal leave teardown timing unresolved. The input does not establish that they refer to the same code revision.\n4. Missing timestamps, real UUIDs, full transcripts and live artifacts prevent a dated reconstruction and current status claims.\n\nThe next move is to supply a read-only evidence bundle inside this workspace containing the requested frozen skill, scoped timestamped transcripts and cache source with its recorded revision and current PR/ticket readbacks. This keeps the existing authorization boundary intact.\n\n## Variant results\n\nThese are separate evidence-limited responses to each declared variant. They are not fabricated executions of absent scenarios. Every recent variant retains the exact window above. The explicit all-history variant removes that date filter while retaining the same authorized input boundary.\n\n| Variant | Result from the authorized inputs |\n| --- | --- |\n| Complete state capsule | No complete capsule was supplied. `capsule.json` identifies itself as partial, has no base SHA and no cache branch. A genuinely complete capsule would skip history mining, while retaining the named-target shared-record sweep and independent current-state checks. That shortcut was not exercised as a successful complete-capsule run. |\n| No capsule | The separate digest-only response finds corrected local-draft claims in `fixture-event-04` through `fixture-event-06`. It cannot recover a branch, timestamps or implementation. Shared-record and current-state passes remain required for named cache recall, and were attempted within the supplied-source boundary. |\n| Three relevant chats | Three fresh-context investigators inspected A, B and C separately. Their schema includes topic, user goal, decisions, open threads, struggles/corrections, artifacts and citations with unknowns explicit. These are synthetic summaries, not retrieved chats. Real modification-time partitioning and date membership are unavailable; `relativeOrder` and filenames were not used as timestamps. See [A](scoped-history.evidence/history-A.json), [B](scoped-history.evidence/history-B.json), [C](scoped-history.evidence/history-C.json). |\n| Shipped then reverted | Retained as an unverified narrative in `fixture-chat-B`. The digest separately corrects unsupported shipping claims. Neither source establishes that shipping or reversion occurred. No invented revert number or completion tag. |\n| Unavailable error tracking | `history.json#/sourceAvailability/errorTracking` says unavailable. No error-tracker query was performed; this is not a searched-empty result. Current errors and recurrence rates remain unknown. |\n| Current PR contradicts history | No PR identifier or current readback was supplied; `livePr` is unavailable. This variant's actual PR comparison is blocked. An independently observed current status would take precedence for current status, with both sources retained, but no such observation occurred. The observed contradiction instead concerns the capsule's claim that the fixture is not an independent checkout: `git rev-parse --show-toplevel` and HEAD inspection establish this checkout. That does not substitute for PR evidence. |\n| Partial capsule | Used only for its covered proposal. Needed history was not skipped. Its `../cache/...` paths resolve outside the authorized root and were not followed. The missing branch/base/current-state evidence remains missing. |\n| Single-session pickup | Route to `session-pickup`. No specific real session ID or full transcript is supplied. `fixture-event-02` is a synthetic draft boundary, not a resumable host chat. No claim of recovered tools, files or actual prior actions. |\n| Pure activity recall | A separate digest-only pass omits the shared-record sweep. The supplied digest describes draft preparation, unsupported shipping claims and corrections. Its events cannot be assigned to the requested seven days. This result does not import the target-specific shared sweep. |\n| Explicit all-history | All authorized supplied digest events remain eligible, without a seven-day filter. Cache-relevant events 04, 05 and 06 repeat the shipping correction; the supplied A/B/C summaries remain synthetic and undated. All-history means the full authorized supplied set here, not authorization to search real or other-workspace history. Completeness remains unknown. |\n| Habits / human-readable summary | Habits route to `automate-me`; a human-readable work summary is a separate output from working-context Recall. `jay-mode.md` labels its preferences synthetic, so no personal baseline acceptance is inferred and no durable skill was changed. |\n\n## Sources and current-state limits\n\n| Evidence category | Observation and limits |\n| --- | --- |\n| Source control | Independent local fixture Git inspection succeeded. Cache-path searches returned empty in this fixture. The only commit is the seed input at `2026-10-16T11:44:51+03:00`, after the recent window. No cache commit, remote, PR or code anchor was found. This says nothing about another repository. |\n| Issue / ticket tracker | No authorized live target or readback. `retryDecision.ticketRecord` is a synthetic narrative without a ticket ID; its connection to cache is unestablished and it is excluded from cache findings. |\n| Long-form shared documents | An independent investigator inspected the supplied `shared-records.json`. This local fixture source is available. No real document service was searched. |\n| Real-time team chat | Only supplied summaries/digest are authorized. No real chat read was attempted. Full transcripts and UUIDs are unavailable. |\n| Infrastructure observability | No authorized supplied logs or metrics; no query performed. |\n| Error / exception tracking | Explicitly unavailable in the supplied source. No query performed. |\n| Product analytics | No supplied telemetry or authorized query target; no quantitative correlation claimed. |\n\nExposed service tools are not authorization to read the user's actual accounts. Metadata inspection did not invoke those services. Unavailable, unauthorized, failed and searched-empty sources are distinct above. In particular, a successful empty local Git search does not make live PR or error-tracker access searched-empty.\n\n## Native host method and evidence\n\nThe current host executed actual local commands and fresh-context worker calls. Requested model policy was `inherit-parent`; actual models were not exposed by the worker returns and remain unknown. Worker identities establish separate contexts, not model diversity. These are not sequential passes represented as parallel workers.\n\nImmutable assignments precede dispatch in [assignments.json](scoped-history.evidence/assignments.json) and [source-assignments.json](scoped-history.evidence/source-assignments.json). Activity variant scope was declared in its fresh-context dispatch. Workers own distinct output paths. The parent inspected result bytes and input revisions before integration. Execution events and captured native returns are stored in the evidence directory. The method used synthetic-ID partitions because real chat timestamps were absent; it cannot satisfy timestamp-based mining or full-transcript inspection.\n\nThe three chat tasks were dispatched before collection, and local source inspection ran while workers were active. Independent shared-source tasks were dispatched afterward. The full requested concurrent source-and-chat investigator roster was not achieved; unavailable live sources had no investigator. The parent had already read the supplied digest and summaries before worker partitioning. Those files were the entire supplied excerpts, not raw host transcripts, and no full-transcript privacy or coverage claim is made.\n\nNo real history, other-workspace cache source, live PR/ticket state, external service action, installation, configuration, schedule, commit or push was performed. The external action `fixture-verdict-post-1` has unknown outcome and explicit `authorizationToReplay: false`; it was not replayed. Only task-owned reports and evidence were written. Input preservation and report readback are checked in the saved verification returns.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-11/scoped-history/input",
      "owner": "grades-native-11.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/scoped-history/source-reads.json",
      "owner": "grades-native-11.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/scoped-history/input",
      "owner": "grades-native-11.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/scoped-history/source-reads.json",
      "owner": "grades-native-11.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-06/scoped-history.evidence/tool-returns.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-06/scoped-history.evidence/tool-returns.json",
      "sha256": "c478051a6e3bcf2186ebc5734f1d21bddc07d07ee9f0d5cb4924b466b961181e",
      "bytes": 83713,
      "owner": "grades-native-rerun-06.json#0",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
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
