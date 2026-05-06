---
description: Active Directory offensive phase — credential attacks (spray if allowed), AS-REP and Kerberoast workflows, NTLM relay opportunities, delegation abuse paths, ACL-based escalation, AD CS template abuse, lateral movement within ROE. Usage: /hunt corp.local
---

# /hunt

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/hunt <domain.fqdn>` |
| **ROE gate** | **Strict** — spray, relay, coercion, destructive steps require explicit items from `/scope`. Re-read ROE before each noisy phase. |
| **Outputs** | Redacted technique notes, ticket/template identifiers, paths for `/validate` and `/report`. |
| **Stop conditions** | Out-of-scope host, missing spray approval, or SOC halt → stop immediately. |
| **Related** | [`skills/ad-attack-classes`](../skills/ad-attack-classes/SKILL.md), [`commands/scope`](scope.md), [`commands/validate`](validate.md) |

**Offensive testing** against an **authorized** Active Directory domain. Do nothing that violates ROE (no out-of-scope subnets, no unapproved destructive actions).

## Before you start

1. Reread **ROE** — spray allowed? relay? coercion?
2. Load **`recon/<domain>/`** outputs — users, SPNs, BH edges.
3. Define **objective** — e.g. path to Domain Admin vs. app-owner compromise.

## Credential access

- **AS-REP roast** / **Kerberoast** — offline cracking in controlled environment; protect secrets.
- **Spray** — only with customer approval and lockout policy respected.

## Privilege escalation

- **Delegation** (unconstrained, constrained, RBCD) — validate tooling and path.
- **ACLs** — `GenericAll`, reset password, shadow credentials (if in scope).
- **AD CS** — see `/web3-audit` (PKI workflow) and `skills/ad-cs-pki/`.

## Lateral movement

- Use obtained creds only on **in-scope** hosts; prefer least-noisy options when red team rules demand.

## Evidence

- Redacted command logs, ticket types, template names — for `/report`.

## Orchestrator

`python3 tools/hunt.py --target <domain>` runs engagement stubs and directory setup.
