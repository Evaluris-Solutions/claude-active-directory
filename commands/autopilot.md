---
description: Phased autonomous checklist for AD engagements within ROE — not unsupervised internet-wide scanning. Usage: /autopilot corp.local --normal
---

# /autopilot

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/autopilot <domain>` (optional flags per engagement SOP) |
| **ROE gate** | **Phase 1 must be** `/scope`; autopilot never overrides exclusions or spray/destructive bans. |
| **Outputs** | Phase checklist state; reminders to `/validate` material findings. |
| **Stop conditions** | Any ROE conflict → **pause** autopilot and return to human + `/scope`. |
| **Related** | [`skills/ad-methodology`](../skills/ad-methodology/SKILL.md), [`commands/scope`](scope.md) |

## What this is

A **disciplined phase loop** for operators using Claude — **not** permission to exceed ROE.

## Phases

1. **ROE verify** — `/scope`
2. **Recon** — `/recon`
3. **Surface rank** — `/surface`
4. **Hunt** — `/hunt` (credential + escalation per approval)
5. **Validate** — `/validate` on each material finding
6. **Report** — `/report`
7. **Checkpoint** — customer sync if engagement requires

## Modes (conceptual)

- **Paranoid** — human review after each major technique  
- **Normal** — batch validation  
- **Fast** — time-boxed; still **must** respect ROE and lockout policy  

## Agent

See **autopilot** agent brief for narrative structure.
