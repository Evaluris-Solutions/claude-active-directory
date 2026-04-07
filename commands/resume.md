---
description: Resume a previous Active Directory engagement — read journal, recon folder, and untested paths. Usage: /resume corp.local
---

# /resume

## Steps

1. Open `memory/` JSONL journals and last `recon/<domain>/` timestamps.
2. List **completed** vs **pending** techniques from engagement notes.
3. Reload ROE — scope may have been updated.

## Tools

Engagement logging uses `memory/hunt_journal.py` (JSONL). Align entries with current `schemas.py`.

## Goal

Zero duplicate work; clear handoff between sessions.
