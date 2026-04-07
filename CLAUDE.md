# Claude Active Directory — Plugin Guide

This repo is a **Claude Code** plugin for **authorized Active Directory / Windows domain offensive security** (internal pentest, red team, lab). It is maintained by **Evaluris Solutions** ([https://evaluris.ae](https://evaluris.ae)) as part of the **Department of Offensive Security (DoOS)**.

**Docs:** [docs/ad-glossary.md](docs/ad-glossary.md) (terms) · [docs/ad-resources.md](docs/ad-resources.md) (external links)

## What's here

### Skills (8 domains — load with `/ad-pentest` context or skill names under `~/.claude/skills/`)

| Skill | Domain |
|------|--------|
| `skills/ad-pentest/` | Master workflow — ROE, enum → creds → escalation → lateral → objectives |
| `skills/ad-methodology/` | Engagement mindset, phased workflow, tool routing, session discipline |
| `skills/ad-recon/` | DNS, trusts, LDAP/LDAPS & signing, gMSA, SMB, Kerberos, BloodHound collection |
| `skills/ad-attack-classes/` | Kerberos, NTLM relay, coercion awareness, delegation, ACL abuse, SQL pivot |
| `skills/ad-arsenal/` | NetExec/CME patterns, Impacket, Certipy, Event IDs, MITRE pointers, OPSEC |
| `skills/ad-cs-pki/` | AD CS, templates, ESC1–ESC11 evidence, DC mapping posture |
| `skills/engagement-reporting/` | Internal reports, AD fields, optional MITRE appendix |
| `skills/finding-validation/` | Gates, AD false positives, severity rubric, ATT&CK mapping |

### Commands (13 slash commands — same filenames)

| Command | Usage |
|---------|--------|
| `/recon` | `/recon <domain>` — domain/LDAP/DNS/SMB enumeration |
| `/hunt` | `/hunt <domain>` — offensive phase within ROE |
| `/validate` | Run validation gates on current finding |
| `/report` | Engagement / technical report |
| `/chain` | Build multi-hop attack paths |
| `/scope` | Rules of engagement — allowed targets and constraints |
| `/triage` | Quick validation pass |
| `/web3-audit` | **AD CS / PKI audit** (legacy filename; content is PKI-focused) |
| `/autopilot` | Phased checklist within ROE |
| `/surface` | Prioritize attack surface / high-value targets |
| `/resume` | Resume engagement |
| `/remember` | Log to engagement memory |
| `/intel` | Patch/build intel for domain controllers |

### Agents (7)

- `recon-agent` — domain recon and collection guidance  
- `report-writer` — engagement reports  
- `validator` — finding validation  
- `ad-cs-auditor` — AD CS / PKI and template abuse review  
- `chain-builder` — escalation chains  
- `autopilot` — ROE-safe phased outline  
- `recon-ranker` — prioritize paths from recon + memory  

### Rules (always active)

- `rules/hunting.md` — engagement and safety rules  
- `rules/reporting.md` — reporting quality rules  

### Tools (`tools/`)

- `hunt.py` — engagement orchestrator (enum → attack stubs → report hooks)  
- `ad_recon.sh` — AD-oriented recon steps (DNS, LDAP, SMB checks)  
- `validate.py` — interactive validation for internal findings  
- `report_generator.py` — engagement report skeleton  
- `roe_checker.py` — deterministic ROE / allow-list checks (formerly scope-oriented)  
- `target_loader.py` — load in-scope targets from config (no public bounty APIs)  
- `learn.py` / `intel_engine.py` — OS/patch-oriented intel helpers  
- `mindmap.py` — prioritized AD TTP mindmap hints  

### MCP (`mcp/`)

- `mcp/burp-mcp-client/` — **Optional** Burp Suite for HTTP surfaces (OWA, AD FS, cert web enrollment)

### Memory (`memory/`)

- `memory/hunt_journal.py` — append-only engagement log (JSONL)  
- `memory/pattern_db.py` — cross-engagement technique patterns  
- `memory/audit_log.py` — audit log, rate limiting  
- `memory/schemas.py` — schema validation  

## Start here

```bash
claude
# /scope          # confirm ROE first
# /recon <domain>
# /hunt <domain>
# /validate
# /report
```

## Install skills

```bash
chmod +x install.sh && ./install.sh
```

## Critical rules (always active)

1. **Written authorization and ROE** before touching customer or production systems  
2. **No out-of-scope systems** — treat exclusions as hard blocks  
3. **Validate findings** before client-facing writeups  
4. **Minimize impact** — prefer read-only techniques unless explicitly allowed  
5. **Document evidence** — commands, timestamps, scope  
