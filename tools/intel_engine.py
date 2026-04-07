#!/usr/bin/env python3
"""
intel_engine.py — Patch/CVE intel for infrastructure keywords (Windows / AD).

Uses learn.py (NVD + GitHub Advisory). Optional hunt memory for overlap.

Usage:
    python3 intel_engine.py --target dc01.corp.local --tech "windows,kerberos"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from learn import fetch_github_advisories, fetch_nvd_cves, severity_order

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def load_memory_context(memory_dir: str, target: str) -> dict:
    context = {
        "tested_endpoints": [],
        "findings": [],
        "tech_stack": [],
        "last_hunted": None,
        "hunt_sessions": 0,
        "patterns": [],
        "tested_cves": [],
    }
    if not memory_dir or not os.path.isdir(memory_dir):
        return context
    targets_dir = os.path.join(memory_dir, "targets")
    if os.path.isdir(targets_dir):
        target_file = target.replace(".", "-").replace("/", "-") + ".json"
        target_path = os.path.join(targets_dir, target_file)
        if os.path.isfile(target_path):
            try:
                with open(target_path) as f:
                    profile = json.load(f)
                context["tested_endpoints"] = profile.get("tested_endpoints", [])
                context["findings"] = profile.get("findings", [])
                context["tech_stack"] = profile.get("tech_stack", [])
                context["last_hunted"] = profile.get("last_hunted")
                context["hunt_sessions"] = profile.get("hunt_sessions", 0)
            except (json.JSONDecodeError, OSError):
                pass
    journal_path = os.path.join(memory_dir, "journal.jsonl")
    if os.path.isfile(journal_path):
        try:
            with open(journal_path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        if entry.get("target") == target:
                            for tag in entry.get("tags", []):
                                if tag.upper().startswith("CVE-"):
                                    context["tested_cves"].append(tag.upper())
                    except json.JSONDecodeError:
                        continue
        except OSError:
            pass
    patterns_path = os.path.join(memory_dir, "patterns.jsonl")
    if os.path.isfile(patterns_path):
        try:
            with open(patterns_path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        context["patterns"].append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        except OSError:
            pass
    return context


def fetch_all_intel(techs: list[str], target: str) -> list[dict]:
    all_results: list[dict] = []
    for tech in techs:
        print(f"  {CYAN}[{tech}]{RESET} GitHub Advisory…")
        all_results.extend(fetch_github_advisories(tech))
        print(f"  {CYAN}[{tech}]{RESET} NVD…")
        all_results.extend(fetch_nvd_cves(tech))
    return all_results


def prioritize_intel(results: list[dict], memory: dict) -> dict:
    tested_endpoints = set(memory.get("tested_endpoints", []))
    tested_cves = set(memory.get("tested_cves", []))
    critical, high, info = [], [], []
    for r in results:
        sev = str(r.get("severity", "UNKNOWN")).upper()
        cve_id = r.get("id", "")
        already_tested = (
            cve_id.upper() in tested_cves if str(cve_id).upper().startswith("CVE") else False
        )
        entry = {**r, "already_tested": already_tested}
        if already_tested:
            entry["note"] = "Already tested in a previous hunt session."
            info.append(entry)
        elif sev == "CRITICAL":
            entry["note"] = "Untested critical vulnerability. Hunt candidate."
            critical.append(entry)
        elif sev == "HIGH":
            entry["note"] = "Untested high-severity finding. Priority target."
            high.append(entry)
        else:
            info.append(entry)
    critical.sort(key=lambda x: severity_order(x.get("severity", "UNKNOWN")))
    high.sort(key=lambda x: severity_order(x.get("severity", "UNKNOWN")))
    memory_context: dict = {}
    if memory.get("last_hunted"):
        memory_context["last_hunted"] = memory["last_hunted"]
    if memory.get("tech_stack"):
        memory_context["tech_stack"] = memory["tech_stack"]
    if memory.get("hunt_sessions"):
        memory_context["hunt_sessions"] = memory["hunt_sessions"]
    memory_context["tested_endpoints_count"] = len(tested_endpoints)
    memory_context["tested_cves_count"] = len(tested_cves)
    matching_patterns = []
    target_tech = {t.lower() for t in memory.get("tech_stack", [])}
    for pattern in memory.get("patterns", []):
        pattern_tech = {t.lower() for t in pattern.get("tech_stack", [])}
        if target_tech & pattern_tech:
            matching_patterns.append(
                {
                    "target": pattern.get("target", ""),
                    "technique": pattern.get("technique", ""),
                    "vuln_class": pattern.get("vuln_class", ""),
                    "payout": pattern.get("payout", 0),
                }
            )
    if matching_patterns:
        memory_context["matching_patterns"] = matching_patterns
    return {
        "critical": critical,
        "high": high,
        "info": info,
        "memory_context": memory_context,
        "total": len(results),
    }


def format_output(target: str, intel: dict) -> str:
    lines = [f"", f"{BOLD}INTEL: {target}{RESET}", f"{'═' * 50}", ""]
    for label, key in (("CRITICAL", "critical"), ("HIGH", "high")):
        items = intel.get(key, [])
        if not items:
            continue
        lines.append(f"{BOLD}{label}:{RESET}")
        for item in items[:15]:
            lines.append(f"  {item.get('id', '')} — {item.get('summary', '')[:120]}")
        lines.append("")
    lines.append(f"{DIM}Total: {intel['total']} (GitHub Advisory + NVD){RESET}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Infrastructure CVE intel")
    parser.add_argument("--target", required=True, help="Target hostname or domain")
    parser.add_argument("--tech", default="", help="Comma-separated keywords e.g. windows,kerberos")
    parser.add_argument("--memory-dir", default="", help="Hunt memory directory")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    techs = [t.strip() for t in args.tech.split(",") if t.strip()] if args.tech else []
    if not techs:
        techs = ["windows server", "active directory"]

    memory = load_memory_context(args.memory_dir, args.target)
    if memory.get("tech_stack"):
        for t in memory["tech_stack"]:
            if t.lower() not in [x.lower() for x in techs]:
                techs.append(t)

    print(f"\n{BOLD}Intel (AD edition){RESET}")
    print(f"Target: {CYAN}{args.target}{RESET}  Tech: {', '.join(techs)}\n")

    results = fetch_all_intel(techs, args.target)
    intel = prioritize_intel(results, memory)

    if args.json:
        print(json.dumps(intel, indent=2, default=str))
    else:
        print(format_output(args.target, intel))


if __name__ == "__main__":
    main()
