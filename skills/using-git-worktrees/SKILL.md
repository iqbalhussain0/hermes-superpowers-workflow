---
name: using-git-worktrees
description: Use when repository work benefits from branch isolation.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [git, worktree, isolation, branches]
    related_skills: [finishing-development-branch, subagent-driven-development]
---

# Using Git Worktrees

## Purpose

Protect the current branch from implementation changes and parallel edits. Worktrees are the default recommendation for multi-file or delegated repository work, not an unconditional requirement. Follow an explicit user choice to work in place unless a higher-priority safety or authorization constraint prevents it.

## Detect isolation first

Run:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
git branch --show-current
git rev-parse --show-superproject-working-tree 2>/dev/null
```

If `GIT_DIR` differs from `GIT_COMMON` and the path is not a submodule, report the existing worktree and do not create another one.

## Create isolation

1. Check for a user-specified location.
2. Prefer an existing `.worktrees/` or `worktrees/` directory.
3. Verify the chosen directory is ignored:

```bash
git check-ignore -q .worktrees || git check-ignore -q worktrees
```

4. If the user authorized creation and no native worktree mechanism exists:

```bash
git worktree add <path> -b <branch-name>
```

5. Record repository root, base branch, starting commit, worktree path, and branch.
6. Follow repository instructions before installing dependencies.
7. Run a baseline test or explicitly record that no baseline exists.

Do not blindly run package installers or mutate lockfiles. Respect project instructions and the user's chosen scope.

## Completion criteria

- Isolation state was detected rather than assumed.
- Worktree location is ignored and recorded.
- Base commit and branch provenance are recorded.
- Baseline state is known or explicitly documented.
- Cleanup or retention remains under the user's integration decision.
