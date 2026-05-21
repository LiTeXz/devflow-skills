#!/usr/bin/env python3
"""Lightweight text checks for DDD event-storming artifacts.

This script is intentionally heuristic. It catches common process smells in
drafts or persisted Markdown; it does not replace human domain review.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SMELLS = {
    "table_first": [
        r"\b(create|update|delete)\s+(table|record|row)\b",
        r"\b(order_item|user_table|.*_table)\b",
        r"数据库表|数据表|表结构",
    ],
    "technical_event": [
        r"缓存.*已刷新|消息.*已发送|日志.*已记录|接口.*已调用",
        r"MQ|Kafka|Redis|HTTP.*事件",
    ],
    "crud_command": [
        r"新增.*命令|修改.*命令|删除.*命令|Create.*Command|Update.*Command|Delete.*Command",
    ],
}

REQUIRED_SECTIONS = [
    "问题域边界",
    "领域事件",
    "命令",
    "Policy",
    "聚合",
    "读模型",
    "完整性检查",
]


def read_text(path: Path) -> str:
    if path.is_dir():
        parts = []
        for file in sorted(path.rglob("*.md")):
            parts.append(f"\n# FILE: {file}\n")
            parts.append(file.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Markdown file or event-storming directory")
    parser.add_argument("--require-sections", action="store_true")
    args = parser.parse_args()

    text = read_text(Path(args.path))
    findings: list[str] = []

    for smell, patterns in SMELLS.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                findings.append(f"{smell}: matched {pattern}")

    if args.require_sections:
        for section in REQUIRED_SECTIONS:
            if section not in text:
                findings.append(f"missing_section: {section}")

    if findings:
        print("DDD design guardrail findings:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("DDD design guardrail checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
