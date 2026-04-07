<p align="center">
  <img src="logo.png" alt="Claude Active Directory" width="280"/>
  &nbsp;&nbsp;
  <img src="logo-2.png" alt="Evaluris Solutions" width="280"/>
</p>

<div align="center">

# Claude Active Directory

### The power of structured AI assistance for Active Directory offensive security

**Claude Active Directory** turns **Claude Code** into an engagement-aware copilot: eight skill domains, thirteen slash commands, seven agents, validation gates, and ROE-safe orchestration—so operators spend less time reinventing methodology and more time proving impact with defensible evidence.

*Part of the **Department of Offensive Security (DoOS)** — [Evaluris Solutions](https://evaluris.ae).*

<br>

<img src="https://img.shields.io/badge/v1.0.0-Claude_Active_Directory-1e40af?style=for-the-badge" alt="v1.0.0">

### AI agent harness for professional Active Directory penetration testing

*Structured methodology, validation, and reporting for authorized internal assessments and red team engagements.*

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-D97706.svg?style=flat-square&logo=anthropic&logoColor=white)](https://claude.ai/claude-code)

**0xaxgb** · **[Evaluris Solutions](https://evaluris.ae)** · DoOS

<br>

```
  13 commands  ·  7 AI agents  ·  8 skill domains
  Kerberos · LDAP · AD CS · Delegation · BloodHound-style analysis
  Optional: Burp MCP for HTTP surfaces (OWA, AD FS, enrollment web)
```

</div>

---

## Documentation

| Resource | Description |
|----------|-------------|
| [docs/ad-glossary.md](docs/ad-glossary.md) | AD / Kerberos terms used across skills |
| [docs/ad-resources.md](docs/ad-resources.md) | Curated external references (links only) |
| [CLAUDE.md](CLAUDE.md) | Plugin layout: skills, commands, tools, memory |

---

## Use case

Offensive security teams need more than a list of tools: they need **consistent methodology**, **evidence discipline**, **finding validation**, and **client-ready reports**. Claude Active Directory is a **Claude Code plugin** that packages skills, slash commands, agents, and helper scripts around **authorized** Active Directory assessments — from reconnaissance and credential attacks through privilege escalation, lateral movement, and AD CS misconfigurations.

---

## Quick start

**1. Install**

```bash
cd claude-active-directory
chmod +x install.sh && ./install.sh
```

**2. Load rules of engagement**

Confirm written authorization, in-scope domains/controllers, and forbidden actions before any testing.

**3. Run the workflow**

```bash
claude

/recon corp.local              # DNS, LDAP, SMB, user/SPN discovery, BloodHound prep
/hunt corp.local               # Offensive phase: cred attacks, relay, delegation, AD CS — within ROE
/scope                         # Re-check ROE / target allow list
/validate                      # Validate a finding (evidence + impact)
/report                        # Engagement-style technical report
```

**Optional:** `bash install_tools.sh` documents common external tools (Impacket, Certipy, CrackMapExec, SharpHound, etc.).

**Optional:** `python3 tools/hunt.py --target corp.local` for scripted orchestration stubs.

---

## Commands (names unchanged)

| Command | Role |
|--------|------|
| `/recon` | Domain/LDAP/DNS/SMB enumeration; Kerberos pre-auth; SPN/users; SharpHound collection prep |
| `/hunt` | Credential abuse, Kerberos attacks, NTLM relay opportunities, delegation, AD CS — **only inside ROE** |
| `/scope` | Rules of engagement — allowed domains/DCs, exclusions, destructive vs read-only |
| `/validate` / `/triage` | Internal finding validation (evidence, blast radius, reproducibility) |
| `/report` | Engagement / technical report outline |
| `/chain` | Attack path chaining (e.g. kerberoast → crack → lateral → escalation) |
| `/surface` | Prioritize hosts/paths (e.g. from BloodHound or notes) |
| `/autopilot` | Phased checklist within ROE (not unsupervised internet-wide testing) |
| `/intel` | DC/OS build and patch intel; known abuse patterns for versions |
| `/resume` / `/remember` | Engagement memory and continuity |
| `/web3-audit` | **Repurposed:** AD CS / PKI and certificate-template audit workflow (filename kept for install compatibility) |

---

## Skills

| Skill folder | Focus |
|-------------|--------|
| `ad-pentest` | Master workflow: ROE, kill chain, evidence |
| `ad-methodology` | Phases, tool routing, session discipline |
| `ad-recon` | DNS, LDAP, SMB, users, passwords policy, SPNs, trusts |
| `ad-attack-classes` | Kerberoasting, AS-REP, delegation, ACL abuse, lateral movement, etc. |
| `ad-arsenal` | Commands, OPSEC, lab-safe patterns |
| `ad-cs-pki` | AD CS templates, ESC patterns, evidence bundles |
| `engagement-reporting` | Executive + technical reporting |
| `finding-validation` | Gates before reporting |

---

## Agents

| Agent | Role |
|--------|------|
| **recon-agent** | Domain reconnaissance and collection guidance |
| **recon-ranker** | Prioritize paths from graph + context |
| **validator** | Evidence and impact for AD findings |
| **report-writer** | Engagement reports |
| **chain-builder** | Multi-hop escalation chains |
| **ad-cs-auditor** | PKI / template / ESC-focused review |
| **autopilot** | ROE-safe phased automation outline |

---

## Repository layout

```
claude-active-directory/
├── skills/           # 8 AD skill domains (SKILL.md each)
├── commands/         # 13 slash commands
├── agents/             # 7 agent briefs
├── tools/              # Python/shell helpers (orchestration, ROE, validate, report)
├── memory/             # Engagement journal, patterns, audit log, schemas
├── mcp/                # Optional Burp MCP client
├── tests/
├── docs/               # Glossary, AD resource pointers
├── rules/              # Always-on engagement rules
├── hooks/
└── wordlists/          # Password spray lists (authorized use only)
```

---

## Legal and ethics

**Use only on systems you own or are explicitly authorized to test in writing.** Unauthorized access is illegal. This software is provided for **professional security assessments** with clear rules of engagement. Evaluris Solutions and the authors are not responsible for misuse.

---

## License

MIT — see [LICENSE](LICENSE). Copyright **Evaluris Solutions**. Authored by **0xaxgb** — [https://evaluris.ae](https://evaluris.ae).
