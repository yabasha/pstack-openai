# Personal customization boundary

Preserve the complete shared baseline before adding personal customizations. The accepted baseline remains pstack v0.15.30, port 0.2.3, recorded in [UPSTREAM.md](../../UPSTREAM.md). The unaccepted 0.2.4 compiler candidate tracks 580 source files and 58 canonical roots, with 57 runtime skills, 24 principles and 23 playbooks. One unrequested root is an inert relocated reference. The principles are part of the root skills and the playbooks are part of the support files; these counts do not describe additional files.

## Baseline gate

Personal customization begins only after every baseline inventory record has a reviewed disposition and dependency closure, and each host has evidence for supported behavior or an explicit block. Review the [inventory](../parity/inventory.json), [support map](../parity/support-map.md), [case registry](../parity/case-registry.json), [compatibility summary](../compatibility.md) and [host matrix](../testing/host-matrix.md) together.

The current candidate has no installed discovery or behavioral passes on either host. Its registry and source membership are recorded in the candidate metadata; every behavioral host status remains not-run. Case definitions, local package checks and isolated helper fixtures are not host observations. Both hosts remain unverified and undiscovered, so the baseline is not release-ready. An explicit blocked disposition records a limit; it does not establish support. A sequential reduced-pass never establishes independent workers.

Complete baseline accounting is required even when a useful reduced workflow exists. Release readiness is a separate evidence gate evaluated by the [release report CLI](../../tools/release_report.py). Keep blocked branches and separately required setup visible. A later final report must use actual observations and the frozen tested revision.

## Separate personal mode and provenance

This implementation generates no personal mode. Any later personal mode requires a separate request and review after the baseline gate. Keep its instructions and changelog separate from the shared baseline. Record the exact package version, frozen tested commit, canonical source pin, reviewed personal changes, owner, affected callers and validation evidence. Record unknown capabilities and blocked checks explicitly.

Personal instructions may narrow a workflow, but they do not grant installation, model selection, independent workers, integration access, external writes or recurring schedules. Confirm exposed operations and authorization for each action. Preserve the original baseline and its lineage so a personal change can be reviewed independently of an upstream change.

Upstream updates never own personal settings, modes or secrets. Do not put these paths into an update resolution as package-owned destinations. A destination-only personal file needs an explicit preservation reason in a rollback ownership document. Required inventory destinations, dependencies and update provenance remain package files and cannot be relabelled personal to avoid validation. Keep secrets and host settings outside the package write set.

## Update and acceptance boundary

Follow the implemented [upstream update workflow](upstream-updates.md) and [rollback procedure](rollback.md). The [update CLI](../../tools/sync_upstream.py) implements check, prepare, apply and rollback. It has no accept command.

| Stage | Actual operation and boundary |
| --- | --- |
| Check | After exact public-fetch permission, inspect an exact source SHA and write a new retained review bundle. Never execute fetched source code. |
| Prepare | Write exact-byte drafts where the adaptation permits them. Preserve immutable review artifacts and review every change, conflict, caller, rename, deletion and notice. Existing bundles are not overwritten. |
| Apply | Obtain explicit approval of the exact resolution digest and owned linked worktree. Apply reviewed package changes, write the apply receipt and invalidate affected observations. Apply does not advance the accepted baseline. |
| Validate | Check package links and schemas, run affected authorized helper checks and gather fresh affected host evidence at the frozen tested commit. Missing discovery, tools or permission remains blocked. |
| Separate acceptance | After evidence review and explicit acceptance authorization, record the strict hash-bound accepted-baseline receipt. Neither apply nor a successful structural check accepts a candidate. |
| Next update | Check and prepare bind the accepted receipt and its manifest and evidence digests. An unaccepted staged source pin or tampered receipt blocks another proposal. |

The accepted receipt identifies the source commit, exact manifest and evidence paths and hashes, and an ancestor package commit containing that manifest. Keep the original canonical manifest. The apply receipt records staging; it is not acceptance or a release claim. Git-admin owner markers assert worktree ownership and do not authenticate human approval.

## Recovery and frozen bytes

Retain failed candidates and their evidence as unaccepted. Rollback needs a separately authorized clean local snapshot commit, a locally available immutable ancestor release, exhaustive ownership and preservation classifications, and a reviewed assertion that no runtime-state migration is required. Preview the plan without a write approval flag. Approve its exact digest and worktree, then recompute before restoring bytes. Retain the resulting receipt outside the owned write set and review the diff before any separately authorized commit.

Rollback preserves current destination-only personal files classified in the ownership document. It does not restore installed host settings, external state or user data, and it does not install, reload, accept or release a package. Caught failures restore touched bytes; power loss, uncatchable termination, storage failure and hostile concurrent replacement require manual recovery from retained artifacts.

Freeze this document and README navigation with the operative package. Later handoff reports must preserve these bytes under the tested-package marker contract in the rollback procedure. If catalog regeneration or another operative edit requires a second freeze, record that revision and gather fresh discovery observations at its exact SHA. Behavioral passes never transfer automatically between freezes.
