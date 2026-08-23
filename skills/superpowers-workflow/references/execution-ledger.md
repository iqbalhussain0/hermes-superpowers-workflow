# Execution Ledger

Use one ledger per long-running or cross-session change at:

```text
.hermes/workflows/<plan-id>/progress.md
```

The ledger exists for cross-session handoff, long-running operations, and audit. The Hermes `todo` tool is the live task list within a session; do not mirror every task state into the ledger. Ledger entries are timestamped historical observations. The ledger is never authoritative over Git, filesystem, services, or live infrastructure, and a ledger entry is never an authorization token.

## Sensitive data

Never store secrets, credential values, authentication codes, private keys, session tokens, or raw sensitive payloads. Redact command output before recording it. Record hashes, references, redacted excerpts, and verification outcomes. Run a secret scan before committing or publishing artifacts. Store sensitive operational evidence in the project's access-controlled runbook location, not in the repository ledger.

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
- User workflow choices or overrides (with accepted tradeoffs):
- Prohibited side effects:

## Authorization records

For each privileged, destructive, security-boundary, or externally visible action:

- Source/principal (authenticated chat session):
- Exact action and target:
- Issued at / expires:
- One-shot or reusable:
- Consumed / revoked state:
- Revalidation result after any resume:

A stale, expired, consumed, or scope-changed authorization must not be replayed.

## Task state (historical observations with timestamps)

| Task | Owner | Status (observed at) | Scope | Commit/range | Focused evidence | Review disposition |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Evidence

- Baseline command and result:
- Focused verification commands and results (full output retained, real exit status):
- Broad verification command and result:
- Final integrated review:
- Runtime or deployment checks:
- Recovery-path checks:

## Findings and rulings

- Finding:
- Evidence:
- Disposition (valid / invalid / out of scope; accepted / rejected / ESCALATED-ACCEPTED RISK):
- Fix round:
- Coordinator ruling:

## Reconciliation on resume

Before continuing after compaction, interruption, or handoff, record fresh observations and update `todo` from them, not the reverse:

- `git status`:
- Current branch and commit:
- Worktree list:
- Relevant filesystem state:
- Relevant service/runtime state:
- Differences from ledger:
- Authorization records revalidated:
- Corrected ledger entries:

## Completion

- State: COMPLETE / PARTIALLY COMPLETE / BLOCKED — a blocked requirement never satisfies completion
- Complete diff inspected:
- Fresh verification complete:
- Remaining unverified claims:
- Integration choice (separately authorized):
- Cleanup state:
- Documentation updated:
- Completion date:
