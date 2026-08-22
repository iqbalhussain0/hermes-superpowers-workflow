---
name: verification-before-completion
description: Use before claiming work is complete, fixed, or verified.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [verification, evidence, completion, testing]
    related_skills: [superpowers-workflow, receiving-code-review]
---

# Verification Before Completion

## Iron law

Do not make a completion, correctness, deployment, or success claim without fresh evidence appropriate to that claim.

This is an evidence requirement, not a demand for a particular ceremony. The user may explicitly choose not to run an optional check; report the result as unverified rather than claiming success.

## Gate

1. Identify the exact claim.
2. Identify the command, observation, or user-visible result that proves it.
3. Run the freshest practical check.
4. Read the complete output and exit status.
5. Compare the result against the actual requirement.
6. Report passed, failed, skipped, blocked, and unverified conditions separately.

## Claim-to-evidence examples

- Tests pass: fresh test output and exit status.
- Build works: fresh build output and exit status.
- Bug fixed: original symptom or regression test passes.
- Agent completed: inspect the diff and independently verify the result.
- Deployment works: deployed state, service health, and functional probe.
- Firewall is safe: effective rules plus an external-boundary probe.
- Recovery works: exercised recovery or explicitly recorded why it was not exercised.
- Requirements met: checklist mapped to the approved requirements.

## Rules

- Older output provides background; it is not fresh proof.
- A changed file is not proof that the change works.
- A worker's report is not proof that its artifact exists.
- A passing test is not proof that deployment or external behavior works.
- A partial check proves only the checked portion.
- Never fabricate output, counts, URLs, or service state.

## Completion criteria

A completion report includes the evidence used, its scope, and any remaining gaps. If a check cannot run, say exactly why and use `BLOCKED` or `UNVERIFIED` rather than substituting confidence.
