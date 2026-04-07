#!/usr/bin/env python3
"""
Claude Active Directory — engagement orchestrator.

Phases: recon (ad_recon.sh) → optional report generation → structured directories under recon/ and findings/.

External tooling (Impacket, Certipy, CrackMapExec, SharpHound) is optional; this script checks presence and prints hints.

Usage:
    python3 hunt.py --target corp.local
    python3 hunt.py --recon-only --target corp.local
    python3 hunt.py --status
    python3 hunt.py --check-tools
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(TOOLS_DIR)
TARGETS_DIR = os.path.join(BASE_DIR, "targets")
RECON_DIR = os.path.join(BASE_DIR, "recon")
FINDINGS_DIR = os.path.join(BASE_DIR, "findings")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")

GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
BOLD = "\033[1m"
NC = "\033[0m"


def log(level, msg):
    colors = {"ok": GREEN, "err": RED, "warn": YELLOW, "info": CYAN}
    symbols = {"ok": "+", "err": "-", "warn": "!", "info": "*"}
    print(f"{colors.get(level, '')}{BOLD}[{symbols.get(level, '*')}]{NC} {msg}")


def run_cmd(cmd, cwd=None, timeout=600):
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, cwd=cwd, timeout=timeout
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def check_tools():
    """Check common AD / offensive tooling (optional)."""
    tools = [
        "nmap",
        "dig",
        "ldapsearch",
        "crackmapexec",
        "certipy",
        "secretsdump.py",
        "GetUserSPNs.py",
    ]
    installed, missing = [], []
    for tool in tools:
        success, _ = run_cmd(f"command -v {tool} 2>/dev/null || which {tool} 2>/dev/null")
        if success:
            installed.append(tool)
        else:
            missing.append(tool)
    # Impacket often has no single binary name
    imp_ok, _ = run_cmd(
        "python3 -c \"import importlib.util; "
        "print('ok') if importlib.util.find_spec('impacket') else exit(1)\""
    )
    if imp_ok:
        installed.append("impacket (python)")
    else:
        missing.append("impacket (pip install impacket)")
    return installed, missing


def setup_wordlists():
    """Ensure wordlists dir exists; document spray lists (authorized use only)."""
    os.makedirs(WORDLIST_DIR, exist_ok=True)
    readme = os.path.join(WORDLIST_DIR, "README.txt")
    if not os.path.exists(readme):
        with open(readme, "w") as f:
            f.write(
                "Password lists for authorized spray only.\n"
                "Do not use against systems without written permission.\n"
            )
    log("ok", f"Wordlist directory ready: {WORDLIST_DIR}")


def _resolve_recon_dir(domain: str) -> str:
    d = os.path.join(RECON_DIR, domain)
    os.makedirs(d, exist_ok=True)
    return d


def _resolve_findings_dir(domain: str, create: bool = True):
    d = os.path.join(FINDINGS_DIR, domain)
    if create:
        os.makedirs(d, exist_ok=True)
    return d if os.path.isdir(d) else None


def _activate_recon_session(domain: str, requested_session_id: str = "latest", create: bool = True):
    """Return (session_id, recon_dir) for agent.py — artifacts live under recon/<domain>/."""
    recon_dir = _resolve_recon_dir(domain)
    sid = requested_session_id if requested_session_id not in (None, "", "latest") else "default"
    return sid, recon_dir


def run_recon(domain: str, scope_lock: bool = False, max_urls: int = 100) -> bool:
    """Run AD-oriented recon shell script."""
    log("info", f"Running AD recon for {domain}...")
    script = os.path.join(TOOLS_DIR, "ad_recon.sh")
    if not os.path.isfile(script):
        log("err", f"Missing {script}")
        return False
    sl = "1" if scope_lock else "0"
    ok, out = run_cmd(f'bash "{script}" "{domain}" {sl}', cwd=BASE_DIR, timeout=1800)
    if out:
        print(out[-4000:])
    return ok


def run_vuln_scan(domain: str, quick: bool = False, full: bool = False) -> bool:
    log(
        "warn",
        "Web vuln pipeline removed in Claude Active Directory edition — use manual testing per ROE.",
    )
    return True


def run_js_analysis(domain: str) -> bool:
    log("info", "JS analysis stub — not used in AD edition.")
    return True


def run_secret_hunt(domain: str) -> bool:
    log("info", "Secret hunt stub — use customer-approved secret scanners if in scope.")
    return True


def run_param_discovery(domain: str) -> bool:
    log("info", "Param discovery stub — AD edition focuses on LDAP/Kerberos paths.")
    return True


def run_post_param_discovery(domain: str, cookies: str = "") -> bool:
    log("info", "POST param discovery stub.")
    return True


def run_api_fuzz(domain: str) -> bool:
    log("info", "API fuzz stub.")
    return True


def run_cors_check(domain: str) -> bool:
    log("info", "CORS check stub — use for OWA/AD FS web only if in scope.")
    return True


def run_cms_exploit(domain: str) -> bool:
    log("info", "CMS exploit stub — not applicable to core AD workflow.")
    return True


def run_rce_scan(domain: str) -> bool:
    log("info", "RCE scan stub.")
    return True


def run_sqlmap_targeted(domain: str) -> bool:
    log("info", "sqlmap stub.")
    return True


def run_sqlmap_request_file(
    request_file: str, domain: str = "", level: int = 5, risk: int = 3
) -> bool:
    log("info", "sqlmap request-file stub.")
    return False


def run_jwt_audit(domain: str) -> bool:
    log("info", "JWT audit stub — relevant for AD FS / OAuth web surfaces.")
    return True


def load_targets(top_n: int = 10):
    """Load targets from targets/engagement_targets.json (see target_loader.py)."""
    loader = os.path.join(TOOLS_DIR, "target_loader.py")
    ok, out = run_cmd(f'python3 "{loader}" --list --top {top_n}', cwd=BASE_DIR)
    print(out)
    path = os.path.join(TARGETS_DIR, "engagement_targets.json")
    if os.path.isfile(path):
        with open(path) as f:
            data = json.load(f)
        return data.get("targets", [])
    return []


def generate_reports(domain: str) -> int:
    findings_dir = os.path.join(FINDINGS_DIR, domain)
    if not os.path.isdir(findings_dir):
        log("warn", f"No findings dir for {domain}")
        return 0
    log("info", f"Generating report skeleton for {domain}...")
    script = os.path.join(TOOLS_DIR, "report_generator.py")
    ok, out = run_cmd(f'python3 "{script}" "{findings_dir}"', cwd=BASE_DIR)
    print(out)
    report_dir = os.path.join(REPORTS_DIR, domain)
    if os.path.isdir(report_dir):
        return len([f for f in os.listdir(report_dir) if f.endswith(".md")])
    return 0


def show_status():
    print(f"\n{BOLD}{'='*50}{NC}")
    print(f"{BOLD}  Claude Active Directory — status{NC}\n")
    installed, missing = check_tools()
    print(f"  Optional tools: {len(installed)} found")
    if missing:
        print(f"  Not found (install as needed): {', '.join(missing[:8])}")
    for name, path in (
        ("Recon", RECON_DIR),
        ("Findings", FINDINGS_DIR),
        ("Reports", REPORTS_DIR),
    ):
        n = len(os.listdir(path)) if os.path.isdir(path) else 0
        print(f"  {name} dirs: {n}")
    print(f"\n{'='*50}\n")


def print_dashboard(results):
    print(f"\n{BOLD}{'='*60}{NC}")
    print(f"{BOLD}  Engagement summary{NC}")
    print(f"{BOLD}{'='*60}{NC}\n")
    for r in results:
        icon = f"{GREEN}OK{NC}" if r.get("success") else f"{RED}FAIL{NC}"
        print(f"  [{icon}] {r.get('domain')}")
    print(f"\n{'='*60}\n")


def hunt_target(
    domain: str,
    quick: bool = False,
    recon_only: bool = False,
    scan_only: bool = False,
    cve_hunt: bool = False,
    zero_day: bool = False,
):
    result = {"domain": domain, "success": True, "recon": False, "scan": False, "reports": 0, "findings": 0}
    if not scan_only:
        result["recon"] = run_recon(domain, scope_lock=quick)
    if recon_only:
        return result
    result["scan"] = run_vuln_scan(domain, quick=quick)
    if cve_hunt:
        log("info", "CVE hunt: use intel tools / customer VM inventory — no automatic scanner in AD edition.")
    if zero_day:
        log("warn", "--zero-day disabled in AD edition.")
    result["reports"] = generate_reports(domain)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Claude Active Directory — engagement orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--target", type=str, help="Target AD DNS name (e.g. corp.local)")
    parser.add_argument("--quick", action="store_true", help="Scope-lock style recon")
    parser.add_argument("--recon-only", action="store_true")
    parser.add_argument("--scan-only", action="store_true")
    parser.add_argument("--report-only", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--check-tools", action="store_true")
    parser.add_argument("--setup-wordlists", action="store_true")
    parser.add_argument("--cve-hunt", action="store_true")
    parser.add_argument("--zero-day", action="store_true")
    parser.add_argument("--select-targets", action="store_true")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    print(
        f"""
{BOLD}╔══════════════════════════════════════════╗
║   Claude Active Directory — orchestrator ║
╚══════════════════════════════════════════╝{NC}
"""
    )

    if args.status:
        show_status()
        return
    if args.check_tools:
        installed, missing = check_tools()
        print("Installed:", ", ".join(installed) or "(none)")
        print("Missing:", ", ".join(missing) or "(none)")
        return
    if args.setup_wordlists:
        setup_wordlists()
        return

    if args.report_only:
        if args.target:
            generate_reports(args.target)
        return

    if args.select_targets:
        load_targets(top_n=args.top)
        return

    if args.target:
        hunt_target(
            args.target,
            quick=args.quick,
            recon_only=args.recon_only,
            scan_only=args.scan_only,
            cve_hunt=args.cve_hunt,
            zero_day=args.zero_day,
        )
        print_dashboard([{"domain": args.target, "success": True}])
        return

    log("info", "No --target; use: python3 hunt.py --target corp.local")
    parser.print_help()


if __name__ == "__main__":
    main()
