# Active Directory resources (curated pointers)

**Claude Active Directory** — [Evaluris Solutions](https://evaluris.ae)

This file lists **external** references for operators. Methodology lives in `skills/` — do not paste long third-party cheat sheets into the repo.

## Vendor and platform documentation

- [Securing Active Directory — Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/securing-active-directory-and-windows-server) — hardening and architecture context  
- [Active Directory Domain Services overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) — terminology anchor  

## Threat framework (mapping findings)

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — technique IDs for reports (verify current version)  
- [MITRE D3FEND](https://d3fend.mitre.org/) — optional defensive countermeasure mapping for remediation sections  

## Graph and path analysis

- [BloodHound documentation](https://bloodhound.specterops.io/) — collectors, edges, and analysis (SpecterOps)  
- [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound) — CE project  

## AD Certificate Services (research lineage)

- [Certified Pre-Owned — SpecterOps](https://specterops.io/blog/2021/06/17/certified-pre-owned/) — foundational AD CS abuse research (read at source)  
- [Certipy — privilege escalation / ESC notes](https://github.com/ly4k/Certipy/wiki) — tool wiki aligned with community ESC labels (authorized testing only)  
- [Ghostpack Certify — ESC11 documentation](https://docs.specterops.io/ghostpack-docs/Certify.wik-mdx/esc11-ntlm-relay-to-ad-cs-rpc-interfaces) — RPC / interface context (read at source)  

## Tools (authorized use only)

- [Certipy](https://github.com/ly4k/Certipy) — AD CS enumeration and testing workflows  
- [Impacket](https://github.com/fortra/impacket) — Kerberos and Windows protocol examples  
- [NetExec](https://github.com/Pennyw0rth/NetExec) — maintained network execution framework (CrackMapExec successor in many environments)  

## Optional defensive baselines (read-only assessments)

- [PingCastle](https://github.com/vletoux/pingcastle) — AD health reporting (use only with customer authorization; not a substitute for offensive proof)  

## Methodology and research (read at source)

- SpecterOps [specterops.io](https://specterops.io/) — blog and materials on Kerberos, AD CS, and BloodHound — cite by title/URL; do not copy long excerpts into this repository.

---

Do not use these resources to target systems without **written authorization**.
