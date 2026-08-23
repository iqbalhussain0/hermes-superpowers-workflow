---
name: using-git-worktrees
description: Use when repository work needs an extra isolated checkout.
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [git, worktree, isolation, branches]
    related_skills: [finishing-development-branch]
---

# Using Git Worktrees

## Purpose

Create or verify an isolated checkout for in-session work that needs its own working tree — parallel subagent edits, long-running changes, or work that must not touch the current checkout.

Session-level isolation is already covered by spawning Hermes with `hermes -w`, which creates its own worktree and `hermes/<hash>` branch. This skill covers *additional* checkouts inside a session, not the session default.

## Capture provenance before any mutation

```bash
REPO_ROOT=$(git rev-parse --show-toplevel)
BASE_BRANCH=$(git branch --show-current || echo DETACHED)
BASE_COMMIT=$(git rev-parse HEAD)
git worktree list --porcelain
git status --short
```

Record these in the plan or ledger. If HEAD is detached, the intended base branch is ambiguous, the branch name already exists, or the tree is dirty in a way the task depends on, resolve that with the user before creating anything.

## Check existing isolation

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" && pwd -P)
```

If `GIT_DIR` differs from `GIT_COMMON`, this checkout is already a linked worktree — say so and record it. That does not block creating *sibling* worktrees for parallel work; create those from the common git directory with an explicit base commit.

## Create an extra worktree

Only when isolation was selected (by recommendation plus user direction, or by explicit request):

1. Choose a location — a user-specified path, an existing `.worktrees/` or `worktrees/` directory, or a path outside the repository.
2. If the parent is outside the repository, no ignore check applies. If it is inside, create it first, then verify the exact selected parent path is ignored:

```bash
mkdir -p "$WORKTREE_PARENT"
git check-ignore -q -- "$WORKTREE_PARENT"
```

If it is not ignored, select an external location, or — only with explicit current-user direction — add that exact repo-relative path to `.gitignore` and verify again.

3. Create with an explicit start point:

```bash
git worktree add -b "$BRANCH" "$WORKTREE_PATH" "$BASE_COMMIT"
```

4. Follow repository setup instructions before installing dependencies; do not mutate lockfiles outside scope.
5. Run a baseline test or record that none exists.

## Completion criteria

- Provenance was captured before mutation.
- Existing isolation was detected, not assumed.
- The selected parent path itself is ignored or external.
- The worktree records base commit and branch.
- Baseline state is known or explicitly documented.
- Cleanup or retention follows the user's integration decision in `finishing-development-branch`.
