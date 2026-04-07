---
name: ad-recon
description: Active Directory reconnaissance — DNS and AD DNS, domain and forest trusts, LDAP anonymous and authenticated enumeration, SMB signing posture, password policy and spray approval gates, Kerberos pre-authentication and SPN discovery, BloodHound collection methods, LDAP filter cookbook for common goals. Authorized testing only. Pentest, LDAP, Kerberos, BloodHound, trust relationships.
---

# AD Reconnaissance

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae) — **authorized assessments only.**

**Related:** [ad-methodology](../ad-methodology/SKILL.md) · [ad-attack-classes](../ad-attack-classes/SKILL.md) · [Glossary](../../docs/ad-glossary.md)

---

## Preconditions

- **ROE** lists domain name(s), DCs or subnets, and whether anonymous/unauthenticated tests are allowed.
- **Trusts:** If multi-domain/forest is in scope, note which **direction** and **type** of trust testing is permitted.

---

## DNS

- Resolve DCs: `nslookup -type=SRV _ldap._tcp.dc._msdcs.<domain>`
- Zone transfers are rarely allowed; if denied, document and continue with other channels.
- Record **all** DC hostnames returned — Tier-0 proximity for reporting.

---

## Domain and forest trusts

Trusts change **where** authentication and credential material may flow.

| Enumerate | Why it matters |
|-----------|----------------|
| **Trust partners** (inbound / outbound) | Identifies extra domains to map in ROE |
| **Forest trusts** vs **external** | Different default security (e.g. SID filtering, selective auth) |
| **Trust direction** | Affects which domain’s accounts can authenticate where |
| **Transitivity** | Shortcut paths across the graph |

**Awareness (not a bypass guide):** **SID filtering** limits which security identifiers from a trusted forest are accepted. **Selective authentication** restricts which users from a trusted forest may access resources. These controls affect whether a theoretical cross-trust path is **actually exploitable** — validate in environment and document in the report.

When **trusts are visible but you have no creds yet**, prioritize LDAP/DNS against **each in-scope trusted name** once ROE allows, and note blind spots for the customer.

---

## Password policy and password spray

**Never spray without explicit written customer approval** and a documented **lockout policy**.

| Check | Action |
|-------|--------|
| Lockout threshold | Stay **below** threshold per user (typically **one attempt per user per window**; confirm `lockoutDuration` / `lockoutObservationWindow`) |
| Fine-grained password policies | May apply to different groups — enumerate if possible |
| Account lockout | Stop immediately if unexpected lockouts occur; notify customer per ROE |

Record **policy source** (default domain policy vs PSO) for the report appendix.

---

## LDAP — goals and filter cookbook

Substitute `<BASE_DN>` and bind credentials per engagement. Filters use standard LDAP syntax; verify **bitwise** flags against current Microsoft documentation if results look wrong.

| Goal | Filter pattern (illustrative) |
|------|--------------------------------|
| All users | `(objectClass=user)(objectCategory=person)` |
| Users with **SPN** (Kerberoast candidates) | `(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))` |
| **Pre-auth not required** (AS-REP roast candidates) | Bitwise `userAccountControl` match for `DONT_REQUIRE_PREAUTH` — use documented OID `1.2.840.113556.1.4.803` and the correct bitmask |
| **Computers** | `(objectClass=computer)` |
| **Unconstrained delegation** (computer trusted for delegation) | Bitwise `userAccountControl` match for `TRUSTED_FOR_DELEGATION` on computer objects |
| **Constrained delegation** fields | Inspect `msDS-AllowedToDelegateTo` on relevant principals |
| **RBCD** | Inspect `msDS-AllowedToActOnBehalfOfOtherIdentity` on computer objects |
| **Domain admins (example group)** | `(&(objectClass=user)(memberOf:1.2.840.113556.1.4.1941:=CN=Domain Admins,CN=Users,<BASE_DN>))` (adjust group DN) |

**Useful attributes** (non-exhaustive): `sAMAccountName`, `userPrincipalName`, `servicePrincipalName`, `userAccountControl`, `memberOf`, `msDS-AllowedToDelegateTo`, `msDS-AllowedToActOnBehalfOfOtherIdentity`, `whenCreated`, `lastLogonTimestamp`.

---

## SMB

- **Signing:** Note whether **required** or **enabled** on DCs, member servers, and workstations you are allowed to probe — affects **relay** hypotheses (often **off** for DCs; environment-specific).
- **Null session / guest** — often disabled; document result.
- Enumerate **shares** only on in-scope hosts and with approved accounts.

---

## Kerberos (no or low privilege)

- **Pre-auth disabled** → AS-REP roast candidate set (validate with LDAP + tooling).
- **SPNs on user accounts** → Kerberoast candidate set (TGS + offline crack workflow per ROE).

---

## BloodHound / SharpHound

| Collection | Noise / visibility | Credential need | When to use |
|----------|-------------------|-----------------|-------------|
| `DCOnly` | Lower than full | Often needs domain session | Quick graph of DC-resolvable data |
| `Default` / broader | Higher | Session typically required | Standard internal assessment |
| `All` | Highest | Session + ROE for stealth | Only when explicitly allowed |

If collectors are **blocked** (EDR, policy, no join): fall back to **manual LDAP goals** in this skill, document coverage gaps, and recommend customer-run collection if appropriate.

---

## Output

Store notes under `recon/<domain>/` — `tools/ad_recon.sh` creates a baseline layout; see `notes/ldap-goals.txt` for a checklist mirror.

---

## Safety

- Document every enumeration action for the final report.
- **Hybrid identity:** If the org syncs to Entra ID, passwords or lockout may also affect cloud sign-in — stay within ROE; see `ad-pentest` skill **Hybrid identity** note.
