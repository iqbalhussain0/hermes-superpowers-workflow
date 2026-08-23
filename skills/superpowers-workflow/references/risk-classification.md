# Risk Classification

Every task is classified on two independent axes. Apply the *union* of both axes' controls — never let one replace the other.

## Axis 1: Work shape

| Shape | Trigger | Controls |
|---|---|---|
| Inquiry | inspection, research, diagnosis, reporting | fresh evidence; no mutation; read-only debugging rules |
| Empirical spike | a question that requires an experiment | route to the official `spike` skill; operational authorization if the probe mutates anything or is externally visible |
| Bounded code | limited change to an existing flow | short design, acceptance checks, focused verification, diff inspection |
| Architectural code | new subsystem, public interface, major refactor, several independent tasks | design agreement, implementation plan, isolation recommendation, per-task and integrated review |

## Axis 2: Operational risk

| Risk | Trigger | Controls |
|---|---|---|
| None | local, reversible, private | ordinary workflow controls |
| Reversible configuration | local config with a rollback path | backup or diff, syntax check, rollback path |
| Deployment | service restart or release | staged change, health check, recovery path, rollback |
| Privileged | root/admin or credential-bearing action | exact scoped authorization via the host's grant path, audit, post-check |
| Security boundary | firewall, SSH, auth, permissions | independent recovery path verified first, effective-state check, external probe where relevant |
| Destructive | deletion, irreversible migration, credential revocation | explicit irreversible authorization for the exact action and target, restore evidence, narrow scope |

## Selection rules

- Choose the lightest accurate work shape.
- Add controls from the highest applicable operational risk.
- A bounded code change that touches a firewall is *bounded code plus security boundary*: both columns apply.
- A user may reduce ordinary workflow ceremony by explicit direction, but may not remove non-bypassable authorization, credential, recovery, or safety controls.
- A failed baseline does not become a pass because the requested change is unrelated; record the baseline and isolate new evidence.
- If recovery is unverified, say so before any action that could remove the remaining recovery path.

## Recording

Record both axis selections, the controls applied, user overrides, and evidence in the plan or ledger when one exists.
