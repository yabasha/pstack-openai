# Candidate compatibility

This is an evidence-bounded candidate summary, not a list of assumed product tools. Current [inventory](parity/inventory.json) records both hosts as not-run. Installed discovery is absent and required host validation is pending. Local source inspection, schema checks and helper fixtures prove no host loading or behavioral parity.

| Host or operation | Candidate status | Evidence needed |
| --- | --- | --- |
| Personal ChatGPT loading | Unsupported route, explicitly blocked | Actual supported loading control, exact separate setup authorization and fresh complete discovery |
| Codex loading | Documented route, unverified and undiscovered | Actual installed-copy operation, full 51-root enumeration, version and final frozen SHA |
| Independent Arena or Swarm | Not-run on both hosts | Authorized observed spawn, terminal results and inspected artifacts |
| Sequential supplied-source work | Possible reduced branch, not a recorded pass | Actual authorized reads and artifacts, required observations and complete discovery for package acceptance |
| Dependency-backed helpers | Setup-required in operative candidate | Exact local dependency metadata and caller-specific execution evidence |
| Historical helper validation | Passed only in isolated snapshot | [Helper guide](testing/helper-setup.md) identifies the exact tested source SHA and limits |
| Optional integrations and Benny | Not-run or blocked when unavailable | [Benny readiness](testing/benny-readiness.md), actual bindings and separate action permission |

Use [host matrix](testing/host-matrix.md), [case registry](parity/case-registry.json), [case schema](parity/cases/schema.json) and [evidence schema](parity/evidence.schema.json). Required cases need actual host observations or explicit blocked records. Complete discovery needs the identical 51-root receipt in a direct pass, worker pass or validated sequential reduced-pass. Ordinary direct completion is full when it satisfies every case requirement. A reduction never proves worker independence or full orchestration.

[Release report](../tools/release_report.py) checks actual root evidence and discovery. An empty evidence directory is not a pass. Regenerate or check this summary against the actual release report after host testing; retain missing, stale and blocked results.

Freeze operative content and navigation together. Record the exact tested SHA separately from later report commits in `docs/parity/tested-package.json` only once the frozen SHA exists. The [marker contract](maintenance/rollback.md) permits only explicit narrow report paths and verification changes. Full tracked bytes and modes, including setup and navigation, must match. After blocked records merge and catalog regeneration changes operative catalog bytes, take an explicit second freeze and attach fresh blocked discovery observations to its exact SHA. Preserve both freeze SHAs and earlier records in Git history. The final handoff navigation must be a no-op unless explicitly refrozen; no evidence pass is inherited.
