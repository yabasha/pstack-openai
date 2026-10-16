# Optional Wiki export

Repository documentation remains canonical. The exporter derives Wiki pages and copies their linked local support files. It includes all 51 skill pages, the 24 principles within that catalog, both host setup guides, workflows, troubleshooting, maintenance, compatibility and a Home page. Each Markdown page records its source path, package version and actual local package commit. Uncommitted documentation changes are included, so review the source tree before exporting a release snapshot.

Create an explicitly task-owned empty directory under `/Users/digital-hawk/Herd`, outside the package source tree. Run the exporter from the package root through Bun:

```sh
bun --no-install -e 'const p=Bun.spawnSync(["python3","-B","tools/export_wiki.py","--root",".","--output","/Users/digital-hawk/Herd/my-owned-wiki-export"],{stdout:"inherit",stderr:"inherit"});process.exit(p.exitCode)'
```

The destination must already exist and be empty. The exporter refuses symlinks, overlapping source trees and overwrites. It does not delete existing content. Local Markdown links become flat Wiki page names; anchors, images and external URLs retain their targets. Linked support files accompany the pages. Code examples remain literal. Missing local documentation links stop the export before it writes files. Directory links become generated indexes. Missing or placeholder links in adjacent support files appear as explicit unresolved source support targets; they do not become valid links or host evidence.

Inspect Home.md, both catalog overviews and the host guides in the exported directory. Run `tests.test_wiki_export` through Bun with Python's `-B` flag for structural export checks. These checks do not establish host behavior or whole-package parity.

Publication is a separate, optional user-authorized operation. Before requesting that authorization, review the exact remote repository, its visibility, Wiki availability and the desired exported content. Check whether the private repository supports a Wiki rather than assuming it does. Review linked support files for publication suitability. Neither the exporter nor these instructions enable a Wiki, invoke GitHub, create a remote or push content.
