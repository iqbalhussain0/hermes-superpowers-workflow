---
name: finishing-development-branch
description: Use when finishing verified repository work and deciding branch disposition.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [git, branch, merge, pull-request, cleanup]
    related_skills: [verification-before-completion, using-git-worktrees]
---

# Finishing a Development Branch

## Purpose

Close verified repository work without silently merging, publishing, deleting, or discarding it.

## Final checks

Before presenting branch choices:

1. Run the applicable focused and broad tests.
2. Inspect the complete diff and status.
3. Confirm no secrets, credentials, temporary files, or unrelated changes are included.
4. Confirm the base branch and commit provenance.
5. Confirm final integrated review and unresolved findings.
6. Record the evidence in the workflow ledger.

Do not claim the branch is complete from a worker report or a clean-looking diff alone.

## Integration choices

Present the available disposition in plain text:

1. Merge into the base branch.
2. Open or update a pull request.
3. Keep the branch and worktree.
4. Discard the branch and worktree.

Follow the user's explicit choice. Do not merge, push, publish, or discard without the corresponding direction or previously scoped authorization.

## Cleanup

Only after the disposition is known:

- Remove a worktree if the user selected cleanup.
- Verify the branch and worktree are gone when deletion was requested.
- Preserve rollback or review artifacts when required.
- Do not delete a branch containing unmerged work without explicit authorization.

## Completion criteria

- Final requirements and verification evidence are recorded.
- Complete diff and branch provenance were inspected.
- Integration or retention choice is explicit.
- Any merge, push, publication, or deletion was separately authorized.
- Cleanup matches the selected disposition.
