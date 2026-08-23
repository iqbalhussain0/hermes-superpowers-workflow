---
name: superpowers-workflow
description: Use only when one task crosses two risk or lifecycle boundaries.
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [workflow, routing, risk, verification, superpowers]
    related_skills: [brainstorming-and-design, verification-before-completion]
---

# Superpowers Workflow for Hermes

## Purpose

Route work that crosses lifecycle or risk boundaries — for example a design task that becomes a privileged deployment — through the right focused skills in the right order. This skill only routes; it contains no procedures of its own beyond classification and authorization binding.

## When to use / when not to use

Load this skill when one task crosses at least two boundaries, such as design plus deployment, code plus privileged operations, or implementation plus publication.

Do not load for:

- A single-domain task already governed by one focused skill (plan-only turns, TDD, debugging, review, spike, deployment).
- Work that merely has multiple steps but one domain.
- Simple lookups, edits, or read-only questions.

## Authority and user overrides

Make a strong recommendation about workflow, ceremony, risks, and tradeoffs. An explicit current user direction overrides workflow recommendations and ordinary ceremony. Follow the user's direction unless a higher-priority system, authorization, legal, or security constraint prevents it.

When the user overrides a recommendation: state the consequence briefly, record the deviation in the plan or ledger when one exists, follow the direction, and preserve applicable safety, authorization, credential, and evidence requirements. Do not repeatedly ask for reaffirmation.

An explicit user skip of a ceremony means *do not load that skill* — never load it and then try to override its iron law.

## Classify on two axes

Use the [risk classification reference](references/risk-classification.md). Every task gets both:

1. **Work shape:** inquiry / empirical spike / bounded code / architectural code.
2. **Operational risk:** none / reversible configuration / deployment / privileged / security boundary / destructive.

Apply the *union* of the controls both axes demand. Never let one axis replace the other. When uncertain, choose the lightest accurate work shape, then add controls from the highest risk dimension.

## Conditional routing

These are independent gates: each fires only when its trigger is true, and several may fire on one task. An explicit user skip of a ceremony means the skill is not loaded. When an official skill is already loaded, follow it — do not add a second procedure that fights its rules; this package only narrows *when* each skill is loaded.

- **plan:** load only when the user asked for a plan instead of execution. The official `plan` skill forbids execution in the same turn. For an already-authorized implementation, use the package's implementation-plan template directly and do not load `plan`.
- **test-driven-development:** load for new behavioral production code unless the user explicitly skipped it.
- **systematic-debugging:** load only for an unexplained defect. For a read-only investigation, use its evidence-gathering discipline but do not create tests, harnesses, or instrumentation without execution direction covering that mutation.
- **spike:** route feasibility experiments to the official `spike` skill. This package adds only one constraint: a mutating or externally visible probe needs operational authorization.
- **subagent-driven-development (official):** load only when the user chose delegated multi-task execution. Apply the overlay below whenever it is loaded.
- **requesting-code-review:** load only when the user asked for a pre-commit review pass. Never run its commit step unless the user explicitly asked to commit, and never run `git add -A`. All evidence commands must use `set -o pipefail` and retain full output; tailed pipeline output is not evidence. Never start it from `finishing-development-branch` or `receiving-code-review`.
- **milestone-backed-execution:** do not load when this router governs completion. If it is already loaded, map its ACTIVE/BLOCKED/STALLED onto this package's states and do not maintain a second completion vocabulary.
- **receiving-code-review:** load when responding to actual review findings from a human or another agent.
- **model-routed-delegation:** load only when different models or runtimes are assigned to different slices of the work.
- **Domain skills** (security, deployment, remote access, Proxmox, etc.): load for their domains as usual.

### Official subagent-driven-development constraints

The official skill predates some current Hermes constraints. These are dispatch-side corrections, not an attempt to override its text:

- Workers cannot ask the user questions. The worker brief must contain every decision; the coordinator resolves ambiguity before dispatch.
- `delegate_task` accepts `goal`, `context`, and optionally `role`/`tasks` — there is no `toolsets` parameter.
- Workers may not commit, push, or create remotes. Git mutations belong to the coordinator and need explicit user direction.
- The coordinator independently verifies each claimed artifact and diff.

## Authorization binding

Approval labels in this package map to real controls:

- **Intent approval** and **execution direction:** the user's explicit statement in authenticated chat.
- **Git mutations** (commit, push, merge, publish, discard): explicit current user direction for that action. A plan, spec checkbox, or earlier general approval is not commit or push authority.
- **Operational authorization** (privileged, network, credential, security-boundary, destructive, externally visible): the host's privileged-operation grant path only — a scoped wrapper, a TOTP/lease, or a named installed approval bridge. If the host has no grant path for the action, fail closed and hand the exact command to the user. A chat "yes" is intent or ordinary execution direction; it is never operational authorization by itself.
- **Integration authorization:** explicit direction to merge, push, publish, deploy, or discard, given at integration time.

Risk acceptance comes only from the profile owner or configured approval principal — not from whoever happens to send a message in a shared chat.

Authorizations for privileged or destructive actions are recorded in the ledger with source, exact action and target, issued time, expiry, one-shot versus reusable, and consumed/revoked state. A ledger entry documents authorization; it is not an authorization token. After any interruption or resume, revalidate that the authorization still matches the current action and state before using it.

## Progress state

The Hermes `todo` tool is the live task list. The [execution ledger](references/execution-ledger.md) exists only for cross-session handoff, long-running operations, and audit needs — as timestamped historical observations that must be reconciled against Git, filesystem, and runtime state before reuse.

## Artifact data policy

Never store secrets, credential values, authentication codes, private keys, session tokens, or raw sensitive payloads in plans, specs, ledgers, or review records. Redact command output before recording it. Record hashes, references, redacted excerpts, and outcomes. Run a secret scan before committing or publishing workflow artifacts.

## Completion states

- **COMPLETE:** every in-scope required criterion passed with fresh evidence.
- **PARTIALLY COMPLETE:** the authorized requester reduced scope; remaining scope is explicitly deferred.
- **BLOCKED:** a required criterion cannot be verified or completed.

A blocked requirement never satisfies completion. Report UNVERIFIED for claims with no evidence gathered.

## Verification checklist

- [ ] Both classification axes recorded.
- [ ] Only triggered focused skills were loaded.
- [ ] User overrides honored by not loading skipped ceremonies.
- [ ] Every git mutation and operational action matched explicit current authorization.
- [ ] Evidence came from full-output commands with real exit status.
- [ ] Completion state uses COMPLETE / PARTIALLY COMPLETE / BLOCKED / UNVERIFIED.
