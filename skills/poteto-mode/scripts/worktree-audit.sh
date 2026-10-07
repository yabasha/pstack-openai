#!/usr/bin/env bash
# Read-only audit. Explicit local base and optional user-scoped JSON exports.
set -euo pipefail
exec python3 -B "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/worktree-audit.py" "$@"
