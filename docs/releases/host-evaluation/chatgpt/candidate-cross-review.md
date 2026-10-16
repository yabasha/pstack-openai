# chatgpt: candidate-cross-review

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "candidate-cross-review",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-05-08.json#20",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.",
  "caseDefinition": {
    "id": "candidate-cross-review",
    "sourcePaths": [
      "skills/arena/SKILL.md"
    ],
    "prompt": "Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.",
    "requirements": [
      "At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.",
      "Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.",
      "Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.",
      "Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.",
      "Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.",
      "One survivor means incomplete competition, never a full arena pass."
    ],
    "expectedFull": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.",
    "expectedReduced": "Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.",
    "expectedBlocked": "Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.",
    "forbiddenClaims": [
      "Sequential role switching proves independent candidates or independent review.",
      "Requested model names prove actual model diversity.",
      "A judge begins while candidates still write.",
      "One survivor establishes full competition.",
      "Structural validation or a case definition establishes host pass.",
      "The rubric is supplied to candidates.",
      "Upstream autonomy permits external writes or implicit setup."
    ],
    "caseFile": "docs/parity/cases/skills/arena.json"
  },
  "registry": {
    "caseId": "candidate-cross-review",
    "caseFile": "docs/parity/cases/skills/arena.json",
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
      "attemptId": "grades-chatgpt-05-08.json#20",
      "order": 0,
      "gradeFile": "grades-chatgpt-05-08.json",
      "rankWithinFile": 20,
      "host": "chatgpt",
      "caseId": "candidate-cross-review",
      "status": "reduced-pass",
      "grade": {
        "caseId": "candidate-cross-review",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "response",
          "review-outcome",
          "spawn",
          "inspect-result"
        ],
        "missing": [
          "Bun verification of synthesis",
          "Actual task Git revision and complete structured method receipt",
          "Candidate dropout and unavailable-worker variants"
        ],
        "review": "Two real isolated candidates and a fresh later judge support actual comparative design work; parent reads, rubric scores, base selection and graft are retained. Bun verification, task revision and dropout/unavailable-worker variants remain open. Reused candidates across cases are not independent replications.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/result.json",
        "variantReview": {
          "reported": [
            [
              "two candidates",
              "attempted",
              "cache_a and cache_b separate owned paths"
            ],
            [
              "fresh judge after terminal candidates",
              "attempted",
              "cache_judge inspected both"
            ],
            [
              "base/graft",
              "attempted",
              "B chosen, documentation adapted"
            ],
            [
              "runtime verification",
              "blocked",
              "Bun absent"
            ],
            [
              "candidate dropout",
              "blocked",
              "Not induced; both completed"
            ],
            [
              "unavailable workers",
              "blocked",
              "Scenario-only variant; actual host exposes workers"
            ],
            [
              "full exact-revision receipt",
              "blocked",
              "Task Git SHA unknown"
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
        "expectedFull": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.",
        "expectedReduced": "Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection."
      },
      "topLevelContext": {
        "packageCommit": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "ChatGPT baseline batches05–08, 32 unique workflow cases",
        "gradingPolicy": "Qualitative full/reduced/blocked outcomes plus actual native observation limits; corrected uncertain-result execution/persistence grants enforced. Model-captured wrappers are not independently raw-event verified; no self-grade imported."
      },
      "response": {
        "text": "Two independent workers produced isolated A and B artifacts for this case before a fresh read-only judge inspected them. I read both artifacts and rationales end to end. Select B's captured mount-owned value plus identity-checked deletion. A's unconditional invalidation can remove a replacement mount; B avoids this. Graft A's lifetime/mutable-reference documentation, reject its lease machinery for ordinary reporting. Judge and parent agree criterion by criterion; see synthesis.md. Runtime verification is blocked by absent Bun. Dropout and unavailable-worker variants remain explicitly unexercised; one survivor would be incomplete competition. Same workers also handled another case, so these are not independent cross-case replications. Actual models and task Git SHA remain unknown.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/result.json",
          "sha256": "dcb09504ea2238a70b6376d6b71d2b6591780ab3df7274f4453139b5936797b9",
          "bytes": 2396
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/artifact.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/artifact.md",
      "sha256": "6a5fea4e1bf08d075457ea58ca3435c8f22ee4e161bd497a41c73ae5e69dfa28",
      "bytes": 2138,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Candidate cross-a: snapshot leases\n\nSeparate lookup visibility from ownership. Invalidating a key removes it from future lookups immediately. An acquired lease keeps the exact value alive for its existing consumer. The disposal callback reads that lease rather than looking up a potentially absent or replaced key.\n\n```js\nexport function createCache() {\n  const entries = new Map();\n  return {\n    put(key, value) { entries.set(key, value); },\n    acquire(key) {\n      if (!entries.has(key)) return undefined;\n      let entry = { value: entries.get(key) };\n      return {\n        get value() {\n          if (!entry) throw new Error('Lease released');\n          return entry.value;\n        },\n        release() { entry = undefined; }\n      };\n    },\n    invalidate(key) { entries.delete(key); }\n  };\n}\n```\n\nCaller:\n\n```js\nconst cache = createCache();\nexport function mount(key, report) {\n  cache.put(key, { ready: true });\n  const lease = cache.acquire(key);\n  const subscription = createDisposer(() => {\n    try { report(lease.value.ready); }\n    finally { lease.release(); }\n  });\n  let closed = false;\n  return () => {\n    if (closed) return;\n    closed = true;\n    subscription.dispose();\n    cache.invalidate(key);\n  };\n}\n```\n\nAn existing mount sees its acquired snapshot even after invalidation or replacement. Future acquisitions see only the current entry. This intentionally does not claim resource disposal, deep immutability, TTL, or eviction. Values are ordinary shared JS references. For external resources, a separate ownership contract would be needed.\n\nStatic trace of supplied code: `dispose()` queues a microtask; synchronous `invalidate()` deletes the map entry; the queued original callback dereferences `undefined.ready`. The proposed callback dereferences its retained lease instead. This is source reasoning, not a runtime observation.\n\nExecution-dependent checks remain blocked because Bun is absent: original teardown reproduction, proposed teardown, replacement before queued callback, repeat unmount, missing acquisition, released-lease access, and callback-throws cleanup. No Node/Python substitute was used.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/rationale.md",
      "sha256": "e218d0b36a48eeda8111eccd27cbeab8e184e6e5ab1e073560d1ed2c091d4cb6",
      "bytes": 1756,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "Assignment cross-a; owner /root/eval_05_08/cache_a. Input artifact SHA-256 supplied by coordinator: 6ef42285eecd1bef7789167f6297283ebd8fae65a93092d5a84d232163885d88. Task Git SHA unknown, blocking the full revision contract. Requested model and effort: inherit-parent. Observed model and effort: unknown. Parent rubric and other candidate artifacts were not read.\n\nThe dominant access is a current-key lookup followed by an asynchronous consumer that still needs its acquired value. A lease explicitly represents this lifetime instead of making map deletion timing part of the caller contract. The tiny closure owns the retained reference; no global reference-count registry is needed for this fixture.\n\nRejected alternatives: restoring setTimeout preserves accidental event-loop ordering and remains brittle across different disposal implementations. Awaiting a promise returned by dispose cannot work with the supplied dependency because dispose returns no completion promise. Making all cache invalidation asynchronous changes ordinary lookup semantics. A reference-counted entry and disposal state machine adds policy for resources not present here. Simply optional-chaining get(key) suppresses the required ready report and hides the lifetime error.\n\nRead sources: arena, host-capabilities, model-roles, orchestration-contract, workflow-ownership, model-the-domain, foundational-thinking, laziness-protocol; copies retained under sources. Source reads succeeded through tools.exec_command. One broad rg listing was truncated, and an initial cat glob exited 1 on vendor directory while displaying fixture text; these are retained as limitations, not execution checks. No runtime probes, installs, live accounts, persistence claim, or full Arena claim.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/tool-observations.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/tool-observations.md",
      "sha256": "bd04854d3de56b192684c8ff8148c9f8cf97c27fed6515d43c1ae278587bfe4b",
      "bytes": 1999,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Actual worker observations\n\nAll operations used functions.exec calling tools.exec_command. No script runtime executed.\n\n- cwd/file inventory command: exit 0, cwd /workspace/scratch/305945b957dd; listed local case paths. Output chunk 19ea44.\n- broad rg file inventory: exit 0; tool reported truncated output (27643 original tokens). Output chunk a04437. Full omitted output is unavailable and is not reconstructed here.\n- case and fixture cat: exit 1 because both vendor paths were directories; case JSON and ordinary fixture files were displayed. Output chunk e886a4. Failure was retained; vendored file was subsequently read by exact path.\n- arena/principle/vendor cat: exit 0. Output chunk 08acb5. Source copies retained.\n- four support contract cat: exit 0. Output chunk 9a0a02. Source copies retained.\n- isolated mkdir/copy/source-output command: exit 0, stdout empty. Output chunk 59a2c5.\n- exact cross-review disposer source cat: exit 0; stdout:\n  // Exact vendored fixture dependency implementation, pinned by local SHA-256 in manifest.json.\n  export function createDisposer(onDispose) {\n    return { dispose: () => queueMicrotask(onDispose) };\n  }\n  Output chunk 8dfaa1.\n- artifact/rationale writes and sha256sum: exit 0. Output chunk e0afca. Digests:\n  walkthrough artifact 87a5e44b9196d4efa252ff6f919f859be4562911a90c3d818775fe3b78a698e7\n  walkthrough rationale 6d64341eefc29a4f572d6c7b41caf2c80c032c42f550c868a94145aec28973fa\n  cross artifact 6a5fea4e1bf08d075457ea58ca3435c8f22ee4e161bd497a41c73ae5e69dfa28\n  cross rationale e218d0b36a48eeda8111eccd27cbeab8e184e6e5ab1e073560d1ed2c091d4cb6\n\nThe tool transcript has exact arguments and returned outputs. This local ledger is a summary, not a raw receipt replacement. source-read-output.txt contains copied source bytes, not an independently observed runtime verification. Full raw transcript capture to local file was not available retrospectively for the first operations. Do not claim this ledger satisfies full receipt preservation.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/artifact.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/artifact.md",
      "sha256": "7624247bdb8133817b1b93d3758922bfea6b88d45fd1e5a9866c5f5bf83cf476",
      "bytes": 1787,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Candidate B: mount owns its cached value\n\nUse a cache instance with synchronous `set`, `get` and `delete`, but bind teardown to the value owned by the mount. A deferred callback must not look that value up through a key whose ownership may already have ended.\n\n```js\nexport function createCache() {\n  const entries = new Map();\n  return {\n    set(key, value) { entries.set(key, value); },\n    get(key) { return entries.get(key); },\n    deleteIf(key, value) {\n      if (entries.get(key) === value) entries.delete(key);\n    }\n  };\n}\n\nexport function mount(cache, key, report) {\n  const value = { ready: true };\n  cache.set(key, value);\n  const subscription = createDisposer(() => report(value.ready));\n  let mounted = true;\n  return () => {\n    if (!mounted) return;\n    mounted = false;\n    cache.deleteIf(key, value);\n    subscription.dispose();\n  };\n}\n```\n\n`createDisposer` is the supplied locally pinned dependency. Its `dispose` queues a microtask. The after-state caller schedules that callback and synchronously deletes the key; its eventual `get(key).ready` therefore reads `undefined.ready` when no replacement intervenes. This is a source-derived ordering prediction, not an executed result.\n\nThe proposed caller captures its owned value. Its deferred callback can report after key removal. `deleteIf` also prevents an old mount from deleting a replacement mount's value. This contract reports the disposed mount's final value, not whichever value is current under the key at callback time.\n\nRemaining checks: run the supplied after-state probe and compare restored timeout before-state; test proposed caller unmount, repeated unmount, and replacement mount before prior teardown. All runtime branches are unexercised because Bun is absent; no Node/Python substitute was used.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/identity.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/identity.txt",
      "sha256": "707300de4d15ead2b57b6e4536bfc431648c5958b29f30f3a5bc577ecbbde39b",
      "bytes": 266,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "assignmentId: cross-b\nowner: /root/eval_05_08/cache_b\ninputArtifactSha256: 6ef42285eecd1bef7789167f6297283ebd8fae65a93092d5a84d232163885d88\ntaskGitSha: unknown\nrequestedModel: inherit-parent\nactualModel: unknown\nexecution: blocked because Bun absent; no substitutes\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/input-read.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/input-read.stdout",
      "sha256": "c15c85b4f59877229943c8908c502be5087ab2689ba6baff6a8aef2ff8841062",
      "bytes": 3316,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "{\n  \"id\": \"candidate-cross-review\",\n  \"sourcePaths\": [\n    \"skills/arena/SKILL.md\"\n  ],\n  \"prompt\": \"Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\",\n  \"requirements\": [\n    \"At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.\",\n    \"Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.\",\n    \"Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.\",\n    \"Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.\",\n    \"Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.\",\n    \"One survivor means incomplete competition, never a full arena pass.\"\n  ]\n}\nReview invalidation.diff against the after-state cache.mjs and the real caller outside the diff. The vendored disposer is the exact locally pinned dependency, not a mock pretending to prove a public dependency. Determine whether synchronous invalidation races the deferred disposal callback. probe.mjs runs this actual supplied implementation and intentionally exits nonzero if teardown throws. A before-state copy may restore the removed setTimeout line to compare ordering. No execution result is supplied.\n{\n  \"scope\": \"exact local vendored fixture only\",\n  \"dependency\": {\n    \"path\": \"vendor/disposer-v1.mjs\",\n    \"version\": \"fixture-v1\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  \"publicPackageClaim\": false\n}\nconst entries = new Map();\nexport function put(key, value) { entries.set(key, value); }\nexport function get(key) { return entries.get(key); }\nexport function invalidate(key) { entries.delete(key); }\nimport { createDisposer } from './vendor/disposer-v1.mjs';\nimport { get, put, invalidate } from './cache.mjs';\nexport function mount(key, report) {\n  put(key, { ready: true });\n  const subscription = createDisposer(() => report(get(key).ready));\n  return () => { subscription.dispose(); invalidate(key); };\n}\n// Exact vendored fixture dependency implementation, pinned by local SHA-256 in manifest.json.\nexport function createDisposer(onDispose) {\n  return { dispose: () => queueMicrotask(onDispose) };\n}\nimport { mount } from './caller.mjs';\nlet error;\nprocess.once('uncaughtException', caught => { error = caught; });\nconst unmount = mount('fixture-key', ready => console.log('disposed ready:', ready));\nunmount();\nawait new Promise(resolve => setTimeout(resolve, 5));\nconsole.log(error ? `teardown error: ${error.name}: ${error.message}` : 'teardown completed');\nprocess.exitCode = error ? 1 : 0;\ndiff --git a/cache.mjs b/cache.mjs\n--- a/cache.mjs\n+++ b/cache.mjs\n@@ -1,4 +1,4 @@\n const entries = new Map();\n export function put(key, value) { entries.set(key, value); }\n export function get(key) { return entries.get(key); }\n-export function invalidate(key) { setTimeout(() => entries.delete(key), 0); }\n+export function invalidate(key) { entries.delete(key); }\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/rationale.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/rationale.md",
      "sha256": "2f52c296eb44373ce5ff696086b0b96b910dce63430ab602237108f2448b16a4",
      "bytes": 1459,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Rationale\n\nKeep invalidation synchronous and transfer teardown data ownership to the mounted subscription. `deleteIf` is an ownership check at the cache boundary rather than reliance on timing. A per-consumer cache instance removes module-global coupling.\n\nRejected a timer in invalidate: it implicitly orders unrelated callbacks and leaves stale entries visible until a future turn. Rejected `get(key)?.ready`: it prevents one exception but loses the required teardown value and can still report replacement state. Rejected an async invalidation promise: callers would need to thread disposal completion through a larger lifecycle API even though this callback needs only its own value. If consumers truly require asynchronous destruction of a shared resource rather than value reporting, that requirement changes this proposal and needs a lease/refcount model.\n\nNo parent rubric or other candidate was read. Source evidence consists of the supplied cache implementation, actual caller, pinned disposer, probe and invalidation diff, plus Arena contracts and model-the-domain/separate-state leaves copied beside this output. This is a design artifact, not a verified implementation. No runtime or live service was exercised.\n\nRequested model and effort: inherit-parent. Actual model and effort: unknown. Input artifact SHA-256: 6ef42285eecd1bef7789167f6297283ebd8fae65a93092d5a84d232163885d88. Task Git SHA: unknown; full revision contract remains blocked.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/checklist.md",
      "sha256": "ef0e297fd5bc9bef425ff4b06977cce7180a8dc462b602168dba60751c2489c3",
      "bytes": 62,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "1. Frame\n2. Fan out\n3. Cross-judge\n4. Pick\n5. Graft\n6. Verify\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/evidence/source-status.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/evidence/source-status.tsv",
      "sha256": "7f421714166463535ead1766fe9c50c958b97ee0fc81ce0509e76d4f3db4b0e3",
      "bytes": 24,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "0\tskills/arena/SKILL.md\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/judge/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/judge/judge.md",
      "sha256": "9a90ab3113691d7a4c1013a30be54c69b6ed4725de29a3d9d4810b73aa169047",
      "bytes": 3353,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Fresh read-only cross-judge\n\nRequested model/effort: inherit-parent. Observed model/effort: unknown. Fixture SHA supplied in assignment: 6ef42285eecd1bef7789167f6297283ebd8fae65a93092d5a84d232163885d88. Task Git revision unknown. This is a static design judgment; no runtime verification performed.\n\nBoth complete candidate artifacts and rationales, the case prompt, parent rubric, supplied cache/caller/disposer/probe/diff, and copied host/model/assignment/ownership contracts were read end to end. Installed arena was read successfully through skills__read. Four support resource reads through skills__read failed with \"failed to read skill resource\"; their available copied source text was read through exec_command. Copies do not independently establish installed package identity.\n\n| Criterion (0-2) | A | B | Source-grounded reason |\n|---|---:|---:|---|\n| Explicit owned cache state without module leakage | 1 | 2 | A encloses entries but its caller creates a module-level cache; B injects the cache into mount and captures the mount-owned value. |\n| Total lookup and invalidation contract | 1 | 2 | A explicitly returns undefined on absent acquisition but invalidate(key) unconditionally deletes a replacement. B get returns undefined and deleteIf(key,value) preserves a replacement object. B should state its absent-key semantics explicitly. |\n| Safe teardown when disposer callbacks are deferred | 1 | 2 | Both retain the original value for the microtask. A old unmount can delete a newer mount's entry; B guards deletion by identity. A has finally-based lease release; B needs no lease release. |\n| Small maintainable caller API | 1 | 2 | A adds acquire/value/release lifecycle and a released-lease exception for ordinary value reporting. B uses set/get/deleteIf with a captured value, sufficient for the supplied fixture. |\n| Rationale grounded in fixture code | 2 | 2 | Both correctly trace queueMicrotask disposal followed by synchronous map deletion, reject timer ordering and optional chaining, and identify static reasoning as unexecuted. |\n\nRecommend B as base. Scores compare proposals, not method compliance or host pass grades. B's small API handles same-key replacement and deferred reporting directly. Graft A's explicit contract documentation: values remain mutable shared references; deletion changes future lookup visibility, not the lifetime of captured values; resource destruction is outside this fixture. Do not graft lease machinery without a resource-lifetime requirement.\n\nDefects and limits: B's phrase \"per-consumer cache instance\" is stronger than the shown injection guarantees; a caller may share one cache. deleteIf uses value identity, so a generalized primitive-valued cache could encounter equal-value replacement ambiguity; this fixture creates a fresh object each mount. Neither candidate contains executed tests. A calls its held reference a snapshot although it does not clone or freeze it. The original caller's scheduled get(key).ready is source-predicted to throw when deletion leaves no replacement; this judge did not run that probe. Required verification remains blocked by the parent-observed absence of Bun, not independently re-probed here. Worker/model diversity, task revision, durable persistence and full workflow compliance are not inferred from file presence.\n\nJudge identity: cross-judge.\n\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/parent-rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/parent-rubric.md",
      "sha256": "2403d140494df2400668f43090c59fde51c693bdc99fa7e9115671dd3bdefdb2",
      "bytes": 260,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "Criteria withheld from candidates.\n1. Explicit owned cache state without module leakage.\n2. Total lookup and invalidation contract.\n3. Safe teardown when disposer callbacks are deferred.\n4. Small maintainable caller API.\n5. Rationale grounded in fixture code.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/result.json",
      "sha256": "dcb09504ea2238a70b6376d6b71d2b6591780ab3df7274f4453139b5936797b9",
      "bytes": 2396,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "{\n  \"caseId\": \"candidate-cross-review\",\n  \"batch\": \"batch-07\",\n  \"actualResponse\": \"Two independent workers produced isolated A and B artifacts for this case before a fresh read-only judge inspected them. I read both artifacts and rationales end to end. Select B's captured mount-owned value plus identity-checked deletion. A's unconditional invalidation can remove a replacement mount; B avoids this. Graft A's lifetime/mutable-reference documentation, reject its lease machinery for ordinary reporting. Judge and parent agree criterion by criterion; see synthesis.md. Runtime verification is blocked by absent Bun. Dropout and unavailable-worker variants remain explicitly unexercised; one survivor would be incomplete competition. Same workers also handled another case, so these are not independent cross-case replications. Actual models and task Git SHA remain unknown.\",\n  \"variants\": [\n    [\n      \"two candidates\",\n      \"attempted\",\n      \"cache_a and cache_b separate owned paths\"\n    ],\n    [\n      \"fresh judge after terminal candidates\",\n      \"attempted\",\n      \"cache_judge inspected both\"\n    ],\n    [\n      \"base/graft\",\n      \"attempted\",\n      \"B chosen, documentation adapted\"\n    ],\n    [\n      \"runtime verification\",\n      \"blocked\",\n      \"Bun absent\"\n    ],\n    [\n      \"candidate dropout\",\n      \"blocked\",\n      \"Not induced; both completed\"\n    ],\n    [\n      \"unavailable workers\",\n      \"blocked\",\n      \"Scenario-only variant; actual host exposes workers\"\n    ],\n    [\n      \"full exact-revision receipt\",\n      \"blocked\",\n      \"Task Git SHA unknown\"\n    ]\n  ],\n  \"observedOperations\": [\n    \"tools.exec_command named installed sources, cases and fixtures reads\",\n    \"tools.apply_patch isolated result/trail/synthesis writes\",\n    \"collaboration.spawn_agent two candidates and fresh judge\",\n    \"tools.exec_command candidate+judge result inspection\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"input/\",\n    \"work/\",\n    \"evidence/source-status.tsv\",\n    \"../../fixture-read-receipt.json\",\n    \"../../../batch-05/source-read-receipts.json\"\n  ],\n  \"limits\": [\n    \"No Bun; no Node/Python substitution\",\n    \"No live account writes\",\n    \"Git task revision unknown\",\n    \"Prior broad tool outputs truncated; retained per-source raw receipts supersede for source content\",\n    \"Not every early tool call has local full raw capture; host transcript retains them\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/synthesis.md",
      "sha256": "f5163a6b813ac6d67fdb8e6909b9ea9feb33884d94850f24c4d3c67e6a7d34ca",
      "bytes": 1105,
      "owners": [
        "grades-chatgpt-05-08.json#20"
      ],
      "text": "# Synthesis\n\nUse B as the base. Parent read both complete artifacts and rationales and agrees with the fresh judge. The parent criterion scores agree with the judge's A 1/1/1/1/2 and B 2/2/2/2/2. These compare designs, not host grades.\n\nB captures the mount's object and conditionally deletes only that object. A keeps the teardown value alive but unconditional invalidation can delete a replacement mount's entry. Retain B's smaller API. Adapt A's documentation that values remain mutable references, key deletion affects future lookup, and external resource destruction needs a different lifetime contract. Reject the lease state machine for ordinary value reporting. No model diversity was observed.\n\nVerification is static. Bun is absent, so teardown, replacement, repeated unmount and error callback probes were not run. Candidate files are design proposals, not runnable implementation proof. The two cases were separate assignments but reused the same workers and designs across case boundaries; they are not independent replications. Task Git SHA is missing and no full method receipt is claimed.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/source-read-output.txt",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/a/sources",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/candidates/b/sources",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/case.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/evidence/sources",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/input",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/judge/receipts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/judge/receipts.json",
      "sha256": "7cb12455abbf0de825531cd43f7098baaf5add54dd64697e6b3aa82dcc813b74",
      "bytes": 68009,
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/README.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/README.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/README.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/cache.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/invalidation.diff",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/manifest.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/probe.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/corpus/records.jsonl",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/dead-path/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/dead-path/duplicate-reference.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/dead-path/handler.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/dead-path/instructions.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/dead-path/scope.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/history/capsule.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/history/history.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/history/jay-mode.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/history/shared-records.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/adapter.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/calculator.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/controller.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/decision.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/exporter.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/facade.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/invoice/formatter.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/legal-header/source.diff",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/legal-header/source.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/migration/api.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/migration/contract.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/migration/notification.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/migration/profile.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/migration/scope.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/scenario-map.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/types/README.md",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/types/boundary.ts",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/additional/types/context.ts",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/dashboard.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/forge.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/history.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/invoice.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/orders.json",
      "owner": "grades-chatgpt-05-08.json#20",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/candidate-cross-review/work/runtime.mjs",
      "owner": "grades-chatgpt-05-08.json#20",
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
