---
description: Validate an Active Directory finding for internal reporting — reproducibility, ROE, impact, evidence quality. Usage: /validate
---

# /validate

Run structured validation before anything goes to a client report.

## Gates

1. **ROE** — Finding only touches in-scope assets.
2. **Replay** — Steps are documented and repeatable.
3. **Evidence** — Commands/output (redacted) support the narrative.
4. **Impact** — Clear business/technical impact in AD terms.
5. **False positives** — Ruled out (e.g. lab ticket vs. production).

## Tool

```bash
python3 tools/validate.py
```

Outputs markdown under `findings/` for the engagement folder.

## Skill

See `skills/finding-validation/SKILL.md`.
