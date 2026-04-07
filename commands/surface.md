---
description: Rank and prioritize Active Directory attack surface — high-value hosts, Tier-0 proximity, Kerberoastable accounts, AD CS CAs, delegation flags. Usage: /surface corp.local
---

# /surface

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
