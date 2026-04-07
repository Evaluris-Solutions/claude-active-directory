---
name: ad-methodology
description: Active Directory penetration testing methodology — engagement phases, non-linear routing when stuck, tool selection by phase (recon vs creds vs escalation), session discipline, switching context when a path dead-ends, red team vs internal pentest pacing, OPSEC notes. Use when planning or unblocking an AD assessment. Kerberos, Windows domain, red team, pentest.
---

# AD Methodology — How to Run the Engagement

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae)

## Mindset

- **Authorized only** — ROE is the source of truth.
- **Graph + paths** — think in attack paths, not isolated tricks.
- **One crown jewel** per session — what would worst-case compromise look like for this client?

## Skill reading order (recommended path)

Use this as a **default navigation** order; loop back whenever a phase stalls.

1. **[ad-pentest](../ad-pentest/SKILL.md)** — ROE, phases, path-hunting mindset.
2. **[ad-recon](../ad-recon/SKILL.md)** — DNS/LDAP/SMB/Kerberos/BloodHound, trusts, spray gates.
3. **[ad-attack-classes](../ad-attack-classes/SKILL.md)** — Technique reference, lateral matrix, trust overview.
4. **[ad-arsenal](../ad-arsenal/SKILL.md)** — Tool patterns and telemetry awareness.
5. **[ad-cs-pki](../ad-cs-pki/SKILL.md)** — AD CS triage and evidence bundles.
6. **[finding-validation](../finding-validation/SKILL.md)** — Before client-facing write-up.
7. **[engagement-reporting](../engagement-reporting/SKILL.md)** — Structure and AD finding fields.

**Glossary:** [docs/ad-glossary.md](../../docs/ad-glossary.md)

## Five phases (loop freely)

1. **Orient** — Reread ROE, objectives, time box.
2. **Map** — Domain users, computers, trusts, interesting groups, AD CS, Tier-0 assets.
3. **Probe** — Low-noise checks first unless engagement allows noise (spray, scans).
4. **Prove** — Repeatable exploitation evidence for findings.
5. **Report** — Impact, likelihood, remediation, residual risk.

## Stuck? Quick table

| Symptom | Try |
|---------|-----|
| No creds | AS-REP, Kerberoast, LLMNR coerced capture (if allowed), misconfig ACLs from BloodHound |
| Creds but no path | Delegation, local admin reuse, GPO, certificate templates |
| BH graph empty | Collection method, scope of session, run from multiple hosts |
| Everything patched | Misconfig-only: ACLs, AD CS, delegation, password in description |
| **Trusts visible but no creds** | Trust-targeted **DNS/LDAP** (in-scope names only), document SID filtering / selective auth awareness; request customer-side session or jump box if blocked |
| **SQL in scope** | AD-joined **SQL** checks per [ad-attack-classes](../ad-attack-classes/SKILL.md) — instances, auth mode, linked servers; destructive probes only with explicit ROE |

## Tool routing (examples)

- **LDAP / users / groups** → ldapsearch, bloodyAD, windapsearch  
- **Sessions / SMB** → CrackMapExec  
- **Kerberos tickets** → getTGT/getST (Impacket), Rubeus  
- **AD CS** → Certipy, manual `certipy find` / `certipy req` per ROE  
- **Graph** → SharpHound → BloodHound  

## Session discipline

- Time-box noisy actions.
- Log your commands for the report appendix.
- When rotating off a host, note what was attempted so `/resume` stays useful.
