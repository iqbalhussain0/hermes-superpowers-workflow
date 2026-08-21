---
name: subagent-driven-development
description: Use for multi-task plans with bounded independent work.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [delegation, implementation, subagents, review, workflow]
    related_skills: [superpowers-workflow, verification-before-completion, receiving-code-review]
---

# Subagent-Driven Development

## Overview

Execute an approved implementation plan by routing bounded, independently verifiable tasks to fresh worker contexts, then reviewing and verifying each result before advancing. This skill is a workflow option, not a mandatory ceremony for every change.

The coordinator owns decomposition, user communication, integration, authorization boundaries, and final verification. Workers own only their explicitly bounded task.

## When to Use

Use when:

- An approved plan has multiple implementation tasks.
- Tasks have stable interfaces and can be tested independently.
- A fresh context would reduce implementation or review errors.
- The user requests delegated or multi-agent execution.

Prefer inline execution when:

- The change is tiny or tightly coupled.
- Investigation results will continually change the next task.
- Live operational state must remain with one coordinator.
- The user explicitly directs inline work or a shorter workflow.

A strong workflow recommendation may be overridden by the user's explicit direction unless a higher-priority safety, authorization, legal, or security constraint applies.

## Preconditions

Before dispatching a worker:

1. Confirm the task has an approved scope or the user's explicit instruction to proceed.
2. Read the relevant plan and acceptance criteria.
3. Confirm the task is independently verifiable.
4. Identify the exact files, interfaces, tests, and prohibited side effects.
5. Establish a clean or documented baseline.
6. Use an isolated worktree or directory when parallel edits could conflict, unless the user explicitly chooses otherwise.

If the plan is missing, ambiguous, or broken enough that implementation would be guesswork, stop and report the blocker. Do not invent requirements.

## Worker brief

Every worker receives a self-contained brief containing:

- Objective
- Relevant context
- Exact scope
- Files it may create or modify
- Interfaces it must preserve
- Required tests and commands
- Prohibited side effects
- Whether it may commit
- The evidence the coordinator requires

Do not give a worker unrelated credentials, broad root access, or authority outside its task.

## Per-task loop

For each task:

1. Dispatch one bounded worker when delegation is appropriate.
2. Require the applicable development discipline, normally TDD for behavioral code.
3. Inspect the worker's claimed files and diff independently.
4. Run focused tests and checks yourself or through an independent reviewer.
5. Review specification compliance and code quality/security as separate logical gates.
6. If findings exist, send only the findings back for a scoped fix.
7. Re-run the affected verification and perform a focused re-review.
8. Record the task result, evidence, findings, and any ruling before advancing.

Never treat a worker's success message as proof that the task is complete.

## Integrated review

After all tasks complete:

1. Inspect the complete diff against the approved requirements.
2. Check cross-task interfaces and integration behavior.
3. Run the broadest practical test suite.
4. Run an independent final review for security, correctness, scope, and regressions.
5. Resolve or explicitly record every finding before branch finishing.

Per-task approval is not sufficient for a whole-change completion claim.

## Progress and recovery

For multi-task work, maintain a plan-specific ledger containing:

- Plan or specification identity
- Current task
- Completed tasks and commits
- Focused and broad verification results
- Review findings and dispositions
- Fix-round count
- Coordinator rulings
- Blocked prerequisites
- Cleanup state

On resume or after context compaction, reconcile the ledger against Git, files, and live runtime state. The ledger records prior belief; current probes establish current truth.

## Completion criteria

This skill's execution is complete only when:

- Every in-scope task is met, explicitly excluded, or blocked.
- The complete diff has been inspected.
- Focused and broad verification has fresh evidence.
- Final integrated review is complete or explicitly waived by the user where policy permits.
- Required documentation and ledger entries are updated.
- Any remaining uncertainty is reported plainly.

## Common pitfalls

- Dispatching a worker for a task with no stable boundary.
- Letting workers edit overlapping files without isolation.
- Assuming a worker's report proves its changes landed.
- Reviewing each task but never reviewing the integrated diff.
- Resuming from a ledger without checking Git or runtime state.
- Treating this workflow's recommendations as higher authority than an explicit user override.

## Verification checklist

- [ ] Worker scope and prohibited side effects were explicit.
- [ ] Worker output and diff were independently inspected.
- [ ] Focused verification ran for each task.
- [ ] Review findings were fixed or dispositioned.
- [ ] Final integrated diff was reviewed.
- [ ] Broad verification ran at an appropriate scope.
- [ ] Ledger state matches current repository/runtime state.
- [ ] Completion claims are backed by fresh evidence.
