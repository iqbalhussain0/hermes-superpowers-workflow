---
name: verification-before-completion
description: Use for final evidence reports after complex work.
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [verification, evidence, completion, testing]
    related_skills: [receiving-code-review]
---

# Verification Before Completion

## Purpose

Produce an evidence-backed final report for complex, multi-claim work — deployments, recovery events, security-boundary changes, multi-task implementations. Do not load for every ordinary "done"; a single focused check that already ran fresh is its own evidence.

## Iron law

Do not make a completion, correctness, deployment, or success claim without fresh evidence appropriate to that claim.

## Gate

1. Identify the exact claim.
2. Identify the command, observation, or user-visible result that proves it.
3. Run the freshest practical check with `set -o pipefail` where pipes are used, and retain the full output.
4. Read the complete output and the real exit status — the producer's status, not the last command in a pipeline.
5. Compare the result against the actual requirement.
6. Report PASS / FAIL / BLOCKED / UNVERIFIED per claim.

Never accept tailed pipeline output as completion evidence. The user may explicitly skip a check; report it as UNVERIFIED rather than claiming success.

## Claim-to-evidence

- Tests pass: full fresh test output and the test command's exit status.
- Build works: full fresh build output and exit status.
- Bug fixed: original symptom or regression test passes.
- Agent completed: the claimed artifact exists, its diff was inspected, and its checks were re-run independently.
- Deployment works: deployed state, service health, and a functional probe.
- Firewall exposure closed: effective rules from the authoritative source, plus a probe from an external vantage point, plus an explicit list of what was not probed. Never call a firewall "safe"; state exactly what was verified and from where.
- Recovery works: requires an exercised recovery test. Reviewing a recovery document or config proves only "recovery procedure reviewed." If recovery was not exercised, the status is UNVERIFIED.
- Requirements met: checklist mapped to the approved requirements, one evidence line each.

## Rules

- Older output provides background; it is not fresh proof.
- A changed file is not proof that the change works.
- A worker's report is not proof that its artifact exists.
- A passing test is not proof that deployment or external behavior works.
- A partial check proves only the checked portion.
- Never fabricate output, counts, URLs, or service state.

## Completion criteria

Use the [verification report template](templates/verification-report.md) when the work has multiple claims. The report includes the evidence used, its scope, and any remaining gaps, and concludes VERIFIED / PARTIALLY VERIFIED / NOT VERIFIED with the evidence boundary stated.
