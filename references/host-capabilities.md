# Discover capabilities in the current session

Read the tools exposed to this session before assigning work. Cached official-subagents.txt is documentation context; it proves no operation succeeded. Local agent configuration is not portable plugin configuration.

Record each binding as `{operation, tool, exposed, succeeded, evidence, limits}`. `tool` is the exact exposed identifier or null when absent. `succeeded` is true only after observing a result. Keep failed and unavailable bindings. Successful bindings become `successfulOperations` in host evidence, with a root-relative evidence file. The operation labels below describe purposes, never callable APIs.

| Operation | Discovery and observation required |
| --- | --- |
| spawn | Find an exposed independent-worker operation; retain returned worker identity and exact assigned revision. |
| follow-up | Find the operation that sends input to that worker; observe acceptance by the same identity. |
| wait | Find the operation that waits for worker state; retain terminal or interrupted state. |
| inspect-result | Read the worker result and its referenced artifacts; a wait notification alone is insufficient. |
| stop | Observe cancellation or termination through the exposed operation. |
| read | Observe the requested file content through the available file tool. |
| isolated-write | Observe a write within the worker's assigned path and permissions. |
| history | Observe available prior turns or records; declare gaps explicitly. |
| execution | Observe command execution with exit status and output. |
| persistence | Write and read an authorized durable record; a claimed save is insufficient. |
| external-write | Record explicit authorization and action identity; inspect the result before replay. |
| resolve-ownership | Observe distinct owned paths before contested writes. |
| inspect-terminal | Observe the worker's terminal state after stop. |
| quarantine-artifacts | Observe partial artifacts withheld from integration. |
| inspect-prior-action | Read the interrupted action identity and prior outcome. |
| inspect-destination | Observe the destination state for that action identity. |
| safe-recovery | Observe explicitly authorized idempotent recovery after identity and destination inspection. |

No default API names are assigned here. Tool names differ by host and session. An exposed tool may still be denied or fail. Record requested and actual models only when observed; otherwise use `unknown`. A requested model never proves the actual model.

A denied or unavailable operation blocks the branch that requires it. Sequential substitution for required independent work is reduced capability and uses `reduced-pass`; ordinary direct completion can fully pass. Missing persistence limits session pickup even when current work succeeds. Preserve user authorization and host permission boundaries through every fallback.

Worker passes require observed spawn and result inspection. Each registry entry declares `requiredObservations` for `pass` and `reduced-pass`; tool observations need exposed bindings and existing evidence artifacts; native text observations use the separate reviewed native record below. Full cancellation requires stop, terminal inspection and artifact quarantine. Full persistence requires durable write and readback. Full interrupted-action recovery requires prior identity inspection, destination inspection, safe recovery, explicit external permission and a recorded prior action identity even when no external-write observation is listed.

Permission checks follow performed operations. Isolated writes and persistence require granted writes. External writes and safe recovery require granted external permission and prior identity. Authorized read-only reductions may retain denied writes; their limits must preserve denied or unavailable permissions. Required observations remain applicable to those reductions.

Host evidence is stored as object or array JSON files under `docs/parity/evidence/`. Required fields are defined by `docs/parity/evidence.schema.json`. Artifacts and operation evidence must be existing files inside the tested root. Test fixtures belong in `tests/` and prove validator behavior only.

Run `python3 tools/validate_evidence.py --root . --commit <tested-package-commit>` through Bun, for example `bun -e 'const p=Bun.spawnSync(["python3","-B","tools/validate_evidence.py","--root",".","--commit",process.argv[1]],{env:{...process.env,PYTHONDONTWRITEBYTECODE:"1"}});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode)' <tested-package-commit>`. It reads every JSON record below the evidence directory, prints each error, and exits 1 for invalid records or 0 for valid records. An empty directory has no invalid records and supplies no behavioral evidence.

The required registry file in `docs/parity/case-registry.json` declares applicability. Missing or non-file registry, unknown case, structural-only entry or unlisted host rejects behavioral validation. Maintenance fixtures use a temporary copy of this registry; they cannot bypass applicability. Required hosts must receive observed evidence or explicit blocked records before release claims. Structural checks have no required host and cannot populate host status. Later producers propose task-owned entries; only the coordinator integrates them. Source paths select callers through the task 3 case contract. Case definitions alone leave host statuses `not-run`.

## Direct completion and recorded observations

`direct` means the task is completed in the current context. Restatement, supplied-text writing and complete installed discovery can pass directly. `sequential` is reserved for replacing a required independent method with sequential work and remains reduced. A text response has no invented callable tool. Record supplied input, the actual response and qualitative outcome review as `nativeObservations`, each with its existing listed evidence artifact and named reviewer. Their labels are `supplied-input`, `response` and `review-outcome`. The reviewer assesses the case's expected outcome; validation checks evidence relationships and does not decide prose quality.

Each registry entry declares allowed execution modes and required permissions for each status. A grant is required for the performed action: worker spawn, command execution and stop need execution; isolated output or persistence needs writes; external actions need their separate permission and prior identity. Read-only discovery does not inherit an execution grant requirement. Tool observations still name an actually exposed tool and existing evidence. Native observations cannot claim tool discovery, worker identity or saved writes.

Full Arena and Swarm results additionally provide `inputRevision` and a listed `methodReceipt` artifact. An exposed `inspect-method` operation must reference that receipt. Assignment operations name `assignmentId` and the corresponding inspected output. See the [structured method contract](orchestration-contract.md). All positive maintenance fixtures are synthetic; none is an observed host result.
