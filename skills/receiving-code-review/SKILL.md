---
name: receiving-code-review
description: Use when evaluating and responding to code-review findings.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [code-review, feedback, verification, fixes]
    related_skills: [verification-before-completion, subagent-driven-development]
---

# Receiving Code Review

## Purpose

Handle review feedback as technical input, not as an automatic command and not as a status signal.

## Process

1. Read each finding in full.
2. Map it to the approved requirements, code, test, or security property.
3. Reproduce or inspect the claimed issue where practical.
4. Classify it as blocking, important, minor, invalid, or outside scope.
5. Accept the finding and make the smallest scoped fix, or record a reasoned disposition.
6. Run the focused regression test and relevant broader checks.
7. Request or perform a focused re-review of changed areas.
8. Record the finding, evidence, disposition, and any user override.

Do not dismiss a finding because the implementation is already complete. Do not implement unrelated cleanup during a review fix.

## Security and authorization

Security, credential, authorization, data-loss, recovery, and privilege findings are blocking unless an authorized policy owner explicitly accepts the risk. A workflow preference or user desire for speed does not erase a higher-priority safety constraint.

## Disagreement

When a finding conflicts with the specification or another review:

- State the conflict.
- Gather the smallest decisive evidence.
- Ask the user only when the decision changes scope, risk, or external behavior and cannot be resolved from the approved requirements.
- Record the coordinator ruling and its cost if wrong.

## Completion criteria

- Every finding has evidence and a disposition.
- Fixes are scoped to accepted findings.
- Focused re-verification ran after fixes.
- Blocking findings are closed or explicitly escalated.
