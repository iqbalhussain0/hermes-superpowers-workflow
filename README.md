# Hermes Superpowers Workflow

Hermes-native workflow discipline adapted from Superpowers without installing the upstream plugin alongside Hermes skills. This repository is distributed as a Hermes skill tap because it contains skills and no Python plugin runtime.

**Do not install the upstream Superpowers plugin (`obra/superpowers`) on the same profile as this tap.** The upstream package uses the same skill names and identifier resolution becomes ambiguous.

## Included skills

- `superpowers-workflow` — routes work by risk and complexity.
- `brainstorming-and-design` — requirements, alternatives, design, and approval.
- `using-git-worktrees` — repository isolation when appropriate.
- `receiving-code-review` — evidence-based review feedback handling.
- `verification-before-completion` — claim-to-evidence completion gate.
- `finishing-development-branch` — explicit merge, PR, retain, or discard disposition.

`subagent-driven-development` is not redistributed here. Current Hermes releases ship an official optional skill with that name; install it with `hermes skills install official/software-development/subagent-driven-development`. The `superpowers-workflow` skill carries a compatibility overlay for its current Hermes limitations (workers cannot ask questions; no `toolsets` parameter; workers do not commit).

The package preserves Hermes' higher-priority safety, authorization, credential, operational, and recovery rules. It makes strong recommendations, but explicit current user directions override ordinary workflow ceremony.

## Installation from a GitHub skill tap

After the repository is created on GitHub:

```bash
hermes skills tap add OWNER/hermes-superpowers-workflow
hermes skills install OWNER/hermes-superpowers-workflow/skills/superpowers-workflow
```

Install the other workflow skills from the same tap when needed:

```bash
hermes skills install OWNER/hermes-superpowers-workflow/skills/brainstorming-and-design --yes
hermes skills install OWNER/hermes-superpowers-workflow/skills/using-git-worktrees --yes
hermes skills install OWNER/hermes-superpowers-workflow/skills/receiving-code-review --yes
hermes skills install OWNER/hermes-superpowers-workflow/skills/verification-before-completion --yes
hermes skills install OWNER/hermes-superpowers-workflow/skills/finishing-development-branch --yes
```

Do not install `subagent-driven-development` from this tap on a current Hermes release; the official bundled skill of the same name wins identifier resolution. Review the repository before installation; installed skills have the same trusted instruction posture as other Hermes skills.

## Local development

Skill taps use this layout:

```text
skills/<skill-name>/SKILL.md
```

Validate frontmatter and related-skill references with:

```bash
python3 tests/validate_package.py
```

After installation, start a fresh Hermes session so the skill index reloads.

## Removal and rollback

```bash
hermes skills uninstall superpowers-workflow
hermes skills tap remove OWNER/hermes-superpowers-workflow
```

Removing the tap or an installed skill does not delete project plans, specifications, ledgers, Git branches, or Obsidian notes. Review and preserve those artifacts according to the project workflow.

## Behavioral scenario tests

`tests/run_scenarios.py` runs live fresh-session checks against the default profile (`hermes chat -q --skills ...`). These cost real model calls — run them deliberately:

```bash
python3 tests/run_scenarios.py
```

## Artifact conventions

- Plan-only turns (official `plan` skill): `.hermes/plans/`
- Execution plans (this package): `.hermes/workflows/<plan-id>/plan.md`
- Specifications: `docs/specs/`
- Execution ledgers: `.hermes/workflows/<plan-id>/progress.md`
- Operational records: wherever the project already keeps runbooks. Do not create an Obsidian note unless the project already uses Obsidian.
- Workflow artifacts never contain secrets, credential values, or unredacted sensitive output.
