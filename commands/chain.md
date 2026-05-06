---
description: Build multi-hop Active Directory attack paths — combine AS-REP, Kerberoast, delegation, ACL abuse, AD CS, lateral steps into one narrative. Usage: /chain
---

# /chain

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/chain` |
| **ROE gate** | Every hop must use **confirmed** primitives from **in-scope** hosts; no speculative edges in customer PDFs. |
| **Outputs** | Multi-hop narrative with evidence pointers per hop; handoff to **chain-builder** agent optional. |
| **Stop conditions** | Next hop blocked by ROE or unproven → end chain at last proven step. |
| **Related** | [`skills/ad-attack-classes`](../skills/ad-attack-classes/SKILL.md), [`agents/chain-builder`](../agents/chain-builder.md) |

## Purpose

Bug-bounty “A→B→C” chaining becomes **path enumeration** in AD:

**Example:** Kerberoast service account → cracked password → SMB to server → local privilege → lateral to DC-adjacent host → ACL edge to Tier-0.

## Process

1. List **confirmed** primitives (tickets, creds, cert, session).
2. Map edges from BloodHound or manual trust of admin relationships.
3. Document **each hop** with evidence.
4. Stop when objective met or ROE blocks next hop.

## Agent

Use **chain-builder** agent for structured path drafting.
