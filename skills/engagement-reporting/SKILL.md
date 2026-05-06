---
name: engagement-reporting
description: Use when writing or restructuring internal Active Directory penetration test or red team reports after findings exist. Guides executive summary, scope, AD-specific object fields, optional MITRE ATT&CK columns, evidence bundles, remediation, and narrative severity. Third-person reporting tone for Evaluris-style engagements.
---

# Engagement Reporting

**Evaluris Solutions**

## External references

- [finding-validation](../finding-validation/SKILL.md) — severity rubric and ATT&CK mapping table  
- [docs/ad-resources.md](../../docs/ad-resources.md) — curated links (MITRE, BloodHound, tools)

## Usage examples

1. **Post-assessment write-up** — After `/validate` PASS, the operator fills one finding section per AD CS template abuse with DN, CA FQDN, and redacted `certipy` output.  
2. **Executive + technical split** — A red team lead uses this skill to keep the executive summary free of SPN jargon while the technical appendix lists commands and Event IDs cited in [ad-arsenal](../ad-arsenal/SKILL.md).  
3. **Customer asks for ATT&CK** — The report appendix adds the optional technique column using IDs verified on [attack.mitre.org](https://attack.mitre.org/).

## Troubleshooting

| Problem | What to do |
|---------|------------|
| Finding reads like a blog, not a report | Re-anchor each claim to **evidence** bullets and customer **scope** section. |
| CVSS fights with narrative severity | Put CVSS in an optional management table; keep AD narrative (Tier 0 / forest) primary per [finding-validation](../finding-validation/SKILL.md). |
| Missing trust or forest context | Pull domain/forest/trust bullets from recon notes before publishing. |

## Structure

1. **Executive summary** — business risk, headline outcomes, no jargon overload.
2. **Scope and limitations** — what was tested, what was excluded, time window.
3. **Methodology** — high-level phases (recon, creds, escalation); tool names optional.
4. **Findings** — one section per finding:
   - Title, severity, CVSS (if used)
   - Affected systems / accounts / templates
   - **AD finding template (bullets)** — include where applicable:
     - **Distinguished Name (DN)** of the affected object(s) (user, computer, group, template, CA)
     - **Domain** and **forest** name (if known)
     - **Trust context** — inbound/outbound, partner DNS name, if the issue spans a trust boundary
     - **Replication / directory** notes — e.g. rights that replicate (`Replicating Directory Changes`), or **GPO** / **SYSVOL** path
     - **Template / CA** — template display name, CA FQDN, enrollment principals (for AD CS)
     - **ACL summary** — trustee and right type (e.g. `GenericAll`, enroll) without pasting full SDDL unless required
   - Description and impact (tie severity to [finding-validation](../finding-validation/SKILL.md) rubric: Tier 0 proximity, forest-wide auth impact vs single resource)
   - **Evidence** — commands, redacted output, screenshots
   - Remediation (specific: GPO, template, ACL, not “use strong passwords” alone)
5. **Roadmap** — quick wins vs structural fixes.
6. **Appendix** — command log if required; **MITRE ATT&CK mapping table** (optional — see [finding-validation](../finding-validation/SKILL.md)) when the customer expects detection-engineering alignment.

## Tone

- Professional, defensible, reproducible.
- No platform-specific “submission” language.

## Severity

Align with customer’s risk model; default to **impact × likelihood** in the domain context. For AD, prefer **narrative severity** (Tier 0 / forest / trust) per `finding-validation`; add **CVSS** only when the customer expects it.

### MITRE ATT&CK column (optional)

When included, each finding may add: **Tactic**, **Technique ID**, **Procedure** (one sentence: what was actually executed in scope). Keep IDs current with the ATT&CK release date in the report footer.
