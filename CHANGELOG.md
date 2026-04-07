# Changelog

## v1.0.0 — Claude Active Directory (Apr 2026)

### Product pivot

- **Claude Active Directory** replaces the prior bug-bounty-focused plugin. This release is an **authorized Active Directory / Windows domain offensive security** harness: reconnaissance, credential and privilege attacks, AD CS/PKI review, reporting, and validation — for internal assessments and red teams with explicit rules of engagement only.
- **Attribution**: [Evaluris Solutions](https://evaluris.ae). Primary author: **Evaluris Team**.
- **License**: MIT; copyright **Evaluris Solutions** (see [LICENSE](LICENSE)).

### Structure (unchanged counts)

- 13 slash commands (same names; content is AD-specific — e.g. `/recon` = domain/LDAP/DNS enum, `/hunt` = offensive phase within ROE).
- 8 skill domains under `skills/` (renamed folders: `ad-pentest`, `ad-methodology`, `ad-recon`, `ad-attack-classes`, `ad-arsenal`, `ad-cs-pki`, `engagement-reporting`, `finding-validation`).
- 7 agents (including **ad-cs-auditor** replacing the former web3 auditor).
- Tools: engagement orchestration, ROE checking, validation, reporting, AD-oriented recon script; removed HackerOne-specific and unrelated web-only scanners.

### Removed or replaced

- HackerOne MCP and bug-bounty program workflows.
- Web3 / smart-contract skill chain and related commands content.
- Public bug-bounty target selection and platform report templates.

### Optional integrations

- **Burp MCP** remains optional for HTTP-facing surfaces (OWA, AD FS, certificate enrollment web).

---

Earlier changelog entries referred to the previous bug-bounty-oriented project and are archived for history only in git; this tree is maintained as **Claude Active Directory** by Evaluris Solutions.
