#!/usr/bin/env python3
"""
Engagement report generator — Active Directory / internal pentest style.

Usage:
    python3 report_generator.py <findings_dir>
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")


def process_findings_dir(findings_dir: str) -> tuple[int, list[dict]]:
    """Build a summary markdown from loose files in findings_dir."""
    target_name = os.path.basename(os.path.normpath(findings_dir))
    report_dir = os.path.join(REPORTS_DIR, target_name)
    os.makedirs(report_dir, exist_ok=True)

    index: list[dict] = []
    artifacts: list[str] = []
    if os.path.isdir(findings_dir):
        for root, _, files in os.walk(findings_dir):
            for fn in files:
                if fn.endswith((".md", ".txt", ".json")):
                    artifacts.append(os.path.join(root, fn))

    summary_path = os.path.join(report_dir, "SUMMARY.md")
    lines = [
        f"# Engagement report — {target_name}",
        "",
        f"**Generated:** {datetime.now().isoformat()}Z",
        "",
        "## Scope reference",
        "",
        "Document customer name, ROE limits, and assessment window in this section.",
        "",
        "## Findings index",
        "",
    ]
    if not artifacts:
        lines.append("_No artifact files found under findings directory._")
    else:
        for p in sorted(artifacts)[:200]:
            rel = os.path.relpath(p, findings_dir)
            lines.append(f"- `{rel}`")
        if len(artifacts) > 200:
            lines.append(f"- _…and {len(artifacts) - 200} more_")

    lines.extend(
        [
            "",
            "## Narrative",
            "",
            "Fill: methodology, key paths, impact, remediation priorities.",
            "",
            "---",
            "",
            "_Claude Active Directory — Evaluris Solutions_",
            "",
        ]
    )

    with open(summary_path, "w") as f:
        f.write("\n".join(lines))

    index.append({"severity": "info", "title": "summary", "path": summary_path})
    return 1, index


def main() -> None:
    parser = argparse.ArgumentParser(description="AD engagement report generator")
    parser.add_argument("findings_dir", nargs="?", help="Directory containing finding artifacts")
    args = parser.parse_args()

    print("=============================================")
    print("  Claude Active Directory — reports")
    print("=============================================")

    if not args.findings_dir:
        print("Usage: python3 report_generator.py <findings_dir>")
        sys.exit(1)
    if not os.path.isdir(args.findings_dir):
        print(f"Not a directory: {args.findings_dir}")
        sys.exit(1)

    total, index = process_findings_dir(args.findings_dir)
    print(f"\n[+] Wrote summary ({total})")
    if index:
        t = os.path.basename(os.path.normpath(args.findings_dir))
        print(f"Summary: {REPORTS_DIR}/{t}/SUMMARY.md")


if __name__ == "__main__":
    main()
