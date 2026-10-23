# Automatic workflow documentation sync

Edit `docs/workflows/examples.json`. Push the change to `main` to trigger **Sync workflow documentation**. Pull requests check that generated files match the source; run `bun tools/render_workflow_examples.mjs` locally before opening one.

The Action uses Bun to generate the workflow section in `README.md` and `docs/workflows/site-feed.json`. It commits only those two generated files when they change. The feed contains the matching README and workflows in one response, with a content digest. It needs no manually configured secret and uses the repository's short-lived Actions token. Generated commits do not start another push run.

The existing public site loads the feed from `raw.githubusercontent.com` on page load, every five minutes while visible, and when a visitor returns to the tab. GitHub's cache can delay delivery. A visitor does not need to reload after a successful background refresh. Open workflow panels remain open. Copy controls use the refreshed prompts.

If GitHub cannot be reached or the feed is invalid, the site keeps its last loaded content and indicates that the latest update could not be checked. A new visitor always receives the published static snapshot before the feed loads. No account, private repository access, or Sites deployment credential is involved.

This automation updates the workflow section and embedded README. Package inventory, compatibility claims, branding, policies, and site code still require a reviewed site build and publication. It does not rebuild the plugin, change its version, modify the directory submission candidate, or update host verification records.

## Check or recover

1. Open [workflow runs](https://github.com/yabasha/pstack-openai/actions/workflows/sync-workflows.yml). A successful run establishes generation and, when needed, a successful push. Check the live site separately.
2. Run `bun tools/render_workflow_examples.mjs --check` to check README and feed drift locally.
3. If a run fails because `main` advanced, rerun the latest workflow. It checks out the current `main`; it never force-pushes or retries over concurrent changes.
4. If repository rules block bot pushes, retain those rules and report the failure. Do not bypass them. Regenerate the files locally and submit them through the required review process.
5. Use **Run workflow** to regenerate after recovery. A no-change run makes no commit.

The public feed is [docs/workflows/site-feed.json](https://raw.githubusercontent.com/yabasha/pstack-openai/main/docs/workflows/site-feed.json). To change a workflow, edit the source JSON rather than the generated feed or README block.
