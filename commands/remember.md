---
description: Log a technique, finding, or pattern to engagement memory for later reuse. Usage: /remember
---

# /remember

Append structured entries for:

- **Technique** that worked (e.g. Certipy ESC1 on template X)
- **Environment** fingerprint (functional level, CA present)
- **Outcome** (severity, objective progress)

Use the memory API in `memory/hunt_journal.py` / `pattern_db.py` or maintain markdown in `findings/` per customer policy.

**Do not** store cleartext production passwords in the repo.
