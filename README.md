# Hermes Superpowers Workflow

Hermes-native workflow discipline adapted from Superpowers without installing the upstream plugin alongside Hermes skills.

## Included skills

- `superpowers-workflow` — routes work by risk and complexity.
- `brainstorming-and-design` — requirements, alternatives, design, and approval.
- `using-git-worktrees` — repository isolation when appropriate.
- `subagent-driven-development` — bounded workers, review, integration, and ledger recovery.
- `receiving-code-review` — evidence-based review feedback handling.
- `verification-before-completion` — claim-to-evidence completion gate.
- `finishing-development-branch` — explicit merge, PR, retain, or discard disposition.

The package preserves Hermes' higher-priority safety, authorization, credential, operational, and recovery rules. It makes strong recommendations, but explicit current user directions override ordinary workflow ceremony.

## Portable installation

From a GitHub repository:

```bash
hermes plugins install OWNER/hermes-superpowers-workflow --no-enable
hermes plugins list
hermes plugins enable hermes-superpowers-workflow
```

The plugin is opt-in. Enabling it grants the package's instructions the same trusted posture as other installed skills; review the repository before installation.

## Local development

Portable packages use this layout:

```text
plugin.json
skills/<skill-name>/SKILL.md
```

Validate frontmatter and related-skill references with:

```bash
python3 tests/validate_package.py
```

After installation, start a fresh Hermes session so the skill index reloads.

## Removal and rollback

```bash
hermes plugins disable hermes-superpowers-workflow
hermes plugins remove hermes-superpowers-workflow
```

Removing the plugin does not delete project plans, specifications, ledgers, Git branches, or Obsidian notes. Review and preserve those artifacts according to the project workflow.

## Artifact conventions

- Plans: `.hermes/plans/`
- Specifications: `docs/specs/`
- Execution ledgers: `.hermes/workflows/<plan-id>/progress.md`
- Operational records: the project's runbook or Obsidian operational note
