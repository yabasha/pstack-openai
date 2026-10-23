# Publication preparation

Prepared on 2026-10-17, Asia/Amman. The repository and documentation site are public. The plugin remains a publication candidate; it has not been submitted to a plugin directory or published as an approved directory release.

## Package and listing

| Item | Status |
| --- | --- |
| Package identity | `pstack-openai`, version `0.1.3`; no upstream update included |
| Publisher | yabasha, confirmed by the maintainer; portal verification remains separate |
| Upstream attribution | Lauren Tan created the original pstack skills and principles; MIT notice retained |
| Listing copy | Display name, subtitle, long description, three starter prompts, and release notes in [plugin.json](../plugin.json) |
| Icon | Existing upstream MIT PNG, 512 × 512, reused for listing and composer; source hash retained in [UPSTREAM.md](../UPSTREAM.md) |
| Connections | Skills-only; no MCP server, app binding, authentication service, or lifecycle hooks |
| README | Usage examples, skill selection, setup links, compatibility results, and credits |
| Archive | Build with the command below; ZIP inventory and SHA-256 sidecars accompany each archive |
| Distribution | Free, with no plugin purchases; all available countries, explicitly confirmed by the maintainer |

The subtitle is 30 characters, including spaces. The existing icon has been visually inspected. No optional dark-mode branding has been added.

## Public listing pages and remaining portal steps

| Requirement | What remains |
| --- | --- |
| Public website | [Documentation site](https://pstack-openai.abloommink3.chatgpt.site), including the full README, 10 featured skill examples, six principle walkthroughs, and a searchable 51-entry directory. Verified anonymously after deployment. |
| Support page | [Support](https://pstack-openai.abloommink3.chatgpt.site/support/), with a public GitHub issue route and reporting guidance. Verified anonymously. |
| Privacy policy | [Privacy](https://pstack-openai.abloommink3.chatgpt.site/privacy/), describing the inspected static site and skills-only package, external host processing, and public support records. No publisher analytics, forms, accounts, or application database were added. Verified anonymously. |
| Terms | [Terms and license](https://pstack-openai.abloommink3.chatgpt.site/terms/), covering free use, host limits, permissions, attribution, and the retained MIT notice. Verified anonymously. |
| Country targeting | All available countries, represented by an explicit empty `publication.countries` array. |
| Payments or purchases | Free with no plugin purchases, confirmed by the maintainer; `review.commerce` is false. Host subscriptions and external services may charge separately. |
| Category | Select a supported category in the intended submission dashboard. |
| Publisher verification | Select or verify yabasha's intended publisher identity in the portal. |

All four URLs are written to `extensions.com.openai.interface.websiteURL`, `supportURL`, `privacyPolicyURL`, and `termsOfServiceURL`. Each returned HTTP 200 without credentials and contained its expected page content. The [repository](https://github.com/yabasha/pstack-openai) was changed from private to public at the maintainer's explicit request and verified without authentication.

The site was created and published with the requested public audience through Sites. Its source is maintained separately from the plugin package. Search, filters, example switching, and prompt copying were checked in the desktop browser. All four published pages were checked anonymously. A mobile viewport run was not performed.

This skills-only plugin needs no MCP review cases, recorded demo, or reviewer credentials. Do not add a server solely to satisfy an inapplicable requirement.

## Verification boundary

Before these preparation edits, the release report passed for frozen revision `51f209daf83cd97d64f89881d66533bb59dc57db`, version `0.1.3`. Each host had 105 validated cases, including discovery. Workflow-only counts are in the [controller report](releases/remaining-controller-report.md).

That result does not qualify the edited README, manifest, or new files. Preserve the historical evidence and [tested-package marker](parity/tested-package.json). Before release, choose the final release version, freeze the prepared files in a commit, and collect fresh discovery for that exact package. Follow the existing [identity contract](maintenance/rollback.md); do not rewrite historical evidence to claim a new test run.

The archive retains the repository's documentation, historical evidence, and development checks because the package links to them. It excludes Git data, local task state, operating-system files, dependency installations, and unrelated untracked files. The maintainer explicitly authorized making the repository public. Before that change, 4,457 reachable historical file versions were scanned for common API tokens and private keys, with no matches. Historical reports include local paths and captured execution text; this pattern scan is not a complete privacy audit. The site publishes only the README, catalog-derived examples, attribution, and project policy pages.

## Build and inspect

Run from the repository root with Bun, Python 3, and the system ZIP utilities available:

```sh
bun --no-install tools/package_release.mjs
```

To choose another output directory outside the repository:

```sh
bun --no-install tools/package_release.mjs /absolute/path/to/release-artifacts
```

The command validates package structure, listing lengths, prompts, icon dimensions, public-upload restrictions, and common credential patterns. It checks ZIP integrity and member names, rereads the archived manifest, and verifies every archived file against its recorded size and SHA-256. It writes a candidate ZIP, an inventory with per-file hashes, and a SHA-256 checksum outside the source directory. `submissionReady` remains false because packaging cannot complete the portal requirements or establish final host observations.

The preparation archive is local and reviewable. Upload, submission for review, and publication are separate actions requiring authorization. Portal verification, scans, and legal attestations remain the publisher's responsibility. Rebuild after every metadata or source change and inspect the exact archive intended for upload.

## References

- [Official plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Portable manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [README](../README.md), [changelog](../CHANGELOG.md), [notice](../NOTICE.md)
