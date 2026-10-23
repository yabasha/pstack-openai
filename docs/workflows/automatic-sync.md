# Automatic repository documentation sync

Edit `docs/workflows/examples.json`. Push the change to `main` to trigger **Sync repository documentation**. Pull requests check that generated files match the source; run `bun tools/render_workflow_examples.mjs` locally before opening one.

The Action uses Bun to generate the workflow section in `README.md`, the backward-compatible workflow feed, and `docs/site/content.json`. It commits only those three generated files when they change. The repository feed contains the matching README, workflows, skill catalog and full instructions, all principles, manifest versions and package counts, current release record, compatibility guidance, host matrix, verification inventory statuses, and license in one response with a content digest. It needs no manually configured secret and uses the repository's short-lived Actions token. Generated commits do not start another push run.

The existing public site loads the feed from `raw.githubusercontent.com` on page load, every five minutes while visible, and when a visitor returns to the tab. GitHub's cache can delay delivery. A visitor does not need to reload after a successful background refresh. Open workflow panels remain open. Copy controls use the refreshed prompts.

If GitHub cannot be reached or the feed is invalid, the site keeps its last loaded content and indicates that the latest update could not be checked. A new visitor always receives the published static snapshot before the feed loads. No account, private repository access, or Sites deployment credential is involved.

Changes to the manifest, skill files and playbooks, catalog, release records, compatibility documents, host matrix, pinned upstream metadata, verification inventory, README, and license trigger generation. New skills without a curated catalog entry use their frontmatter description and link to their source; removed skills disappear from the site. A workflow that refers to a removed skill blocks generation until its source is corrected.

The site updates its workflow examples, README, complete skill directory and instructions, all principles, example prompts, version details, current release record, compatibility documentation, inventory status table, package counts, metadata description, and license. Search text, filters, selected skill example, and open panels survive refresh. A version without a matching release record displays that absence instead of borrowing another version's results. Inventory status counts describe source entries, not workflow passes.

Branding, design, publisher attribution, support and legal-policy wording, and site code still require a reviewed site build and publication. It does not rebuild the plugin, change its version, modify the directory submission candidate, or update host verification records.

## Check or recover

1. Open [workflow runs](https://github.com/yabasha/pstack-openai/actions/workflows/sync-workflows.yml). A successful run establishes generation and, when needed, a successful push. Check the live site separately.
2. Run `bun tools/render_workflow_examples.mjs --check` to check README and feed drift locally.
3. If a run fails because `main` advanced, rerun the latest workflow. It checks out the current `main`; it never force-pushes or retries over concurrent changes.
4. If repository rules block bot pushes, retain those rules and report the failure. Do not bypass them. Regenerate the files locally and submit them through the required review process.
5. Use **Run workflow** to regenerate after recovery. A no-change run makes no commit.

The public repository feed is [docs/site/content.json](https://raw.githubusercontent.com/yabasha/pstack-openai/main/docs/site/content.json). The original `docs/workflows/site-feed.json` remains a generated compatibility feed for older site clients. To change a workflow, edit the source JSON rather than the generated feed or README block.
