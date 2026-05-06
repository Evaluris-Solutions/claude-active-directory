---
name: ad-methodology
description: Use when planning or unblocking an authorized Active Directory assessment—phasing work, choosing which skill to open next, routing when stuck (no creds, empty BH graph, SQL in scope), or aligning deliverables with MITRE-ready reporting. Covers session discipline, optional read-only baselines, and tool routing. Does not replace ROE written with the customer.
---

# AD Methodology — How to Run the Engagement

**Evaluris Solutions** — [evaluris.ae](https://evaluris.ae)

## External references

- [ad-pentest](../ad-pentest/SKILL.md) — master workflow  
- [docs/ad-resources.md](../../docs/ad-resources.md)

## Usage examples

1. **Monday kickoff** — Lead opens this skill to walk the team through skill reading order and time-boxes noisy tests against the signed ROE.  
2. **Stuck after recon** — Trusts are visible but no creds; the team uses the **stuck table** row and schedules trust-targeted LDAP only on allow-listed names.  
3. **Detection workshop prep** — Methodology’s MITRE pointer plus [finding-validation](../finding-validation/SKILL.md) mapping table feeds a dry-run with the customer SOC.

## Troubleshooting

| Problem | What to do |
|---------|------------|
| Team keeps jumping to exploits | Re-center on **five phases** and `/scope`; log what was skipped for the report. |
| PingCastle output conflicts with offensive proof | Treat scanner output as **hints** only; offensive claims still need replayable steps. |
| Tool routing outdated | Prefer NetExec / CrackMapExec per [ad-arsenal](../ad-arsenal/SKILL.md); verify binary names in the appendix. |

## Mindset

- **Authorized only** — ROE is the source of truth.
- **Graph + paths** — think in attack paths, not isolated tricks.
- **One crown jewel** per session — what would worst-case compromise look like for this client?

## Skill reading order (recommended path)

Use this as a **default navigation** order; loop back whenever a phase stalls.

1. **[ad-pentest](../ad-pentest/SKILL.md)** — ROE, phases, path-hunting mindset.
2. **[ad-recon](../ad-recon/SKILL.md)** — DNS/LDAP/SMB/Kerberos/BloodHound, trusts, spray gates.
3. **[ad-attack-classes](../ad-attack-classes/SKILL.md)** — Technique reference, lateral matrix, trust overview.
4. **[ad-arsenal](../ad-arsenal/SKILL.md)** — Tool patterns and telemetry awareness.
5. **[ad-cs-pki](../ad-cs-pki/SKILL.md)** — AD CS triage and evidence bundles.
6. **[finding-validation](../finding-validation/SKILL.md)** — Before client-facing write-up.
7. **[engagement-reporting](../engagement-reporting/SKILL.md)** — Structure and AD finding fields.

**Glossary:** [docs/ad-glossary.md](../../docs/ad-glossary.md)

## Five phases (loop freely)

1. **Orient** — Reread ROE, objectives, time box.
2. **Map** — Domain users, computers, trusts, interesting groups, AD CS, Tier-0 assets.
3. **Probe** — Low-noise checks first unless engagement allows noise (spray, scans).
4. **Prove** — Repeatable exploitation evidence for findings.
5. **Report** — Impact, likelihood, remediation, residual risk.

## Stuck? Quick table

| Symptom | Try |
|---------|-----|
| No creds | AS-REP, Kerberoast, LLMNR coerced capture (if allowed), misconfig ACLs from BloodHound |
| Creds but no path | Delegation, local admin reuse, GPO, certificate templates |
| BH graph empty | Collection method, scope of session, run from multiple hosts |
| Everything patched | Misconfig-only: ACLs, AD CS, delegation, password in description |
| **Trusts visible but no creds** | Trust-targeted **DNS/LDAP** (in-scope names only), document SID filtering / selective auth awareness; request customer-side session or jump box if blocked |
| **SQL in scope** | AD-joined **SQL** checks per [ad-attack-classes](../ad-attack-classes/SKILL.md) — instances, auth mode, linked servers; destructive probes only with explicit ROE |

## Tool routing (examples)

- **LDAP / users / groups** → ldapsearch, bloodyAD, windapsearch  
- **Sessions / SMB** → NetExec / CrackMapExec  
- **Kerberos tickets** → getTGT/getST (Impacket), Rubeus  
- **AD CS** → Certipy, manual `certipy find` / `certipy req` per ROE  
- **Graph** → SharpHound → BloodHound  

## Session discipline

- Time-box noisy actions.
- Log your commands for the report appendix.
- When rotating off a host, note what was attempted so `/resume` stays useful.

---

## Optional defensive baselines (read-only, if in scope)

Some customers authorize **read-only** domain health tools (e.g. **PingCastle**-class scanners, vendor AD security dashboards) **in addition to** offensive validation.

- Treat output as **prioritization hints**, not proof of exploitability — **offensive findings** still need **reproducible** evidence per ROE.
- Align tool **version** and **ruleset** date in the methodology appendix.
- If not in scope, state **“baseline scanner not used”** so the report scope is clear.

---

## MITRE ATT&CK (deliverable alignment)

For **enterprise** and **detection-engineering** audiences, map confirmed behaviors to **[MITRE ATT&CK](https://attack.mitre.org/)** techniques (e.g. credential access, lateral movement). Use **[finding-validation](../finding-validation/SKILL.md)** for the mapping table pattern — **verify technique IDs** against the current ATT&CK release; do not invent sub-techniques.
