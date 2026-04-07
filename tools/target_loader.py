#!/usr/bin/env python3
"""
Load in-scope AD targets from a JSON file — replaces public bug-bounty APIs.

Default file: targets/engagement_targets.json

Schema example:
{
  "targets": [
    {
      "name": "Customer A",
      "scope_domains": ["corp.local"],
      "notes": "ROE signed 2026-04-01"
    }
  ]
}
"""

from __future__ import annotations

import argparse
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PATH = os.path.join(BASE, "targets", "engagement_targets.json")


def load_targets(path: str = DEFAULT_PATH) -> list[dict]:
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        data = json.load(f)
    return data.get("targets", [])


def main() -> None:
    p = argparse.ArgumentParser(description="Load engagement targets from JSON")
    p.add_argument("--list", action="store_true")
    p.add_argument("--top", type=int, default=20)
    p.add_argument("--path", default=DEFAULT_PATH)
    args = p.parse_args()

    targets = load_targets(args.path)[: args.top]
    if args.list:
        for t in targets:
            name = t.get("name", "?")
            doms = t.get("scope_domains", [])
            print(f"  {name}: {', '.join(doms)}")
        print(f"Total: {len(targets)}")
    if not os.path.isfile(args.path):
        print(f"Create {args.path} to list customer domains.")


if __name__ == "__main__":
    main()
