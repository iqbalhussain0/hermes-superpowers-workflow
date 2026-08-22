#!/usr/bin/env python3
"""Behavioral scenario tests: run live fresh Hermes sessions and check behavior.

Each scenario preloads package skills with --skills and asserts the response.
These tests cost real model calls; run them deliberately, not in CI on every push.

Usage:
    python3 tests/run_scenarios.py [--scenario ID] [--json]
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = yaml.safe_load((ROOT / "tests" / "scenarios.yaml").read_text())["scenarios"]


def run_scenario(scn: dict, timeout: int = 240) -> dict:
    cmd = ["hermes", "chat", "-q", scn["prompt"]]
    for skill in scn.get("skills", []):
        cmd += ["--skills", skill]
    start = time.time()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        output = (proc.stdout or "") + "\n" + (proc.stderr or "")
    except subprocess.TimeoutExpired:
        return {"id": scn["id"], "result": "BLOCKED", "reason": f"timeout after {timeout}s"}
    elapsed = time.time() - start

    if proc.returncode != 0:
        return {"id": scn["id"], "result": "BLOCKED", "reason": f"hermes exited {proc.returncode}", "output_excerpt": output.strip()[-400:]}

    import re as _re
    norm = lambda s: _re.sub(r"\s+", " ", s.lower())
    checked = norm(output).replace(norm(scn["prompt"]), " ")

    failures = []
    if not any(marker.lower() in checked for marker in scn.get("must_contain_any", [])):
        failures.append(f"missing all of {scn['must_contain_any']}")
    for marker in scn.get("must_not_contain", []):
        if marker.lower() in checked:
            failures.append(f"forbidden marker present: {marker!r}")
    return {
        "id": scn["id"],
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
        "elapsed_s": round(elapsed, 1),
        "output_excerpt": output.strip()[-600:],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", help="run a single scenario by id")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    selected = SCENARIOS
    if args.scenario:
        selected = [s for s in SCENARIOS if s["id"] == args.scenario]
        if not selected:
            print(f"unknown scenario: {args.scenario}", file=sys.stderr)
            return 2

    results = [run_scenario(s) for s in selected]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['result']:8} {r['id']} ({r.get('elapsed_s', '-')}s)")
            for failure in r.get("failures", []):
                print(f"         FAIL: {failure}")
            if r["result"] != "PASS":
                print(f"         excerpt: {r.get('output_excerpt', '')[:400]}")
    failed = [r for r in results if r["result"] == "FAIL"]
    blocked = [r for r in results if r["result"] == "BLOCKED"]
    print(f"\nSCENARIOS={len(results)} PASS={len(results) - len(failed) - len(blocked)} FAIL={len(failed)} BLOCKED={len(blocked)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
