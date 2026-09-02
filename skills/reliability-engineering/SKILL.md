---
name: reliability-engineering
description: Use when an agent workflow runs unattended, recurs, resumes, or can silently produce bad results.
version: 0.3.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [reliability, unattended, state, checkpoints, idempotency, regression]
    related_skills: [superpowers-workflow, verification-before-completion]
---

# Reliability Engineering for Agent Workflows

## Overview

Make recurring and unattended agent workflows observable, resumable, idempotent, and resistant to silent corruption. This skill adds reliability controls; it does not replace domain procedures, authorization gates, or final verification.

## When to Use

Load when a workflow is scheduled, unattended, long-running, resumable, externally visible, stateful, or expensive enough that restarting from zero is undesirable.

Do not load for simple read-only lookups or a one-off edit with no durable state and no recurring execution.

## Core rules

1. **Process success is not result success.** Require both execution-health checks and result-health checks. A zero exit code alone never proves success.
2. **Keep deterministic control flow in code or configuration.** Use code for hashes, schemas, dates, deduplication, retries, permissions, thresholds, routing, and state transitions. Use the model for interpretation, synthesis, drafting, and genuinely ambiguous decisions.
3. **Make repeated runs idempotent where possible.** Derive a stable key from canonical inputs, task identity, operation, and target. Check provider-supported idempotency, locks, compare-and-swap/version checks, or a transactional outbox before a side effect. A key recorded after an external call does not guarantee exactly-once execution; reconcile the external system after crashes.
4. **Monitor before invoking the agent.** Normalize and hash upstream input; exit silently when unchanged only if freshness and heartbeat checks also pass. Invoke the model only when a meaningful change or scheduled action exists. Use a script-only watchdog when no interpretation is needed.
5. **Persist state and checkpoints.** Read machine-readable state before execution. Write atomically at meaningful recovery boundaries. Before resuming, reconcile persisted state with authoritative filesystem, API, or host state; never assume that a recorded checkpoint proves an external side effect completed.
6. **Compact errors before context injection.** Keep the full traceback outside context with a correlation ID, timestamp, command, exit status, and evidence path. Give the model a bounded classification containing component, safe retry status, attempt count, next action, escalation condition, and evidence path.
7. **Bound self-healing.** Retry only classified safe operations, with a finite attempt limit and a clear escalation path. Self-healing must not rotate credentials, install dependencies, change parsers, skip future work, or mutate configuration without the authorization required for that action.
8. **Promote autonomy gradually.** Use L1 report-only, L2 assist/stage-and-approve, and L3 bounded autonomous execution. L3 never removes action-specific authorization for privileged, destructive, financial, externally visible, credential, publication, or integration effects. Promotion requires exercised recovery, validator coverage, rollback/recovery, and alert rules.

## Required workflow record

Use `templates/workflow-state.yaml` as a starting point for machine-readable state and `templates/regression-case.json` for behavior tests. Do not create state for short tasks already fully represented by Hermes `todo`, session history, or the Superpowers ledger. At minimum record:

- workflow and schema version
- run ID and status
- current phase, last verified step, and next step
- normalized input hash
- attempts and retry decisions
- artifact paths and hashes
- pending side effects and idempotency records
- lock/lease owner where applicable
- approval status where applicable
- last classified error and evidence path
- update timestamp

State must contain no secrets, tokens, private keys, or raw sensitive payloads. Use `[REDACTED]` for credential fields and hashes or references for sensitive evidence.

## Validation contract

For every unattended run, define:

### Execution health

- Expected process/API phases completed
- No unhandled exception
- Expected artifacts exist
- Runtime and retry counts are within bounds

### Output validity

- Output validates against its schema
- Required fields and counts are present
- Input was not empty, stale, duplicated, or malformed

### Outcome plausibility

- Evidence supports the conclusion
- Freshness and provenance are within policy
- Independent checks or semantic spot checks pass where required
- No forbidden side effect occurred

If execution health, output validity, or outcome plausibility fails, report `BLOCKED` or `UNVERIFIED`, not success. A changed input hash proves only that input changed; it does not prove that the generated result is correct.

## Skill and model evolution

Treat skill text, model changes, routing changes, and tool changes as behavior changes.

Before promotion:

1. Snapshot the current version and record the reason for change.
2. Run the existing regression cases and retain the baseline.
3. Apply the change in an isolated branch/profile where practical.
4. Run the same cases plus new cases for the changed behavior.
5. Check forbidden behaviors, side-effect gates, secrets handling, and fallback behavior.
6. Compare old and new results; old failures must not return and old required successes must remain successful.
7. Promote only with explicit authorization; preserve a rollback version.

An independent second-model review is a critique or quality gate, not authority to modify files, approve side effects, or declare deployment success. Keep regression cases executable where possible: assert tool calls, denied calls, artifact contents, authorization behavior, side-effect absence, repeated-run behavior, and preservation of prior required successes. Lexical checks alone are policy smoke tests, not runtime evidence.

## Common anti-patterns

- “The command exited zero, so it worked.” → Validate the result contract.
- “The state is in the conversation.” → Persist state and checkpoints.
- “Retry everything.” → Classify retry safety and cap attempts.
- “The cron ran once.” → Use idempotency keys and durable completion records.
- “A recorded checkpoint proves the side effect happened.” → Reconcile against authoritative external state.
- “The model can decide every branch.” → Move deterministic decisions into code/configuration.
- “More agents means more reliability.” → Add a bounded outcome owner only when it removes a real failure mode.
- “A changed skill is automatically an improvement.” → Run regression comparisons before promotion.
- “Separate agent conversations isolate credentials.” → Treat filesystems, browsers, hosts, and credentials as shared trust boundaries.

## Verification checklist

- [ ] L1/L2/L3 maturity and scope are recorded.
- [ ] Deterministic gates do not depend on an LLM.
- [ ] Monitor-before-agent is used where upstream change detection is possible.
- [ ] Idempotency key and duplicate behavior are defined.
- [ ] State schema and checkpoint locations are defined.
- [ ] Execution health and result health both pass.
- [ ] Output validity and outcome plausibility are checked independently.
- [ ] Errors are classified and bounded before context injection.
- [ ] Retry, timeout, and escalation limits are tested.
- [ ] Resume logic reconciles checkpoints against authoritative external state.
- [ ] Regression cases cover normal, failure, duplicate, interruption, and unauthorized-side-effect paths.
- [ ] A fresh artifact, log, or test result supports every completion claim.
