---
name: finishing-development-branch
description: Use when choosing merge, PR, keep, or discard for finished work.
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [git, branch, merge, pull-request, cleanup]
    related_skills: [verification-before-completion, using-git-worktrees]
---

# Finishing a Development Branch

## Purpose

Decide and execute the disposition of finished repository work without silently merging, committing, publishing, deleting, or discarding it.

## Final checks

Run whatever checks are still missing before presenting dispositions:

1. Focused and broad tests, with `set -o pipefail` and full retained output.
2. Inspect the complete diff (`git diff`, not `--stat` alone) and `git status`.
3. Secret scan: no credentials, tokens, private endpoints, or sensitive output in the change or its workflow artifacts.
4. Confirm base branch and commit provenance.
5. Inspect the review evidence that already exists. If review was skipped or never selected, mark review UNVERIFIED — do not start a new review pipeline from here.

If verification already exists or the user explicitly skipped remaining checks, present dispositions immediately and mark skipped claims UNVERIFIED — do not re-run gates the user waived.

## Integration choices

Present the available disposition in plain text:

1. Merge into the base branch.
2. Open or update a pull request.
3. Keep the branch and worktree.
4. Discard the branch and worktree.

Follow the user's explicit choice. **Commit, merge, push, publish, and discard are each separately authorized git mutations** — an earlier "go ahead" on implementation is not commit or push authority. Ask for the specific action if it was not already directed.

## Cleanup

Only after the disposition is known:

- Remove the worktree if the user selected cleanup.
- Verify the branch and worktree are gone when deletion was requested.
- Preserve rollback or review artifacts when required.
- Do not delete a branch containing unmerged work without explicit authorization.

## Completion criteria

- Final requirements and verification evidence are recorded.
- The complete diff and branch provenance were inspected with the actual commands, whose results are retained.
- The integration or retention choice is explicit.
- Each commit, merge, push, publication, or deletion was separately authorized.
- Cleanup matches the selected disposition.
