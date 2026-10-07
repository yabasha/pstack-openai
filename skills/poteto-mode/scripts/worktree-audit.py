"""Read-only worktree audit adapted from Lauren Tan's MIT-licensed pstack.

CLI exports: history-map is an object keyed by complete worktree paths, with
Unix last-chat timestamps or null for explicitly known absent history.
pr-state is an array of {number, state, headRefName} records. Neither input
is discovered automatically. Null output fields mean unavailable evidence.
The first worktree is retained as the primary checkout and excluded, as upstream.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time


def _git(repo, *args):
    return subprocess.run(['git', '-C', str(repo), *args], capture_output=True,
                          env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0', 'GIT_NO_LAZY_FETCH': '1'})


def _text(result):
    return os.fsdecode(result.stdout).strip() if result.returncode == 0 else None


def _size(path):
    try:
        total = 0
        def fail(error):
            raise error
        for root, dirs, files in os.walk(path, followlinks=False, onerror=fail):
            for name in files:
                total += (Path(root) / name).lstat().st_size
        return total if path.is_dir() else None
    except OSError:
        return None


def audit_worktrees(repo: Path, base: str, history_map: dict | None, pr_state: list | None) -> list[dict]:
    if not base or base.startswith('-'):
        raise ValueError('base must be an explicit Git ref')
    if history_map is not None:
        if not isinstance(history_map, dict) or any(not isinstance(k, str) or (v is not None and (type(v) not in (int, float) or not 0 <= v <= time.time())) for k, v in history_map.items()):
            raise ValueError('history-map must map complete paths to past Unix timestamps or null')
    if pr_state is not None:
        if not isinstance(pr_state, list) or any(not isinstance(p, dict) or not isinstance(p.get('headRefName'), str) or type(p.get('number')) is not int or p['number'] <= 0 or p.get('state') not in ('OPEN', 'CLOSED', 'MERGED') for p in pr_state):
            raise ValueError('pr-state must contain number, state and headRefName records')
    listing = _git(repo, 'worktree', 'list', '--porcelain', '-z')
    if listing.returncode:
        raise ValueError('cannot list local worktrees: ' + os.fsdecode(listing.stderr).strip())
    records = []
    current = {}
    for token in os.fsdecode(listing.stdout).split('\0'):
        if not token:
            if current:
                records.append(current)
                current = {}
        else:
            key, _, value = token.partition(' ')
            current[key] = value
    if current:
        records.append(current)
    base_head = _text(_git(repo, 'rev-parse', '--verify', base + '^{commit}'))
    rows = []
    now = time.time()
    for record in records[1:]:
        path = Path(record['worktree'])
        head = _text(_git(path, 'rev-parse', '--verify', 'HEAD^{commit}'))
        branch = _text(_git(path, 'symbolic-ref', '--quiet', '--short', 'HEAD'))
        stamp = _text(_git(path, 'log', '-1', '--format=%ct', 'HEAD'))
        age = max(0, int((now - int(stamp)) // 86400)) if stamp and stamp.isdigit() else None
        merged = None
        if head and base_head:
            check = _git(repo, 'merge-base', '--is-ancestor', head, base_head)
            merged = True if check.returncode == 0 else False if check.returncode == 1 else None
        status = _git(path, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
        tracked = untracked = 0
        entries = status.stdout.split(b'\0')
        i = 0
        while i < len(entries):
            item = entries[i]
            if item:
                if item[:2] == b'??':
                    untracked += 1
                else:
                    tracked += 1
                    if b'R' in item[:2] or b'C' in item[:2]:
                        i += 1
            i += 1
        dirty = None if status.returncode else f'wip:{tracked}' if tracked else f'scratch:{untracked}' if untracked else 'clean'
        remote = None
        if head and branch is None:
            remote = 'detached'
        elif branch and head:
            # Use the configured local tracking ref, never assume origin.
            upstream = _text(_git(path, 'rev-parse', '--verify', '@{upstream}^{commit}'))
            if upstream:
                ahead = _text(_git(path, 'rev-list', '--count', upstream + '..' + head))
                remote = 'pushed' if upstream == head else 'ahead' + ahead if ahead else None
            else:
                remote = 'no-remote'
        matches = None if pr_state is None or branch is None else [p for p in pr_state if p['headRefName'] == branch]
        last = history_map.get(str(path)) if history_map is not None else None
        history_known = history_map is not None and str(path) in history_map
        recent = last is not None and (now - last) / 86400 <= 4
        size = _size(path)
        if dirty is not None and dirty != 'clean':
            bucket = 'hold-wip'
        elif matches and any(p['state'] == 'OPEN' for p in matches):
            bucket = 'hold-open-pr'
        elif dirty is None or merged is None or matches is None or not history_known or size is None or age is None or remote is None:
            bucket = 'hold-unknown'
        elif recent:
            bucket = 'verify-recent-chat'
        elif merged or any(p['state'] == 'MERGED' for p in matches):
            bucket = 'review-merged'
        else:
            bucket = 'review'
        rows.append(dict(size=size, age=age, merged=merged, dirty=dirty, remote=remote,
                         pr=matches, last_chat=last, bucket=bucket, worktree=str(path),
                         head=head, branch=branch, tracked_changes=tracked if dirty is not None else None,
                         untracked_changes=untracked if dirty is not None else None,
                         history_known=history_known, base=base, base_head=base_head))
    return sorted(rows, key=lambda row: row['size'] if row['size'] is not None else -1, reverse=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--base', required=True)
    parser.add_argument('--history-map', type=Path)
    parser.add_argument('--pr-state', type=Path)
    args = parser.parse_args()
    try:
        history = json.loads(args.history_map.read_text()) if args.history_map else None
        prs = json.loads(args.pr_state.read_text()) if args.pr_state else None
        print(json.dumps(audit_worktrees(args.repo, args.base, history, prs), ensure_ascii=True))
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
