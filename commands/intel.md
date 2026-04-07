---
description: Domain controller and Windows Server build intel — patch level, known abuse techniques relevant to version, planning prioritization. Usage: /intel corp.local
---

# /intel

## Purpose

Replace “CVE bounty intel” with **infrastructure intel**:

- DC OS build and patch level (from customer, WMI, or safe enum per ROE)
- Known issues for that **build** (e.g. Zerologon era — verify patch state)
- Elevation of privilege **patches** vs. **misconfiguration** focus

## Tools

```bash
python3 tools/learn.py --target <domain>
python3 tools/intel_engine.py --target <domain>
```

Adapt outputs to **your** engagement — scripts provide structure, not live Microsoft feeds by default.

## Memory

Cross-engagement patterns live in `memory/pattern_db.py` (technique + environment).
