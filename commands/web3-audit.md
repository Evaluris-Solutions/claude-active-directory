---
description: AD CS and PKI security review — enterprise CA inventory, certificate templates, enrollment permissions, ESC-pattern triage with Certipy-style methodology, optional web enrollment attack surface. Filename legacy; content is PKI only. Usage: /web3-audit or /web3-audit corp.local
---

# /web3-audit (AD CS / PKI)

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/web3-audit` or `/web3-audit <context>` |
| **ROE gate** | CA hosts, web enrollment URLs, and relay surfaces must be **in-scope**; cert enrollment attempts require explicit approval. |
| **Outputs** | CA/template inventory, ESC-aligned evidence bundle fields per `ad-cs-pki` skill. |
| **Stop conditions** | Enrollment or relay step not approved → document theoretical risk only. |
| **Related** | [`skills/ad-cs-pki`](../skills/ad-cs-pki/SKILL.md), [`agents/ad-cs-auditor`](../agents/ad-cs-auditor.md), [`commands/scope`](scope.md) |

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
