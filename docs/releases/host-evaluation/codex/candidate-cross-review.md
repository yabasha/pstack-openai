# codex: candidate-cross-review

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "candidate-cross-review",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-07.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
      "attemptId": "grades-native-07.json#4",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "candidate-cross-review",
      "status": "reduced-pass",
      "grade": {
        "caseId": "candidate-cross-review",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_25",
          "item_26",
          "item_27",
          "item_31"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Exact taskGit revision/structured assignment-method receipt absent.",
          "Actual observed model diversity unknown."
        ],
        "review": "Two real isolated candidates finish, later fresh readonly judge compares complete outputs; parent selects B and runs7tests26assertions. Dropout and unavailable-worker limits retained. Required exact Git revision and full structured method receipt absent, so method cannot fully pass merely because artifacts/tests exist.",
        "responseArtifact": "fixtures/batch-07/candidate-cross-review.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.",
        "reducedExpected": "Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-07.json",
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
        "text": "# candidate-cross-review\n\n## Supplied input\n\nArena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\n\nThe installed source is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md. It and its required contracts and principle leaves were read through actual file tools. Package freeze supplied is f4623636a287bea2aa79c4b2234a53d20a5f193c. Only package 0.1.0 was used.\n\nConcrete cache requirement comes from the copied prepared fixture: retain ready values through the actual deferred disposal callback, release after reporting, and prevent old lifetimes deleting or overwriting replacements. Fixture data is not evidence of any service contact.\n\n## Actual output\n\nSelected candidate B, generation-owned handles. Its keyed cache exposes the newest generation; old handles keep their own value until released. Identity checks protect replacement and deletion. The selected implementation is candidate-cross-review/selected. Parent verification passed seven tests with 26 assertions, using the unchanged pinned local disposer.\n\nCandidate A uses shared counted leases and first-value-wins until all owners release. It fixes callback lifetime but changes the original per-mount replacement behavior. Candidate B is the stronger base for the supplied source. No material code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. The parent removed an obvious factory description comment while adapting B. The complete synthesis and rejections are in synthesis.md.\n\n## Observed method and artifacts\n\nNative candidates /root/cache_candidate_a and /root/cache_candidate_b wrote distinct authorized directories. The parent read both full implementations, callers, tests, rationales and verification artifacts. Both completed before /root/cache_judge was spawned as a fresh readonly judge. The judge returned scores and a base recommendation before selection and integration. It did not write candidate files.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Retention and finally cleanup | 2 | 2 |\n| Original fresh replacement behavior | 0 | 2 |\n| Stale lifetime safety | 2 | 2 |\n| Ownership/API tradeoffs | 2 | 2 |\n| Lifecycle coverage | 1 | 2 |\n\nThese are candidate scores, not evaluation grades. The parent agrees with the judge after inspecting the code. Its intermediate arithmetic said B=9; the displayed criteria total B=10. judge.md retains that correction. The fresh-replacement criterion is grounded in original cache.put and caller.mount, though more specific than the short task summary.\n\nCandidate A observed baseline failure exit 1 and six passing tests. Candidate B observed baseline failure exit 1 and seven passing tests. selected/cache.test.mjs was actually rerun by the parent. Original command arguments, stdout, stderr and exit codes are preserved in candidate verification.json files and synthesis-verification.json.\n\nRequested models and efforts for candidates were inherit-parent. Judge requested gpt-6-luna/high using current exposed tool documentation. All actual model and effort observations remain unknown. Requesting different selections proves no diversity. No aliases were supplied and no model selection rejection was observed. An earlier unrelated full-history forge worker dispatch failed with invalid thread-store/no rollout; fresh fork-none dispatch worked. Neither result is a model rejection.\n\n## Variants and limits\n\nThe normal two-candidate native-worker branch completed with a fresh judge. Task Git SHA is absent because the fixture root has no Git repository. Per-file digests identify copied inputs, but exact input-SHA assignment acceptance remains blocked. The package freeze is not substituted for task revision. No complete valid structured Arena method receipt or full Arena claim is made.\n\nThere are framing deviations. The rubric was written after candidate dispatch. The same substantive task and source grounding were used, but candidate wrapper wording differed. Immutable assignment records were not all persisted before dispatch. These limits remain explicit instead of retroactively rewriting dispatch history.\n\nDropout branch was an actual new worker /root/candidate_dropout, assignment cache-dropout-1. It required an exact task SHA, observed git rev-parse HEAD exit 128, and returned BLOCKED with no implementation. dropout/receipt.json preserves that result. It ran after the original competition as a separate negative variant, not an invented third competitor in the original ordering. With only candidate A retained as the survivor in that variant, competition is incomplete. The selected B artifact is not used to relabel that one-survivor variant as complete.\n\nUnavailable-worker branch was simulated, not enforced by this host. With worker calls deliberately omitted, the parent can compare the two shapes sequentially, but that leaves candidate independence, fresh independent judging and model diversity unmet. It does not produce a second full Arena result. The actual host did expose and successfully run workers in the normal branch.\n\nNo external service, configuration change, dependency install, commit, push, PR, message to others, publishing or schedule was performed. Worker messages were internal assignment/result operations only.\n",
        "artifact": {
          "path": "fixtures/batch-07/candidate-cross-review.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review.result.md",
          "sha256": "b0273bc111b69dae91a9157ff85a6e99a40c41c2e557ea76afe87d14e28cb986",
          "bytes": 5499
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-07.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-07.events.jsonl",
            "sha256": "26078a6d01730e84b6d57421e843541eb5b82f4c8b0cdd0b167ecf6636bbc630",
            "bytes": 636607,
            "eventReferences": [
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9c7e49e193d7e6fc52fd5690dadc8cb1c7dd9e7b66ad9c98a27361e9e40d31f5"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0b4bd71add486f8096424ea4384d9d00a84ea374bb3ef05e77fa7ec6a667fb9c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "650f5e9b7f40c3edf201a414197dd4b743093ff3cf4839c72768cbb308032037"
              },
              {
                "eventId": "item_25",
                "line": 48,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "faee36f0b43167185f291a747e52e89664840ada51b3d51dbfce4e914b671164",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_26",
                "line": 49,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "35e8ec07685b6e5df8a857303502e100e801a7aacd17ff9b13552d2c751a5698"
              },
              {
                "eventId": "item_26",
                "line": 50,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7261d690fa4bb9f801845f567d4eb161f7afba53bf59288f7467fb999cdbb907",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 51,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9bbd7c142dcb2190315310f1211e77d686156092c519bdf1ae8bcfcb911c12ec"
              },
              {
                "eventId": "item_27",
                "line": 52,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c3aa727b5bf17acd21d05aa984a11c6e2dd240b849c8ee06a075389096bc67b0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3d414913782b0e95aaf45c305c1fdca1f3ea5abcdce2891e23d7fb14a293978f"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "71440977a8a877d92807af16b9a2f0fa68b61440a86f9814aa56a5169107323d",
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
            "item_8",
            "item_25",
            "item_26",
            "item_27",
            "item_31"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-07.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/README.md",
      "sha256": "bce6ca314730b60a78520358702c99e55882b9d9b3cf6320bf5f2c45a3392568",
      "bytes": 2970,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# Candidate A\n\nThe caller acquires one lease per mount and releases it only after the vendored deferred disposal callback reports. The release runs in `finally`, including when reporting throws. Multiple mounts of one key share the current entry. Each lease releases at most once, and deletion checks entry identity.\n\nCaller usage is the design boundary:\n\n```js\nconst lease = acquire(key, { ready: true });\n// Inside the disposer's callback:\ntry { report(lease.value.ready); }\nfinally { lease.release(); }\n```\n\nThe cache exports `acquire` and `get`. `acquire` returns the value and a release capability tied to that entry. `get` preserves ordinary cache reads but does not acquire a lease. There is no public `put`, `invalidate`, replacement, or reference-count mutation. The caller cannot publish a stale deferred write. A fresh generation can start once the previous generation has no owners, and a repeated old release cannot remove it. For one key, the first value wins until all leases release. Later acquire calls do not overwrite it.\n\n`mount` remains the caller's only export. Its returned unmount function is idempotent, so repeated cleanup cannot queue duplicate reports. Reading the lease inside disposal also avoids accidentally reporting a different generation's value.\n\nRejected alternatives:\n\n- Restoring `setTimeout` relies on scheduler ordering and leaves cache lifetime detached from the callback that needs the value.\n- Deleting immediately and guarding `get(key)?.ready` avoids a throw but loses the required ready report.\n- A captured value with immediate cache invalidation reports correctly but violates retention through reporting.\n- A compare-and-delete token without lease counting lets one unmount evict an entry another active mount still needs.\n- Public replace and invalidate operations require extra lifecycle rules. This fixture has no replacement caller, so the API prevents replacement while an entry has owners.\n\nThe supplied after-state probe fails with a TypeError under Bun. The six candidate tests use the actual copied pinned disposer and pass. They cover retention during reporting, overlapping mounts, stale release after a new generation, repeated unmount, a mount created during reporting, and report failure with cleanup. `verification.json` records exact commands, outputs, and exit codes.\n\nThe supported callback contract is synchronous reporting, matching the fixture. An asynchronous report that returns a promise would need a separate decision about whether its settlement owns the lease. There is no claim about any public dependency or other disposer implementation. No service, installation, commit, or configuration change was performed.\n\nAssignment `cache-a-1` uses package freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c`. `input-digest.json` records every copied input hash and their aggregate content digest. Requested model and effort are inherited; actual values are unobserved. No parent rubric was supplied.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/artifacts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/artifacts.json",
      "sha256": "1f263ff783d4a887bc2a75c8d50b44084bd3a08dd27385340707e252b6c02277",
      "bytes": 1073,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"artifacts\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"bce6ca314730b60a78520358702c99e55882b9d9b3cf6320bf5f2c45a3392568\"\n    },\n    {\n      \"path\": \"assignment.json\",\n      \"sha256\": \"34e394a7c317b30b50cd43f56d94262adc4e70e1f196838d9afff55e159dee29\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"eecd30f1c41ceef55ddf6c107ca356ed688f77938ea764a9a0facedac3b430f2\"\n    },\n    {\n      \"path\": \"cache.test.mjs\",\n      \"sha256\": \"6ab47769367dd5f73c00fdc994edb2b6a31f3af08bcae2616d91137881b608c9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"7900387370c14152237da8e8f1a180d2d2bfa75488ec28209e2eb04ece9db157\"\n    },\n    {\n      \"path\": \"input-digest.json\",\n      \"sha256\": \"74fc9c5db9764d63293a8955431320090757af201f4ca55fa33b173824ad40c3\"\n    },\n    {\n      \"path\": \"throw-probe.mjs\",\n      \"sha256\": \"59f873ebb286c111eef407560023c422c53148bc7e7d4bc60249c4f9cdb523f4\"\n    },\n    {\n      \"path\": \"verification.json\",\n      \"sha256\": \"e7fe060b62479ccf778abe3e0c67aef803e587f41f3b163f8e3385051d572872\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/assignment.json",
      "sha256": "34e394a7c317b30b50cd43f56d94262adc4e70e1f196838d9afff55e159dee29",
      "bytes": 468,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"workerId\": \"/root/cache_candidate_a\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"inputContentSha256\": \"1573556b38b3867e89399540f97bfd6a490b7a3e6c4942f5b98700b7c2da35f7\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"role\": \"candidate\",\n  \"rubricProvided\": false,\n  \"outputPath\": \"candidate-cross-review/candidate-a\"\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/cache.mjs",
      "sha256": "eecd30f1c41ceef55ddf6c107ca356ed688f77938ea764a9a0facedac3b430f2",
      "bytes": 656,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "const entries = new Map();\n\n// Acquire synchronously. Mounts of the same key share its current value.\nexport function acquire(key, value) {\n  let entry = entries.get(key);\n  if (!entry) {\n    entry = { value, leases: 0 };\n    entries.set(key, entry);\n  }\n  entry.leases++;\n  let released = false;\n  return {\n    value: entry.value,\n    release() {\n      if (released) return;\n      released = true;\n      if (--entry.leases === 0 && entries.get(key) === entry) {\n        entries.delete(key);\n      }\n    },\n  };\n}\n\n// A read never acquires ownership. Teardown reads through its lease instead.\nexport function get(key) {\n  return entries.get(key)?.value;\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/cache.test.mjs",
      "sha256": "6ab47769367dd5f73c00fdc994edb2b6a31f3af08bcae2616d91137881b608c9",
      "bytes": 2702,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { acquire, get } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\ntest('entry survives unmount until the actual deferred report returns', async () => {\n  const observed = [];\n  const unmount = mount('lifetime', ready => {\n    observed.push(ready);\n    expect(get('lifetime').ready).toBe(true);\n  });\n  unmount();\n  expect(get('lifetime').ready).toBe(true);\n  expect(observed).toEqual([]);\n  await Promise.resolve();\n  expect(observed).toEqual([true]);\n  expect(get('lifetime')).toBeUndefined();\n});\n\ntest('overlapping mounts retain the same entry until both reports finish', async () => {\n  const reports = [];\n  const first = mount('overlap', ready => reports.push(['first', ready]));\n  const original = get('overlap');\n  first();\n  const second = mount('overlap', ready => reports.push(['second', ready]));\n  expect(get('overlap')).toBe(original);\n  await Promise.resolve();\n  expect(reports).toEqual([['first', true]]);\n  expect(get('overlap')).toBe(original);\n  second();\n  await Promise.resolve();\n  expect(reports).toEqual([['first', true], ['second', true]]);\n  expect(get('overlap')).toBeUndefined();\n});\n\ntest('a stale release cannot delete or replace a fresh generation', () => {\n  const old = acquire('generation', { ready: true, generation: 1 });\n  old.release();\n  const replacement = acquire('generation', { ready: true, generation: 2 });\n  old.release();\n  expect(get('generation')).toBe(replacement.value);\n  expect(get('generation').generation).toBe(2);\n  replacement.release();\n  expect(get('generation')).toBeUndefined();\n});\n\ntest('repeated unmount queues only one report and cannot release another mount', async () => {\n  let count = 0;\n  const first = mount('repeat', () => count++);\n  const second = mount('repeat', () => count++);\n  first();\n  first();\n  await Promise.resolve();\n  expect(count).toBe(1);\n  expect(get('repeat').ready).toBe(true);\n  second();\n  await Promise.resolve();\n  expect(count).toBe(2);\n  expect(get('repeat')).toBeUndefined();\n});\n\ntest('a mount created within reporting remains alive after the old release', async () => {\n  let next;\n  const first = mount('reentrant', () => {\n    next = mount('reentrant', () => {});\n  });\n  first();\n  await Promise.resolve();\n  expect(get('reentrant').ready).toBe(true);\n  next();\n  await Promise.resolve();\n  expect(get('reentrant')).toBeUndefined();\n});\n\ntest('a throwing report releases the cache through the real disposer', () => {\n  const result = Bun.spawnSync([process.execPath, 'throw-probe.mjs'], {\n    cwd: import.meta.dir,\n  });\n  expect(result.exitCode).toBe(0);\n  expect(result.stdout.toString()).toContain('report failed; cache released');\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/caller.mjs",
      "sha256": "7900387370c14152237da8e8f1a180d2d2bfa75488ec28209e2eb04ece9db157",
      "bytes": 455,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './input/vendor/disposer-v1.mjs';\nimport { acquire } from './cache.mjs';\n\nexport function mount(key, report) {\n  const lease = acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(lease.value.ready);\n    } finally {\n      lease.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/input-digest.json",
      "sha256": "74fc9c5db9764d63293a8955431320090757af201f4ca55fa33b173824ad40c3",
      "bytes": 1095,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"algorithm\": \"sha256 of sorted relative-path file digest manifest, lines sha256 two spaces path newline\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    }\n  ],\n  \"digest\": \"1573556b38b3867e89399540f97bfd6a490b7a3e6c4942f5b98700b7c2da35f7\"\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/throw-probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/throw-probe.mjs",
      "sha256": "59f873ebb286c111eef407560023c422c53148bc7e7d4bc60249c4f9cdb523f4",
      "bytes": 452,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { mount } from './caller.mjs';\nimport { get } from './cache.mjs';\n\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throws', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 0));\nif (caught?.message !== 'report failed' || get('throws') !== undefined) {\n  throw new Error('Report error or cache cleanup was lost');\n}\nconsole.log('report failed; cache released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-a/verification.json",
      "sha256": "e7fe060b62479ccf778abe3e0c67aef803e587f41f3b163f8e3385051d572872",
      "bytes": 1220,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-a-1\",\n  \"results\": [\n    {\n      \"name\": \"baseline\",\n      \"command\": [\n        \"bun\",\n        \"candidate-cross-review/candidate-a/input/probe.mjs\"\n      ],\n      \"exitCode\": 1,\n      \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"name\": \"candidate\",\n      \"command\": [\n        \"bun\",\n        \"test\",\n        \"candidate-cross-review/candidate-a/cache.test.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n      \"stderr\": \"\\ncandidate-cross-review/candidate-a/cache.test.mjs:\\n(pass) entry survives unmount until the actual deferred report returns [0.21ms]\\n(pass) overlapping mounts retain the same entry until both reports finish [0.07ms]\\n(pass) a stale release cannot delete or replace a fresh generation [0.02ms]\\n(pass) repeated unmount queues only one report and cannot release another mount [0.05ms]\\n(pass) a mount created within reporting remains alive after the old release [0.04ms]\\n(pass) a throwing report releases the cache through the real disposer [11.60ms]\\n\\n 6 pass\\n 0 fail\\n 21 expect() calls\\nRan 6 tests across 1 file. [18.00ms]\\n\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/README.md",
      "sha256": "5a23a05f777224b13db2a26059017c01a7550a481221aa94938dd98cbf2df7b3",
      "bytes": 4803,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# Cache candidate B\n\nUse a mount-owned cache handle. The disposer reads that handle before releasing it.\n\n```js\nimport { mount } from './implementation/caller.mjs';\nimport { cache } from './implementation/cache.mjs';\n\nconst unmount = mount('panel', ready => console.log(ready));\nunmount();\nconsole.log(cache.get('panel').ready); // true until the disposal microtask runs\nawait new Promise(resolve => queueMicrotask(resolve));\nconsole.log(cache.get('panel')); // undefined\n```\n\nThe complete caller is in `implementation/caller.mjs`. Its unmount callback schedules the exact supplied vendored disposer once. Inside the disposal callback, `report(entry.read().ready)` runs before `entry.release()`. A `finally` releases the entry even if reporting throws. It does not catch or suppress the reporting error.\n\n## Cache API\n\n`implementation/cache.mjs` exports `createCache()` for an independent cache and the shared `cache` used by `mount`.\n\n| Operation | Contract |\n| --- | --- |\n| `cache.acquire(key, initialValue)` | Installs a new current entry and returns its owning handle. Superseded handles retain their own value until released. |\n| `cache.get(key)` | Returns the current value, or `undefined` when no current entry exists. |\n| `handle.read()` | Returns this handle's value, even after another mount replaces the key. Throws after release. |\n| `handle.replace(nextValue)` | Updates only while this handle is current and unreleased. Returns `false` for stale or released handles. |\n| `handle.release()` | Drops this handle's value. Deletes the keyed entry only if this handle still owns it. Returns `false` after the first release. |\n\nFor asynchronous producers, acquire before starting work and publish through that same handle:\n\n```js\nconst entry = cache.acquire('panel', { ready: true });\nconst result = await loadPanel();\nif (!entry.replace({ ready: true, result })) {\n  // Another mount replaced this generation, or this mount already released it.\n}\n```\n\nThis is a replacement of the original `put/get/invalidate` contract. Migrate mount ownership and producer writes together. A stale producer must retain its handle rather than call `acquire` again when work completes.\n\n## Why this shape\n\nThe original caller disposes asynchronously and invalidates synchronously. Its callback subsequently reads `undefined.ready`. Delaying invalidation with a timer repairs that one ordering but leaves a key-reuse race. An older timer can delete a newer mount's entry.\n\nA handle separates a mount's retained value from whichever mount currently owns the key. Entry identity checks protect both writes and deletion. Deleting a current entry never reveals an older generation. If a newer mount unmounts first, an older live mount can still report its own ready value, but key lookup remains empty until a later mount acquires the key.\n\nThe public key lookup deliberately returns only the current generation. Disposal must read its own handle. A key lookup inside old teardown cannot identify which mount it belongs to.\n\nI considered these alternatives:\n\n- Moving `invalidate(key)` into the disposal callback fixes the missing value but still allows old teardown to delete a replacement.\n- Comparing values during invalidation protects deletion but does not stop stale reads or late producer writes. Dedicated handles make all three operations use the same ownership check.\n- Keeping a set of all generations in the cache would expose more bookkeeping than callers need. Each mount's handle already retains its generation, and release clears its value.\n- A reference count would keep a shared entry alive but would conflate replacement with shared ownership. This fixture creates a fresh ready entry on every mount.\n\nValues remain ordinary JavaScript references. Callers should use `replace` rather than mutate retained objects. Reporting is synchronous, as in the supplied caller. The cache releases after `report` returns or throws; it does not await a returned promise. If a disposer never invokes its callback, its handle remains retained. The local pinned disposer always queues that callback in a microtask.\n\n## Verification\n\nRun `bun test candidate-cross-review/candidate-b/implementation/cache.test.mjs` from the fixture root.\n\nSeven tests cover retention during reporting, final release, old and new mount teardown in both orders, rejected stale producer writes, duplicate unmount/release, reentrant mounting during reporting, and release after a reporter throws. The last case runs in a subprocess so an uncaught reporting error cannot interfere with the test runner.\n\nThe original copied probe fails with `TypeError` under Bun. The candidate uses the unchanged vendored dependency bytes. These checks establish behavior for the exact local fixture only. They make no claim about a public dependency.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.mjs",
      "sha256": "aff32bea0c029542adca1c7f652e3c49087ccf6f6f934a15ae654faaf75a5547",
      "bytes": 920,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "/** A keyed cache whose handles own one generation until release. */\nexport function createCache() {\n  const current = new Map();\n\n  return {\n    get(key) { return current.get(key)?.value; },\n    acquire(key, initialValue) {\n      const entry = { value: initialValue };\n      let released = false;\n      current.set(key, entry);\n\n      return {\n        read() {\n          if (released) throw new Error('Cache handle already released');\n          return entry.value;\n        },\n        replace(nextValue) {\n          if (released || current.get(key) !== entry) return false;\n          entry.value = nextValue;\n          return true;\n        },\n        release() {\n          if (released) return false;\n          released = true;\n          if (current.get(key) === entry) current.delete(key);\n          entry.value = undefined;\n          return true;\n        },\n      };\n    },\n  };\n}\n\nexport const cache = createCache();\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/cache.test.mjs",
      "sha256": "b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0",
      "bytes": 3768,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { describe, expect, test } from 'bun:test';\nimport { createCache, cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst flushDisposal = () => new Promise(resolve => queueMicrotask(resolve));\n\ndescribe('ownership and deferred disposal', () => {\n  test('retains ready through reporting and releases after reporting', async () => {\n    const observed = [];\n    const unmount = mount('single', ready => {\n      observed.push([ready, cache.get('single')?.ready]);\n    });\n    unmount();\n    expect(cache.get('single')).toEqual({ ready: true });\n    expect(observed).toEqual([]);\n    await flushDisposal();\n    expect(observed).toEqual([[true, true]]);\n    expect(cache.get('single')).toBeUndefined();\n  });\n\n  test('old callback reads its own ready value and cannot delete a replacement', async () => {\n    const observed = [];\n    const stopOld = mount('reused', ready => observed.push(['old', ready]));\n    stopOld();\n    const stopNew = mount('reused', ready => observed.push(['new', ready]));\n    await flushDisposal();\n    expect(observed).toEqual([['old', true]]);\n    expect(cache.get('reused')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(observed).toEqual([['old', true], ['new', true]]);\n    expect(cache.get('reused')).toBeUndefined();\n  });\n\n  test('replacement unmounting first still leaves old handle readable', async () => {\n    const observed = [];\n    const stopOld = mount('reverse', ready => observed.push(['old', ready]));\n    const stopNew = mount('reverse', ready => observed.push(['new', ready]));\n    stopNew();\n    stopOld();\n    await flushDisposal();\n    expect(observed).toEqual([['new', true], ['old', true]]);\n    expect(cache.get('reverse')).toBeUndefined();\n  });\n\n  test('a stale asynchronous producer cannot overwrite a replacement', () => {\n    const local = createCache();\n    const old = local.acquire('key', { ready: true, id: 'old' });\n    const replacement = local.acquire('key', { ready: true, id: 'new' });\n    expect(old.replace({ ready: false, id: 'late-old' })).toBe(false);\n    expect(old.read()).toEqual({ ready: true, id: 'old' });\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    old.release();\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    expect(replacement.replace({ ready: false, id: 'updated-new' })).toBe(true);\n    expect(local.get('key')).toEqual({ ready: false, id: 'updated-new' });\n    replacement.release();\n    expect(local.get('key')).toBeUndefined();\n  });\n\n  test('unmount and release are idempotent', async () => {\n    let count = 0;\n    const stop = mount('duplicate', () => count++);\n    stop(); stop();\n    await flushDisposal();\n    stop();\n    await flushDisposal();\n    expect(count).toBe(1);\n    const local = createCache();\n    const handle = local.acquire('key', 1);\n    expect(handle.release()).toBe(true);\n    expect(handle.release()).toBe(false);\n    expect(handle.replace(2)).toBe(false);\n    expect(() => handle.read()).toThrow('already released');\n  });\n\n  test('report may synchronously mount a replacement without old release deleting it', async () => {\n    let stopNew;\n    const stopOld = mount('reentrant', () => {\n      stopNew = mount('reentrant', () => {});\n    });\n    stopOld();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toBeUndefined();\n  });\n\n  test('a throwing reporter still releases its entry', () => {\n    const result = Bun.spawnSync([process.execPath, new URL('./throwing-reporter.mjs', import.meta.url).pathname]);\n    expect(result.exitCode).toBe(0);\n    expect(result.stdout.toString()).toContain('throw observed; entry released');\n  });\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/caller.mjs",
      "sha256": "8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34",
      "bytes": 454,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './vendor/disposer-v1.mjs';\nimport { cache } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = cache.acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(entry.read().ready);\n    } finally {\n      entry.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/throwing-reporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/implementation/throwing-reporter.mjs",
      "sha256": "9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc",
      "bytes": 410,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throw', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 5));\nif (caught?.message !== 'report failed' || cache.get('throw') !== undefined) process.exit(1);\nconsole.log('throw observed; entry released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/input-digest.json",
      "sha256": "d39add47ed04ef0102dec4155c4f5c0496f3ecea1ca486147e15bd3a7911be48",
      "bytes": 1071,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"algorithm\": \"sha256 of JSON.stringify(sorted array of path and sha256 records)\",\n  \"digest\": \"0c36430ae8b0398d1853696b1fed0cb0a7aadb2b785a6d8e954376516b50080e\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/output-digest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/output-digest.json",
      "sha256": "42dc97cb373c5daa2ab60e77c6f4b1b2168516b8ba675b474508f2fbf5152b78",
      "bytes": 2299,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-b-1\",\n  \"outputSha256\": \"7408ca18cce4dddf132899f4d11aefade59021d9d1b11c9eb16d9090e28f7b62\",\n  \"files\": [\n    {\n      \"path\": \"README.md\",\n      \"sha256\": \"5a23a05f777224b13db2a26059017c01a7550a481221aa94938dd98cbf2df7b3\"\n    },\n    {\n      \"path\": \"implementation/cache.mjs\",\n      \"sha256\": \"aff32bea0c029542adca1c7f652e3c49087ccf6f6f934a15ae654faaf75a5547\"\n    },\n    {\n      \"path\": \"implementation/cache.test.mjs\",\n      \"sha256\": \"b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0\"\n    },\n    {\n      \"path\": \"implementation/caller.mjs\",\n      \"sha256\": \"8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34\"\n    },\n    {\n      \"path\": \"implementation/throwing-reporter.mjs\",\n      \"sha256\": \"9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc\"\n    },\n    {\n      \"path\": \"implementation/vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    },\n    {\n      \"path\": \"input-digest.json\",\n      \"sha256\": \"d39add47ed04ef0102dec4155c4f5c0496f3ecea1ca486147e15bd3a7911be48\"\n    },\n    {\n      \"path\": \"input/README.md\",\n      \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n    },\n    {\n      \"path\": \"input/cache.mjs\",\n      \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n    },\n    {\n      \"path\": \"input/caller.mjs\",\n      \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n    },\n    {\n      \"path\": \"input/invalidation.diff\",\n      \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n    },\n    {\n      \"path\": \"input/manifest.json\",\n      \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n    },\n    {\n      \"path\": \"input/probe.mjs\",\n      \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n    },\n    {\n      \"path\": \"input/vendor/disposer-v1.mjs\",\n      \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n    },\n    {\n      \"path\": \"task-input.md\",\n      \"sha256\": \"d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b\"\n    },\n    {\n      \"path\": \"verification.json\",\n      \"sha256\": \"23c13584548c4edaf3719c5f85d8deac8012fad0b30cc383113381687412eaab\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/task-input.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/task-input.md",
      "sha256": "d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b",
      "bytes": 720,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Produce isolated candidate B for the local cache API from ../shared/additional/cache.\nThe cache must retain its ready entry until the deferred disposer reports on unmount, then release the entry. Stale concurrent mounts must not overwrite or delete replacements.\nDeliver the whole API with caller-first usage, implementation, rationale naming alternatives, and meaningful tests. Preserve a source copy in input. Write only candidate-cross-review/candidate-b. Do not use live services, install, commit, or change configuration. Run scripts with Bun.\nAssignment: cache-b-1. Requested model and effort: inherit-parent. Actual model and effort: unknown.\nInstruction package freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/candidate-b/verification.json",
      "sha256": "23c13584548c4edaf3719c5f85d8deac8012fad0b30cc383113381687412eaab",
      "bytes": 3165,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"cache-b-1\",\n  \"role\": \"candidate\",\n  \"outputPath\": \"candidate-cross-review/candidate-b\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"inputRevision\": \"unknown; fixture root has no Git repository\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"taskInputSha256\": \"d9102ff8a6e3252595f82309fdd4df19dfad86b9d233cf325d4889d7e1a48c1b\",\n  \"fixtureInputSha256\": \"0c36430ae8b0398d1853696b1fed0cb0a7aadb2b785a6d8e954376516b50080e\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one independently generated API candidate, verified against the pinned local disposer\",\n    \"order\": 1\n  },\n  \"tests\": [\n    {\n      \"name\": \"baseline\",\n      \"argv\": [\n        \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n        \"candidate-cross-review/candidate-b/input/probe.mjs\"\n      ],\n      \"exitCode\": 1,\n      \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"name\": \"candidate-tests\",\n      \"argv\": [\n        \"/opt/homebrew/Cellar/bun/1.4.2/bin/bun\",\n        \"test\",\n        \"candidate-cross-review/candidate-b/implementation/cache.test.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n      \"stderr\": \"\\ncandidate-cross-review/candidate-b/implementation/cache.test.mjs:\\n(pass) ownership and deferred disposal > retains ready through reporting and releases after reporting [0.20ms]\\n(pass) ownership and deferred disposal > old callback reads its own ready value and cannot delete a replacement [0.07ms]\\n(pass) ownership and deferred disposal > replacement unmounting first still leaves old handle readable [0.04ms]\\n(pass) ownership and deferred disposal > a stale asynchronous producer cannot overwrite a replacement [0.04ms]\\n(pass) ownership and deferred disposal > unmount and release are idempotent [0.07ms]\\n(pass) ownership and deferred disposal > report may synchronously mount a replacement without old release deleting it [0.03ms]\\n(pass) ownership and deferred disposal > a throwing reporter still releases its entry [16.19ms]\\n\\n 7 pass\\n 0 fail\\n 26 expect() calls\\nRan 7 tests across 1 file. [22.00ms]\\n\"\n    }\n  ],\n  \"terminalStatus\": \"completed\",\n  \"limits\": [\n    \"Task repository Git revision unavailable; coordinator confirmed no task Git SHA exists. Exact-revision method gate remains blocked.\",\n    \"Requested selection is inherited; actual model and effort are unknown.\",\n    \"Local candidate completion is not a full Arena claim.\",\n    \"Behavior verified only against the exact supplied vendored disposer.\"\n  ],\n  \"methodReads\": [\n    \"skills/arena/SKILL.md\",\n    \"references/host-capabilities.md\",\n    \"references/model-roles.md\",\n    \"references/orchestration-contract.md\",\n    \"references/workflow-ownership.md\",\n    \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"skills/principle-laziness-protocol/SKILL.md\",\n    \"skills/principle-redesign-from-first-principles/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\",\n    \"skills/unslop/SKILL.md\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/dropout/receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/dropout/receipt.json",
      "sha256": "1c74d318b7b6ba8ecf8341854307716fc38c126ecfad6f32a2d144a9adb03d55",
      "bytes": 1595,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"assignmentId\": \"cache-dropout-1\",\n  \"workerId\": \"/root/candidate_dropout\",\n  \"role\": \"candidate\",\n  \"status\": \"blocked\",\n  \"scope\": \"Retain ready cache entry until deferred disposer reports on unmount, then release it; prevent stale concurrent mounts from overwriting or deleting replacement entries.\",\n  \"outputOwner\": \"/root/candidate_dropout\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/dropout\",\n  \"inputRevision\": \"unknown\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"retryCount\": 0,\n  \"reason\": \"Required exact task repository Git SHA is unavailable. Assignment contract requires the full task Git SHA before candidate implementation.\",\n  \"prerequisite\": {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"command\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07\",\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\",\n    \"exitCode\": 128\n  },\n  \"packageCommitIsNotInputRevision\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"implementationProduced\": false,\n  \"integrationEligible\": false,\n  \"variant\": \"Separate dropout exercise after the original completed competition; no retroactive third candidate and no new cancellation.\",\n  \"evidenceLinks\": [\n    \"candidate-cross-review/dropout/receipt.json\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/judge.md",
      "sha256": "d0ea959a6c0e1d95e0e67773ef82792edf7d667e1f303532df802b3b39c8833c",
      "bytes": 1235,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Fresh judge /root/cache_judge started after both candidates returned terminal reports and parent read their artifacts. Requested gpt-6-luna/high; actual model and effort unknown.\n\nObserved recommendation: base B.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Ready retained and finally cleanup | 2 | 2 |\n| Fresh put per mount | 0 | 2 |\n| Stale teardown and producer protection | 2 | 2 |\n| Coherent API and tradeoffs | 2 | 2 |\n| Lifecycle test coverage | 1 | 2 |\n\nThe judge reported \"B wins clearly (9 vs 7)\" in its intermediate message. The displayed scores actually total B=10, A=7. Parent corrects only that arithmetic; the base recommendation is unchanged.\n\nThe judge found A first-value-wins semantics change original put behavior. B preserves fresh generation replacement and old handles remain readable until their own release. No material graft was recommended. A's refcount model was rejected because current source overwrites on each put. The fresh-put criterion is stronger than the short task summary but grounded in source. Rubric was authored after candidate dispatch, a framing-order deviation. Judge read the artifacts and verification records without executing code. Both actual model and task Git SHA remain unknown.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/rubric.md",
      "sha256": "5920be7c5f9351f3ea2a8e3c702c1cb435eb1e3d91dea0ff94888a1b04ddd3fb",
      "bytes": 1018,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Parent criteria, 0 absent, 1 partial, 2 demonstrated. Candidates were not given this rubric. It was written after dispatch, which is a framing-order deviation.\n\n1. Retains ready value through the actual deferred callback and releases in finally.\n2. Preserves the original fresh put per mount behavior under key reuse.\n3. Prevents old teardown or delayed producers from deleting or overwriting a newer generation.\n4. Keeps state ownership inside a small coherent API and states lifecycle tradeoffs.\n5. Tests real pinned disposal, reverse teardown, repeated teardown, reentrant mount, and reporter failure.\n\nCommon substantive task used in both dispatches: cache must retain ready entry until deferred disposer reports on unmount, then release entry; avoid stale concurrent mounts overwriting or deleting replacements. Produce caller-first API, implementation and rationale. Input copied from shared/additional/cache. Dispatch wrapper instructions differ; exact task SHA is unavailable because no Git repository exists.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/cache.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/cache.mjs",
      "sha256": "e781951753c4275bc4a078b7f836e1939d7c40399e8085fd146971fe4c25b443",
      "bytes": 851,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "export function createCache() {\n  const current = new Map();\n\n  return {\n    get(key) { return current.get(key)?.value; },\n    acquire(key, initialValue) {\n      const entry = { value: initialValue };\n      let released = false;\n      current.set(key, entry);\n\n      return {\n        read() {\n          if (released) throw new Error('Cache handle already released');\n          return entry.value;\n        },\n        replace(nextValue) {\n          if (released || current.get(key) !== entry) return false;\n          entry.value = nextValue;\n          return true;\n        },\n        release() {\n          if (released) return false;\n          released = true;\n          if (current.get(key) === entry) current.delete(key);\n          entry.value = undefined;\n          return true;\n        },\n      };\n    },\n  };\n}\n\nexport const cache = createCache();\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/cache.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/cache.test.mjs",
      "sha256": "b9702c26bec15d779ea3f2462a6ffe2678daf82750b91c38db17254810e6e2c0",
      "bytes": 3768,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { describe, expect, test } from 'bun:test';\nimport { createCache, cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\n\nconst flushDisposal = () => new Promise(resolve => queueMicrotask(resolve));\n\ndescribe('ownership and deferred disposal', () => {\n  test('retains ready through reporting and releases after reporting', async () => {\n    const observed = [];\n    const unmount = mount('single', ready => {\n      observed.push([ready, cache.get('single')?.ready]);\n    });\n    unmount();\n    expect(cache.get('single')).toEqual({ ready: true });\n    expect(observed).toEqual([]);\n    await flushDisposal();\n    expect(observed).toEqual([[true, true]]);\n    expect(cache.get('single')).toBeUndefined();\n  });\n\n  test('old callback reads its own ready value and cannot delete a replacement', async () => {\n    const observed = [];\n    const stopOld = mount('reused', ready => observed.push(['old', ready]));\n    stopOld();\n    const stopNew = mount('reused', ready => observed.push(['new', ready]));\n    await flushDisposal();\n    expect(observed).toEqual([['old', true]]);\n    expect(cache.get('reused')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(observed).toEqual([['old', true], ['new', true]]);\n    expect(cache.get('reused')).toBeUndefined();\n  });\n\n  test('replacement unmounting first still leaves old handle readable', async () => {\n    const observed = [];\n    const stopOld = mount('reverse', ready => observed.push(['old', ready]));\n    const stopNew = mount('reverse', ready => observed.push(['new', ready]));\n    stopNew();\n    stopOld();\n    await flushDisposal();\n    expect(observed).toEqual([['new', true], ['old', true]]);\n    expect(cache.get('reverse')).toBeUndefined();\n  });\n\n  test('a stale asynchronous producer cannot overwrite a replacement', () => {\n    const local = createCache();\n    const old = local.acquire('key', { ready: true, id: 'old' });\n    const replacement = local.acquire('key', { ready: true, id: 'new' });\n    expect(old.replace({ ready: false, id: 'late-old' })).toBe(false);\n    expect(old.read()).toEqual({ ready: true, id: 'old' });\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    old.release();\n    expect(local.get('key')).toEqual({ ready: true, id: 'new' });\n    expect(replacement.replace({ ready: false, id: 'updated-new' })).toBe(true);\n    expect(local.get('key')).toEqual({ ready: false, id: 'updated-new' });\n    replacement.release();\n    expect(local.get('key')).toBeUndefined();\n  });\n\n  test('unmount and release are idempotent', async () => {\n    let count = 0;\n    const stop = mount('duplicate', () => count++);\n    stop(); stop();\n    await flushDisposal();\n    stop();\n    await flushDisposal();\n    expect(count).toBe(1);\n    const local = createCache();\n    const handle = local.acquire('key', 1);\n    expect(handle.release()).toBe(true);\n    expect(handle.release()).toBe(false);\n    expect(handle.replace(2)).toBe(false);\n    expect(() => handle.read()).toThrow('already released');\n  });\n\n  test('report may synchronously mount a replacement without old release deleting it', async () => {\n    let stopNew;\n    const stopOld = mount('reentrant', () => {\n      stopNew = mount('reentrant', () => {});\n    });\n    stopOld();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toEqual({ ready: true });\n    stopNew();\n    await flushDisposal();\n    expect(cache.get('reentrant')).toBeUndefined();\n  });\n\n  test('a throwing reporter still releases its entry', () => {\n    const result = Bun.spawnSync([process.execPath, new URL('./throwing-reporter.mjs', import.meta.url).pathname]);\n    expect(result.exitCode).toBe(0);\n    expect(result.stdout.toString()).toContain('throw observed; entry released');\n  });\n});\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/caller.mjs",
      "sha256": "8d0d984ce37ada3e550e22a54ea358adaae769bb7245aeaec3e272ca84527d34",
      "bytes": 454,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { createDisposer } from './vendor/disposer-v1.mjs';\nimport { cache } from './cache.mjs';\n\nexport function mount(key, report) {\n  const entry = cache.acquire(key, { ready: true });\n  const subscription = createDisposer(() => {\n    try {\n      report(entry.read().ready);\n    } finally {\n      entry.release();\n    }\n  });\n  let unmounted = false;\n  return () => {\n    if (unmounted) return;\n    unmounted = true;\n    subscription.dispose();\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/throwing-reporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/selected/throwing-reporter.mjs",
      "sha256": "9eae6aad94b33adeff92a0f92a926fa97b730c7f75e043cd7a18b12b1c2b81dc",
      "bytes": 410,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import { cache } from './cache.mjs';\nimport { mount } from './caller.mjs';\nlet caught;\nprocess.once('uncaughtException', error => { caught = error; });\nmount('throw', () => { throw new Error('report failed'); })();\nawait new Promise(resolve => setTimeout(resolve, 5));\nif (caught?.message !== 'report failed' || cache.get('throw') !== undefined) process.exit(1);\nconsole.log('throw observed; entry released');\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/source-files.json",
      "sha256": "58668f493711f2bd7abdcdd5fa6f7eb12f6a4dc9081bdbb24b1c26591d6dbd36",
      "bytes": 29,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "[\n  \"skills/arena/SKILL.md\"\n]"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesis-verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesis-verification.json",
      "sha256": "0a4c218a1d59a0ef979c7a0e02dadb34969a69d39c573c9d133301d843d5e90f",
      "bytes": 1072,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"candidate-cross-review/selected/cache.test.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncandidate-cross-review/selected/cache.test.mjs:\\n(pass) ownership and deferred disposal > retains ready through reporting and releases after reporting [0.22ms]\\n(pass) ownership and deferred disposal > old callback reads its own ready value and cannot delete a replacement [0.07ms]\\n(pass) ownership and deferred disposal > replacement unmounting first still leaves old handle readable [0.05ms]\\n(pass) ownership and deferred disposal > a stale asynchronous producer cannot overwrite a replacement [0.04ms]\\n(pass) ownership and deferred disposal > unmount and release are idempotent [0.07ms]\\n(pass) ownership and deferred disposal > report may synchronously mount a replacement without old release deleting it [0.04ms]\\n(pass) ownership and deferred disposal > a throwing reporter still releases its entry [17.05ms]\\n\\n 7 pass\\n 0 fail\\n 26 expect() calls\\nRan 7 tests across 1 file. [24.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesis.md",
      "sha256": "5109aa97ff171faa23d462ee3b6a7c0eacf78c366f2ddbb25a684c60f4f964cf",
      "bytes": 1361,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "Parent selection is B. Parent read complete candidate cache/caller/test/rationale files before selection and agrees with the fresh judge's criterion scores. B preserves source replacement semantics with current-generation identity checks. A has a smaller API, but hides replacement by reusing the first value until every lease releases. That tradeoff loses this contract.\n\nThe synthesis uses B's implementation. No code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. Rejected A's refcount policy, public lease.value and first-value-wins behavior. Divergence is a real ownership distinction, not a reason to average the designs. No reframing or forced convergence is claimed.\n\nParent hand-adaptation removes the factory doc comment, whose meaning is apparent from the code, and retains tests and pinned disposer unchanged. No mechanical cross-candidate merge occurs. Actual verification receipt is synthesis-verification.json.\n\nNo full Arena claim. Missing task Git SHA, unknown actual models, post-dispatch rubric and immutable assignment framing-order gaps remain explicit. Candidate A/B wrapper prompts differed although their substantive goal and copied input bytes were the same. The common task and rubric are preserved in rubric.md. Unavailable-worker and dropout variants are recorded separately.\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/synthesize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review/synthesize.mjs",
      "sha256": "eba0194475328af7569fea84bee5b1494dbc6784bb4225eee54fc63a393e2f2f",
      "bytes": 701,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "import {cpSync,readFileSync,writeFileSync,mkdirSync} from 'node:fs';\ncpSync('candidate-cross-review/candidate-b/implementation','candidate-cross-review/selected',{recursive:true});\nconst p='candidate-cross-review/selected/cache.mjs';writeFileSync(p,readFileSync(p,'utf8').replace('/** A keyed cache whose handles own one generation until release. */\\n',''));\nconst argv=['bun','test','candidate-cross-review/selected/cache.test.mjs'];const r=Bun.spawnSync(argv);const receipt={argv,exitCode:r.exitCode,stdout:r.stdout.toString(),stderr:r.stderr.toString()};writeFileSync('candidate-cross-review/synthesis-verification.json',JSON.stringify(receipt,null,2));console.log(JSON.stringify(receipt,null,2));\n"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/candidate-cross-review.result.md",
      "sha256": "b0273bc111b69dae91a9157ff85a6e99a40c41c2e557ea76afe87d14e28cb986",
      "bytes": 5499,
      "owners": [
        "grades-native-07.json#4"
      ],
      "text": "# candidate-cross-review\n\n## Supplied input\n\nArena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.\n\nThe installed source is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md. It and its required contracts and principle leaves were read through actual file tools. Package freeze supplied is f4623636a287bea2aa79c4b2234a53d20a5f193c. Only package 0.1.0 was used.\n\nConcrete cache requirement comes from the copied prepared fixture: retain ready values through the actual deferred disposal callback, release after reporting, and prevent old lifetimes deleting or overwriting replacements. Fixture data is not evidence of any service contact.\n\n## Actual output\n\nSelected candidate B, generation-owned handles. Its keyed cache exposes the newest generation; old handles keep their own value until released. Identity checks protect replacement and deletion. The selected implementation is candidate-cross-review/selected. Parent verification passed seven tests with 26 assertions, using the unchanged pinned local disposer.\n\nCandidate A uses shared counted leases and first-value-wins until all owners release. It fixes callback lifetime but changes the original per-mount replacement behavior. Candidate B is the stronger base for the supplied source. No material code graft from A is justified because B already includes its useful finally cleanup and idempotent unmount. The parent removed an obvious factory description comment while adapting B. The complete synthesis and rejections are in synthesis.md.\n\n## Observed method and artifacts\n\nNative candidates /root/cache_candidate_a and /root/cache_candidate_b wrote distinct authorized directories. The parent read both full implementations, callers, tests, rationales and verification artifacts. Both completed before /root/cache_judge was spawned as a fresh readonly judge. The judge returned scores and a base recommendation before selection and integration. It did not write candidate files.\n\n| Criterion | A | B |\n| --- | ---: | ---: |\n| Retention and finally cleanup | 2 | 2 |\n| Original fresh replacement behavior | 0 | 2 |\n| Stale lifetime safety | 2 | 2 |\n| Ownership/API tradeoffs | 2 | 2 |\n| Lifecycle coverage | 1 | 2 |\n\nThese are candidate scores, not evaluation grades. The parent agrees with the judge after inspecting the code. Its intermediate arithmetic said B=9; the displayed criteria total B=10. judge.md retains that correction. The fresh-replacement criterion is grounded in original cache.put and caller.mount, though more specific than the short task summary.\n\nCandidate A observed baseline failure exit 1 and six passing tests. Candidate B observed baseline failure exit 1 and seven passing tests. selected/cache.test.mjs was actually rerun by the parent. Original command arguments, stdout, stderr and exit codes are preserved in candidate verification.json files and synthesis-verification.json.\n\nRequested models and efforts for candidates were inherit-parent. Judge requested gpt-6-luna/high using current exposed tool documentation. All actual model and effort observations remain unknown. Requesting different selections proves no diversity. No aliases were supplied and no model selection rejection was observed. An earlier unrelated full-history forge worker dispatch failed with invalid thread-store/no rollout; fresh fork-none dispatch worked. Neither result is a model rejection.\n\n## Variants and limits\n\nThe normal two-candidate native-worker branch completed with a fresh judge. Task Git SHA is absent because the fixture root has no Git repository. Per-file digests identify copied inputs, but exact input-SHA assignment acceptance remains blocked. The package freeze is not substituted for task revision. No complete valid structured Arena method receipt or full Arena claim is made.\n\nThere are framing deviations. The rubric was written after candidate dispatch. The same substantive task and source grounding were used, but candidate wrapper wording differed. Immutable assignment records were not all persisted before dispatch. These limits remain explicit instead of retroactively rewriting dispatch history.\n\nDropout branch was an actual new worker /root/candidate_dropout, assignment cache-dropout-1. It required an exact task SHA, observed git rev-parse HEAD exit 128, and returned BLOCKED with no implementation. dropout/receipt.json preserves that result. It ran after the original competition as a separate negative variant, not an invented third competitor in the original ordering. With only candidate A retained as the survivor in that variant, competition is incomplete. The selected B artifact is not used to relabel that one-survivor variant as complete.\n\nUnavailable-worker branch was simulated, not enforced by this host. With worker calls deliberately omitted, the parent can compare the two shapes sequentially, but that leaves candidate independence, fresh independent judging and model diversity unmet. It does not produce a second full Arena result. The actual host did expose and successfully run workers in the normal branch.\n\nNo external service, configuration change, dependency install, commit, push, PR, message to others, publishing or schedule was performed. Worker messages were internal assignment/result operations only.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-read.txt",
      "owner": "grades-native-07.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-a/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/implementation/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/candidate-b/input",
      "owner": "grades-native-07.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/selected/vendor/disposer-v1.mjs",
      "owner": "grades-native-07.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-07/candidate-cross-review/source-read.txt",
      "owner": "grades-native-07.json#4",
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
