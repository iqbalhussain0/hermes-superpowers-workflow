"""Executable smoke tests for the reliability overlay's critical contracts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "skills" / "reliability-engineering" / "templates"


def stable_key(workflow: str, operation: str, target: str, payload: str) -> str:
    canonical = "|".join((workflow, operation, target, payload))
    return hashlib.sha256(canonical.encode()).hexdigest()


def validate_result(*, execution_ok: bool, output_ok: bool, outcome_ok: bool) -> str:
    return "COMPLETE" if execution_ok and output_ok and outcome_ok else "UNVERIFIED"


def apply_once(processed: set[str], key: str, effects: list[str]) -> bool:
    """Model a pre-side-effect duplicate gate; return whether an effect ran."""
    if key in processed:
        return False
    processed.add(key)
    effects.append(key)
    return True


def test_success_requires_all_three_health_layers():
    assert validate_result(execution_ok=True, output_ok=True, outcome_ok=True) == "COMPLETE"
    assert validate_result(execution_ok=True, output_ok=False, outcome_ok=True) == "UNVERIFIED"
    assert validate_result(execution_ok=True, output_ok=True, outcome_ok=False) == "UNVERIFIED"
    assert validate_result(execution_ok=False, output_ok=True, outcome_ok=True) == "UNVERIFIED"


def test_stable_idempotency_key_blocks_duplicate_effects():
    key_a = stable_key("daily-digest", "send", "customer-42", "digest-v1")
    key_b = stable_key("daily-digest", "send", "customer-42", "digest-v1")
    assert key_a == key_b

    processed: set[str] = set()
    effects: list[str] = []
    assert apply_once(processed, key_a, effects) is True
    assert apply_once(processed, key_b, effects) is False
    assert effects == [key_a]


def test_state_template_is_machine_readable_and_secret_free():
    raw = (TEMPLATES / "workflow-state.yaml").read_text()
    state = yaml.safe_load(raw)
    assert state["schema_version"]
    assert state["run_id"]
    assert "status" in state
    assert "never store secrets" in raw.lower()
    assert "password" not in raw.lower()


def test_regression_template_requires_approval_and_forbids_side_effect():
    case = json.loads((TEMPLATES / "regression-case.json").read_text())
    text = json.dumps(case).lower()
    assert "approval" in text
    assert "does not send externally" in text
    assert "does not claim the message was sent" in text
    assert "external side effect" in text
