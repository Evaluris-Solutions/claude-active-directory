---
name: ad-cs-pki
description: Use when triaging or reporting authorized Active Directory Certificate Services risk—enterprise CA inventory, template permissions, ESC1–ESC11 style labels from Certipy-style tools, DC certificate mapping and strong-binding evidence, web enrollment and RPC relay surfaces. Use with /web3-audit command content and evidence tables before claiming production-wide impact.
---

# AD CS / PKI

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae)

## External references

- [docs/ad-resources.md](../../docs/ad-resources.md) — Certified Pre-Owned lineage, Certipy wiki, Microsoft PKI hardening  
- [finding-validation](../finding-validation/SKILL.md) — false positives when enrollment is blocked

## Usage examples

1. **First CA pass** — Operator runs `certipy find` (or equivalent), archives **redacted** output, fills ESC row in evidence bundle for any template flagged enrollable.  
2. **ESC10 discussion** — Assessor samples `StrongCertificateBindingEnforcement` / `CertificateMappingMethods` on two DCs, documents values only for in-scope hosts.  
3. **Web enrollment** — Burp MCP is used only where HTTP scope exists; screenshots redact session cookies.

## Troubleshooting

| Problem | What to do |
|---------|------------|
| Tool shows ESC* but enrollment fails | Treat as [finding-validation](../finding-validation/SKILL.md) “enrollment blocked” path; capture ACL or workflow denial. |
| ESC numbering differs from blog post | Trust **your tool version’s label**; cite version string in appendix. |
| **ESC12 / ESC13** labels appear in newer releases | Record the label and vendor reference your build prints; community numbering extends past ESC11 — update glossary when your team standardizes on definitions. |

## Why it matters

Misconfigured templates, **weak certificate-to-account mapping**, and **exposed enrollment interfaces** are common **high-impact** paths to domain-authenticating credentials. Community tooling groups scenarios under **ESC1–ESC11** (and beyond in some forks); labels evolve — **cite the tool version and SpecterOps / Certipy references** in your appendix.

## Enumeration

- **CA hosts**, enrollment endpoints (**RPC**, **HTTP/HTTPS web enrollment**, optional **ICertPassage**-style interfaces per environment).
- **Certipy** `find` (often with vulnerability-oriented flags per version): template display name, **EKU**, `ENROLLEE_SUPPLIES_SUBJECT`, **template flags** (e.g. `NO_SECURITY_EXTENSION` when present), **owner**, **enrollment rights**, and **CA-level** flags when reported.
- **Domain controllers:** evidence for **certificate mapping** and **strong binding** policy (registry / GPO) when your scenario depends on it — record **values**, not exploitation steps (see evidence table for ESC9/ESC10).
- **BloodHound / graph:** optional cross-check for certificate-related edges when the customer allows collection.

## ESC matrix (conceptual)

Map findings to the ESC label your toolchain reports; **validate** impact in a **lab** or with **explicit customer authorization** before claiming production-wide compromise.

| Label | High-level theme |
|-------|------------------|
| **ESC1–2** | Dangerous templates (e.g. enrollee-supplied subject / SAN), enrollment agent chains |
| **ESC3** | Enrollment agent templates and “on behalf of” relationships |
| **ESC4** | Vulnerable ACLs or ownership on templates or CA objects |
| **ESC5** | Offline / alternate publishing or trust to CA material |
| **ESC6** | CA-level settings enabling weak issuance paths |
| **ESC7** | Web enrollment and other HTTP(S) enrollment UIs |
| **ESC8** | NTLM relay to HTTP(S) enrollment or similar **web** surfaces |
| **ESC9** | Templates with **NO_SECURITY_EXTENSION** (or equivalent) interacting with **mapping** and **strong binding** posture |
| **ESC10** | **Weak certificate mapping** — DC **`CertificateMappingMethods`**, **`StrongCertificateBindingEnforcement`**, and related policy (see Microsoft security updates and KBs for the engagement’s OS level) |
| **ESC11** | **NTLM relay to AD CS RPC** — CA **interface** encryption flags (e.g. `IF_ENFORCEENCRYPTICERTREQUEST` / `certutil` policy views); record whether RPC enrollment **requires encryption** |

Always cite **template name**, **CA FQDN**, **principals who can enroll**, and **measured policy values** in the report.

## Web enrollment

HTTP attack surface may justify **Burp MCP** from this plugin’s optional integration — only in scope.

## Reporting

Include: affected CA, templates, principals who can enroll, remediation (disable template, ACL fix, HSM, etc.).

---

## Evidence bundle (per ESC category — names only)

Align triage with **Certipy-style** `find` / `req` workflows. Record **facts**, not exploit recipes. Map each scenario to the ESC label the team agrees on (community naming evolves — cite your reference version in the appendix).

| ESC (label) | Record in the bundle |
|-------------|----------------------|
| **ESC1** | Template **display name** and LDAP name; issuing **CA FQDN**; principals with **enroll** / **auto-enroll**; **EKU** summary (e.g. client auth); **`ENROLLEE_SUPPLIES_SUBJECT`** yes/no; **redacted** enrollment or CSR output (no private key); **screenshot** of template security / GUI if allowed |
| **ESC2** | Same core fields; note **any** enrollment agent or “on behalf of” chain visible in template or CA policy |
| **ESC3** | Enrollment agent template + **who** holds agent rights; target template relationship |
| **ESC4** | **ACL** or ownership change path on template or CA object; **before/after** descriptor summary (redacted) |
| **ESC5** | **Offline** or **publishing** path if applicable; file share / registry evidence per your validated scenario |
| **ESC6** | CA-level **flag** or setting evidence (name the attribute/flag as shown in tooling output); who can request affected templates |
| **ESC7** | **Web enrollment** or alternate **interface** surface; URL, auth mode, and **request** flow summary |
| **ESC8** | **HTTP(S)** endpoint to CA; relay **prerequisites** you actually demonstrated (listener, signing, channel); redacted capture only |
| **ESC9** | Template shows **NO_SECURITY_EXTENSION** (or tooling-equivalent); plus **DC mapping / strong binding** evidence (registry keys or policy export **redacted**); screenshot of template flags |
| **ESC10** | **CertificateMappingMethods** / **StrongCertificateBindingEnforcement** (or successor settings) on **DCs** — document **which DCs** sampled and **values**; tie to Microsoft guidance version for the forest functional level |
| **ESC11** | **CA RPC** / **ICertPassage** posture: **InterfaceFlags** / encryption requirement for certificate requests; prove **interface exposure** only in scope; redacted `certutil -getreg` / CA-policy excerpts |

### Redaction and repo hygiene

- **Never** store private keys, full `.pfx`, or decryptable ticket blobs in the repo or client-shared drives without encryption policy.
- In reports: **truncate** hashes and ticket excerpts; reference **file hashes** for evidence archives instead of pasting secrets.
- Prefer **screenshots** of dialogs with sensitive fields blurred over raw PEM in the body.

## `/web3-audit` command

The slash command file is named `web3-audit.md` for install compatibility; it drives **this** PKI workflow, not smart contracts.
