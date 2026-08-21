# Hermes Superpowers Workflow

Hermes-native workflow discipline adapted from Superpowers without installing the upstream plugin alongside Hermes skills. This repository is distributed as a Hermes skill tap because it contains skills and no Python plugin runtime.

## Included skills

- `superpowers-workflow` — routes work by risk and complexity.
- `brainstorming-and-design` — requirements, alternatives, design, and approval.
- `using-git-worktrees` — repository isolation when appropriate.
- `subagent-driven-development` — bounded workers, review, integration, and ledger recovery.
- `receiving-code-review` — evidence-based review feedback handling.
- `verification-before-completion` — claim-to-evidence completion gate.
- `finishing-development-branch` — explicit merge, PR, retain, or discard disposition.

The package preserves Hermes' higher-priority safety, authorization, credential, operational, and recovery rules. It makes strong recommendations, but explicit current user directions override ordinary workflow ceremony.

## Installation from a GitHub skill tap

After the repository is created on GitHub:

```bash
hermes skills tap add OWNER/hermes-superpowers-workflow
hermes skills install OWNER/hermes-superpowers-workflow/skills/superpowers-workflow
```

Install the other workflow skills from the same tap when needed. Review the repository before installation; installed skills have the same trusted instruction posture as other Hermes skills.

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

## Artifact conventions

- Plans: `.hermes/plans/`
- Specifications: `docs/specs/`
- Execution ledgers: `.hermes/workflows/<plan-id>/progress.md`
- Operational records: the project's runbook or Obsidian operational note
