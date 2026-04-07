#!/usr/bin/env python3
"""
Prioritized AD TTP checklist and optional Mermaid overview.

Usage:
  python3 tools/mindmap.py --target corp.local
  python3 tools/mindmap.py --domain corp.local
"""

import argparse
import os
from datetime import datetime

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

AD_CHECKS = [
    ("HIGH", "AS-REP roastable users (UAC) — offline crack", "skills/ad-attack-classes"),
    ("HIGH", "Kerberoastable SPNs on user accounts", "skills/ad-attack-classes"),
    ("HIGH", "Unconstrained / constrained delegation / RBCD edges", "BloodHound"),
    ("HIGH", "AD CS dangerous templates (ESC patterns)", "skills/ad-cs-pki"),
    ("MED", "ACL abuse — GenericAll, WriteDACL, ownership", "BloodHound / manual"),
    ("MED", "GPP / cPassword remnants", "SYSVOL policy review"),
    ("MED", "NTLM relay opportunities (signing disabled)", "crackmapexec, mitm6 if allowed"),
    ("LOW", "Password policy + lockout for spray planning", "recon notes"),
]


def build_mermaid(domain: str) -> str:
    sid = "".join(c if c.isalnum() else "_" for c in domain)
    return f"""flowchart TD
    recon[Recon DNS LDAP] --> creds[Credential Access]
    creds --> esc[Privilege Escalation]
    esc --> lateral[Lateral Movement]
    lateral --> obj[Engagement Objectives]
    subgraph {sid}["{domain}"]
        recon
        creds
        esc
        lateral
        obj
    end
"""


def main() -> None:
    p = argparse.ArgumentParser(description="AD engagement mindmap")
    p.add_argument("--target", default="", help="AD domain name")
    p.add_argument("--domain", default="", help="Alias for --target")
    p.add_argument("--output", default="")
    args = p.parse_args()

    domain = args.domain or args.target or "domain.local"
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "findings", domain)
    os.makedirs(base, exist_ok=True)
    out = args.output or os.path.join(base, "mindmap.md")

    lines = [
        f"# Active Directory engagement map — {domain}",
        "",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "## Flow",
        "",
        "```mermaid",
        build_mermaid(domain),
        "```",
        "",
        "## Prioritized checks",
        "",
    ]
    for impact, desc, ref in AD_CHECKS:
        lines.append(f"- **{impact}** — {desc} → `{ref}`")

    lines.extend(["", "---", "", "_Evaluris Solutions — Claude Active Directory_", ""])

    with open(out, "w") as f:
        f.write("\n".join(lines))

    print(f"{BOLD}{CYAN}Wrote{RESET} {out}\n")
    for impact, desc, ref in AD_CHECKS:
        color = {"HIGH": RED, "MED": YELLOW, "LOW": GREEN}.get(impact, "")
        print(f"  {color}[{impact}]{RESET} {desc}")
        print(f"         → {ref}")


if __name__ == "__main__":
    main()
