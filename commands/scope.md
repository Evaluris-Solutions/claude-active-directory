---
description: Rules of engagement — verify authorized domains, DCs, subnets, accounts, destructive actions, and exclusions before testing. Usage: /scope or /scope corp.local
---

# /scope

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/scope` or `/scope <domain>` |
| **ROE gate** | **Canonical** — this command defines whether written authorization, allow lists, exclusions, spray, and destructive actions are confirmed. **Run before** `/recon`, `/hunt`, `/intel`, `/chain`, `/surface`, `/web3-audit`, or any intrusive testing. |
| **Outputs** | Checklist completion; optional `python3 tools/roe_checker.py` against `config.json`. |
| **Stop conditions** | Missing authorization or ambiguous exclusions → **halt** all engagement activity until clarified. |
| **Related** | [`skills/ad-pentest`](../skills/ad-pentest/SKILL.md), [`commands/recon`](recon.md), [`commands/hunt`](hunt.md) |

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
