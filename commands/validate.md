---
description: Validate an Active Directory finding for internal reporting — reproducibility, ROE, impact, evidence quality. Usage: /validate
---

# /validate

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/validate` |
| **ROE gate** | Finding must reference **in-scope** assets only; re-check scope if asset identity is unclear. |
| **Outputs** | Markdown under `findings/` via `tools/validate.py`; verdict PASS/KILL/DOWNGRADE/CHAIN. |
| **Stop conditions** | Insufficient evidence → KILL or PARK until replayable steps exist. |
| **Related** | [`skills/finding-validation`](../skills/finding-validation/SKILL.md), [`commands/triage`](triage.md) |

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
