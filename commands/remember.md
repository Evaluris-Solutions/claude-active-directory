---
description: Log a technique, finding, or pattern to engagement memory for later reuse. Usage: /remember
---

# /remember

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/remember` |
| **ROE gate** | Do not log **classified** customer secrets or cleartext production passwords; follow data-handling in ROE. |
| **Outputs** | JSONL / markdown pattern entries via `memory/` modules or customer-approved `findings/` notes. |
| **Stop conditions** | If storage location is unclear → operator chooses customer-approved path before logging. |
| **Related** | [`memory/hunt_journal.py`](../memory/hunt_journal.py), [`commands/resume`](resume.md) |

Append structured entries for:

- **Technique** that worked (e.g. Certipy ESC1 on template X)
- **Environment** fingerprint (functional level, CA present)
- **Outcome** (severity, objective progress)

Use the memory API in `memory/hunt_journal.py` / `pattern_db.py` or maintain markdown in `findings/` per customer policy.

**Do not** store cleartext production passwords in the repo.
