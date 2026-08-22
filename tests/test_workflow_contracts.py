from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def text(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


def test_router_preserves_authority_and_override_policy():
    body = text("superpowers-workflow")
    assert "explicit current user direction overrides" in body
    assert "higher-priority system, authorization, legal, or security constraint" in body
    for approval in ("intent approval", "execution direction", "operational authorization", "integration authorization"):
        assert approval in body.lower()


def test_router_has_risk_sensitive_profiles():
    body = text("superpowers-workflow")
    for profile in ("Read-only inquiry", "Spike", "Bounded code change", "Architectural or multi-task code", "Operations and deployment"):
        assert profile in body
    assert ".hermes/plans/" in body
    assert "docs/specs/" in body
    assert ".hermes/workflows/<plan-id>/progress.md" in body
    assert "references/risk-classification.md" in body
    assert (SKILLS / "superpowers-workflow" / "references" / "risk-classification.md").is_file()


def test_subagent_execution_uses_official_skill_and_package_ledger():
    body = text("superpowers-workflow")
    assert "official Hermes `subagent-driven-development` skill" in body
    assert "official/software-development/subagent-driven-development" in body
    assert "references/execution-ledger.md" in body
    assert (SKILLS / "superpowers-workflow" / "references" / "execution-ledger.md").is_file()
    assert not (SKILLS / "subagent-driven-development").exists()


def test_verification_refuses_unsupported_completion_claims():
    body = text("verification-before-completion")
    assert "Do not make a completion, correctness, deployment, or success claim without fresh evidence" in body
    assert "Never fabricate output" in body
    assert "BLOCKED" in body
    assert "UNVERIFIED" in body


def test_branch_finishing_separates_integration_authorization():
    body = text("finishing-development-branch")
    assert "Do not merge, push, publish, or discard" in body
    for choice in ("Merge into the base branch", "Open or update a pull request", "Keep the branch and worktree", "Discard the branch and worktree"):
        assert choice in body


def test_templates_exist_and_are_linked():
    expected = {
        "brainstorming-and-design": ["templates/design-spec.md", "templates/implementation-plan.md"],
        "receiving-code-review": ["templates/review-disposition.md"],
        "verification-before-completion": ["templates/verification-report.md"],
    }
    for skill, templates in expected.items():
        body = text(skill)
        for template in templates:
            assert template in body
            assert (SKILLS / skill / template).is_file()


def test_repository_documents_supported_tap_installation():
    body = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "hermes skills tap add OWNER/hermes-superpowers-workflow" in body
    assert "hermes skills install OWNER/hermes-superpowers-workflow/skills/superpowers-workflow" in body
    assert "hermes plugins install" not in body
