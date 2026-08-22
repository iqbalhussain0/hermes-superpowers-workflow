# Execution Ledger

Use one ledger per plan or multi-task change at:

```text
.hermes/workflows/<plan-id>/progress.md
```

The ledger records coordinator state and evidence. It is not authoritative over Git, filesystem, services, or live infrastructure.

## Identity

- Plan/spec path:
- Plan/spec digest:
- Repository root:
- Base branch:
- Starting commit:
- Worktree path:
- Created at:
- Coordinator:

## Scope

- Objective:
- In scope:
- Explicit non-goals:
- User workflow choices or overrides:
- Required approvals:
- Prohibited side effects:

## Task state

| Task | Owner | Status | Scope | Commit/range | Focused evidence | Review disposition |
|---|---|---|---|---|---|---|
|  |  | pending / active / complete / blocked |  |  |  |  |

## Evidence

- Baseline command and result:
- Focused verification commands and results:
- Broad verification command and result:
- Final integrated review:
- Runtime or deployment checks:
- Recovery-path checks:

## Findings and rulings

- Finding:
- Evidence:
- Disposition:
- Fix round:
- Coordinator ruling:

## Reconciliation on resume

Before continuing after compaction, interruption, or handoff, record fresh observations:

- `git status`:
- Current branch and commit:
- Worktree list:
- Relevant filesystem state:
- Relevant service/runtime state:
- Differences from ledger:
- Corrected ledger entries:

## Completion

- All in-scope tasks complete, explicitly excluded, or blocked:
- Complete diff inspected:
- Fresh verification complete:
- Remaining unverified claims:
- Integration choice:
- Cleanup state:
- Documentation updated:
- Completion date:
