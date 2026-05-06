---
name: finding-validation
description: Use when validating an Active Directory finding before client or management delivery, or when triaging BloodHound edges, Kerberoast lists, or AD CS template visibility for false positives. Covers seven-question gates, AD-specific KILL/DOWNGRADE rules, narrative severity, and optional MITRE ATT&CK mapping. Improves pentest report defensibility.
---

# Finding Validation (internal)

**Evaluris Solutions**

## External references

- [engagement-reporting](../engagement-reporting/SKILL.md) — where validated findings land in the report  
- [docs/ad-glossary.md](../../docs/ad-glossary.md) — terms (Tier 0, ESC, delegation)

## Usage examples

1. **BloodHound path noise** — An edge shows `GenericAll` to a user, but no session exists; operator applies the AD-specific table and **DOWNGRADE**s to “hardening” unless a primitive is demonstrated in ROE.  
2. **Kerberoast without crack** — Service accounts have weak-looking SPNs but cracking is out of scope; finding is framed as **configuration exposure** with impact not demonstrated.  
3. **Enterprise SOC asks for ATT&CK** — After PASS, the operator attaches T1558.003 (verify current ID) only because Kerberoasting was **reproduced** with evidence.

## Troubleshooting

| Problem | What to do |
|---------|------------|
| Verdict stuck between CHAIN and multiple findings | Merge into one **CHAIN** narrative with a single blast-radius paragraph. |
| Customer rejects severity | Re-read Tier 0 / forest rubric; separate **demonstrated** vs **theoretical** impact. |
| MITRE ID outdated | Re-check [attack.mitre.org](https://attack.mitre.org/) for the assessment year; note version in appendix. |

## Before reporting a finding

1. **ROE** — Was every affected asset in scope?
2. **Replay** — Can another engineer reproduce with your steps?
3. **Evidence** — Logs, tickets, hashes (redacted), template names, ACL before/after?
4. **Impact** — What could an attacker actually do in production?
5. **Blast radius** — Single host, site, forest?
6. **Root cause** — Misconfig, weak process, or missing control?
7. **Remediation** — Actionable, owned, testable?

## Verdicts

| Verdict | Meaning |
|---------|---------|
| **PASS** | Report as-is |
| **KILL** | False positive, out of scope, or unproven — drop |
| **DOWNGRADE** | Lower severity or merge with another finding |
| **CHAIN** | Must document as multi-step path with single narrative |

## Common false positives

- Lab-only Kerberos tickets presented as production PoC  
- BloodHound edges without validation on target  
- “Possible” relay without constrained demo  

### AD-specific false positives (internal assessments)

| Situation | Often **KILL** or **DOWNGRADE** unless… |
|-----------|-------------------------------------------|
| **BloodHound path** exists but **no credential** or primitive can traverse it with current ROE | You document as *theoretical graph noise* or request expanded scope — do not sell as “exploitable” |
| **Kerberoast list** long but **no crackable** material in scope (strong passwords / no ROE to crack) | Report as *configuration exposure* with clear “impact not demonstrated” |
| **AD CS template** visible in `find` but **enrollment blocked** (ACL, CA policy, approval workflow) | DOWNGRADE to “hardening opportunity” unless you show a permitted enrollment proof |
| **Delegation flag** on object with **no path** to coerce or use a session | Tie to concrete session or ROE-approved demo |
| **LAPS readable** by group you cannot join or authenticate as | Note exposure of *who could* read — severity follows demonstrated read |
| **SQL linked-server** graph without auth to any hop | Same as BH — path vs proof |

## Severity rubric (AD — narrative)

Use alongside the customer risk model. Heuristic for **internal** discussion:

- **Higher** — Misconfiguration touches **Tier 0** (or equivalent crown-jewel) assets, **forest-wide** authentication trust (e.g. KRBTGT-adjacent scenarios, enterprise CA abuse with broad enrollment), or **many** principals in blast radius.
- **Medium** — Single-domain, **bounded** group or host set; requires **chaining** with creds you proved.
- **Lower** — **Theoretical** graph edges, **visible** but **blocked** enrollments, **informational** LDAP exposure without demonstrated misuse.

**CVSS** is optional for management summaries; the **narrative** (who, what forest, which trust) usually matters more for AD remediation prioritization.

---

## MITRE ATT&CK mapping (optional but best-in-class)

Enterprise and **blue-team** stakeholders often expect **technique IDs** alongside narrative severity. When you **PASS** a finding, add one row to an internal tracker:

| Your finding (examples) | ATT&CK tactic (illustrative) | Example technique / sub-technique IDs — **verify at [attack.mitre.org](https://attack.mitre.org/)** |
|-------------------------|------------------------------|--------------------------------------------------------------------------------------------------------|
| Kerberoast → cracked service | Credential Access | [T1558](https://attack.mitre.org/techniques/T1558/) Steal or Forge Kerberos Tickets — sub **.003** Kerberoasting |
| AS-REP roast | Credential Access | [T1558](https://attack.mitre.org/techniques/T1558/) — sub **.004** AS-REP Roasting |
| DCSync / replication abuse | Credential Access | [T1003](https://attack.mitre.org/techniques/T1003/) OS Credential Dumping — sub **.006** DCSync |
| NTLM relay / forced auth | Credential Access / Initial Access | [T1187](https://attack.mitre.org/techniques/T1187/) Forced Authentication; relay varies by scenario |
| AD CS certificate abuse | Credential Access | [T1649](https://attack.mitre.org/techniques/T1649/) Steal or Forge Authentication Certificate (verify wording per ATT&CK version) |
| Pass-the-ticket / forged tickets | Credential Access | [T1550](https://attack.mitre.org/techniques/T1550/) Use Alternate Authentication Material — sub **.003** Pass the Ticket |

**Rules:** Only map behaviors you **demonstrated**. Prefer **sub-techniques** when they exist. If ATT&CK renumbers, update the appendix — do not treat this table as canonical forever.

## Alignment

Use `/validate` and `tools/validate.py` for structured walkthrough.
