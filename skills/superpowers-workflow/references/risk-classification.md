# Workflow Risk Classification

Classify the work before choosing ceremony. Use the highest applicable risk dimension.

## Dimensions

- **Mutation:** read-only, local mutation, remote mutation, external publication.
- **Privilege:** ordinary user, scoped privilege, root/administrator, credential-bearing.
- **Reversibility:** disposable, reversible, rollback-dependent, destructive.
- **Blast radius:** one file, one repository, one service, host, network boundary, fleet, public users.
- **Recovery dependence:** independent recovery path available, degraded recovery, no verified recovery.
- **Visibility:** private, internal, externally observable, irreversible/public.

## Profiles

| Profile | Typical work | Minimum controls |
|---|---|---|
| Read-only | inspect, search, diagnose | fresh evidence; no mutation |
| Spike | feasibility probe | scope, disposable artifacts, approval for mutation |
| Bounded code | small existing-flow change | focused acceptance checks; diff inspection |
| Architectural code | new subsystem or cross-cutting refactor | design/spec, plan, isolation recommendation, integrated review |
| Reversible configuration | local config with rollback | backup or diff, syntax check, rollback path |
| Restart/deployment | service activation or release | staged change, health check, recovery path, rollback |
| Privileged mutation | scoped root/admin action | exact authorization, bounded wrapper, audit, post-check |
| Security boundary | firewall, SSH, auth, permissions | independent recovery, effective-state check, external probe where relevant |
| Destructive/irreversible | deletion, migration, credential revocation | explicit irreversible approval, restore evidence, narrow scope |

## Escalation rules

- A higher risk dimension upgrades the minimum controls.
- A user may choose less ordinary workflow ceremony, but may not remove non-bypassable authorization, credential, recovery, or safety controls.
- A failed baseline does not become a pass because the requested change is unrelated; record the baseline and isolate the new evidence.
- If recovery is unverified, report that state before any action that could remove the remaining recovery path.

## Output

Record the selected profile, dimensions, controls, user overrides, and evidence in the plan or execution ledger when one exists.
