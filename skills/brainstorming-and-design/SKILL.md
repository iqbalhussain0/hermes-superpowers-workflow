---
name: brainstorming-and-design
description: Use when architecture tradeoffs need user agreement.
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [brainstorming, design, requirements, specification]
    related_skills: [superpowers-workflow]
---

# Brainstorming and Design

## Purpose

Turn an idea into an agreed scope, design, and acceptance criteria when architecture tradeoffs need the user's agreement before implementation.

Do not load for:

- One-file fixes, typos, or config tweaks with an obvious correct shape.
- Feasibility experiments (route those to the official `spike` skill).
- Read-only research questions (answer them; no design ceremony).

## Plan-only requests

If the user asked for a plan instead of execution, do not use this skill's artifacts: load the official `plan` skill, write the plan to `.hermes/plans/`, and stop — that skill forbids same-turn execution. Do not write `docs/specs/` on a plan-only turn.

## Bounded change

For a limited modification to an existing flow:

1. Inspect the current flow, tests, and recent changes.
2. Present the intended behavior, affected files or surfaces, risks, and acceptance checks in chat.
3. Record any user override of recommended ceremony.
4. Proceed through the selected implementation and verification path.

No written specification or plan document is required unless the user wants one.

## Architectural change

For new subsystems, public interfaces, major refactors, or multiple interacting components:

1. Understand purpose, constraints, success criteria, and non-goals.
2. Present two or three approaches with tradeoffs and a recommendation.
3. Present the design in reviewable sections.
4. Record the approved design in `docs/specs/YYYY-MM-DD--<slug>.md` using the [design spec template](templates/design-spec.md).
5. Self-review for contradictions, missing requirements, undefined interfaces, and scope gaps.
6. If the user wants execution to continue in this turn, write the [implementation plan](templates/implementation-plan.md) to `.hermes/workflows/<plan-id>/plan.md` and proceed. If the user wants only a plan, see Plan-only requests above.

## Approval separation

Design approval, execution direction, operational authorization, and integration authorization are distinct. Design approval never silently authorizes deployment, publication, credential changes, commits, or unrelated cleanup. Authorization semantics are defined by `superpowers-workflow`.

## Completion criteria

- Scope, non-goals, acceptance checks, and risks are clear at the depth the path warrants.
- User overrides are recorded and honored.
- Required authorization and user-only prerequisites are identified.
- The next execution artifact exists *and has its required sections filled* when the selected path requires one — an empty file at the right path does not count.
