---
name: brainstorming-and-design
description: Use before designing a new feature or changing behavior.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [brainstorming, design, requirements, specification]
    related_skills: [superpowers-workflow]
---

# Brainstorming and Design

## Purpose

Turn an idea into an agreed scope, design, and acceptance criteria before implementation when the work would benefit from design discussion. This skill recommends a gate; an explicit user instruction may choose a shorter path unless a higher-priority safety, authorization, legal, or security constraint applies.

## Classify the request

- **Spike:** feasibility question; produce evidence and a recommendation, not production code.
- **Bounded:** an existing flow has a small, understood change; use a short in-chat design and acceptance checks.
- **Architectural:** new subsystem, public interface, major refactor, or multiple interacting components; use alternatives, a written specification, and then a detailed plan.
- **Operational:** classify privilege, reversibility, blast radius, recovery dependence, and external visibility separately.

When uncertain, recommend the heavier path and state why. If hidden complexity appears, announce the upgrade and revise the artifacts.

## Process

### Spike

1. State the feasibility question and proposed probe.
2. Identify any mutation, credential, cost, or external side effect.
3. Get approval for a mutating probe when required.
4. Investigate with disposable artifacts.
5. Report evidence, limitations, and recommendation.

### Bounded change

1. Inspect the existing flow, tests, and recent changes.
2. Present the intended behavior, files or surfaces affected, risks, and acceptance checks.
3. Record any user override of the recommended ceremony.
4. Proceed through the selected implementation and verification path.

Do not create a formal specification or plan document unless the scope warrants it or the user requests one.

### Architectural change

1. Understand purpose, constraints, success criteria, and non-goals.
2. Present two or three approaches with tradeoffs and a recommendation.
3. Present the design in reviewable sections.
4. Record the approved design in `docs/specs/YYYY-MM-DD--<slug>.md` when a written specification is useful.
5. Self-review for contradictions, missing requirements, undefined interfaces, and scope gaps.
6. Convert the approved design into `.hermes/plans/` unless the user explicitly chooses another execution path.

## Approval separation

Design approval, implementation direction, operational authorization, and integration authorization are separate concepts. Approval of a design never silently authorizes deployment, publication, credential changes, or unrelated cleanup.

## Completion criteria

- The task path is stated.
- Scope, non-goals, acceptance checks, and risks are clear at the appropriate depth.
- User overrides are recorded and honored.
- Required authorization and user-only prerequisites are identified.
- The next execution artifact exists when the selected path requires one.
