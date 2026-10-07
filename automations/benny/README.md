# Benny

Benny provides two optional workflows for Slack issue reports. One triages each report. The other reproduces confirmed bugs, verifies existing fixes, and may prepare a bounded draft fix.

The twelve files are dormant setup and operational sources. All three nested skills remain outside the registered root skills and discovery.

## Set it up

1. Read [FOR_AGENTS.md](./FOR_AGENTS.md) directly and name the target repository.
2. With explicit copy authorization, merge this pack into the target at automations/benny/. Preserve destination-only files and review conflicts without overwriting local edits.
3. Verify shared pstack dependencies in the target execution context through current host capabilities. Missing project loading requires separate setup. Do not edit host settings or install a plugin automatically.
4. Keep user-owned configuration outside this pack, for example under .benny/. Adapt [configuration.example.yaml](./templates/configuration.example.yaml) and [feature-map.example.md](./skills/reproduce-and-fix-issues/references/feature-map.example.md). Secrets stay in a secret manager or environment.
5. The pack and referenced secret-free configuration must be committed in the target checkout before enabled execution. Committing needs authorization.
6. Prepare each draft and validate its supported trigger and connectors. Creating or updating an automation, sending test reports, ticket writes, and draft PR creation need separate action authorization. Use [readiness checks](../../docs/testing/benny-readiness.md) before enabling normal traffic.

Missing Benny setup blocks this optional pack, not the normal pstack skills. No host behavior has been tested by copying these files.
