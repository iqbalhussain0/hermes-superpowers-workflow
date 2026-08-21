---
name: superpowers-workflow
description: Use when coordinating software or operational work across planning and verification.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [workflow, planning, delegation, verification, superpowers]
    related_skills: [subagent-driven-development]
---

# Superpowers Workflow for Hermes

## Purpose

Coordinate Superpowers-style development discipline with Hermes execution, security, authorization, model routing, and operational boundaries. This skill routes to focused skills; it does not replace TDD, debugging, planning, review, deployment, or security skills.

## Authority and user overrides

Make a strong recommendation about workflow, ceremony, risks, and tradeoffs. An explicit current user direction overrides workflow recommendations and ordinary ceremony. Follow the user's direction unless a higher-priority system, authorization, legal, or security constraint prevents it.

When the user overrides a recommendation:

1. State the consequence briefly.
2. Record the deviation in the plan or ledger when one exists.
3. Follow the user's direction.
4. Preserve applicable safety, authorization, credential, and evidence requirements.

Do not repeatedly ask the user to reaffirm an explicit override.

## Classify before acting

Use the [risk classification reference](references/risk-classification.md) to record mutation, privilege, reversibility, blast radius, recovery dependence, and visibility. Choose the lightest accurate profile. Hidden complexity upgrades the profile; user direction may choose a lighter workflow when policy permits.

### Read-only inquiry

Use for inspection, research, diagnosis, and reporting without mutation.

- Discover relevant skills.
- Gather evidence.
- Use systematic debugging when investigating a defect.
- Do not impose design or implementation ceremony.

### Spike

Use for feasibility questions and disposable probes.

- State the question and probe.
- Obtain approval before a mutating or externally visible probe.
- Keep artifacts disposable and clearly labeled.
- Report evidence and recommendation.
- Do not promote spike code directly to production.

### Bounded code change

Use for a limited modification to an existing flow.

- Inspect the current flow and tests.
- Present a short design and acceptance checks.
- Recommend TDD and isolation proportionate to risk.
- Follow the user's chosen execution path.
- Run focused verification and inspect the diff.

A formal specification and plan are not mandatory for every bounded change.

### Architectural or multi-task code

Use for new subsystems, public interfaces, major refactors, or several independently testable tasks.

- Explore alternatives.
- Present and record the design when useful.
- Create a detailed plan unless the user explicitly chooses a shorter path.
- Recommend a worktree and ledger.
- Use `subagent-driven-development` for independent tasks when appropriate.
- Perform per-task and final integrated review.
- Finish with fresh verification and branch handling.

### Operations and deployment

Classify separately by privilege, reversibility, blast radius, recovery dependence, and external visibility:

- Read-only diagnosis
- Reversible local change
- Service restart or deployment
- Privileged mutation
- Network or security-boundary change
- Destructive or irreversible action

Use operational preflight, staging, scoped authorization, rollback preparation, runtime verification, and recovery checks as applicable. Coding workflow ceremony does not replace operational safety.

## Canonical artifacts

- Bounded or implementation plans: `.hermes/plans/`
- Architectural specifications: `docs/specs/`
- Multi-task execution ledger: `.hermes/workflows/<plan-id>/progress.md`
- Operational records: the project's runbook or Obsidian operational note

A ledger is evidence of prior coordinator state, not current truth. On resume, reconcile it against Git, files, services, and live system probes.

## Required routing

Load and use the narrowest applicable Hermes skills:

- `plan` for detailed implementation plans
- `test-driven-development` for behavioral code when applicable
- `systematic-debugging` before fixing an unexplained defect
- `model-routed-delegation` when using different workers or models
- `subagent-driven-development` for independent plan tasks
- `requesting-code-review` for code-quality and security review
- Security, privileged-operation, deployment, remote-access, or domain skills for those tasks

Do not duplicate a skill's body in this router. If a referenced skill is unavailable, report it and use the closest verified alternative rather than inventing its behavior.

## Approval separation

Keep these distinct:

1. Intent approval: agreement with the design or requested change.
2. Execution direction: instruction to implement within scope.
3. Operational authorization: permission for a privileged or external side effect.
4. Integration authorization: permission to merge, push, publish, deploy, or discard.

An approved design does not authorize deployment. A request to implement does not authorize unrelated cleanup. An explicit user direction may combine ordinary workflow steps, but it does not silently expand scope.

## Completion gate

Before claiming completion:

1. Identify the exact evidence required by the claim.
2. Run the freshest practical verification.
3. Read the complete result and exit status.
4. Compare it with the actual requirement.
5. Report skipped, blocked, or unverifiable requirements plainly.

Never substitute a worker's report, a changed file, or a plausible explanation for evidence.

## Common pitfalls

- Applying an architectural workflow to a simple read-only request.
- Treating a strong recommendation as a mandatory gate after the user overrules it.
- Treating an explicit user direction as authorization for an unrelated side effect.
- Using a plan or ledger as a substitute for current system state.
- Delegating tightly coupled work to independent workers.
- Reviewing tasks individually without a final integrated review.
- Letting this router duplicate or contradict a domain-specific security skill.

## Verification checklist

- [ ] Work was classified accurately.
- [ ] The user's explicit workflow choices were followed.
- [ ] Higher-priority safety and authorization rules were preserved.
- [ ] Relevant domain skills were loaded.
- [ ] Artifacts and paths match the selected profile.
- [ ] Required review and verification evidence is fresh.
- [ ] Unverified or blocked requirements are reported.
