# Acceptance case contract

Each JSON file contains one case object or an array of complete case objects. IDs are unique across the registry. `schema.json` defines each object. Expected full, reduced, and blocked observations are nonempty strings. Source paths, requirements, and forbidden claims are nonempty arrays of nonempty strings.

`--scope <upstream-path>` selects inventory records by `upstreamPath` and individual case objects by membership in `sourcePaths`, including objects inside arrays. It checks destinations and references for that unit. An explicitly inventoried pending destination can be deferred in scoped mode. A scoped pass does not establish full-package acceptance or behavioral parity. Full-package validation rejects missing pending destinations.

Remnant dispositions identify an exact file hash, token, and line range. A reviewed binding explains the replacement API or runtime contract. A source-only explanation identifies a quoted example. Historical records preserve approved plan and spec text. Wildcard paths are invalid. Editing a reviewed file invalidates its hash-bound dispositions.
