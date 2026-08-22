# Implementation Plan: <title>

- **Spec:** <path to design spec, or "inline — bounded change">
- **Plan ID:** <slug used for .hermes/workflows/<plan-id>/progress.md>
- **Repository root:**
- **Base branch / starting commit:**
- **Worktree:** <path, or "in place per user direction">

## Global constraints

- Safety, authorization, credential, and policy constraints.
- User overrides and the tradeoffs they accepted.
- Prohibited side effects.

## Interface contracts

Interfaces, schemas, and invariants every task must preserve. Exact code only where the boundary demands it (security, schemas, migrations, commands, subtle algorithms).

## Tasks

Each task must be independently verifiable to be delegatable.

### Task 1: <name>

- **Scope:** exact files/surfaces
- **Behavior:** what changes, observable terms
- **Acceptance:** exact commands/checks and expected results
- **Depends on:** none / task N
- **Delegation:** fresh worker / inline / paired with task N (reason)

### Task 2: <name>

- **Scope:**
- **Behavior:**
- **Acceptance:**
- **Depends on:**
- **Delegation:**

## Verification plan

- Baseline check before changes:
- Focused check per task:
- Broad suite after integration:
- Runtime/deployment evidence required:

## Completion definition

All acceptance criteria pass with fresh evidence, or are explicitly excluded/blocked with the reason recorded in the ledger.
