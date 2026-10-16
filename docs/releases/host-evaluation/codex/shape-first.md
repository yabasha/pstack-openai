# codex: shape-first

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "shape-first",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-04.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.",
  "caseDefinition": {
    "id": "shape-first",
    "sourcePaths": [
      "skills/principle-foundational-thinking/SKILL.md"
    ],
    "prompt": "Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.",
    "requirements": [
      "Identify core types, data shape, dominant access patterns and ownership before writing logic.",
      "Ask what happens when another actor modifies shared state concurrently; isolate state when the answer is not nothing.",
      "Remove dead code before foundations; sequence shared types, CI, linting and test infrastructure before features, and tests before fixes.",
      "Converge types and data models, prefer explicit code, avoid premature abstractions, and test behavior and edge cases.",
      "Keep increments coherent and commits small and single-purpose; do not distribute a capability as special-case caller coordination.",
      "Source inspection, authorized writes and observed execution are needed for implementation and verification."
    ],
    "expectedFull": "Identify job identity, state and ownership before queue logic. Trace enqueue, claim, completion and state-list access patterns; choose structures for those paths and isolate concurrently mutable state. Remove dead code first, sequence useful infrastructure before features, and test behavior and edge cases. Report actual edits and checks.",
    "expectedReduced": "With supplied source but unavailable writes or execution, provide a concrete shape, ownership and sequencing proposal. Label reduced capability and list edits and checks not performed.",
    "expectedBlocked": "If required source or access patterns are unavailable, state the missing inputs and stop implementation claims. Any provisional design must identify its assumptions.",
    "forbiddenClaims": [
      "Core data or ownership can be deferred until after logic.",
      "Shared mutable state is safe without considering concurrent actors.",
      "Edits, tests or commits completed without observed authorized operations.",
      "Structural validation proves host behavioral parity."
    ],
    "caseFile": "docs/parity/cases/skills/principle-foundational-thinking.json"
  },
  "registry": {
    "caseId": "shape-first",
    "caseFile": "docs/parity/cases/skills/principle-foundational-thinking.json",
    "sourcePaths": [
      "skills/principle-foundational-thinking/SKILL.md"
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
        "review-outcome"
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
      "pass": [],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-04.json#6",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "shape-first",
      "status": "blocked",
      "grade": {
        "caseId": "shape-first",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_12",
          "item_19"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Real shared queue/source/storage ownership and implementation target absent."
        ],
        "review": "Concrete provisional queue shape/access/ownership proposal, but no actual queue/storage source or deployment contract exists. No implementation/tests run. Capability exists; cannot silently classify source gap as unavailable execution.",
        "responseArtifact": "fixtures/batch-04/shape-first.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [
          "Supply missing concrete inputs and rerun. Fixture incompleteness is not a skill source defect."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-04.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Identify job identity, state and ownership before queue logic. Trace enqueue, claim, completion and state-list access patterns; choose structures for those paths and isolate concurrently mutable state. Remove dead code first, sequence useful infrastructure before features, and test behavior and edge cases. Report actual edits and checks.",
        "reducedExpected": "With supplied source but unavailable writes or execution, provide a concrete shape, ownership and sequencing proposal. Label reduced capability and list edits and checks not performed."
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Baseline case definitions used, with corrected full observation contracts for uncertain-result/shared-path-conflict.",
          "Native raw command events and saved outputs reviewed; model check-script assertions are not workflow grades.",
          "Worker tools exposed does not establish success. Missing assignment prerequisites is not absent tool or startup failure.",
          "Proxy local payment/recovery behavior never establishes service execution.",
          "OS process concurrency is appropriate for two-writers case and is not AI-worker independence."
        ]
      },
      "response": {
        "text": "# shape-first\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"shape-first\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-foundational-thinking/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.\",\n  \"requirements\": [\n    \"Identify core types, data shape, dominant access patterns and ownership before writing logic.\",\n    \"Ask what happens when another actor modifies shared state concurrently; isolate state when the answer is not nothing.\",\n    \"Remove dead code before foundations; sequence shared types, CI, linting and test infrastructure before features, and tests before fixes.\",\n    \"Converge types and data models, prefer explicit code, avoid premature abstractions, and test behavior and edge cases.\",\n    \"Keep increments coherent and commits small and single-purpose; do not distribute a capability as special-case caller coordination.\",\n    \"Source inspection, authorized writes and observed execution are needed for implementation and verification.\"\n  ]\n}\n```\n\n## Actual response and output\n\nFoundational Thinking changed the deliverable into data, access patterns and ownership before queue logic. The actual provisional design is [design.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/design.md). It defines immutable deduplicated submissions, a tagged job-state model, attempt identities, lease fences, atomic claim and completion ownership, status indexes and snapshot reads.\n\nIndependent submissions and worker attempt records use separate ownership. The canonical claim transition is genuinely shared, so one queue module owns it through an atomic storage transaction or a single queue owner. Two workers must never coordinate claims through separate caller-side read-and-write sequences. The design describes how a stale worker's fence fails after reclamation.\n\nThe sequence is dead-code inspection before shared types, lint and test infrastructure before features, behavioral tests before implementation, then coherent enqueue/claim/completion/reader increments. Proposed checks cover duplicate submissions, simultaneous claims, stale leases, fencing, retry completion, empty and delayed jobs and readers during transitions. No commits or CI changes were made.\n\nSource discovery inspected the available fixture inventory and searched queue-related terms. The source contains cache queueMicrotask usage and unrelated synthetic status aliases, but no shared job-queue implementation or storage/deployment contract. The search also traversed synthetic shared history and corpus fixtures; those incidental matches were not used as queue design evidence. This is a source gap, not a denied execution capability.\n\nOnly the principle/source reads, discovery command and design save/readback were actually performed. No queue implementation, test execution, lint, type-check, concurrency test or storage check is claimed. The design remains provisional until the real source and storage contract are available.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/.\n\n\nCommand: `rg -n queue|enqueue|claim|sourceRevision|imbalance /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared`. Exit 0. Full receipt: [queue-discovery.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/queue-discovery.receipt.json).\n\nOutput is retained without truncation in the linked receipt.\n\n\n## Variants and limits\n\nProvisional data and ownership design saved after source inspection. No queue source or storage contract was available, so feature implementation and verification remain blocked rather than simulated as complete.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/shape-first.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first.result.md",
          "sha256": "680b4929435da8486ac166a27d7230346ccc6f2c1644e58e5385e1db4a5f7115",
          "bytes": 5718
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-04.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-04.events.jsonl",
            "sha256": "614c212bfe1cb1201ad58cdd814f4bcd05080cd9c2ba5fc9f09a7127c3730143",
            "bytes": 382761,
            "eventReferences": [
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1f2e8bdcc8604989787ac3ee28840dfed3d703a8ffd8398732282508f5db08ae"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "467beb11dce6fdb184fe61496efe374f22d7816ff1734110c9bacbc4b69be271",
                "commandResult": {
                  "exitCode": 128
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "034ef504598ef9a3e9fc53b89295cca14edf990ee9b7c70b2fcc207694ae8e59"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "17a56f51a91f3757b32260b9b516167601c47e6a1597f4edac9a8ad7c566074c",
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
            "item_12",
            "item_19"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-04.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-04/shape-first/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/design.md",
      "sha256": "6401d787239dbcf7300db6c7cb712706ebb25dafcbe710383cc858e2afcf1f59",
      "bytes": 4283,
      "owners": [
        "grades-native-04.json#6"
      ],
      "text": "# Shared job queue before logic\n\nThis is a provisional design. The supplied files contain no queue implementation, storage contract, deployment topology, throughput requirement, or existing queue tests. The inspected queueMicrotask call belongs to cache teardown. It does not establish a job queue.\n\n## Data and ownership\n\nJob identity is stable across enqueue retries. An immutable submission contains jobId, producerId, producerKey, kind, payload, payloadVersion and creation time. A unique producerId and producerKey pair rejects duplicate submissions with different payloads.\n\nJob state is a tagged union. A queued job has availableAt. A running job has workerId, attemptId, leaseUntil and a monotonically increasing fence. A completed job has a result reference and completion time. A failed job has a bounded error record and failure time. Lease fields exist only on running jobs. Keep payloads and large results out of hot state indexes.\n\nProducers own separate immutable submissions, each worker owns its attempt records, and the status reader owns no queue writes. One queue module owns authoritative state transitions. Independent output files and attempt records remain separate. Claims require one canonical state, so enforce that invariant through a transaction or a single queue owner, rather than locks scattered through callers.\n\nWhat if another worker claims the same job concurrently? A read followed by an ordinary update can assign both workers. The queue owner must atomically select and transition one eligible job, returning a fresh fence. Completion compares jobId, attemptId and fence in the same transaction. A stale worker cannot complete a reclaimed job. A reader uses a consistent snapshot and never rewrites state.\n\n## Access patterns\n\n| Actor | Access | Organizing structure |\n| --- | --- | --- |\n| Producer | Deduplicate and enqueue | Unique producerId plus producerKey, primary jobId |\n| Worker | Claim earliest eligible job | Index on state, availableAt, creation time and jobId, atomic transition |\n| Worker | Renew or complete its claim | Primary jobId with expected running state, attemptId and fence |\n| Recovery owner | Reclaim expired leases | Index on running state and leaseUntil, increment fence atomically |\n| Status reader | List by state | Index on state, creation time and jobId, cursor pagination |\n\nWhether separate priority or tenant indexes are needed remains unknown. Use the simplest storage transaction that fits the actual deployment. A single-host SQLite transaction and a distributed database transaction are different deployment choices. Neither has been tested here.\n\nDelivery is at least once. Job fencing protects queue state, not payment side effects. External actions need their own stable identity, permission, destination inspection and supported idempotency mechanism. An unknown outcome blocks automatic resend.\n\n## Work sequence\n\n1. Obtain the queue source, deployment contract and acceptance inputs. Audit and remove demonstrably dead queue code first. Nothing was deleted because none was supplied.\n2. Define shared submission and tagged state types, transition ownership and storage constraints. Keep this a coherent local unit.\n3. Establish the existing lint, type-check and test commands. Propose CI wiring for review. This evaluation does not authorize configuration changes or commits.\n4. Write behavioral checks before fixes or implementation. Cover duplicate enqueue with equal and conflicting payloads, two simultaneous claims, empty queue, future availability, stale lease completion, wrong fence, renewal racing reclaim, repeated completion, invalid transitions and snapshot pagination during concurrent transitions.\n5. Implement enqueue and atomic claim through the queue module. Verify the preceding tests on real storage before adding completion and lease recovery.\n6. Add completion, renewal and status reads as coherent increments. Verify each before the next. Keep any future authorized commits small and single-purpose.\n\nNo queue feature, CI setting, type-check, concurrent claim test or storage test was run. The actual checks here were source discovery, reading the requested principle and saving this design with readback. Missing source blocks implementation and verified concurrency claims.\n"
    },
    {
      "path": "fixtures/batch-04/shape-first/queue-discovery.receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/queue-discovery.receipt.json",
      "sha256": "7a4d03ba4e801af22ae361b5e9c1645fc2679aadfe4fe573787f2ee105c0c407",
      "bytes": 22497,
      "owners": [
        "grades-native-04.json#6"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"queue|enqueue|claim|sourceRevision|imbalance\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first\",\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/cache/vendor/disposer-v1.mjs:3:  return { dispose: () => queueMicrotask(onDispose) };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js:22:var aliases = { queued: \\\"waiting\\\", running: \\\"active\\\", completed: \\\"done\\\" };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js:23:var statuses = [\\\"queued\\\", \\\"running\\\", \\\"completed\\\"];\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/history/shared-records.json:3:  \\\"retryDecision\\\":{\\\"codeRecord\\\":\\\"Retry threshold changed from 2 to 3 in supplied narrative; no commit supplied\\\", \\\"ticketRecord\\\":\\\"Fixture ticket requests three attempts for intermittent upstream failures\\\", \\\"telemetry\\\":\\\"not supplied; no quantitative correlation can be claimed\\\", \\\"chat\\\":\\\"unavailable\\\"},\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:1:{\\\"record\\\":1,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:5:{\\\"record\\\":5,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:9:{\\\"record\\\":9,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:13:{\\\"record\\\":13,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:17:{\\\"record\\\":17,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:21:{\\\"record\\\":21,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:25:{\\\"record\\\":25,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:29:{\\\"record\\\":29,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:33:{\\\"record\\\":33,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:37:{\\\"record\\\":37,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:41:{\\\"record\\\":41,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:45:{\\\"record\\\":45,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:49:{\\\"record\\\":49,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:53:{\\\"record\\\":53,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:57:{\\\"record\\\":57,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:61:{\\\"record\\\":61,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:65:{\\\"record\\\":65,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:69:{\\\"record\\\":69,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:73:{\\\"record\\\":73,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:77:{\\\"record\\\":77,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:81:{\\\"record\\\":81,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:85:{\\\"record\\\":85,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:89:{\\\"record\\\":89,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:93:{\\\"record\\\":93,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:97:{\\\"record\\\":97,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:101:{\\\"record\\\":101,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:105:{\\\"record\\\":105,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:109:{\\\"record\\\":109,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:113:{\\\"record\\\":113,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:117:{\\\"record\\\":117,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:121:{\\\"record\\\":121,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:125:{\\\"record\\\":125,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:129:{\\\"record\\\":129,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:133:{\\\"record\\\":133,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:137:{\\\"record\\\":137,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:141:{\\\"record\\\":141,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:145:{\\\"record\\\":145,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:149:{\\\"record\\\":149,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:153:{\\\"record\\\":153,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/corpus/records.jsonl:157:{\\\"record\\\":157,\\\"source\\\":\\\"synthetic corpus input\\\",\\\"topic\\\":\\\"cache\\\",\\\"body\\\":\\\"Disposal is queued in a microtask; invalidation removes shared state synchronously. Inspect timing before asserting safety.\\\",\\\"detail\\\":\\\"This repeated text is an input for bounded extraction, not an observed log or independent evidence.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/empty-function/subject.mjs:7:export const aliases = { queued: 'waiting', running: 'active', completed: 'done' };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/empty-function/subject.mjs:8:export const statuses = ['queued', 'running', 'completed'];\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/history/history.json:8:    {\\\"id\\\":\\\"fixture-event-04\\\",\\\"role\\\":\\\"assistant\\\",\\\"text\\\":\\\"The cache change is shipped. This was an incorrect unsupported claim in the fixture.\\\"},\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/history/history.json:10:    {\\\"id\\\":\\\"fixture-event-06\\\",\\\"role\\\":\\\"assistant\\\",\\\"text\\\":\\\"I repeated the same unsupported shipped claim. This is the second fixture occurrence.\\\"},\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional/history/history.json:11:    {\\\"id\\\":\\\"fixture-event-07\\\",\\\"role\\\":\\\"user\\\",\\\"text\\\":\\\"Keep status claims tied to observed artifacts. Preserve the Bun preference.\\\"}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/README.md:5:empty-function contains all five requested weak test shapes, plus table-relation and compile-time exceptions. The task is to repair or remove the weaknesses and observe the empty-function mutation failing after repair. Neither a repaired test nor mutation result is pre-supplied. caller-migration and dead-path now include actual baseline behavior tests, explicit applicability decisions and concrete acceptance inputs. Baseline tests are supplied, not claimed to have run. Only source-loadability checks are performed by fixture preparation.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js:22:var aliases = { queued: \\\"waiting\\\", running: \\\"active\\\", completed: \\\"done\\\" };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js:23:var statuses = [\\\"queued\\\", \\\"running\\\", \\\"completed\\\"];\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js:19:var aliases = { queued: \\\"waiting\\\", running: \\\"active\\\", completed: \\\"done\\\" };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js:20:var statuses = [\\\"queued\\\", \\\"running\\\", \\\"completed\\\"];\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-04/shape-first/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/readback.json",
      "sha256": "d0e3360453f8e117b71a7d5cbae606ba8d372f2b88332977e2db544ada9c516d",
      "bytes": 482,
      "owners": [
        "grades-native-04.json#6"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first.result.md\",\n  \"sha256\": \"680b4929435da8486ac166a27d7230346ccc6f2c1644e58e5385e1db4a5f7115\",\n  \"readbackMatched\": true,\n  \"persisted\": [\n    {\n      \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/design.md\",\n      \"sha256\": \"6401d787239dbcf7300db6c7cb712706ebb25dafcbe710383cc858e2afcf1f59\",\n      \"bytes\": 4283\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/shape-first.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first.result.md",
      "sha256": "680b4929435da8486ac166a27d7230346ccc6f2c1644e58e5385e1db4a5f7115",
      "bytes": 5718,
      "owners": [
        "grades-native-04.json#6"
      ],
      "text": "# shape-first\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"shape-first\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-foundational-thinking/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.\",\n  \"requirements\": [\n    \"Identify core types, data shape, dominant access patterns and ownership before writing logic.\",\n    \"Ask what happens when another actor modifies shared state concurrently; isolate state when the answer is not nothing.\",\n    \"Remove dead code before foundations; sequence shared types, CI, linting and test infrastructure before features, and tests before fixes.\",\n    \"Converge types and data models, prefer explicit code, avoid premature abstractions, and test behavior and edge cases.\",\n    \"Keep increments coherent and commits small and single-purpose; do not distribute a capability as special-case caller coordination.\",\n    \"Source inspection, authorized writes and observed execution are needed for implementation and verification.\"\n  ]\n}\n```\n\n## Actual response and output\n\nFoundational Thinking changed the deliverable into data, access patterns and ownership before queue logic. The actual provisional design is [design.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/design.md). It defines immutable deduplicated submissions, a tagged job-state model, attempt identities, lease fences, atomic claim and completion ownership, status indexes and snapshot reads.\n\nIndependent submissions and worker attempt records use separate ownership. The canonical claim transition is genuinely shared, so one queue module owns it through an atomic storage transaction or a single queue owner. Two workers must never coordinate claims through separate caller-side read-and-write sequences. The design describes how a stale worker's fence fails after reclamation.\n\nThe sequence is dead-code inspection before shared types, lint and test infrastructure before features, behavioral tests before implementation, then coherent enqueue/claim/completion/reader increments. Proposed checks cover duplicate submissions, simultaneous claims, stale leases, fencing, retry completion, empty and delayed jobs and readers during transitions. No commits or CI changes were made.\n\nSource discovery inspected the available fixture inventory and searched queue-related terms. The source contains cache queueMicrotask usage and unrelated synthetic status aliases, but no shared job-queue implementation or storage/deployment contract. The search also traversed synthetic shared history and corpus fixtures; those incidental matches were not used as queue design evidence. This is a source gap, not a denied execution capability.\n\nOnly the principle/source reads, discovery command and design save/readback were actually performed. No queue implementation, test execution, lint, type-check, concurrency test or storage check is claimed. The design remains provisional until the real source and storage contract are available.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/.\n\n\nCommand: `rg -n queue|enqueue|claim|sourceRevision|imbalance /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/../shared`. Exit 0. Full receipt: [queue-discovery.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shape-first/queue-discovery.receipt.json).\n\nOutput is retained without truncation in the linked receipt.\n\n\n## Variants and limits\n\nProvisional data and ownership design saved after source inspection. No queue source or storage contract was available, so feature implementation and verification remain blocked rather than simulated as complete.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/shape-first/additional-source-reads.json",
      "owner": "grades-native-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shape-first/fixture-README.md",
      "owner": "grades-native-04.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/shape-first/input.json",
      "owner": "grades-native-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shape-first/source-manifest.json",
      "owner": "grades-native-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shape-first/additional-source-reads.json",
      "owner": "grades-native-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shape-first/fixture-README.md",
      "owner": "grades-native-04.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/shape-first/input.json",
      "owner": "grades-native-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shape-first/source-manifest.json",
      "owner": "grades-native-04.json#6",
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
