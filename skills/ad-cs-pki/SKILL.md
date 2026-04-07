---
name: ad-cs-pki
description: Active Directory Certificate Services — enterprise CA, certificate templates, enrollment permissions, ESC1 through ESC8 abuse patterns, Certipy-oriented triage, web enrollment surface, overlap with AD FS. For authorized security assessments. AD CS, PKI, certificate templates, pentest.
---

# AD CS / PKI

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae)

## Why it matters

Misconfigured templates and enrollment permissions are common **high-impact** paths to domain authentication material.

## Enumeration

- CA hosts, enrollment endpoints (RPC, web), template list.
- **Certipy** `find` output: template name, EKU, `ENROLLEE_SUPPLIES_SUBJECT`, owner, enrollment rights.

## ESC matrix (conceptual)

Map findings to published ESC categories; validate in lab before claiming production impact.

- **ESC1** — misconfigured templates allowing arbitrary SAN / enrollee supplies subject  
- **ESC3/4/8** — agent/template/relay contexts per current research  
- Always cite **template name**, **CA**, and **evidence** in the report.

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

### Redaction and repo hygiene

- **Never** store private keys, full `.pfx`, or decryptable ticket blobs in the repo or client-shared drives without encryption policy.
- In reports: **truncate** hashes and ticket excerpts; reference **file hashes** for evidence archives instead of pasting secrets.
- Prefer **screenshots** of dialogs with sensitive fields blurred over raw PEM in the body.

## `/web3-audit` command

The slash command file is named `web3-audit.md` for install compatibility; it drives **this** PKI workflow, not smart contracts.
