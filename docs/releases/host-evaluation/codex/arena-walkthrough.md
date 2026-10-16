# codex: arena-walkthrough

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "arena-walkthrough",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-06.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.",
  "caseDefinition": {
    "id": "arena-walkthrough",
    "sourcePaths": [
      "skills/arena/SKILL.md"
    ],
    "prompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.",
      "Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge."
    ],
    "expectedFull": "Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.",
    "expectedReduced": "Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.",
    "expectedBlocked": "Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.",
    "forbiddenClaims": [
      "Links or direct source reads prove installed discovery.",
      "Sequential roles are independent workers.",
      "An isolated helper snapshot proves this candidate or host passed.",
      "A resolution file, owner marker or upstream autonomy grants approval.",
      "Apply automatically accepts an update or refreshes a host."
    ],
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json"
  },
  "registry": {
    "caseId": "arena-walkthrough",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
    "sourcePaths": [
      "skills/arena/SKILL.md"
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    },
    "requiredMethod": "arena"
  },
  "attempts": [
    {
      "attemptId": "grades-native-06.json#6",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "arena-walkthrough",
      "status": "reduced-pass",
      "grade": {
        "caseId": "arena-walkthrough",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_13",
          "item_20",
          "item_28",
          "item_33"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Exact task Git input revision absent.",
          "Pre-dispatch immutable assignment events/full structured receipt absent."
        ],
        "review": "Reads README→Arena and uses two actual fresh candidate outputs and later judge, then selects/grafts and inspects synthesis. Initial inherited launch failure followed successful fresh contexts, not absent tool. Missing taskSHA/pre-dispatch event method receipt prevents full despite useful native comparison.",
        "responseArtifact": "fixtures/batch-06/arena-walkthrough.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.",
        "reducedExpected": "Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.",
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
        "text": "# arena-walkthrough\n\n## Supplied input\n\n> Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\n\nNamed source files and exact copied source bytes are retained in [arena-walkthrough/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-manifest.json) and [arena-walkthrough/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Navigation, frame and capability decisions\n\nRead installed README. It links docs/workflows/arena.md and that destination exists and was fully read. Read Arena and its capability, model-role, assignment and ownership contracts plus applied leaves. Source reads establish navigation, not a registered /arena command or installed-discovery pass. Installed package is visibly listed in this host's skill catalog, but source invocation was manual and no host registration command was tested.\n\nA local six-phase checklist replaces an unavailable todo operation. task.md requests two Markdown cache API proposals. The parent-only rubric has five criteria, caller clarity, state ownership, teardown correctness, failure handling and extension cost. Candidates did not receive the rubric. Frozen fixture input-manifest.json hashes to7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43. No exact task Git SHA exists. This missing concrete prerequisite prevents a full assignment-contract run; isolated comparison proceeds with that explicit reduction.\n\n## Fan out and inspect\n\nCandidate A's inherited-context spawn failed with invalid thread-store/no rollout. The actual error is preserved in worker-events.json. A fresh fork_turns none attempt under arena-a-v1 retry1 returned /root/arena_a_retry and produced a/proposal.md. Candidate B, /root/arena_b under arena-b-v1 retry0, produced b/proposal.md. Their outputs are disjoint and both were read end to end. SHA256 values are4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e and366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b.\n\nWorker requests inherited model/effort. Observed model and effort are unknown. No cloud-placement or diversity claim. Actual workers wrote only their assigned proposals according to inspected files and returns; no OS-enforced per-worker sandbox is claimed. Append-only immutable pre-dispatch assignment events were not fully persisted before dispatch, so later coordinator event transcription is not a complete structured method receipt.\n\n## Cross-judge, pick and graft\n\nOnly after both terminal candidates and full artifacts were inspected, fresh read-only /root/arena_judge received candidates plus rubric. judge.md retains its result and independently checked artifact hashes. Parent criterion scores match the judge, A2/2/2/1/2 and B2/2/2/2/2. These are proposal comparison scores, not host case grades. Choose B because it defines closed-before-disposal and owned invalidation in finally. Graft A staged migration, optional-chaining warning and deferred-error policy. Reject scheduling-dependent lifetime, raw-key consumer invalidation, placeholders and unjustified reference counts. Both converge on generation handles; the graft keeps one model.\n\n## Verify and actual output\n\nsynthesis.md is the resulting cache API proposal; synthesis-note.md records base, grafts, rejections and inspection. verification.json retains hashes and bounded parent textual review aids. The parent reviewed the real caller/vendor path and reproduced after-state failure and before-state completion in command-results.json. API implementation and proposed future regression checks did not run. Prove It Works changed the verification from trusting worker summaries to reading artifacts and actual probe output. Separate Before Serializing Shared State changed candidate ownership to disjoint paths. Laziness Protocol rejected reference counting. Redesign From First Principles kept ownership coherent. Unslop was applied to synthesis prose.\n\nSix phases were exercised with native candidates and a fresh judge. Exact task Git SHA, observed model diversity and a full structured method receipt remain unmet. A source read or local text assertion is not evidence those gates passed. No dependency, settings, Git history or external action was changed.\n",
        "artifact": {
          "path": "fixtures/batch-06/arena-walkthrough.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough.result.md",
          "sha256": "a80484ae5850eccc0940c33b3bc99c0dd10574911c55635575e4f7ce0c58a13c",
          "bytes": 6019
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
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "067f64069a80d6bee7ae8fdc112f1eea7455c1a4f54059494a780082448eec31"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c12abe4f5d18352075fa27322540432154741adccfe652ee2aa9d4abbdb6f8d4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2e4adcfd8b33b29e8507ed6a18a5c3a631eab90e0ec6aac17ca8f441a2815f2b"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d334f54d4bfc726c80daf9c513ab237a570be5e8d9d1d48810140dcac6251519",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 52,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f95634a991bdf83a520d38029a33cffd5c0c1d25553b2c7b58c0de0780830db8"
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "897622be432f98a936806993bfadfeaf44ae238d2155a8b6f7be5292d6d44677",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_33",
                "line": 60,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "353993c230c9b434d1046ae45f631f6084edf7f0aca8dd85ebdec20b93d227ca"
              },
              {
                "eventId": "item_33",
                "line": 61,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8fa578ef231b70734b6c4fbaa3d3be0e900ac49b4552e533139f7f5a3ab426ff",
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
            "item_13",
            "item_20",
            "item_28",
            "item_33"
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
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/arena-walkthrough/a/proposal.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/a/proposal.md",
      "sha256": "4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e",
      "bytes": 7313,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache ownership and teardown proposal\n\nRecommend synchronous invalidation, with teardown callbacks retaining the value they own. Add an entry handle returned by `put` so a consumer can remove only its own entry. A cache lookup is a point-in-time lookup, not a lifetime guarantee.\n\n## Observed failure\n\nThe supplied after-state deletes an entry synchronously. In `caller.mjs`, unmount calls `subscription.dispose()` and then `invalidate(key)`. The exact vendored disposer schedules `onDispose` with `queueMicrotask` and returns immediately. The callback therefore runs after deletion and `get(key).ready` dereferences undefined.\n\nI ran `bun arena-walkthrough/input/probe.mjs` against the supplied files. It exited 1 and printed:\n\n    teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\n\nThe removed timer previously deferred deletion until after the disposal microtask. That ordering explains why this caller depended on the old behavior. I did not execute a restored before-state, so that comparison is based on source inspection. The local vendor file SHA256 matches `manifest.json`: `d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f`. This evidence concerns fixture-v1 only and establishes no public package behavior.\n\n## Proposed API contract\n\n| Operation | Contract |\n| --- | --- |\n| `put(key, value)` | Replace the current lookup entry and return an owned entry handle. Each put creates a fresh identity, even for the same value. |\n| `get(key)` | Return the current value or undefined. Missing entries are ordinary misses. The result grants no guarantee about later lookups. |\n| `handle.value` | Retain the exact value passed to this put, independent of lookup replacement or invalidation. |\n| `handle.invalidate()` | Immediately remove the lookup entry only if this handle is still current for its key. Return whether removal occurred. Repeated calls are harmless. |\n| `invalidate(key)` | Immediately remove whatever entry currently occupies the key and return whether removal occurred. Reserve this operation for code intentionally invalidating the current entry regardless of owner. |\n\nThe cache owns lookup membership. The consumer owns its subscription and the value reference needed during teardown. Removing an entry does not dispose subscriptions or mutate the value. A handle retains its value while consumers retain the handle. This proposal assumes ordinary JavaScript values as in the fixture; resource disposal requires a separate contract.\n\nFor `mount`, retain the handle returned by `put`. The disposal callback reports `handle.value.ready` instead of performing `get(key).ready`. Unmount schedules disposal once and invalidates through that handle. Guard unmount so repeated calls cannot queue duplicate reports. The pinned disposer itself does not provide idempotence.\n\nThis also handles overlapping mounts using the same key. If mount A is replaced by mount B before A unmounts, A reports its own value and its handle cannot delete B. A raw key-based invalidation would still delete B after fixing the missing lookup alone.\n\nThe retained reference is not a deep snapshot. Mutations to that object remain visible. If consumers require the final value of another owner instead, that is a different requirement and needs an explicit handoff. The fixture supplies no such requirement.\n\n## Errors and completion\n\nDo not turn the failed lookup into an optional-chain expression. That would suppress the exception while changing the report from true to undefined.\n\nCache operations contain no user callbacks. A missing or replaced entry makes `handle.invalidate()` return false. Define this as a normal result, not an error. Value validation belongs with the caller that understands `ready`.\n\nA report callback can still throw. Under the supplied disposer, that exception escapes from a microtask; a try/catch around unmount cannot catch it. Catch and route report failures inside the deferred callback through the application's existing error policy, or explicitly document uncaught callback errors if that is the policy. Do not claim that unmount reports asynchronous errors synchronously.\n\nKeep unmount synchronous for this migration and document that it schedules teardown but does not signal its completion. The vendor supplies no completion promise. If a future consumer must await disposal, introduce an adapter that observes callback completion and rejection, then expose an explicit asynchronous teardown contract. Merely awaiting `dispose()` would not provide that guarantee.\n\n## Alternatives rejected\n\n| Alternative | Reason |\n| --- | --- |\n| Restore timer deletion permanently | It repairs this exact ordering but makes membership depend on scheduling. A pending deletion can also remove a replacement written under the same key. |\n| Delay deletion with `queueMicrotask` | It couples the cache to this disposer's current scheduling and does not protect later or nested asynchronous cleanup. |\n| Capture only the value and keep key-based invalidation | It fixes the demonstrated exception with a small caller change, but an old mount can still invalidate a newer mount. Use it only as an explicitly limited interim patch. |\n| Make the whole cache reference counted | It requires release discipline and leak handling that the supplied ordinary-value cache does not need. Retained handles already preserve the required callback value. |\n| Make every invalidation asynchronous | It expands the migration and still needs a definition of whose cleanup has completed. The cache does not own these subscriptions. |\n\n## Migration and acceptance checks\n\nFirst introduce entry handles without changing existing timer behavior, then migrate `mount` to retained values and owner-specific invalidation. Audit every caller for teardown-time `get` and overlapping key ownership before switching key-based invalidation to synchronous deletion. Deprecate unsafe consumer use of `invalidate(key)`, while keeping its deliberate current-entry semantics clear for administrative callers. Version or announce the timing change if callers outside this fixture consume the API.\n\nBefore implementation ships, verify actual behavior with the pinned vendor: normal unmount reports true exactly once after lookup removal; repeated unmount queues no extra report; external invalidation does not break disposal; A replaced by B can unmount without deleting B; a stale handle cannot remove a later put of the same object; report failures follow the documented policy. Keep the existing probe as evidence of the original failure. These proposed contracts and checks have not been implemented or validated here.\n\n## Assignment evidence and limits\n\nCandidate assignment: `arena-a-v1`, retry 1. This artifact is proposal-only and contains no implementation. The supplied package freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The supplied input manifest revision is SHA256 `7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43`; the manifest hashing convention was not supplied, so I do not claim to have independently reproduced that aggregate digest. No task Git SHA is available. The full Git input-revision gate remains reduced and this proposal cannot establish a full Arena method pass. The coordinator owns comparison, judgment and integration.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/b/proposal.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/b/proposal.md",
      "sha256": "366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b",
      "bytes": 7541,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache API proposal\n\nKeep cache invalidation synchronous and make teardown read the entry owned by its mount. Return an entry handle from put so an old mount can remove only its own generation. This separates lookup visibility from consumer lifetime without depending on event-loop delays.\n\n## Confirmed failure\n\nThe after-state invalidate deletes the Map entry immediately. The exact vendored createDisposer queues its callback with queueMicrotask and returns no completion signal. The caller invokes dispose, deletes the entry, then the queued callback evaluates get(key).ready against undefined. The diff alone hides that dependency.\n\nI ran bun arena-walkthrough/input/probe.mjs against the supplied files. It exited 1 with: teardown error: TypeError: undefined is not an object (evaluating get(key).ready). The vendor SHA-256 matches manifest.json: d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f. This establishes behavior for the local fixture-v1 implementation only. It establishes no public dependency behavior.\n\nThe removed setTimeout would place deletion after the queued microtask for this teardown. That ordering follows from the supplied code; I did not run a before-state comparison. Restoring it would preserve this narrow ordering but leave ownership ambiguous.\n\n## Proposed contract\n\n| Operation | Contract |\n| --- | --- |\n| put(key, value) | Replace the lookup entry and return a handle for that exact generation. |\n| get(key) | Return the current value, or undefined when absent. |\n| handle.value | Retain the supplied value reference for this consumer, even after replacement or invalidation. |\n| handle.invalidate() | Synchronously remove the key only if it still refers to this handle generation. Return whether removal occurred. Repeat calls are harmless. |\n| invalidate(key) | Synchronously remove the current lookup entry. Reserve this for a caller explicitly authorized to invalidate whichever generation is current. Return whether removal occurred. |\n\nA handle needs a unique internal identity. Comparing value equality is insufficient because callers can put the same object twice. The cache owns discoverability through get. Consumers own references they retain. Removing a lookup entry does not destroy its value, cancel a subscription, or invalidate an existing handle. The cache never invokes vendor disposal or owns consumer resource cleanup.\n\nThe consumer migration is conceptual, not an implementation in this proposal:\n\n1. Mount saves the handle returned by put.\n2. The disposal callback reports handle.value.ready rather than performing another lookup by key.\n3. Unmount calls subscription.dispose and calls handle.invalidate in a finally block. A local closed flag makes unmount idempotent before either action starts.\n\nThe retained object preserves reads of that particular object, including its later mutations. It does not promise a frozen snapshot. If two mounts use the same key, the older mount still reports its own value and cannot delete the newer mount when it closes. Explicit key-wide invalidation hides the entry from future lookups while retained consumers can finish cleanup.\n\n## Errors and completion\n\nA missing get returns undefined. Code that requires an entry must check it or keep an owned handle. Invalidation of an absent or replaced entry returns false, without throwing.\n\nIf dispose throws synchronously, finally still attempts owned invalidation and the original exception propagates. The closed flag prevents repeated disposal on another unmount call. The vendor provides no retry contract, so automatic disposal retries would be unsafe.\n\nErrors thrown by report inside the queued callback remain asynchronous errors under the existing consumer contract. A synchronous try/catch around unmount cannot catch them. Handle retention removes the missing-entry error, but does not suppress application callback failures. If the product requires error delivery through a promise, add a separate explicit completion/error adapter and define its callback semantics. Do not claim the current dispose method is awaitable.\n\nUnmount completion means disposal was requested and lookup ownership was released. It does not mean the queued report completed. Consumers that need stronger completion must use the separate adapter. A retained handle can prolong object lifetime, so consumers should release their subscription and handle references once their lifecycle finishes.\n\n## Alternatives considered\n\n| Alternative | Reason rejected for this proposal |\n| --- | --- |\n| Restore setTimeout deletion | Repairs this fixture ordering but delays lookup invalidation, and an old timer can delete a replacement entry. |\n| Queue deletion in a microtask | Relies on this vendor callback queue order and still lets stale owners delete new generations. |\n| Await subscription.dispose() | The supplied dispose returns undefined. Awaiting it establishes no general disposal completion contract. |\n| Change get to return a placeholder | Conceals missing entries and changes the meaning of ready. |\n| Retain only a captured value with the current key-based invalidate | Fixes the observed exception, but leaves overlapping mounts vulnerable to deleting a newer entry. |\n| Add reference counts and acquire/release leases | Useful if cache entries own destructible shared resources. The supplied cache holds plain values, so a generation handle is sufficient. |\n\n## Migration and verification plan\n\nFirst inspect all callers before changing put return values or enforcing handle ownership. Existing callers that ignore the new return can continue, but every consumer with delayed teardown must migrate before relying on synchronous invalidation. Document the lookup and lifetime contracts next to the exports. Update mount to keep its handle and remove its teardown lookup. Keep key-wide invalidation explicit for administrative invalidation use cases.\n\nBefore shipping an implementation, run the supplied real dependency probe and verify it reports disposed ready: true, then teardown completed with exit 0. Add behavioral checks for repeated unmount, old-unmount-after-replacement, two puts of the same object, invalidation before disposal, and report errors. Verify that synchronous invalidation hides lookup state before the queued callback while the callback still reads its retained value. These are proposed checks, not completed implementation tests.\n\n## Assignment evidence and limits\n\nThis artifact belongs to assignment arena-b-v1, candidate role, retryCount 0. Its only output is arena-walkthrough/b/proposal.md. I read task.md and every supplied input file. No implementation, external service, commit, installation, setting, or schedule was changed.\n\nThe coordinator supplied input manifest SHA-256 7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43 and package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The input task Git SHA is unavailable, so the full Git-revision assignment gate remains reduced. I have not substituted the package freeze for the task revision. The supplied manifest identifier is not the hash of the literal input/manifest.json file, whose observed SHA-256 is 5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29. I have not independently reconstructed the coordinator manifest algorithm.\n\nThe probe result and dependency hash above are observed command output. The proposed API and migration checks remain design work. No candidate comparison, independent judging, or full Arena completion is claimed by this artifact.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/checklist.md",
      "sha256": "5d87a149c9c9f496bca93211c6d84b9258c0b0df8d99baa9e3200fa317832554",
      "bytes": 211,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "- [x] Frame\n- [ ] Fan out\n- [ ] Cross-judge\n- [ ] Pick\n- [ ] Graft\n- [ ] Verify\nLocal checklist replaces unavailable todo operation. Exact repository Git SHA unavailable; manifest hashes identify fixture bytes.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/input-manifest.json",
      "sha256": "7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43",
      "bytes": 594,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "[[\"README.md\",\"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"],[\"cache.mjs\",\"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"],[\"caller.mjs\",\"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"],[\"invalidation.diff\",\"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"],[\"manifest.json\",\"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"],[\"probe.mjs\",\"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"],[\"vendor/disposer-v1.mjs\",\"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"]]"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/judge.md",
      "sha256": "e2b4d05c492ccaa99816a4e8a806a2df75f6b86bde50187b9baab8e74415f312",
      "bytes": 759,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Fresh worker /root/arena_judge, assignment arena-judge-v1. A hashes 4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e, B hashes 366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b. Scores caller clarity A2 B2; single state owner A2 B2; teardown correctness A2 B2; failure handling A1 B2; extension cost A2 B2. Choose B because closed-before-disposal and finally make synchronous failure explicit. Graft A staged migration and callback error guidance, optional chaining warning. Reject timer/microtask lifetime coupling, captured values with unrestricted invalidation, placeholders, reference counting. Proposed checks are unimplemented. Actual model/effort unknown. No task Git SHA. Coordinator transcription of returned judgment.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/rubric.md",
      "sha256": "a59d89d0e5b46cee7e128711a5e9485d939a77b1345b3762df61e2e1f91d8ce6",
      "bytes": 141,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Parent-only rubric. Score 0-2 each. Caller clarity; single state owner; teardown correctness; explicit failure handling; low extension cost.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/synthesis-note.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/synthesis-note.md",
      "sha256": "2ad624aea27df93d2dd341c56a59fa54ba3d4da4dfcb4ce853e58c8bb85f8935",
      "bytes": 1105,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Base B. Parent scores A 2/2/2/1/2 and B 2/2/2/2/2 on caller clarity, ownership, teardown, failures and extension cost. Fresh judge agrees. Both complete candidate artifacts were read before judging and reread for grafting. B contributes closed-before-disposal, finally and distinct generation identity. A contributes staged migration, optional-chaining warning and explicit deferred-error policy. Reject timing-based lifetime, key-only consumer deletion, placeholders and unnecessary reference counts. No terminal candidate dropout; A's initial spawn failed and its isolated retry completed.\n\nVerification is design review against real fixture and parent reproduction, not API implementation verification. command-results.json records after-state probe exit1 and restored before-state exit0. The synthesis addresses the demonstrated callback lifetime path and replacement ownership. Future behavioral checks remain proposals. No task Git SHA, model diversity, complete structured method receipt or installed-discovery pass is claimed. Manifest hashes and native worker identities are retained separately.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/synthesis.md",
      "sha256": "749432b24c38954ecb7702a67afc1b23010e4789bc88663c7612aa86bdf3f350",
      "bytes": 2607,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# Cache API proposal\n\nRetain consumer values across synchronous cache invalidation. Return an identity-bound handle from put so an older consumer cannot remove a newer entry under the same key. The cache owns lookup membership. Each consumer owns its subscription and retained value.\n\n| Operation | Contract |\n|---|---|\n| put(key, value) | Replace lookup membership and return a fresh generation handle, even if the same value is inserted twice. |\n| get(key) | Return the current value or undefined for a miss. |\n| handle.value | Retain that generation's exact object reference, without promising a deep snapshot. |\n| handle.invalidate() | Remove membership only if this generation is still current, returning whether removal occurred. |\n| invalidate(key) | Remove whichever generation is current. Reserve for deliberate key-wide invalidation. |\n\nMount retains its handle. Its deferred callback reads handle.value.ready. Unmount marks itself closed before requesting disposal, then invalidates its own handle in finally. Repeated unmount does nothing. A synchronous disposal error propagates after owned invalidation. Asynchronous report errors follow an explicit application policy inside the deferred callback. The synchronous unmount return means teardown was requested, not that its callback finished.\n\nThe vendored dispose queues a microtask and returns undefined. Awaiting that return does not establish callback completion. The after-state probe throws because deletion precedes the deferred get(key).ready. Retention removes that dependency. Optional chaining would hide the broken contract and change the report value.\n\nIntroduce handles, migrate consumers, audit teardown-time lookups and overlapping mounts, then change existing key-wide invalidation timing. Publish or version this timing change only through a separately authorized delivery. No delivery occurred here.\n\nReject timer and microtask deferrals as a permanent lifetime contract. They couple correctness to scheduling and can remove replacement entries. Capturing only a value fixes the demonstrated exception but leaves stale key-wide deletion. Placeholder values hide missing data. Reference counting adds release and leak handling without evidence of destructible shared resources in this fixture.\n\nAn implementation must exercise successful deferred reporting after immediate lookup removal, repeated unmount, A replaced by B before A closes, two generations sharing one object, external invalidation before disposal, synchronous disposal errors and asynchronous report errors. No implementation or those future checks ran here.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/task.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/task.md",
      "sha256": "3fb521843cc17b61dd816a343036e322cbddf44d3a0ee5bb2cc49eb1d382641a",
      "bytes": 326,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "Produce one Markdown proposal for a cache API using input/cache.mjs, caller.mjs, vendor/disposer-v1.mjs and README.md. Preserve consumer teardown correctness. Explain API ownership, errors, alternatives rejected and migration. No implementation or external actions. Input revision is SHA256 manifest, not an invented Git SHA.\n"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/verification.json",
      "sha256": "b84d79259fd627401ac6acb9551958507a2f560c7ecb03c4cc40d487adb2ceda",
      "bytes": 399,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "{\n  \"kind\": \"parent design inspection; not implementation test\",\n  \"criteria\": {\n    \"callerClarity\": true,\n    \"stateOwnership\": true,\n    \"teardown\": true,\n    \"failureHandling\": true,\n    \"extensionCost\": true\n  },\n  \"candidateHashes\": {\n    \"a\": \"4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e\",\n    \"b\": \"366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b\"\n  }\n}"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough.result.md",
      "sha256": "a80484ae5850eccc0940c33b3bc99c0dd10574911c55635575e4f7ce0c58a13c",
      "bytes": 6019,
      "owners": [
        "grades-native-06.json#6"
      ],
      "text": "# arena-walkthrough\n\n## Supplied input\n\n> Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\n\nNamed source files and exact copied source bytes are retained in [arena-walkthrough/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-manifest.json) and [arena-walkthrough/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/arena-walkthrough/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Navigation, frame and capability decisions\n\nRead installed README. It links docs/workflows/arena.md and that destination exists and was fully read. Read Arena and its capability, model-role, assignment and ownership contracts plus applied leaves. Source reads establish navigation, not a registered /arena command or installed-discovery pass. Installed package is visibly listed in this host's skill catalog, but source invocation was manual and no host registration command was tested.\n\nA local six-phase checklist replaces an unavailable todo operation. task.md requests two Markdown cache API proposals. The parent-only rubric has five criteria, caller clarity, state ownership, teardown correctness, failure handling and extension cost. Candidates did not receive the rubric. Frozen fixture input-manifest.json hashes to7dcb94c57c4014015efe5ffdd3b5c78548bf2e13e4029c103b7b55165aee3c43. No exact task Git SHA exists. This missing concrete prerequisite prevents a full assignment-contract run; isolated comparison proceeds with that explicit reduction.\n\n## Fan out and inspect\n\nCandidate A's inherited-context spawn failed with invalid thread-store/no rollout. The actual error is preserved in worker-events.json. A fresh fork_turns none attempt under arena-a-v1 retry1 returned /root/arena_a_retry and produced a/proposal.md. Candidate B, /root/arena_b under arena-b-v1 retry0, produced b/proposal.md. Their outputs are disjoint and both were read end to end. SHA256 values are4e13a7b539a42c8c47a6892f4b958595c834131547758ca5eb979bda16666f1e and366442d900bfe138e26bdbf8f6a86617afbfab48d520ce674aa9031cfd5c815b.\n\nWorker requests inherited model/effort. Observed model and effort are unknown. No cloud-placement or diversity claim. Actual workers wrote only their assigned proposals according to inspected files and returns; no OS-enforced per-worker sandbox is claimed. Append-only immutable pre-dispatch assignment events were not fully persisted before dispatch, so later coordinator event transcription is not a complete structured method receipt.\n\n## Cross-judge, pick and graft\n\nOnly after both terminal candidates and full artifacts were inspected, fresh read-only /root/arena_judge received candidates plus rubric. judge.md retains its result and independently checked artifact hashes. Parent criterion scores match the judge, A2/2/2/1/2 and B2/2/2/2/2. These are proposal comparison scores, not host case grades. Choose B because it defines closed-before-disposal and owned invalidation in finally. Graft A staged migration, optional-chaining warning and deferred-error policy. Reject scheduling-dependent lifetime, raw-key consumer invalidation, placeholders and unjustified reference counts. Both converge on generation handles; the graft keeps one model.\n\n## Verify and actual output\n\nsynthesis.md is the resulting cache API proposal; synthesis-note.md records base, grafts, rejections and inspection. verification.json retains hashes and bounded parent textual review aids. The parent reviewed the real caller/vendor path and reproduced after-state failure and before-state completion in command-results.json. API implementation and proposed future regression checks did not run. Prove It Works changed the verification from trusting worker summaries to reading artifacts and actual probe output. Separate Before Serializing Shared State changed candidate ownership to disjoint paths. Laziness Protocol rejected reference counting. Redesign From First Principles kept ownership coherent. Unslop was applied to synthesis prose.\n\nSix phases were exercised with native candidates and a fresh judge. Exact task Git SHA, observed model diversity and a full structured method receipt remain unmet. A source read or local text assertion is not evidence those gates passed. No dependency, settings, Git history or external action was changed.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/arena-walkthrough/input",
      "owner": "grades-native-06.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-manifest.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-reads.txt",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input",
      "owner": "grades-native-06.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/input.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-manifest.json",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/arena-walkthrough/source-reads.txt",
      "owner": "grades-native-06.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
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
