---
name: ad-attack-classes
description: Active Directory attack techniques — Kerberoasting, AS-REP roasting, Golden and Silver tickets (lab sensitivity), unconstrained and constrained delegation and RBCD, ACL abuse, DCSync prerequisites, NTLM relay concepts, LAPS, shadow credentials, GPP, trust paths, AD-joined SQL lateral pivot, lateral movement protocol matrix. For authorized pentest and red team. Kerberos, NTLM, delegation, ACL, lateral movement.
---

# AD Attack Classes (reference)

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae) — **authorized use only.**

**Related:** [ad-recon](../ad-recon/SKILL.md) · [ad-cs-pki](../ad-cs-pki/SKILL.md) · [ad-arsenal](../ad-arsenal/SKILL.md) · [Glossary](../../docs/ad-glossary.md)

---

## Credential access

| Technique | Notes |
|-----------|--------|
| **AS-REP roast** | Users without Kerberos pre-auth; crack material offline per ROE |
| **Kerberoast** | Request TGS for user-backed SPNs; crack offline |
| **Spray** | Only with **written approval** and lockout policy math |
| **NTLM capture** | Responder / IPv6 / coercion families — **scope and stealth** per ROE |
| **Coercion → auth** | Often paired with relay or delegation abuse; document each hop |

---

## Privilege escalation (domain context)

| Technique | Notes |
|-----------|--------|
| **Unconstrained delegation** | Sensitive on compromised hosts; TGT visibility assumptions |
| **Constrained / S4U2** | Service-to-user delegation; validate KB and tooling version |
| **RBCD** | `msDS-AllowedToActOnBehalfOfOtherIdentity`; machine account scenarios |
| **ACL abuse** | `GenericAll`, `WriteDACL`, reset password, force password change, add to group |
| **DCSync** | Requires `Replicating Directory Changes` rights — evidence = who holds them |
| **Shadow credentials** | Evidence: ability to write target key trust material; report **what was writable**, not raw keys |
| **LAPS** | Enumeration: who can read LAPS passwords; abuse = possession of that read right |
| **Machine account quota** | Creating machine accounts for RBCD / delegation chains — ROE for object creation |
| **GPP / SYSVOL** | Legacy `Groups.xml` style credentials in SYSVOL — cite path + redacted proof |

---

## Golden and Silver tickets (sensitivity)

**Laboratory and mature-assessment only** unless the customer explicitly authorizes ticket forgery scenarios. These techniques are **highly destructive to trust** in detection narratives and are often **indistinguishable from advanced adversary activity**.

- Do **not** treat them as default “next steps” after local admin.
- If used in a lab, document **KRBTGT** / service key source assumptions and **recovery** expectations.

---

## Trust and cross-domain paths (on-prem)

Cross-domain attacks depend on **trust type**, **direction**, **SID filtering**, and **selective authentication**. Typical artifacts:

- **Inter-realm TGT** when moving between realms in the same forest (conceptual).
- **Foreign principals** in groups — follow membership across domains **only** where ROE permits.

Stay within **on-prem AD** scope; hybrid cloud identity is a **context** note only (see `ad-pentest`).

---

## Lateral movement — protocol matrix

No step-by-step exploitation; use for **planning and reporting** (prereqs and ROE).

| Protocol | Typical prerequisites | Firewall / exposure | ROE note |
|----------|----------------------|----------------------|----------|
| **WinRM (5985/5986)** | Creds; often admin on target | May be restricted | Confirm destructive cmd execution allowed |
| **SMB (445)** | Creds; share access or admin | Often open internally | Signing may block relay **to** that host |
| **WMI (RPC)** | Creds; admin common | RPC filters vary | Noisy; document |
| **DCOM** | Creds; specific CLSIDs | Per-app | Scope app servers explicitly |
| **RDP (3389)** | Creds; interactive | Highly visible | Screen recording / customer rules |

---

## Credential reuse patterns (reporting narrative)

| Pattern | What to document |
|---------|------------------|
| **Same password / local admin reuse** | Host list, hash or password proof (redacted), blast radius |
| **Service account reuse** | SPN → cracked cred → where it was replayed |
| **Session reuse** | Ticket or session type; time window; hosts touched |

---

## AD-joined Microsoft SQL Server (lateral pivot)

When **in scope** and **authorized**:

- **Identity:** SQL runs as domain account or virtual accounts; linked servers may store **delegated** trust to other DBs.
- **Enumeration:** Instance name, auth mode, linked server names (read-only where possible).
- **Destructive** actions (`xp_cmdshell`, job creation) — **explicit ROE** only.

If SQL is out of scope, record **“SQL not tested”** in methodology.

---

## AD CS (detail)

See **[ad-cs-pki](../ad-cs-pki/SKILL.md)** for ESC categories and **evidence bundles**.

---

## Persistence (awareness)

Document for **impact** and **detectability**; implement only if engagement permits.

---

## Chaining

Use `/chain` mindset: each confirmed primitive should suggest the **next edge** on the path to the stated objective (e.g. Tier 0, crown-jewel application).
