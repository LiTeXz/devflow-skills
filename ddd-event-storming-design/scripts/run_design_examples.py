#!/usr/bin/env python3
"""Regression checks for validate_ddd_design.py examples."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VALIDATOR = ROOT / "validate_ddd_design.py"
EXAMPLES = ROOT / "examples"


CASES = [
    ("valid_design", EXAMPLES / "valid_design.md", ["--require-sections"], 0),
    ("table_first", EXAMPLES / "table_first.md", [], 1),
]


def main() -> int:
    failures = 0
    for name, path, extra_args, expected in CASES:
        cmd = [sys.executable, str(VALIDATOR), str(path), *extra_args]
        result = subprocess.run(
            cmd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )
        ok = result.returncode == expected
        status = "PASS" if ok else "FAIL"
        print(f"{status} {name}: expected {expected}, got {result.returncode}")
        if not ok:
            print(result.stdout)
            print(result.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
