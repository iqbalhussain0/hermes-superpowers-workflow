# Changelog

## [0.2.0] - 2026-08-22

### Changed

- Major revision after independent reviews from GPT-5.6 Sol and Grok 4.6.
- Narrowed skill descriptions and added explicit counter-triggers to prevent the router and design skills from acting as global interceptors.
- Routing is now conditional and exclusive: `plan` loads only for plan-only turns; TDD, debugging, review, and delegation load only when their triggers are true; explicit user skips mean the skill is not loaded.
- Added a compatibility overlay for the official `subagent-driven-development` skill (workers cannot ask questions; no `toolsets` parameter; workers do not commit).
- Operational authorization is bound to real Hermes controls: explicit authenticated-chat direction for git mutations, host grant paths for privileged and destructive actions, and one-shot/expiry/revalidation semantics in the ledger.
- Risk classification is now two independent axes (work shape × operational risk) with union-of-controls selection.
- Worktree procedures rewritten: provenance captured before mutation, explicit base commit, exact-path ignore checks, sibling-worktree handling, and `hermes -w` documented as the session-level default.
- Completion states are COMPLETE / PARTIALLY COMPLETE / BLOCKED; blocked requirements never satisfy completion.
- Verification claims split precisely (recovery exercised vs. procedure reviewed; firewall evidence scoped); pipeline evidence requires real exit status and full output.
- Review reception now gates scope-changing fixes behind user confirmation and defines authenticated risk acceptance.
- Branch finishing treats commit, merge, push, publish, and discard as separately authorized actions.
- Ledger demoted to cross-session/audit use; the `todo` tool remains live task state. Added sensitive-data policy for all artifacts.
- Removed duplicated spike procedures; spikes route to the official skill.
- Dropped the Windows platform claim where procedures are POSIX-only.

### Added

- Live behavioral scenario harness (`tests/run_scenarios.py`, `tests/scenarios.yaml`).
- Expanded contract tests locking review fixes in.

## [0.1.0] - 2026-08-21

### Added

- Initial Hermes-native workflow skills adapted from Superpowers.
- `superpowers-workflow` orchestrator with risk-sensitive profiles and explicit user-override handling.
- Brainstorming/design, worktree, subagent execution, review reception, verification, and branch-finishing skills.
- Execution-ledger and risk-classification references.
- Structural package validator and workflow contract tests.
- GitHub Actions validation workflow.
