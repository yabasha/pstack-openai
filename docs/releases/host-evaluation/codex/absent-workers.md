# codex: absent-workers

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "absent-workers",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-durable-00.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "No independent worker operation is available.",
  "caseDefinition": {
    "id": "absent-workers",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "No independent worker operation is available.",
    "requirements": [
      "Record unavailable workers; use authorized sequential work only.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "A discovered spawn operation and result inspection support independent workers after capability becomes available.",
    "expectedReduced": "Complete authorized sequential work and label it reduced-pass; report absent workers.",
    "expectedBlocked": "Workers are required and unavailable; record blocked without launching invented operations.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "absent-workers",
    "caseFile": "docs/parity/cases/contracts.json",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
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
        "spawn",
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
      "attemptId": "grades-native-06.json#2",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "absent-workers",
      "status": "reduced-pass",
      "grade": {
        "caseId": "absent-workers",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "sequential",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_15"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Case condition simulated; independent method intentionally unexercised.",
          "No concrete program/task Git revision; helper dependency gate fails."
        ],
        "review": "Treats worker absence as case-local simulated restriction and completes sequential source-guided handoff. Explicitly recognizes exposed worker operations and successful fresh workers elsewhere; initial inherited-context rollout error is not tool absence.",
        "responseArtifact": "fixtures/batch-06/absent-workers.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "A discovered spawn operation and result inspection support independent workers after capability becomes available.",
        "reducedExpected": "Complete authorized sequential work and label it reduced-pass; report absent workers.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-06.json",
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
        "text": "# absent-workers\n\n## Supplied input\n\n> No independent worker operation is available.\n\nNamed source files and exact copied source bytes are retained in [absent-workers/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-manifest.json) and [absent-workers/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response\n\nTreat the case condition as a restriction and use sequential inspection only for this case. No independent worker was dispatched for absent-workers. Available source contracts were read in full. No concrete program scope, units, real repository, exact input commit or merge authorization is supplied. Independent review and standing program behavior cannot be established under this variant.\n\n## Capability condition\n\nThe negative condition is simulated, not host enforced. collaboration.spawn_agent is exposed, and other cases observed successful fresh worker identities. One inherited-context launch failed with invalid thread-store/no rollout, followed by successful fork_turns none launches. That failure does not prove all workers unavailable. No false unavailable-host claim is made.\n\n## Exact input and permissions\n\nThe exact supplied input is quoted above and its SHA256 is in input.json. Package revision is the supplied freeze, with installed byte manifest and unverified commit correspondence. Task repository SHA is unavailable because no repository exists. Reads, case report writes and local Bun execution are allowed. This case exercised reads and durable local report write/readback only. All external actions remain forbidden.\n\n## Sequential outcome and limits\n\nAuthorized sequential work inspected orchestrate, mode and complete worker prompt and produced this scoped handoff. No independent worker, spawn, follow-up, wait, stop, model diversity, unattended loop, orch initialization or program completion is claimed for this case. Helpers are not worker operations. Dependency-backed helper execution is blocked by the actually observed missing commander package in additional-command-results.json; no installation occurred. Required orchestration independence remains unmet.\n",
        "artifact": {
          "path": "fixtures/batch-06/absent-workers.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers.result.md",
          "sha256": "808dd7a257cf49bfcd37ce3140fe339a3be720dc154e0a35304a0d189f12287f",
          "bytes": 3875
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-06.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-06.events.jsonl",
            "sha256": "29e250d426d7f6e1853f71ccc210620bd85774dbbfaa2645ed41e80fe5d27d0b",
            "bytes": 497874,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "47752e596478dfe15ca960f407621e4b414297317af6fa359ed92ee8b7fbf796"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f92e8885378702b4bd7f8c8923b9d86fe857b3100ddd122500e258c0eea90617",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "042fee062c81f8755873d67b8dc68300f076a102d5f4f590ff813784dae9972f"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7e254c6cdfabf60dde410229ad5c7c86da809b98a5d60bd1c1e8a1c6a6fd0185",
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
            "item_7",
            "item_15"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-06.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    },
    {
      "attemptId": "grades-native-durable-00.json#0",
      "order": 200,
      "gradeFile": "grades-native-durable-00.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "absent-workers",
      "status": "pass",
      "grade": {
        "caseId": "absent-workers",
        "host": "codex",
        "status": "pass",
        "execution": "workers",
        "rawTrace": "codex/durable-00.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_6",
          "item_7",
          "item_10",
          "item_11"
        ],
        "actualExecutionEventIds": [
          "item_48",
          "item_50",
          "item_68",
          "item_70",
          "item_71"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [],
        "review": "Separate capability-available variant actually spawns a read-only worker at verified taskSHA and inspects its completed invoice path response against source. Earlier unavailable-worker baseline remains historical. Native activity metadata supports observed worker model separately from request; actual compiler check is bounded. Late checklist/assignment-placeholder/trail repairs remain deviations, not invented proof.",
        "responseArtifact": "fixtures/durable-00/absent-workers/absent-workers.result.md",
        "variantReview": [
          "Actual case-owned source/artifacts and native trace reviewed; conditional withholding is simulation unless a concrete host error is preserved.",
          "No schema-validator, bookkeeping label, compiler version, or verification script selfgrade is accepted as workflow success."
        ],
        "limits": [
          "Actual extra memory-registry read occurred at root item8; no unrelated memory content is relied upon or projected.",
          "Late checklist recording, logical owner placeholder before native binding, encrypted spawn payload and unreviewed audit-time trail repair limits retained."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "evidence": [
          "fixtures/durable-00/absent-workers/evidence/native-calls-and-returns.json",
          "fixtures/durable-00/absent-workers/evidence/trace-native-identity.json",
          "fixtures/durable-00/absent-workers/evidence/compiler-noemit.json"
        ],
        "fullExpected": "A discovered spawn operation and result inspection support independent workers after capability becomes available."
      },
      "topLevelContext": {
        "attempt": "durable-00",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Full/reduced results derive from actual worker artifacts, raw current/child transcripts and native activity metadata, not helper/script selfgrades.",
          "Root item8 reads a memory registry beyond needed fixture scope; no such unrelated personal contents are reused in this grade/report.",
          "Permission and independence are not conflated with model diversity or permanent process termination."
        ]
      },
      "response": {
        "text": "# absent-workers actual durable-host result\n\nThis file records observations and limits. It assigns no case grade.\n\n## Supplied input and workflow\n\nThe exact supplied group input is in supplied-input.json and evidence/current-transcript.jsonl. This includes the case contract, taskPayload, sourceFiles, baseline and every variant. The immutable task-input revision was independently verified as 7b1fcb74b4a5ed3fcadc979da831aa98a621d236. The installed package is 0.1.0 at source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, a distinct revision. All seven requested exact source paths were read through actual command tools and copied under sources/. source-manifest.json records their digests. evidence/source-freeze-comparison.json records byte-for-byte comparisons against the source freeze, all matching with Git exit 0. No package update occurred.\n\npermissions.json retains the current explicit grant for isolated native delegation, scoped writes, persistence and local execution. No external services, commits, installations, configuration, schedules, messages, posts, pushes or publishing are authorized. Source scenario narratives grant none.\n\nOrchestrate small-task collapse uses bounded direct foreground coordination with native workers, not its fleet helper. workflow-checklist.md retains exact selected steps and skipped dispositions. The verbatim checklist was copied after execution, a retained sequencing deviation; the initial throughput checkpoint preceded native dispatch. The root throughput-checkpoint.md records blocking prerequisites, disjoint workstreams, single-writer state and decomposition. Applicable principle Separate Before Serializing Shared State changed ownership to distinct files before spawn. Prove It Works changed verification to source and artifact inspection plus actual Bun execution. Installed 0.1.0 Unslop and Technical Writing shaped the report. Missing cursor-team-kit companions were not run. No missing dependency was installed.\n\n## Actual response and every variant\n\nThe capability-change variant dispatched /root/invoice_trace through collaboration.spawn_agent. Native result inspection reported completed and the returned source trace matched assignment absent-workers/trace, input SHA and HEAD. The controller returns the arithmetic total through controller line 4, facade line 3, adapter line 2 and calculate line 1 in committed-inputs/invoice.mjs. format line 5 is outside that call chain. The coordinator independently ran exact committed bytes and observed total 11, exit 0.\n\nThe earlier no-worker scenario is retained in baseline.md with supplied batch-06 active-or-not-yet-finished and grade null. Its original raw evidence was not supplied in this root. It has not been regraded. The authorized sequential check in this run is an independent coordinator inspection of the new native result, not evidence that the earlier worker trial succeeded. If substituted for workers it would be reduced capability.\n\nArtifacts. assignments/trace.json, evidence/trace-actual-dispatch.json, evidence/trace-native-identity.json, evidence/trace-worker-transcript.jsonl, evidence/trace-returned-messages.json, evidence/coordinator-independent-invoice-probe.json, outputs/coordinator-inspection.md.\n\nCompiler proof. The already installed TypeScript 5.9.3 compiler actually ran through Bun with --noEmit --allowJs --checkJs --target es2023 committed-inputs/invoice.mjs and exited 0 with empty stdout and stderr. evidence/compiler-noemit.json contains exact argv and outputs. This bounded compiler check proves no general input validation or worker capability.\n\n## Native tools, raw outputs and ordering\n\nNative tools were collaboration.spawn_agent, collaboration.list_agents and, for controlled stop cases, collaboration.interrupt_agent. Discovery included the actual collaboration namespace outside ALL_TOOLS. functions.exec with tools.exec_command and tools.apply_patch provided read, execution and authorized persistence. Exact native call objects, call IDs, arguments and corresponding unmodified returned objects are retained in evidence/native-calls-and-returns.json. Returns were captured during this run, with earlier live snapshots preserved. Root and assigned-worker transcripts preserve actual commands, stdout, stderr, exit status and results. Some host-stored spawn message strings are encrypted; the raw ciphertext is retained without claiming a plaintext history audit of those encrypted fields. Full readable immutable role briefs are in assignments/, and the complete supplied role prompt is in sources/references/agent-prompts/poteto-agent.md. Workers confirmed reading their briefs and the exact installed mode.\n\nObserved worker model and effort are gpt-6.1-sol and medium, from native SubAgentActivity metadata in evidence/*-native-identity.json. Spawn return alone did not expose this. Original worker reports left them unknown; those raw reports remain unchanged and the later coordinator observation is recorded separately. Requested policy was inherit-parent. These six workers provide no model diversity.\n\nNo claims derive from a case definition, fixture test, expectedFull string, bookkeeping label or compiler exit alone. No synthetic telemetry or external service counts are recorded. Results are bounded to this actual run and exact inputs. Prior unavailable raw trials were not accessible here.\n\n## Trail and persistence\n\nThe decision trail is decisions.tsv, created through the exact installed show-me-your-work/scripts/log.sh helper, executed via Bun orchestration of bash, with output and exit status captured. Only this run and its assigned workers were read. Transcript audit is limited by encrypted spawn-message fields and absent earlier-trial raw history. No unrelated private chat was searched. Durable source, assignment, raw return and result files were written within the authorized root and read back. Local persistence does not establish crash durability, automatic recovery or unattended continuity.\n\n## Attention\n\nreviewed by gpt-5.6-sol\n\nThe independent gpt-5.6-sol reviewer inspected the original trails, transcripts and artifacts. The unmodified review is evidence/trail-review-original.md. Native model observation is evidence/trail-review-native-identity.json. Review findings and the root response are in evidence/review-response.md. Missing decision and lifecycle entries were appended during audit with existing evidence pointers; the entries expressly do not claim new worker actions. Current trail readback is evidence/final-trail-readback.json, and earlier readbacks remain historical snapshots. No independent re-review of these local repairs is claimed.\n\nRemaining flags. Exact plaintext spawn equality is unobservable in encrypted host history. Full readable immutable assignment components are retained in evidence/*-full-readable-assignment.md. The pre-dispatch immutable outputOwner fields are placeholders; actual native owners were bound on spawn, after path separation and before the worker writes visible in the transcripts. The verbatim checklist was recorded late. Worker A read Investigation and How after its probe. Native interrupt exposes stopped turns as interrupted, not literal cancelled or process teardown. Unknown side-effect completion blocks replay. Earlier raw unavailable-trial evidence was not supplied. No self-grade is assigned.\n",
        "artifact": {
          "path": "fixtures/durable-00/absent-workers/absent-workers.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/absent-workers.result.md",
          "sha256": "c13a509d83d2291c1b484236c228604d7a43e29acd448865fb6698662278a798",
          "bytes": 7357
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/durable-00.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/durable-00.events.jsonl",
            "sha256": "1cdf426e1c8d97876acb0dbef1a052d411b2d6938c952319c52982eed31475c4",
            "bytes": 488050,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ba63417967432af0873229300aef4c664b519c898c793db10d7b99b5c8d1901a"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f1c9ee8c22b55352bad621df92d8d5974edca919c9cecf0203c4c58e4b4bba61",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d931ac5de83b01d5001caa72a076d687088a5cd9e7c8706d4d957d7bf7e5c6fb"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "32bf0139e83a388459054da8064ae19a34e9bbb57378acc8e69627c9002bf6d2",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f5f3c682ac588d153c816bf3191ee602a6ba9a6932a0f7d7b542ba1a0759dad8"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6d1a045dd970c3c87639b5a798584b9e8c0051300c3f317fd1b41df3acb8ecc2",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4eaca67f9a10d7fd9f00ddcbf00ab72dd014ab49ed67263496ae0ac3faedea6e"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7166dc01b4d95507739d915770e6ff56de29e8aaa1dfad4f4221d56afe4b0cc9",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ee57c7b345a5ce4a3b02c75ff5a2155874c853281814a4836709380430cdddaa"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "413427d2de5fa7958fc3650c637937e2f3143ad85af41254df4872e5c6d7303c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_48",
                "line": 91,
                "type": "item.started",
                "itemType": "file_change",
                "recordSha256": "ee2b3d890dd789b8a284f232fb08abb0ca1fe924d45ce943c2566bfaae7d4266"
              },
              {
                "eventId": "item_48",
                "line": 92,
                "type": "item.completed",
                "itemType": "file_change",
                "recordSha256": "5c12f6e21a884d94cb13d0c777d2e0597da7dfa8c59ea863fc36dec385bda0d3"
              },
              {
                "eventId": "item_50",
                "line": 95,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a908829748a3281d7589fabcf93e2d9da62ae33a3f1a59a496fe8a3378cca5e8"
              },
              {
                "eventId": "item_50",
                "line": 96,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "9f8eb5997a754785b49da563dd51fa029140a0c076c8c8edf2427f9f2db9dcc8",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_68",
                "line": 129,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "704891cccd6336c5f4080a630535777ac6d869764ee72e013599d7b3dec721c1"
              },
              {
                "eventId": "item_68",
                "line": 130,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8cd7abeb2f00c805a806a894df0526948e4a40b2d54883b698d302b3b60fc3f5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_70",
                "line": 133,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ecbdd3c4968a1781fa5af89a16641c78f0d5b6979a60f7b4f80ca1b4ea9ad38b"
              },
              {
                "eventId": "item_70",
                "line": 134,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c15e88182c6320b2d31be75f12560b318be36f1bf3cc8a060aa59884f0af11ac",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_71",
                "line": 135,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "39295e174f66ac874e62b3d5affd9ee3b90d0ffe0ce94f7c10c3cf9a281a004a"
              },
              {
                "eventId": "item_71",
                "line": 136,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "cba81df5a47197324bac27c94e69a44c79e4bd9249d226ae402b33649b65a0ed",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/durable-00/absent-workers/evidence/native-calls-and-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/native-calls-and-returns.json",
            "sha256": "aad99d21a35c078c7a0e4b11fd24ee4722e919de85714cb6435d0504b941efe4",
            "bytes": 55478
          },
          {
            "path": "fixtures/durable-00/absent-workers/evidence/trace-native-identity.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-native-identity.json",
            "sha256": "70e2bb2a3ecbafcdc87593bdda83f952ee7d788170d5bb0dc67d6a82f65be335",
            "bytes": 627
          },
          {
            "path": "fixtures/durable-00/absent-workers/evidence/compiler-noemit.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/compiler-noemit.json",
            "sha256": "274c1e93187a7798b29ed348e0de0aeb1f24e23db43f8708cfe85b7503b17788",
            "bytes": 293
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_6",
            "item_7",
            "item_10",
            "item_11"
          ],
          "actualExecutionEventIds": [
            "item_48",
            "item_50",
            "item_68",
            "item_70",
            "item_71"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/absent-workers.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers.result.md",
      "sha256": "808dd7a257cf49bfcd37ce3140fe339a3be720dc154e0a35304a0d189f12287f",
      "bytes": 3875,
      "owners": [
        "grades-native-06.json#2"
      ],
      "text": "# absent-workers\n\n## Supplied input\n\n> No independent worker operation is available.\n\nNamed source files and exact copied source bytes are retained in [absent-workers/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-manifest.json) and [absent-workers/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response\n\nTreat the case condition as a restriction and use sequential inspection only for this case. No independent worker was dispatched for absent-workers. Available source contracts were read in full. No concrete program scope, units, real repository, exact input commit or merge authorization is supplied. Independent review and standing program behavior cannot be established under this variant.\n\n## Capability condition\n\nThe negative condition is simulated, not host enforced. collaboration.spawn_agent is exposed, and other cases observed successful fresh worker identities. One inherited-context launch failed with invalid thread-store/no rollout, followed by successful fork_turns none launches. That failure does not prove all workers unavailable. No false unavailable-host claim is made.\n\n## Exact input and permissions\n\nThe exact supplied input is quoted above and its SHA256 is in input.json. Package revision is the supplied freeze, with installed byte manifest and unverified commit correspondence. Task repository SHA is unavailable because no repository exists. Reads, case report writes and local Bun execution are allowed. This case exercised reads and durable local report write/readback only. All external actions remain forbidden.\n\n## Sequential outcome and limits\n\nAuthorized sequential work inspected orchestrate, mode and complete worker prompt and produced this scoped handoff. No independent worker, spawn, follow-up, wait, stop, model diversity, unattended loop, orch initialization or program completion is claimed for this case. Helpers are not worker operations. Dependency-backed helper execution is blocked by the actually observed missing commander package in additional-command-results.json; no installation occurred. Required orchestration independence remains unmet.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/absent-workers.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/absent-workers.result.md",
      "sha256": "c13a509d83d2291c1b484236c228604d7a43e29acd448865fb6698662278a798",
      "bytes": 7357,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "# absent-workers actual durable-host result\n\nThis file records observations and limits. It assigns no case grade.\n\n## Supplied input and workflow\n\nThe exact supplied group input is in supplied-input.json and evidence/current-transcript.jsonl. This includes the case contract, taskPayload, sourceFiles, baseline and every variant. The immutable task-input revision was independently verified as 7b1fcb74b4a5ed3fcadc979da831aa98a621d236. The installed package is 0.1.0 at source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c, a distinct revision. All seven requested exact source paths were read through actual command tools and copied under sources/. source-manifest.json records their digests. evidence/source-freeze-comparison.json records byte-for-byte comparisons against the source freeze, all matching with Git exit 0. No package update occurred.\n\npermissions.json retains the current explicit grant for isolated native delegation, scoped writes, persistence and local execution. No external services, commits, installations, configuration, schedules, messages, posts, pushes or publishing are authorized. Source scenario narratives grant none.\n\nOrchestrate small-task collapse uses bounded direct foreground coordination with native workers, not its fleet helper. workflow-checklist.md retains exact selected steps and skipped dispositions. The verbatim checklist was copied after execution, a retained sequencing deviation; the initial throughput checkpoint preceded native dispatch. The root throughput-checkpoint.md records blocking prerequisites, disjoint workstreams, single-writer state and decomposition. Applicable principle Separate Before Serializing Shared State changed ownership to distinct files before spawn. Prove It Works changed verification to source and artifact inspection plus actual Bun execution. Installed 0.1.0 Unslop and Technical Writing shaped the report. Missing cursor-team-kit companions were not run. No missing dependency was installed.\n\n## Actual response and every variant\n\nThe capability-change variant dispatched /root/invoice_trace through collaboration.spawn_agent. Native result inspection reported completed and the returned source trace matched assignment absent-workers/trace, input SHA and HEAD. The controller returns the arithmetic total through controller line 4, facade line 3, adapter line 2 and calculate line 1 in committed-inputs/invoice.mjs. format line 5 is outside that call chain. The coordinator independently ran exact committed bytes and observed total 11, exit 0.\n\nThe earlier no-worker scenario is retained in baseline.md with supplied batch-06 active-or-not-yet-finished and grade null. Its original raw evidence was not supplied in this root. It has not been regraded. The authorized sequential check in this run is an independent coordinator inspection of the new native result, not evidence that the earlier worker trial succeeded. If substituted for workers it would be reduced capability.\n\nArtifacts. assignments/trace.json, evidence/trace-actual-dispatch.json, evidence/trace-native-identity.json, evidence/trace-worker-transcript.jsonl, evidence/trace-returned-messages.json, evidence/coordinator-independent-invoice-probe.json, outputs/coordinator-inspection.md.\n\nCompiler proof. The already installed TypeScript 5.9.3 compiler actually ran through Bun with --noEmit --allowJs --checkJs --target es2023 committed-inputs/invoice.mjs and exited 0 with empty stdout and stderr. evidence/compiler-noemit.json contains exact argv and outputs. This bounded compiler check proves no general input validation or worker capability.\n\n## Native tools, raw outputs and ordering\n\nNative tools were collaboration.spawn_agent, collaboration.list_agents and, for controlled stop cases, collaboration.interrupt_agent. Discovery included the actual collaboration namespace outside ALL_TOOLS. functions.exec with tools.exec_command and tools.apply_patch provided read, execution and authorized persistence. Exact native call objects, call IDs, arguments and corresponding unmodified returned objects are retained in evidence/native-calls-and-returns.json. Returns were captured during this run, with earlier live snapshots preserved. Root and assigned-worker transcripts preserve actual commands, stdout, stderr, exit status and results. Some host-stored spawn message strings are encrypted; the raw ciphertext is retained without claiming a plaintext history audit of those encrypted fields. Full readable immutable role briefs are in assignments/, and the complete supplied role prompt is in sources/references/agent-prompts/poteto-agent.md. Workers confirmed reading their briefs and the exact installed mode.\n\nObserved worker model and effort are gpt-6.1-sol and medium, from native SubAgentActivity metadata in evidence/*-native-identity.json. Spawn return alone did not expose this. Original worker reports left them unknown; those raw reports remain unchanged and the later coordinator observation is recorded separately. Requested policy was inherit-parent. These six workers provide no model diversity.\n\nNo claims derive from a case definition, fixture test, expectedFull string, bookkeeping label or compiler exit alone. No synthetic telemetry or external service counts are recorded. Results are bounded to this actual run and exact inputs. Prior unavailable raw trials were not accessible here.\n\n## Trail and persistence\n\nThe decision trail is decisions.tsv, created through the exact installed show-me-your-work/scripts/log.sh helper, executed via Bun orchestration of bash, with output and exit status captured. Only this run and its assigned workers were read. Transcript audit is limited by encrypted spawn-message fields and absent earlier-trial raw history. No unrelated private chat was searched. Durable source, assignment, raw return and result files were written within the authorized root and read back. Local persistence does not establish crash durability, automatic recovery or unattended continuity.\n\n## Attention\n\nreviewed by gpt-5.6-sol\n\nThe independent gpt-5.6-sol reviewer inspected the original trails, transcripts and artifacts. The unmodified review is evidence/trail-review-original.md. Native model observation is evidence/trail-review-native-identity.json. Review findings and the root response are in evidence/review-response.md. Missing decision and lifecycle entries were appended during audit with existing evidence pointers; the entries expressly do not claim new worker actions. Current trail readback is evidence/final-trail-readback.json, and earlier readbacks remain historical snapshots. No independent re-review of these local repairs is claimed.\n\nRemaining flags. Exact plaintext spawn equality is unobservable in encrypted host history. Full readable immutable assignment components are retained in evidence/*-full-readable-assignment.md. The pre-dispatch immutable outputOwner fields are placeholders; actual native owners were bound on spawn, after path separation and before the worker writes visible in the transcripts. The verbatim checklist was recorded late. Worker A read Investigation and How after its probe. Native interrupt exposes stopped turns as interrupted, not literal cancelled or process teardown. Unknown side-effect completion blocks replay. Earlier raw unavailable-trial evidence was not supplied. No self-grade is assigned.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/artifact-paths.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/artifact-paths.json",
      "sha256": "83f311b87fdcca65a6a169c9bb4e824834a663d02d2964ed868f6db5291198b2",
      "bytes": 14375,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/source-manifest.json\",\n    \"bytes\": 1606,\n    \"sha256\": \"12e2ac43a57fce00e11af38dec98c53d1099a07dc7b40b8a913c8ad5c4a3db91\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/permissions.json\",\n    \"bytes\": 511,\n    \"sha256\": \"2e64c5f79500558c17a65539f91d559ca3ffc1c5b3f0f6138f8de72c48641f28\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/workflow-checklist.md\",\n    \"bytes\": 3653,\n    \"sha256\": \"1e157e1ff64f052949a72e17685f9be50b32945ff093289b420f60eba7c7d16b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/assignments/trace.json\",\n    \"bytes\": 1537,\n    \"sha256\": \"dce24d4ab6b25a209d4b4e342885f8cf0a32caea2cbcec127ca0d1e9f4bc0ead\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-native-identity.json\",\n    \"bytes\": 629,\n    \"sha256\": \"35f11570ce3c68bdcdcad31768ca416bddf10114bf64b6dbbd9ae4165f16fd50\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/observed-worker-metadata.json\",\n    \"bytes\": 4036,\n    \"sha256\": \"d603d3ffa271b25e9699a2432638c6df89a791f5b21217246bb7bf9b42d31c04\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/native-calls-and-returns.json\",\n    \"bytes\": 55478,\n    \"sha256\": \"aad99d21a35c078c7a0e4b11fd24ee4722e919de85714cb6435d0504b941efe4\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/source-freeze-comparison.json\",\n    \"bytes\": 850,\n    \"sha256\": \"7713aa5795e838435793e62d6a55af9b404a6ec1401645e44b8f1496ed45548b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-4.json\",\n    \"bytes\": 577,\n    \"sha256\": \"101d837dbfe1610becd69266ba0762ccfbe1202998db2340d95763ae73639a9c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-worker-transcript.jsonl\",\n    \"bytes\": 462894,\n    \"sha256\": \"d3438e052c2f49240339fc957e21160d2c06d02655abb7db4dddfcffee00de63\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-returned-messages.json\",\n    \"bytes\": 6503,\n    \"sha256\": \"1ca7081644da4b8dd8a9f25c4177c9dcc60eea2b7f033c7c15bfb107be511da2\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-trail-readback.json\",\n    \"bytes\": 2303,\n    \"sha256\": \"28bd2328987452923378cb5e43d5e61855a5df1137428c801827964df881b07a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-original.md\",\n    \"bytes\": 14564,\n    \"sha256\": \"c7d9fd6d1323a14a52b90834a910b9d0afc8a41acb8c3c59129c2aee26edc8ef\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-head.json\",\n    \"bytes\": 150,\n    \"sha256\": \"07f9a2720ef5aa1a89e2c68d23f0202a2f11fe51765a0c2347db33899f6fe13c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/compiler-noemit.json\",\n    \"bytes\": 293,\n    \"sha256\": \"274c1e93187a7798b29ed348e0de0aeb1f24e23db43f8708cfe85b7503b17788\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-tracked-diff.json\",\n    \"bytes\": 158,\n    \"sha256\": \"880e428b992afb471bdb448a74396ac70977d15dec34c27457d5959a0e287890\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-3.json\",\n    \"bytes\": 587,\n    \"sha256\": \"c00a88d256502ac2f171dea77fee0811eb95d857436dfed1b7a6c43872430416\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-readback-after-audit.json\",\n    \"bytes\": 1970,\n    \"sha256\": \"a068857058aef405b55a52197329f7ad924c6ce9d043614554e89cce8eef0630\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-close.json\",\n    \"bytes\": 756,\n    \"sha256\": \"76b8eed4efb2542ccfa18570a7261555444ad440cd5b9309098c89bd3753b8cd\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-actual-dispatch.json\",\n    \"bytes\": 5655,\n    \"sha256\": \"bb88bdbec70ec1f260746f76c3608598f2290c081000a0b367d75c143b95ae3c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/current-transcript.jsonl\",\n    \"bytes\": 1574291,\n    \"sha256\": \"0d9275227a0b714de9c57243fb7457ecdbb4ab53d4a69fa2dfa0867715276f50\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-2.json\",\n    \"bytes\": 591,\n    \"sha256\": \"b584d4b52ccfef9f1eabac764b276d989183ac4cfa285e569af1dfe8f1c8788f\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-spawn-return.json\",\n    \"bytes\": 41,\n    \"sha256\": \"b8c66d035fe94e311811aeb8e7fc09860c6a4a466a9d10f40797927badbad7ee\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-1.json\",\n    \"bytes\": 571,\n    \"sha256\": \"21905b4cfa7aca50be3757e670793a0d537cd59500f17e94c3bad2aae77c473d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/compiler.json\",\n    \"bytes\": 209,\n    \"sha256\": \"65d9dd78e1c8992fcd22f5fd2ace51bfd504916ca43a0ac1b07894f617876c89\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-trail-audit.json\",\n    \"bytes\": 1661,\n    \"sha256\": \"f40f57adb16a1577d127848e4919dcc5bfbd1f635ed9ac1acaf3c998ef01a7b2\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/live-transcript-2.jsonl\",\n    \"bytes\": 909368,\n    \"sha256\": \"3f1703e6adeefaa1db660270cbdf180630e186ece62cab107f960525b896bc01\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-native-identity.json\",\n    \"bytes\": 627,\n    \"sha256\": \"70e2bb2a3ecbafcdc87593bdda83f952ee7d788170d5bb0dc67d6a82f65be335\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-full-readable-assignment.md\",\n    \"bytes\": 3476,\n    \"sha256\": \"a9e2b8b5568f166cef13a1085a3172f8aa7426d56729d0954727fa0faa0392e7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-readback.json\",\n    \"bytes\": 497,\n    \"sha256\": \"1db32025bdfe7fb414ecc86029171ff29edba209b48fd08fc679ccc6d125e39b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/revision.json\",\n    \"bytes\": 150,\n    \"sha256\": \"07f9a2720ef5aa1a89e2c68d23f0202a2f11fe51765a0c2347db33899f6fe13c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/coordinator-independent-invoice-probe.json\",\n    \"bytes\": 550,\n    \"sha256\": \"1a4fc52950b7ea6dbf1ccea2ce298a73f948129276e4e6569c92841986d70f0a\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/review-response.md\",\n    \"bytes\": 1370,\n    \"sha256\": \"06e97d34429d3ad72cae89acf0581bbcecb40fcb7c94f07cf2533a44a6a59afb\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/worker-metadata.json\",\n    \"bytes\": 10094,\n    \"sha256\": \"45eb58df4beb8f2dd8e152267b915d081de5baccd189abef1d4d0f4483f63028\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-audit-limits.json\",\n    \"bytes\": 705,\n    \"sha256\": \"f64f8b240c2f0230971f46269406ea26d1282b5e5fb6c0dbebf096d3130e59d3\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-input.json\",\n    \"bytes\": 546,\n    \"sha256\": \"0f658c9e7fa9b7f2c6583e6bff2d27f6f3c15ca691e6b142dd7dbf9edb5cec9d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-assignment-history.json\",\n    \"bytes\": 3,\n    \"sha256\": \"37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/live-transcript.jsonl\",\n    \"bytes\": 709039,\n    \"sha256\": \"839a697d3a4b0c0d8ff92cfb3af6cff5498a58af5cc8d8b42e2a35cd7566c3b0\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-observed.json\",\n    \"bytes\": 517,\n    \"sha256\": \"67e5c9518b6b0d6903e73f06499e6d1c469838948b3406f0f933cf861b27d9c1\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-start.json\",\n    \"bytes\": 505,\n    \"sha256\": \"b607f63b44eda1eed29518fe9f1f8334e5f233dfedb8cc1510d62f9fd1204e8c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/initial-status.json\",\n    \"bytes\": 149,\n    \"sha256\": \"8337d81b45a106e3a053ec73379a259422c0c634101b7fecda622f3e68001e8e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/root-trail-audit.json\",\n    \"bytes\": 1022,\n    \"sha256\": \"8aa2c040da084878369376368f618d1eac5f7372eb1f05c0f0c61a4a2731d9bb\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-input-diff.json\",\n    \"bytes\": 192,\n    \"sha256\": \"e9df7a83cc6470e7ce365839f74bd7de2e28bc9905adf6ea7663a12d6e0fdf05\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/absent-workers.result.md\",\n    \"bytes\": 7357,\n    \"sha256\": \"c13a509d83d2291c1b484236c228604d7a43e29acd448865fb6698662278a798\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/supplied-input.json\",\n    \"bytes\": 17976,\n    \"sha256\": \"17441414e08a1265fb5035413a88c8303a39c343039ff71b988a2b614ebea2a3\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"bytes\": 2127,\n    \"sha256\": \"a9e8990c6d469f9ca731c011fc5c6131eb9fb2b65d6b2d8dd477aad22d462858\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/baseline.md\",\n    \"bytes\": 216,\n    \"sha256\": \"aa769b2d59578f3a403e739222cd8905fcc14cc818600cd45aa303abf06f37dd\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/events.jsonl\",\n    \"bytes\": 7214,\n    \"sha256\": \"17096f43172c42775f88eb70e94044b9ee67ca1aad2066c57c7b40a7ec45e812\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/references/agent-prompts/poteto-agent.md\",\n    \"bytes\": 1221,\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/show-me-your-work/references/decision-log-template.tsv\",\n    \"bytes\": 38,\n    \"sha256\": \"6779378006a2f5225e8c06deb84f1d913fb532041ebbb6e50d94600bfe3f4b76\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/show-me-your-work/scripts/log.sh\",\n    \"bytes\": 1717,\n    \"sha256\": \"fb47611cbb75ea17aa80cb4f8dbfc7978b8844450b0ce702961bdef65cbb1342\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/show-me-your-work/SKILL.md\",\n    \"bytes\": 8456,\n    \"sha256\": \"3c4f05ffecc162b6ae376b7adcf4e7d030c8dfc65a7f26f8519f2c1544c3b98b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/poteto-mode/playbooks/pause-safely.md\",\n    \"bytes\": 3717,\n    \"sha256\": \"bfc3a370414d4365f05d6821c30a9731868f429f9bbc7570cd028a12d174982e\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/poteto-mode/playbooks/orchestrate.md\",\n    \"bytes\": 24094,\n    \"sha256\": \"bd3d7d52f475effd6c0365125da3dccbef4c79a93be5cd0752a1bc71545e0adb\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/sources/skills/poteto-mode/SKILL.md\",\n    \"bytes\": 32329,\n    \"sha256\": \"cb03eedb91cea96b570af30a7af317c6aae6a47a321cff2e82af656141ab0f14\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/outputs/coordinator-inspection.md\",\n    \"bytes\": 379,\n    \"sha256\": \"510c20aec108e30d249a622b6de9bde3d444e2075bd037550a317099eb8b8d56\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/inputs/invoice.mjs\",\n    \"bytes\": 371,\n    \"sha256\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\"\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/assignments/trace.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/assignments/trace.json",
      "sha256": "dce24d4ab6b25a209d4b4e342885f8cf0a32caea2cbcec127ca0d1e9f4bc0ead",
      "bytes": 1537,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"id\": \"absent-workers/trace\",\n  \"scope\": \"Trace controller total through facade, adapter and calculate with concrete file lines and symbols. Read only the committed source. Return result in terminal response; do not write any files. One sample is one source trace, sampleCount 1, order read then trace then report.\",\n  \"inputRevision\": \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\",\n  \"outputOwner\": \"reserved for native identity of trace\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/outputs/trace.json\",\n  \"role\": \"trace\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"absent-workers/evidence/trace-input.json\"\n  ],\n  \"inputPath\": \"committed-inputs/invoice.mjs\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"permissions\": \"read-only; no writes\",\n  \"verify\": \"git rev-parse HEAD; git show 7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs; verify source citations; use Bun for any scripts\",\n  \"timebox\": \"5 minutes maximum, return partial or blocked on expiry\",\n  \"forbidden\": \"No commits, source changes, network, installs, config, external services, spawning, contested output, or other worker paths\",\n  \"report\": \"Return assignmentId, inputRevision, current full HEAD, status, method, evidence, artifact path, executed commands and outputs with exit codes. Models and efforts unknown unless actually observed.\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/baseline.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/baseline.md",
      "sha256": "aa769b2d59578f3a403e739222cd8905fcc14cc818600cd45aa303abf06f37dd",
      "bytes": 216,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "Supplied earlier no-worker trial remains unchanged. Baseline batch-06 was active-or-not-yet-finished, grade null. Earlier raw trial files were not supplied in this root. This is a separate capability-change variant.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/decisions.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv",
      "sha256": "a9e8990c6d469f9ca731c011fc5c6131eb9fb2b65d6b2d8dd477aad22d462858",
      "bytes": 2127,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T08:11:36Z\tframe\tPreserved prior trial and prepared exact committed input\tCurrent host operations require observation\tabsent-workers/permissions.json\topen\n2026-10-16T08:17:26Z\tobserve\tInspected native invoice trace and reproduced total\tObserved artifacts govern integration\tabsent-workers/evidence/current-transcript.jsonl\tobserved\n2026-10-16T08:20:32Z\taudit\tRecorded checklist timing and encrypted history limits\tPreserve actual method deviations instead of reconstructing history\tabsent-workers/evidence/native-calls-and-returns.json\tExact verbatim workflow checklist copied after execution; initial throughput checkpoint preceded dispatch. Spawn wrapper plaintext is encrypted in host history.\n2026-10-16T08:24:11Z\taudit-gap\tKept the original no-worker trial separate\tNew host capability does not regrade prior supplied history\tabsent-workers/baseline.md\tAudit-time record of prior observation. Earlier raw trial unavailable\n2026-10-16T08:24:11Z\taudit-gap\tDispatched native read-only invoice worker\tUser authorized a capability-change test\tabsent-workers/evidence/trace-actual-dispatch.json\tAudit-time record of prior observation. Native identity /root/invoice_trace returned\n2026-10-16T08:24:11Z\taudit-gap\tAccepted the inspected matching invoice trace\tResult SHA, HEAD, symbols and method matched\tabsent-workers/outputs/coordinator-inspection.md\tAudit-time record of prior observation. Bun independently returned total 11\n2026-10-16T08:24:11Z\taudit-gap\tRan the installed TypeScript compiler on committed source\tUser required actual compiler execution\tabsent-workers/evidence/compiler-noemit.json\tAudit-time record of prior observation. No-emit check exited 0\n2026-10-16T08:25:41Z\treview\tPreserved independent cross-model trail review and responded to gaps\tReviewer checked the pre-repair evidence; root repaired local preservation only\tabsent-workers/evidence/review-response.md\tObserved reviewer gpt-5.6-sol medium. Plaintext dispatch equality, placeholder pre-dispatch owners, late checklist and native interrupted-state limits remain. No independent re-review of repairs.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/audit-gap-1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-1.json",
      "sha256": "21905b4cfa7aca50be3757e670793a0d537cd59500f17e94c3bad2aae77c473d",
      "bytes": 571,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"audit-gap\",\n    \"Kept the original no-worker trial separate\",\n    \"New host capability does not regrade prior supplied history\",\n    \"absent-workers/baseline.md\",\n    \"Audit-time record of prior observation. Earlier raw trial unavailable\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/audit-gap-2.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-2.json",
      "sha256": "b584d4b52ccfef9f1eabac764b276d989183ac4cfa285e569af1dfe8f1c8788f",
      "bytes": 591,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"audit-gap\",\n    \"Dispatched native read-only invoice worker\",\n    \"User authorized a capability-change test\",\n    \"absent-workers/evidence/trace-actual-dispatch.json\",\n    \"Audit-time record of prior observation. Native identity /root/invoice_trace returned\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/audit-gap-3.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-3.json",
      "sha256": "c00a88d256502ac2f171dea77fee0811eb95d857436dfed1b7a6c43872430416",
      "bytes": 587,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"audit-gap\",\n    \"Accepted the inspected matching invoice trace\",\n    \"Result SHA, HEAD, symbols and method matched\",\n    \"absent-workers/outputs/coordinator-inspection.md\",\n    \"Audit-time record of prior observation. Bun independently returned total 11\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/audit-gap-4.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/audit-gap-4.json",
      "sha256": "101d837dbfe1610becd69266ba0762ccfbe1202998db2340d95763ae73639a9c",
      "bytes": 577,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"audit-gap\",\n    \"Ran the installed TypeScript compiler on committed source\",\n    \"User required actual compiler execution\",\n    \"absent-workers/evidence/compiler-noemit.json\",\n    \"Audit-time record of prior observation. No-emit check exited 0\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/compiler-noemit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/compiler-noemit.json",
      "sha256": "274c1e93187a7798b29ed348e0de0aeb1f24e23db43f8708cfe85b7503b17788",
      "bytes": 293,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--noEmit\",\n    \"--allowJs\",\n    \"--checkJs\",\n    \"--target\",\n    \"es2023\",\n    \"committed-inputs/invoice.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/compiler.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/compiler.json",
      "sha256": "65d9dd78e1c8992fcd22f5fd2ace51bfd504916ca43a0ac1b07894f617876c89",
      "bytes": 209,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--version\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"Version 5.9.3\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/coordinator-independent-invoice-probe.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/coordinator-independent-invoice-probe.json",
      "sha256": "1a4fc52950b7ea6dbf1ccea2ce298a73f948129276e4e6569c92841986d70f0a",
      "bytes": 550,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const p=Bun.spawnSync([\\\"git\\\",\\\"show\\\",\\\"7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs\\\"]);if(p.exitCode)process.exit(p.exitCode);const m=await import(\\\"data:text/javascript;base64,\\\"+Buffer.from(p.stdout).toString(\\\"base64\\\"));const got=m.controller({rows:[{qty:2,unitPrice:3.5},{qty:1,unitPrice:4}]});if(got.total!==11)throw new Error(\\\"invoice mismatch\\\");console.log(JSON.stringify(got));\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"total\\\":11}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-dirty-paths.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-dirty-paths.json",
      "sha256": "144c78f173d66fcd996632e9a7404d256bc7e3460fd98505542b8d127778841f",
      "bytes": 15722,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"status\",\n    \"--porcelain=v1\",\n    \"--untracked-files=all\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"?? RESULTS.md\\n?? absent-workers/absent-workers.result.md\\n?? absent-workers/artifact-paths.json\\n?? absent-workers/assignments/trace.json\\n?? absent-workers/baseline.md\\n?? absent-workers/decisions.tsv\\n?? absent-workers/events.jsonl\\n?? absent-workers/evidence/audit-gap-1.json\\n?? absent-workers/evidence/audit-gap-2.json\\n?? absent-workers/evidence/audit-gap-3.json\\n?? absent-workers/evidence/audit-gap-4.json\\n?? absent-workers/evidence/compiler-noemit.json\\n?? absent-workers/evidence/compiler.json\\n?? absent-workers/evidence/coordinator-independent-invoice-probe.json\\n?? absent-workers/evidence/current-transcript.jsonl\\n?? absent-workers/evidence/final-head.json\\n?? absent-workers/evidence/final-input-diff.json\\n?? absent-workers/evidence/final-tracked-diff.json\\n?? absent-workers/evidence/final-trail-audit.json\\n?? absent-workers/evidence/final-trail-readback.json\\n?? absent-workers/evidence/initial-status.json\\n?? absent-workers/evidence/live-transcript-2.jsonl\\n?? absent-workers/evidence/live-transcript.jsonl\\n?? absent-workers/evidence/native-calls-and-returns.json\\n?? absent-workers/evidence/observed-worker-metadata.json\\n?? absent-workers/evidence/review-response.md\\n?? absent-workers/evidence/revision.json\\n?? absent-workers/evidence/root-trail-audit.json\\n?? absent-workers/evidence/source-freeze-comparison.json\\n?? absent-workers/evidence/trace-actual-dispatch.json\\n?? absent-workers/evidence/trace-assignment-history.json\\n?? absent-workers/evidence/trace-full-readable-assignment.md\\n?? absent-workers/evidence/trace-input.json\\n?? absent-workers/evidence/trace-native-identity.json\\n?? absent-workers/evidence/trace-returned-messages.json\\n?? absent-workers/evidence/trace-spawn-return.json\\n?? absent-workers/evidence/trace-worker-transcript.jsonl\\n?? absent-workers/evidence/trail-audit-limits.json\\n?? absent-workers/evidence/trail-observed.json\\n?? absent-workers/evidence/trail-readback-after-audit.json\\n?? absent-workers/evidence/trail-readback.json\\n?? absent-workers/evidence/trail-review-close.json\\n?? absent-workers/evidence/trail-review-native-identity.json\\n?? absent-workers/evidence/trail-review-original.md\\n?? absent-workers/evidence/trail-start.json\\n?? absent-workers/evidence/worker-metadata.json\\n?? absent-workers/inputs/invoice.mjs\\n?? absent-workers/outputs/coordinator-inspection.md\\n?? absent-workers/permissions.json\\n?? absent-workers/source-manifest.json\\n?? absent-workers/sources/references/agent-prompts/poteto-agent.md\\n?? absent-workers/sources/skills/poteto-mode/SKILL.md\\n?? absent-workers/sources/skills/poteto-mode/playbooks/orchestrate.md\\n?? absent-workers/sources/skills/poteto-mode/playbooks/pause-safely.md\\n?? absent-workers/sources/skills/show-me-your-work/SKILL.md\\n?? absent-workers/sources/skills/show-me-your-work/references/decision-log-template.tsv\\n?? absent-workers/sources/skills/show-me-your-work/scripts/log.sh\\n?? absent-workers/supplied-input.json\\n?? absent-workers/workflow-checklist.md\\n?? cancelled-worker/assignments/complete-B.json\\n?? cancelled-worker/assignments/partial-A.json\\n?? cancelled-worker/baseline.md\\n?? cancelled-worker/cancelled-worker.result.md\\n?? cancelled-worker/decisions.tsv\\n?? cancelled-worker/events.jsonl\\n?? cancelled-worker/evidence/audit-gap-1.json\\n?? cancelled-worker/evidence/audit-gap-2.json\\n?? cancelled-worker/evidence/audit-gap-3.json\\n?? cancelled-worker/evidence/audit-gap-4.json\\n?? cancelled-worker/evidence/audit-gap-5.json\\n?? cancelled-worker/evidence/audit-gap-6.json\\n?? cancelled-worker/evidence/complete-B-actual-dispatch.json\\n?? cancelled-worker/evidence/complete-B-assignment-history.json\\n?? cancelled-worker/evidence/complete-B-full-readable-assignment.md\\n?? cancelled-worker/evidence/complete-B-input.json\\n?? cancelled-worker/evidence/complete-B-native-identity.json\\n?? cancelled-worker/evidence/complete-B-returned-messages.json\\n?? cancelled-worker/evidence/complete-B-worker-transcript.jsonl\\n?? cancelled-worker/evidence/coordinator-corpus-inspection.json\\n?? cancelled-worker/evidence/current-transcript.jsonl\\n?? cancelled-worker/evidence/final-trail-audit.json\\n?? cancelled-worker/evidence/final-trail-readback.json\\n?? cancelled-worker/evidence/initial-status.json\\n?? cancelled-worker/evidence/live-transcript-2.jsonl\\n?? cancelled-worker/evidence/live-transcript.jsonl\\n?? cancelled-worker/evidence/native-calls-and-returns.json\\n?? cancelled-worker/evidence/observed-worker-metadata.json\\n?? cancelled-worker/evidence/partial-A-actual-dispatch.json\\n?? cancelled-worker/evidence/partial-A-assignment-history.json\\n?? cancelled-worker/evidence/partial-A-full-readable-assignment.md\\n?? cancelled-worker/evidence/partial-A-input.json\\n?? cancelled-worker/evidence/partial-A-native-identity.json\\n?? cancelled-worker/evidence/partial-A-returned-messages.json\\n?? cancelled-worker/evidence/partial-A-spawn-return.json\\n?? cancelled-worker/evidence/partial-A-worker-transcript.jsonl\\n?? cancelled-worker/evidence/partial-before-stop.json\\n?? cancelled-worker/evidence/review-response.md\\n?? cancelled-worker/evidence/revision.json\\n?? cancelled-worker/evidence/root-trail-audit.json\\n?? cancelled-worker/evidence/source-freeze-comparison.json\\n?? cancelled-worker/evidence/stop-return.json\\n?? cancelled-worker/evidence/terminal-inspection.json\\n?? cancelled-worker/evidence/trail-audit-limits.json\\n?? cancelled-worker/evidence/trail-observed.json\\n?? cancelled-worker/evidence/trail-readback-after-audit.json\\n?? cancelled-worker/evidence/trail-readback.json\\n?? cancelled-worker/evidence/trail-review-close.json\\n?? cancelled-worker/evidence/trail-review-native-identity.json\\n?? cancelled-worker/evidence/trail-review-original.md\\n?? cancelled-worker/evidence/trail-start.json\\n?? cancelled-worker/evidence/worker-metadata.json\\n?? cancelled-worker/inputs/records.jsonl\\n?? cancelled-worker/outputs/complete-B/review.json\\n?? cancelled-worker/outputs/coordinator/summary.md\\n?? cancelled-worker/outputs/partial-A/PARTIAL.json\\n?? cancelled-worker/permissions.json\\n?? cancelled-worker/quarantine/index.json\\n?? cancelled-worker/quarantine/partial-A/PARTIAL.json\\n?? cancelled-worker/source-manifest.json\\n?? cancelled-worker/sources/references/agent-prompts/poteto-agent.md\\n?? cancelled-worker/sources/skills/poteto-mode/SKILL.md\\n?? cancelled-worker/sources/skills/poteto-mode/playbooks/orchestrate.md\\n?? cancelled-worker/sources/skills/poteto-mode/playbooks/pause-safely.md\\n?? cancelled-worker/sources/skills/show-me-your-work/SKILL.md\\n?? cancelled-worker/sources/skills/show-me-your-work/references/decision-log-template.tsv\\n?? cancelled-worker/sources/skills/show-me-your-work/scripts/log.sh\\n?? cancelled-worker/supplied-input.json\\n?? cancelled-worker/workflow-checklist.md\\n?? capture-live.mjs\\n?? close-audit-gaps.mjs\\n?? finalize-evidence.mjs\\n?? inspect-results.mjs\\n?? interrupted-action/action-record.json\\n?? interrupted-action/assignments/partial-A.json\\n?? interrupted-action/baseline.md\\n?? interrupted-action/decisions.tsv\\n?? interrupted-action/destination-state.json\\n?? interrupted-action/events.jsonl\\n?? interrupted-action/evidence/audit-gap-1.json\\n?? interrupted-action/evidence/audit-gap-2.json\\n?? interrupted-action/evidence/audit-gap-3.json\\n?? interrupted-action/evidence/audit-gap-4.json\\n?? interrupted-action/evidence/audit-gap-5.json\\n?? interrupted-action/evidence/audit-gap-6.json\\n?? interrupted-action/evidence/audit-gap-7.json\\n?? interrupted-action/evidence/audit-gap-8.json\\n?? interrupted-action/evidence/audit-gap-9.json\\n?? interrupted-action/evidence/branch.json\\n?? interrupted-action/evidence/checkpoint-dirty-paths.json\\n?? interrupted-action/evidence/checkpoint-readback.json\\n?? interrupted-action/evidence/current-transcript.jsonl\\n?? interrupted-action/evidence/destination-reinspection.json\\n?? interrupted-action/evidence/final-trail-audit.json\\n?? interrupted-action/evidence/final-trail-readback.json\\n?? interrupted-action/evidence/initial-status.json\\n?? interrupted-action/evidence/input-forge.json.json\\n?? interrupted-action/evidence/input-history.json.json\\n?? interrupted-action/evidence/inspected-action-record.json\\n?? interrupted-action/evidence/inspected-destination-state.json\\n?? interrupted-action/evidence/live-transcript-2.jsonl\\n?? interrupted-action/evidence/live-transcript.jsonl\\n?? interrupted-action/evidence/native-calls-and-returns.json\\n?? interrupted-action/evidence/observed-worker-metadata.json\\n?? interrupted-action/evidence/partial-A-actual-dispatch.json\\n?? interrupted-action/evidence/partial-A-assignment-history.json\\n?? interrupted-action/evidence/partial-A-full-readable-assignment.md\\n?? interrupted-action/evidence/partial-A-input.json\\n?? interrupted-action/evidence/partial-A-native-identity.json\\n?? interrupted-action/evidence/partial-A-returned-messages.json\\n?? interrupted-action/evidence/partial-A-spawn-return.json\\n?? interrupted-action/evidence/partial-A-worker-transcript.jsonl\\n?? interrupted-action/evidence/partial-before-stop.json\\n?? interrupted-action/evidence/review-response.md\\n?? interrupted-action/evidence/revision.json\\n?? interrupted-action/evidence/root-trail-audit.json\\n?? interrupted-action/evidence/source-freeze-comparison.json\\n?? interrupted-action/evidence/stop-return.json\\n?? interrupted-action/evidence/terminal-inspection.json\\n?? interrupted-action/evidence/trail-audit-limits.json\\n?? interrupted-action/evidence/trail-observed.json\\n?? interrupted-action/evidence/trail-readback-after-audit.json\\n?? interrupted-action/evidence/trail-readback.json\\n?? interrupted-action/evidence/trail-review-close.json\\n?? interrupted-action/evidence/trail-review-native-identity.json\\n?? interrupted-action/evidence/trail-review-original.md\\n?? interrupted-action/evidence/trail-start.json\\n?? interrupted-action/evidence/worker-metadata.json\\n?? interrupted-action/inputs/records.jsonl\\n?? interrupted-action/interrupted-action.result.md\\n?? interrupted-action/outputs/partial-A/PARTIAL.json\\n?? interrupted-action/permissions.json\\n?? interrupted-action/quarantine/index.json\\n?? interrupted-action/quarantine/partial-A/PARTIAL.json\\n?? interrupted-action/resume-note.md\\n?? interrupted-action/source-manifest.json\\n?? interrupted-action/sources/references/agent-prompts/poteto-agent.md\\n?? interrupted-action/sources/skills/poteto-mode/SKILL.md\\n?? interrupted-action/sources/skills/poteto-mode/playbooks/orchestrate.md\\n?? interrupted-action/sources/skills/poteto-mode/playbooks/pause-safely.md\\n?? interrupted-action/sources/skills/show-me-your-work/SKILL.md\\n?? interrupted-action/sources/skills/show-me-your-work/references/decision-log-template.tsv\\n?? interrupted-action/sources/skills/show-me-your-work/scripts/log.sh\\n?? interrupted-action/supplied-input.json\\n?? interrupted-action/workflow-checklist.md\\n?? run-evidence.mjs\\n?? shared-path-conflict/assignments/worker-A.json\\n?? shared-path-conflict/assignments/worker-B.json\\n?? shared-path-conflict/baseline.md\\n?? shared-path-conflict/decisions.tsv\\n?? shared-path-conflict/events.jsonl\\n?? shared-path-conflict/evidence/audit-gap-1.json\\n?? shared-path-conflict/evidence/audit-gap-2.json\\n?? shared-path-conflict/evidence/audit-gap-3.json\\n?? shared-path-conflict/evidence/audit-gap-4.json\\n?? shared-path-conflict/evidence/audit-gap-5.json\\n?? shared-path-conflict/evidence/audit-gap-6.json\\n?? shared-path-conflict/evidence/audit-gap-7.json\\n?? shared-path-conflict/evidence/coordinator-behavior-inspection.json\\n?? shared-path-conflict/evidence/current-transcript.jsonl\\n?? shared-path-conflict/evidence/final-trail-audit.json\\n?? shared-path-conflict/evidence/final-trail-readback.json\\n?? shared-path-conflict/evidence/initial-inspection.json\\n?? shared-path-conflict/evidence/initial-status.json\\n?? shared-path-conflict/evidence/inspect-method.json\\n?? shared-path-conflict/evidence/installed-method-validator-attempt-2.json\\n?? shared-path-conflict/evidence/installed-method-validator.json\\n?? shared-path-conflict/evidence/live-transcript-2.jsonl\\n?? shared-path-conflict/evidence/live-transcript.jsonl\\n?? shared-path-conflict/evidence/native-calls-and-returns.json\\n?? shared-path-conflict/evidence/observed-worker-metadata.json\\n?? shared-path-conflict/evidence/receipt-first-draft.json\\n?? shared-path-conflict/evidence/receipt-order-and-role-mapping.json\\n?? shared-path-conflict/evidence/review-response.md\\n?? shared-path-conflict/evidence/revision.json\\n?? shared-path-conflict/evidence/root-trail-audit.json\\n?? shared-path-conflict/evidence/source-freeze-comparison.json\\n?? shared-path-conflict/evidence/trail-audit-limits.json\\n?? shared-path-conflict/evidence/trail-observed.json\\n?? shared-path-conflict/evidence/trail-readback-after-audit.json\\n?? shared-path-conflict/evidence/trail-readback.json\\n?? shared-path-conflict/evidence/trail-receipt-correction.json\\n?? shared-path-conflict/evidence/trail-review-close.json\\n?? shared-path-conflict/evidence/trail-review-native-identity.json\\n?? shared-path-conflict/evidence/trail-review-original.md\\n?? shared-path-conflict/evidence/trail-start.json\\n?? shared-path-conflict/evidence/worker-A-actual-dispatch.json\\n?? shared-path-conflict/evidence/worker-A-assignment-history.json\\n?? shared-path-conflict/evidence/worker-A-full-readable-assignment.md\\n?? shared-path-conflict/evidence/worker-A-input.json\\n?? shared-path-conflict/evidence/worker-A-native-identity.json\\n?? shared-path-conflict/evidence/worker-A-returned-messages.json\\n?? shared-path-conflict/evidence/worker-A-spawn-return.json\\n?? shared-path-conflict/evidence/worker-A-worker-transcript.jsonl\\n?? shared-path-conflict/evidence/worker-B-actual-dispatch.json\\n?? shared-path-conflict/evidence/worker-B-assignment-history.json\\n?? shared-path-conflict/evidence/worker-B-full-readable-assignment.md\\n?? shared-path-conflict/evidence/worker-B-input.json\\n?? shared-path-conflict/evidence/worker-B-native-identity.json\\n?? shared-path-conflict/evidence/worker-B-returned-messages.json\\n?? shared-path-conflict/evidence/worker-B-spawn-return.json\\n?? shared-path-conflict/evidence/worker-B-worker-transcript.jsonl\\n?? shared-path-conflict/evidence/worker-metadata.json\\n?? shared-path-conflict/inputs/calculator.mjs\\n?? shared-path-conflict/inputs/formatter.mjs\\n?? shared-path-conflict/method-evidence.json\\n?? shared-path-conflict/method-receipt.json\\n?? shared-path-conflict/outputs/coordinator/summary.md\\n?? shared-path-conflict/outputs/worker-A/calculator-review.txt\\n?? shared-path-conflict/outputs/worker-B/formatter-review.txt\\n?? shared-path-conflict/ownership-before-dispatch.json\\n?? shared-path-conflict/permissions.json\\n?? shared-path-conflict/shared-path-conflict.result.md\\n?? shared-path-conflict/source-manifest.json\\n?? shared-path-conflict/sources/references/agent-prompts/poteto-agent.md\\n?? shared-path-conflict/sources/skills/poteto-mode/SKILL.md\\n?? shared-path-conflict/sources/skills/poteto-mode/playbooks/orchestrate.md\\n?? shared-path-conflict/sources/skills/poteto-mode/playbooks/pause-safely.md\\n?? shared-path-conflict/sources/skills/show-me-your-work/SKILL.md\\n?? shared-path-conflict/sources/skills/show-me-your-work/references/decision-log-template.tsv\\n?? shared-path-conflict/sources/skills/show-me-your-work/scripts/log.sh\\n?? shared-path-conflict/supplied-input.json\\n?? shared-path-conflict/workflow-checklist.md\\n?? throughput-checkpoint.md\\n?? trail-review/assignment.json\\n?? trail-review/native-identity.json\\n?? trail-review/native-transcript.jsonl\\n?? trail-review/review.md\\n?? trail-review/spawn-return.json\\n?? write-reports.mjs\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-head.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-head.json",
      "sha256": "07f9a2720ef5aa1a89e2c68d23f0202a2f11fe51765a0c2347db33899f6fe13c",
      "bytes": 150,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-input-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-input-diff.json",
      "sha256": "e9df7a83cc6470e7ce365839f74bd7de2e28bc9905adf6ea7663a12d6e0fdf05",
      "bytes": 192,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"diff\",\n    \"--name-only\",\n    \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\",\n    \"--\",\n    \"committed-inputs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-tracked-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-tracked-diff.json",
      "sha256": "880e428b992afb471bdb448a74396ac70977d15dec34c27457d5959a0e287890",
      "bytes": 158,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"diff\",\n    \"--name-only\",\n    \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-trail-audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-trail-audit.json",
      "sha256": "f40f57adb16a1577d127848e4919dcc5bfbd1f635ed9ac1acaf3c998ef01a7b2",
      "bytes": 1661,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"runId\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n  \"rows\": [\n    {\n      \"row\": 2,\n      \"phase\": \"frame\",\n      \"evidence\": \"absent-workers/permissions.json\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 3,\n      \"phase\": \"observe\",\n      \"evidence\": \"absent-workers/evidence/current-transcript.jsonl\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 4,\n      \"phase\": \"audit\",\n      \"evidence\": \"absent-workers/evidence/native-calls-and-returns.json\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 5,\n      \"phase\": \"audit-gap\",\n      \"evidence\": \"absent-workers/baseline.md\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 6,\n      \"phase\": \"audit-gap\",\n      \"evidence\": \"absent-workers/evidence/trace-actual-dispatch.json\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 7,\n      \"phase\": \"audit-gap\",\n      \"evidence\": \"absent-workers/outputs/coordinator-inspection.md\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 8,\n      \"phase\": \"audit-gap\",\n      \"evidence\": \"absent-workers/evidence/compiler-noemit.json\",\n      \"evidenceExists\": true\n    },\n    {\n      \"row\": 9,\n      \"phase\": \"review\",\n      \"evidence\": \"absent-workers/evidence/review-response.md\",\n      \"evidenceExists\": true\n    }\n  ],\n  \"scope\": \"Root checked each final row evidence path against actual source, calls, returns or artifacts. Independent reviewer inspected pre-repair evidence; no complete plaintext audit of encrypted spawn wrappers or earlier-trial raw history is possible.\",\n  \"reviewModel\": \"gpt-5.6-sol\",\n  \"reviewArtifact\": \"evidence/trail-review-original.md\",\n  \"repairResponse\": \"evidence/review-response.md\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-trail-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/final-trail-readback.json",
      "sha256": "28bd2328987452923378cb5e43d5e61855a5df1137428c801827964df881b07a",
      "bytes": 2303,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"path\": \"absent-workers/decisions.tsv\",\n  \"contents\": \"ts\\tphase\\tdecision\\twhy\\tevidence\\tresult\\n2026-10-16T08:11:36Z\\tframe\\tPreserved prior trial and prepared exact committed input\\tCurrent host operations require observation\\tabsent-workers/permissions.json\\topen\\n2026-10-16T08:17:26Z\\tobserve\\tInspected native invoice trace and reproduced total\\tObserved artifacts govern integration\\tabsent-workers/evidence/current-transcript.jsonl\\tobserved\\n2026-10-16T08:20:32Z\\taudit\\tRecorded checklist timing and encrypted history limits\\tPreserve actual method deviations instead of reconstructing history\\tabsent-workers/evidence/native-calls-and-returns.json\\tExact verbatim workflow checklist copied after execution; initial throughput checkpoint preceded dispatch. Spawn wrapper plaintext is encrypted in host history.\\n2026-10-16T08:24:11Z\\taudit-gap\\tKept the original no-worker trial separate\\tNew host capability does not regrade prior supplied history\\tabsent-workers/baseline.md\\tAudit-time record of prior observation. Earlier raw trial unavailable\\n2026-10-16T08:24:11Z\\taudit-gap\\tDispatched native read-only invoice worker\\tUser authorized a capability-change test\\tabsent-workers/evidence/trace-actual-dispatch.json\\tAudit-time record of prior observation. Native identity /root/invoice_trace returned\\n2026-10-16T08:24:11Z\\taudit-gap\\tAccepted the inspected matching invoice trace\\tResult SHA, HEAD, symbols and method matched\\tabsent-workers/outputs/coordinator-inspection.md\\tAudit-time record of prior observation. Bun independently returned total 11\\n2026-10-16T08:24:11Z\\taudit-gap\\tRan the installed TypeScript compiler on committed source\\tUser required actual compiler execution\\tabsent-workers/evidence/compiler-noemit.json\\tAudit-time record of prior observation. No-emit check exited 0\\n2026-10-16T08:25:41Z\\treview\\tPreserved independent cross-model trail review and responded to gaps\\tReviewer checked the pre-repair evidence; root repaired local preservation only\\tabsent-workers/evidence/review-response.md\\tObserved reviewer gpt-5.6-sol medium. Plaintext dispatch equality, placeholder pre-dispatch owners, late checklist and native interrupted-state limits remain. No independent re-review of repairs.\\n\",\n  \"readAt\": \"2026-10-16T08:25:41.496Z\",\n  \"matched\": true\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/initial-status.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/initial-status.json",
      "sha256": "8337d81b45a106e3a053ec73379a259422c0c634101b7fecda622f3e68001e8e",
      "bytes": 149,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"status\",\n    \"--short\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"?? absent-workers/\\n?? run-evidence.mjs\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/observed-worker-metadata.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/observed-worker-metadata.json",
      "sha256": "d603d3ffa271b25e9699a2432638c6df89a791f5b21217246bb7bf9b42d31c04",
      "bytes": 4036,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"timestamp\": \"2026-10-16T08:09:48.153Z\",\n    \"ordinal\": 64,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c2-9502-7c73-b6ba-964bda515a17\",\n        \"agent_path\": \"/root/invoice_trace\"\n      },\n      \"started_at_ms\": 1792138188153,\n      \"completed_at_ms\": 1792138188153\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:10.695Z\",\n    \"ordinal\": 72,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_ae9034d5fad6437f9cfa3344c4b62fbb\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c2-ecf9-7a12-9254-cd633b958a08\",\n        \"agent_path\": \"/root/calculator_review\"\n      },\n      \"started_at_ms\": 1792138210695,\n      \"completed_at_ms\": 1792138210695\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:24.174Z\",\n    \"ordinal\": 77,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_153cdbf4cf3e498f99f617ed5f3227bc\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c3-21c6-77a2-bfd2-822121232fd0\",\n        \"agent_path\": \"/root/formatter_review\"\n      },\n      \"started_at_ms\": 1792138224174,\n      \"completed_at_ms\": 1792138224174\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:11:17.636Z\",\n    \"ordinal\": 119,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_c43ac9613b8048f68693fedf40cd107a\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c3-f2ba-7e02-86b2-21c54bd26898\",\n        \"agent_path\": \"/root/corpus_partial\"\n      },\n      \"started_at_ms\": 1792138277636,\n      \"completed_at_ms\": 1792138277636\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:12:41.920Z\",\n    \"ordinal\": 174,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_de934ce5074a4112b3b486a796f974df\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c5-3bf6-7c23-98ae-3082ae587d46\",\n        \"agent_path\": \"/root/corpus_complete\"\n      },\n      \"started_at_ms\": 1792138361920,\n      \"completed_at_ms\": 1792138361920\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:12:55.971Z\",\n    \"ordinal\": 180,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_b92ab5fb156841daa5260d16fca99728\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c5-72ca-72f2-8f35-883e59ecb4d9\",\n        \"agent_path\": \"/root/pause_partial\"\n      },\n      \"started_at_ms\": 1792138375971,\n      \"completed_at_ms\": 1792138375971\n    }\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/review-response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/review-response.md",
      "sha256": "06e97d34429d3ad72cae89acf0581bbcecb40fcb7c94f07cf2533a44a6a59afb",
      "bytes": 1370,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "# Response to independent trail review\n\nThe original review is retained byte for byte in trail-review-original.md. Missing trail decisions were appended using the exact installed helper, with explicit audit-time wording and specific existing evidence. Assignment lifecycle closure was appended to events.jsonl, explicitly as audit records of prior observed actions, not new native operations. The original immutable pending assignments and pre-dispatch owner placeholders remain unchanged. Updated trail readback is trail-readback-after-audit.json; the older trail-readback.json is a historical snapshot, not current proof.\n\nRemaining limits. Exact plaintext spawn wrapper equality cannot be verified from encrypted host history. Readable immutable briefs and full role prompts are preserved separately. Native owners were bound on spawn rather than known in the immutable pre-dispatch assignment. The exact verbatim checklist was created late, though the throughput checkpoint preceded dispatch. Worker A read some routing instructions after its probe. Native stop exposes interrupted, not literal cancelled or process teardown. Earlier raw unavailable-trial history is absent.\n\nThe reviewer independently checked the pre-repair evidence. The root checked these local preservation repairs; no independent re-review of the repairs is claimed. No case grade is assigned.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/revision.json",
      "sha256": "07f9a2720ef5aa1a89e2c68d23f0202a2f11fe51765a0c2347db33899f6fe13c",
      "bytes": 150,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/root-trail-audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/root-trail-audit.json",
      "sha256": "8aa2c040da084878369376368f618d1eac5f7372eb1f05c0f0c61a4a2731d9bb",
      "bytes": 1022,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"runId\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n  \"scope\": \"Current root conversation and six assigned workers only\",\n  \"rows\": [\n    {\n      \"line\": 2,\n      \"decision\": \"Preserved baseline and exact input\",\n      \"evidence\": [\n        \"permissions.json\",\n        \"baseline.md\",\n        \"evidence/revision.json\"\n      ]\n    },\n    {\n      \"line\": 3,\n      \"decision\": \"Observed native results, source inspection or safe pause\",\n      \"evidence\": [\n        \"evidence/current-transcript.jsonl\"\n      ]\n    },\n    {\n      \"line\": 4,\n      \"decision\": \"Recorded method and history limits\",\n      \"evidence\": [\n        \"evidence/native-calls-and-returns.json\",\n        \"workflow-checklist.md\"\n      ]\n    }\n  ],\n  \"limits\": [\n    \"Earlier ephemeral trial raw records were not supplied.\",\n    \"Native history encrypts spawn wrapper text; readable assignment components are preserved separately.\",\n    \"Exact verbatim workflow checklist was written after execution.\",\n    \"Independent reviewer findings are pending.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/source-freeze-comparison.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/source-freeze-comparison.json",
      "sha256": "7713aa5795e838435793e62d6a55af9b404a6ec1401645e44b8f1496ed45548b",
      "bytes": 850,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"skills/poteto-mode/SKILL.md\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/playbooks/orchestrate.md\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"references/agent-prompts/poteto-agent.md\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/playbooks/pause-safely.md\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"skills/show-me-your-work/SKILL.md\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"skills/show-me-your-work/scripts/log.sh\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  },\n  {\n    \"path\": \"skills/show-me-your-work/references/decision-log-template.tsv\",\n    \"exitCode\": 0,\n    \"match\": true,\n    \"stderr\": \"\"\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-actual-dispatch.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-actual-dispatch.json",
      "sha256": "bb88bdbec70ec1f260746f76c3608598f2290c081000a0b367d75c143b95ae3c",
      "bytes": 5655,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"call\": {\n    \"timestamp\": \"2026-10-16T08:09:48.004Z\",\n    \"ordinal\": 62,\n    \"type\": \"response_item\",\n    \"payload\": {\n      \"type\": \"function_call\",\n      \"id\": \"fc_0efd8d4695b6d13b016ad1dbbeb48c819184ab1de2cd53edb0\",\n      \"name\": \"spawn_agent\",\n      \"namespace\": \"collaboration\",\n      \"arguments\": \"{\\\"task_name\\\":\\\"invoice_trace\\\",\\\"fork_turns\\\":\\\"all\\\",\\\"message\\\":\\\"gAAAAABq0dvLbgdjDgahSRoFVCDRgCiptubZ4gOjBzydhxNTZGD36stb4LcGy8XYSU1hfity4AI_dnMnIDo6zPOA7JjQ3_aDnkG94rdIjg8yIhNQtMlewPHo8fMqGzIeMuwsN7wdI_tznje9GjWjFuXx8jyQCR1u4oK4WSjGSS4DW0ge0PA7CGiexoBZBn2FQSmQGQZ5_vEXXsuE_DHXEUL23dxNzaNcXJ_rX0rYbxpewVJA71L5jSzrLCwhuLBUlUIlTRqQL7z5ivou0_8-Xa-QtpwZ8QLDzv35Rl5QzmOj0DzTUeB3y7SIFNxxrQy_uQYacMwlG2wnbovIqIOYCRij0L--tTcZQIxlL9uU5p4ZfeZxNcnhgxLn8DzILqbqcslMM0UcSHCT-vEQlZ8PBvuHq4GLkxHWVMX5ypF8RWF5sRH-fF9QcVEyoBFebE4RlsafNbNau7AMJHo5Vck5Ee9vFdq9GFcUsMkub46wT4dxklbmhsQDol_j2D-9nmWKg1PsSXnnB2lntjGKwMfWg7rUzcgUeHyzfbw-ZOyRNPbSW--xh6AzOYMVb1NtUFtliP9o9Duz_YtlD1R-6JMddulnurR7L3L6A6l0PSR1SH4SSR3k6Z6OGeOg2M_ZxAJ5UsQM5AyFKF64Nsw9IY0JsE3w1p4PypMRSp5KdISwkjDQFjywThd0ZE5GUGyKY7DzrPbLCg6d0XMsC2qzY32CfFlxZET5dEvD48XvvNzEonOtz-bLYwLgg9BJ5r1pZYsi6YPWYm0nlD5_c00v8PBQR0Hk3CyheVmEoRDcu8eKJt3xJvEMHhn2scog7tsfv_nE5Ge4rbpD1IXMyEuZeb_OPGBKFRcAg5MzW4_xwwZe8sfxn-LdrTND1dvszuuBsNA1skcG7tMoUjw0IXsOWZTHbVzdIta0CSK5jMqUgpwqczNGDn9BpOK_NJOT-1LBNYHeTzzG55YOd6qvsKIQ9aLPYHGGeE-G4npwrnUhk7twMidWXZBZnNd2Vbcr7qrregwiU7PxGeIktKSOzYbV_GJnYIYPI0Ql8ksD6E4vOmr9flAO1JnGzsg3ChfH1BSseMdcPQpDLYaxlXYv9SugMWF8ay849lm4TnxGJ9QHGk1VO7zml5msByGnOxv45-cCNs2xvF5ESrM6JvkZR9yQPtdDE7MVS2wc0oVCehgoua8SmzB4wUOB208tOAOKaWhx1p4nFKaebPklmrn_WoXuoJGlUZLnuqS91_PogHmxv3Posf10KrMp18CSn4mCELbyA-1xZGTh-2JVfQmDxOA2bU1za3jKhVn0AZ0Q6hSwbTXjlu3IA11NhwSIRn_ZDcEEwvdR13tqEkrJp8AWq6EfHxttXwlsIFGRJNIlpj2lSaxjc8PE7jku77Oyb02H-ZvdmWALWkez19qKfA6AUev8iar5GAjlUgoHmHl-buGenVrVyTvh5hoJrKCAzzT8RNw2KCvoO9qhZFRF-ZVHVUAzWFjjREUuRS3mc2PLahtEvyRZ3ZNPbZjsW9Npr9dmZzrMWAn3xtobTLPe_6zZDFpQq-_co1u_CKQQK8FFv_RlpgnIgzCO50C1hKksbujBE3DzX9kf1W-aFJ8PX4rpx2RDw1sfXSsLaYE8vx1-CCdqZ48cXUjzs7hXuUGaxeuHQ7p987bTNXRwvlQ3pOoYyFuXAepIzgiYHEzGGbJhOZa0ltSQAY1y2PccqstdXIDtnLyBq7xov_hdCBxTEIYVYPF4MBLjdWG8diMhSf1ZkjZ_7BaIKI6G1qJCTDp1DF8H7OzEBRaKroUsspLscPEnQYOQP-cBS0lp5VEaa-gmpnDYvCV4ifqW6xjswBYOcXZqGSXKeKXQGC-fv6grsq7iP0_mGN7vcH9W_FBlhxAAdytdGTtnlU9ZEm1w2BITWJTP0k_Tz15as4MbXIfCnyxibLHSs_NZ_Oh6MpywgONt_-6z7-Ntrh0Z3TYJVqwj-MABiMYNqDz7rcZdRM7kA2uFXQRtiXHnzBpxRxRNVz3SPcD-oVhv-YmORbCxCkc5HAkPQqiWqOdJdQVWgcuhgtY1vgz9VYN-vkRMd3eyKrYk718bM4xn2eqObN2_MXzThVjfIVfImhcaMNV1_50DBF5vfe9Fc9MNGp9XVgo4iQitUMaL2DizZnSMpEZg4LqW02Pgb-16IZbxU_xNLfsn8Qpf8V637qP3qrIYxM0FCeOMMcCJ7NC3NoOI1qpuLFr8iOKY1e0RDKzMpPpSVTfjCpr48Zz2_wT7ogOFrHfPsmEpr2aOSgqllXuDTQ_IKzslz0hfa5lvPQc2gVWA3LI8cpzj6UsSYuaDCSiflS3KXqw6-YVmTd39HeFFhNheHneMnZ768qtUKSzmuQrgNWcH4nItPJOiPfaFXl2f1XQD1GwJ8fszs9pZd_X4CFGBHtSae8YHKsQDQy79ljCGLW5F7w3h7ps-2WnSyI_LLhQ8MSdeXcYTuZDlamgM9aRYJOJM6CKB4uhwGl0cpPrzk47l8KZImpJkC816BfIqsqJjwRjdyTsTtgl9YsGeNnc5jRJqggmEK_-vP2kQ9bIdDKwQ7fZrBO3X_rsWx-wtbGD_frLozR0EF_IUvDBeBVaxBZZ1G7WlFakce1UV3wqebwOrPPhlENuGMh6JQZrqWwlpPdFGD5ZZlEoxkUM9qYtk8zihTOAjglSoEOZvB2cSEK7D5ls1OlJeCL7ATwK8kjmDaUicGNcWA7_2NNxlCVMXZzYkJZ1ewq10qW6gKUhJFRgsUUHg_pNOuAaVnlce6a9tf6Y22LvTQLDdy8Qp4P4vz4ekwijb5xW7F8zgFPxFcq1lEjRiYYeeL2Ez99-sT0aa5sQO4fc81ZNxr4m6HmBd8vLsxYaPtxdWRuUy2d4kqRRQdkonEnJDI8GGRoghbSFC88ZmY_5b5OIBOK1jj8_j5W2Au4GUr973lfI7wNMJ4MUvRqivlxNNEZtvX87qnHKHrKjbp0pwJA1pMo1sfVA50hdTzamIHmgSXHsF2k2xukGqf3X4LHymmYEmKCLWX5RLcDf_eoqSz-4skF_EDlkQm_G1ISKOp_zFziOAxf4b1K2wEDxf47O3yxdp1JQsGJicces5in3TO8JwcyxRlD1uZCoOXG6xanbVb6xXuomL0GeSRCKOfJO8KTIB5UXqDQrBz3ro1TBFtSHC41ZHhEpJXsXRoJ1e8hBANhpQxIc24PIfF-ooO7nSNZ3PnHuzZ79TilRdOEhMzhCGMejmiTSfbH_m2_3oGE3358NLt2tBIqnaEfzcwRaSxWkyMdVCeYpEwDGRmw9rNa2VQS2rQthcyNQFQi-r1wBLJkV2vv1I688GrLsqnWqUcb_b1cjL25tZJzvYz1lEYIiSv9-vphIK-V34HbSCNlr5yzlhPl1AFnnN5et2wdiEjm8imp_f2GZlsai6YcgZNsNI4qquIT-lzFdrx9pGbXE3WUhqTBaWdGal3p4me_W-fjmyrWKXWfE1izVCNK6rP0qYB9gJbCdeFg6pDBayFOz22VIEa9KO0G3UBI82yHsoU52DBoOTUcUsfapDkzXoTENi89ZR9fXMJ07FykM9JuCMSztfgVnVkUF-0hxzc2pQr0mnKgM9QTotdeWbXC2b6nbPTldUE2i95upP6SvKSmeGREZlRBCoBTR6CORl\\\"}\",\n      \"call_id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n      \"internal_chat_message_metadata_passthrough\": {\n        \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n        \"create_time\": 1792138174.70931\n      }\n    },\n    \"metadata\": {\n      \"client_authored\": false,\n      \"user_input_order\": 3\n    }\n  },\n  \"returned\": {\n    \"timestamp\": \"2026-10-16T08:09:48.170Z\",\n    \"ordinal\": 65,\n    \"type\": \"response_item\",\n    \"payload\": {\n      \"type\": \"function_call_output\",\n      \"id\": \"fco_01a143c2-958a-7ca0-8454-8064b1f4e805\",\n      \"call_id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n      \"output\": \"{\\\"task_name\\\":\\\"/root/invoice_trace\\\"}\",\n      \"internal_chat_message_metadata_passthrough\": {\n        \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n        \"create_time\": 1792138188.170913\n      }\n    },\n    \"metadata\": {\n      \"client_authored\": false,\n      \"fallback_token_limit_override\": 12000\n    }\n  },\n  \"metadata\": {\n    \"timestamp\": \"2026-10-16T08:09:48.153Z\",\n    \"ordinal\": 64,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c2-9502-7c73-b6ba-964bda515a17\",\n        \"agent_path\": \"/root/invoice_trace\"\n      },\n      \"started_at_ms\": 1792138188153,\n      \"completed_at_ms\": 1792138188153\n    }\n  }\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-assignment-history.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-assignment-history.json",
      "sha256": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
      "bytes": 3,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-full-readable-assignment.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-full-readable-assignment.md",
      "sha256": "a9e2b8b5568f166cef13a1085a3172f8aa7426d56729d0954727fa0faa0392e7",
      "bytes": 3476,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "# Full immutable assignment components\n\nThis preserves the complete pre-dispatch assignment and installed role prompt. It is not a decrypted or byte-identical rendering of the host-encrypted spawn wrapper. The raw original invocation and returned object are preserved separately.\n\n```json\n{\n  \"id\": \"absent-workers/trace\",\n  \"scope\": \"Trace controller total through facade, adapter and calculate with concrete file lines and symbols. Read only the committed source. Return result in terminal response; do not write any files. One sample is one source trace, sampleCount 1, order read then trace then report.\",\n  \"inputRevision\": \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\",\n  \"outputOwner\": \"reserved for native identity of trace\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/outputs/trace.json\",\n  \"role\": \"trace\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"absent-workers/evidence/trace-input.json\"\n  ],\n  \"inputPath\": \"committed-inputs/invoice.mjs\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"permissions\": \"read-only; no writes\",\n  \"verify\": \"git rev-parse HEAD; git show 7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs; verify source citations; use Bun for any scripts\",\n  \"timebox\": \"5 minutes maximum, return partial or blocked on expiry\",\n  \"forbidden\": \"No commits, source changes, network, installs, config, external services, spawning, contested output, or other worker paths\",\n  \"report\": \"Return assignmentId, inputRevision, current full HEAD, status, method, evidence, artifact path, executed commands and outputs with exit codes. Models and efforts unknown unless actually observed.\"\n}\n```\n\n# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\n\nAll role-relative links resolve against /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md. The exact assigned mode is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md. Native worker identity and observed model are bound by the corresponding actual dispatch and native identity artifacts.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-input.json",
      "sha256": "0f658c9e7fa9b7f2c6583e6bff2d27f6f3c15ca691e6b142dd7dbf9edb5cec9d",
      "bytes": 546,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"show\",\n    \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-native-identity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-native-identity.json",
      "sha256": "70e2bb2a3ecbafcdc87593bdda83f952ee7d788170d5bb0dc67d6a82f65be335",
      "bytes": 627,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"timestamp\": \"2026-10-16T08:09:48.153Z\",\n  \"ordinal\": 64,\n  \"type\": \"event_msg\",\n  \"payload\": {\n    \"type\": \"item_completed\",\n    \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n    \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n    \"item\": {\n      \"type\": \"SubAgentActivity\",\n      \"model\": \"gpt-6.1-sol\",\n      \"reasoning_effort\": \"medium\",\n      \"id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n      \"kind\": \"started\",\n      \"agent_thread_id\": \"01a143c2-9502-7c73-b6ba-964bda515a17\",\n      \"agent_path\": \"/root/invoice_trace\"\n    },\n    \"started_at_ms\": 1792138188153,\n    \"completed_at_ms\": 1792138188153\n  }\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-returned-messages.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-returned-messages.json",
      "sha256": "1ca7081644da4b8dd8a9f25c4177c9dcc60eea2b7f033c7c15bfb107be511da2",
      "bytes": 6503,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"timestamp\": \"2026-10-16T08:09:58.207Z\",\n    \"ordinal\": 24,\n    \"type\": \"response_item\",\n    \"payload\": {\n      \"type\": \"message\",\n      \"id\": \"msg_05daf06b168cf485016ad1dbd552d48191b432c411bac0fb44\",\n      \"role\": \"assistant\",\n      \"content\": [\n        {\n          \"type\": \"output_text\",\n          \"text\": \"I’m applying the installed pstack-openai 0.1.0 Investigation workflow to the committed invoice source. This worker has read-only ownership and will return the trace to the coordinator.\\n\"\n        }\n      ],\n      \"phase\": \"commentary\",\n      \"internal_chat_message_metadata_passthrough\": {\n        \"turn_id\": \"01a143c2-9579-7d41-afc8-f309c5c2d8ac\",\n        \"create_time\": 1792138197.3267648,\n        \"content_item_kinds\": [\n          \"unknown\"\n        ]\n      }\n    },\n    \"metadata\": {\n      \"retained_source\": {\n        \"id\": {\n          \"message_id\": \"msg_05daf06b168cf485016ad1dbd552d48191b432c411bac0fb44\",\n          \"turn_id\": \"01a143c2-9579-7d41-afc8-f309c5c2d8ac\",\n          \"role\": \"assistant\"\n        },\n        \"revision\": \"retained_01a143c2-bcbf-7780-8c1f-7d6a5eea164f\",\n        \"complete\": true\n      },\n      \"client_authored\": false,\n      \"user_input_order\": 1\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:41.059Z\",\n    \"ordinal\": 48,\n    \"type\": \"response_item\",\n    \"payload\": {\n      \"type\": \"message\",\n      \"id\": \"msg_05daf06b168cf485016ad1dbea7be88191a949dde6b2cf54e6\",\n      \"role\": \"assistant\",\n      \"content\": [\n        {\n          \"type\": \"output_text\",\n          \"text\": \"Assignment `absent-workers/trace` completed its read-only source trace.\\n\\n- Input revision and observed full HEAD both equal `7b1fcb74b4a5ed3fcadc979da831aa98a621d236`.\\n- Requested model and effort were `inherit-parent`. Observed model and effort remain unknown.\\n- Method was one committed-source trace, `sampleCount 1`, ordered read, trace, report.\\n- No files were written. The terminal response is the returned artifact.\\n\\n`throughput checkpoint: n/a, read-only investigation`\\n\\nThe Investigation checklist was completed inline because this assignment prohibits writes. I read How, traced the source, produced the explanation, and applied Unslop. Nested delegation was explicitly forbidden, so I performed the explainer role directly.\\n\\nThe controller returns the arithmetic total without formatting. All evidence below refers to `committed-inputs/invoice.mjs` at the verified input revision.\\n\\n| Line | Symbol | Observed behavior |\\n|---|---|---|\\n| 4 | `controller(invoice)` | Returns `{total: facade(invoice)}`. |\\n| 3 | `facade(invoice)` | Returns `adapter(invoice)`. |\\n| 2 | `adapter(invoice)` | Passes `invoice.rows` to `calculate`. |\\n| 1 | `calculate(rows)` | Reduces from `0`, adding `r.qty * r.unitPrice` for each row. |\\n| 5 | `format(n)` | Rejects nonfinite numbers and returns two decimal places, but the controller trace never calls it. |\\n\\nAn executed Bun check loaded these exact committed bytes through a data URL. For rows `{qty:2, unitPrice:3.5}` and `{qty:1, unitPrice:4}`, it returned:\\n\\n```json\\n{\\\"invoice\\\":{\\\"rows\\\":[{\\\"qty\\\":2,\\\"unitPrice\\\":3.5},{\\\"qty\\\":1,\\\"unitPrice\\\":4}]},\\\"controller\\\":{\\\"total\\\":11},\\\"facade\\\":11,\\\"adapter\\\":11,\\\"calculate\\\":11}\\n```\\n\\nProve It Works shaped the verification choice. I inspected numbered committed source and executed that source directly. This sample verifies the traced happy path only. It does not establish validation, rounding guarantees, or behavior for malformed input.\\n\\nCommands and observed results:\\n\\n1. `cat` read the complete assignment at `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/assignments/trace.json` and the complete installed `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md`. Combined command exited `0`.\\n2. `cat` read the complete installed `playbooks/investigation.md`, `references/host-capabilities.md`, `references/model-roles.md`, `references/orchestration-contract.md`, `skills/unslop/SKILL.md`, and `skills/principle-prove-it-works/SKILL.md`. Combined command exited `0`.\\n3. A combined command read `skills/how/SKILL.md`, ran `git rev-parse HEAD`, ran `git show 7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs`, then ran `rg --files -g AGENTS.md -g CLAUDE.md`. It returned the full How instructions, matching HEAD and five source lines. The combined exit was `1` because `rg` found no matching files. The Git operations were independently repeated successfully.\\n4. `cat /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/how/references/explainer-prompt.md` exited `0`.\\n5. `git rev-parse HEAD` exited `0` and returned the exact input SHA.\\n6. `git show 7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs | nl -ba` exited `0` and returned the cited five numbered lines.\\n7. The following executed command exited `0` and returned the JSON above:\\n\\n```sh\\nbun --no-install -e 'const p=Bun.spawnSync([\\\"git\\\",\\\"show\\\",\\\"7b1fcb74b4a5ed3fcadc979da831aa98a621d236:committed-inputs/invoice.mjs\\\"]); if(p.exitCode!==0){process.stderr.write(p.stderr);process.exit(p.exitCode)} const mod=await import(\\\"data:text/javascript;base64,\\\"+Buffer.from(p.stdout).toString(\\\"base64\\\")); const invoice={rows:[{qty:2,unitPrice:3.5},{qty:1,unitPrice:4}]}; console.log(JSON.stringify({invoice,controller:mod.controller(invoice),facade:mod.facade(invoice),adapter:mod.adapter(invoice),calculate:mod.calculate(invoice.rows)}));'\\n```\\n\\nRead and execution operations succeeded through `functions.exec` and `tools.exec_command`. This worker did not inspect its own spawn result or claim model diversity. The coordinator must independently inspect this returned result before integration.\"\n        }\n      ],\n      \"phase\": \"final_answer\",\n      \"internal_chat_message_metadata_passthrough\": {\n        \"turn_id\": \"01a143c2-9579-7d41-afc8-f309c5c2d8ac\",\n        \"create_time\": 1792138218.4898534,\n        \"content_item_kinds\": [\n          \"unknown\"\n        ]\n      }\n    },\n    \"metadata\": {\n      \"retained_source\": {\n        \"id\": {\n          \"message_id\": \"msg_05daf06b168cf485016ad1dbea7be88191a949dde6b2cf54e6\",\n          \"turn_id\": \"01a143c2-9579-7d41-afc8-f309c5c2d8ac\",\n          \"role\": \"assistant\"\n        },\n        \"revision\": \"retained_01a143c3-6423-74b3-acf2-f2ece628e2cb\",\n        \"complete\": false\n      },\n      \"client_authored\": false,\n      \"user_input_order\": 2\n    }\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-spawn-return.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trace-spawn-return.json",
      "sha256": "b8c66d035fe94e311811aeb8e7fc09860c6a4a466a9d10f40797927badbad7ee",
      "bytes": 41,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"task_name\": \"/root/invoice_trace\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-audit-limits.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-audit-limits.json",
      "sha256": "f64f8b240c2f0230971f46269406ea26d1282b5e5fb6c0dbebf096d3130e59d3",
      "bytes": 705,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"audit\",\n    \"Recorded checklist timing and encrypted history limits\",\n    \"Preserve actual method deviations instead of reconstructing history\",\n    \"absent-workers/evidence/native-calls-and-returns.json\",\n    \"Exact verbatim workflow checklist copied after execution; initial throughput checkpoint preceded dispatch. Spawn wrapper plaintext is encrypted in host history.\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-observed.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-observed.json",
      "sha256": "67e5c9518b6b0d6903e73f06499e6d1c469838948b3406f0f933cf861b27d9c1",
      "bytes": 517,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"observe\",\n    \"Inspected native invoice trace and reproduced total\",\n    \"Observed artifacts govern integration\",\n    \"absent-workers/evidence/current-transcript.jsonl\",\n    \"observed\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-readback-after-audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-readback-after-audit.json",
      "sha256": "a068857058aef405b55a52197329f7ad924c6ce9d043614554e89cce8eef0630",
      "bytes": 1970,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"path\": \"absent-workers/decisions.tsv\",\n  \"contents\": \"ts\\tphase\\tdecision\\twhy\\tevidence\\tresult\\n2026-10-16T08:11:36Z\\tframe\\tPreserved prior trial and prepared exact committed input\\tCurrent host operations require observation\\tabsent-workers/permissions.json\\topen\\n2026-10-16T08:17:26Z\\tobserve\\tInspected native invoice trace and reproduced total\\tObserved artifacts govern integration\\tabsent-workers/evidence/current-transcript.jsonl\\tobserved\\n2026-10-16T08:20:32Z\\taudit\\tRecorded checklist timing and encrypted history limits\\tPreserve actual method deviations instead of reconstructing history\\tabsent-workers/evidence/native-calls-and-returns.json\\tExact verbatim workflow checklist copied after execution; initial throughput checkpoint preceded dispatch. Spawn wrapper plaintext is encrypted in host history.\\n2026-10-16T08:24:11Z\\taudit-gap\\tKept the original no-worker trial separate\\tNew host capability does not regrade prior supplied history\\tabsent-workers/baseline.md\\tAudit-time record of prior observation. Earlier raw trial unavailable\\n2026-10-16T08:24:11Z\\taudit-gap\\tDispatched native read-only invoice worker\\tUser authorized a capability-change test\\tabsent-workers/evidence/trace-actual-dispatch.json\\tAudit-time record of prior observation. Native identity /root/invoice_trace returned\\n2026-10-16T08:24:11Z\\taudit-gap\\tAccepted the inspected matching invoice trace\\tResult SHA, HEAD, symbols and method matched\\tabsent-workers/outputs/coordinator-inspection.md\\tAudit-time record of prior observation. Bun independently returned total 11\\n2026-10-16T08:24:11Z\\taudit-gap\\tRan the installed TypeScript compiler on committed source\\tUser required actual compiler execution\\tabsent-workers/evidence/compiler-noemit.json\\tAudit-time record of prior observation. No-emit check exited 0\\n\",\n  \"readAt\": \"2026-10-16T08:24:11.203Z\",\n  \"scope\": \"Readback after append-only audit-gap closure. Earlier readback remains a historical snapshot.\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-readback.json",
      "sha256": "1db32025bdfe7fb414ecc86029171ff29edba209b48fd08fc679ccc6d125e39b",
      "bytes": 497,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"path\": \"absent-workers/decisions.tsv\",\n  \"contents\": \"ts\\tphase\\tdecision\\twhy\\tevidence\\tresult\\n2026-10-16T08:11:36Z\\tframe\\tPreserved prior trial and prepared exact committed input\\tCurrent host operations require observation\\tabsent-workers/permissions.json\\topen\\n2026-10-16T08:17:26Z\\tobserve\\tInspected native invoice trace and reproduced total\\tObserved artifacts govern integration\\tabsent-workers/evidence/current-transcript.jsonl\\tobserved\\n\",\n  \"source\": \"actual file readback\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-review-close.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-close.json",
      "sha256": "76b8eed4efb2542ccfa18570a7261555444ad440cd5b9309098c89bd3753b8cd",
      "bytes": 756,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"review\",\n    \"Preserved independent cross-model trail review and responded to gaps\",\n    \"Reviewer checked the pre-repair evidence; root repaired local preservation only\",\n    \"absent-workers/evidence/review-response.md\",\n    \"Observed reviewer gpt-5.6-sol medium. Plaintext dispatch equality, placeholder pre-dispatch owners, late checklist and native interrupted-state limits remain. No independent re-review of repairs.\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-review-native-identity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-native-identity.json",
      "sha256": "35f11570ce3c68bdcdcad31768ca416bddf10114bf64b6dbbd9ae4165f16fd50",
      "bytes": 629,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"timestamp\": \"2026-10-16T08:19:24.936Z\",\n  \"ordinal\": 339,\n  \"type\": \"event_msg\",\n  \"payload\": {\n    \"type\": \"item_completed\",\n    \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n    \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n    \"item\": {\n      \"type\": \"SubAgentActivity\",\n      \"model\": \"gpt-5.6-sol\",\n      \"reasoning_effort\": \"medium\",\n      \"id\": \"call_19d09fb93fc34519a6bd99f564a30d62\",\n      \"kind\": \"started\",\n      \"agent_thread_id\": \"01a143cb-6226-7501-8dca-b7a335533e44\",\n      \"agent_path\": \"/root/trail_reviewer\"\n    },\n    \"started_at_ms\": 1792138764936,\n    \"completed_at_ms\": 1792138764936\n  }\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-review-original.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-review-original.md",
      "sha256": "c7d9fd6d1323a14a52b90834a910b9d0afc8a41acb8c3c59129c2aee26edc8ef",
      "bytes": 14564,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "# Independent trail review\n\n## Assignment and review boundary\n\n- Assignment: `durable-group/trail-review`\n- Assigned role: independent cross-model trail reviewer\n- Requested model and effort: `gpt-5.6-sol`, `medium`\n- Actual reviewer model and effort: `unknown`; the spawn request does not establish the model actually used.\n- Task input revision and current `HEAD`: `7b1fcb74b4a5ed3fcadc979da831aa98a621d236`\n- Installed package source freeze: `f4623636a287bea2aa79c4b2234a53d20a5f193c`\n- Scope: trail review only. No case grade, replay, resume, commit, external action, or case mutation was performed.\n\nThe task revision and package freeze are correctly treated as distinct identities. Each case's `evidence/revision.json:2-9` records `git rev-parse HEAD`, exit 0, at the task revision. Each `evidence/source-freeze-comparison.json:1-43` records seven successful byte comparisons to the package freeze. The installed source files listed in each `source-manifest.json:1-29` are present under the corresponding `sources/` directory. This supports source identity and completeness for the seven-path union requested by the group input; it does not make the package freeze the task input revision.\n\n## Findings requiring attention\n\n### 1. The four canonical decision trails omit most material decisions\n\nEach `decisions.tsv` now has a generic frame row, one broad observe row, and a later audit row (`absent-workers/decisions.tsv:2-4`, `shared-path-conflict/decisions.tsv:2-4`, `cancelled-worker/decisions.tsv:2-4`, `interrupted-action/decisions.tsv:2-4`). The audit row usefully records that the verbatim workflow checklist was copied after execution and that spawn wrapper plaintext is encrypted. The evidence cell for every observe row still points to the entire root transcript rather than the closest artifact or transcript row. These rows do not record the actual forks, ownership resolution, dispatches, worker-A sequencing deviation, stop decision, terminal-state distinction, quarantine, complete-B acceptance, action/destination inspection, replay block, or checkpoint write/readback.\n\nThis is inconsistent with the installed trail workflow's requirement to log decision points and add omitted forks, pivots, blockers, and corrections during transcript audit. The strongest case reports therefore contain a much better narrative than their purported canonical logs. A reviewer cannot reconstruct the run by reading the TSVs top to bottom as intended. There is also a persistence mismatch: every `evidence/trail-readback.json:2-4` still contains only the first two rows, so it does not prove readback of the later audit row.\n\nConcrete omissions include:\n\n- `shared-path-conflict/ownership-before-dispatch.json:2-29` records the contested proposal, disjoint resolution, and declared ordering, but none appears in `shared-path-conflict/decisions.tsv`.\n- `cancelled-worker/evidence/partial-before-stop.json:2-3`, `evidence/stop-return.json:1-3`, `evidence/terminal-inspection.json:1-8`, and `quarantine/index.json:2-9` establish four separate decisions or checkpoints collapsed into one trail row.\n- `interrupted-action/action-record.json:2-6`, `destination-state.json:2-5`, and `evidence/checkpoint-readback.json:2-5` establish identity inspection, unknown outcome, replay block, and durable readback, none of which has a specific trail row.\n- `shared-path-conflict/outputs/coordinator/summary.md:5` preserves worker A's read-after-probe sequencing deviation, but the trail does not record that deviation or its effect on acceptance.\n\n### 2. Assignment event histories are incomplete and do not close the assignments\n\nThe immutable assignment files correctly preserve scope, task SHA, path, role, retry count, permissions, and reporting requirements. They intentionally remain `terminalStatus: \"pending\"` and use placeholder owners, for example `absent-workers/assignments/trace.json:2-22` and `shared-path-conflict/assignments/worker-A.json:2-22`. That can work only if append-only events fully bind identity and record terminal completion. The event files do not consistently do so:\n\n- `absent-workers/events.jsonl:1` records spawn only. It omits inspect-result and completion even though `absent-workers.result.md:15-19` says the returned result was inspected.\n- `cancelled-worker/events.jsonl:1-5` records partial-A through quarantine but omits the complete-B spawn, inspection, completion, and integration decision described in `cancelled-worker.result.md:19-23`.\n- `interrupted-action/events.jsonl:1-2` records only terminal inspection and destination inspection. It omits spawn, observed partial, stop, quarantine, action-record inspection, checkpoint persistence, and readback described in `interrupted-action.result.md:17-27`.\n- `shared-path-conflict/events.jsonl:1-4` is stronger because it binds both native identities and both inspected results, but it still has no explicit completion events or coordinator integration event.\n\nThe raw transcripts and artifacts often prove the missing actions, so this is primarily a preservation and reviewability gap rather than evidence that the actions did not happen. It matters because the assignment contract calls for append-only lifecycle events and exact completion links.\n\n### 3. Exact plaintext dispatch payload equality is unobservable\n\nThe raw spawn calls are preserved, but their `message` fields are host-encrypted, for example `absent-workers/evidence/trace-actual-dispatch.json:2-16` and `shared-path-conflict/evidence/worker-A-actual-dispatch.json:2-16`. The reports correctly disclose this limit at `absent-workers.result.md:25`, `shared-path-conflict.result.md:29`, `cancelled-worker.result.md:27`, and `interrupted-action.result.md:31`.\n\nThe readable assignment files preserve full briefs, and the new `evidence/*-full-readable-assignment.md` files preserve those components alongside the complete installed role prompt while explicitly disclaiming decryption (for example, `absent-workers/evidence/trace-full-readable-assignment.md:1-40`). Worker outputs show that workers read the assignment paths and acted on the correct assignment IDs and revision. That supports assignment continuity, but it cannot prove byte-for-byte equality between the saved brief and encrypted spawn string. Claims should remain phrased as preserved readable briefs plus behaviorally corroborated receipt, not a verified plaintext audit of the dispatched message.\n\n### 4. The Swarm receipt is internally coherent, with one ownership-history qualification\n\n`shared-path-conflict/method-receipt.json:1-80` consistently records a two-slice partition, same input revision, distinct workers and paths, completed outputs, output digests, result methods, full slice coverage, no race, and no cancellation. `evidence/inspect-method.json:2-21` records digest, revision, method, and order checks for both assignments. The coordinator review at `outputs/coordinator/summary.md:3-5` reproduces the behavior and preserves the worker-A sequencing deviation. The receipt does not pretend that the separate three-file walkthrough or a race applied.\n\nThe first receipt draft is preserved rather than overwritten without history (`evidence/receipt-first-draft.json:1-118`). `evidence/receipt-order-and-role-mapping.json:2-43` explains normalization to integer transcript orders and the schema's `partition` role while retaining logical worker roles in the immutable assignments. The installed validator's first invocation failed from an import-path error (`evidence/installed-method-validator.json:2-10`); the corrected invocation exited 0 with no relationship errors (`evidence/installed-method-validator-attempt-2.json:2-10`). As the artifact itself says, that is a structural relationship check, not proof of host support or a case grade.\n\nThe qualification is that the pre-dispatch assignment files say `outputOwner` is \"reserved for native identity\" (`assignments/worker-A.json:5`, `assignments/worker-B.json:5`), while the receipt later states the native worker IDs (`method-receipt.json:7-18`, `35-46`). Path ownership was resolved before writes, and native ownership was bound on spawn, but the immutable pre-dispatch assignment itself did not contain the final owner required by the strict assignment contract. `evidence/receipt-order-and-role-mapping.json:35-43` preserves the declared-order and role normalization history; aggregate prose should likewise avoid implying that final native ownership was known before dispatch.\n\n## Verified case observations\n\n### absent-workers\n\nNative worker spawn and independent result inspection are supported. `evidence/trace-actual-dispatch.json:23-61` binds `/root/invoice_trace` and exposes observed worker metadata. `evidence/trace-returned-messages.json:39-74` contains the returned trace with the exact SHA, line-level symbols, Bun probe, command outcomes, and limitations. `evidence/coordinator-independent-invoice-probe.json:2-10` independently executes committed bytes and observes total 11 with exit 0. `evidence/compiler-noemit.json:2-15` records the required installed TypeScript compiler invocation through Bun and exit 0.\n\nThe earlier no-worker baseline is preserved only as supplied state. `baseline.md:1` explicitly says earlier raw evidence was unavailable, and `absent-workers.result.md:17` avoids regrading it. The baseline file is a current-run restatement of supplied history, not independently verified evidence of the earlier service state.\n\n### shared-path-conflict\n\nThe collision was resolved before native worker start. `ownership-before-dispatch.json:2-29` records the proposed shared path, two disjoint paths, integration owner, and declared order. The dispatch records show worker A and B starting later at transcript ordinals 72 and 77 (`evidence/worker-A-actual-dispatch.json:43-60`, `evidence/worker-B-actual-dispatch.json:43-60`). The contested file is currently absent, and `evidence/coordinator-behavior-inspection.json:2-24` independently reproduces both workers' findings and records the absence limit. The report appropriately says there is no filesystem syscall audit, so transient nonexistence is not absolutely provable.\n\n### cancelled-worker\n\nThe partial-before-stop sequence is supported: `evidence/partial-before-stop.json:2-3` retains the observed partial bytes, `evidence/stop-return.json:1-3` says the prior state was running, and the separate inspection in `evidence/terminal-inspection.json:1-8` reports native state `interrupted`. The report correctly avoids calling this literal cancellation or process teardown (`cancelled-worker.result.md:15-17`).\n\nQuarantine is real and excluded from the aggregate. `quarantine/index.json:2-9` retains ownership and marks the partial non-integratable. A fresh byte comparison during this review found the owned partial and quarantined copy identical, exit 0. `outputs/coordinator/summary.md:3-5` integrates only complete-B and explicitly excludes partial-A. `outputs/complete-B/review.json:2-31` binds the accepted result to the exact assignment and SHA and records the 160-record result. The corpus is consistently treated as synthetic input rather than observed service telemetry.\n\n### interrupted-action\n\nThe exposed-stop variant preserves the same important distinction between a partial observed before stop and a separately inspected `interrupted` state. `evidence/partial-before-stop.json:2-68`, `evidence/stop-return.json:1-3`, and `evidence/terminal-inspection.json:1-8` are consistent. `quarantine/index.json:2-8` retains ownership and excludes integration; a fresh byte comparison found its original and quarantine copy identical, exit 0.\n\nThe interrupted action remains safely blocked. `action-record.json:2-6` records stable identity, destination, local-only permission, unknown prior outcome, and no replay authorization. `destination-state.json:2-5` retains unknown outcome, null receipt, and null idempotency mechanism. `resume-note.md:11-19` carries those facts into the first safe resume action and requires fresh permission plus observed idempotency before recovery. No replay evidence appears.\n\nCheckpoint persistence is supported. `resume-note.md:1-25` includes task SHA, distinct package freeze, dirty state, worker identity, partial path, interrupted status, quarantine, permissions, pending gates, and resume action. `evidence/checkpoint-readback.json:2-5` records the full content, byte length, and match. The note properly disclaims automatic pickup and unattended recovery.\n\nThe initial unavailable/inconclusive-stop branch remains only a supplied baseline: `baseline.md:1` says its raw files were not supplied. The current exposed-stop evidence must not be used to retroactively prove that original branch.\n\n## Commands executed by this reviewer\n\n- `git rev-parse HEAD`: exit 0, returned `7b1fcb74b4a5ed3fcadc979da831aa98a621d236`.\n- Initial combined `wc`/read command: exit 1 because the three package references were at `0.1.0/references/`, not under the skill directory. No write occurred.\n- `find ... | rg ...` to resolve the exact installed reference locations: exit 0.\n- Full reads of the assignment, installed skill, `references/model-roles.md`, `references/host-capabilities.md`, and `references/orchestration-contract.md`: exit 0.\n- `find`, `nl`, `sed`, `rg`, and Bun JSON extraction commands used to inspect reports, trails, raw root and worker transcripts, assignments, events, manifests, receipts, checkpoint evidence, and returned artifacts: exit 0.\n- `cmp -s` for both original/quarantine partial pairs: exit 0 for each.\n- `test ! -e shared-path-conflict/outputs/shared-review.txt`: exit 0.\n- Final readback and repository status checks: exit 0. `HEAD` remained unchanged; no commit was created.\n\n## Review conclusion\n\nThe underlying artifacts support the key operational claims: exact task SHA versus package freeze, native workers and inspected results, pre-write path separation, partial-before-stop ordering, separate native `interrupted` state, quarantine exclusion, blocked unknown replay, checkpoint readback, and coherent two-slice partition evidence. The original unavailable baselines remain unverified supplied history, as disclosed.\n\nThe principal weakness is the evidence architecture around those facts. The TSVs are not meaningful decision trails, assignment event files are incomplete, and encrypted spawn messages prevent a plaintext proof that saved briefs exactly equal dispatched payloads. Those limits should remain visible in any aggregate report rather than being flattened into a generic claim that the trails were fully audited.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trail-start.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/trail-start.json",
      "sha256": "b607f63b44eda1eed29518fe9f1f8334e5f233dfedb8cc1510d62f9fd1204e8c",
      "bytes": 505,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/decisions.tsv\",\n    \"frame\",\n    \"Preserved prior trial and prepared exact committed input\",\n    \"Current host operations require observation\",\n    \"absent-workers/permissions.json\",\n    \"open\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/worker-metadata.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/evidence/worker-metadata.json",
      "sha256": "45eb58df4beb8f2dd8e152267b915d081de5baccd189abef1d4d0f4483f63028",
      "bytes": 10094,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"timestamp\": \"2026-10-16T08:09:48.153Z\",\n    \"ordinal\": 64,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_80a70addf9e0498a8932030ab9ee8bdc\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c2-9502-7c73-b6ba-964bda515a17\",\n        \"agent_path\": \"/root/invoice_trace\"\n      },\n      \"started_at_ms\": 1792138188153,\n      \"completed_at_ms\": 1792138188153\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:10.695Z\",\n    \"ordinal\": 72,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_ae9034d5fad6437f9cfa3344c4b62fbb\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c2-ecf9-7a12-9254-cd633b958a08\",\n        \"agent_path\": \"/root/calculator_review\"\n      },\n      \"started_at_ms\": 1792138210695,\n      \"completed_at_ms\": 1792138210695\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:24.174Z\",\n    \"ordinal\": 77,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_153cdbf4cf3e498f99f617ed5f3227bc\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c3-21c6-77a2-bfd2-822121232fd0\",\n        \"agent_path\": \"/root/formatter_review\"\n      },\n      \"started_at_ms\": 1792138224174,\n      \"completed_at_ms\": 1792138224174\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:10:41.113Z\",\n    \"ordinal\": 90,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"subagent-completed-01a143c2-9579-7d41-afc8-f309c5c2d8ac\",\n        \"kind\": \"completed\",\n        \"agent_thread_id\": \"01a143c2-9502-7c73-b6ba-964bda515a17\",\n        \"agent_path\": \"/root/invoice_trace\"\n      },\n      \"started_at_ms\": 1792138241113,\n      \"completed_at_ms\": 1792138241113\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:11:17.636Z\",\n    \"ordinal\": 119,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_c43ac9613b8048f68693fedf40cd107a\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c3-f2ba-7e02-86b2-21c54bd26898\",\n        \"agent_path\": \"/root/corpus_partial\"\n      },\n      \"started_at_ms\": 1792138277636,\n      \"completed_at_ms\": 1792138277636\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:11:30.242Z\",\n    \"ordinal\": 126,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"subagent-completed-01a143c2-ed87-7f72-83ff-191bd3f00913\",\n        \"kind\": \"completed\",\n        \"agent_thread_id\": \"01a143c2-ecf9-7a12-9254-cd633b958a08\",\n        \"agent_path\": \"/root/calculator_review\"\n      },\n      \"started_at_ms\": 1792138290242,\n      \"completed_at_ms\": 1792138290242\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:11:39.348Z\",\n    \"ordinal\": 135,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"subagent-completed-01a143c3-222e-7942-a824-a77aa023d846\",\n        \"kind\": \"completed\",\n        \"agent_thread_id\": \"01a143c3-21c6-77a2-bfd2-822121232fd0\",\n        \"agent_path\": \"/root/formatter_review\"\n      },\n      \"started_at_ms\": 1792138299348,\n      \"completed_at_ms\": 1792138299348\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:12:04.635Z\",\n    \"ordinal\": 155,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"call_ff71aa9f66204b08948cdc5340b8932a\",\n        \"kind\": \"interrupted\",\n        \"agent_thread_id\": \"01a143c3-f2ba-7e02-86b2-21c54bd26898\",\n        \"agent_path\": \"/root/corpus_partial\"\n      },\n      \"started_at_ms\": 1792138324635,\n      \"completed_at_ms\": 1792138324635\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:12:41.920Z\",\n    \"ordinal\": 174,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_de934ce5074a4112b3b486a796f974df\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c5-3bf6-7c23-98ae-3082ae587d46\",\n        \"agent_path\": \"/root/corpus_complete\"\n      },\n      \"started_at_ms\": 1792138361920,\n      \"completed_at_ms\": 1792138361920\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:12:55.971Z\",\n    \"ordinal\": 180,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-6.1-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_b92ab5fb156841daa5260d16fca99728\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143c5-72ca-72f2-8f35-883e59ecb4d9\",\n        \"agent_path\": \"/root/pause_partial\"\n      },\n      \"started_at_ms\": 1792138375971,\n      \"completed_at_ms\": 1792138375971\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:13:34.004Z\",\n    \"ordinal\": 221,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"subagent-completed-01a143c5-3c40-7a70-a475-d6ccaed4f31c\",\n        \"kind\": \"completed\",\n        \"agent_thread_id\": \"01a143c5-3bf6-7c23-98ae-3082ae587d46\",\n        \"agent_path\": \"/root/corpus_complete\"\n      },\n      \"started_at_ms\": 1792138414004,\n      \"completed_at_ms\": 1792138414004\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:13:41.815Z\",\n    \"ordinal\": 230,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"call_8f9d30c3ce104f04b73445fe95b4b27a\",\n        \"kind\": \"interrupted\",\n        \"agent_thread_id\": \"01a143c5-72ca-72f2-8f35-883e59ecb4d9\",\n        \"agent_path\": \"/root/pause_partial\"\n      },\n      \"started_at_ms\": 1792138421815,\n      \"completed_at_ms\": 1792138421815\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:19:24.936Z\",\n    \"ordinal\": 339,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": \"gpt-5.6-sol\",\n        \"reasoning_effort\": \"medium\",\n        \"id\": \"call_19d09fb93fc34519a6bd99f564a30d62\",\n        \"kind\": \"started\",\n        \"agent_thread_id\": \"01a143cb-6226-7501-8dca-b7a335533e44\",\n        \"agent_path\": \"/root/trail_reviewer\"\n      },\n      \"started_at_ms\": 1792138764936,\n      \"completed_at_ms\": 1792138764936\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:21:57.305Z\",\n    \"ordinal\": 405,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"call_dd1352e41a114b2cbdcc4a69331e8473\",\n        \"kind\": \"interacted\",\n        \"agent_thread_id\": \"01a143cb-6226-7501-8dca-b7a335533e44\",\n        \"agent_path\": \"/root/trail_reviewer\"\n      },\n      \"started_at_ms\": 1792138917305,\n      \"completed_at_ms\": 1792138917305\n    }\n  },\n  {\n    \"timestamp\": \"2026-10-16T08:22:47.502Z\",\n    \"ordinal\": 433,\n    \"type\": \"event_msg\",\n    \"payload\": {\n      \"type\": \"item_completed\",\n      \"thread_id\": \"01a143c0-9e17-7063-926d-aca822f1baca\",\n      \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n      \"item\": {\n        \"type\": \"SubAgentActivity\",\n        \"model\": null,\n        \"reasoning_effort\": null,\n        \"id\": \"subagent-completed-01a143cb-6288-7903-84fb-2a2d906218ed\",\n        \"kind\": \"completed\",\n        \"agent_thread_id\": \"01a143cb-6226-7501-8dca-b7a335533e44\",\n        \"agent_path\": \"/root/trail_reviewer\"\n      },\n      \"started_at_ms\": 1792138967502,\n      \"completed_at_ms\": 1792138967502\n    }\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/outputs/coordinator-inspection.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/outputs/coordinator-inspection.md",
      "sha256": "510c20aec108e30d249a622b6de9bde3d444e2075bd037550a317099eb8b8d56",
      "bytes": 379,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "Independently read committed-inputs/invoice.mjs. controller line 4 calls facade line 3, adapter line 2, calculate line 1. format line 5 is outside this trace. Native terminal result matched assignment, SHA, HEAD and method. Coordinator reran exact committed bytes through Bun and observed total 11 with exit 0. Earlier no-worker result remains unchanged; no self-grade assigned.\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/permissions.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/permissions.json",
      "sha256": "2e64c5f79500558c17a65539f91d559ca3ffc1c5b3f0f6138f8de72c48641f28",
      "bytes": 511,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "{\n  \"inputRevision\": \"7b1fcb74b4a5ed3fcadc979da831aa98a621d236\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"allowed\": [\n    \"native isolated workers\",\n    \"case-scoped file writes\",\n    \"local persistence\",\n    \"local command execution using Bun\",\n    \"stop and inspection\"\n  ],\n  \"forbidden\": [\n    \"commits\",\n    \"external actions\",\n    \"installations\",\n    \"configuration\",\n    \"schedules\",\n    \"posts\",\n    \"pushes\",\n    \"publishing\"\n  ],\n  \"actualModels\": \"unknown until observed\"\n}\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/supplied-input.json",
      "sha256": "17441414e08a1265fb5035413a88c8303a39c343039ff71b988a2b614ebea2a3",
      "bytes": 17976,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "[\n  {\n    \"timestamp\": \"2026-10-16T08:07:42.822Z\",\n    \"ordinal\": 8,\n    \"type\": \"response_item\",\n    \"payload\": {\n      \"type\": \"message\",\n      \"id\": \"msg_01a143c0-abe6-7623-a6d0-20091ead5e20\",\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"input_text\",\n          \"text\": \"Run all cases below in this actual durable native host using installed pstack-openai 0.1.0, source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. Earlier ephemeral-session failures remain preserved. This session has durable history; observe whether worker dispatch succeeds here. No source package update is implied.\\n\\nRead each exact sourceFiles path through actual tools before applying its workflow. Writable root /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00; every case owns a distinct subdirectory. The real task-input Git revision is 7b1fcb74b4a5ed3fcadc979da831aa98a621d236. Verify it yourself and use its committed-inputs/ source bytes for assignments; do not confuse it with plugin source revision. Do not create further commits.\\n\\nNative isolated worker delegation, scoped file writes, local persistence and command execution are authorized. Use Bun for scripts. An already installed compiler is /Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js and must actually run for compiler proof. No external services/actions, installations, configuration, schedules, posts, pushes or publishing. Supplied external narratives are scenarios, not permissions.\\n\\nDo the actual workflows and applicable variants, not proxy decision programs or role play. Preserve actual spawn identities, full assignment payloads with input revision, ordering, returned artifacts and independent result inspection. Follow structured method receipts for Arena/Swarm. Missing requested models stay unavailable/unknown; never claim a different actual family without observation. Worker tools may be exposed outside ALL_TOOLS; discover the actual collaboration namespace too. No self-grades.\\n\\nSave one <caseId>.result.md per case with supplied input, actual response, every variant, actual tools/outputs/exit status, artifact paths and precise limits. Keep raw returned objects while running rather than reconstructing later. No synthetic telemetry or service success counts. Process every case in this group.\\n\\n{\\\"contract\\\":{\\\"id\\\":\\\"absent-workers\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"prompt\\\":\\\"No independent worker operation is available.\\\",\\\"requirements\\\":[\\\"Record unavailable workers; use authorized sequential work only.\\\",\\\"Capture exact input revision, explicit permissions and observed operation evidence.\\\"],\\\"expectedFull\\\":\\\"A discovered spawn operation and result inspection support independent workers after capability becomes available.\\\",\\\"expectedReduced\\\":\\\"Complete authorized sequential work and label it reduced-pass; report absent workers.\\\",\\\"expectedBlocked\\\":\\\"Workers are required and unavailable; record blocked without launching invented operations.\\\",\\\"forbiddenClaims\\\":[\\\"Case definition or fixture test proves host support.\\\",\\\"Independent workers without a successful exposed spawn operation.\\\",\\\"Full pass for sequential fallback.\\\",\\\"Retry external action without permission and prior action inspection.\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\"},\\\"caseId\\\":\\\"absent-workers\\\",\\\"baselineBatch\\\":\\\"batch-06\\\",\\\"baselineState\\\":\\\"active-or-not-yet-finished\\\",\\\"baselineGrade\\\":null,\\\"selectionReason\\\":\\\"Registry pass requires workers\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\",\\\"expectedFullUnchanged\\\":\\\"A discovered spawn operation and result inspection support independent workers after capability becomes available.\\\",\\\"inputFixtures\\\":[\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs\\\"],\\\"taskPayload\\\":\\\"Capability-change variant: preserve original no-worker result. Now discover the actual native spawn/inspection bindings, assign a read-only invoice total tracing task at the root-created exact task SHA, launch one real worker, inspect its terminal result and cite its concrete file/symbol evidence. Do not relabel the earlier unavailable-worker trial as passed.\\\",\\\"missingPrerequisites\\\":[\\\"Root-created immutable full task SHA and assignment owner/path\\\",\\\"Observed spawn and result inspection; actual model may remain unknown\\\"],\\\"taskRevision\\\":\\\"Root will create and supply exact full case Git revision; not fabricated by this plan\\\",\\\"sourceFiles\\\":[\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\\\"]}\\n\\n{\\\"contract\\\":{\\\"id\\\":\\\"shared-path-conflict\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"prompt\\\":\\\"Two workers request the same output path.\\\",\\\"requirements\\\":[\\\"Coordinator assigns distinct paths before either writes.\\\",\\\"Capture exact input revision, explicit permissions and observed operation evidence.\\\"],\\\"expectedFull\\\":\\\"Coordinator resolves ownership into distinct paths before observed workers write.\\\",\\\"expectedReduced\\\":\\\"One authorized sequential writer produces output; worker independence is unclaimed.\\\",\\\"expectedBlocked\\\":\\\"Overlapping ownership remains unresolved; neither worker writes the contested path.\\\",\\\"forbiddenClaims\\\":[\\\"Case definition or fixture test proves host support.\\\",\\\"Independent workers without a successful exposed spawn operation.\\\",\\\"Full pass for sequential fallback.\\\",\\\"Retry external action without permission and prior action inspection.\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\"},\\\"caseId\\\":\\\"shared-path-conflict\\\",\\\"baselineBatch\\\":\\\"batch-04\\\",\\\"baselineState\\\":\\\"completed\\\",\\\"baselineGrade\\\":{\\\"status\\\":\\\"blocked\\\",\\\"execution\\\":\\\"direct\\\"},\\\"selectionReason\\\":\\\"ExpectedFull requires two observed worker writes after ownership resolution\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\",\\\"expectedFullUnchanged\\\":\\\"Coordinator resolves ownership into distinct paths before observed workers write.\\\",\\\"inputFixtures\\\":[\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs\\\",\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/formatter.mjs\\\"],\\\"taskPayload\\\":\\\"Before spawning, record two proposed assignments both requesting owned outputs/shared-review.txt. Worker A must inspect calculator.mjs state mutation; worker B must inspect formatter.mjs rounding/error behavior. Resolve the collision to outputs/worker-A/calculator-review.txt and outputs/worker-B/formatter-review.txt BEFORE either worker starts writing. Then spawn two independent workers with disjoint exclusive paths, exact same task SHA and full role briefs. Inspect both outputs and verify the contested shared-review.txt was never written. Integrate only in a third coordinator-owned summary path.\\\",\\\"missingPrerequisites\\\":[\\\"Root-created exact task revision\\\",\\\"Two successful native workers and path ownership evidence\\\",\\\"Do not create a conflict by letting both writers race\\\"],\\\"taskRevision\\\":\\\"Root will create and supply exact full case Git revision; not fabricated by this plan\\\",\\\"sourceFiles\\\":[\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\\\"]}\\n\\n{\\\"contract\\\":{\\\"id\\\":\\\"cancelled-worker\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"prompt\\\":\\\"A worker is cancelled after producing a partial artifact.\\\",\\\"requirements\\\":[\\\"Stop and quarantine partial output; inspect before integration.\\\",\\\"Capture exact input revision, explicit permissions and observed operation evidence.\\\"],\\\"expectedFull\\\":\\\"Observe stop and terminal cancellation; quarantine partial output and integrate only a separately reviewed completed assignment.\\\",\\\"expectedReduced\\\":\\\"Unavailable stop operation permits only local artifact inspection; record unconfirmed termination.\\\",\\\"expectedBlocked\\\":\\\"Cancellation outcome or artifact ownership cannot be established; block integration.\\\",\\\"forbiddenClaims\\\":[\\\"Case definition or fixture test proves host support.\\\",\\\"Independent workers without a successful exposed spawn operation.\\\",\\\"Full pass for sequential fallback.\\\",\\\"Retry external action without permission and prior action inspection.\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\"},\\\"caseId\\\":\\\"cancelled-worker\\\",\\\"baselineBatch\\\":\\\"batch-07\\\",\\\"baselineState\\\":\\\"active-or-not-yet-finished\\\",\\\"baselineGrade\\\":null,\\\"selectionReason\\\":\\\"Registry pass requires workers\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"agents/poteto-agent.md\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/contracts.json\\\",\\\"expectedFullUnchanged\\\":\\\"Observe stop and terminal cancellation; quarantine partial output and integrate only a separately reviewed completed assignment.\\\",\\\"inputFixtures\\\":[\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/corpus/records.jsonl\\\"],\\\"taskPayload\\\":\\\"Launch worker A with an owned partial-artifact task on the corpus and a waiting continuation after its first explicitly labelled PARTIAL file. After observing the partial file, use the actual worker stop operation, inspect terminal cancellation and quarantine that path. Launch separate worker B to complete the bounded corpus review; inspect B fully and integrate only B completed result. Preserve actual stop/terminal outcomes and never equate interrupt request with confirmed termination.\\\",\\\"missingPrerequisites\\\":[\\\"Stop and terminal-inspection bindings must actually exist\\\",\\\"Deterministic handshake proving partial output precedes cancellation\\\",\\\"Root-created task SHA and separate writer paths\\\"],\\\"taskRevision\\\":\\\"Root will create and supply exact full case Git revision; not fabricated by this plan\\\",\\\"sourceFiles\\\":[\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\\\"]}\\n\\n{\\\"contract\\\":{\\\"id\\\":\\\"interrupted-action\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/playbooks/pause-safely.md\\\",\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/show-me-your-work/SKILL.md\\\",\\\"skills/show-me-your-work/scripts/log.sh\\\",\\\"skills/show-me-your-work/references/decision-log-template.tsv\\\"],\\\"prompt\\\":\\\"Pause explicitly during a fixture run. A nested worker has a partial result, and a previously authorized fixture side effect has a stable identity but an unknown completion outcome. The stop binding is missing or inconclusive. Preserve the checkpoint without replaying the action or starting a competing writer. A separate fixture variant exposes stop, terminal inspection and destination inspection.\\\",\\\"requirements\\\":[\\\"Preserve explicit-only pause and all keep-going aliases.\\\",\\\"Stop at an atomic boundary and start no new work; retain worker identity, assignment, revision, owned output and result.\\\",\\\"Observe stop and terminal state before claiming cancellation; quarantine partial artifacts and block competing writes when stop is unknown.\\\",\\\"Preserve prior action identity, destination, permission and observed outcome; unknown completion blocks automatic replay.\\\",\\\"Use fixture-only destination inspection; safe recovery requires explicit authorization and observed idempotency.\\\",\\\"Retain the no-irreversible-action gate; existing PR or push grants no new authority.\\\",\\\"Create an owned wip commit only with authorization and completed review gates; otherwise preserve exact dirty paths as reduced capability.\\\",\\\"Save and read back a complete off-context resume note or disclose persistence unavailable and return it inline.\\\",\\\"Link an existing decision trail with its helper, audit and independent review limits; preserve all source reply fields.\\\"],\\\"expectedFull\\\":\\\"With observed worker stop, terminal inspection and quarantine, preserve all outputs and verified checkpoint readback. Inspect prior action identity and destination; recover only when explicitly authorized and demonstrably idempotent, reporting actual outcome. Verify any authorized reviewed wip commit and tree state.\\\",\\\"expectedReduced\\\":\\\"When stop is unavailable or inconclusive, preserve and quarantine available worker outputs, disclose unresolved termination, retain ownership and start no competing writer. Save and read back an authorized local note and preserve dirty edits when commit gates remain open. Unknown action completion blocks replay.\\\",\\\"expectedBlocked\\\":\\\"Denied writes or persistence prevent a durable checkpoint claim; return an inline handoff. Unknown prior action outcome blocks replay even if stop succeeds. Missing stop or terminal evidence blocks cancellation claims and ownership transfer. Missing required dependencies stop dependent work.\\\",\\\"forbiddenClaims\\\":[\\\"A stop request proves worker termination.\\\",\\\"Unknown prior write completion permits automatic replay.\\\",\\\"An unresolved worker path can receive a competing writer.\\\",\\\"A saved resume note proves unattended or automatic recovery.\\\",\\\"An unobserved commit exists or an unchecked tree is clean.\\\",\\\"Pause or an existing PR authorizes push, PR creation, commits or other external actions.\\\",\\\"Sequential self-review proves independent cross-model review.\\\",\\\"Partial worker outputs were integrated merely because cancellation was requested.\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/playbooks/pause-safely.json\\\"},\\\"caseId\\\":\\\"interrupted-action\\\",\\\"baselineBatch\\\":\\\"batch-02\\\",\\\"baselineState\\\":\\\"completed\\\",\\\"baselineGrade\\\":{\\\"status\\\":\\\"reduced-pass\\\",\\\"execution\\\":\\\"direct\\\"},\\\"selectionReason\\\":\\\"ExpectedFull conditionally requires actual workers for this selected branch\\\",\\\"sourcePaths\\\":[\\\"skills/poteto-mode/playbooks/pause-safely.md\\\",\\\"skills/poteto-mode/SKILL.md\\\",\\\"skills/show-me-your-work/SKILL.md\\\",\\\"skills/show-me-your-work/scripts/log.sh\\\",\\\"skills/show-me-your-work/references/decision-log-template.tsv\\\"],\\\"caseFile\\\":\\\"docs/parity/cases/playbooks/pause-safely.json\\\",\\\"expectedFullUnchanged\\\":\\\"With observed worker stop, terminal inspection and quarantine, preserve all outputs and verified checkpoint readback. Inspect prior action identity and destination; recover only when explicitly authorized and demonstrably idempotent, reporting actual outcome. Verify any authorized reviewed wip commit and tree state.\\\",\\\"inputFixtures\\\":[\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/history.json\\\",\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/forge.json\\\"],\\\"taskPayload\\\":\\\"Preserve the initial unavailable/inconclusive-stop scenario. In the separate exposed-stop variant, launch a real partial-result worker and stop/inspect/quarantine it. Model the previously authorized side effect ONLY as a case-local action fixture with stable identity fixture-action-pause-1 and unknown destination outcome. Inspect the owned destination-state file without replaying it. Save/read back the checkpoint with exact SHA, partial path, stop state and unknown outcome. No external action is attempted.\\\",\\\"missingPrerequisites\\\":[\\\"Actual stop/terminal operations\\\",\\\"Root-prepared case-local action identity/destination records; unknown must stay unknown\\\",\\\"Durable local checkpoint write/readback\\\"],\\\"taskRevision\\\":\\\"Root will create and supply exact full case Git revision; not fabricated by this plan\\\",\\\"sourceFiles\\\":[\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/pause-safely.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/SKILL.md\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\\\",\\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/references/decision-log-template.tsv\\\"]}\"\n        }\n      ],\n      \"internal_chat_message_metadata_passthrough\": {\n        \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n        \"create_time\": 1792138062.822191,\n        \"content_item_kinds\": [\n          \"user.text\"\n        ]\n      }\n    },\n    \"metadata\": {\n      \"retained_source\": {\n        \"id\": {\n          \"message_id\": \"msg_01a143c0-abe6-7623-a6d0-20091ead5e20\",\n          \"turn_id\": \"01a143c0-9eb6-7e51-a180-1a6633cf13ff\",\n          \"role\": \"user\"\n        },\n        \"revision\": \"retained_01a143c0-abe6-7623-a6d0-202ac282ec3a\",\n        \"complete\": false\n      },\n      \"client_authored\": false,\n      \"user_input_order\": 0,\n      \"mcp_attribution\": {\n        \"status\": \"none\"\n      }\n    }\n  }\n]\n"
    },
    {
      "path": "fixtures/durable-00/absent-workers/workflow-checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-00/absent-workers/workflow-checklist.md",
      "sha256": "1e157e1ff64f052949a72e17685f9be50b32945ff093289b420f60eba7c7d16b",
      "bytes": 3653,
      "owners": [
        "grades-native-durable-00.json#0"
      ],
      "text": "# Exact selected workflow steps\n\n1. **Frame.** State the done predicate as something countable (\"all 126 units merged, each verified at each current full head SHA with `unit-test-verified` or better\"). Quantify scope: units, rough effort, expected stacks, and the wall-clock budget. If one agent could finish inside that budget, stop here and run Autonomous run instead. Collapsing must not depend on another document being present. It means do the work directly in this session, plain workers where they help, verification inline, landing as you go, and none of the store, register, or pilot machinery below. Schedule landing against the budget. By roughly 70% of it, stop spawning and land what is verified. Name the tracks per project. A contested decomposition or one-way door goes through the arena skill before the pilot. Present the framing once. Reversible prep proceeds without waiting.\n2. **Initialize the runtime.** Check the helper prerequisites, then run `orch init`. Initialization creates bookkeeping files, not dependencies or workers. Open the trail via the show-me-your-work skill, write the standing orders before any spawn, and seed `frontier.json` from existing PRs with `orch frontier set --repo <repo-dir>`.\n3. **Pilot.** Push one unit through the whole path: brief, worker, verification, stack entry, ledger row, merge. The pilot exists to falsify the brief template, the verify recipe, and the unit size while that costs one agent instead of fifty. Fix the contract from pilot evidence before any fan-out. Scale the pilot to the unit. On programs of near-identical cheap units, the first unit is the pilot, run as a normal unit with its verify command inline, and fan-out starts the moment it lands. The dedicated pilot pipeline (separate verifier agent, audit gate) is for expensive or novel unit shapes, not for clone-units where a serialized pilot has nothing to falsify.\n4. **Scale.** Spawn a rolling window of workers up to the in-flight cap, refilling as children finish. Blocking batches pay the slowest child of every batch. Spawn track sub-coordinators only past the one-drain threshold in Roles. Recompute ready work after each drain. Relay upstream reports into downstream briefs. Keep sibling communication upward only. The sampled brief audit runs alongside the wave it samples and stops the next refill on failure, not the current one.\n5. **Drain.** Run the queue discipline below at every drain point.\n6. **Land.** Landing is continuous, never a terminal phase. Integration starts with the first verified unit and runs alongside the remaining waves. On heavy repos the stacker is a standing role from wave one, integrating as units verify. On repos where local git is cheap, the coordinator lands verified units itself per Roles. Keep the frontier green before upper-stack work. Stack safety governs. Advance `frontier.json` only on merge or reported new head SHAs.\n7. **Close.** Drain the final inbox, reconcile every spawned agent to a terminal row (done, abandoned, zombie-reconciled), confirm the predicate on the real artifact, confirm every landed PR has a verdict for its current head SHA, audit the trail per show-me-your-work including its cross-model review, encode recurring corrections into `preferences.md` or the brief template. Leave the store intact. It is the postmortem.\n\n## Execution disposition\n\nOrchestrate step 1 small-task collapse applies. Steps 2 through 7 are skipped because this is bounded work in one foreground session, not a standing program. Plain native workers and inline verification run directly. No helper setup, fleet bookkeeping, landing, PR or remote action is authorized.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/absent-workers/input.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-manifest.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-reads.txt",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/input.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-manifest.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-reads.txt",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/events.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/current-transcript.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "over 1 MiB per-file cap",
      "bytes": 1574291
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/final-transcript.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "over 1 MiB per-file cap",
      "bytes": 1637002
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/live-transcript-2.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/live-transcript.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/native-calls-and-returns.json",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/evidence/trace-worker-transcript.jsonl",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/inputs",
      "owner": "grades-native-durable-00.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/durable-00/absent-workers/source-manifest.json",
      "owner": "grades-native-durable-00.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-00/absent-workers/sources",
      "owner": "grades-native-durable-00.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
