# Compatibility

The repository retains reviewed version 0.1.3 evidence at frozen revision `51f209daf83cd97d64f89881d66533bb59dc57db`. Before publication preparation, the release report validated discovery and 104 workflow cases per host. This does not establish full behavioral parity. The edited publication candidate needs a new frozen identity and fresh discovery; historical results do not transfer automatically.

| Frozen 0.1.3 workflow results | Passed | Reduced capability | Blocked |
| --- | ---: | ---: | ---: |
| Codex | 33 | 50 | 21 |
| ChatGPT | 21 | 56 | 27 |

Package discovery is a separate passing case on each host. See the [controller report](releases/remaining-controller-report.md) and the [publication checklist](publication.md) for the current preparation boundary. The table below describes capability limits; use the case indexes for exact observed outcomes.

| Host or operation | Candidate status | Evidence needed |
| --- | --- | --- |
| ChatGPT loading | Discovery recorded at the frozen revision; other environments require their own supported route | Actual supported loading control, setup authorization and fresh complete discovery for the candidate |
| Codex loading | Discovery recorded at the frozen revision | Actual installed-copy operation, full 51-root enumeration, version and final frozen SHA for the candidate |
| Independent Arena or Swarm | Workflow outcomes include reduced capability; full orchestration depends on the case and host | Authorized observed spawn, terminal results and inspected artifacts |
| Sequential supplied-source work | Possible reduced branch, not a recorded pass | Actual authorized reads and artifacts, required observations and complete discovery for package acceptance |
| Dependency-backed helpers | Setup-required in operative candidate | Exact local dependency metadata and caller-specific execution evidence |
| Historical helper validation | Passed only in isolated snapshot | [Helper guide](testing/helper-setup.md) identifies the exact tested source SHA and limits |
| Optional integrations and Benny | Case-specific; unavailable adapters and integrations remain blocked | [Benny readiness](testing/benny-readiness.md), actual bindings and separate action permission |

Use [host matrix](testing/host-matrix.md), [case registry](parity/case-registry.json), [case schema](parity/cases/schema.json) and [evidence schema](parity/evidence.schema.json). Required cases need actual host observations or explicit blocked records. Complete discovery needs the identical 51-root receipt in a direct pass, worker pass or validated sequential reduced-pass. Ordinary direct completion is full when it satisfies every case requirement. A reduction never proves worker independence or full orchestration.

[Release report](../tools/release_report.py) checks actual root evidence and discovery. An empty evidence directory is not a pass. Regenerate or check this summary against the actual release report after host testing; retain missing, stale and blocked results.

Freeze operative content and navigation together. Record the exact tested SHA separately from later report commits in `docs/parity/tested-package.json` only once the frozen SHA exists. The [marker contract](maintenance/rollback.md) permits only explicit narrow report paths and verification changes. Full tracked bytes and modes, including setup and navigation, must match. After blocked records merge and catalog regeneration changes operative catalog bytes, take an explicit second freeze and attach fresh blocked discovery observations to its exact SHA. Preserve both freeze SHAs and earlier records in Git history. The final handoff navigation must be a no-op unless explicitly refrozen; no evidence pass is inherited.
