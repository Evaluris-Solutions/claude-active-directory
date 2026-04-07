---
description: Rules of engagement — verify authorized domains, DCs, subnets, accounts, destructive actions, and exclusions before testing. Usage: /scope or /scope corp.local
---

# /scope

**Scope** here means **ROE** (rules of engagement), not a public bug bounty program.

## Checklist

- [ ] Written authorization on file (statement of work / letter)
- [ ] In-scope **domains** and **forests**
- [ ] In-scope **IP ranges** / **DC names**
- [ ] **Excluded** systems (production DB, OT, mailboxes, etc.)
- [ ] **Windows**: password spray **allowed or forbidden**
- [ ] **Destructive** tests (GPO change, mass lockout, production persistence) **allowed or forbidden**
- [ ] **Hours** / **maintenance windows** / SOC coordination

## Tooling

Use `python3 tools/roe_checker.py --target <host>` with `config.json` allow lists (see `config.example.json`).

## If unclear

**Stop** and clarify with the customer — do not “assume” scope.
