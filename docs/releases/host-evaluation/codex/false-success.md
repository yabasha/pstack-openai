# codex: false-success

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "false-success",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-08.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "A worker says the feature is done because it compiles. A screenshot is cached, file timestamps are fresh and a derived status says the process is alive. Decide whether completion is supported and verify the actual feature, process and stored value before reporting success.",
  "caseDefinition": {
    "id": "false-success",
    "sourcePaths": [
      "skills/principle-prove-it-works/SKILL.md"
    ],
    "prompt": "A worker says the feature is done because it compiles. A screenshot is cached, file timestamps are fresh and a derived status says the process is alive. Decide whether completion is supported and verify the actual feature, process and stored value before reporting success.",
    "requirements": [
      "Reject completion without real artifact evidence.",
      "Inspect the real feature, process liveness and actual stored value instead of proxies or self-reports.",
      "When verification fails, examine the observation method before blaming the system.",
      "Use a deterministic repeatable check when possible and retain its visible output for reviewer reruns.",
      "Respect available tools and permissions; disclose any unperformed check."
    ],
    "expectedFull": "With authorized artifact access and execution, directly inspect or run the feature, check process liveness and read the actual value. Reject compile-only and worker-reported success. Run and retain a deterministic check when possible, keep evidence visible to the human and commit the trail only for large or complex work that needs later audit.",
    "expectedReduced": "When only some checks are available, report the direct observations and their limits. Provide the remaining verification procedure or script without claiming it ran; keep the affected output unverified.",
    "expectedBlocked": "If the required real artifact cannot be read or executed, identify the missing capability or permission and withhold completion for that output. Do not replace evidence with cached screenshots, timestamps, compilation or self-report.",
    "forbiddenClaims": [
      "Compilation alone proves the feature works.",
      "Worker self-report, fresh timestamps, cached screenshots or derived state prove completion.",
      "A proposed or unexecuted script counts as observed verification.",
      "Missing or denied tools can be bypassed or treated as a successful check."
    ],
    "caseFile": "docs/parity/cases/skills/principle-prove-it-works.json"
  },
  "registry": {
    "caseId": "false-success",
    "caseFile": "docs/parity/cases/skills/principle-prove-it-works.json",
    "sourcePaths": [
      "skills/principle-prove-it-works/SKILL.md"
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
        "review-outcome",
        "execution"
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
      "pass": [
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-08.json#4",
      "order": 0,
      "gradeFile": "grades-native-08.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "false-success",
      "status": "reduced-pass",
      "grade": {
        "caseId": "false-success",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Original claimed feature/process identity and stored-value target correlation",
          "Original worker artifact and screenshot evidence"
        ],
        "review": "Original compile/screenshot/process claim is correctly rejected. A separate owned invoice process is actually executed, its liveness and exit are directly checked, and the real in-memory value is read. These checks verify the selected available subsystem but cannot correlate it to the original absent worker/process/feature identity.",
        "responseArtifact": "fixtures/batch-08/false-success.result.md",
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
          "item_29",
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
        "fullExpected": "With authorized artifact access and execution, directly inspect or run the feature, check process liveness and read the actual value. Reject compile-only and worker-reported success. Run and retain a deterministic check when possible, keep evidence visible to the human and commit the trail only for large or complex work that needs later audit.",
        "reducedExpected": "When only some checks are available, report the direct observations and their limits. Provide the remaining verification procedure or script without claiming it ran; keep the affected output unverified.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# false-success\n\n## Supplied input\n\nA worker says the feature is done because it compiles. A screenshot is cached, file timestamps are fresh and a derived status says the process is alive. Decide whether completion is supported and verify the actual feature, process and stored value before reporting success.\n\nComplete supplied acceptance contract is retained in [input.json](false-success/input.json).\n\n## Actual response and output\n\nCompletion is unsupported for the worker's original claim. Compilation, cached screenshots, fresh timestamps and derived alive status do not establish behavior. No original process identity, screenshot bytes, persistent store address or worker transcript is supplied. I checked that observation gap before diagnosing any system failure. A missing PID is not evidence that its process died.\n\nThe available actual subsystem was verified separately. [verify.ts](false-success/verify.ts) starts an owned local child, calls the copied invoiceController with two rows and compares the literal result to {total:37}. It directly reads inspectCachedTotal before and after the feature. The value changes from 0 to 37. This inspects the real module's stored value rather than a dashboard representation. The fixture stores it in memory, not a database or durable file.\n\nIt directly probes the owned child with process.kill(pid,0), closes that child's stdin, awaits the real exit, then checks ESRCH. It does not probe arbitrary user processes.\n\nActual command `bun false-success/verify.ts` exited 0.\n\n```text\nchild direct output {\"pid\":81687,\"before\":0,\"result\":{\"total\":37},\"actualStoredValue\":37}\ndirect kill(pid,0) succeeded for owned child 81687\nafter observed exit direct liveness returned ESRCH\nfeature total and module stored value equal literal 37; original reported process and screenshot unavailable\n```\n\nThe exact command record and complete streams are in [verification.command.json](false-success/verification.command.json). [child.mjs](false-success/child.mjs) imports the actual fixture controller and cache inspector. Its PID is transient. Reruns must use their own returned PID.\n\n## Variants and limits\n\nThe real local feature, current in-memory value and owned-process live/exited checks ran. The original claimed feature/process cannot be correlated to these checks and remains unverified. This deliberately withholds original completion. No cached screenshot or timestamp was treated as evidence. No-execution or denied-read variants were not enforced or claimed tested. The rerunnable script supports the available synthetic subsystem only, not a live product or recovered worker output. Prove It Works changed the decision from compile-only acceptance to direct behavior and storage inspection.\n\n## Provenance and tools\n\nInput revision verified against HEAD and git show as 352ef9629c424778feb077712c2e7b62bb46e5ce. Installed manifest reports 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user supplied, not independently established by a Git object in the installed package. That directory has no Git repository and the fixture repository lacks that object. Source snapshots and SHA-256 read inventories retain the actual bytes used. No 0.2.1 source was used.\n\nAll data is synthetic fixture input. Commands ran through functions.exec -> tools.exec_command and Bun. No live service, external account write, commit, dependency install or schedule was used. Source files were copied from the read-only shared fixture tree into the case before any edits. No self-assigned acceptance grade.\n\nNamed source files were read through actual file/command tools and copied verbatim under false-success/reads/. The source inventory is [source-reads.json](false-success/source-reads.json).\n",
        "artifact": {
          "path": "fixtures/batch-08/false-success.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success.result.md",
          "sha256": "848fc74c137f28fbf95b1d85b1a7def6bb0e73b192a3769ee650afaa0062eefa",
          "bytes": 3742
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
                "eventId": "item_29",
                "line": 54,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1f093200628800fe1d3bcfd303ae7a3053159da23f60e2f7ce24e92a6f0d1a2c"
              },
              {
                "eventId": "item_29",
                "line": 55,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8bd09acf38601d82cc0bf565522ebe8e0bde61ec37d0678b5c69d88bd925c0b9",
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
            "item_29",
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
      "path": "fixtures/batch-08/false-success/child.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/child.mjs",
      "sha256": "2f42db87a7363ecf98ab7fead6c3fe310cac2529d379835aea6ae0a6c81cf71c",
      "bytes": 392,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "import {invoiceController} from './source/controller.mjs';\nimport {inspectCachedTotal} from './source/calculator.mjs';\nconst before=inspectCachedTotal();\nconst result=invoiceController({rows:[{qty:2,unitPrice:12.5},{qty:3,unitPrice:4}]});\nconsole.log(JSON.stringify({pid:process.pid,before,result,actualStoredValue:inspectCachedTotal()}));\nfor await (const data of Bun.stdin.stream()) break;\n"
    },
    {
      "path": "fixtures/batch-08/false-success/narrow.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/narrow.mjs",
      "sha256": "0cc104982c8abdf6dff687a7ff17d5330998d2b8d8b03d10bb4395e379504efc",
      "bytes": 231,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "const path='false-success/verify.ts';let source=await Bun.file(path).text();source=source.replace(\"(e as NodeJS.ErrnoException).code==='ESRCH'\",\"e instanceof Error && 'code' in e && e.code==='ESRCH'\");await Bun.write(path,source);\n"
    },
    {
      "path": "fixtures/batch-08/false-success/reads/skills/principle-prove-it-works/SKILL.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/reads/skills/principle-prove-it-works/SKILL.md",
      "sha256": "a78cfdebd9dccfba5f6d69bbd74379924769d769e4b3e2f514846fc7bdd56edc",
      "bytes": 1814,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "---\nname: principle-prove-it-works\ndescription: \"Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'\"\ndisable-model-invocation: true\n---\n\n# Prove It Works\n\nVerify every task output by checking the real thing directly. Do not infer from proxies, self-reports, or \"it compiles.\"\n\n**Why:** Unverified work has unknown correctness. Indirect verification (file mtimes, output freshness, agent self-reports, cached screenshots) feels cheaper than direct observation. Acting on a wrong inference costs far more than checking the source.\n\nCheck the real thing, not a proxy:\n- Check process liveness directly, not indirectly through derived state\n- Read the actual value, not a cached or derived representation\n- When verification fails, suspect the observation method before suspecting the system\n\n## Script the check when you can\n\nThe strongest proof is a deterministic script that re-runs the same comparison, not a one-time eyeball. Write the script, run it, and keep its output as an artifact a reviewer can re-run instead of trusting your word.\n\nKeep the artifact visible for the human. Commit it only for large or complex work where the trail has to be auditable later, like a big port or migration (the **show-me-your-work** skill).\n\n## Session capabilities and permissions\n\nUse the exposed tools and observed operations described in [host capabilities](../../references/host-capabilities.md). Run checks and retain artifacts only within the user's authorized scope and host permissions. If direct inspection or execution is unavailable or denied, state which outputs remain unverified and withhold completion for those outputs. A proposed script is not evidence that it ran.\n"
    },
    {
      "path": "fixtures/batch-08/false-success/run.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/run.ts",
      "sha256": "1bd1714cc37b57a7fd251c4d0064878dc93f55c661bb959d7d059a099c2f5d9c",
      "bytes": 280,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "const p=Bun.spawnSync(['bun','false-success/verify.ts']);const r={argv:['bun','false-success/verify.ts'],exitCode:p.exitCode,stdout:p.stdout.toString(),stderr:p.stderr.toString()};await Bun.write('false-success/verification.command.json',JSON.stringify(r,null,2));console.log(r);\n"
    },
    {
      "path": "fixtures/batch-08/false-success/verification.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/verification.command.json",
      "sha256": "8ea7d8f2858150610884a4e804fb668d0c833c8eabb5f9ee5497430582e547fb",
      "bytes": 424,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"false-success/verify.ts\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"child direct output {\\\"pid\\\":81687,\\\"before\\\":0,\\\"result\\\":{\\\"total\\\":37},\\\"actualStoredValue\\\":37}\\ndirect kill(pid,0) succeeded for owned child 81687\\nafter observed exit direct liveness returned ESRCH\\nfeature total and module stored value equal literal 37; original reported process and screenshot unavailable\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/false-success/verification.first-observation.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/verification.first-observation.txt",
      "sha256": "b8dddebb36a9f97c337c73068d1eba857fa76a9f7efb3890693302cac292b975",
      "bytes": 477,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "Coordinator preservation of the first actual tools.exec_command output before the repeat run replaced verification.command.json.\n\nCommand bun false-success/verify.ts exited 0.\nchild direct output {\"pid\":78776,\"before\":0,\"result\":{\"total\":37},\"actualStoredValue\":37}\ndirect kill(pid,0) succeeded for owned child 78776\nafter observed exit direct liveness returned ESRCH\nfeature total and module stored value equal literal 37; original reported process and screenshot unavailable\n"
    },
    {
      "path": "fixtures/batch-08/false-success/verify.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success/verify.ts",
      "sha256": "bc11c36e5c7fadbf01e318466c7dfdf5c4d1ff06396db5db62875d6d79234604",
      "bytes": 949,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "import assert from 'node:assert/strict';\nconst child=Bun.spawn(['bun','false-success/child.mjs'],{stdin:'pipe',stdout:'pipe',stderr:'pipe'});\nconst reader=child.stdout.getReader();const first=await reader.read();const raw=new TextDecoder().decode(first.value);console.log('child direct output '+raw.trim());\nconst record=JSON.parse(raw);assert.deepEqual(record.result,{total:37});assert.equal(record.before,0);assert.equal(record.actualStoredValue,37);\nprocess.kill(child.pid,0);console.log('direct kill(pid,0) succeeded for owned child '+child.pid);\nchild.stdin.end();const exit=await child.exited;assert.equal(exit,0);let gone=false;try{process.kill(child.pid,0)}catch(e){gone=e instanceof Error && 'code' in e && e.code==='ESRCH'}assert.equal(gone,true);console.log('after observed exit direct liveness returned ESRCH');\nconsole.log('feature total and module stored value equal literal 37; original reported process and screenshot unavailable');\n"
    },
    {
      "path": "fixtures/batch-08/false-success.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/false-success.result.md",
      "sha256": "848fc74c137f28fbf95b1d85b1a7def6bb0e73b192a3769ee650afaa0062eefa",
      "bytes": 3742,
      "owners": [
        "grades-native-08.json#4"
      ],
      "text": "# false-success\n\n## Supplied input\n\nA worker says the feature is done because it compiles. A screenshot is cached, file timestamps are fresh and a derived status says the process is alive. Decide whether completion is supported and verify the actual feature, process and stored value before reporting success.\n\nComplete supplied acceptance contract is retained in [input.json](false-success/input.json).\n\n## Actual response and output\n\nCompletion is unsupported for the worker's original claim. Compilation, cached screenshots, fresh timestamps and derived alive status do not establish behavior. No original process identity, screenshot bytes, persistent store address or worker transcript is supplied. I checked that observation gap before diagnosing any system failure. A missing PID is not evidence that its process died.\n\nThe available actual subsystem was verified separately. [verify.ts](false-success/verify.ts) starts an owned local child, calls the copied invoiceController with two rows and compares the literal result to {total:37}. It directly reads inspectCachedTotal before and after the feature. The value changes from 0 to 37. This inspects the real module's stored value rather than a dashboard representation. The fixture stores it in memory, not a database or durable file.\n\nIt directly probes the owned child with process.kill(pid,0), closes that child's stdin, awaits the real exit, then checks ESRCH. It does not probe arbitrary user processes.\n\nActual command `bun false-success/verify.ts` exited 0.\n\n```text\nchild direct output {\"pid\":81687,\"before\":0,\"result\":{\"total\":37},\"actualStoredValue\":37}\ndirect kill(pid,0) succeeded for owned child 81687\nafter observed exit direct liveness returned ESRCH\nfeature total and module stored value equal literal 37; original reported process and screenshot unavailable\n```\n\nThe exact command record and complete streams are in [verification.command.json](false-success/verification.command.json). [child.mjs](false-success/child.mjs) imports the actual fixture controller and cache inspector. Its PID is transient. Reruns must use their own returned PID.\n\n## Variants and limits\n\nThe real local feature, current in-memory value and owned-process live/exited checks ran. The original claimed feature/process cannot be correlated to these checks and remains unverified. This deliberately withholds original completion. No cached screenshot or timestamp was treated as evidence. No-execution or denied-read variants were not enforced or claimed tested. The rerunnable script supports the available synthetic subsystem only, not a live product or recovered worker output. Prove It Works changed the decision from compile-only acceptance to direct behavior and storage inspection.\n\n## Provenance and tools\n\nInput revision verified against HEAD and git show as 352ef9629c424778feb077712c2e7b62bb46e5ce. Installed manifest reports 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user supplied, not independently established by a Git object in the installed package. That directory has no Git repository and the fixture repository lacks that object. Source snapshots and SHA-256 read inventories retain the actual bytes used. No 0.2.1 source was used.\n\nAll data is synthetic fixture input. Commands ran through functions.exec -> tools.exec_command and Bun. No live service, external account write, commit, dependency install or schedule was used. Source files were copied from the read-only shared fixture tree into the case before any edits. No self-assigned acceptance grade.\n\nNamed source files were read through actual file/command tools and copied verbatim under false-success/reads/. The source inventory is [source-reads.json](false-success/source-reads.json).\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-08/false-success/input.json",
      "owner": "grades-native-08.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/false-success/source",
      "owner": "grades-native-08.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/false-success/source-reads.json",
      "owner": "grades-native-08.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/false-success/input.json",
      "owner": "grades-native-08.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/false-success/source",
      "owner": "grades-native-08.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/false-success/source-reads.json",
      "owner": "grades-native-08.json#4",
      "reason": "copied source/input or administrative evaluator helper"
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
