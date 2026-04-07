#!/usr/bin/env python3
"""
Interactive validation for Active Directory / internal pentest findings.
Walks through ROE, evidence, impact, and produces a markdown draft in findings/.

Usage:
  python3 tools/validate.py
  python3 tools/validate.py --output findings/validation-draft.md
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime

BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def ask(prompt: str, default: str = "") -> str:
    extra = f" [{default}]" if default else ""
    line = input(f"{prompt}{extra}: ").strip()
    return line or default


def ask_yn(prompt: str, default: bool = False) -> bool:
    suf = "Y/n" if default else "y/N"
    r = input(f"{prompt} ({suf}): ").strip().lower()
    if not r:
        return default
    return r in ("y", "yes")


def main() -> None:
    parser = argparse.ArgumentParser(description="AD finding validation assistant")
    parser.add_argument("--output", default="", help="Write markdown to this path")
    args = parser.parse_args()

    print(f"\n{BOLD}Claude Active Directory — finding validation{RESET}\n")

    title = ask("Finding title")
    technique = ask("Technique (e.g. Kerberoast, ESC1, ACL GenericAll)")
    target = ask("Affected domain / hostname")
    in_roe = ask_yn("All affected systems explicitly in ROE?", default=True)
    if not in_roe:
        print(f"{RED}Stop — clarify scope before continuing.{RESET}")
        sys.exit(1)
    reproducible = ask_yn("Steps reproduced by a second tester?", default=True)
    evidence = ask("Evidence summary (paths to logs, redacted commands)")
    impact = ask("Business / technical impact")
    severity = ask("Proposed severity (critical/high/medium/low/info)", "high")

    lines = [
        "# Validated finding (draft)",
        "",
        f"**Title:** {title}",
        f"**Technique:** {technique}",
        f"**Target:** {target}",
        f"**Severity:** {severity}",
        f"**Validated:** {datetime.now().isoformat()}Z",
        "",
        "## ROE",
        f"- In scope: **{'yes' if in_roe else 'no'}**",
        "",
        "## Evidence",
        evidence,
        "",
        "## Impact",
        impact,
        "",
        "## Reproducibility",
        f"- Second tester can replay: **{'yes' if reproducible else 'needs work'}**",
        "",
        "## Remediation (draft)",
        "- (fill with customer-specific controls)",
        "",
    ]
    body = "\n".join(lines)
    print(f"\n{GREEN}--- Draft ---{RESET}\n{body}")

    out = args.output
    if not out:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        findings = os.path.join(base, "findings")
        os.makedirs(findings, exist_ok=True)
        safe = "".join(c if c.isalnum() else "_" for c in title.lower())[:40] or "finding"
        out = os.path.join(findings, f"validation-{safe}.md")

    with open(out, "w") as f:
        f.write(body)
    print(f"\n{GREEN}Wrote {out}{RESET}")


if __name__ == "__main__":
    main()
