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


def test_subagent_loop_is_bounded_and_integrated():
    body = text("subagent-driven-development")
    assert "Prefer inline execution" in body
    assert "Worker brief" in body
    assert "Inspect the worker's claimed files and diff independently" in body
    assert "Integrated review" in body
    assert "reconcile the ledger against Git, files, and live runtime state" in body
    assert "references/execution-ledger.md" in body
    assert (SKILLS / "subagent-driven-development" / "references" / "execution-ledger.md").is_file()


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


def test_repository_documents_supported_tap_installation():
    body = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "hermes skills tap add OWNER/hermes-superpowers-workflow" in body
    assert "hermes skills install OWNER/hermes-superpowers-workflow/skills/superpowers-workflow" in body
    assert "hermes plugins install" not in body
