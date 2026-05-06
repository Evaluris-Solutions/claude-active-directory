---
description: Rank and prioritize Active Directory attack surface — high-value hosts, Tier-0 proximity, Kerberoastable accounts, AD CS CAs, delegation flags. Usage: /surface corp.local
---

# /surface

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/surface <domain>` (domain aligns engagement notes) |
| **ROE gate** | Prioritization must not **drive** testing of excluded Tier-0 or out-of-scope forests; `/scope` must allow the ranked targets. |
| **Outputs** | Ranked host/user/template list with rationale; optional `tools/mindmap.py` hints. |
| **Stop conditions** | Graph data stale or from wrong session → refresh recon first. |
| **Related** | [`skills/ad-methodology`](../skills/ad-methodology/SKILL.md), [`commands/recon`](recon.md) |

Prioritize **where to spend time** after recon and partial collection.

## Inputs

- BloodHound paths (shortest to DA / sensitive groups)
- List of Tier-0 assets from customer
- Your own notes: SPN density, old OS versions, extra forests

## Output

- Top 5 hosts/users/templates to investigate  
- Rationale tied to engagement objectives  

## Tool hint

`python3 tools/mindmap.py --domain <domain>` emits prioritized AD TTP reminders (text).
