---
description: Quick go/no-go on a suspected AD finding before deep validation. Usage: /triage
---

# /triage

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/triage` |
| **ROE gate** | First check: asset **in scope** per `/scope`; drop if not. |
| **Outputs** | Pursue / Park / Drop decision for the operator. |
| **Stop conditions** | Theoretical-only → **Drop**; do not spend deep time without `/scope` alignment. |
| **Related** | [`skills/finding-validation`](../skills/finding-validation/SKILL.md), [`commands/validate`](validate.md) |

Fast triage — is this worth full `/validate`?

## 2-minute checks

- Is the asset **in ROE**?
- Is the technique **demonstrated** or only theoretical?
- Does it require **chain** documentation with other issues?

## Outcomes

- **Pursue** — schedule full validation and evidence capture.
- **Park** — needs more access or time-boxed slot.
- **Drop** — out of scope, duplicate, or unprovable.

Use `skills/finding-validation/SKILL.md` for criteria.
