---
name: engagement-reporting
description: Internal penetration test and red team report writing for Active Directory engagements — executive summary, scope and limitations, methodology, findings with severity and CVSS where appropriate, evidence bundles, remediation, prioritized fix order, timeline. Not bug bounty platform format. Pentest report, AD assessment.
---

# Engagement Reporting

**Evaluris Solutions**

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
6. **Appendix** — command log if required.

## Tone

- Professional, defensible, reproducible.
- No platform-specific “submission” language.

## Severity

Align with customer’s risk model; default to **impact × likelihood** in the domain context. For AD, prefer **narrative severity** (Tier 0 / forest / trust) per `finding-validation`; add **CVSS** only when the customer expects it.
