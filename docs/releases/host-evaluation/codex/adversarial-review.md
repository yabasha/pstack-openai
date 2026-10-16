# codex: adversarial-review

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "adversarial-review",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-durable-01.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.",
  "caseDefinition": {
    "id": "adversarial-review",
    "sourcePaths": [
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md"
    ],
    "prompt": "Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.",
    "requirements": [
      "State intent and give every competing reviewer the identical diff, context, rubric and code-quality lens.",
      "Preserve all rubric lenses, evidence-based findings and pragmatic lead judgment across act on, consider, noted and dismissed categories.",
      "Report reviewer models, finding counts, independent consensus, lone findings and disagreements in the complete verdict format.",
      "Verify independent worker results and observed model diversity; disclose sequential review as reduced capability.",
      "Do not auto-apply changes or create external changes to fix rejected model defaults."
    ],
    "expectedFull": "Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit.",
    "expectedReduced": "When independent workers are unavailable, an authorized sequential review applies the complete rubric and lead judgment and labels reduced capability. It does not claim independent agreement or model diversity; unknown actual models remain unknown.",
    "expectedBlocked": "Unavailable diff or context, or denied review capability, blocks grounded findings. Report the missing source or permission without inventing findings, reviewer execution or agreement.",
    "forbiddenClaims": [
      "Sequential passes are independent reviewers.",
      "Requested model names prove actual model diversity.",
      "The rubric or code-quality lens can be omitted.",
      "A review authorizes automatic fixes or an external PR.",
      "Structural checks establish host behavioral parity."
    ],
    "caseFile": "docs/parity/cases/skills/interrogate.json"
  },
  "registry": {
    "caseId": "adversarial-review",
    "caseFile": "docs/parity/cases/skills/interrogate.json",
    "sourcePaths": [
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md"
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
      "attemptId": "grades-native-06.json#4",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "adversarial-review",
      "status": "reduced-pass",
      "grade": {
        "caseId": "adversarial-review",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_21",
          "item_25",
          "item_27"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Exact task Git assignment identity absent.",
          "Reviewer models unknown; coordinator-condensed outputs/provenance do not provide complete structured method evidence."
        ],
        "review": "Two observed independent reviewers receive same complete template/context and identify one lifetime regression. Parent reproduces actual failing after-state and passing restored timer before-state; lead deduplicates, attributes and presents all categories/agreement. Full exact assignment revision/result evidence absent; model diversity unknown and condensed worker records not full transcript.",
        "responseArtifact": "fixtures/batch-06/adversarial-review.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit.",
        "reducedExpected": "When independent workers are unavailable, an authorized sequential review applies the complete rubric and lead judgment and labels reduced capability. It does not claim independent agreement or model diversity; unknown actual models remain unknown.",
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
        "text": "# adversarial-review\n\n## Supplied input\n\n> Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.\n\nNamed source files and exact copied source bytes are retained in [adversarial-review/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/source-manifest.json) and [adversarial-review/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Intent\n\nMake invalidate(key) remove a cache entry synchronously while preserving the caller's deferred disposal callback. This intent is inferred from supplied README and diff, not confirmed by a live PR description. No current Git diff exists. The prepared invalidation.diff is the review target.\n\n## Reviewers\n\nBoth reviewers received identical common-prompt.md containing intent, full diff, surrounding caller, exact vendor implementation, manifest, probe, all six rubric lenses and the complete code-quality lens. Its independently checked SHA256 is eee01486cb794ebd8d13894b6a249be66fdc8e585c2062500ec5bf94591da75b.\n\n- Reviewer A, /root/review_a, requested inherit-parent model/effort, actual unknown, one critical finding.\n- Reviewer B, /root/review_b, requested inherit-parent model/effort, actual unknown, one critical finding.\n\nNative worker identities and returned results were observed and inspected. Model diversity is unverified. Full input Git SHA is unavailable. reviewer-a.md and reviewer-b.md retain the complete finding content in coordinator-condensed prose. Worker self-reports of execution were checked against the parent's actual probe.\n\n## Act On\n\nBoth reviewers identify one concrete lifetime regression at input/cache.mjs:4 through caller.mjs:5-6 and vendor/disposer-v1.mjs:3. dispose queues a microtask. Synchronous invalidate deletes the entry before that callback reads get(key).ready, so teardown throws and report never runs. Parent run exits1 and prints \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\". Restoring the removed timer line in a separate before/ copy exits0 with \"disposed ready: true\" and \"teardown completed\". Exact results are in command-results.json.\n\nThis warrants action because the normal integration path breaks. Retain the mounted value rather than querying invalidated shared membership in the callback, and test both immediate removal and eventual report. This is a recommendation only. The current fixture was not fixed.\n\n## Consider\n\nNone of the independent reviewers raised a separate finding in this category. Identity-bound ownership for overlapping mounts is a useful future API design consideration from Arena, but is not promoted here into independent review consensus or a proven new regression from this diff.\n\n## Noted\n\nNo separate low-priority findings. The dependency is the exact locally pinned vendored fixture, SHA256 d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f. No public dependency or live service behavior is inferred.\n\n## Dismissed\n\nNo reviewer finding was dismissed. Optional chaining would hide the failed report contract and is rejected as a proposed response, not represented as a reviewer finding. There is no evidence for inventing security, size or style blockers.\n\n## Agreement Map\n\nIndependent workers agree on the same one correctness/root-cause/structure/verification finding. No lone finding or explicit disagreement exists. Security and complexity lenses yield no supported additional finding. The code-quality lens favors removing lifetime coupling rather than adding a timing workaround or abstraction. Agreement is worker consensus, not observed multi-model consensus. Lead judgment accepts the one reproduced issue. No changes were auto-applied, and no external defaults or settings were changed.\n",
        "artifact": {
          "path": "fixtures/batch-06/adversarial-review.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review.result.md",
          "sha256": "2d797944421c0431ec26dc472aedddaf54fe4e90b478c62a48950bdc9c1127e1",
          "bytes": 5542
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
                "eventId": "item_21",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ffbc35a438978cea908c763de8fefac87f45b53762fcd9352d7be9251655f4f9"
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4b8c5e5185728ca05000907ba4dc414d5ab262b1952248558699c44547a437f5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 46,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "0c4bda60212ae8f15d6e4d4e9e8c1f3700ac0afbd056873624f99946211ab5da"
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b3533798c26d91627a79425097658c8ab453124a4aa19371a25515e4e29be192",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 50,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "47fbe6897f86bc3d9917266468318c0e49bf61a9b39bed14ffaabbfb3f9b6a41"
              },
              {
                "eventId": "item_27",
                "line": 51,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2963a386f6619798b78d8fe66a3dc5c90fbc2a8f806b6c59dd253219cf804106",
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
            "item_21",
            "item_25",
            "item_27"
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
      "attemptId": "grades-native-durable-01.json#0",
      "order": 201,
      "gradeFile": "grades-native-durable-01.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "adversarial-review",
      "status": "reduced-pass",
      "grade": {
        "caseId": "adversarial-review",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/durable-01.events.jsonl",
        "actualReadEventIds": [
          "item_6",
          "item_7",
          "item_8",
          "item_10",
          "item_11",
          "item_18"
        ],
        "actualExecutionEventIds": [
          "item_13",
          "item_15",
          "item_22",
          "item_39",
          "item_43"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "execution",
          "review-outcome"
        ],
        "missing": [
          "Scoped source/context compliance deviation; ancillary wrong-version read must not be erased"
        ],
        "review": "Two independent native reviewers receive matching frozen diff/context/template/rubric and both return the same critical teardown finding. Parent actual before/after probe exits0/1 and full attributed verdict cover all disposition categories. Core native review succeeds with explicit unknown-model limit. Raw item5 reads ancillary Unslop0.2.1 plus unrelated memory registry before correct frozen case templates; saved only0.1.0 claim is inaccurate. Core case templates later match f462, but unqualified scoped-source compliance is not met.",
        "responseArtifact": "fixtures/durable-01/adversarial-review/adversarial-review.result.md",
        "variantReview": [
          "Actual case-owned source/artifacts and native trace reviewed; conditional withholding is simulation unless a concrete host error is preserved.",
          "No schema-validator, bookkeeping label, compiler version, or verification script selfgrade is accepted as workflow success."
        ],
        "limits": [
          "Raw item5 reads ancillary Unslop0.2.1 plus unrelated memory registry before correct frozen case templates; saved only0.1.0 claim is inaccurate. Core case templates later match f462, but unqualified scoped-source compliance is not met.",
          "Local spawn wrappers retain actual observations, not complete offline raw native-envelope/concurrency proof."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "evidence": [
          "fixtures/durable-01/adversarial-review/verdict.md",
          "fixtures/durable-01/adversarial-review/reviewer-payload.md",
          "fixtures/durable-01/adversarial-review/execution/after.json",
          "fixtures/durable-01/adversarial-review/freeze-proof.json"
        ],
        "fullExpected": "Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit."
      },
      "topLevelContext": {
        "attempt": "durable-01",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Durable01 raw stream ends turn.completed; wrapper exit receipt was absent at inspection.",
          "Ancillary wrong-version and unrelated-context reads are preserved as deviations; copied personal-memory bytes are excluded from reports."
        ]
      },
      "response": {
        "text": "# adversarial-review\n\nObserved result: two native independent reviewers completed; both found one critical disposal regression, which the coordinator reproduced. Actual model diversity is unverified. No grade is assigned.\n\n## Supplied input\n\nTask payload: “Intent: change deferred invalidation to immediate deletion while preserving disposal correctness. Supply every independent reviewer the identical diff, dependent caller, exact pinned dependency bytes, full template, rubric and code-quality lens at one SHA. Inspect all worker findings and lead-classify every deduplicated item into Act On/Consider/Noted/Dismissed, with attributed Agreement Map. Do not apply a fix or open a PR. Actual model diversity must be observed or limited explicitly.”\n\nVerified task input HEAD: `2478f73932fd235358105d47301f4f8bc3e9782b`. Plugin freeze supplied separately: `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed 0.1.0 exact path prefix `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/`. Source paths read in full: skills/interrogate/SKILL.md and references/code-quality-review.md, lead-judgment.md, reviewer-prompt.md, rubric.md. Original source snapshots and digests: sources.json and sources/. Original fixture locations are recorded in the user's supplied request; execution and assignments use committed-inputs bytes extracted by git show, never mutable shared inputs. inputs.json records each Git path, revision, extracted copy and SHA256. Full supplied case definitions are also retained in supplied-contracts.json.\n\n## Actual response\n\nThe complete required verdict is verdict.md, including Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map. The complete filled identical reviewer template is reviewer-payload.md. Reviewer A returned a JSON object in review-a/returned.json; B returned Markdown in review-b/returned.md. Both originals are retained. Every returned finding has a disposition in the verdict.\n\n## Actual tools and observations\n\n- functions.exec with tools.exec_command read exact installed sources and repository instructions, ran git rev-parse HEAD, git status and git show; reads and setup exited 0. The first large combined source read truncated; the affected rubric and reflection context were subsequently read in separate calls. No claim rests on the truncated portion.\n- collaboration.list_agents returned the running root. collaboration.spawn_agent accepted review_a then review_b and returned /root/review_a and /root/review_b. Exact spawn arguments, returned objects and dispatch order are in each review directory's spawn.json. Immutable assignments predate dispatch. Both pending declarations are preserved; subsequent statuses belong to events.jsonl rather than edits to original assignment scope.\n- Native final notifications returned A then B. Both contained the assigned input revision and full findings. functions.exec / exec_command read both persisted responses before synthesis. No operation exit code exists for native spawn or returned final messages; they return objects and messages, not process statuses.\n- Bun executed run-checks.mjs, which ran the supplied probe against case-owned after and before copies. execution/after.json records exit 1 and actual TypeError; execution/before.json records exit 0 and completed teardown. The deliberate before variant restores only the removed setTimeout deletion. No committed input was edited.\n- Bun invoked installed TypeScript 5.9.3 with --version, exit 0. This is compiler execution proof only and is recorded under ../decision-trail/compiler.json; no TypeScript correctness is claimed for these JavaScript fixtures.\n\n## Variants and limits\n\nIndependent native review ran; sequential fallback was inapplicable. The supplied before and after implementations both actually executed. No requested historical Claude or Grok defaults were attempted, configured or substituted. Exposed choices were GPT variants or inherit-parent; neither returned worker object exposes an actual model. The whole review covers exact local pinned bytes only. No fix, PR, commit, package update, external action or service call occurred. Arena and Swarm are not cases in this group; their receipt schemas are not asserted for this Interrogate workflow. Assignment events and original native payloads are preserved without invented telemetry.\n\n## Final verification addendum\n\nfreeze-proof.json independently compares every requested installed source file and saved snapshot with git show at package revision f4623636a287bea2aa79c4b2234a53d20a5f193c in the existing local package repository. All requested bytes match. This is source identity verification, not a behavioral host grade. The task-input revision remains separately 2478f73932fd235358105d47301f4f8bc3e9782b. Committed input copies were rechecked against git show at handoff. Local spawn wrappers are coordinator-serialized observations, not raw complete exported host envelopes; see ../decision-trail/evidence-limits.md. Exact tool ordering is observed in the current conversation but independently replayable offline native history remains incomplete.\n\n## Complete actual response\n\nSource artifact: adversarial-review/verdict.md. Original returned prose is preserved below. For Interrogate this is the coordinator's required synthesized verdict; for Reflect this is the independent synthesizer's original full output; for the trail this is the independent final review.\n\n## Intent\n\n> Change deferred invalidation to immediate deletion while preserving disposal correctness.\n\n## Reviewers\n\n| Reviewer | Native identity | Requested model / effort | Observed model / effort | Findings |\n|---|---|---|---|---|\n| A | /root/review_a | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n| B | /root/review_b | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n\nTwo independent native dispatches returned complete results at input revision 2478f73932fd235358105d47301f4f8bc3e9782b. Both received the identical filled template, byte-for-byte shared context, complete rubric and code-quality lens at reviewer-payload.md. Their final outputs were independently read and checked against the code by the coordinator. The actual models were not exposed. This establishes independent worker agreement, not cross-model consensus or model diversity. No sequential substitute was used.\n\n## Act On\n\n1. **Immediate deletion invalidates data still needed by deferred disposal.** A1 and B1, critical. `caller.mjs:5-6` queues a callback through the exact pinned `vendor/disposer-v1.mjs:3`, then immediately deletes the key through `cache.mjs:4`. The microtask later evaluates `get(key).ready` and throws before reporting. This is an ordinary teardown path and violates the stated disposal requirement. Coordinator verification ran the actual probe on case-owned copies: after-state exited 1 with TypeError, before-state exited 0 with `disposed ready: true`. Recommended action is to remove the disposal callback's dependence on continued cache membership, for example by capturing the mounted entry. Do not restore deferred deletion as a fix to an immediate-deletion requirement. No fix was applied.\n\n## Consider\n\nNone. Both reviewers' capture suggestions belong to the same root cause and are not additional findings. The real integration probe should verify immediate disappearance and correct disposal after any future authorized fix.\n\n## Noted\n\nReviewer B noted that repeated teardown and overlapping keys are possible in the supplied design. These predate the change and were explicitly not raised as additional regressions. They remain context, not blockers without a stronger scoped contract.\n\n## Dismissed\n\nNo returned finding was dismissed. Silent optional chaining is rejected as a proposed remedy by both reviewers because it would alter reporting semantics without proving disposal correctness. No reviewer recommended an abstraction, wrapper, type layer or scheduling mechanism requiring separate disposition.\n\n## Agreement Map\n\n| Item | A | B | Lead judgment |\n|---|---|---|---|\n| Deferred callback reads deleted entry | A1 critical | B1 critical | Act On, reproduced with actual probe |\n| Remove callback dependency on mutable cache membership | Suggested | Suggested | Concrete structural simplification for the same issue |\n| Repeated teardown and overlapping-key behavior | No separate finding | Preexisting context only | Noted, outside this regression |\n| Security defect, file-size growth, scattered branching, unnecessary abstraction | None found | None found | No evidence-backed finding in supplied scope |\n\nThere are no lone returned findings and no explicit disagreements. Independent agreement comes from two workers whose actual models are unknown. The pinned disposer digest matches the local manifest. This says nothing about public packages, upstream service behavior, or host-wide parity.\n\n",
        "artifact": {
          "path": "fixtures/durable-01/adversarial-review/adversarial-review.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/adversarial-review.result.md",
          "sha256": "ceb23264c18324f9ecf69312a8162c10297ae6485401013792eb2c4eb3b65e50",
          "bytes": 8919
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/durable-01.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/durable-01.events.jsonl",
            "sha256": "641a8f829bac84bbb209f8b31615620c4c8568902dcc09aef20a840b11bc484c",
            "bytes": 222630,
            "eventReferences": [
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "859273da541e234893b93b03f52f27e5afdb1fa75b275629760ff4ef225d73aa"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "973452edb4093eee5bb9260a8e35897815855baeb7e649380824698f86cda94f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7036a3c6f1576a46faab14dc6e3ec2554c81705c7da11e4bab95a2366ba74b94"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c722a0490fc6249c3edb4acfa704393ea6f84dd787c544e9a3109500b7f7e368",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8866905548d92deaf64bf1a34a7afa5a5f661b813edddfe24aa732e13546d953"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "093c3bcd58b4125b3d02bf7d5fd740b190613b2db6fa8b4ee9004882fc3f379d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f134279cd6b7be6d02bdfacc6b65ff4ec87e5d53fdc637c758992981f9f3e7e4"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c09c156785962492dad34bf7d5fd88b251a56149985741096752cca1ae65999c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5dec2915cbf784fbfa598b24e0faf386786e284c9cc62ded0a47b0424c72c9e6"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5fe8ebd14557871c5c391e884466d15a01e6fc930c6d9a94eb2c50df54b81b5d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "44222457cb2cd86e8a79afcaa04f4a449f2ec26ccbc8e5516ac166407e3099ec"
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "24e3bc7f2a10428aa5aaac17693a26b3e2db18cfacbf4425131b2b9551d7710f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d5a61225b006e5c2fd0daeadf70619c1530fbd17b52cc80ef9687b5f4f038dd2"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2a3d1b28daf68125285c6c7d076b0f77aeece21481a5b8a392bedbefc3a0c037",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "806edbd866499bf9202d175bc7ac591fef26ac81bf33c7fd83715e0cd2d8ac95"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d62ecc74f6af4eeea86b76d1c9b9bef6e477c29542efb00804d5291016a566f4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2f28bf0a362a41ea3fab77cacf0cbcc3240261cf5ea398c4f40ac57d49b7cdb7"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b696c45bb7921c9271b8d350235e0acf57cd41822b50a02cadfe322d9b4af244",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_39",
                "line": 74,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ad8faca34f695f3260bc9352bcec74be136f168fc5ce19423b6ff5e9078a3c1d"
              },
              {
                "eventId": "item_39",
                "line": 75,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "fccfff0db2293c68def1632a4e5d30c98bcccac133bc0df2a74fabce6838b3e7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_43",
                "line": 81,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b7dfbf34dc0ab61b739b406422a2974109666d61a1cc35e26c84318b93071b39"
              },
              {
                "eventId": "item_43",
                "line": 82,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5199329863204b1cdf936284acee2bf1cb1349ab8b535230906ba7e2341351d9",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/durable-01/adversarial-review/verdict.md",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/verdict.md",
            "sha256": "affb68c0c0b4901de4bff8103d797c6e38ca8bd7ced9c5ee3a9a91f537a8519a",
            "bytes": 3460
          },
          {
            "path": "fixtures/durable-01/adversarial-review/reviewer-payload.md",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md",
            "sha256": "68ac944b2aeb52eb09576f287bdce15f67479405a5adf8bb261c24f255af14fa",
            "bytes": 15168
          },
          {
            "path": "fixtures/durable-01/adversarial-review/execution/after.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/execution/after.json",
            "sha256": "9271def765d1c65271de84b37a1613dd6a5833c1908e34125e869300309fd74c",
            "bytes": 180
          },
          {
            "path": "fixtures/durable-01/adversarial-review/freeze-proof.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/freeze-proof.json",
            "sha256": "3838a728c325d7307935d44371fbdb4f0b6155bbb9731704c11883a995745649",
            "bytes": 3228
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_6",
            "item_7",
            "item_8",
            "item_10",
            "item_11",
            "item_18"
          ],
          "actualExecutionEventIds": [
            "item_13",
            "item_15",
            "item_22",
            "item_39",
            "item_43"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/adversarial-review/common-prompt.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/common-prompt.md",
      "sha256": "eee01486cb794ebd8d13894b6a249be66fdc8e585c2062500ec5bf94591da75b",
      "bytes": 15392,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "# Reviewer Prompt Template\n\nBuild each reviewer subagent's prompt from this template, filling in the placeholders.\n\n---\n\nYou are an adversarial code reviewer. Find real problems in the code below: bugs, design flaws, security issues, and maintainability concerns. You are not here to be helpful or encouraging. You are here to stress-test.\n\n## Intent\n\nThe author's stated intent for this change:\n\n> The inferred intent is to make invalidate(key) remove a cache entry synchronously while preserving the caller's deferred disposal callback. This is inferred from invalidation.diff and README, not an author-confirmed PR description. Review that intent using the exact vendored fixture dependency and real caller outside the diff. No public dependency claims.\n\n\nYou are reviewing whether the code achieves this intent well. Do NOT question the intent itself. Assume the goal is correct and challenge the execution.\n\n## Code Under Review\n\n\nFILE invalidation.diff\ndiff --git a/cache.mjs b/cache.mjs\n--- a/cache.mjs\n+++ b/cache.mjs\n@@ -1,4 +1,4 @@\n const entries = new Map();\n export function put(key, value) { entries.set(key, value); }\n export function get(key) { return entries.get(key); }\n-export function invalidate(key) { setTimeout(() => entries.delete(key), 0); }\n+export function invalidate(key) { entries.delete(key); }\n\nFILE cache.mjs\nconst entries = new Map();\nexport function put(key, value) { entries.set(key, value); }\nexport function get(key) { return entries.get(key); }\nexport function invalidate(key) { entries.delete(key); }\n\nFILE caller.mjs\nimport { createDisposer } from './vendor/disposer-v1.mjs';\nimport { get, put, invalidate } from './cache.mjs';\nexport function mount(key, report) {\n  put(key, { ready: true });\n  const subscription = createDisposer(() => report(get(key).ready));\n  return () => { subscription.dispose(); invalidate(key); };\n}\n\nFILE vendor/disposer-v1.mjs\n// Exact vendored fixture dependency implementation, pinned by local SHA-256 in manifest.json.\nexport function createDisposer(onDispose) {\n  return { dispose: () => queueMicrotask(onDispose) };\n}\n\nFILE manifest.json\n{\n  \"scope\": \"exact local vendored fixture only\",\n  \"dependency\": {\n    \"path\": \"vendor/disposer-v1.mjs\",\n    \"version\": \"fixture-v1\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  \"publicPackageClaim\": false\n}\n\nFILE README.md\nReview invalidation.diff against the after-state cache.mjs and the real caller outside the diff. The vendored disposer is the exact locally pinned dependency, not a mock pretending to prove a public dependency. Determine whether synchronous invalidation races the deferred disposal callback. probe.mjs runs this actual supplied implementation and intentionally exits nonzero if teardown throws. A before-state copy may restore the removed setTimeout line to compare ordering. No execution result is supplied.\n\nFILE probe.mjs\nimport { mount } from './caller.mjs';\nlet error;\nprocess.once('uncaughtException', caught => { error = caught; });\nconst unmount = mount('fixture-key', ready => console.log('disposed ready:', ready));\nunmount();\nawait new Promise(resolve => setTimeout(resolve, 5));\nconsole.log(error ? `teardown error: ${error.name}: ${error.message}` : 'teardown completed');\nprocess.exitCode = error ? 1 : 0;\n\n\n## Review Rubric\n\n# Review Rubric\n\nReview through whichever lenses are relevant. Not every lens applies to every change. Use judgment.\n\n## Correctness\n\nDoes the code actually do what the intent says it should?\n\n- Edge cases: empty inputs, nil/undefined, boundary values, concurrent access\n- Error handling: are errors caught, propagated, or silently swallowed?\n- Off-by-one, type coercion, integer overflow, string encoding\n- State management: race conditions, stale closures, dangling references\n- Does the happy path work? Does the sad path work?\n- Idempotency: what happens if this operation runs twice, or if a previous run crashed halfway? If the answer is \"it depends on what state was left behind,\" there's a missing reconciliation step.\n- Concurrency: if multiple actors can touch the same mutable state (files, branches, shared data), is access serialized structurally (locks, sequential phases, exclusive ownership), or by conventions that won't hold?\n\nWhen you find a potential bug, trace the execution path. Don't just flag \"this could be nil\". Show the call chain that makes it nil.\n\n## Root Causes vs. Symptoms\n\nIs the code fixing the actual problem or papering over a symptom?\n\nAnswering this often requires looking beyond the changed files. Read the surrounding code (callers, callees, type definitions, sibling modules) and understand the architecture the change lives in. Use the tools available to you (Read, Grep, Glob) to explore. Follow the call chain. Read the types. Understand why the code exists before judging whether the change addresses the right layer.\n\n- Guard clauses that mask a deeper invariant violation\n- Retry logic that hides a broken contract\n- Type casts that silence a modeling error\n- If you see a workaround, ask: why is the workaround needed? What would a proper fix look like?\n- A fix in module A that should really be a fix in module B's contract\n- Instructions where structure would be better: if the fix is a comment saying \"don't do X\" or a convention someone has to remember, ask whether it could instead be a type constraint, a lint rule, or a runtime check that makes the wrong thing impossible\n\n## Structural Integrity\n\nDoes the code fit well into the system it's part of?\n\n- Boundary discipline: is validation at system boundaries, or scattered through business logic? Validate data once where it enters the system, then trust it internally.\n- Abstraction level: is the code mixing high-level orchestration with low-level detail?\n- Coupling: does this change introduce dependencies that will make future changes harder?\n- Data model fit: do the data structures match the actual access patterns? The right structure makes downstream code obvious. The wrong one fights you at every turn.\n- Bolted-on vs. integrated: was the change patched onto the existing design, or does it read as if the design always accounted for it? If the new requirement had been known from the start, would the code look like this?\n- Legacy dual-paths: does the change introduce a new API while keeping the old one alive? If there are no external consumers, migrate callers and delete the old path in the same wave. Don't leave compatibility layers that will become permanent.\n\nDon't penalize simple code for lacking abstraction. Premature abstraction is worse than duplication.\n\n## Verification\n\nCan you tell that this code works from reading it?\n\n- Are there tests? Do they test behavior or implementation details?\n- Are there assertions/invariants that would catch regressions?\n- If this is a bug fix: is there a test for the bug?\n- If this touches an integration boundary: is the full path tested?\n- Check the real thing, not a proxy. If the code checks liveness via file mtime or cached state instead of reading the actual value, that's a verification gap.\n- For delegated or async work: does the code verify actual output artifacts, or does it trust self-reports and summaries?\n\n## Complexity Budget\n\nIs the complexity justified by what the code accomplishes?\n\n- Code that could be simpler without losing correctness or clarity\n- Abstractions that serve only one call site\n- Configuration or parameterization for cases that don't exist yet\n- Dead code, unused imports, vestigial parameters\n- Over-engineering: \"just in case\" code paths with no current callers\n- Obsolete compatibility paths kept alive for transitional stability that's no longer needed. If the migration is done, delete the scaffolding\n- Does the user experience justify the complexity? Every feature, control, and option should earn its place. Half-finished features are worse than missing ones.\n\nSimpler is better unless simpler is wrong. Three lines of duplication beat a premature abstraction.\n\n## Security\n\nFor each security finding, trace the input path through the code and show it.\n\n- User input flowing to dangerous sinks (SQL, shell, eval, innerHTML) without sanitization\n- Authentication/authorization gaps in new endpoints\n- Secrets in code, logs, or error messages\n- TOCTOU (time-of-check-time-of-use) in security-critical paths\n\n\n## Code Quality Lens\n\n# Code Quality Review\n\nEach reviewer applies this code-quality lens in addition to the rubric. It is a strict standard focused on implementation quality, maintainability, abstraction quality, and codebase health.\n\nAbove all, be ambitious about code structure. Do not merely identify local cleanup. Actively search for \"code judo\" moves, restructurings that preserve behavior while making the implementation dramatically simpler, smaller, more direct, and more elegant.\n\n## Core Prompt\n\nStart from this baseline:\n\n> Perform a deep code quality audit of the current branch's changes.\n> Rethink how to structure / implement the changes to meaningfully improve code quality without impacting behavior.\n> Work to improve abstractions, modularity, reduce Spaghetti code, improve succinctness and legibility.\n> Be ambitious, if there is a clear path to improving the implementation that involves restructuring some of the codebase, go for it.\n> Be extremely thorough and rigorous. Measure twice, cut once.\n\n## Dimensions\n\nEach dimension is stated once. Apply the ones that are relevant.\n\n0. **Be ambitious about structural simplification.** Do not stop at \"this could be a bit cleaner.\" Look for reframings that make whole branches, helpers, modes, conditionals, or layers disappear. Assume a \"code judo\" move is often available. It uses the existing architecture more effectively and makes the change dramatically simpler. If you can delete complexity rather than rearrange it, push hard for that.\n\n1. **Do not let a PR push a file from under 1k lines to over 1k lines without a very strong reason.** Treat this as a strong smell. Prefer extracting helpers, subcomponents, or modules. If the diff crosses that threshold, ask whether the code should be decomposed first. Waive only for a compelling structural reason where the resulting file stays clearly organized.\n\n2. **Do not allow spaghetti growth in existing code.** Be suspicious of new ad-hoc conditionals, scattered special cases, or one-off branches inserted into unrelated flows. Treat \"weird if statements in random places\" as a design problem, not a style nit. Prefer pushing the logic into a dedicated helper, state machine, or module instead of tangling an existing path.\n\n3. **Bias toward cleaning the design, not just accepting working code.** If behavior can stay the same while the structure becomes meaningfully cleaner, push for the cleaner version. Prefer simplifications that remove moving pieces over refactors that spread the same complexity around.\n\n4. **Prefer direct, boring, maintainable code over hacky or magical code.** Treat brittle, ad-hoc, or \"magic\" behavior as a problem. Be skeptical of generic mechanisms that hide simple data-shape assumptions. Flag thin abstractions, identity wrappers, or pass-through helpers that add indirection without buying clarity.\n\n5. **Push on type and boundary cleanliness when it affects maintainability.** Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer type boundary could exist. Prefer explicit typed models over loosely-shaped ad-hoc objects. If a branch leans on a silent fallback to paper over an unclear invariant, ask whether the boundary should be made explicit.\n\n6. **Keep logic in the canonical layer and reuse existing helpers.** Call out feature logic leaking into shared paths or implementation details leaking through APIs. Prefer existing canonical utilities over bespoke one-offs. Push code toward the right package, service, or module instead of normalizing drift.\n\n7. **Treat unnecessary sequential orchestration and non-atomic updates as design smells when the cleaner structure is obvious.** If independent work is serialized for no reason, ask whether it should run in parallel. If related updates can leave state half-applied, push for a more atomic structure. Do not over-index on micro-optimizations, but do flag avoidable orchestration complexity that makes the code more brittle.\n\n## Output Expectations\n\nPrioritize structural code-quality regressions and missed simplifications first, then spaghetti and branching complexity, then boundary, type, and file-size concerns, then smaller modularity and legibility issues.\n\n## Approval Bar\n\nDo not approve merely because behavior seems correct. Treat these as presumptive blockers unless the author can justify them: the PR keeps a lot of incidental complexity when a code-judo move would delete it. Pushes a file from below 1000 lines to above 1000 lines. Adds ad-hoc branching that tangles an existing flow. Scatters feature checks across shared code. Adds an unnecessary abstraction, wrapper, or cast-heavy contract, or duplicates an existing helper or puts logic in the wrong layer when there is a clear canonical home. If those conditions are not met, leave explicit, actionable feedback and push for a cleaner decomposition.\n\n## Review Tone\n\nBe direct, serious, and demanding about quality. Do not be rude, but do not soften major maintainability issues into mild suggestions. If the code is making the codebase messier, say so. If the implementation missed an obvious dramatic simplification, say that too. Do not be satisfied with \"maybe rename this\" when the real issue is structural.\n\n\n## Instructions\n\nReview the code through every lens in the rubric and the code-quality lens above that you find relevant. Do not force lenses that don't apply. A simple bug fix does not need paragraphs about architectural integrity.\n\nFor each finding, provide:\n\n1. **Severity**: `critical` | `warning` | `nit`\n   - `critical`: Would cause bugs, data loss, security issues, or fundamentally broken behavior\n   - `warning`: Design concern, maintainability risk, or correctness issue that isn't immediately broken but will cause pain\n   - `nit`: Style, naming, minor improvement.\n2. **Finding**: What the problem is, in concrete terms. Reference specific lines/functions.\n3. **Evidence**: Why you believe this is a problem. Show your reasoning. Don't just assert.\n4. **Suggestion** (optional): What you'd do instead, if you have a concrete alternative. Skip this if you don't have a clear fix.\n\n## What Makes a Good Finding\n\n- It references specific code, not vague concerns (\"this could be better\")\n- It explains WHY something is a problem, not just THAT it is\n- It distinguishes between \"this is broken\" and \"I would have done this differently\"\n- It considers the stated intent. A finding that ignores the context of what's being built is a bad finding\n\n## What to Avoid\n\n- Restating what the code does without identifying a problem\n- Praising the code. You're an adversary, not a cheerleader. If you find nothing wrong, say \"no findings\" and stop.\n\n## Output\n\nReturn your findings as a structured list. If you have zero findings, say so. An empty review is a valid outcome.\n\n```\n## Findings\n\n### 1. [Severity] Short title\n**Location**: file:line or function name\n**Finding**: What's wrong\n**Evidence**: Why this matters\n**Suggestion**: (optional) What to do instead\n\n### 2. [Severity] Short title\n...\n```\n"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/git-diff-attempt.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/git-diff-attempt.txt",
      "sha256": "b36846cd27f936f669e95e14a9f8f4607fdb8f69e20b0e2db39be822e81d1b00",
      "bytes": 7443,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "warning: Not a git repository. Use --no-index to compare two paths outside a working tree\nusage: git diff --no-index [<options>] <path> <path> [<pathspec>...]\n\nDiff output format options\n    -p, --patch           generate patch\n    -s, --no-patch        suppress diff output\n    -u                    generate patch\n    -U, --unified[=<n>]   generate diffs with <n> lines context\n    -W, --[no-]function-context\n                          generate diffs with <n> lines context\n    --raw                 generate the diff in raw format\n    --patch-with-raw      synonym for '-p --raw'\n    --patch-with-stat     synonym for '-p --stat'\n    --numstat             machine friendly --stat\n    --shortstat           output only the last line of --stat\n    -X, --dirstat[=<param1>,<param2>...]\n                          output the distribution of relative amount of changes for each sub-directory\n    --cumulative          synonym for --dirstat=cumulative\n    --dirstat-by-file[=<param1>,<param2>...]\n                          synonym for --dirstat=files,<param1>,<param2>...\n    --check               warn if changes introduce conflict markers or whitespace errors\n    --summary             condensed summary such as creations, renames and mode changes\n    --name-only           show only names of changed files\n    --name-status         show only names and status of changed files\n    --stat[=<width>[,<name-width>[,<count>]]]\n                          generate diffstat\n    --stat-width <width>  generate diffstat with a given width\n    --stat-name-width <width>\n                          generate diffstat with a given name width\n    --stat-graph-width <width>\n                          generate diffstat with a given graph width\n    --stat-count <count>  generate diffstat with limited lines\n    --[no-]compact-summary\n                          generate compact summary in diffstat\n    --binary              output a binary diff that can be applied\n    --[no-]full-index     show full pre- and post-image object names on the \"index\" lines\n    --[no-]color[=<when>] show colored diff\n    --ws-error-highlight <kind>\n                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff\n    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat\n    --[no-]abbrev[=<n>]   use <n> digits to display object names\n    --src-prefix <prefix> show the given source prefix instead of \"a/\"\n    --dst-prefix <prefix> show the given destination prefix instead of \"b/\"\n    --line-prefix <prefix>\n                          prepend an additional prefix to every line of output\n    --no-prefix           do not show any source or destination prefix\n    --default-prefix      use default prefixes a/ and b/\n    --inter-hunk-context <n>\n                          show context between diff hunks up to the specified number of lines\n    --output-indicator-new <char>\n                          specify the character to indicate a new line instead of '+'\n    --output-indicator-old <char>\n                          specify the character to indicate an old line instead of '-'\n    --output-indicator-context <char>\n                          specify the character to indicate a context instead of ' '\n\nDiff rename options\n    -B, --break-rewrites[=<n>[/<m>]]\n                          break complete rewrite changes into pairs of delete and create\n    -M, --find-renames[=<n>]\n                          detect renames\n    -D, --irreversible-delete\n                          omit the preimage for deletes\n    -C, --find-copies[=<n>]\n                          detect copies\n    --[no-]find-copies-harder\n                          use unmodified files as source to find copies\n    --no-renames          disable rename detection\n    --[no-]rename-empty   use empty blobs as rename source\n    --[no-]follow         continue listing the history of a file beyond renames\n    -l <n>                limit to cheap rename/copy detection if the number of rename/copy targets exceeds this value\n\nDiff algorithm options\n    --minimal             produce the smallest possible diff\n    -w, --ignore-all-space\n                          ignore whitespace when comparing lines\n    -b, --ignore-space-change\n                          ignore changes in amount of whitespace\n    --ignore-space-at-eol ignore changes in whitespace at EOL\n    --ignore-cr-at-eol    ignore carrier-return at the end of line\n    --ignore-blank-lines  ignore changes whose lines are all blank\n    -I, --[no-]ignore-matching-lines <regex>\n                          ignore changes whose all lines match <regex>\n    --[no-]indent-heuristic\n                          heuristic to shift diff hunk boundaries for easy reading\n    --patience            generate diff using the \"patience diff\" algorithm\n    --histogram           generate diff using the \"histogram diff\" algorithm\n    --diff-algorithm <algorithm>\n                          choose a diff algorithm\n    --anchored <text>     generate diff using the \"anchored diff\" algorithm\n    --word-diff[=<mode>]  show word diff, using <mode> to delimit changed words\n    --word-diff-regex <regex>\n                          use <regex> to decide what a word is\n    --color-words[=<regex>]\n                          equivalent to --word-diff=color --word-diff-regex=<regex>\n    --[no-]color-moved[=<mode>]\n                          moved lines of code are colored differently\n    --[no-]color-moved-ws <mode>\n                          how white spaces are ignored in --color-moved\n\nOther diff options\n    --[no-]relative[=<prefix>]\n                          when run from subdir, exclude changes outside and show relative paths\n    -a, --[no-]text       treat all files as text\n    -R                    swap two inputs, reverse the diff\n    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise\n    --[no-]quiet          disable all output of the program\n    --[no-]ext-diff       allow an external diff helper to be executed\n    --[no-]textconv       run external text conversion filters when comparing binary files\n    --ignore-submodules[=<when>]\n                          ignore changes to submodules in the diff generation\n    --submodule[=<format>]\n                          specify how differences in submodules are shown\n    --ita-invisible-in-index\n                          hide 'git add -N' entries from the index\n    --ita-visible-in-index\n                          treat 'git add -N' entries as real in the index\n    -S <string>           look for differences that change the number of occurrences of the specified string\n    -G <regex>            look for differences that change the number of occurrences of the specified regex\n    --pickaxe-all         show all changes in the changeset with -S or -G\n    --pickaxe-regex       treat <string> in -S as extended POSIX regular expression\n    -O <file>             control the order in which files appear in the output\n    --rotate-to <path>    show the change in the specified path first\n    --skip-to <path>      skip the output to the specified path\n    --find-object <object-id>\n                          look for differences that change the number of occurrences of the specified object\n    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]\n                          select files by diff type\n    --max-depth <depth>   maximum tree depth to recurse\n    --output <file>       output to a specific file\n\n"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/intent.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/intent.md",
      "sha256": "98f8930ec34caf21cfba063598b2c2a1a5cf55c7f5b103236f5b3aca24e6fa16",
      "bytes": 358,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "The inferred intent is to make invalidate(key) remove a cache entry synchronously while preserving the caller's deferred disposal callback. This is inferred from invalidation.diff and README, not an author-confirmed PR description. Review that intent using the exact vendored fixture dependency and real caller outside the diff. No public dependency claims.\n"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/reviewer-a.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/reviewer-a.md",
      "sha256": "0243e7d5c1e709fe2de57f4a4d6de78850e6d542c6e2aaf2a55ce8c6a5057d54",
      "bytes": 727,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "Assignment review-a-v1 retry0. Worker /root/review_a. Prompt hash verified eee01486cb794ebd8d13894b6a249be66fdc8e585c2062500ec5bf94591da75b. One critical finding, no warnings or nits. Synchronous deletion in cache.mjs:4 breaks deferred disposal via caller.mjs:5-6 and vendor/disposer-v1.mjs:3. mount stores ready true, dispose queues callback, invalidate deletes entry, callback reads undefined.ready. Probe exited1 with teardown TypeError. Suggest retain mounted value and test immediate removal plus deferred report. Applicable correctness, root cause, structure and verification. No supported security, complexity or file-size findings. This is the complete finding content transcribed by coordinator, with prose condensed.\n"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/reviewer-b.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/reviewer-b.md",
      "sha256": "0e9181809e2000945a1f5fcf05f034c586b13fd884f95b4c19fc7250710ddee4",
      "bytes": 668,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "Assignment review-b-v1 retry0. Worker /root/review_b. Same prompt hash verified. One critical finding. Synchronous invalidation deletes entry before queued disposal reads get(key).ready, so report never runs. Locations cache.mjs:4, caller.mjs:5-6, vendored queueMicrotask. Probe exited1 with teardown TypeError. Suggest retain value and report value.ready. Optional chaining would conceal broken contract. Correctness, root cause, structure, verification; code quality dimensions3,4,5,6. No separate security, complexity, file-size or style finding. No task Git SHA and no public dependency claim. Complete finding content transcribed by coordinator, prose condensed.\n"
    },
    {
      "path": "fixtures/batch-06/adversarial-review.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review.result.md",
      "sha256": "2d797944421c0431ec26dc472aedddaf54fe4e90b478c62a48950bdc9c1127e1",
      "bytes": 5542,
      "owners": [
        "grades-native-06.json#4"
      ],
      "text": "# adversarial-review\n\n## Supplied input\n\n> Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.\n\nNamed source files and exact copied source bytes are retained in [adversarial-review/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/source-manifest.json) and [adversarial-review/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/adversarial-review/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Intent\n\nMake invalidate(key) remove a cache entry synchronously while preserving the caller's deferred disposal callback. This intent is inferred from supplied README and diff, not confirmed by a live PR description. No current Git diff exists. The prepared invalidation.diff is the review target.\n\n## Reviewers\n\nBoth reviewers received identical common-prompt.md containing intent, full diff, surrounding caller, exact vendor implementation, manifest, probe, all six rubric lenses and the complete code-quality lens. Its independently checked SHA256 is eee01486cb794ebd8d13894b6a249be66fdc8e585c2062500ec5bf94591da75b.\n\n- Reviewer A, /root/review_a, requested inherit-parent model/effort, actual unknown, one critical finding.\n- Reviewer B, /root/review_b, requested inherit-parent model/effort, actual unknown, one critical finding.\n\nNative worker identities and returned results were observed and inspected. Model diversity is unverified. Full input Git SHA is unavailable. reviewer-a.md and reviewer-b.md retain the complete finding content in coordinator-condensed prose. Worker self-reports of execution were checked against the parent's actual probe.\n\n## Act On\n\nBoth reviewers identify one concrete lifetime regression at input/cache.mjs:4 through caller.mjs:5-6 and vendor/disposer-v1.mjs:3. dispose queues a microtask. Synchronous invalidate deletes the entry before that callback reads get(key).ready, so teardown throws and report never runs. Parent run exits1 and prints \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\". Restoring the removed timer line in a separate before/ copy exits0 with \"disposed ready: true\" and \"teardown completed\". Exact results are in command-results.json.\n\nThis warrants action because the normal integration path breaks. Retain the mounted value rather than querying invalidated shared membership in the callback, and test both immediate removal and eventual report. This is a recommendation only. The current fixture was not fixed.\n\n## Consider\n\nNone of the independent reviewers raised a separate finding in this category. Identity-bound ownership for overlapping mounts is a useful future API design consideration from Arena, but is not promoted here into independent review consensus or a proven new regression from this diff.\n\n## Noted\n\nNo separate low-priority findings. The dependency is the exact locally pinned vendored fixture, SHA256 d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f. No public dependency or live service behavior is inferred.\n\n## Dismissed\n\nNo reviewer finding was dismissed. Optional chaining would hide the failed report contract and is rejected as a proposed response, not represented as a reviewer finding. There is no evidence for inventing security, size or style blockers.\n\n## Agreement Map\n\nIndependent workers agree on the same one correctness/root-cause/structure/verification finding. No lone finding or explicit disagreement exists. Security and complexity lenses yield no supported additional finding. The code-quality lens favors removing lifetime coupling rather than adding a timing workaround or abstraction. Agreement is worker consensus, not observed multi-model consensus. Lead judgment accepts the one reproduced issue. No changes were auto-applied, and no external defaults or settings were changed.\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/adversarial-review.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/adversarial-review.result.md",
      "sha256": "ceb23264c18324f9ecf69312a8162c10297ae6485401013792eb2c4eb3b65e50",
      "bytes": 8919,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "# adversarial-review\n\nObserved result: two native independent reviewers completed; both found one critical disposal regression, which the coordinator reproduced. Actual model diversity is unverified. No grade is assigned.\n\n## Supplied input\n\nTask payload: “Intent: change deferred invalidation to immediate deletion while preserving disposal correctness. Supply every independent reviewer the identical diff, dependent caller, exact pinned dependency bytes, full template, rubric and code-quality lens at one SHA. Inspect all worker findings and lead-classify every deduplicated item into Act On/Consider/Noted/Dismissed, with attributed Agreement Map. Do not apply a fix or open a PR. Actual model diversity must be observed or limited explicitly.”\n\nVerified task input HEAD: `2478f73932fd235358105d47301f4f8bc3e9782b`. Plugin freeze supplied separately: `f4623636a287bea2aa79c4b2234a53d20a5f193c`, installed 0.1.0 exact path prefix `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/`. Source paths read in full: skills/interrogate/SKILL.md and references/code-quality-review.md, lead-judgment.md, reviewer-prompt.md, rubric.md. Original source snapshots and digests: sources.json and sources/. Original fixture locations are recorded in the user's supplied request; execution and assignments use committed-inputs bytes extracted by git show, never mutable shared inputs. inputs.json records each Git path, revision, extracted copy and SHA256. Full supplied case definitions are also retained in supplied-contracts.json.\n\n## Actual response\n\nThe complete required verdict is verdict.md, including Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map. The complete filled identical reviewer template is reviewer-payload.md. Reviewer A returned a JSON object in review-a/returned.json; B returned Markdown in review-b/returned.md. Both originals are retained. Every returned finding has a disposition in the verdict.\n\n## Actual tools and observations\n\n- functions.exec with tools.exec_command read exact installed sources and repository instructions, ran git rev-parse HEAD, git status and git show; reads and setup exited 0. The first large combined source read truncated; the affected rubric and reflection context were subsequently read in separate calls. No claim rests on the truncated portion.\n- collaboration.list_agents returned the running root. collaboration.spawn_agent accepted review_a then review_b and returned /root/review_a and /root/review_b. Exact spawn arguments, returned objects and dispatch order are in each review directory's spawn.json. Immutable assignments predate dispatch. Both pending declarations are preserved; subsequent statuses belong to events.jsonl rather than edits to original assignment scope.\n- Native final notifications returned A then B. Both contained the assigned input revision and full findings. functions.exec / exec_command read both persisted responses before synthesis. No operation exit code exists for native spawn or returned final messages; they return objects and messages, not process statuses.\n- Bun executed run-checks.mjs, which ran the supplied probe against case-owned after and before copies. execution/after.json records exit 1 and actual TypeError; execution/before.json records exit 0 and completed teardown. The deliberate before variant restores only the removed setTimeout deletion. No committed input was edited.\n- Bun invoked installed TypeScript 5.9.3 with --version, exit 0. This is compiler execution proof only and is recorded under ../decision-trail/compiler.json; no TypeScript correctness is claimed for these JavaScript fixtures.\n\n## Variants and limits\n\nIndependent native review ran; sequential fallback was inapplicable. The supplied before and after implementations both actually executed. No requested historical Claude or Grok defaults were attempted, configured or substituted. Exposed choices were GPT variants or inherit-parent; neither returned worker object exposes an actual model. The whole review covers exact local pinned bytes only. No fix, PR, commit, package update, external action or service call occurred. Arena and Swarm are not cases in this group; their receipt schemas are not asserted for this Interrogate workflow. Assignment events and original native payloads are preserved without invented telemetry.\n\n## Final verification addendum\n\nfreeze-proof.json independently compares every requested installed source file and saved snapshot with git show at package revision f4623636a287bea2aa79c4b2234a53d20a5f193c in the existing local package repository. All requested bytes match. This is source identity verification, not a behavioral host grade. The task-input revision remains separately 2478f73932fd235358105d47301f4f8bc3e9782b. Committed input copies were rechecked against git show at handoff. Local spawn wrappers are coordinator-serialized observations, not raw complete exported host envelopes; see ../decision-trail/evidence-limits.md. Exact tool ordering is observed in the current conversation but independently replayable offline native history remains incomplete.\n\n## Complete actual response\n\nSource artifact: adversarial-review/verdict.md. Original returned prose is preserved below. For Interrogate this is the coordinator's required synthesized verdict; for Reflect this is the independent synthesizer's original full output; for the trail this is the independent final review.\n\n## Intent\n\n> Change deferred invalidation to immediate deletion while preserving disposal correctness.\n\n## Reviewers\n\n| Reviewer | Native identity | Requested model / effort | Observed model / effort | Findings |\n|---|---|---|---|---|\n| A | /root/review_a | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n| B | /root/review_b | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n\nTwo independent native dispatches returned complete results at input revision 2478f73932fd235358105d47301f4f8bc3e9782b. Both received the identical filled template, byte-for-byte shared context, complete rubric and code-quality lens at reviewer-payload.md. Their final outputs were independently read and checked against the code by the coordinator. The actual models were not exposed. This establishes independent worker agreement, not cross-model consensus or model diversity. No sequential substitute was used.\n\n## Act On\n\n1. **Immediate deletion invalidates data still needed by deferred disposal.** A1 and B1, critical. `caller.mjs:5-6` queues a callback through the exact pinned `vendor/disposer-v1.mjs:3`, then immediately deletes the key through `cache.mjs:4`. The microtask later evaluates `get(key).ready` and throws before reporting. This is an ordinary teardown path and violates the stated disposal requirement. Coordinator verification ran the actual probe on case-owned copies: after-state exited 1 with TypeError, before-state exited 0 with `disposed ready: true`. Recommended action is to remove the disposal callback's dependence on continued cache membership, for example by capturing the mounted entry. Do not restore deferred deletion as a fix to an immediate-deletion requirement. No fix was applied.\n\n## Consider\n\nNone. Both reviewers' capture suggestions belong to the same root cause and are not additional findings. The real integration probe should verify immediate disappearance and correct disposal after any future authorized fix.\n\n## Noted\n\nReviewer B noted that repeated teardown and overlapping keys are possible in the supplied design. These predate the change and were explicitly not raised as additional regressions. They remain context, not blockers without a stronger scoped contract.\n\n## Dismissed\n\nNo returned finding was dismissed. Silent optional chaining is rejected as a proposed remedy by both reviewers because it would alter reporting semantics without proving disposal correctness. No reviewer recommended an abstraction, wrapper, type layer or scheduling mechanism requiring separate disposition.\n\n## Agreement Map\n\n| Item | A | B | Lead judgment |\n|---|---|---|---|\n| Deferred callback reads deleted entry | A1 critical | B1 critical | Act On, reproduced with actual probe |\n| Remove callback dependency on mutable cache membership | Suggested | Suggested | Concrete structural simplification for the same issue |\n| Repeated teardown and overlapping-key behavior | No separate finding | Preexisting context only | Noted, outside this regression |\n| Security defect, file-size growth, scattered branching, unnecessary abstraction | None found | None found | No evidence-backed finding in supplied scope |\n\nThere are no lone returned findings and no explicit disagreements. Independent agreement comes from two workers whose actual models are unknown. The pinned disposer digest matches the local manifest. This says nothing about public packages, upstream service behavior, or host-wide parity.\n\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/artifact-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/artifact-inventory.json",
      "sha256": "7eff3d5647df1f4090d745a72d37adce6a9ea820c3b78f8b066044f57700b844",
      "bytes": 7788,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"adversarial-review/sources.json\",\n    \"bytes\": 1575,\n    \"sha256\": \"1309a99c4f626a0cf9dba8d5f84878d0d74db6bb62686b4429e6467fd2892514\"\n  },\n  {\n    \"path\": \"adversarial-review/bindings.json\",\n    \"bytes\": 1854,\n    \"sha256\": \"9b0aaafe378ed40a641ab6ed70adb11da893b4ad125d7acccaa53d6ffecd3123\"\n  },\n  {\n    \"path\": \"adversarial-review/freeze-proof.json\",\n    \"bytes\": 3228,\n    \"sha256\": \"3838a728c325d7307935d44371fbdb4f0b6155bbb9731704c11883a995745649\"\n  },\n  {\n    \"path\": \"adversarial-review/supplied-contracts.json\",\n    \"bytes\": 16443,\n    \"sha256\": \"5761bb98aeefb88031bd265e849a310bf755b17b2ae7a41370874162600f3d0d\"\n  },\n  {\n    \"path\": \"adversarial-review/verdict.md\",\n    \"bytes\": 3460,\n    \"sha256\": \"affb68c0c0b4901de4bff8103d797c6e38ca8bd7ced9c5ee3a9a91f537a8519a\"\n  },\n  {\n    \"path\": \"adversarial-review/review-b/dispatch.txt\",\n    \"bytes\": 732,\n    \"sha256\": \"d363f03c54a3fa0bc20ef2cd3b9d216aeb485b6fa425786f872bd14aa3a7507a\"\n  },\n  {\n    \"path\": \"adversarial-review/review-b/assignment.json\",\n    \"bytes\": 629,\n    \"sha256\": \"6b0f740186a6a6cd1bc46eeb8cfe2dc41d4c669fc571351a57009b46038b4870\"\n  },\n  {\n    \"path\": \"adversarial-review/review-b/returned.md\",\n    \"bytes\": 3307,\n    \"sha256\": \"44255acb9c74429c101beaaaa44b54f289fc9c3ed20a828083d5bd25a7646a14\"\n  },\n  {\n    \"path\": \"adversarial-review/review-b/spawn.json\",\n    \"bytes\": 1053,\n    \"sha256\": \"89533a9495d6d35649d0c18776298772077c4b6afb1e008015205b27ffb9b5eb\"\n  },\n  {\n    \"path\": \"adversarial-review/events.jsonl\",\n    \"bytes\": 1520,\n    \"sha256\": \"8b1949a3b21bc4bc45019284b4011dcf7cebcc881135907b0e2078d0739e2387\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs.json\",\n    \"bytes\": 1944,\n    \"sha256\": \"1796752e671a780a142d0c8fec22380f239eea9582cbae1cbb269e411528ace0\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before.json\",\n    \"bytes\": 137,\n    \"sha256\": \"7a0bb3aac1cb56d42f3ce3ca9eeadaa52964c0d8fde917ada336b322ab995809\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after.json\",\n    \"bytes\": 180,\n    \"sha256\": \"9271def765d1c65271de84b37a1613dd6a5833c1908e34125e869300309fd74c\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/probe.mjs\",\n    \"bytes\": 395,\n    \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/invalidation.diff\",\n    \"bytes\": 365,\n    \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/README.md\",\n    \"bytes\": 509,\n    \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/caller.mjs\",\n    \"bytes\": 309,\n    \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/manifest.json\",\n    \"bytes\": 253,\n    \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/cache.mjs\",\n    \"bytes\": 220,\n    \"sha256\": \"b9ff3cf490c78675ef169324135630dcd5741dbd031de81d2798f7c67c020dea\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/before/vendor/disposer-v1.mjs\",\n    \"bytes\": 196,\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/probe.mjs\",\n    \"bytes\": 395,\n    \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/invalidation.diff\",\n    \"bytes\": 365,\n    \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/README.md\",\n    \"bytes\": 509,\n    \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/caller.mjs\",\n    \"bytes\": 309,\n    \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/manifest.json\",\n    \"bytes\": 253,\n    \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/cache.mjs\",\n    \"bytes\": 199,\n    \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n  },\n  {\n    \"path\": \"adversarial-review/execution/after/vendor/disposer-v1.mjs\",\n    \"bytes\": 196,\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  {\n    \"path\": \"adversarial-review/reviewer-payload.md\",\n    \"bytes\": 15168,\n    \"sha256\": \"68ac944b2aeb52eb09576f287bdce15f67479405a5adf8bb261c24f255af14fa\"\n  },\n  {\n    \"path\": \"adversarial-review/sources/interrogate__references__reviewer-prompt.md\",\n    \"bytes\": 2491,\n    \"sha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\"\n  },\n  {\n    \"path\": \"adversarial-review/sources/interrogate__SKILL.md\",\n    \"bytes\": 5853,\n    \"sha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\"\n  },\n  {\n    \"path\": \"adversarial-review/sources/interrogate__references__lead-judgment.md\",\n    \"bytes\": 3465,\n    \"sha256\": \"6e5bdf5670eb34017692e9b6c546f36ac7552e6bb9f3f2f3429164fcc46a9361\"\n  },\n  {\n    \"path\": \"adversarial-review/sources/interrogate__references__code-quality-review.md\",\n    \"bytes\": 5217,\n    \"sha256\": \"79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8\"\n  },\n  {\n    \"path\": \"adversarial-review/sources/interrogate__references__rubric.md\",\n    \"bytes\": 5025,\n    \"sha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\"\n  },\n  {\n    \"path\": \"adversarial-review/verification.json\",\n    \"bytes\": 605,\n    \"sha256\": \"a2a91b1888d73608daaa4aa46bc1f2ad0bc50f328543f537af81177f39473281\"\n  },\n  {\n    \"path\": \"adversarial-review/adversarial-review.result.md\",\n    \"bytes\": 8919,\n    \"sha256\": \"ceb23264c18324f9ecf69312a8162c10297ae6485401013792eb2c4eb3b65e50\"\n  },\n  {\n    \"path\": \"adversarial-review/review-a/dispatch.txt\",\n    \"bytes\": 732,\n    \"sha256\": \"d51d5ec4703ff47e3b3ebef45784a8127d699e8cea9578f8e26a82359c54e1b7\"\n  },\n  {\n    \"path\": \"adversarial-review/review-a/assignment.json\",\n    \"bytes\": 629,\n    \"sha256\": \"6e85e8d72656d8a040da1f81cc16ad2502d95659b48416da92a06e61f84ff8ec\"\n  },\n  {\n    \"path\": \"adversarial-review/review-a/returned.json\",\n    \"bytes\": 4157,\n    \"sha256\": \"7e2eb701badcfae6681bb79c7db0052fc5087baf39264e5cef08e64fdc0de3a4\"\n  },\n  {\n    \"path\": \"adversarial-review/review-a/spawn.json\",\n    \"bytes\": 1053,\n    \"sha256\": \"8580d4eeca3a95ace35325a6970e406a966acf04990ddd6ef7ca4cc3b85ef6b2\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/probe.mjs\",\n    \"bytes\": 395,\n    \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/invalidation.diff\",\n    \"bytes\": 365,\n    \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/README.md\",\n    \"bytes\": 509,\n    \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/caller.mjs\",\n    \"bytes\": 309,\n    \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/manifest.json\",\n    \"bytes\": 253,\n    \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/cache.mjs\",\n    \"bytes\": 199,\n    \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n  },\n  {\n    \"path\": \"adversarial-review/inputs/cache/vendor/disposer-v1.mjs\",\n    \"bytes\": 196,\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/bindings.json",
      "sha256": "9b0aaafe378ed40a641ab6ed70adb11da893b4ad125d7acccaa53d6ffecd3123",
      "bytes": 1854,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"adversarial-review/sources.json\",\n    \"limits\": \"Full requested source bytes read; large truncated read followed by affected separate full reads\"\n  },\n  {\n    \"operation\": \"spawn\",\n    \"tool\": \"collaboration.spawn_agent\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"adversarial-review/events.jsonl\",\n    \"limits\": \"Native operation returned worker identity; full host envelope export unavailable\"\n  },\n  {\n    \"operation\": \"inspect-result\",\n    \"tool\": \"exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"adversarial-review/adversarial-review.result.md\",\n    \"limits\": \"Full original returned findings read; worker internal tool history not exported\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"adversarial-review/freeze-proof.json\",\n    \"limits\": \"Observed process results; native collaboration returns do not have exit codes\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"apply_patch and exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"adversarial-review/adversarial-review.result.md\",\n    \"limits\": \"Local write and readback only; not proof of unattended recovery\"\n  },\n  {\n    \"operation\": \"history\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": \"decision-trail/history-limits.md\",\n    \"limits\": \"Visible active context and bounded digest available; no raw active transcript path/export binding supplied\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": \"adversarial-review/adversarial-review.result.md\",\n    \"limits\": \"No authorization and no attempt\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/execution/after.json",
      "sha256": "9271def765d1c65271de84b37a1613dd6a5833c1908e34125e869300309fd74c",
      "bytes": 180,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"args\": [\n    \"bun\",\n    \"probe.mjs\"\n  ],\n  \"exitCode\": 1,\n  \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/execution/before.json",
      "sha256": "7a0bb3aac1cb56d42f3ce3ca9eeadaa52964c0d8fde917ada336b322ab995809",
      "bytes": 137,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"args\": [\n    \"bun\",\n    \"probe.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"disposed ready: true\\nteardown completed\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/freeze-proof.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/freeze-proof.json",
      "sha256": "3838a728c325d7307935d44371fbdb4f0b6155bbb9731704c11883a995745649",
      "bytes": 3228,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"results\": [\n    {\n      \"args\": [\n        \"git\",\n        \"-C\",\n        \"/Users/digital-hawk/Herd/pstack-openai\",\n        \"show\",\n        \"f4623636a287bea2aa79c4b2234a53d20a5f193c:skills/interrogate/SKILL.md\"\n      ],\n      \"exitCode\": 0,\n      \"stderr\": \"\",\n      \"gitPath\": \"skills/interrogate/SKILL.md\",\n      \"frozenSha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\",\n      \"installedSha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\",\n      \"snapshotSha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\",\n      \"matches\": true\n    },\n    {\n      \"args\": [\n        \"git\",\n        \"-C\",\n        \"/Users/digital-hawk/Herd/pstack-openai\",\n        \"show\",\n        \"f4623636a287bea2aa79c4b2234a53d20a5f193c:skills/interrogate/references/code-quality-review.md\"\n      ],\n      \"exitCode\": 0,\n      \"stderr\": \"\",\n      \"gitPath\": \"skills/interrogate/references/code-quality-review.md\",\n      \"frozenSha256\": \"79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8\",\n      \"installedSha256\": \"79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8\",\n      \"snapshotSha256\": \"79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8\",\n      \"matches\": true\n    },\n    {\n      \"args\": [\n        \"git\",\n        \"-C\",\n        \"/Users/digital-hawk/Herd/pstack-openai\",\n        \"show\",\n        \"f4623636a287bea2aa79c4b2234a53d20a5f193c:skills/interrogate/references/lead-judgment.md\"\n      ],\n      \"exitCode\": 0,\n      \"stderr\": \"\",\n      \"gitPath\": \"skills/interrogate/references/lead-judgment.md\",\n      \"frozenSha256\": \"6e5bdf5670eb34017692e9b6c546f36ac7552e6bb9f3f2f3429164fcc46a9361\",\n      \"installedSha256\": \"6e5bdf5670eb34017692e9b6c546f36ac7552e6bb9f3f2f3429164fcc46a9361\",\n      \"snapshotSha256\": \"6e5bdf5670eb34017692e9b6c546f36ac7552e6bb9f3f2f3429164fcc46a9361\",\n      \"matches\": true\n    },\n    {\n      \"args\": [\n        \"git\",\n        \"-C\",\n        \"/Users/digital-hawk/Herd/pstack-openai\",\n        \"show\",\n        \"f4623636a287bea2aa79c4b2234a53d20a5f193c:skills/interrogate/references/reviewer-prompt.md\"\n      ],\n      \"exitCode\": 0,\n      \"stderr\": \"\",\n      \"gitPath\": \"skills/interrogate/references/reviewer-prompt.md\",\n      \"frozenSha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\",\n      \"installedSha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\",\n      \"snapshotSha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\",\n      \"matches\": true\n    },\n    {\n      \"args\": [\n        \"git\",\n        \"-C\",\n        \"/Users/digital-hawk/Herd/pstack-openai\",\n        \"show\",\n        \"f4623636a287bea2aa79c4b2234a53d20a5f193c:skills/interrogate/references/rubric.md\"\n      ],\n      \"exitCode\": 0,\n      \"stderr\": \"\",\n      \"gitPath\": \"skills/interrogate/references/rubric.md\",\n      \"frozenSha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\",\n      \"installedSha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\",\n      \"snapshotSha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\",\n      \"matches\": true\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/inputs.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/inputs.json",
      "sha256": "1796752e671a780a142d0c8fec22380f239eea9582cbae1cbb269e411528ace0",
      "bytes": 1944,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "[\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/README.md\",\n    \"artifact\": \"adversarial-review/inputs/cache/README.md\",\n    \"sha256\": \"b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/cache.mjs\",\n    \"artifact\": \"adversarial-review/inputs/cache/cache.mjs\",\n    \"sha256\": \"e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/caller.mjs\",\n    \"artifact\": \"adversarial-review/inputs/cache/caller.mjs\",\n    \"sha256\": \"9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/invalidation.diff\",\n    \"artifact\": \"adversarial-review/inputs/cache/invalidation.diff\",\n    \"sha256\": \"0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/manifest.json\",\n    \"artifact\": \"adversarial-review/inputs/cache/manifest.json\",\n    \"sha256\": \"5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/probe.mjs\",\n    \"artifact\": \"adversarial-review/inputs/cache/probe.mjs\",\n    \"sha256\": \"fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002\"\n  },\n  {\n    \"revision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n    \"path\": \"committed-inputs/additional/cache/vendor/disposer-v1.mjs\",\n    \"artifact\": \"adversarial-review/inputs/cache/vendor/disposer-v1.mjs\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-a/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/assignment.json",
      "sha256": "6e85e8d72656d8a040da1f81cc16ad2502d95659b48416da92a06e61f84ff8ec",
      "bytes": 629,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"id\": \"review-a\",\n  \"scope\": \"Review identical pinned invalidation diff, caller and dependency\",\n  \"inputRevision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n  \"outputOwner\": \"review-a\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a\",\n  \"role\": \"adversarial reviewer A\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"adversarial-review/inputs.json\",\n    \"adversarial-review/reviewer-payload.md\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-a/dispatch.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/dispatch.txt",
      "sha256": "d51d5ec4703ff47e3b3ebef45784a8127d699e8cea9578f8e26a82359c54e1b7",
      "bytes": 732,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "Assignment review-a. Read the immutable assignment at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/assignment.json and the FULL identical filled reviewer template at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md. Apply every relevant rubric and code-quality lens. Read-only; write no files. Return the full structured findings with assignment id and input revision. Your result is captured by coordinator in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/returned.json. Do not infer actual model from request. No further delegation."
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-a/returned.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/returned.json",
      "sha256": "7e2eb701badcfae6681bb79c7db0052fc5087baf39264e5cef08e64fdc0de3a4",
      "bytes": 4157,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"assignmentId\": \"review-a\",\n  \"inputRevision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n  \"actualModel\": \"unknown\",\n  \"findingCount\": 1,\n  \"findings\": [\n    {\n      \"id\": \"A1\",\n      \"severity\": \"critical\",\n      \"title\": \"Immediate deletion breaks the deferred disposal callback\",\n      \"location\": \"cache.mjs:4; caller.mjs:5-6; vendor/disposer-v1.mjs:3\",\n      \"finding\": \"The change achieves immediate deletion but violates the explicit requirement to preserve disposal correctness. An ordinary mount followed by its returned teardown now schedules a callback that dereferences a deleted entry.\",\n      \"evidence\": [\n        \"mount stores { ready: true } under the key.\",\n        \"createDisposer receives a callback that evaluates get(key).ready when the callback executes, rather than capturing the stored value.\",\n        \"The returned teardown calls subscription.dispose(), whose exact pinned implementation invokes queueMicrotask(onDispose). That call schedules the callback; it does not execute the callback synchronously.\",\n        \"The teardown next calls invalidate(key), which now deletes the entry synchronously.\",\n        \"When the microtask executes, get(key) returns undefined and evaluating .ready throws TypeError before report is called.\",\n        \"Before the change, invalidate scheduled a timer. The disposal microtask ran before that timer, so the entry remained available during disposal.\",\n        \"I independently read the supplied after-state cache, dependent caller, pinned disposer and probe through actual tools. git rev-parse HEAD returned the assigned input revision. I did not run the probe or claim an observed runtime result.\"\n      ],\n      \"suggestion\": \"Keep immediate invalidation while removing the disposer callback's dependence on future cache membership. For this supplied caller, capture the mounted entry or required disposal value when creating the subscription. Verify the actual mount-to-teardown path against the exact pinned dependency. An optional-chaining fallback would suppress the exception while changing the disposal result, so it would not establish the required correctness.\",\n      \"lenses\": [\n        \"Correctness: asynchronous ordering, state lifetime and observable teardown failure\",\n        \"Root causes versus symptoms: caller's disposal contract depends on deferred cache retention\",\n        \"Structural integrity: immediate cache deletion and asynchronous disposal need compatible ownership of disposal data\",\n        \"Code quality: a direct captured disposal value can remove the implicit timing dependency without adding scheduling layers\"\n      ]\n    }\n  ],\n  \"coverage\": {\n    \"correctness\": \"Traced the complete mount, dispose, invalidate and microtask execution chain.\",\n    \"rootCauses\": \"The root cause is disposal data being retrieved from cache after its new lifetime ends.\",\n    \"structuralIntegrity\": \"Covered in A1; no separate evidence-backed structural finding.\",\n    \"verification\": \"The supplied probe exercises the real integration boundary and intentionally fails on an uncaught teardown error. Execution was not performed because this assignment authorized execution only against its assigned copy and supplied no executable copy within review-a.\",\n    \"complexityBudget\": \"No added abstraction, branching, compatibility path or unnecessary parameterization in the one-line change.\",\n    \"security\": \"No demonstrated dangerous input-to-sink path, authorization boundary or secret exposure in the supplied scope.\",\n    \"codeQualityDimensions\": \"Applied structural simplification, directness, canonical ownership, boundary cleanliness and ordering concerns. File-size growth, casts, scattered conditionals and unnecessary wrappers do not apply to this supplied diff.\"\n  },\n  \"limits\": [\n    \"Actual reviewer model identity was not exposed in observed tool results; requested or inherited model selection is not evidence of diversity.\",\n    \"No runtime execution, source modification, commit or external action was performed.\",\n    \"The vendored fixture supports conclusions about these exact dependency bytes only; it establishes no public-package behavior.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-a/spawn.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/spawn.json",
      "sha256": "8580d4eeca3a95ace35325a6970e406a966acf04990ddd6ef7ca4cc3b85ef6b2",
      "bytes": 1053,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"tool\": \"collaboration.spawn_agent\",\n  \"arguments\": {\n    \"task_name\": \"review_a\",\n    \"message\": \"Assignment review-a. Read the immutable assignment at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/assignment.json and the FULL identical filled reviewer template at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md. Input revision 2478f73932fd235358105d47301f4f8bc3e9782b, plugin freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. Apply every relevant rubric and code-quality lens. Read-only; write no files. Return full structured findings with assignment id and input revision. Your result is captured by coordinator in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-a/returned.json. Do not infer actual model from request. No further delegation.\",\n    \"fork_turns\": \"all\"\n  },\n  \"returned\": {\n    \"task_name\": \"/root/review_a\"\n  },\n  \"dispatchOrder\": 1\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-b/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/assignment.json",
      "sha256": "6b0f740186a6a6cd1bc46eeb8cfe2dc41d4c669fc571351a57009b46038b4870",
      "bytes": 629,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"id\": \"review-b\",\n  \"scope\": \"Review identical pinned invalidation diff, caller and dependency\",\n  \"inputRevision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n  \"outputOwner\": \"review-b\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b\",\n  \"role\": \"adversarial reviewer B\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"adversarial-review/inputs.json\",\n    \"adversarial-review/reviewer-payload.md\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-b/dispatch.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/dispatch.txt",
      "sha256": "d363f03c54a3fa0bc20ef2cd3b9d216aeb485b6fa425786f872bd14aa3a7507a",
      "bytes": 732,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "Assignment review-b. Read the immutable assignment at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/assignment.json and the FULL identical filled reviewer template at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md. Apply every relevant rubric and code-quality lens. Read-only; write no files. Return the full structured findings with assignment id and input revision. Your result is captured by coordinator in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/returned.json. Do not infer actual model from request. No further delegation."
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-b/returned.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/returned.md",
      "sha256": "44255acb9c74429c101beaaaa44b54f289fc9c3ed20a828083d5bd25a7646a14",
      "bytes": 3307,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "Assignment: `review-b`  \nInput revision: `2478f73932fd235358105d47301f4f8bc3e9782b`  \nRequested model: inherited. Observed actual model: unknown.\n\nRead the assignment, complete filled reviewer payload, and all five exact interrogate source files through command tools. Verified repository `HEAD` equals the supplied input revision. All read commands exited `0`. No files written, runtime execution performed, fixes applied, or further delegation requested.\n\n## Findings\n\n### 1. [critical] Immediate deletion breaks the existing deferred disposal callback\n\n**Location:** `cache.mjs:4`, `caller.mjs:5-6`, `vendor/disposer-v1.mjs:3`\n\n**Finding:** The change implements immediate deletion but violates the explicit requirement to preserve disposal correctness. Ordinary teardown now causes the disposal callback to dereference `undefined`.\n\n**Evidence:** The supplied, exact pinned implementation gives this execution path:\n\n1. `mount(key, report)` stores `{ ready: true }`.\n2. The returned teardown invokes `subscription.dispose()`.\n3. `dispose()` queues `onDispose` using `queueMicrotask`; it does not execute it synchronously.\n4. Teardown immediately calls the changed `invalidate(key)`, which deletes the entry before returning.\n5. The queued callback then evaluates `report(get(key).ready)`.\n6. `get(key)` returns `undefined`, so evaluating `.ready` throws before `report` runs.\n\nThe previous `setTimeout` deletion allowed the microtask callback to read the entry before the timer removed it. This conclusion follows from the provided caller and vendored dependency, rather than an assumed public dependency contract. It is a static execution trace; I did not run the probe.\n\n**Suggestion:** Preserve immediate cache deletion while making disposal independent of the cache entry’s continued existence. For this caller, capture the mounted entry in the callback instead of looking it up after teardown. Validate the resulting full `mount → teardown → queued callback` behavior against the actual pinned dependency, including that the entry disappears immediately and reporting still completes correctly. Optional chaining alone would suppress the exception while changing reporting semantics.\n\n## Lens coverage\n\n- **Correctness:** Concrete teardown failure traced above; immediate deletion itself is achieved.\n- **Root cause and structural integrity:** The callback’s lifetime exceeds its cache entry’s lifetime. Fix that ownership relationship rather than adding a silent fallback or restoring deferred invalidation contrary to the stated intent.\n- **Verification:** A full integration probe is supplied in the fixture inventory, but this reviewer did not execute it. No runtime outcome claimed.\n- **Complexity and code quality:** The relevant simplification is removing the delayed callback’s dependency on mutable global cache lookup. No evidence supports additional abstractions, file decomposition, type layers, or branching.\n- **Security:** No traced security issue in the supplied slice.\n- **Idempotency and overlapping keys:** The supplied code also permits repeated teardown and shared-key interference, but those behaviors predate this one-line diff. I do not raise them as additional regressions without a stronger scoped contract.\n\nFinding count: **1 critical, 0 warnings, 0 nits**.\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/review-b/spawn.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/spawn.json",
      "sha256": "89533a9495d6d35649d0c18776298772077c4b6afb1e008015205b27ffb9b5eb",
      "bytes": 1053,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"tool\": \"collaboration.spawn_agent\",\n  \"arguments\": {\n    \"task_name\": \"review_b\",\n    \"message\": \"Assignment review-b. Read the immutable assignment at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/assignment.json and the FULL identical filled reviewer template at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md. Input revision 2478f73932fd235358105d47301f4f8bc3e9782b, plugin freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. Apply every relevant rubric and code-quality lens. Read-only; write no files. Return full structured findings with assignment id and input revision. Your result is captured by coordinator in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/review-b/returned.json. Do not infer actual model from request. No further delegation.\",\n    \"fork_turns\": \"all\"\n  },\n  \"returned\": {\n    \"task_name\": \"/root/review_b\"\n  },\n  \"dispatchOrder\": 2\n}"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/reviewer-payload.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/reviewer-payload.md",
      "sha256": "68ac944b2aeb52eb09576f287bdce15f67479405a5adf8bb261c24f255af14fa",
      "bytes": 15168,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "Input revision: 2478f73932fd235358105d47301f4f8bc3e9782b. The exact committed-inputs bytes above were extracted with git show. Read-only review; no fixes, external services, installations or commits. Report assignmentId, inputRevision and observed actual model only if host metadata exposes it; otherwise unknown. Execution only against your assigned case-owned copy; return findings through final response.\n\n# Reviewer Prompt Template\n\nBuild each reviewer subagent's prompt from this template, filling in the placeholders.\n\n---\n\nYou are an adversarial code reviewer. Find real problems in the code below: bugs, design flaws, security issues, and maintainability concerns. You are not here to be helpful or encouraging. You are here to stress-test.\n\n## Intent\n\nThe author's stated intent for this change:\n\n> Change deferred invalidation to immediate deletion while preserving disposal correctness.\n\nYou are reviewing whether the code achieves this intent well. Do NOT question the intent itself. Assume the goal is correct and challenge the execution.\n\n## Code Under Review\n\n### cache.mjs\n\n```\nconst entries = new Map();\nexport function put(key, value) { entries.set(key, value); }\nexport function get(key) { return entries.get(key); }\nexport function invalidate(key) { entries.delete(key); }\n```\n\n### caller.mjs\n\n```\nimport { createDisposer } from './vendor/disposer-v1.mjs';\nimport { get, put, invalidate } from './cache.mjs';\nexport function mount(key, report) {\n  put(key, { ready: true });\n  const subscription = createDisposer(() => report(get(key).ready));\n  return () => { subscription.dispose(); invalidate(key); };\n}\n```\n\n### vendor/disposer-v1.mjs\n\n```\n// Exact vendored fixture dependency implementation, pinned by local SHA-256 in manifest.json.\nexport function createDisposer(onDispose) {\n  return { dispose: () => queueMicrotask(onDispose) };\n}\n```\n\n### manifest.json\n\n```\n{\n  \"scope\": \"exact local vendored fixture only\",\n  \"dependency\": {\n    \"path\": \"vendor/disposer-v1.mjs\",\n    \"version\": \"fixture-v1\",\n    \"sha256\": \"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\"\n  },\n  \"publicPackageClaim\": false\n}\n```\n\n### invalidation.diff\n\n```\ndiff --git a/cache.mjs b/cache.mjs\n--- a/cache.mjs\n+++ b/cache.mjs\n@@ -1,4 +1,4 @@\n const entries = new Map();\n export function put(key, value) { entries.set(key, value); }\n export function get(key) { return entries.get(key); }\n-export function invalidate(key) { setTimeout(() => entries.delete(key), 0); }\n+export function invalidate(key) { entries.delete(key); }\n```\n\n### README.md\n\n```\nReview invalidation.diff against the after-state cache.mjs and the real caller outside the diff. The vendored disposer is the exact locally pinned dependency, not a mock pretending to prove a public dependency. Determine whether synchronous invalidation races the deferred disposal callback. probe.mjs runs this actual supplied implementation and intentionally exits nonzero if teardown throws. A before-state copy may restore the removed setTimeout line to compare ordering. No execution result is supplied.\n```\n\n\n## Review Rubric\n\n# Review Rubric\n\nReview through whichever lenses are relevant. Not every lens applies to every change. Use judgment.\n\n## Correctness\n\nDoes the code actually do what the intent says it should?\n\n- Edge cases: empty inputs, nil/undefined, boundary values, concurrent access\n- Error handling: are errors caught, propagated, or silently swallowed?\n- Off-by-one, type coercion, integer overflow, string encoding\n- State management: race conditions, stale closures, dangling references\n- Does the happy path work? Does the sad path work?\n- Idempotency: what happens if this operation runs twice, or if a previous run crashed halfway? If the answer is \"it depends on what state was left behind,\" there's a missing reconciliation step.\n- Concurrency: if multiple actors can touch the same mutable state (files, branches, shared data), is access serialized structurally (locks, sequential phases, exclusive ownership), or by conventions that won't hold?\n\nWhen you find a potential bug, trace the execution path. Don't just flag \"this could be nil\". Show the call chain that makes it nil.\n\n## Root Causes vs. Symptoms\n\nIs the code fixing the actual problem or papering over a symptom?\n\nAnswering this often requires looking beyond the changed files. Read the surrounding code (callers, callees, type definitions, sibling modules) and understand the architecture the change lives in. Use the tools available to you (Read, Grep, Glob) to explore. Follow the call chain. Read the types. Understand why the code exists before judging whether the change addresses the right layer.\n\n- Guard clauses that mask a deeper invariant violation\n- Retry logic that hides a broken contract\n- Type casts that silence a modeling error\n- If you see a workaround, ask: why is the workaround needed? What would a proper fix look like?\n- A fix in module A that should really be a fix in module B's contract\n- Instructions where structure would be better: if the fix is a comment saying \"don't do X\" or a convention someone has to remember, ask whether it could instead be a type constraint, a lint rule, or a runtime check that makes the wrong thing impossible\n\n## Structural Integrity\n\nDoes the code fit well into the system it's part of?\n\n- Boundary discipline: is validation at system boundaries, or scattered through business logic? Validate data once where it enters the system, then trust it internally.\n- Abstraction level: is the code mixing high-level orchestration with low-level detail?\n- Coupling: does this change introduce dependencies that will make future changes harder?\n- Data model fit: do the data structures match the actual access patterns? The right structure makes downstream code obvious. The wrong one fights you at every turn.\n- Bolted-on vs. integrated: was the change patched onto the existing design, or does it read as if the design always accounted for it? If the new requirement had been known from the start, would the code look like this?\n- Legacy dual-paths: does the change introduce a new API while keeping the old one alive? If there are no external consumers, migrate callers and delete the old path in the same wave. Don't leave compatibility layers that will become permanent.\n\nDon't penalize simple code for lacking abstraction. Premature abstraction is worse than duplication.\n\n## Verification\n\nCan you tell that this code works from reading it?\n\n- Are there tests? Do they test behavior or implementation details?\n- Are there assertions/invariants that would catch regressions?\n- If this is a bug fix: is there a test for the bug?\n- If this touches an integration boundary: is the full path tested?\n- Check the real thing, not a proxy. If the code checks liveness via file mtime or cached state instead of reading the actual value, that's a verification gap.\n- For delegated or async work: does the code verify actual output artifacts, or does it trust self-reports and summaries?\n\n## Complexity Budget\n\nIs the complexity justified by what the code accomplishes?\n\n- Code that could be simpler without losing correctness or clarity\n- Abstractions that serve only one call site\n- Configuration or parameterization for cases that don't exist yet\n- Dead code, unused imports, vestigial parameters\n- Over-engineering: \"just in case\" code paths with no current callers\n- Obsolete compatibility paths kept alive for transitional stability that's no longer needed. If the migration is done, delete the scaffolding\n- Does the user experience justify the complexity? Every feature, control, and option should earn its place. Half-finished features are worse than missing ones.\n\nSimpler is better unless simpler is wrong. Three lines of duplication beat a premature abstraction.\n\n## Security\n\nFor each security finding, trace the input path through the code and show it.\n\n- User input flowing to dangerous sinks (SQL, shell, eval, innerHTML) without sanitization\n- Authentication/authorization gaps in new endpoints\n- Secrets in code, logs, or error messages\n- TOCTOU (time-of-check-time-of-use) in security-critical paths\n\n\n## Code Quality Lens\n\n# Code Quality Review\n\nEach reviewer applies this code-quality lens in addition to the rubric. It is a strict standard focused on implementation quality, maintainability, abstraction quality, and codebase health.\n\nAbove all, be ambitious about code structure. Do not merely identify local cleanup. Actively search for \"code judo\" moves, restructurings that preserve behavior while making the implementation dramatically simpler, smaller, more direct, and more elegant.\n\n## Core Prompt\n\nStart from this baseline:\n\n> Perform a deep code quality audit of the current branch's changes.\n> Rethink how to structure / implement the changes to meaningfully improve code quality without impacting behavior.\n> Work to improve abstractions, modularity, reduce Spaghetti code, improve succinctness and legibility.\n> Be ambitious, if there is a clear path to improving the implementation that involves restructuring some of the codebase, go for it.\n> Be extremely thorough and rigorous. Measure twice, cut once.\n\n## Dimensions\n\nEach dimension is stated once. Apply the ones that are relevant.\n\n0. **Be ambitious about structural simplification.** Do not stop at \"this could be a bit cleaner.\" Look for reframings that make whole branches, helpers, modes, conditionals, or layers disappear. Assume a \"code judo\" move is often available. It uses the existing architecture more effectively and makes the change dramatically simpler. If you can delete complexity rather than rearrange it, push hard for that.\n\n1. **Do not let a PR push a file from under 1k lines to over 1k lines without a very strong reason.** Treat this as a strong smell. Prefer extracting helpers, subcomponents, or modules. If the diff crosses that threshold, ask whether the code should be decomposed first. Waive only for a compelling structural reason where the resulting file stays clearly organized.\n\n2. **Do not allow spaghetti growth in existing code.** Be suspicious of new ad-hoc conditionals, scattered special cases, or one-off branches inserted into unrelated flows. Treat \"weird if statements in random places\" as a design problem, not a style nit. Prefer pushing the logic into a dedicated helper, state machine, or module instead of tangling an existing path.\n\n3. **Bias toward cleaning the design, not just accepting working code.** If behavior can stay the same while the structure becomes meaningfully cleaner, push for the cleaner version. Prefer simplifications that remove moving pieces over refactors that spread the same complexity around.\n\n4. **Prefer direct, boring, maintainable code over hacky or magical code.** Treat brittle, ad-hoc, or \"magic\" behavior as a problem. Be skeptical of generic mechanisms that hide simple data-shape assumptions. Flag thin abstractions, identity wrappers, or pass-through helpers that add indirection without buying clarity.\n\n5. **Push on type and boundary cleanliness when it affects maintainability.** Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer type boundary could exist. Prefer explicit typed models over loosely-shaped ad-hoc objects. If a branch leans on a silent fallback to paper over an unclear invariant, ask whether the boundary should be made explicit.\n\n6. **Keep logic in the canonical layer and reuse existing helpers.** Call out feature logic leaking into shared paths or implementation details leaking through APIs. Prefer existing canonical utilities over bespoke one-offs. Push code toward the right package, service, or module instead of normalizing drift.\n\n7. **Treat unnecessary sequential orchestration and non-atomic updates as design smells when the cleaner structure is obvious.** If independent work is serialized for no reason, ask whether it should run in parallel. If related updates can leave state half-applied, push for a more atomic structure. Do not over-index on micro-optimizations, but do flag avoidable orchestration complexity that makes the code more brittle.\n\n## Output Expectations\n\nPrioritize structural code-quality regressions and missed simplifications first, then spaghetti and branching complexity, then boundary, type, and file-size concerns, then smaller modularity and legibility issues.\n\n## Approval Bar\n\nDo not approve merely because behavior seems correct. Treat these as presumptive blockers unless the author can justify them: the PR keeps a lot of incidental complexity when a code-judo move would delete it. Pushes a file from below 1000 lines to above 1000 lines. Adds ad-hoc branching that tangles an existing flow. Scatters feature checks across shared code. Adds an unnecessary abstraction, wrapper, or cast-heavy contract, or duplicates an existing helper or puts logic in the wrong layer when there is a clear canonical home. If those conditions are not met, leave explicit, actionable feedback and push for a cleaner decomposition.\n\n## Review Tone\n\nBe direct, serious, and demanding about quality. Do not be rude, but do not soften major maintainability issues into mild suggestions. If the code is making the codebase messier, say so. If the implementation missed an obvious dramatic simplification, say that too. Do not be satisfied with \"maybe rename this\" when the real issue is structural.\n\n\n## Instructions\n\nReview the code through every lens in the rubric and the code-quality lens above that you find relevant. Do not force lenses that don't apply. A simple bug fix does not need paragraphs about architectural integrity.\n\nFor each finding, provide:\n\n1. **Severity**: `critical` | `warning` | `nit`\n   - `critical`: Would cause bugs, data loss, security issues, or fundamentally broken behavior\n   - `warning`: Design concern, maintainability risk, or correctness issue that isn't immediately broken but will cause pain\n   - `nit`: Style, naming, minor improvement.\n2. **Finding**: What the problem is, in concrete terms. Reference specific lines/functions.\n3. **Evidence**: Why you believe this is a problem. Show your reasoning. Don't just assert.\n4. **Suggestion** (optional): What you'd do instead, if you have a concrete alternative. Skip this if you don't have a clear fix.\n\n## What Makes a Good Finding\n\n- It references specific code, not vague concerns (\"this could be better\")\n- It explains WHY something is a problem, not just THAT it is\n- It distinguishes between \"this is broken\" and \"I would have done this differently\"\n- It considers the stated intent. A finding that ignores the context of what's being built is a bad finding\n\n## What to Avoid\n\n- Restating what the code does without identifying a problem\n- Praising the code. You're an adversary, not a cheerleader. If you find nothing wrong, say \"no findings\" and stop.\n\n## Output\n\nReturn your findings as a structured list. If you have zero findings, say so. An empty review is a valid outcome.\n\n```\n## Findings\n\n### 1. [Severity] Short title\n**Location**: file:line or function name\n**Finding**: What's wrong\n**Evidence**: Why this matters\n**Suggestion**: (optional) What to do instead\n\n### 2. [Severity] Short title\n...\n```\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/sources.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/sources.json",
      "sha256": "1309a99c4f626a0cf9dba8d5f84878d0d74db6bb62686b4429e6467fd2892514",
      "bytes": 1575,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/SKILL.md\",\n    \"artifact\": \"adversarial-review/sources/interrogate__SKILL.md\",\n    \"sha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/code-quality-review.md\",\n    \"artifact\": \"adversarial-review/sources/interrogate__references__code-quality-review.md\",\n    \"sha256\": \"79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/lead-judgment.md\",\n    \"artifact\": \"adversarial-review/sources/interrogate__references__lead-judgment.md\",\n    \"sha256\": \"6e5bdf5670eb34017692e9b6c546f36ac7552e6bb9f3f2f3429164fcc46a9361\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/reviewer-prompt.md\",\n    \"artifact\": \"adversarial-review/sources/interrogate__references__reviewer-prompt.md\",\n    \"sha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/rubric.md\",\n    \"artifact\": \"adversarial-review/sources/interrogate__references__rubric.md\",\n    \"sha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\"\n  }\n]"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/supplied-contracts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/supplied-contracts.json",
      "sha256": "5761bb98aeefb88031bd265e849a310bf755b17b2ae7a41370874162600f3d0d",
      "bytes": 16443,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "[\n  {\n    \"contract\": {\n      \"id\": \"adversarial-review\",\n      \"sourcePaths\": [\n        \"skills/interrogate/SKILL.md\",\n        \"skills/interrogate/references/code-quality-review.md\",\n        \"skills/interrogate/references/lead-judgment.md\",\n        \"skills/interrogate/references/reviewer-prompt.md\",\n        \"skills/interrogate/references/rubric.md\"\n      ],\n      \"prompt\": \"Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.\",\n      \"requirements\": [\n        \"State intent and give every competing reviewer the identical diff, context, rubric and code-quality lens.\",\n        \"Preserve all rubric lenses, evidence-based findings and pragmatic lead judgment across act on, consider, noted and dismissed categories.\",\n        \"Report reviewer models, finding counts, independent consensus, lone findings and disagreements in the complete verdict format.\",\n        \"Verify independent worker results and observed model diversity; disclose sequential review as reduced capability.\",\n        \"Do not auto-apply changes or create external changes to fix rejected model defaults.\"\n      ],\n      \"expectedFull\": \"Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit.\",\n      \"expectedReduced\": \"When independent workers are unavailable, an authorized sequential review applies the complete rubric and lead judgment and labels reduced capability. It does not claim independent agreement or model diversity; unknown actual models remain unknown.\",\n      \"expectedBlocked\": \"Unavailable diff or context, or denied review capability, blocks grounded findings. Report the missing source or permission without inventing findings, reviewer execution or agreement.\",\n      \"forbiddenClaims\": [\n        \"Sequential passes are independent reviewers.\",\n        \"Requested model names prove actual model diversity.\",\n        \"The rubric or code-quality lens can be omitted.\",\n        \"A review authorizes automatic fixes or an external PR.\",\n        \"Structural checks establish host behavioral parity.\"\n      ],\n      \"caseFile\": \"docs/parity/cases/skills/interrogate.json\"\n    },\n    \"caseId\": \"adversarial-review\",\n    \"baselineBatch\": \"batch-06\",\n    \"baselineState\": \"active-or-not-yet-finished\",\n    \"baselineGrade\": null,\n    \"selectionReason\": \"Registry pass requires workers\",\n    \"sourcePaths\": [\n      \"skills/interrogate/SKILL.md\",\n      \"skills/interrogate/references/code-quality-review.md\",\n      \"skills/interrogate/references/lead-judgment.md\",\n      \"skills/interrogate/references/reviewer-prompt.md\",\n      \"skills/interrogate/references/rubric.md\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/interrogate.json\",\n    \"expectedFullUnchanged\": \"Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit.\",\n    \"inputFixtures\": [\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/invalidation.diff\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/caller.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/vendor/disposer-v1.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/manifest.json\"\n    ],\n    \"taskPayload\": \"Intent: change deferred invalidation to immediate deletion while preserving disposal correctness. Supply every independent reviewer the identical diff, dependent caller, exact pinned dependency bytes, full template, rubric and code-quality lens at one SHA. Inspect all worker findings and lead-classify every deduplicated item into Act On/Consider/Noted/Dismissed, with attributed Agreement Map. Do not apply a fix or open a PR. Actual model diversity must be observed or limited explicitly.\",\n    \"missingPrerequisites\": [\n      \"At least two independent reviewer completions\",\n      \"All source templates/rubric/lenses read in full\",\n      \"Any execution only against case-owned copies\"\n    ],\n    \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n    \"sourceFiles\": [\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/SKILL.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/code-quality-review.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/lead-judgment.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/reviewer-prompt.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/rubric.md\"\n    ]\n  },\n  {\n    \"contract\": {\n      \"id\": \"approval-before-edit\",\n      \"sourcePaths\": [\n        \"skills/reflect/SKILL.md\",\n        \"skills/reflect/references/divergent-reviewer.md\",\n        \"skills/reflect/references/judgment-reviewer.md\",\n        \"skills/reflect/references/synthesizer.md\",\n        \"skills/reflect/references/tooling-reviewer.md\"\n      ],\n      \"prompt\": \"Reflect on this active session. Review the judgment, tooling and divergent lenses, synthesize all findings, and propose durable skill improvements. Show all Accepted, Rejected and Backlog items before editing. I have not approved any edits or tracker writes.\",\n      \"requirements\": [\n        \"Authorized active-session history or an explicitly limited digest\",\n        \"Independent reviewers and synthesizer with observed spawn and result inspection for full behavior\",\n        \"Read access to referenced context and target skills\",\n        \"Explicit user approval of the Accepted subset before skill changes\",\n        \"Authorized writes and available authoring/validation workflow for approved substantive edits\"\n      ],\n      \"expectedFull\": \"Locate only the active transcript or disclose a digest fallback. Run three independent parallel reviewers with the complete judgment, tooling and divergent prompts, then an independent synthesizer with their full outputs. Preserve evidence, actual-use/missed-trigger routing, already-covered rejection and structural Backlog checks. Present the full Accepted/Rejected/Backlog result and wait for explicit subset approval before edits. File Backlog only with explicit tracker authorization. Use the approved authoring workflow for substantive changes and descriptions; verify any validator and written results before reporting.\",\n      \"expectedReduced\": \"If independent workers are unavailable, disclose reduced capability and apply all three lenses and synthesis sequentially without claiming independence or model diversity. Use a limited digest when history is unavailable. Preserve full output and the explicit approval gate. Without an authoring workflow or tracker authorization, return drafts and unfiled Backlog with limits.\",\n      \"expectedBlocked\": \"Without usable authorized history or digest, block evidence-backed reflection. Denied reads block affected findings. Without explicit approval, apply no Accepted edit. Denied writes or unavailable required authoring/validation block the affected application and leave proposals reviewable.\",\n      \"forbiddenClaims\": [\n        \"Skill edits before explicit Accepted-subset approval\",\n        \"Automatic tracker writes without explicit authorization\",\n        \"Sequential role passes described as independent reviewers\",\n        \"Reading unrelated workspace chats to locate the active transcript\",\n        \"Requested models represented as observed models or guaranteed diversity\",\n        \"Invented citations, applied edits, filed issues or host passes\"\n      ],\n      \"caseFile\": \"docs/parity/cases/skills/reflect.json\"\n    },\n    \"caseId\": \"approval-before-edit\",\n    \"baselineBatch\": \"batch-06\",\n    \"baselineState\": \"active-or-not-yet-finished\",\n    \"baselineGrade\": null,\n    \"selectionReason\": \"Registry pass requires workers\",\n    \"sourcePaths\": [\n      \"skills/reflect/SKILL.md\",\n      \"skills/reflect/references/divergent-reviewer.md\",\n      \"skills/reflect/references/judgment-reviewer.md\",\n      \"skills/reflect/references/synthesizer.md\",\n      \"skills/reflect/references/tooling-reviewer.md\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/reflect.json\",\n    \"expectedFullUnchanged\": \"Locate only the active transcript or disclose a digest fallback. Run three independent parallel reviewers with the complete judgment, tooling and divergent prompts, then an independent synthesizer with their full outputs. Preserve evidence, actual-use/missed-trigger routing, already-covered rejection and structural Backlog checks. Present the full Accepted/Rejected/Backlog result and wait for explicit subset approval before edits. File Backlog only with explicit tracker authorization. Use the approved authoring workflow for substantive changes and descriptions; verify any validator and written results before reporting.\",\n    \"inputFixtures\": [\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/history.json\"\n    ],\n    \"taskPayload\": \"Use the ACTUAL durable rerun session transcript when available; otherwise disclose the supplied fixture digest as a limited digest. Run three independent parallel reviewers using the complete judgment/tooling/divergent prompts, then a fresh independent synthesizer after all full reviewer outputs arrive. Present all Accepted/Rejected/Backlog items and stop before any skill edit or tracker write. No Accepted-subset approval is supplied.\",\n    \"missingPrerequisites\": [\n      \"Three parallel reviewers plus fresh synthesizer, respecting actual capacity\",\n      \"Authorized active-session transcript or explicitly limited supplied digest\",\n      \"Lack of subset approval intentionally closes all edit branches\"\n    ],\n    \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n    \"sourceFiles\": [\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/SKILL.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/divergent-reviewer.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/judgment-reviewer.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/synthesizer.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/tooling-reviewer.md\"\n    ]\n  },\n  {\n    \"contract\": {\n      \"id\": \"decision-trail\",\n      \"sourcePaths\": [\n        \"skills/show-me-your-work/SKILL.md\",\n        \"skills/show-me-your-work/references/decision-log-template.tsv\",\n        \"skills/show-me-your-work/scripts/log.sh\"\n      ],\n      \"prompt\": \"Keep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.\",\n      \"requirements\": [\n        \"Authorized local persistence and readback\",\n        \"Accessible history for this run\",\n        \"task 16 logging helper or equally safe TSV append\",\n        \"Authorized independent reviewer with observed different model family for full review\"\n      ],\n      \"expectedFull\": \"Save and read back one canonical six-column TSV with sanitized single-line cells and formula-prefix protection. Preserve run start boundaries and append-only corrections. Resolve evidence, audit this run against its transcript, and obtain independent different-family review. End every trail-producing reply with Attention, observed reviewer model and row-specific flags or No flags. Exclude secrets and unobserved results.\",\n      \"expectedReduced\": \"When history or different-family review is unavailable, preserve the local trail and report the precise audit or review gap in Attention. Sequential self-review is reduced capability and never substitutes for independent cross-model review. If durable writes are unavailable, provide an unsaved in-chat handoff only when authorized and disclose that no durable trail was saved.\",\n      \"expectedBlocked\": \"Denied persistence blocks a claimed saved trail. Missing helper blocks helper execution unless an authorized equivalent preserves sanitization. Missing transcript or observed different-family reviewer blocks the corresponding full audit or cross-model claim. Report denied or unavailable capabilities without invented success.\",\n      \"forbiddenClaims\": [\n        \"Secrets or private unrelated transcripts in the trail\",\n        \"Saved trail without write and readback\",\n        \"Edited or deleted prior rows\",\n        \"Independent cross-model review from self-review or unknown model family\",\n        \"Tests green, completed work or evidence resolution without observation\",\n        \"Commit, publication or external writes without explicit authorization\"\n      ],\n      \"caseFile\": \"docs/parity/cases/skills/show-me-your-work.json\"\n    },\n    \"caseId\": \"decision-trail\",\n    \"baselineBatch\": \"batch-07\",\n    \"baselineState\": \"active-or-not-yet-finished\",\n    \"baselineGrade\": null,\n    \"selectionReason\": \"Registry pass requires workers\",\n    \"sourcePaths\": [\n      \"skills/show-me-your-work/SKILL.md\",\n      \"skills/show-me-your-work/references/decision-log-template.tsv\",\n      \"skills/show-me-your-work/scripts/log.sh\"\n    ],\n    \"caseFile\": \"docs/parity/cases/skills/show-me-your-work.json\",\n    \"expectedFullUnchanged\": \"Save and read back one canonical six-column TSV with sanitized single-line cells and formula-prefix protection. Preserve run start boundaries and append-only corrections. Resolve evidence, audit this run against its transcript, and obtain independent different-family review. End every trail-producing reply with Attention, observed reviewer model and row-specific flags or No flags. Exclude secrets and unobserved results.\",\n    \"inputFixtures\": [\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/history.json\"\n    ],\n    \"taskPayload\": \"During this rerun record a canonical six-column TSV through the actual supplied log helper, set a run boundary, and append a correction rather than changing an old row. Sanitize newlines/formula prefixes. Read back every persisted row and audit only this run against its actual transcript. Request a genuinely independent different-family reviewer with full transcript and TSV; inspect its row-specific flags. If different-family selection or actual-family observation is unavailable, preserve the trail and mark that review gate unmet; same-family independence cannot silently satisfy it.\",\n    \"missingPrerequisites\": [\n      \"Observed independent different-family review is REQUIRED for full case\",\n      \"Actual run transcript and boundary; supplied synthetic history is context only\",\n      \"Canonical helper use and real readback\"\n    ],\n    \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n    \"sourceFiles\": [\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/SKILL.md\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/references/decision-log-template.tsv\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\"\n    ]\n  }\n]"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/verdict.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/verdict.md",
      "sha256": "affb68c0c0b4901de4bff8103d797c6e38ca8bd7ced9c5ee3a9a91f537a8519a",
      "bytes": 3460,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "## Intent\n\n> Change deferred invalidation to immediate deletion while preserving disposal correctness.\n\n## Reviewers\n\n| Reviewer | Native identity | Requested model / effort | Observed model / effort | Findings |\n|---|---|---|---|---|\n| A | /root/review_a | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n| B | /root/review_b | inherit-parent / inherit-parent | unknown / unknown | 1 critical |\n\nTwo independent native dispatches returned complete results at input revision 2478f73932fd235358105d47301f4f8bc3e9782b. Both received the identical filled template, byte-for-byte shared context, complete rubric and code-quality lens at reviewer-payload.md. Their final outputs were independently read and checked against the code by the coordinator. The actual models were not exposed. This establishes independent worker agreement, not cross-model consensus or model diversity. No sequential substitute was used.\n\n## Act On\n\n1. **Immediate deletion invalidates data still needed by deferred disposal.** A1 and B1, critical. `caller.mjs:5-6` queues a callback through the exact pinned `vendor/disposer-v1.mjs:3`, then immediately deletes the key through `cache.mjs:4`. The microtask later evaluates `get(key).ready` and throws before reporting. This is an ordinary teardown path and violates the stated disposal requirement. Coordinator verification ran the actual probe on case-owned copies: after-state exited 1 with TypeError, before-state exited 0 with `disposed ready: true`. Recommended action is to remove the disposal callback's dependence on continued cache membership, for example by capturing the mounted entry. Do not restore deferred deletion as a fix to an immediate-deletion requirement. No fix was applied.\n\n## Consider\n\nNone. Both reviewers' capture suggestions belong to the same root cause and are not additional findings. The real integration probe should verify immediate disappearance and correct disposal after any future authorized fix.\n\n## Noted\n\nReviewer B noted that repeated teardown and overlapping keys are possible in the supplied design. These predate the change and were explicitly not raised as additional regressions. They remain context, not blockers without a stronger scoped contract.\n\n## Dismissed\n\nNo returned finding was dismissed. Silent optional chaining is rejected as a proposed remedy by both reviewers because it would alter reporting semantics without proving disposal correctness. No reviewer recommended an abstraction, wrapper, type layer or scheduling mechanism requiring separate disposition.\n\n## Agreement Map\n\n| Item | A | B | Lead judgment |\n|---|---|---|---|\n| Deferred callback reads deleted entry | A1 critical | B1 critical | Act On, reproduced with actual probe |\n| Remove callback dependency on mutable cache membership | Suggested | Suggested | Concrete structural simplification for the same issue |\n| Repeated teardown and overlapping-key behavior | No separate finding | Preexisting context only | Noted, outside this regression |\n| Security defect, file-size growth, scattered branching, unnecessary abstraction | None found | None found | No evidence-backed finding in supplied scope |\n\nThere are no lone returned findings and no explicit disagreements. Independent agreement comes from two workers whose actual models are unknown. The pinned disposer digest matches the local manifest. This says nothing about public packages, upstream service behavior, or host-wide parity.\n"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/verification.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-01/adversarial-review/verification.json",
      "sha256": "a2a91b1888d73608daaa4aa46bc1f2ad0bc50f328543f537af81177f39473281",
      "bytes": 605,
      "owners": [
        "grades-native-durable-01.json#0"
      ],
      "text": "{\n  \"inputRevision\": \"2478f73932fd235358105d47301f4f8bc3e9782b\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"head\": {\n    \"args\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"2478f73932fd235358105d47301f4f8bc3e9782b\\n\",\n    \"stderr\": \"\"\n  },\n  \"status\": {\n    \"args\": [\n      \"git\",\n      \"status\",\n      \"--short\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"?? adversarial-review/\\n?? setup.mjs\\n\",\n    \"stderr\": \"\"\n  },\n  \"note\": \"Package commit is user-supplied freeze identifier; source bytes captured, no package Git identity inferred.\"\n}"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/adversarial-review/before",
      "owner": "grades-native-06.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/input",
      "owner": "grades-native-06.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/input.json",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/source-manifest.json",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/source-reads.txt",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/before",
      "owner": "grades-native-06.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/input",
      "owner": "grades-native-06.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/input.json",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/source-manifest.json",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/adversarial-review/source-reads.txt",
      "owner": "grades-native-06.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/events.jsonl",
      "owner": "grades-native-durable-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/README.md",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/cache.mjs",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/caller.mjs",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/invalidation.diff",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/manifest.json",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/probe.mjs",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/after/vendor/disposer-v1.mjs",
      "owner": "grades-native-durable-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/durable-01/adversarial-review/execution/before",
      "owner": "grades-native-durable-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/inputs",
      "owner": "grades-native-durable-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/durable-01/adversarial-review/sources",
      "owner": "grades-native-durable-01.json#0",
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
