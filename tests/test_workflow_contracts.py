from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def text(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


def test_router_has_narrow_trigger_and_counter_triggers():
    import yaml
    body = text("superpowers-workflow")
    desc = yaml.safe_load(body.split("---", 2)[1])["description"]
    assert len(desc) <= 57 or "Superpowers" in desc or "Route" in desc
    assert "Do not load for" in body
    assert "single-domain task" in body


def test_router_preserves_authority_and_override_policy():
    body = text("superpowers-workflow")
    assert "explicit current user direction overrides" in body
    assert "higher-priority system, authorization, legal, or security constraint" in body
    assert "never load it and then try to override" in body


def test_router_routing_is_conditional_and_exclusive():
    body = text("superpowers-workflow")
    assert "plan-only" in body
    assert "For an already-authorized implementation" in body
    assert "unless the user explicitly skipped it" in body
    assert "unexplained defect" in body
    assert "official `spike` skill" in body
    assert "only when the user chose delegated multi-task execution" in body
    assert "only when the user asked for a pre-commit review pass" in body
    assert "git add -A" in body
    assert "set -o pipefail" in body


def test_sdd_compatibility_overlay():
    body = text("superpowers-workflow")
    assert "Workers cannot ask the user questions" in body
    assert "no `toolsets` parameter" in body
    assert "Workers may not commit, push, or create remotes" in body


def test_authorization_binding_and_ledger_semantics():
    body = text("superpowers-workflow")
    assert "not an authorization token" in body
    assert "revalidate" in body
    ledger = (SKILLS / "superpowers-workflow" / "references" / "execution-ledger.md").read_text()
    assert "One-shot or reusable" in ledger
    assert "Consumed / revoked" in ledger
    assert "timestamped historical observations" in ledger
    assert "todo` tool is the live task list" in ledger
    assert "secret scan" in ledger


def test_completion_states():
    body = text("superpowers-workflow")
    assert "COMPLETE" in body and "PARTIALLY COMPLETE" in body and "BLOCKED" in body
    assert "A blocked requirement never satisfies completion" in body
    plan = (SKILLS / "brainstorming-and-design" / "templates" / "implementation-plan.md").read_text()
    assert "A blocked requirement never satisfies completion" in plan


def test_risk_classification_is_two_axis():
    body = (SKILLS / "superpowers-workflow" / "references" / "risk-classification.md").read_text()
    assert "Axis 1: Work shape" in body and "Axis 2: Operational risk" in body
    assert "union" in body.lower()
    assert "bounded code plus security boundary" in body


def test_worktree_predicates_are_correct():
    body = text("using-git-worktrees")
    assert "no native worktree mechanism" not in body
    assert 'git check-ignore -q -- "$WORKTREE_PARENT"' in body
    assert '"$BASE_COMMIT"' in body
    assert "hermes -w" in body
    assert "before any mutation" in body
    assert "DETACHED" in body


def test_verification_wording_is_precise():
    body = text("verification-before-completion")
    assert "set -o pipefail" in body
    assert "recovery procedure reviewed" in body.lower()
    assert 'Never call a firewall "safe"' in body
    assert "UNVERIFIED" in body
    assert "tailed pipeline output" in body.lower() and "completion evidence" in body.lower()


def test_receiving_review_gates_fixes_and_risk_acceptance():
    body = text("receiving-code-review")
    assert "Ask the user first" in body
    assert "ESCALATED/ACCEPTED RISK" in body
    assert "authenticated principal" in body
    assert "never authorizes execution by itself" in body
    assert "requesting-code-review" in body  # explicitly forbidden from here


def test_finishing_branch_authorizes_commit():
    body = text("finishing-development-branch")
    assert "Commit, merge, push, publish, and discard are each separately authorized" in body
    assert "UNVERIFIED" in body


def test_no_windows_platform_claims():
    for skill_md in SKILLS.glob("*/SKILL.md"):
        assert "windows" not in skill_md.read_text().split("---", 2)[1]


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
    assert "obra/superpowers" in body  # incompatibility warning
    assert "hermes plugins install" not in body
