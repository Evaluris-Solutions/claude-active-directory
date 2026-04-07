---
name: active-directory
description: Claude Active Directory — authorized AD offensive security master skill. ROE, recon, Kerberos and NTLM, coercion awareness, delegation and ACL abuse, AD CS ESC1–ESC11, lateral movement, MITRE-ready validation and reporting. Evaluris Solutions, pentest, red team.
---

# Claude Active Directory (root skill)

This file mirrors the master workflow in [`skills/ad-pentest/SKILL.md`](skills/ad-pentest/SKILL.md). Install copies skills into `~/.claude/skills/` via `./install.sh`.

**Author:** Evaluris Team · **[Evaluris Solutions](https://evaluris.ae)**

---

# Active Directory — Master Engagement Workflow

**Claude Active Directory** by [Evaluris Solutions](https://evaluris.ae) — **Evaluris Team**. For **authorized testing only** — written ROE before any action.

## The question that matters

> **"Given explicit authorization, can we demonstrate impact (credential exposure, privilege escalation, domain compromise path) with reproducible evidence — without exceeding ROE?"**

If the answer is no (out of scope, no proof, or theoretical only) — **stop** and document why.

---

## Critical rules

1. **ROE first** — authorized domains, DCs, subnets, windows, destructive vs read-only.
2. **No unauthorized systems** — exclusions are absolute.
3. **Evidence** — every claim needs command output, screenshot, or log reference.
4. **Validate before the client report** — use `/validate` and `finding-validation` skill.
5. **Minimize harm** — prefer non-destructive techniques unless the engagement allows.
6. **OPSEC** — be aware of event logs, EDR, and SOC; document what telemetry your actions may generate.

---

## Engagement phases (non-linear)

| Phase | Focus |
|-------|--------|
| **Plan** | ROE, objectives, stealth vs noisy tradeoffs, tool inventory |
| **Recon** | DNS, LDAP, SMB signing, user enum, Kerberos pre-auth, SPNs, password policy, BloodHound collection |
| **Credential access** | Spray (if allowed), AS-REP roast, Kerberoast, LLMNR/NBT-NS, captured hashes |
| **Escalation** | Delegation, ACLs (`GenericAll`, `WriteDACL`), GPP/cPassword, misconfigured templates |
| **AD CS** | Template analysis, ESC patterns, Certipy-style checks |
| **Lateral** | WMI, PSRemoting, SMB, scheduled tasks — within ROE |
| **Objective** | Document paths to crown jewels (DA, EA, sensitive groups) |
| **Report** | Executive + technical + remediation |

Deep methodology: **`skills/ad-methodology/SKILL.md`**. Recon detail: **`skills/ad-recon/SKILL.md`**. Attacks: **`skills/ad-attack-classes/SKILL.md`**.

---

## Skill map (when to open which file)

| Skill | Open when… |
|-------|------------|
| [ad-methodology](skills/ad-methodology/SKILL.md) | Planning phases, stuck routing, session discipline |
| [ad-recon](skills/ad-recon/SKILL.md) | Trusts, LDAP cookbook, SMB signing, BloodHound collection choice, spray approval gates |
| [ad-attack-classes](skills/ad-attack-classes/SKILL.md) | Technique names, lateral protocol matrix, LAPS/RBCD/trust/SQL pointers, ticket sensitivity |
| [ad-arsenal](skills/ad-arsenal/SKILL.md) | Concrete tool invocation patterns, OPSEC / log categories |
| [ad-cs-pki](skills/ad-cs-pki/SKILL.md) | Enterprise CA, templates, ESC-labeled evidence bundles |
| [finding-validation](skills/finding-validation/SKILL.md) | Before reporting — AD false positives, severity rubric |
| [engagement-reporting](skills/engagement-reporting/SKILL.md) | Report structure and AD-specific finding fields |
| [Glossary](docs/ad-glossary.md) | Term definitions (TGT/TGS, delegation, Tiering, ESC, …) |
| [ad-resources](docs/ad-resources.md) | Curated external links |

### Hybrid identity (one paragraph)

**Microsoft Entra ID** (cloud) sync and hybrid join **do not replace** on-premises Active Directory testing for engagements scoped to the **Windows Server AD forest**. Password writeback, cloud-only passwords, and cloud session issuance can change **where** credentials are validated and **which** surfaces appear in scope — but methodology here stays **on-prem AD** unless the ROE explicitly expands. Do not add an Azure/Entra pentest chapter to this plugin; note hybrid **context** in kickoff and in the report scope section only.

---

## A → B → C path hunting (domain)

When you confirm technique A, hunt for B and C on the same engagement:

| Signal A | Often leads to B | Escalate to C |
|----------|------------------|---------------|
| AS-REP roastable users | Cracked passwords | Lateral spray / RDP / SMB |
| Kerberoastable SPNs | Cracked service accounts | New sessions, local admin |
| Unconstrained delegation host | Coerced auth to that host | TGT misuse (within lab/ROE) |
| RBCD / constrained misconfig | Machine account abuse | Resource compromise |
| Weak AD CS template | Cert request as user/machine | Authenticated session as higher principal |
| ACL (`GenericAll` on user) | Shadow credentials / reset | Domain escalation path |

---

## Tooling (illustrative)

| Category | Examples |
|----------|----------|
| Enumeration | ldapsearch, rpcclient, NetExec / CrackMapExec, windapsearch, bloodyAD |
| Kerberos | Impacket suite, Rubeus (Windows), Certipy (AD CS) |
| Graph | SharpHound / BloodHound CE, bloodhound-python |
| Relay | ntlmrelayx, mitm6 (only with authorization) |

Scripts in this repo **check** for binaries and structure output; they do not replace operator skill.

---

## Reporting and deliverable standards

- **`skills/engagement-reporting/SKILL.md`** — structure, AD object fields, optional **MITRE ATT&CK** appendix.
- **`skills/finding-validation/SKILL.md`** — validation gates and **ATT&CK** mapping (verify IDs on [attack.mitre.org](https://attack.mitre.org/)).
- **AD CS** — cover **ESC1–ESC11** when tooling reports them; see **`skills/ad-cs-pki/SKILL.md`**.

Internal / red-team style: scope, methodology, findings with severity, evidence, remediation.

---

## License / attribution

MIT — Evaluris Solutions. [https://evaluris.ae](https://evaluris.ae)
