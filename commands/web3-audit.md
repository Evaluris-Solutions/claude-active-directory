---
description: AD CS and PKI security review — enterprise CA inventory, certificate templates, enrollment permissions, ESC-pattern triage with Certipy-style methodology, optional web enrollment attack surface. Filename legacy; content is PKI only. Usage: /web3-audit or /web3-audit corp.local
---

# /web3-audit (AD CS / PKI)

> **Note:** Command filename is unchanged for install compatibility. This command is **only** Active Directory Certificate Services / PKI — **not** smart contracts.

## Workflow

1. **Inventory** — CA servers, enrollment methods (RPC, web).
2. **Templates** — enumerate; flag dangerous EKU + enrollee supplies subject + weak ACLs.
3. **Map ESC patterns** — align with `skills/ad-cs-pki/SKILL.md`.
4. **Evidence** — template name, CA name, principal, request output (redacted).
5. **Report** — remediation: disable template, fix ACLs, enforce manager approval.

## Agent

**ad-cs-auditor** — use for deep PKI review.

## Tools

`certipy` when installed — `certipy find`, targeted `req` only with ROE.
