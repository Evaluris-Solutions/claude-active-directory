---
description: Active Directory reconnaissance — DNS SRV/LDAP DC discovery, LDAP user and group enumeration, Kerberos pre-auth and AS-REP candidates, SPN discovery for Kerberoasting, SMB signing and null session policy, password policy, trust relationships, BloodHound/SharpHound collection prep. Requires ROE. Usage: /recon corp.local
---

# /recon

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/recon <domain.fqdn>` |
| **ROE gate** | **Requires** confirmed `/scope` (or equivalent written ROE): domain, DCs/subnets, exclusions, anonymous LDAP if used. No out-of-scope enumeration. |
| **Outputs** | `recon/<domain>/` folder notes, DNS/LDAP/Kerberos/BH prep artifacts per skill. |
| **Stop conditions** | Zone transfer or intrusive scan denied by policy → document and continue only with allowed methods. |
| **Related** | [`skills/ad-recon`](../skills/ad-recon/SKILL.md), [`commands/scope`](scope.md) |

Authorized **domain** reconnaissance — not internet subdomain mass-scanning unless the ROE defines that.

## Preconditions

1. Confirm **written ROE** — domain FQDN, DCs or IP ranges, exclusions.
2. Create `recon/<domain>/` for notes and tool output.

## Phase 1 — DNS

- Resolve domain controllers: `_ldap._tcp.dc._msdcs.<domain>` SRV records.
- Note any non-standard management hostnames only if in scope.

## Phase 2 — LDAP / RPC

- Enumerate users, groups, computers (tooling: ldapsearch, windapsearch, bloodyAD, rpcclient — per your toolchain).
- Extract: `servicePrincipalName`, `userAccountControl`, interesting group memberships.

## Phase 3 — Kerberos (no creds / low priv)

- Users **without** pre-auth → AS-REP roast candidates.
- SPNs on user accounts → Kerberoast list.

## Phase 4 — BloodHound

- Plan SharpHound or bloodhound-python collection when you have session/creds allowed by ROE.
- Store zip/JSON under `recon/<domain>/bloodhound/`.

## Phase 5 — Document

- Password policy, lockout threshold (for later spray decisions).
- Summary table: DCs, CA hosts if visible, Tier-0 hints.

## Optional script

`./tools/ad_recon.sh <domain>` creates directory layout and prints baseline checks.
