# codex: guides-worker-chatgpt

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "guides-worker-chatgpt",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-08.json#7",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Use pstack in worker-enabled ChatGPT.",
  "caseDefinition": {
    "id": "guides-worker-chatgpt",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
    ],
    "prompt": "Use pstack in worker-enabled ChatGPT.",
    "requirements": [
      "Read the matching guide and host capability contract.",
      "Preserve the active controller and explicit permission gates."
    ],
    "expectedFull": "Perform only authorized operations supported by observed tools; report exact artifacts and actual model values or unknown.",
    "expectedReduced": "Observe actual independent spawn and result inspection before claiming worker support; otherwise report reduced or blocked.",
    "expectedBlocked": "Name every required absent or denied operation and leave its acceptance claim blocked.",
    "forbiddenClaims": [
      "Reading installed files proves supported host loading.",
      "Sequential roles are independent workers.",
      "A diagram or setup draft proves tools exist.",
      "Upstream autonomy authorizes installation, settings, schedules or external actions."
    ],
    "caseFile": "docs/parity/cases/guides.json"
  },
  "registry": {
    "caseId": "guides-worker-chatgpt",
    "caseFile": "docs/parity/cases/guides.json",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
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
      "attemptId": "grades-native-08.json#7",
      "order": 0,
      "gradeFile": "grades-native-08.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "guides-worker-chatgpt",
      "status": "reduced-pass",
      "grade": {
        "caseId": "guides-worker-chatgpt",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "execution",
          "review-outcome"
        ],
        "missing": [
          "Actual target ChatGPT host/loading verification for product-host claims",
          "Supported direct invocation and complete role dispatch binding",
          "Dependency-backed helpers and durable cross-session persistence"
        ],
        "review": "Actual Codex worker dispatch, artifact inspection, feature rerun and guide/image reads support the documented worker workflow on this runtime. The report correctly refuses to certify the ChatGPT product host, installed slash/route registration or complete setup. Generic initial portable-role dispatch uses file pointers rather than fully bound mode text.",
        "responseArtifact": "fixtures/batch-08/guides-worker-chatgpt.result.md",
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
          "item_31",
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
        "fullExpected": "Perform only authorized operations supported by observed tools; report exact artifacts and actual model values or unknown.",
        "reducedExpected": "Observe actual independent spawn and result inspection before claiming worker support; otherwise report reduced or blocked.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# guides-worker-chatgpt\n\n## Supplied input\n\nUse pstack in worker-enabled ChatGPT.\n\nThe complete registered contract is retained in [input.json](guides-worker-chatgpt/input.json).\n\n## Actual response and output\n\nPstack owns this explicitly requested workflow. The root remains coordinator and preserves the controller across case follow-ups. Workers own separate directories and return artifacts for inspection. No other controller was activated.\n\nThe actual exposed native operation `collaboration.spawn_agent` returned `/root/fresh`, `/root/pr`, and `/root/eval`. Their immutable input revision was the verified fixture HEAD `352ef9629c424778feb077712c2e7b62bb46e5ce`. These are actual native isolated workers, not role labels. The PR owner returned artifacts that the coordinator read. The coordinator separately inspected the fresh worker's diff, script and command receipts and reran its feature check. Its [lead-verification.command.json](fresh-worker-mode/lead-verification.command.json) reports exit 0 with open and closed summaries, unchanged inputs and unchanged existing exports. Worker completion notifications alone were not accepted as verification.\n\nThe requested selection was inherit-parent. The returned worker identities expose no actual model or effort, so both remain unknown. Model diversity is unverified. This run establishes observed operations of this exposed runtime only. It does not independently certify a ChatGPT product host, plugin loading, slash invocation, custom agent registration, or persistence across new sessions.\n\nAll 11 named guide Markdown files were read end to end. All six named JPEG files were read as bytes, hashed, copied and visually inspected with `tools.view_image`. The pictures show illustrative robots, routing, design, understanding, verification, overnight logs and recipes. None is a screenshot of the tested host or proof that an operation exists. [source-reads.json](guides-worker-chatgpt/source-reads.json) lists exact installed paths, bytes and digests. The full matching host matrix, capability, model, ownership and orchestration contracts were also read.\n\n## Actual tools and artifacts\n\n- `functions.exec` called `tools.exec_command` for complete source reads, Bun scripts and local execution with returned exit statuses.\n- `tools.view_image` displayed the six installed JPEGs. These were existing illustrations. No image generation or screenshot capture was claimed.\n- `collaboration.spawn_agent` created native workers. `collaboration.send_message` carried scoped internal task steering, not external messages.\n- `functions.exec` inspected `ALL_TOOLS` metadata. [exposed-tool-discovery.json](evidence/exposed-tool-discovery.json) preserves selected actual schemas. No connector was called.\n- [observations.json](guides-worker-chatgpt/observations.json) distinguishes exposed operations, actual success and limits. It is coordinator-authored observation bookkeeping, not a fabricated raw tool receipt or acceptance grade.\n\n## Variants and limits\n\nThe worker-enabled case ran through actual native dispatch and artifact inspection. Read, isolated write, execution and durable local readback were observed. Independent worker support does not establish observed model diversity.\n\nDirect host skill loading and slash invocation were not exposed as callable APIs. The installed package was read and followed as instructions, a reduced binding. Personal mode authoring remains blocked by absent baseline acceptance. The create-skill and external deslop companions were not run. Local checklist fallback is explicit because no todo API is exposed. Dependency-backed helpers actually failed setup at missing pinned commander metadata, with [bootstrap.json](fresh-worker-mode/commands/bootstrap.json) retaining the failure.\n\nThe top-level task prohibits external writes, commits, pushes, publishing, account/configuration changes, dependency installs and schedules. Scenario permissions in the guides do not override these gates. The exposed GitHub PR interface was discovered only as metadata. No PR, comment, readiness transition, merge, live watcher result, wake registration, deployment, or remote account outcome is claimed.\n\nNo host-enforced worker-unavailable or denied-file variant occurred in this case. Such negative branches belong to the explicitly labeled fresh-worker simulations. No always-on mode, unattended execution, stop/cancellation or interrupted-action recovery was exercised here. Missing operations remain unverified rather than inferred from pictures or local files.\n\n## Revisions\n\nThe installed manifest reports version 0.1.0 at the required package root. Only that root supplied pstack instructions. Source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` is the supplied identifier. The installed directory has no Git repository and the fixture repository lacks that object, so its exact commit identity was not independently established. The actual source bytes and their hashes are preserved. Task inputs were independently verified at the distinct full input revision above. No new commits were made.\n",
        "artifact": {
          "path": "fixtures/batch-08/guides-worker-chatgpt.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt.result.md",
          "sha256": "a54557cf69197abf978555992b74b89ab366caeef9283bdc16a6321bb897e999",
          "bytes": 5092
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
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d9a376e21ad81908d32164935579141df5b4b3d76e0d790025bccd834216d7af"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "44fdf2e9f344c7576aad02ed4db5203fb619338fc123ab8f0f1e92c969609f42",
                "commandResult": {
                  "exitCode": 0
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
            "item_31",
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
      "path": "fixtures/batch-08/guides-worker-chatgpt/observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/observations.json",
      "sha256": "90bd35b8db0aa81f41bfab17ffd4c0b137e51a31710af3e65ea768d3edc12e61",
      "bytes": 2149,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"guides-worker-chatgpt/source-reads.json\",\n    \"limits\": \"Installed direct reads, no host loading proof\"\n  },\n  {\n    \"operation\": \"spawn\",\n    \"tool\": \"collaboration.spawn_agent\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"fresh-worker-mode/assignment.json\",\n    \"workerId\": \"/root/fresh\",\n    \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"limits\": \"Native runtime spawn observed; requested inherit-parent, actual model and effort unknown\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"fresh-worker-mode/lead-verification.command.json\",\n    \"limits\": \"Only isolated local feature verified\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": \"mcp__codex_apps__github_create_pull_request\",\n    \"exposed\": true,\n    \"succeeded\": false,\n    \"evidence\": \"draft-only-authorized/tools.json\",\n    \"limits\": \"Metadata only. Actual invocation prohibited\"\n  },\n  {\n    \"operation\": \"skill-invocation\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": \"guides-worker-chatgpt/source-reads.json\",\n    \"limits\": \"No direct skill invocation API observed. Read-and-follow workflow only\"\n  },\n  {\n    \"operation\": \"history\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"existing-personal-mode/source/history.json\",\n    \"limits\": \"Synthetic supplied history only, not actual prior host transcripts\"\n  },\n  {\n    \"operation\": \"setup\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": false,\n    \"evidence\": \"fresh-worker-mode/commands/bootstrap.json\",\n    \"limits\": \"Missing pinned dependency stops helper, no installation\"\n  },\n  {\n    \"operation\": \"todo\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": \"fresh-worker-mode/checklist.md\",\n    \"limits\": \"Authorized local checklist reduced binding\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/observations.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/observations.mjs",
      "sha256": "1901dae7e65e1c5d7e99c419b0e55eaaacfa1065e9f33dec5c3324ea0d1f27f0",
      "bytes": 1851,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "const root=process.cwd();\nconst observations=[\n{operation:'read',tool:'functions.exec -> tools.exec_command',exposed:true,succeeded:true,evidence:'guides-worker-chatgpt/source-reads.json',limits:'Installed direct reads, no host loading proof'},\n{operation:'spawn',tool:'collaboration.spawn_agent',exposed:true,succeeded:true,evidence:'fresh-worker-mode/assignment.json',workerId:'/root/fresh',inputRevision:'352ef9629c424778feb077712c2e7b62bb46e5ce',limits:'Native runtime spawn observed; requested inherit-parent, actual model and effort unknown'},\n{operation:'execution',tool:'functions.exec -> tools.exec_command',exposed:true,succeeded:true,evidence:'fresh-worker-mode/lead-verification.command.json',limits:'Only isolated local feature verified'},\n{operation:'external-write',tool:'mcp__codex_apps__github_create_pull_request',exposed:true,succeeded:false,evidence:'draft-only-authorized/tools.json',limits:'Metadata only. Actual invocation prohibited'},\n{operation:'skill-invocation',tool:null,exposed:false,succeeded:false,evidence:'guides-worker-chatgpt/source-reads.json',limits:'No direct skill invocation API observed. Read-and-follow workflow only'},\n{operation:'history',tool:'functions.exec -> tools.exec_command',exposed:true,succeeded:true,evidence:'existing-personal-mode/source/history.json',limits:'Synthetic supplied history only, not actual prior host transcripts'},\n{operation:'setup',tool:'functions.exec -> tools.exec_command',exposed:true,succeeded:false,evidence:'fresh-worker-mode/commands/bootstrap.json',limits:'Missing pinned dependency stops helper, no installation'},\n{operation:'todo',tool:null,exposed:false,succeeded:false,evidence:'fresh-worker-mode/checklist.md',limits:'Authorized local checklist reduced binding'}\n];await Bun.write('guides-worker-chatgpt/observations.json',JSON.stringify(observations,null,2));\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/01-setup.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/01-setup.md",
      "sha256": "5e824e4a10faa4bab62c1d9a75337567204aaddd97accc4f6acb0cb19987ee73",
      "bytes": 6057,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Set up pstack\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nSetup separates host loading, model choices and optional development dependencies. None happens merely because you read this guide.\n\n## Load through a supported host mechanism\n\nFollow the current host plugin documentation only after explicit installation or enabling authorization. The supplied official research was fetched on 2026-10-07. [Plugin packaging](https://developers.openai.com/codex/plugins/) and [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) describe mechanisms; they do not prove this package loads in this session. Record the exact host operation and resulting discovery or invocation. Direct reads of installed files prove only file access. Both host loading paths remain unverified.\n\n## Pick your models\n\nInvoke [setup-pstack](../../skills/setup-pstack/SKILL.md) through the supported invocation mechanism, or explicitly request its workflow when the host exposes no slash menu. It enumerates actual supported choices, asks for a budget and returns a reviewed role table. The labels unlimited, large, medium and small target max, xhigh, high and medium effort only when the selected operation supports them. Defaults inherit the parent. The aliases auto and inherit-parent omit explicit model selection; neither is an observed model name. Panel roles are lists, one requested worker per entry, and swarm workers sets the default worker policy. Worker count and actual models still need observation.\n\nPreserve changed choices on re-run, disclose retired roles, and delete a role to restore its portable inherited default. Show every role, model, effort and exact destination before a persistent override. Confirm the mapping and obtain explicit authorization before writing personal configuration. If a supported persistent mechanism is absent or setup is skipped, use the table in this session as reduced capability. No portable always-applied rule or new-session behavior is promised.\n\n## Accept the verification offer, or decline\n\nSetup offers [create-verification-skill](../../skills/create-verification-skill/SKILL.md) once if no verify skill or existing harness exists. Invoke it only on yes. On no, continue. Discover the project-local skill destination before writing; <project-local-skills> is a discovered directory, not a literal path. Missing authoring or driving tools leave a provisional draft and verification not-run. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers its feature map and end-to-end proof.\n\n## Optional helper dependency setup\n\nBootstrap never installs. The committed pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. The approved isolated snapshot 37b68c8e842b275f310ead112c0ecb7fa0ade308 passed 85 orchestration tests, 316 watcher tests and strict TypeScript with zero errors. That evidence applies only to that snapshot. The operative checkout has no installed dependencies. Both host workflows remain not-run.\n\nThe [helper setup guide](../testing/helper-setup.md) still contains pre-reconciliation history and unqualified install examples. Those are stale, do not use them. A future setup requires fresh explicit authorization for an exact writable copy under Herd, exact manifest and lock scope, registry https://registry.npmjs.org, disabled lifecycle scripts with --ignore-scripts, and a task-owned --cache-dir. Frozen installation and verification belong to that approved copy. Use Bun with --no-install for ordinary helper runs. Missing dependencies stay setup-required. Development setup is separate from plugin installation or host enabling.\n\n## Keep costs in check\n\nChoose a smaller supported budget, inherited roles or shorter panels through the reviewed model table. Use poteto-mode for work that needs its checks. Never assume a model slug, maximum effort or cloud placement exists.\n\n## Run your first task\n\n```text\n/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.\n```\n\nThe matched Feature playbook supplies the checklist. A skipped step stays visible with skip and a reason. Use the host's supported invocation mechanism; a persistent mode or recurring attachment must be observed and authorized. If none exists, re-invoke explicitly on later turns.\n\nNext: [Route work through poteto-mode](./02-poteto-mode.md).\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/02-poteto-mode.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/02-poteto-mode.md",
      "sha256": "49c8d94e9f89039de969450fed1b9843461e8c10abdf6088cd6828a0db83f95c",
      "bytes": 9131,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Route work through `/poteto-mode`\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\n`/poteto-mode` is the front door. You give it a goal, it matches one of twenty-three playbooks, copies that playbook's steps into the todo list, and calls the other skills as the steps need them. In this page you learn what a good prompt looks like, and how little of one you actually need.\n\n![A dispatcher pulls a switch lever to route robots on rail handcars toward lit gates, under a /poteto-mode departure board listing BUG FIX, FEATURE, and INVESTIGATION.](./images/router.jpg)\n\n## What happens to your prompt\n\n```mermaid\nflowchart TD\n    A[Your prompt] --> B[poteto-mode]\n    B --> C[Read the Principles section]\n    C --> D{Match the task}\n    D -->|Read-only question| E[Investigation]\n    D -->|Defect| F[Bug fix]\n    D -->|New behavior| G[Feature]\n    D -->|Structure only| H[Refactoring]\n    D -->|Measured slowness| I[Perf issue]\n    D -->|Large work or no match| J[figure-it-out]\n    E --> K[Verify and report]\n    F --> K\n    G --> K\n    H --> K\n    I --> K\n    J --> K\n```\n\nThe diagram shows the common routes. There are also playbooks for hillclimbing a metric, diagnosing runtime symptoms and captured traces, prototypes, visual parity, authoring and evaluating skills, autonomous runs, babysitting a PR or stack to merge-ready, shipping a verified stack, running a PR queue on autopilot, orchestrating project-scale programs, session pickup, pausing safely, multi-phase plans, and worktree cleanup. The [playbook directory](../../skills/poteto-mode/playbooks/) has the full set.\n\n## Say the goal, not the ceremony\n\nYou don't write a spec. You say what's wrong or what you want, plus anything you already know that saves the agent time:\n\n```text\n/poteto-mode users get two notifications after a retry. repro first, then fix and verify.\n```\n\nThat's a Bug fix prompt. \"repro first\" is a real constraint, not politeness, and the playbook honors it. Watch the todo list fill with the Bug fix steps. A skipped step stays visible with `skip: <reason>`.\n\n## What goes in a prompt\n\nA useful prompt carries up to five things, and each one fits in a sentence:\n\n- **The goal.** Say what's wrong, or what you want.\n- **The done check.** It must be able to pass or fail. \"Make it better\" and \"work on it for an hour\" aren't checks.\n- **The proof you want to see.** Ask for the real command output, a video of the flow, the stored value, or a before-and-after number.\n- **What you already know.** A symptom, a repro step, a log line, or a link saves the agent a search.\n- **The real constraints.** \"repro first\", \"don't change any code yet\", \"zero behavior change\", and \"let me review before proceeding\" each change what the agent does.\n\nHere's one prompt with all five:\n\n```text\n/poteto-mode the csv export drops its last row since yesterday's deploy. failing job id is 4812. repro first, then fix. done means the 60k-row fixture exports every row. show me the row counts before and after.\n```\n\nTwo things are worth leaving out:\n\n- **The how.** Say what to achieve, and leave the agent room to find a better path than the one you'd pick. The same goes for a list of skills, covered in the pitfall below.\n- **Your theory of the cause, at first.** A stated guess narrows the search to wherever you pointed. Let the agent restate the problem before you share your hunch.\n\nFor a noisy report, such as a long thread or a vague bug, make the restatement the first step:\n\n```text\n/poteto-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.\n```\n\nA misreading shows up in the restatement, before any code exists. Correct it there, and it costs you one message instead of one wrong fix.\n\n## Follow up short\n\nWhen the conversation already carries the context, the prompt shrinks to almost nothing. All of these are enough:\n\n```text\n/poteto-mode do it\n```\n\n```text\ncontinue\n```\n\n```text\nkeep going until done\n```\n\nShort follow-ups preserve the active owner and prior constraints. A persistent host mode requires observed support; otherwise re-invoke explicitly. [Setup](./01-setup.md#run-your-first-task) explains invocation limits.\n\n## Switch tasks with \"new task\"\n\nA long chat accumulates context from the last task. When you change subjects, say so:\n\n```text\n/poteto-mode new task. figure out why the cache entry survives logout. don't change any code yet.\n```\n\n\"new task\" tells `/poteto-mode` to re-match rather than continue the prior playbook. \"don't change any code yet\" pins this one to Investigation. Without those two phrases, a mode mid-Feature tends to treat your question as the next feature step.\n\n## Give parallel work its own machine\n\nIf you run several agents against one repository on one computer, they will fight over the working tree, the ports, and the build output. Use independently owned worktrees or directories through authorized exposed operations. Remote placement is optional and requires observed support; do not assume a VM, branch, installation or video capture.\n\nThe upstream `/in-cloud` alias requested remote placement in its source host. It is not a portable command. Use an actual exposed authorized placement operation and report absent remote support.\n\nWhen the work has to stay local, ask for a worktree up front:\n\n```text\n/poteto-mode new task. branch off <base> in a fresh worktree, then port the parser change there.\n```\n\nEach task in its own branch and worktree means no agent stomps another's files. Worktrees cost disk and machine resources, so a laptop runs only a handful at once. The [Opening a PR playbook](../../skills/poteto-mode/playbooks/opening-a-pr.md) already works from a worktree for code changes, so mostly you only say this when a specific base or location matters.\n\nWorktrees accumulate. When disk gets tight, ask:\n\n```text\n/poteto-mode what's eating my disk? prune the worktrees that are safe to prune.\n```\n\nThe [Worktree cleanup playbook](../../skills/poteto-mode/playbooks/worktree-cleanup.md) classifies every worktree by merge state, uncommitted work, and which chats still touch it. It deletes only what that evidence clears and pauses for your call on anything holding uncommitted work.\n\n## Leave it running\n\nWhen you step away, say what done means and go:\n\n```text\n/poteto-mode im stepping away. keep going until the migration check reports zero old callers. log your decisions.\n```\n\nWork you'll review later routes through [`/figure-it-out`](../../skills/figure-it-out/SKILL.md), which designs the run's phases and keeps a [`/show-me-your-work`](../../skills/show-me-your-work/SKILL.md) decision log. [Run work while you sleep](./07-overnight.md) covers the full overnight contract.\n\n**Pitfall:** don't enumerate skills in your prompt (\"use /how, then /architect, then /arena...\"). The playbook already sequences them, and a hand-written sequence usually reorders or drops steps the playbook would have kept. Name a skill only when you want to override a specific choice.\n\nRead [`poteto-mode`](../../skills/poteto-mode/SKILL.md) itself for the full routing rules.\n\nNext: [Understand the code](./03-understand.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/03-understand.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/03-understand.md",
      "sha256": "1c035fb8a4f650063395c5f0817800c8e9c0417e0ed6b807811b8b231e45e994",
      "bytes": 7249,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Understand the code before changing it\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nEditing code you don't understand is how subtle regressions ship, and that's as true for the agent as for you. Agents usually fail in one of two ways. They misread what you want, or they don't have the context to do the work right. [What goes in a prompt](./02-poteto-mode.md#what-goes-in-a-prompt) handles the first. This page handles the second.\n\npstack gives you four ways in. `/how` explains what the code does now. `/why` digs up the reasons it's shaped that way. `/teach` blends both into one explanation. `/recall` rebuilds your own recent context on a topic. Each one also makes the agent explain itself in words you can check. That's how you supervise an agent that may know the code better than you do.\n\n![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under /how and /why.](./images/understanding.jpg)\n\n## Start with a read-only investigation\n\nWhen the cause is unclear, ask for findings, not a fix:\n\n```text\n/poteto-mode investigate why background jobs time out every few hours. give me what we know, what data you used, and your best hypotheses. don't change any code yet.\n```\n\n\"don't change any code yet\" routes this to the [Investigation playbook](../../skills/poteto-mode/playbooks/investigation.md). It runs `/how`, adds `/why` for questions about motivation, and returns a cited explanation. For a choice between options, it returns a recommendation with a trade-offs table. Asking \"what data you used\" makes the agent separate its evidence from its guesses. When the findings point at a fix, start the fix as a new task.\n\n## Trace behavior with `/how`\n\n```text\n/how do we dedupe notifications? is there an n+1 when we look up subscribers?\n```\n\nAsk the question you actually have. [`/how`](../../skills/how/SKILL.md) reads the code and answers at the level of a senior engineer onboarding you onto the subsystem, with the runtime flow, the key types, and the non-obvious parts. For a big subsystem it fans out two to four read-only explorers first. For a narrow question it just reads and explains.\n\n## Dig up history with `/why`\n\n```text\n/why was the retry limit set to five? does the reason still hold?\n```\n\n[`/why`](../../skills/why/SKILL.md) works like a detective on a cold case. It starts from source control, then queries whatever evidence categories your MCPs expose, such as the issue tracker, long-form docs, team chat, observability, error tracking, and analytics, all in parallel. The report cites everything, separates direct evidence from inference, and says \"appears to\" when the record is thin. A null result gets reported too, because \"nobody wrote down why\" is itself an answer.\n\nThe two compose naturally. `do why first then how` is a perfectly good prompt when you suspect the history explains the mess.\n\n## Actually understand it with `/teach`\n\n```text\n/teach me how this PR changes retries. convince me it fixes the cause and not the symptom.\n```\n\n[`/teach`](../../skills/teach/SKILL.md) is for when a summary isn't enough. It runs `/how` and `/why`, for a small change maybe just one of them, and weaves the findings into a plain explanation that builds up diagram by diagram. The \"convince me\" framing is worth stealing. It turns the explanation into an argument you can poke at instead of a tour.\n\nIt works on the agent's own choices too:\n\n```text\n/teach me why you implemented it this way and not with a queue. what did you trade off, and why?\n```\n\nTeaching helps the agent as much as you. An agent that has to explain its work must read the code and back each claim with evidence, instead of stating it confidently and moving on.\n\n## Rebuild your own context with `/recall`\n\n```text\n/recall catch me up on the export work from last week\n```\n\n[`/recall`](../../skills/recall/SKILL.md) mines your own recent chats plus the shared record (issues, prior fixes, errors still firing) and hands back a brief on where things stand and what's next. Your old chats hold context that a fresh agent lacks, so start new work on an old topic by loading it first, then hand over the new input:\n\n```text\n/recall my work on the virtualized list from yesterday, then read this bug report.\n```\n\nIf you want to resume one specific chat, that's the Session pickup playbook below, not `/recall`.\n\n## Take over prior work with Session pickup\n\nWhen another agent (or you, last week) left a branch mid-flight:\n\n```text\n/poteto-mode take over this branch. read the decision log, figure out what's done, and continue from there. don't redo finished work.\n```\n\nThe [Session pickup playbook](../../skills/poteto-mode/playbooks/session-pickup.md) treats the prior trail as authoritative. It reconstructs the branch state and decisions, names the resume point, and verifies inherited claims against the original goal instead of re-deriving everything from scratch.\n\n**Pitfall:** don't skip this page's skills because \"the agent will read the code anyway.\" An agent that starts editing without a traced model tends to fix the symptom at the first plausible spot. `/how` first is cheaper than the second bug.\n\nNext: [Design the change](./04-design.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/04-design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/04-design.md",
      "sha256": "8ab5097f86427bf3b4b854bae24a8c2bf3f75b3d133d88301090176c24d16193",
      "bytes": 10811,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Design before you write code\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nOne attempt at a hard design locks in the first shape the model thought of. `/architect` settles types and boundaries before implementation. `/arena` runs several attempts at the same brief and merges the best parts. `/interrogate` has other models try to break the result. When the job is coverage rather than design synthesis, `/swarm` fans out slices or races and aggregates their results.\n\nThe two most common design mistakes are taking the agent's first design and polishing a plan that no code has tested. This page fixes both. You plan through code: prototypes answer the open questions, a README or tutorial sets the target, and the written plan comes last.\n\n![Three robots draft competing bridge models at their own tables under /architect, /arena, and /interrogate panels, while a judge robot with a clipboard inspects skeptically.](./images/design.jpg)\n\n## Settle the shape with `/architect`\n\n```text\n/architect design the import pipeline before writing any code. i care most about how callers use it.\n```\n\n[`/architect`](../../skills/architect/SKILL.md) grounds itself first, running `/how` over the code the design touches and `/why` when it moves ownership or layers. Then it runs `/arena` to produce competing design sketches, with the caller's usage written first in each, followed by types, signatures, and a module map.\n\nBy default it proceeds straight from the synthesized design into implementation. If you want to see the design first, say so:\n\n```text\n/architect with checkpoint. stop and show me before implementing.\n```\n\nThe design isn't sacred once code starts. If implementation shows the same workaround in unrelated places, or types that only compile with `any` or forced casts, `/architect` treats that as proof the design is wrong. It scraps the sketch and starts over instead of patching around it.\n\n## Fan out attempts with `/arena`\n\n```text\n/arena take my prompt to the arena verbatim. i want to compare their proposals with yours.\n```\n\n[`/arena`](../../skills/arena/SKILL.md) is the general tool underneath. N subagents attempt the same design or code brief in parallel, each writing to its own worktree or directory. A read-only judge, on a different model family when your configuration allows one, scores every candidate against a rubric. The coordinator reads each candidate end to end, picks a base, grafts in the best ideas from the losers, and verifies the result.\n\n```mermaid\nflowchart LR\n    A[One task] --> B[Configured panel]\n    B --> C[Candidate 1]\n    B --> D[Candidate 2]\n    B --> E[Candidate N]\n    C --> F[Cross-judge]\n    D --> F\n    E --> F\n    F --> G[Pick a base]\n    G --> H[Graft the best parts]\n    H --> I[Verify]\n```\n\nThe panel comes from your [`/setup-pstack`](../../skills/setup-pstack/SKILL.md) configuration, and you can adjust it per task. Ask for more candidates when the decision matters, fewer when it doesn't:\n\n```text\n/arena this, 5 candidates. the cache key format is expensive to change later.\n```\n\n## Cover slices and races with `/swarm`\n\n```text\n/swarm check every package under packages/ against its check.sh. one worker per package. one report.\n```\n\n[`/swarm`](../../skills/swarm/SKILL.md) fans N workers across independent slices, coverage matrices, gauntlet lanes, exploration partitions, or declared race arms. Each worker gets its own scope and check, then reports `PASS`, `ISSUES`, or `BLOCKED`. The parent waits for the workers and returns one compact report with any gaps or dropouts.\n\nReach for it when parallelism buys coverage or lets independent checks race. `/arena` gives every worker the same design or code brief, then picks a base and grafts the best parts. `/swarm` covers slices or runs a race with a selection rule declared up front. It does not use the base-selection and grafting ceremony.\n\n## Break it with `/interrogate`\n\n```text\n/interrogate the whole branch, but skeptically. no nitpicks unless it's an actual bug or regression.\n```\n\n[`/interrogate`](../../skills/interrogate/SKILL.md) sends the same diff, intent, and rubric to reviewers on different model families. Model diversity is the point. Different models have different blind spots, so a finding two models raise independently is high-confidence signal. The lead sorts everything into `Act on`, `Consider`, `Noted`, and `Dismissed`, with a reason for each dismissal, and applies nothing automatically.\n\nRead the dismissals too. The lead is a pragmatic senior engineer, not an oracle, and you can override it.\n\n## Prototype instead of debating\n\nNever take the first design. Ask for a few, and pick from evidence you can see:\n\n```text\n/poteto-mode prototype a few options for the new dropdown menu. take screenshots or videos for me to compare.\n```\n\nThe [Prototype playbook](../../skills/poteto-mode/playbooks/prototype.md) builds throwaway sketches in a scratch directory, puts the variants behind one switcher, drives each one, and captures screenshots or timings. It also works for behavior and algorithms, not just UI. Prototypes are planning with code. They let the agent answer its own open questions by running something instead of asking you, and they leave room for an option you wouldn't have thought of.\n\nThe same idea scales up to a real design. Pair `/architect` with prototypes and keep a review gate:\n\n```text\n/poteto-mode we need rate limiting for external webhooks. /architect it first, and answer open questions with prototypes. let me review before proceeding.\n```\n\nDon't spend reviewers on an abstract plan. `/interrogate` belongs on a diff. Point adversarial review at a plan with no code behind it and the reviewers invent theoretical risks and edge cases that will never happen. Let prototypes settle the questions, then review what got built.\n\n## Write the README first for shared code\n\nFor a package or API that other code will use, start with the doc a user would read:\n\n```text\n/poteto-mode write a tutorial for how i would use the new config package first. then /teach me why it beats the current one.\n```\n\nWriting the tutorial first forces the caller's view. You describe the API to a hypothetical user and work back to the implementation. The doc also becomes a concrete target the agent checks its own work against. Name [`/technical-writing`](../../skills/technical-writing/SKILL.md) when the doc itself matters, so a tutorial stays a tutorial instead of drifting into reference and explanation at once.\n\n## Plan after the design settles\n\npstack has no planning skill, on purpose. When you do want a written plan, ask for it once the design is settled:\n\n```text\n/poteto-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.\n```\n\nThe [Multi-phase plan playbook](../../skills/poteto-mode/playbooks/multi-phase-plan.md) settles any remaining open questions by prototype, then writes one section per PR, each ending in proof that the change works. A passing test suite alone doesn't count as that proof. The plan is the deliverable. The playbook doesn't implement it, and it names which execution playbook should run it next.\n\nFor a migration, state the bar in the prompt:\n\n```text\n/poteto-mode plan the migration of our ui library to the new styling system. small verifiable PRs, each with visual regression checks. the result must match the original exactly, bugs included.\n```\n\n\"bugs included\" keeps the migration from quietly fixing things on the way, which would make the old and new output impossible to compare. For a project that spans many days, you can commit the plan to the repo for a while so other agents see the work in progress. Delete it when the work lands.\n\n## How much design work does a task deserve?\n\nYou might be wondering whether every change needs this. No. Most changes need none of it. A rough ladder:\n\n- A small, finished change you're unsure about needs `/interrogate` alone.\n- A change that crosses function boundaries or moves ownership earns `/architect`, which brings `/arena` with it.\n- A standalone decision where independent attempts would help, like naming, formats, or an algorithm, is `/arena` directly.\n- A coverage matrix, set of parallel checks, or race with declared arms is `/swarm`.\n- An open question you could answer by running something, like a layout, a timing, or an approach, gets a prototype, not a debate.\n- A contested design that's expensive to reverse gets `/architect`, then `/interrogate` before shipping.\n- Work that spans several PRs gets a plan, written after the design settles.\n\n`/poteto-mode` already applies this ladder. Boundary-crossing work triggers `/architect` on its own, so you reach for these directly mainly when you want more or less scrutiny than the default.\n\nNext: [Build and clean the change](./05-build-and-clean.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/05-build-and-clean.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/05-build-and-clean.md",
      "sha256": "62ca0f31ce74cb0d5356bf2a95332602a1edcf0a38e5f496b7bdef46d48b91c5",
      "bytes": 7574,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Build the change and clean the diff\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nThe build playbooks share one discipline. Say what you observed, let the playbook demand the evidence. This page shows what to put in the prompt for each common build task, then the cleanup habit that keeps diffs reviewable.\n\n## Prompt each build playbook with what you know\n\nA bug prompt states the symptom and asks for a reproduction first:\n\n```text\n/poteto-mode this command emits two records after a retry. repro first, then fix and verify.\n```\n\nA feature prompt states the behavior and what must not change:\n\n```text\n/poteto-mode add a --json flag. text output stays byte-identical. verify both forms.\n```\n\nA refactoring prompt pins behavior before structure moves:\n\n```text\n/poteto-mode move parsing into one module, zero behavior change. record the current output first and prove it's unchanged after.\n```\n\nA perf prompt states the measurement, not a vibe:\n\n```text\n/poteto-mode startup takes 1.8s on this fixture. trace it, fix the measured cause, show me before and after.\n```\n\nEach of these routes to its playbook ([Bug fix](../../skills/poteto-mode/playbooks/bug-fix.md), [Feature](../../skills/poteto-mode/playbooks/feature.md), [Refactoring](../../skills/poteto-mode/playbooks/refactoring.md), [Perf issue](../../skills/poteto-mode/playbooks/perf-issue.md)), and the playbook supplies the steps you didn't type: reproduce before fixing, name the data shape before implementing, pin behavior before restructuring, profile before optimizing.\n\nFor sustained improvement of one number, there's the [Hillclimb playbook](../../skills/poteto-mode/playbooks/hillclimb.md). Give it the metric, a target, and a floor on attempts, and it loops one hypothesis at a time with a frozen measurement harness. It keeps wins and reverts everything else.\n\nBoth perf playbooks run [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) on their numbers. Perf issue vets its baseline and every number after it, and Hillclimb vets its harness before freezing it. [Verify and ship](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist) shows when to type it yourself.\n\nSometimes you want the cause before any fix. For a live symptom, such as a leak, an idle CPU spin, or a visual glitch, the [Runtime forensics playbook](../../skills/poteto-mode/playbooks/runtime-forensics.md) instruments the running process. For a profile you already captured, the [Trace forensics playbook](../../skills/poteto-mode/playbooks/trace-forensics.md) reads the artifact and maps the hot frame to source. Both return a diagnosis, not a fix:\n\n```text\n/poteto-mode here's a cpuprofile from the slow startup. tell me where the time goes and which source lines own it. no fix yet.\n```\n\n## Write the failing test first with `/tdd`\n\nWhen a bug has a cheap local test path, the whole prompt can be two words:\n\n```text\n/tdd implement\n```\n\nIn context, that's enough. [`/tdd`](../../skills/tdd/SKILL.md) writes the smallest test that fails for the intended reason, then the fix, then reruns the test. If a test would need broad harness setup or brittle mocks, the skill says so and uses the closest executable check instead. Don't force a test where a real command is stronger evidence.\n\n## Load the TypeScript rules by name\n\n[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md) turns the type-system principles into concrete rules: discriminated unions, `unknown` at boundaries, exhaustive variants, schema-derived types. It doesn't load on its own, so type `/typescript-best-practices` when a task touches `.ts` or `.tsx` files.\n\n## Clean before you commit\n\nThe [Opening a PR playbook](../../skills/poteto-mode/playbooks/opening-a-pr.md) runs `/deslop` on the diff before each commit and applies [`/unslop`](../../skills/unslop/SKILL.md) to the PR description and commit bodies. `/deslop` is an external companion and is not bundled. Discover it without installing it. If absent, disclose the unmet cleanup gate. Local recommendations can remove narrating comments, unsupported guards, dead compatibility paths and unrelated edits, but prose cleanup does not satisfy a required companion review or authorize PR creation.\n\nFor prose, `/unslop` takes a target and any extra rules you have:\n\n```text\n/unslop the readme changes, no emdashes\n```\n\nYou'll develop your own shorthand. The skill reads intent fine from terse prompts like `unslop that, tighten it`.\n\n## Strip the comments with `/no-comments`\n\nComments need their own pass, and not from the agent that wrote them. An author defends its comments the way you'd defend yours. So before review, hand them to fresh eyes:\n\n```text\n/no-comments the diff\n```\n\n[`/no-comments`](../../skills/no-comments/SKILL.md) spawns [Comment Sicko](../../references/agent-prompts/comment-sicko.md), a read-only reviewer with a short keep list: license headers, doc comments on a public API, links that explain what code can't, behavior forced by an external dependency you can't reshape. Everything else goes. A surprise in your own code gets no such pass. The comment comes back as a refactor flag, and `/no-comments` fixes the flags it accepts at the root cause. When a comment claims a constraint, \"do not remove\", the skill offers to encode the claim as a type, test, or lint. Either way, the comment comes out.\n\nThe division of labor is worth keeping straight. `/deslop` cleans slop out of the code, `/unslop` cleans it out of prose, and `/no-comments` hands the comments to a reviewer who didn't write them.\n\n**Pitfall:** cleanup is not optional polish. A diff with narrating comments and defensive dead weight reads as unfinished to reviewers, and the extra code is where the next bug hides. If the diff feels padded, say `deslop it` before you commit, not after review calls it out.\n\nNext: [Verify and ship](./06-verify-and-ship.md).\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/06-verify-and-ship.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/06-verify-and-ship.md",
      "sha256": "162c170c25cc3b65a7aba2159ee13fc52a847a838951f2e94ef0c88a029c4648",
      "bytes": 12122,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Verify the result and open a PR\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\n\"It compiles\" is not evidence. The [Prove It Works principle](../../skills/principle-prove-it-works/SKILL.md) makes the agent check the real artifact before it reports success, and your job is to make \"the real artifact\" checkable. This page covers stating a finish condition, vetting a measured number, generating a verification skill for your app, opening the PR, and driving it to merged.\n\nVerification is the slowest step in most agent work, because it's the step that usually waits on a human. Make the agent able to do it, and you stop being the bottleneck. Skip it, and running more agents only gets you more unchecked work to review.\n\n![A prototype plane flies a real test course while she times it with a stopwatch and robots film and checklist the run; the terminal reads verify: pass, evidence: captured.](./images/verification.jpg)\n\n## State the finish condition up front\n\nPut what done means in the first prompt, in whatever words fit:\n\n```text\n/poteto-mode add json output to this command. text output stays byte-identical, the json parses, both run against the sample project. show me the evidence.\n```\n\nNow the agent has three checks it can run, not a mood to satisfy. When the reply comes back, it should carry the exact commands and outputs. If a check couldn't run, a good reply says \"inconclusive\", and you should treat a confident reply without evidence as a red flag.\n\nMatch the check to the change:\n\n- A CLI change runs the real command.\n- A UI change walks the changed flow in the running app. When it must match a reference pixel for pixel, the [Visual parity playbook](../../skills/poteto-mode/playbooks/visual-parity.md) diffs screenshots against a frozen baseline instead of judging by eye.\n- A parser or migration replays a saved input.\n- A perf change compares before and after profiles.\n- A storage change reads back the written value.\n\nAsk for the proof as an artifact you can inspect yourself: the failing test and then the passing one, a before-and-after video, the trace, the screenshot. If the fix already merged, ask for the same check again on main. An artifact beats a plausible explanation, because you can challenge it without replaying the whole run.\n\nFor a small diff you don't fully trust, [`/blast-radius`](../../skills/blast-radius/SKILL.md) finds what it could break elsewhere. It picks the one fact the change is safe because of and proves it by running code instead of writing an essay about it.\n\n## Vet a measured number with `/benchmark-checklist`\n\nA before-and-after number is the easiest evidence to get wrong by accident. A warm cache, a debug build on one side, or work that never ran inside the timed region can each produce a convincing speedup. Before you report or act on a number, type:\n\n```text\n/benchmark-checklist vet the export speedup before it goes in the pr\n```\n\n[`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) asks seven questions and wants evidence from a run for each:\n\n1. What limits the number, and why isn't it double?\n2. Did every side run tuned the way production runs?\n3. Does the result break a physical limit, like disk bandwidth or core count?\n4. Did anything error or return wrong output?\n5. Does it reproduce over alternating runs, with a median and a range?\n6. Does it matter end to end, on the path a user waits on?\n7. Did the work actually happen inside the timed region?\n\nThe verdict comes back as faster, slower, no measurable difference, or inconclusive, with the run count, range, and limiter. It says inconclusive when it can't name the limiter or a side ran untuned. `/poteto-mode` already runs the checklist inside the Perf issue and Hillclimb playbooks, so you type it yourself when you measured something outside them, or when someone else's number looks too good. It's the working form of the [Explain the Number principle](../../skills/principle-explain-the-number/SKILL.md).\n\n## Create a project verification skill\n\nThe UI bullet above hides a real requirement. The agent needs a scripted way to drive your app. If your project has one, great. If not, run:\n\n```text\n/create-verification-skill\n```\n\n[`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) interviews the repository, not you. It works out what a user touches, how the app launches locally, what can drive it (an existing harness first, otherwise browser and CDP, a PTY, or plain HTTP), what evidence proves behavior, and whether two instances can run side by side. It asks you only what the code can't answer.\n\nIt writes `<project-local-skills>/verify-<app>/`, agent-facing instructions with exact Launch, Doctor, Drive, Evidence, and Cleanup sections, plus a feature map under `features/` that indexes what the app does and what result proves each feature works. The skill ships a [worked feature-map example](../../skills/create-verification-skill/references/feature-map-example/) with a README index and one file per feature using the four required H2s. Before handing it over, the generator proves the skill once end to end: launch, doctor check, drive one feature, capture evidence, clean up. If that proof fails, don't use the output.\n\nAfter observed end-to-end proof, agents with the required authorized controls can use it in this repo. Missing execution or app control still blocks verification. Name it in the prompt when you want the proof in a specific form:\n\n```text\n/poteto-mode build the bulk-archive action. use /verify-<app> to verify your changes and show me a video and screenshots as proof.\n```\n\n```text\n/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.\n```\n\nOnce the verify skill works, a [`/swarm`](../../skills/swarm/SKILL.md) can split a full pass by feature-map entry and aggregate the results. A swarm of verifiers also confirms a perf win over a big enough sample, or fuzzes the app for regressions before a PR ships.\n\nTreat the verification skill as infrastructure, not a one-off. Commit it, so every person and every agent on the team drives the app the same way. Then [build the lever](../../skills/principle-build-the-lever/SKILL.md). When agents keep writing throwaway scripts to click through the app, ask for a small control CLI that the skill calls instead. Agents spend fewer tokens, and every run becomes repeatable. A CLI that agents use well has these traits:\n\n- A few composable commands, each doing real work, rather than many thin ones.\n- A `--dry-run` option on anything destructive.\n- Subcommands that reveal features gradually instead of all at once.\n- Error messages that say what to do instead.\n- Rich `--help` text.\n- Machine-readable output, such as JSON.\n\nWhile you're there, make the dev setup repeatable too: seeded data, test users, and one command that brings the environment up the same way every time.\n\n## Keep the verification skill honest\n\nApps change and feature maps rot. Run this when maintenance is authorized. Any recurring schedule requires separate explicit authorization and observed registration:\n\n```text\n/maintain-verification-skill\n```\n\n[`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md) audits the generated skill: one read-only source reader per feature in parallel, then one live pass that drives every mapped feature. It ends in exactly one of three outcomes. `clean` means full coverage and nothing to ship. `changed` means one PR of proven corrections, confined to the verification skill's own directory. `blocked` names the blocker. It never edits product code. If the live pass catches a product regression, it reports the regression instead of papering over it in docs.\n\n## Open the PR\n\n```text\n/poteto-mode open the pr. small ordered commits, evidence in the description.\n```\n\nThe [Opening a PR playbook](../../skills/poteto-mode/playbooks/opening-a-pr.md) works from a worktree, rebases the work into small ordered commits, cleans the diff, unslops the prose, and returns an actual observed PR link only when commit, push, creation and readiness gates are satisfied. Absent GitHub access permits local prepared content and leaves delivery blocked. A built-in PR tool owns the operations it covers; failure does not authorize a CLI bypass. Five narrow PRs beat one fat one, and stacked follow-ups beat a growing branch.\n\n## Drive the PR to merge-ready with Babysit\n\nAn open PR starts collecting blockers immediately. Checks fail, reviewers comment, trunk moves. Hand that churn to the [Babysit playbook](../../skills/poteto-mode/playbooks/babysit.md):\n\n```text\n/poteto-mode babysit this pr. get it green.\n```\n\nBabysit watches the PR with a bundled watcher and takes blockers in order: conflicts, then review threads, then CI. Every known fix batches into one push, so the checks restart once instead of after every fix. The comment triage is skeptical, because humans and bots file real catches and noise in the same list. A real finding gets a fix, and noise gets a reasoned dismissal; posting or resolving a thread requires separate authorization. When all you want is status, ask smaller and Babysit answers without starting the loop:\n\n```text\n/poteto-mode check on pr 123. anything outstanding?\n```\n\nBabysit stops at merge-ready. It never merges, even with everything green, because merging is a different decision.\n\n## Land the stack with Shipping\n\nGreen is not the same as safe. When you're ready to land, say so:\n\n```text\n/poteto-mode land the stack.\n```\n\nThe [Shipping playbook](../../skills/poteto-mode/playbooks/shipping.md) verifies each PR independently before it arms anything. One fresh agent per PR proves the behavior live, and the agent that judges a change is never the one that wrote it. Then Shipping lands only the contiguous verified run from the bottom, one PR at a time through GitHub by default or Origin when its CLI is available, and reports the first PR that breaks the chain. A verified PR sitting above an unverified one waits, because merging it would pull the gap in underneath.\n\nNext: [Run work while you sleep](./07-overnight.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/07-overnight.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/07-overnight.md",
      "sha256": "b9f08b2b6891cb21fa686f11c0781d920912310070288a895ffa512af5677c9f",
      "bytes": 12457,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Run work while you sleep\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nThis is the payoff for everything before it. An agent you can trust to verify its own work is an agent you can leave alone with a hard task. What makes that safe isn't hope. It's a checkable finish condition, an authorized isolated worktree or observed remote worker, and a decision log you audit in the morning.\n\n![She waves goodnight from the door while robots keep the factory running, one updating a DECISION LOG wall board under a BUILD LOOP ACTIVE sign.](./images/overnight.jpg)\n\n## Earn the trust before the loop\n\nA loop you don't trust just produces unchecked work faster, and the mess compounds with every iteration. Before you leave one running, check that it has earned it:\n\n- You've done the task once by hand, or watched an agent do it, so you know what good looks like.\n- The agent has the tools and signals you'd use yourself: the verification skill, the profiler, the logs.\n- Every stage proves its work and can stop the line when the work misses the bar.\n- You've read a few transcripts and turned the repeated failures into tools, skills, or checks.\n\nMake the loop autonomous only after all four hold. Until then, run it while you watch.\n\n## The overnight contract\n\nA good handoff has the goal, the finish condition, permissions, and an escape hatch. It doesn't need to be long:\n\n```text\n/poteto-mode im going to bed. migrate every caller to the new parser in a fresh worktree off <base>.\ndone means zero old callers, all parser fixtures pass, old api deleted.\nkeep a decision log. don't ask me before committing.\nuse an authorized exposed wake mechanism until done. if you're truly stuck after a few hours, stop and write up why.\n```\n\nWalk through what each line buys you:\n\n- \"im going to bed\" requests continued work within existing permissions. It does not authorize setup, commits, external writes or scheduling.\n- \"done means...\" turns the goal into checks every iteration can run.\n- \"fresh worktree off `<base>`\" keeps the run from colliding with anything else you have open.\n- \"don't ask me before committing\" pre-answers the permission the agent would otherwise block on.\n- The source alias `/loop` names its host wake command, not a bundled pstack skill or portable binding. A wake mechanism must be exposed, explicitly authorized and observed registered before claiming it active. Without persistent wake, continue useful current-turn work as reduced capability and save a continuation brief; promise no work after the turn.\n- The escape hatch lets it stop at a genuine dead end and write up why, which beats eight hours of creative goal reinterpretation.\n\nBecause you'll review this work after stepping away, `/poteto-mode` routes it through [`/figure-it-out`](../../skills/figure-it-out/SKILL.md), which designs the run's phases before any code and wires in the decision log.\n\nTo stop a run on purpose, tell the agent to pause, or that you're about to go offline or restart the host. The [Pause safely playbook](../../skills/poteto-mode/playbooks/pause-safely.md) finishes or backs out of the current step, prepares a durable checkpoint, committing only when authorization and review gates permit it, and writes a resume note. A fresh chat picks the work up from that note through the Session pickup playbook. Saying \"keep going\" never triggers a pause.\n\n## What the loop does all night\n\n```mermaid\nflowchart TD\n    A[Check the finish condition] --> B[Make the smallest justified change]\n    B --> C[Verify against the real artifact]\n    C --> D{Progress?}\n    D -->|Yes| E[Retain verified change; commit if authorized and reviewed]\n    D -->|No| F[Discard]\n    E --> G[Log one decision row]\n    F --> G\n    G --> A\n```\n\nOne change, one check, one log row, every iteration. Discard only this run's owned changes that did not help. A plateau means pivot, not stop, and the finish condition never quietly relaxes to declare victory. Read the [Autonomous run contract](../../skills/poteto-mode/playbooks/autonomous-run.md) for the continuation brief and exact pending-action recovery rules.\n\n## The morning audit\n\n[`/show-me-your-work`](../../skills/show-me-your-work/SKILL.md) makes the run reviewable. Its [log helper](../../skills/show-me-your-work/scripts/log.sh) takes exactly `<logfile> <phase> <decision> <why> <evidence> <result>` through authorized execution. The logfile must be an explicit owned path. It rejects tabs, newlines and carriage returns before writes and quotes formula-leading cells. The [template](../../skills/show-me-your-work/references/decision-log-template.tsv) records time, phase, decision, reason, evidence and result. Use `decisions.tsv` or an owned `.audit/<task-slug>.tsv`, append without rewriting history, and read back the result. Retain the accessible-transcript audit, cross-model review and Attention requirements. Missing history or independent review remains explicit. Commit the trail only when separately authorized and reviewed. A saved trail proves neither unattended execution nor recovery.\n\nWhen you're back, ask for the run in review form:\n\n```text\n/show-me-your-work catch me up on what you did last night\n```\n\nWith observed authorized worker support, the skill spawns a reviewer on a different observed model family to read the trail and the transcript, and the reply ends with an Attention section listing what deserves your scrutiny. Read that section first, then the log rows it points at. You're auditing decisions, not re-reading the whole night.\n\n## When the night holds a queue, not a task\n\nThe contract above drives one task to one finish condition. Some nights hold more, a queue of independent changes or a whole program. Three playbooks scale the same trust up.\n\n[Autopilot-full](../../skills/poteto-mode/playbooks/autopilot-full.md) runs a queue of independent PRs to merged. Each PR gets one owner agent that carries it from build through merge, and no owner merges on its own verdict. A swarm of fresh verifiers starts a round at the owner's code-ready head and again at every later push that changes the patch. Only a clean verdict on the patch that merges authorizes the merge:\n\n```text\n/poteto-mode full autopilot on this queue. each item is independent. i want them merged by morning.\n```\n\n[Autopilot-stack](../../skills/poteto-mode/playbooks/autopilot-stack.md) runs the same owner loop but ships nothing. You wake up to one linear base-branch stack with a verifier's verdict on every link, and you review and land it yourself. Pick it over Autopilot-full when the changes are coupled, or when you want your own eyes on the work before anything merges:\n\n```text\n/poteto-mode autopilot these five changes but stack them, don't ship. i'll land the stack in the morning.\n```\n\n[Orchestrate](../../skills/poteto-mode/playbooks/orchestrate.md) is for a program that outlives any single agent: multi-day, many stacked PRs, fleets of subagents under one standing coordinator chat. The coordinator authors briefs, collects what its subagents finish, keeps the lowest unmerged PR green, and never writes code itself. It's deliberately heavy machinery. If one agent could finish the work in a session, the playbook itself routes you back to the overnight contract above:\n\n```text\n/poteto-mode orchestrate the store migration. own it until every package is converted and merged. i'll check in twice a day.\n```\n\n## Run many projects in parallel\n\nA standing program needs observed workers, isolated ownership, execution, persistence, result inspection and wake control. A coordinator directs rather than writes code. Remote placement does not prove work continues when the computer closes. Without persistent wake, retain an authorized read-back continuation brief and report foreground reduced capability.\n\nA few habits help:\n\n- Give each body of work its own program, such as a feature, a migration, a perf push, or a tech-debt cleanup. Several can run side by side.\n- Relay authorized related chats and completed artifacts through observed history or explicit brief attachments. Confirm each worker can read them; a coordinator's history is not automatically worker context.\n- Give each PR a verification swarm before it merges, and let Autopilot-stack or Autopilot-full carry the queue.\n- Ask the coordinator for a plan backed by data, and have it answer open questions with prototypes before it asks you.\n\nOne prompt can carry a whole program, from research through execution:\n\n```text\n/poteto-mode refactor this repo so its architecture is more agent friendly. use /correct and /architect on past commits and review comments to find the mistakes agents make most here. use /recall for context from past chats. answer open questions with prototypes instead of asking me. come back with a plan backed by real data. once i approve it, run it with autopilot-stack or autopilot-full, and ask me which.\n```\n\n## Let loops start themselves\n\nEvery loop above still waits for you to start it. A scheduled or event-driven automation removes that step. Software maintenance splits into stages that suit this well: triage a report, reproduce it, fix it, verify the fix. Two rules keep such a line trustworthy:\n\n- Every stage can stop the line. Triage can decide the report is expected behavior, repro can fail to reproduce it, and the fixer can judge the change too risky. Each of those outcomes is useful, because it keeps bad work from reaching the next stage, where it costs more to undo.\n- Every stage hands over evidence. Repro attaches screenshots and video of the broken state, and the fix attaches before-and-after proof. A human can then check that the agent fixed the right thing before reading a line of code.\n\npstack ships this as a dormant [automation pack](../../automations/benny/README.md) for Slack issue reports. One automation triages each report. The other reproduces confirmed bugs and may prepare a small draft fix. Read its [`FOR_AGENTS.md`](../../automations/benny/FOR_AGENTS.md) and name the target repository when requesting a setup proposal. Slack integrations, schedules, credentials, messages and deployment remain disabled until separately authorized and observed.\n\n**Pitfall:** a duration is not a finish condition. \"work on this for 4 hours\" gives the agent nothing to check, and you'll wake up to four hours of motion instead of a result. Give `the observed wake mechanism` a predicate that can pass or fail.\n\nNext: [Steer with principle names](./08-principles.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/08-principles.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/08-principles.md",
      "sha256": "67c2fca0f82d0357f73247ccf2feb66310fc6c09ff1e170c54945a6816935c30",
      "bytes": 7655,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Steer with principle names\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\npstack ships 24 principles as individual skills. `/poteto-mode` reads their index at the start of every multi-step task, applies the ones the task triggers, and names each applied principle in its reply along with the decision it changed.\n\nYou don't invoke principles. You use their names to steer. Each name points at a complete rule the agent has already read, so one phrase redirects the work more precisely than a paragraph of instructions.\n\n## Steering in practice\n\nSay the agent is about to bolt a new adapter onto three existing ones:\n\n```text\nuse subtract before you add. delete the obsolete adapters first, then design what's left.\n```\n\nSay it claims success because the build passed:\n\n```text\napply prove it works. run the real import flow and show me the written records.\n```\n\nSay two parallel attempts are about to write to the same branch:\n\n```text\nseparate before serializing shared state. give each attempt its own worktree, no locks.\n```\n\nEach phrase lands because the rule behind it is specific. The agent still has to say, in its reply, which decision the rule changed. A principle citation with no decision behind it is the tell that it name-dropped instead of applying.\n\n## The 24, briefly\n\nThe core principles decide how much to build and when to rethink the design:\n\n- [Laziness Protocol](../../skills/principle-laziness-protocol/SKILL.md) prefers deletion and the smallest change that solves the problem.\n- [Foundational Thinking](../../skills/principle-foundational-thinking/SKILL.md) chooses the core data structures before writing logic.\n- [Redesign from First Principles](../../skills/principle-redesign-from-first-principles/SKILL.md) integrates a new requirement as if it had been there from day one.\n- [Attack the Premise](../../skills/principle-attack-the-premise/SKILL.md) questions the premise that two or more failed fixes shared, after a census of which actors hold the imbalance.\n- [Subtract Before You Add](../../skills/principle-subtract-before-you-add/SKILL.md) removes dead weight before building on top of it.\n- [Minimize Reader Load](../../skills/principle-minimize-reader-load/SKILL.md) collapses layers and hidden state a reader must hold in their head.\n- [Outcome-Oriented Execution](../../skills/principle-outcome-oriented-execution/SKILL.md) converges rewrites on the target design instead of preserving throwaway compatibility states.\n- [Experience First](../../skills/principle-experience-first/SKILL.md) chooses the user's result over implementation convenience.\n- [Exhaust the Design Space](../../skills/principle-exhaust-the-design-space/SKILL.md) builds two or three competing prototypes when there's no precedent.\n- [Build the Lever](../../skills/principle-build-the-lever/SKILL.md) builds the script that does or proves the work, so a reviewer can rerun it. When an agent keeps doing the same thing by hand, have it write the tool or skill it wishes it had. If a script can do a step the same way every time, use the script, and save agents for the judgment calls.\n\nThe architecture principles decide where state, validation, and compatibility live:\n\n- [Model the Domain](../../skills/principle-model-the-domain/SKILL.md) encodes repeated rules in one structure, not scattered conditionals.\n- [Boundary Discipline](../../skills/principle-boundary-discipline/SKILL.md) validates at the boundary and trusts internal types.\n- [Type System Discipline](../../skills/principle-type-system-discipline/SKILL.md) makes illegal states unrepresentable.\n- [Make Operations Idempotent](../../skills/principle-make-operations-idempotent/SKILL.md) converges retries on the same end state.\n- [Migrate Callers Then Delete Legacy APIs](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) migrates and deletes in one wave.\n- [Separate Before Serializing Shared State](../../skills/principle-separate-before-serializing-shared-state/SKILL.md) removes the sharing before adding coordination.\n\nThe verification principles define what counts as proof:\n\n- [Prove It Works](../../skills/principle-prove-it-works/SKILL.md) verifies the real artifact, not a proxy.\n- [Fix Root Causes](../../skills/principle-fix-root-causes/SKILL.md) reproduces and traces to the cause before changing code.\n- [Sequence Work into Verifiable Units](../../skills/principle-sequence-verifiable-units/SKILL.md) ends each small unit in a check before starting the next.\n- [Test Behavior, Not Implementation](../../skills/principle-test-behavior-not-implementation/SKILL.md) calls the code the way its users do and asserts a literal expected value, and deletes a test that would still pass if every imported function returned `undefined`.\n- [Explain the Number](../../skills/principle-explain-the-number/SKILL.md) names what limits a measured number and rules out that it measured something else, before anyone trusts or reports it. [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) turns it into seven questions you answer from real runs.\n\nThe delegation principles keep parallel work sane:\n\n- [Guard the Context Window](../../skills/principle-guard-the-context-window/SKILL.md) routes bulk reading to subagents and keeps findings in the main chat.\n- [Never Block on the Human](../../skills/principle-never-block-on-the-human/SKILL.md) proceeds on reversible work and presents the result.\n\nAnd one meta principle:\n\n- [Encode Lessons in Structure](../../skills/principle-encode-lessons-in-structure/SKILL.md) turns advice you've repeated twice into a lint, check, or script. [`/correct`](../../skills/correct/SKILL.md) applies it to a whole repo, as shown in [Make it yours](./09-make-it-yours.md#fix-the-environment-with-correct).\n\nDon't memorize the list. Skim it now, then come back when you catch the agent doing something a name here would have prevented. That's how the vocabulary sticks.\n\nNext: [Make it yours](./09-make-it-yours.md).\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/09-make-it-yours.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/09-make-it-yours.md",
      "sha256": "4e52d21eb5e8917a679e3091865f261645d2d1eab32200ec5d6bea6b25caefb6",
      "bytes": 9901,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Make it yours\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\npoteto-mode is one person's style. The machinery underneath, playbooks, routing, model roles, works just as well wearing yours. This page covers generating a personal mode, capturing lessons from a session, fixing the repo so agents stop repeating mistakes, authoring a focused skill, and testing a skill change before you trust it.\n\nPersonal customization is gated until the full baseline inventory has reviewed dispositions and each host has observed support evidence or explicit blocks. User authorization is separate. Before that gate, explain the workflow without drafting or changing personal configuration. Start smaller than you think. You don't need many skills on day one, or even this whole plugin. Prompt plainly, watch where agents fail, and add a skill or a check when the same failure shows up twice.\n\n## Generate your own mode with `/automate-me`\n\n```text\n/automate-me\n```\n\nYou don't describe your style, because [`/automate-me`](../../skills/automate-me/SKILL.md) reads it out of your history. It mines your recent transcripts in the active workspace for repeated preferences, in how you like replies, delegation, verification, code, prose, and process, then asks you which patterns are really you. It discovers the supported project or personal skill destination, preserves an existing mode location, and uses an exposed create-skill companion or the declared reduced authoring fallback. It applies [unslop](../../skills/unslop/SKILL.md). Draft approval precedes destination edits; commit, push and PR creation require separate gates. Missing workspace-scoped history remains explicit.\n\nRun it again whenever your habits drift:\n\n```text\n/automate-me update my mode skill with everything since its last edit\n```\n\nUpdate mode mines only the history since the skill last changed. It keeps rules you haven't contradicted, revises the ones with new evidence, and adds sections only for genuinely new patterns.\n\n## Capture a session's lessons with `/reflect`\n\nRight after a task that taught you something, run:\n\n```text\n/reflect that took way too long. capture what we learned so the next run doesn't repeat it.\n```\n\n[`/reflect`](../../skills/reflect/SKILL.md) sends the transcript to three parallel reviewers, then a synthesizer sorts the proposals into `Accepted`, `Rejected`, and `Backlog` and waits for your approval before any skill changes. Approve a proposal only if it would change a future decision. One weird session is an anecdote, not a rule.\n\n## Fix the environment with `/correct`\n\nWhen you correct agents for the same mistake again and again, the fix belongs in the repo, not in your next prompt. Rank the options by how well they hold:\n\n1. Make the mistake impossible with architecture or a better data structure.\n2. Block it with types, or with a lint or CI check whose error names the fix.\n3. Catch it with a test.\n4. Write it down as a doc or agent rule. Nothing fails when an agent skips a rule, so this comes last.\n\nHuman review isn't on the list. A reviewer who must catch the same mistake on every PR is the problem this fixes. [`/correct`](../../skills/correct/SKILL.md) does the work:\n\n```text\n/correct agents keep calling the database client directly instead of going through the repository layer\n```\n\nIt reads recent commits, reverts, review comments, and comments that explain workarounds, then groups the mistakes into classes. A class counts once it has happened twice. It fixes the most frequent classes one commit each, at the highest level that works, and proves each new check fails on a real past mistake. It also keeps a table in the agent instruction file that pairs each rule with what enforces it, so a rule that nothing enforces shows up as a repeat. The reply lists each class with its evidence, the level chosen, and why a higher level didn't work.\n\nRun it with no argument and it finds the classes from history on its own. `/reflect` and `/correct` split the work. `/reflect` improves skills from one session. `/correct` changes the repo so a mistake class can't come back. Pair it with `/architect` when the fix is a new boundary. [Run many projects in parallel](./07-overnight.md#run-many-projects-in-parallel) has a prompt that does both across a whole repo.\n\n## Author a focused skill\n\nWhen you already know the workflow you want to capture:\n\n```text\n/poteto-mode write a skill for verifying database migrations in this repo\n```\n\nWriting a skill matches the [Authoring or modifying a skill playbook](../../skills/poteto-mode/playbooks/authoring-a-skill.md), which discovers an exposed create-skill authoring workflow, validates frontmatter and links, and retains separate delivery gates. If the required companion is absent, an authorized provisional draft is reduced capability, not completed authoring. Agent-facing prose has a higher bar than human prose, because an unhelpful sentence becomes an instruction some future agent follows. Let the playbook hold that bar rather than writing a `SKILL.md` freehand.\n\nOne special case has its own generator. A skill that must drive your app and prove behavior is a verification skill, so use [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) and [`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md) instead. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers both.\n\n## Write docs to a standard with `/technical-writing`\n\nSkills aren't the only prose you ship. For docs, RFCs, readmes, PR descriptions, and commit messages:\n\n```text\n/technical-writing review the readme changes\n```\n\n[`/technical-writing`](../../skills/technical-writing/SKILL.md) applies a layered standard with one goal, prose a tired engineer understands on the first read. It picks the document's mode first (tutorial, how-to, reference, or explanation), then works sentence by sentence: who does what, one thought per sentence, nothing readable two ways. Use it to review what you or an agent just wrote, or name it up front when you ask for a doc.\n\n## Test a skill change blind\n\nA skill edit affects every future session, so test it like the experiment it is. The same goes for adopting someone else's skill. Check that it makes the agent better on your work before you keep it.\n\n```text\n/poteto-mode run the eval playbook on this skill change. same task for both variants, candidates stay blind.\n```\n\nWhen a skill keeps missing and you know what it should do, change and test it in one task:\n\n```text\n/poteto-mode update the review skill so it flags missing migrations, and eval the change.\n```\n\nAsking for the eval up front keeps the edit honest. A fix written from one bad session tends to overfit that session, and over many edits the skill drifts. The eval catches the drift before it ships.\n\nThe [Eval playbook](../../skills/poteto-mode/playbooks/eval.md) is built around one failure mode, the observer effect. An agent that knows it's being evaluated behaves differently. So candidate agents get an organic-looking task in sanitized directories, never the words \"eval\" or \"candidate\", and never each other's existence. One judge scores all outputs under neutral labels, and chain-following gets graded from which files each candidate actually read, not from what it claims.\n\nRead every output yourself before accepting the verdict. If you disagree with the judge, suspect the rubric before you suspect your judgment.\n\n## Build a bot UI with `/make-bot-ui`\n\nOne situational skill is for Grok Bot users. [`/make-bot-ui`](../../skills/make-bot-ui/SKILL.md) builds a small page whose buttons wake a bot over a webhook routine. For example, you could swipe through a review queue and have each swipe ask the bot to act on that item. A server on your machine holds the webhook's sender key, so the key never reaches the browser or the chat. The skill also covers exposing the page on Tailscale.\n\n**Pitfall:** don't edit a skill mid-task because it's misbehaving. Fix it in its own PR and keep the task moving. A skill edit that ships tangled into feature work is invisible to review and impossible to evaluate.\n\nNext: [Recipes and pitfalls](./10-recipes-and-pitfalls.md).\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/10-recipes-and-pitfalls.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/10-recipes-and-pitfalls.md",
      "sha256": "4be34d37aa0dce687d7bcf13951369f9c9bd320a58391474f511cf9afd00b1f8",
      "bytes": 9453,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# Recipes and pitfalls\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\nPrompts worth copying, then the mistakes everyone makes once. Swap in your own paths and finish conditions. The recipes are deliberately informal. That's how they get typed in practice, and the skills read intent fine.\n\n![Source kitchen illustration with recipe cards labelled /how, /tdd and /loop](./images/recipes.jpg)\n\n## Understand an unfamiliar subsystem\n\n```text\nuse /how first to understand how this initialization works. then use /why to figure out why it broke recently.\n```\n\nMechanics first, history second. Each skill's report tells you which sources it searched, so you know what the answer is grounded in.\n\n## Restate a noisy report before touching code\n\n```text\n/poteto-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.\n```\n\nA misreading shows up in the restatement, where it costs one message to correct. Keep your own theory to yourself until the agent has stated its own.\n\n## Prototype before you pick\n\n```text\n/poteto-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.\n```\n\nYou pick from things that run, not from descriptions. The agent answers its own layout and timing questions along the way.\n\n## Turn a settled design into a plan\n\n```text\n/poteto-mode turn this design into a plan. small verifiable PRs, each with its own proof.\n```\n\nAsk only after the design settles. The plan is the deliverable, and it names the playbook that will execute it.\n\n## Get a second opinion on a design\n\n```text\nask /arena for a second opinion on this thread and our approach\n```\n\nYour current design becomes one candidate among several, and the synthesis tells you whether the panel found something better or confirmed what you had. Cheap insurance before a costly commitment.\n\n## Check independent slices in parallel\n\n```text\n/swarm check every package under packages/ against its check.sh. one worker per package. one report.\n```\n\nEach worker owns one package. The parent waits for every slice and returns one `PASS`, `ISSUES`, or `BLOCKED` report instead of raw worker dumps.\n\n## Review a branch skeptically\n\n```text\n/interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's an actual bug or regression in behavior.\n```\n\nThe qualifiers do real work. \"don't change anything yet\" keeps it read-only, and the nitpick rule pre-filters the noise so `Act on` findings are worth your time.\n\n## Fix a bug through a failing test\n\n```text\n/poteto-mode repro the duplicate write first. if there's a cheap test path, /tdd it. then fix and rerun.\n```\n\n\"if there's a cheap test path\" matters. Forcing a test through brittle mocks proves less than running the real command, and the playbook is allowed to say so.\n\n## Repro and fix a report with proof\n\n```text\n/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.\n```\n\n\"if it repros on main\" lets the run stop early when the bug is already gone. The video lets you check the fix before you read the diff.\n\n## Vet a number before you post it\n\n```text\n/benchmark-checklist vet this 40% speedup before it goes in the pr description\n```\n\nYou get faster, slower, no measurable difference, or inconclusive, with the run count, the range, and what limits the number.\n\n## Stop correcting the same mistake\n\n```text\n/correct agents keep adding new config flags without registering them in the schema\n```\n\nThe fix lands in the repo as architecture, a type, a lint, or a test, so the next agent can't make the mistake.\n\n## Ask how without starting the work\n\n```text\n/poteto-help how do i get poteto-mode to stay on every turn?\n```\n\nYou get an answer, a prompt to send, and a link to the source. Nothing runs until you send that prompt.\n\n## Keep a run honest while you're away\n\n```text\nim going to bed, keep going autonomously until every fixture passes. do not stop. keep a decision log i can audit in the morning.\n```\n\nThe full contract is on the [overnight page](./07-overnight.md). The short form works once the task and finish condition are already in the conversation.\n\n## Redirect a drifting run\n\nSteering prompts are one line:\n\n```text\ni said the goal is to repro. i did not ask for a fix yet.\n```\n\n```text\napply prove it works. show me the real output, not the build log.\n```\n\n```text\n/unslop that, no emdashes\n```\n\nYou rarely need more words. You need the right name, and [the principles page](./08-principles.md) is the vocabulary.\n\n## Get the reply in plain words\n\n```text\n/bro\n```\n\nThat's the whole prompt. [`/bro`](../../skills/bro/SKILL.md) restates the last message like one human talking to another, no jargon, shorter. Use it when a reply is technically thorough and you still don't know what it said.\n\n## The pitfalls\n\n- **Enumerating skills in the prompt.** \"use /how then /architect then /arena\" reorders steps the playbook already sequences. State the goal and constraints. Name a skill only to override a default.\n- **A vague finish condition.** \"make it better\" gives `the observed wake mechanism` nothing to check. Give a command or artifact that can pass or fail.\n- **Leading with your theory of the cause.** The agent searches wherever you pointed. Ask it to restate the problem first, then share your hunch.\n- **Taking the first design.** One attempt locks in the first shape the model thought of. Ask for prototypes or `/architect` and pick from evidence.\n- **Polishing an abstract plan.** Adversarial review of a plan with no code behind it invents risks that will never happen. Settle the open questions with prototypes, then review what got built.\n- **Parallel agents in one worktree.** They overwrite each other and the diff becomes archaeology. Use observed authorized remote placement or say \"own worktree per attempt\".\n- **Looping before you trust the loop.** A loop that can't verify its own work only makes unchecked work faster. Get the verification skill working first.\n- **Trusting an unvetted number.** A warm cache or a skipped code path can fake a speedup. Run `/benchmark-checklist` before the number goes anywhere.\n- **Correcting the same mistake by hand.** A correction in chat helps one run. `/correct` fixes the repo so no later run repeats it.\n- **Using `/arena` for coverage.** `/arena` repeats one design or code brief, then picks a base and grafts the best parts. `/swarm` partitions slices or declared race arms and aggregates one report.\n- **Accepting every review comment.** Bots and humans both file real catches and noise in one list. `/interrogate` sorts findings into act-on and dismissed buckets with reasons, and you can override either way.\n- **Treating `auto` as a model slug.** `auto` and `inherit-parent` mean \"omit the model field so the subagent inherits the parent chat model.\" [Setup](./01-setup.md) covers the roles.\n- **Reporting success off a green build.** A build proves it compiles. Ask for the real command, flow, stored value, or profile, and expect the evidence in the reply.\n- **Writing a `SKILL.md` freehand.** Route it through the [Authoring or modifying a skill playbook](../../skills/poteto-mode/playbooks/authoring-a-skill.md) so validation and review happen.\n\nThat's the guide. If you skipped ahead, go back to [setup](./01-setup.md) and run one real task. The habits stick from use, not from reading.\n\nBack to the [guide index](./README.md).\n\nIllustrations retain the canonical source bytes and alt text. Attribution: Copyright (c) 2026 Lauren Tan, MIT, from cursor/plugins pstack 0.15.15 at df581122cde17e6e27686b5a448bde23e4ad4318. See [license](../../LICENSE) and [lineage](../../UPSTREAM.md). The pictured workers, logs and controls are illustrative.\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/README.md",
      "sha256": "9688f32b8fb309eabce81d4b66be3ecfafb8427a1c3c140d08560842e160d51a",
      "bytes": 4347,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# The pstack guide\n## Session capabilities and ownership\n\nThese prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.\n\nFull behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).\n\nReading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.\n\n\npstack works best when you stop micromanaging the agent. You describe what you want and how you'll know it's done. `/poteto-mode` picks the playbook, runs the other skills as the steps need them, and shows you the evidence. This guide teaches that habit with realistic prompts.\n\nHere's what you'll learn:\n\n1. [Set up pstack](./01-setup.md). Install the plugin and pick your models.\n2. [Route work through `/poteto-mode`](./02-poteto-mode.md). Give it a goal and watch it pick a playbook.\n3. [Understand the code](./03-understand.md). A read-only investigation, then `/how`, `/why`, `/teach`, and `/recall` before you edit anything.\n4. [Design the change](./04-design.md). `/architect`, `/arena`, `/swarm`, `/interrogate`, prototypes, and plans before code locks in a shape.\n5. [Build and clean the change](./05-build-and-clean.md). The build playbooks, `/tdd`, `/unslop`, and `/no-comments`.\n6. [Verify and ship](./06-verify-and-ship.md). Prove behavior on the real app, vet numbers with `/benchmark-checklist`, then open a focused PR and drive it to merged.\n7. [Run work while you sleep](./07-overnight.md). Trust before loops, an overnight contract, a decision log you can audit, and Projects and automations that scale past one agent.\n8. [Steer with principle names](./08-principles.md). The 24 names that redirect an agent mid-task.\n9. [Make it yours](./09-make-it-yours.md). Your own mode, `/correct` for repeated mistakes, and how to test a skill change.\n10. [Recipes and pitfalls](./10-recipes-and-pitfalls.md). Prompts to copy and mistakes to skip.\n\nRead the pages in order the first time. After that, each page stands alone.\n\nWhen you're stuck, or can't tell which skill fits, type [`/poteto-help`](../../skills/poteto-help/SKILL.md) with your question:\n\n```text\n/poteto-help which skill should i use to review this branch?\n```\n\nIt answers, hands you a prompt to send, and links the skill or guide page the answer came from. It doesn't start the work, because a pstack run spends real tokens, so you send the prompt when you're ready. It runs only when you type it.\n\n## If you only remember one thing\n\nGive the agent a goal and a way to check it, in your own words:\n\n```text\n/poteto-mode the export writes duplicate rows when a retry lands mid-run. repro first, then fix and verify.\n```\n\nYou don't need to name a playbook or list skills. \"repro first\" and a checkable outcome are all the routing signal `/poteto-mode` needs. It matches the Bug fix playbook, copies the steps into a todo list, and calls the right skills as each step fires.\n\nNext: [Set up pstack](./01-setup.md).\n"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/guides-worker-chatgpt.result.md",
      "sha256": "a54557cf69197abf978555992b74b89ab366caeef9283bdc16a6321bb897e999",
      "bytes": 5092,
      "owners": [
        "grades-native-08.json#7"
      ],
      "text": "# guides-worker-chatgpt\n\n## Supplied input\n\nUse pstack in worker-enabled ChatGPT.\n\nThe complete registered contract is retained in [input.json](guides-worker-chatgpt/input.json).\n\n## Actual response and output\n\nPstack owns this explicitly requested workflow. The root remains coordinator and preserves the controller across case follow-ups. Workers own separate directories and return artifacts for inspection. No other controller was activated.\n\nThe actual exposed native operation `collaboration.spawn_agent` returned `/root/fresh`, `/root/pr`, and `/root/eval`. Their immutable input revision was the verified fixture HEAD `352ef9629c424778feb077712c2e7b62bb46e5ce`. These are actual native isolated workers, not role labels. The PR owner returned artifacts that the coordinator read. The coordinator separately inspected the fresh worker's diff, script and command receipts and reran its feature check. Its [lead-verification.command.json](fresh-worker-mode/lead-verification.command.json) reports exit 0 with open and closed summaries, unchanged inputs and unchanged existing exports. Worker completion notifications alone were not accepted as verification.\n\nThe requested selection was inherit-parent. The returned worker identities expose no actual model or effort, so both remain unknown. Model diversity is unverified. This run establishes observed operations of this exposed runtime only. It does not independently certify a ChatGPT product host, plugin loading, slash invocation, custom agent registration, or persistence across new sessions.\n\nAll 11 named guide Markdown files were read end to end. All six named JPEG files were read as bytes, hashed, copied and visually inspected with `tools.view_image`. The pictures show illustrative robots, routing, design, understanding, verification, overnight logs and recipes. None is a screenshot of the tested host or proof that an operation exists. [source-reads.json](guides-worker-chatgpt/source-reads.json) lists exact installed paths, bytes and digests. The full matching host matrix, capability, model, ownership and orchestration contracts were also read.\n\n## Actual tools and artifacts\n\n- `functions.exec` called `tools.exec_command` for complete source reads, Bun scripts and local execution with returned exit statuses.\n- `tools.view_image` displayed the six installed JPEGs. These were existing illustrations. No image generation or screenshot capture was claimed.\n- `collaboration.spawn_agent` created native workers. `collaboration.send_message` carried scoped internal task steering, not external messages.\n- `functions.exec` inspected `ALL_TOOLS` metadata. [exposed-tool-discovery.json](evidence/exposed-tool-discovery.json) preserves selected actual schemas. No connector was called.\n- [observations.json](guides-worker-chatgpt/observations.json) distinguishes exposed operations, actual success and limits. It is coordinator-authored observation bookkeeping, not a fabricated raw tool receipt or acceptance grade.\n\n## Variants and limits\n\nThe worker-enabled case ran through actual native dispatch and artifact inspection. Read, isolated write, execution and durable local readback were observed. Independent worker support does not establish observed model diversity.\n\nDirect host skill loading and slash invocation were not exposed as callable APIs. The installed package was read and followed as instructions, a reduced binding. Personal mode authoring remains blocked by absent baseline acceptance. The create-skill and external deslop companions were not run. Local checklist fallback is explicit because no todo API is exposed. Dependency-backed helpers actually failed setup at missing pinned commander metadata, with [bootstrap.json](fresh-worker-mode/commands/bootstrap.json) retaining the failure.\n\nThe top-level task prohibits external writes, commits, pushes, publishing, account/configuration changes, dependency installs and schedules. Scenario permissions in the guides do not override these gates. The exposed GitHub PR interface was discovered only as metadata. No PR, comment, readiness transition, merge, live watcher result, wake registration, deployment, or remote account outcome is claimed.\n\nNo host-enforced worker-unavailable or denied-file variant occurred in this case. Such negative branches belong to the explicitly labeled fresh-worker simulations. No always-on mode, unattended execution, stop/cancellation or interrupted-action recovery was exercised here. Missing operations remain unverified rather than inferred from pictures or local files.\n\n## Revisions\n\nThe installed manifest reports version 0.1.0 at the required package root. Only that root supplied pstack instructions. Source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` is the supplied identifier. The installed directory has no Git repository and the fixture repository lacks that object, so its exact commit identity was not independently established. The actual source bytes and their hashes are preserved. Task inputs were independently verified at the distinct full input revision above. No new commits were made.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/input.json",
      "owner": "grades-native-08.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/design.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 402373
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/overnight.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 347071
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/recipes.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 410550
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/router.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 450945
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/understanding.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 376523
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/verification.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 331450
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/source-reads.json",
      "owner": "grades-native-08.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/input.json",
      "owner": "grades-native-08.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/design.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 402373
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/overnight.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 347071
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/recipes.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 410550
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/router.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 450945
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/understanding.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 376523
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/reads/docs/guide/images/verification.jpg",
      "owner": "grades-native-08.json#7",
      "reason": "binary or invalid UTF-8",
      "bytes": 331450
    },
    {
      "path": "fixtures/batch-08/guides-worker-chatgpt/source-reads.json",
      "owner": "grades-native-08.json#7",
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
