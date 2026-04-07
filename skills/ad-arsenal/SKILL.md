---
name: ad-arsenal
description: Active Directory offensive toolkit patterns — Impacket examples, CrackMapExec one-liners, Certipy workflow hints, SharpHound, secretsdump patterns, OPSEC and event log awareness, lab versus production caution. No exploit code delivery; operator supplies tools. Pentest, red team, Kerberos.
---

# AD Arsenal — Patterns and OPSEC

**Evaluris Solutions**

## Principles

- Prefer **documented, repeatable** command lines for the report appendix.
- **Production**: assume EDR/SIEM; noisy techniques need explicit approval.
- **Lab**: still practice safe credential handling — no real user passwords in git.

## OPSEC and telemetry (awareness, not evasion)

Customers often ask **what will show up in logs**. Typical classes:

| Activity class | Often logged (examples) |
|----------------|-------------------------|
| **Kerberos** | AS/TGS requests, pre-auth failures, unusual SPN requests, constrained delegation S4U |
| **LDAP** | Binds, searches with broad filters, anonymous bind attempts (if enabled) |
| **SMB** | Auth success/failure, share enumeration, PsExec-style patterns |
| **Certificate enrollment** | CA database entries, event logs on CA and DC, web enrollment IIS logs |

This is **not** an EDR evasion guide — use it to **set expectations** in kickoff and in the report **detection** subsection.

Task-oriented **patterns** (placeholders: `DOMAIN`, `USER`, `PASS`, `DC`, `TARGET` — operator fills from ROE).

### Kerberos tickets (Impacket / Rubeus on host)

```bash
# TGT — example pattern only
getTGT.py DOMAIN/USER:PASS -dc-ip DC

# Service ticket — example pattern only
getST.py DOMAIN/SVC -spn cifs/TARGET.DOMAIN -dc-ip DC -k -no-pass
```

### LDAP enumeration

```bash
ldapsearch -x -H ldap://DC -D "USER@DOMAIN" -w 'PASS' -b "DC=domain,DC=local" \
  "(servicePrincipalName=*)" sAMAccountName servicePrincipalName
```

Adapt filters to the [ad-recon](../ad-recon/SKILL.md) cookbook (SPN, `DONT_REQUIRE_PREAUTH`, delegation bits).

### SMB (CrackMapExec / enum)

```bash
crackmapexec smb SUBNET -u USER -p 'PASS' --shares
crackmapexec smb DC -u USER -p 'PASS' --pass-pol
```

### AD CS (Certipy)

```bash
certipy find -u USER@DOMAIN -p 'PASS' -dc-ip DC
# Template-specific requests only with explicit ROE
certipy req -u USER@DOMAIN -p 'PASS' -dc-ip DC -ca 'CA_NAME' -template TEMPLATE_NAME
```

### Graph (BloodHound)

- **SharpHound** (Windows): run with collection flags per [ad-recon](../ad-recon/SKILL.md) table; ingest to BloodHound CE.
- **bloodhound-python**: equivalent flags from a Linux jump box when allowed.

### Dumps / secrets (high sensitivity)

- `secretsdump.py`, `ticketer.py` — **lab or explicit customer authorization**; chain to [finding-validation](../finding-validation/SKILL.md) before reporting Golden/Silver scenarios.

---

## Impacket (suite reminder)

- `GetADUsers.py`, `GetUserSPNs.py`, `GetNPUsers.py`, `secretsdump.py`, `ticketer.py` — authorized domains only.

## CrackMapExec

- SMB auth, `--shares`, `--pass-pol` — lockout math on sprays.

## Certipy

- `find` before `req`; document CA + template in every CS finding.

## BloodHound

- Ingest JSON; query paths to Tier 0 / DA / sensitive groups; **validate** edges you report.

## Always-rejected (engagement quality)

- Theoretical chains with no demo in scope  
- “Might be possible” without ticket/material  
- Out-of-scope hosts touched even once  

## References

- Microsoft AD security docs, BloodHound documentation, CERTipy ESC matrix (community).
