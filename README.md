# pstack portable package

An unofficial port of Lauren Tan's pstack v0.15.15. The pinned baseline includes 51 root skills, 24 principles, 23 playbooks and 164 source files. Read [UPSTREAM.md](UPSTREAM.md), [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE) for lineage and attribution.

The implementation is a candidate awaiting aggregate review, frozen-package discovery and fresh host observations. Both hosts remain unverified. A local file read does not prove installed discovery. See [compatibility](docs/compatibility.md) before relying on a workflow.

## Start here

- [Personal ChatGPT setup and blocked route](docs/setup/chatgpt.md).
- [Codex setup and unverified documented route](docs/setup/codex.md).
- [Choose a workflow](docs/workflows/choosing-a-workflow.md).
- [All 51 skills](docs/skills/README.md) and [all 24 principles](docs/principles/README.md).
- [Preserved guide](docs/guide/README.md).
- [Arena walkthrough](docs/workflows/arena.md), [Swarm walkthrough](docs/workflows/swarm.md) and [Poteto mode walkthrough](docs/workflows/poteto-mode.md).
- [Troubleshooting](docs/troubleshooting.md) and [host test matrix](docs/testing/host-matrix.md).
- [Helper dependency setup](docs/testing/helper-setup.md) and [optional Benny readiness](docs/testing/benny-readiness.md).
- [Upstream check, prepare, apply, validation and separate acceptance](docs/maintenance/upstream-updates.md).
- [Conflict resolution format](docs/maintenance/update-resolutions.example.json) and [rollback](docs/maintenance/rollback.md).
- [Package validator](tools/validate_package.py), [evidence validator](tools/validate_evidence.py), [update CLI](tools/sync_upstream.py), [release report CLI](tools/release_report.py) and [catalog renderer](tools/build_catalog.py).
- [Acceptance cases](docs/parity/cases/documentation-walkthroughs.json), [inventory](docs/parity/inventory.json) and [case registry](docs/parity/case-registry.json).
- [Design](docs/superpowers/specs/2026-10-07-pstack-openai-design.md) and [implementation plan](docs/superpowers/plans/2026-10-07-pstack-openai.md).

## Permissions and package identity

Instructions grant no installation, settings, integration, external write or recurring schedule permission. Development dependencies and host plugin loading are separate approvals. Models and workers require current exposed operations and actual observations.

Candidate navigation is frozen with operative content. The final handoff must keep these bytes unchanged or explicitly refreeze and relink fresh blocked observations. Evidence/report commits can follow the tested commit only under the exact [tested-package marker contract](docs/maintenance/rollback.md). After blocked host records enter the inventory and regenerate the catalog, an explicit second freeze is required. Fresh blocked discovery records must then name that final SHA. No behavioral pass transfers between freezes.
