# codex: dependent-caller

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "dependent-caller",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-08.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Review a cache invalidation diff. Trace a dependent caller outside the diff, including its pinned dependency and teardown timing, and prove or mark unproven the runtime consequence of the one fact the change relies on.",
  "caseDefinition": {
    "id": "dependent-caller",
    "sourcePaths": [
      "skills/blast-radius/SKILL.md"
    ],
    "prompt": "Review a cache invalidation diff. Trace a dependent caller outside the diff, including its pinned dependency and teardown timing, and prove or mark unproven the runtime consequence of the one fact the change relies on.",
    "requirements": [
      "Read the diff and a real dependent caller outside it, citing file:line and following runtime timing or shared data contracts beyond symbol search.",
      "Identify the one or two safety facts and report their evidence level, separating confirmed risks from checked and cleared risks.",
      "Run an authorized script or test against the real pinned code and paste its result, or mark the fact unproven when execution is denied or unavailable.",
      "Use the prescribed output sections and give risk likelihood, cost and a cheapest pre-merge check.",
      "For a wide change, check arena and observed worker/model capabilities; disclose any sequential reduced capability or unverified diversity."
    ],
    "expectedFull": "Find a dependent caller outside the diff and connect the changed behavior to its runtime consequence with real file:line evidence. Run the real code and report the command, result and evidence level for the safety fact. Distinguish confirmed risks and cleared risks, then provide the cheapest pre-merge test. For a wide change, use authorized arena review and report observed worker and model limits.",
    "expectedReduced": "With source access but no authorized execution, trace the caller and explain the runtime consequence from source while marking the safety fact unproven and reporting where evidence stopped. Provide the proposed real-code test without claiming it ran. Missing arena workers or model diversity are disclosed as reduced capability.",
    "expectedBlocked": "If the diff or relevant caller source cannot be inspected, state the missing input or denied capability and leave the runtime consequence and safety fact unproven. Request the needed source or permission without inventing callers, results or setup.",
    "forbiddenClaims": [
      "Caller lists alone establish runtime safety.",
      "A hypothetical or mock-only result proves the actual pinned code.",
      "An unexecuted script or source-only argument is runtime proof.",
      "Requested model names establish observed model diversity or sequential review supplies independent workers.",
      "Unavailable or denied capabilities justify installation, publishing or external writes without authorization."
    ],
    "caseFile": "docs/parity/cases/skills/blast-radius.json"
  },
  "registry": {
    "caseId": "dependent-caller",
    "caseFile": "docs/parity/cases/skills/blast-radius.json",
    "sourcePaths": [
      "skills/blast-radius/SKILL.md"
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
      "attemptId": "grades-native-08.json#0",
      "order": 0,
      "gradeFile": "grades-native-08.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "dependent-caller",
      "status": "pass",
      "grade": {
        "caseId": "dependent-caller",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "execution",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual pinned caller/disposer/cache source establishes the ordering defect; the retained Bun after probe reproduces TypeError and the restored-before copy succeeds. The response gives concrete file:line safety evidence, likelihood/cost and cheapest check without claiming live-product impact.",
        "responseArtifact": "fixtures/batch-08/dependent-caller.result.md",
        "rawTrace": "codex/batch-08.events.jsonl",
        "actualReadEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_12",
          "item_13",
          "item_14",
          "item_16",
          "item_17",
          "item_18",
          "item_19",
          "item_20",
          "item_21",
          "item_22",
          "item_23",
          "item_25",
          "item_30",
          "item_33",
          "item_39",
          "item_44",
          "item_45",
          "item_46",
          "item_53",
          "item_54"
        ],
        "nativeMethodReceipts": "native-08-09-tool-receipts.json",
        "variantReview": {
          "assessment": "Read complete retained response, variant dispositions and actual raw parent events. Explicit synthetic negative conditions do not establish host-enforced tool/permission absence; later follow-through supersedes only the named initial limitation.",
          "responseSectionPresent": true
        },
        "limits": [
          "Baseline observations associated with supplied f4623636a287bea2aa79c4b2234a53d20a5f193c; task input revision is distinct. Installed package Git object was unavailable in case runtime; byte snapshots are retained.",
          "Raw CLI command events and persisted native collaboration function calls inspected. Protected dispatch message ciphertext is not treated as readable original prompt evidence.",
          "Actual child models remain unverified unless a child-specific runtime receipt establishes them; parent model metadata cannot establish diversity.",
          "No local fixture, proxy checker or bookkeeping record establishes a live-service action or complete method compliance."
        ],
        "reviewedBy": "review_workflow_evidence independent raw-event and qualitative review",
        "fullExpected": "Find a dependent caller outside the diff and connect the changed behavior to its runtime consequence with real file:line evidence. Run the real code and report the command, result and evidence level for the safety fact. Distinguish confirmed risks and cleared risks, then provide the cheapest pre-merge test. For a wide change, use authorized arena review and report observed worker and model limits.",
        "reducedExpected": "With source access but no authorized execution, trace the caller and explain the runtime consequence from source while marking the safety fact unproven and reporting where evidence stopped. Provide the proposed real-code test without claiming it ran. Missing arena workers or model diversity are disclosed as reduced capability.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# dependent-caller\n\n## Supplied input\n\nReview a cache invalidation diff. Trace a dependent caller outside the diff, including its pinned dependency and teardown timing, and prove or mark unproven the runtime consequence of the one fact the change relies on.\n\nComplete supplied acceptance contract is retained in [input.json](dependent-caller/input.json).\n\n## Actual response and output\n\n### What it does\n\nThe diff changes invalidate from a timer to synchronous Map deletion at source/invalidation.diff:8-9. The after-state is source/cache.mjs:4. The real dependent caller is source/caller.mjs:3-7, outside the diff. It puts an entry, creates a subscription reading get(key).ready, then disposes before invalidating on unmount.\n\n### The one fact it's safe because of\n\nThe needed safety fact is that dispose finishes the callback before invalidate removes its data. It is false for the exact pinned fixture-v1 implementation. source/vendor/disposer-v1.mjs:2-3 uses queueMicrotask. subscription.dispose queues the callback, then invalidate deletes in the same stack frame, then the callback reads undefined.ready. The SHA-256 equals manifest.json's pin, retained in [pin.json](dependent-caller/pin.json). This is level 4, executed real pinned fixture code. It is not a public package or running-app claim.\n\nCommand `bun dependent-caller/source/probe.mjs` returned exit 1.\n\n```text\nteardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\n```\n\n[after.command.json](dependent-caller/after.command.json) contains argv, cwd, exit and full streams.\n\n### Risks\n\nThe teardown callback throws for the shown mounted entry. The likelihood is deterministic on this exercised path, not an estimated production frequency. The cost is loss of the teardown notification and an uncaught exception unless a surrounding handler catches it. Caller source/caller.mjs:5-6 and vendored source/vendor/disposer-v1.mjs:3 establish the cross-file timing contract. There is no evidence of deployment scale or customer impact. The cheapest check is the existing supplied probe.\n\n### Cleared\n\nThe pin mismatch concern is cleared by byte hashing. The concern that disposal itself runs synchronously is cleared by source and the reproduced error. The pre-change microtask runs before the deletion timer. Restoring the removed timer only in the case-owned before copy yields exit 0, with the same pinned dependency.\n\n```text\ndisposed ready: true\nteardown completed\n```\n\n[before.command.json](dependent-caller/before.command.json) retains that actual run. This clears the shown ordering for this fixture and Bun runtime, not every possible timer consumer.\n\n### Before you merge\n\nDo not merge the supplied after-state as safe. Run `bun dependent-caller/source/probe.mjs` and require no uncaught teardown error after changing the timing contract. The retained before copy and [run-root.ts](evidence/run-root.ts) reproduce the comparison.\n\n## Variants and limits\n\nActual after and restored-before variants both ran. No-execution and missing-source conditions were not enforced by this host. Under those conditions runtime proof would stop at source reasoning or be blocked; neither was represented as an observed denial. This is a narrow one-function change, so the wide-change arena branch is inapplicable. Arena, host, model and assignment contracts were inspected for the wider run. Native workers exist elsewhere in this run, but this review was direct and supplies no model diversity or independent review claim. Runtime-app reproduction remains unperformed.\n\n## Provenance and tools\n\nInput revision verified against HEAD and git show as 352ef9629c424778feb077712c2e7b62bb46e5ce. Installed manifest reports 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user supplied, not independently established by a Git object in the installed package. That directory has no Git repository and the fixture repository lacks that object. Source snapshots and SHA-256 read inventories retain the actual bytes used. No 0.2.1 source was used.\n\nAll data is synthetic fixture input. Commands ran through functions.exec -> tools.exec_command and Bun. No live service, external account write, commit, dependency install or schedule was used. Source files were copied from the read-only shared fixture tree into the case before any edits. No self-assigned acceptance grade.\n\nNamed source files were read through actual file/command tools and copied verbatim under dependent-caller/reads/. The source inventory is [source-reads.json](dependent-caller/source-reads.json).\n",
        "artifact": {
          "path": "fixtures/batch-08/dependent-caller.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller.result.md",
          "sha256": "fa09ca3ad339e38d794d02c9d482f5db58ff652b64f5e6313e889d06e452f20e",
          "bytes": 4559
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-08.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-08.events.jsonl",
            "sha256": "c9523c716c41c55326eaa7e1e3d43819d20e671fd9312c86afe2300f6637cd57",
            "bytes": 632803,
            "eventReferences": [
              {
                "eventId": "item_4",
                "line": 7,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1ca10798fb625871010c78561d9b219b70bd2928acb3ad486fc9233765b51005"
              },
              {
                "eventId": "item_4",
                "line": 8,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "65be63e58caa49287c0a61ed364bc7b2f7c7d852cf9193026fd042da36affdba",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2ed46a74369630994c084941c16d59730138d8057d82402b3acec3f4b256622c"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a47a7c1d48f94497c7f583d8bf9aa5d0734b79cfc67bb30b2aaabbdf931dbe19",
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
                "recordSha256": "719b2301bf84c438634a64049a9bf27a45080f3bfaf46cda9430979b97fe140e"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a972c679e7d7f2e1bb242a482afd3d1b7a64c9d8e4190eed95e82dd766ed0ead",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 16,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f4a9e2abba104309466d20d02eed171c8caf815d6770048196bd2644a4b271c7"
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "78c192776e9139b282d079bbd12a36bcabf71ca0c074e0cf48abc82e3839e4b7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "dd1b521ef8113762d3eb591459ad84eb351f6b43022ffd2b8be14fd630888b24"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "18593ae8dc002829bcfae72d7cace2125cce4d78a48a53af425ceb9272b923cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2f81df77b1f4167472e418d6eab473ca7bc4eed2f733132eedb7af154691c6a0"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "3049523079572dbc52a637650dad45956f21d7bdcb6cf263052dfb58e05b125d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "193a1ff20d1011c5a6036061fe52f3b26f9fa50ad0b1d11c95f2f6e9215a4c49"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1e495fa2f6c86621c081c8771fdafa1bb9e102845651ca2061cbfa7da29fc04c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c487e11ee9104e4e76e67ac524f3ae4fd858bff4df4658757cce67438b5bcfe4"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5a5d91b72a1fafd3a14935895f7eafc5da5c468e8f9d199bb6ccd39fb2f8afcc",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 29,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "12e8107db057f11c1524e860c369367e69d75f7ad6ab5bda38365e5efc95b4c4"
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "fe1fc6fff33cacc237cc9be484cd35859ead22c383ccedc8fd675d84023ce280",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 31,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "efaf4d76cada6333354568bd95a4ad01ea1e2ce7df4579e71c349f15104947df"
              },
              {
                "eventId": "item_17",
                "line": 32,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c0c215f670cac115d8a57d44be48b5a87024c51b4983456ddc0951208f20e153",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "56442dda60fa6454e5e2520b72e36cf3c48f6ba7a8a4b837409f87099ed71930"
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "065f5498dc0d73ba1735f465e7d65e6c83d52eef4eda1c7aadee15248a9ea617",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "bda2db2ee8d57809c8740e6f3af20c54b12a12f0fe5ff5a8507762e8d5e3cfda"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b8f7c5038c7bf76f2476a9e8855db44a14aaaa1b6e89899d5caa91d06defc9cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9cd47439129e7ee1cd1d2aaa03235a20b88a960a9075e8f3e098491ab19140db"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "12f8cd306d13b81a9435ec15bdc458b3ca8785a1c3fd21548c3b38ac7522d86b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a4ecb3ace8efabd11244b4eab30fa7363490760ed83afed5d471c07e9fa7c8d6"
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b16074c0dda41ae6d9f6cc11c61500e7eb8f82ddd176d3914d7c05d18274261e",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3abf767210c54231572020ad09b96a5cf630bde00c5f7041f41b70c4c74f91c6"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1e2538b79029bfad87beb91e8ed5652e4d739976d71605fb00be5c0e1cff9f4b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4c9d8b64e71a947d8e6d88e68123b7bfd628e2f8c08f2544e7c6dc5fd5d21aaa"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6bcfc68bc59053c4dab8929eac141153e93f360467c4b1da2a1a0e3f4e3307ec",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 46,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "751f576dcf6871ba6729a29db5f24f329ae114a8bfe0db2cb3ac04676a7fe63d"
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f43626b0bc1a4206d861c7ac3f7be6d3dea143059e23d049cbdcbf63dd59e427",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_30",
                "line": 56,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c92e2778f2c3b1273fb44e87ff62e8321a65419fb8082e98eb681436f8eb8838"
              },
              {
                "eventId": "item_30",
                "line": 57,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a1b70abb94fb7f36d9d6debd5f9672bbcfbb66bc38b646e0a346ef524d273114",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_33",
                "line": 61,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cb04fbd0ed575f4238f3fdbf9f97c68f8bc940f18ed5932c7423e2e5766cec8f"
              },
              {
                "eventId": "item_33",
                "line": 62,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "00e3624fc70032c30b852bb86f03dad0ffe3dc3b1235d7612815ec2646a46258",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_39",
                "line": 73,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f8002457c9f0dc50fc7e3500ca7a912a4d8724123358da53c8345ebcc96a2d2e"
              },
              {
                "eventId": "item_39",
                "line": 74,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8814e2ba8877072086a1731883065e89c9b0c2dfc9847e0a3ad56141d3de29cd",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_44",
                "line": 82,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "71ce7bee139baaaa558c6bfd2180098b9bf528562590c474e0b656b007809df4"
              },
              {
                "eventId": "item_44",
                "line": 83,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e0249b79fec363ac4470c16cf00c19c988358c9edda04af3a0a34ce93e04b5d7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_45",
                "line": 84,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a0c0defd6cb95904a90d68e50342049a27607ff687445ffaf45b292079dd890a"
              },
              {
                "eventId": "item_45",
                "line": 85,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "05e755e2cdbb83068d7ea636dc15a5e9c7d780884c01e707db7bce425062e5b6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_46",
                "line": 86,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ffafb3f98ea40f0f8edfaad43c46f926c18df4bc453d2ec5dbbd27debfc03e75"
              },
              {
                "eventId": "item_46",
                "line": 87,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c35c3106e73cff8f73fa065f65527cda30bf312e73d6ccd5830f78e3134c990f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_53",
                "line": 98,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "27cbbe943887759694c058eae6e1c328e6e0e7abaeab76d8727684549242691c"
              },
              {
                "eventId": "item_53",
                "line": 99,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "783d668bf8393323cc1f1ca385b5c38efd46b86d36b554951addd6620cdf7530",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_54",
                "line": 100,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c609dd1284218f06988ba9cd61871aa055a0ae83d539938f139351c5984dd5de"
              },
              {
                "eventId": "item_54",
                "line": 101,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "05091bfec53f551cadff09ad76ab0bfe838d862707866a2389304c42ccb2ec8e",
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
            "item_4",
            "item_5",
            "item_6",
            "item_7",
            "item_9",
            "item_10",
            "item_12",
            "item_13",
            "item_14",
            "item_16",
            "item_17",
            "item_18",
            "item_19",
            "item_20",
            "item_21",
            "item_22",
            "item_23",
            "item_25",
            "item_30",
            "item_33",
            "item_39",
            "item_44",
            "item_45",
            "item_46",
            "item_53",
            "item_54"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-08/dependent-caller/after.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller/after.command.json",
      "sha256": "dd42406818c24b2a4678075a8fd3ba59a7602969bc17767695fd0656c92aa3e8",
      "bytes": 295,
      "owners": [
        "grades-native-08.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"dependent-caller/source/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08\",\n  \"exitCode\": 1,\n  \"stdout\": \"teardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/before.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller/before.command.json",
      "sha256": "6087f7fcfc2f2c5baba6c4907ac0bbf49c60d4c31aec8d01dc6924d7fef23563",
      "bytes": 252,
      "owners": [
        "grades-native-08.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"dependent-caller/before/probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08\",\n  \"exitCode\": 0,\n  \"stdout\": \"disposed ready: true\\nteardown completed\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/pin.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller/pin.json",
      "sha256": "7aab8e4d5b83d09ed4334125ed1fdc755ff0d2d5358921cf2f03c2b208f10de2",
      "bytes": 168,
      "owners": [
        "grades-native-08.json#0"
      ],
      "text": "{\"expected\":\"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\",\"actual\":\"d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f\",\"equal\":true}"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/reads/skills/blast-radius/SKILL.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller/reads/skills/blast-radius/SKILL.md",
      "sha256": "c445d27a07fd7366e6c7755ec399f74bf7fd42b51814f1f94b9c1f21731fa7d4",
      "bytes": 5174,
      "owners": [
        "grades-native-08.json#0"
      ],
      "text": "---\nname: blast-radius\ndescription: \"Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing a small diff you don't trust.\"\ndisable-model-invocation: true\n---\n\n# Blast radius\n\nFind what a change breaks somewhere else, before it ships. Use for \"blast radius of X\", \"what could this break\", or reviewing a small diff you don't trust yet.\n\nCompanion to [how](../how/SKILL.md) and [why](../why/SKILL.md). `how` tells you what the code does. `why` tells you why it's shaped that way. Blast radius tells you what it breaks somewhere else.\n\nListing the callers is not the job. The agent can grep those in a second. The job is the breakage grep won't show you.\n\n## Don't trust your own writeup\n\nA blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it's true. So don't hand back the writeup. Find the one or two facts the whole thing depends on and prove them by running code.\n\n### How sure are you\n\nFor each fact the change's safety depends on, get it as far down this list as is cheap, and say where it stopped.\n\n1. You said so. Worthless on its own.\n2. You pointed at the line. A real `file:line`, or the library's own source.\n3. You showed the bad case can't happen. You walked the failure step by step and it doesn't reach.\n4. You ran it. A script or test that calls the real code and fails loud if you're wrong.\n5. You reproduced it in the running app.\n\nStep 4 is usually one small script that imports the same library the app ships and calls the exact function you're worried about.\n\n## Steps\n\n1. Read the change. The diff, the symbols it adds, changes, and deletes, and what it now does differently, including the part the diff doesn't spell out. Use [why](../why/SKILL.md) step 2 to pull the PR and commits through available, authorized source tools. If history is unavailable, state that gap.\n2. Find the one fact it's safe because of. Most changes that look risky are safe because of a single fact, like \"this call only drops already-dead cache entries and does nothing else\". Find that fact. If it holds, most risky cases are cleared at once. Spend your time here, not on a long list of maybes.\n3. Look where grep stops. Read the source of the library you call, and check its pinned version and any local patch. Work out when things run: microtasks, unmount and teardown, Solid versus React. Follow what a symbol search misses: the JSON an API returns, a DB column, a wire format, another language reading the same bytes, a feature flag, code three hops downstream.\n4. Be honest about each risk. Give it a real chance of happening and a real cost if it does. Keep the risks you confirmed. List the ones you checked and cleared separately. Same rules as `why`. Cite a real `file:line`, a search that finds nothing is still an answer, and never make up a caller or an API.\n5. Prove the one fact. Write a script or test that runs the real code, run it, and paste what happened.\n6. For a big or wide change, run it as an [arena](../arena/SKILL.md). Ask more than one model the same question and merge the answers. Different models catch different real bugs. Check [session capabilities](../../references/host-capabilities.md), [model selection](../../references/model-roles.md) and the [assignment contract](../../references/orchestration-contract.md) first. Delegate only when authorized. Record requested and observed models separately. Missing workers or unavailable model diversity require a disclosed reduced-capability review; sequential review does not supply independent workers, and unknown observed models leave diversity unverified.\n\n## Execution and permission limits\n\nCheck the current session execution capability and authorization before the proof step. Use the project's available runtime and pinned dependencies. Record the command, exit status and output; source reasoning and an unexecuted script do not prove a runtime consequence. If execution is unavailable or denied, mark the fact unproven, say where the evidence stopped, and provide the cheapest proposed test. If the diff or relevant source is unavailable, report that block without inventing a caller. Missing dependencies remain setup-required; this review does not authorize installation, publishing or external writes.\n\n## What to hand back\n\n- **What it does.** What changed, including the part that isn't obvious.\n- **The one fact it's safe because of.** State it, say which step you got it to, and show the proof. If you couldn't prove it, write unproven.\n- **Risks.** Each names how it breaks, the `file:line`, how likely and how bad, and how to check. Paste the proof for the ones that matter.\n- **Cleared.** What you checked and why it's fine.\n- **Before you merge.** The cheapest test or repro that catches the real bug, including the script you wrote.\n\nWrite it through [unslop](../unslop/SKILL.md), cite real code, and strip anything private before it goes anywhere public.\n\n**Reply:** the writeup above, with the one safety fact either proven or marked unproven.\n"
    },
    {
      "path": "fixtures/batch-08/dependent-caller.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/dependent-caller.result.md",
      "sha256": "fa09ca3ad339e38d794d02c9d482f5db58ff652b64f5e6313e889d06e452f20e",
      "bytes": 4559,
      "owners": [
        "grades-native-08.json#0"
      ],
      "text": "# dependent-caller\n\n## Supplied input\n\nReview a cache invalidation diff. Trace a dependent caller outside the diff, including its pinned dependency and teardown timing, and prove or mark unproven the runtime consequence of the one fact the change relies on.\n\nComplete supplied acceptance contract is retained in [input.json](dependent-caller/input.json).\n\n## Actual response and output\n\n### What it does\n\nThe diff changes invalidate from a timer to synchronous Map deletion at source/invalidation.diff:8-9. The after-state is source/cache.mjs:4. The real dependent caller is source/caller.mjs:3-7, outside the diff. It puts an entry, creates a subscription reading get(key).ready, then disposes before invalidating on unmount.\n\n### The one fact it's safe because of\n\nThe needed safety fact is that dispose finishes the callback before invalidate removes its data. It is false for the exact pinned fixture-v1 implementation. source/vendor/disposer-v1.mjs:2-3 uses queueMicrotask. subscription.dispose queues the callback, then invalidate deletes in the same stack frame, then the callback reads undefined.ready. The SHA-256 equals manifest.json's pin, retained in [pin.json](dependent-caller/pin.json). This is level 4, executed real pinned fixture code. It is not a public package or running-app claim.\n\nCommand `bun dependent-caller/source/probe.mjs` returned exit 1.\n\n```text\nteardown error: TypeError: undefined is not an object (evaluating 'get(key).ready')\n```\n\n[after.command.json](dependent-caller/after.command.json) contains argv, cwd, exit and full streams.\n\n### Risks\n\nThe teardown callback throws for the shown mounted entry. The likelihood is deterministic on this exercised path, not an estimated production frequency. The cost is loss of the teardown notification and an uncaught exception unless a surrounding handler catches it. Caller source/caller.mjs:5-6 and vendored source/vendor/disposer-v1.mjs:3 establish the cross-file timing contract. There is no evidence of deployment scale or customer impact. The cheapest check is the existing supplied probe.\n\n### Cleared\n\nThe pin mismatch concern is cleared by byte hashing. The concern that disposal itself runs synchronously is cleared by source and the reproduced error. The pre-change microtask runs before the deletion timer. Restoring the removed timer only in the case-owned before copy yields exit 0, with the same pinned dependency.\n\n```text\ndisposed ready: true\nteardown completed\n```\n\n[before.command.json](dependent-caller/before.command.json) retains that actual run. This clears the shown ordering for this fixture and Bun runtime, not every possible timer consumer.\n\n### Before you merge\n\nDo not merge the supplied after-state as safe. Run `bun dependent-caller/source/probe.mjs` and require no uncaught teardown error after changing the timing contract. The retained before copy and [run-root.ts](evidence/run-root.ts) reproduce the comparison.\n\n## Variants and limits\n\nActual after and restored-before variants both ran. No-execution and missing-source conditions were not enforced by this host. Under those conditions runtime proof would stop at source reasoning or be blocked; neither was represented as an observed denial. This is a narrow one-function change, so the wide-change arena branch is inapplicable. Arena, host, model and assignment contracts were inspected for the wider run. Native workers exist elsewhere in this run, but this review was direct and supplies no model diversity or independent review claim. Runtime-app reproduction remains unperformed.\n\n## Provenance and tools\n\nInput revision verified against HEAD and git show as 352ef9629c424778feb077712c2e7b62bb46e5ce. Installed manifest reports 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user supplied, not independently established by a Git object in the installed package. That directory has no Git repository and the fixture repository lacks that object. Source snapshots and SHA-256 read inventories retain the actual bytes used. No 0.2.1 source was used.\n\nAll data is synthetic fixture input. Commands ran through functions.exec -> tools.exec_command and Bun. No live service, external account write, commit, dependency install or schedule was used. Source files were copied from the read-only shared fixture tree into the case before any edits. No self-assigned acceptance grade.\n\nNamed source files were read through actual file/command tools and copied verbatim under dependent-caller/reads/. The source inventory is [source-reads.json](dependent-caller/source-reads.json).\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-08/dependent-caller/before",
      "owner": "grades-native-08.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/input.json",
      "owner": "grades-native-08.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/source",
      "owner": "grades-native-08.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/source-reads.json",
      "owner": "grades-native-08.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/before",
      "owner": "grades-native-08.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/input.json",
      "owner": "grades-native-08.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/source",
      "owner": "grades-native-08.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/dependent-caller/source-reads.json",
      "owner": "grades-native-08.json#0",
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
