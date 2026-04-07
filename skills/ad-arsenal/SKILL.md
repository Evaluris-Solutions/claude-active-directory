---
name: ad-arsenal
description: Active Directory toolkit patterns — NetExec and CrackMapExec, Impacket, Certipy, SharpHound, Windows Event IDs for SOC narratives, MITRE mapping pointers, OPSEC and telemetry. Lab versus production caution. Pentest, red team, Kerberos.
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

### Windows Event IDs (reporting hints — verify on target OS)

Use to enrich **detection / remediation** sections. IDs vary by auditing policy; **confirm** on the customer’s baseline.

| ID (common) | Category | Relevance |
|---------------|----------|-----------|
| **4768** | Kerberos AS-REQ success | Issued TGT — account activity |
| **4769** | Kerberos service ticket | TGS — includes Kerberoast-style request volume analysis |
| **4776** | NTLM (domain controller) | Credential validation |
| **5136** | Directory service object modified | ACL / attribute changes (e.g. sensitive writes) |
| **4886 / 4887 / 4888** (CA) | Certificate services | Enrollment and issuance audit (exact set depends on CA auditing) |

Cite **Microsoft** documentation for the **Windows Server** version in scope when arguing detectability.

---

## Task-oriented tool patterns

Placeholders: `DOMAIN`, `USER`, `PASS`, `DC`, `TARGET`, `SUBNET` — operator fills from ROE.

**NetExec** is the actively maintained successor to **CrackMapExec** in many environments; **command shapes are the same** (`netexec` vs `crackmapexec`). Use whichever binary the customer approves.

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

### SMB (NetExec / CrackMapExec)

```bash
netexec smb SUBNET -u USER -p 'PASS' --shares
netexec smb DC -u USER -p 'PASS' --pass-pol
# Equivalent: crackmapexec smb ...
```

### AD CS (Certipy)

```bash
certipy find -u USER@DOMAIN -p 'PASS' -dc-ip DC
# Many builds support a vulnerable-oriented view — see Certipy --help (e.g. -vulnerable) per version
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

## NetExec / CrackMapExec

- SMB auth, `--shares`, `--pass-pol` — lockout math on sprays; **same** module names across forks.

## Certipy

- `find` before `req`; document CA + template in every CS finding.

## BloodHound

- Ingest JSON; query paths to Tier 0 / DA / sensitive groups; **validate** edges you report.

## Always-rejected (engagement quality)

- Theoretical chains with no demo in scope  
- “Might be possible” without ticket/material  
- Out-of-scope hosts touched even once  

## References

- Microsoft AD security docs, BloodHound documentation, Certipy / SpecterOps **Certified Pre-Owned** lineage for ESC labels — see [ad-resources](../../docs/ad-resources.md).
