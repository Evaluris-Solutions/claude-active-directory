---
name: finding-validation
description: Validate Active Directory penetration test findings before client delivery — reproducibility, scope membership, blast radius in forest, false positive elimination, whether misconfiguration vs missing patch, evidence completeness. Seven-question style gate adapted for internal assessments. Pentest quality, AD findings.
---

# Finding Validation (internal)

**Evaluris Solutions**

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

## Alignment

Use `/validate` and `tools/validate.py` for structured walkthrough.
