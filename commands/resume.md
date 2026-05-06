---
description: Resume a previous Active Directory engagement — read journal, recon folder, and untested paths. Usage: /resume corp.local
---

# /resume

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/resume <domain>` |
| **ROE gate** | Reload **current** `/scope` — scope may have changed since last session; do not assume old ROE. |
| **Outputs** | Pending vs completed techniques; journal continuity from `memory/`. |
| **Stop conditions** | Journal missing or corrupted → reconcile with customer before continuing intrusive work. |
| **Related** | [`commands/remember`](remember.md), [`skills/ad-methodology`](../skills/ad-methodology/SKILL.md) |

## Steps

1. Open `memory/` JSONL journals and last `recon/<domain>/` timestamps.
2. List **completed** vs **pending** techniques from engagement notes.
3. Reload ROE — scope may have been updated.

## Tools

Engagement logging uses `memory/hunt_journal.py` (JSONL). Align entries with current `schemas.py`.

## Goal

Zero duplicate work; clear handoff between sessions.
