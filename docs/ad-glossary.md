# Active Directory glossary

**Claude Active Directory** — [Evaluris Solutions](https://evaluris.ae) — authorized testing terminology only.

| Term | Definition |
|------|------------|
| **Active Directory (AD)** | Microsoft directory service for Windows domains; stores users, computers, groups, and policy. |
| **KDC** | Key Distribution Center; on AD it runs on domain controllers and issues Kerberos tickets. |
| **TGT** | Ticket-Granting Ticket; proves identity to the KDC; used to obtain service tickets. |
| **TGS** | Ticket-Granting Service ticket; authenticates a principal to a specific service (identified by SPN). |
| **SPN** | Service Principal Name; binds a Kerberos service instance to an account; Kerberoasting targets user-backed SPNs. |
| **UPN** | User Principal Name; human-friendly login form (`user@domain`). |
| **AS-REQ / AS-REP** | Kerberos messages for initial authentication; AS-REP can be captured for offline cracking if pre-auth is disabled. |
| **Pre-authentication** | Kerberos requirement that the client prove knowledge of the password before the KDC returns an AS-REP; when disabled, enables AS-REP roasting. |
| **UAC (userAccountControl)** | Bit field on user/computer objects; includes flags for account status, trusted-for-delegation, pre-auth, etc. |
| **Kerberoasting** | Requesting TGS tickets for SPNs and cracking them offline (service account passwords). |
| **NTLM** | Legacy challenge-response protocol; still present for compatibility; basis for relay and capture scenarios. |
| **NTLM relay (concept)** | Forcing or capturing an NTLM challenge-response and forwarding it to another service that accepts the same identity material—highly environment-dependent. |
| **DCSync** | Abuse of directory replication rights to pull credential material from a DC (requires specific AD permissions). |
| **Unconstrained delegation** | Kerberos delegation mode where a service can obtain a forwardable TGT for the user; high risk on compromised hosts. |
| **Constrained delegation** | Delegation limited to named SPNs; can still be abused when misconfigured. |
| **RBCD** | Resource-Based Constrained Delegation; `msDS-AllowedToActOnBehalfOfOtherIdentity` on a computer object controls who may delegate to it. |
| **ACL / DACL** | Access control on AD objects; dangerous ACEs (e.g. `GenericAll`, `WriteDACL`) enable takeover paths. |
| **Shadow credentials** | Technique family using key trust on user/computer objects when an attacker can write specific attributes—evidence-focused in reports. |
| **GPO / GPP** | Group Policy and (legacy) Group Policy Preferences; GPP XML in SYSVOL historically stored reversible passwords. |
| **LAPS** | Local Administrator Password Solution; randomizes local admin passwords; enumeration reveals who can read them. |
| **Tier 0 / 1 / 2** | Segmentation model: Tier 0 = direct control of AD identity systems (e.g. DCs, Tier-0 admins); lower tiers for workstations and apps. |
| **Forest / domain / tree** | Forest is the top AD boundary; domains are partitions inside it; trusts link domains or forests. |
| **Trust** | Relationship allowing authentication across domains/forests; direction and type affect attack paths. |
| **SID filtering** | Trust security feature limiting which SIDs from a trusted domain are honored. |
| **Selective authentication** | Restricts which principals from a trusted forest/domain can authenticate to resources. |
| **AD CS / PKI** | Certificate Services; enterprise CAs issue certs; misconfigured **templates** and **CA/DC policy** map to **ESC** abuse categories (ESC1–ESC11 in community tooling). |
| **ESC (AD CS)** | Community naming for certificate abuse scenarios — **ESC1–ESC8** (templates, agents, web/Relay surfaces); **ESC9–ESC11** extend to template **NO_SECURITY_EXTENSION**, **certificate mapping** / strong-binding posture, and **CA RPC** encryption — see `skills/ad-cs-pki/SKILL.md`. **ESC12 / ESC13** (and beyond) may appear in newer **Certipy** or research forks—always record the **label string** your tool version prints and link the vendor/community note; numbering is not frozen across releases. |
| **Certificate mapping / strong binding** | How a certificate is bound to an AD account (UPN, SAN, SID in extensions); DC **StrongCertificateBindingEnforcement** and related settings affect whether mapping attacks are viable — document values in evidence, cite current Microsoft guidance. |
| **Coerced authentication (concept)** | Inducing a host or account to authenticate to an attacker-influenced target; often discussed alongside **relay** and **AD CS**; named families (e.g. MS-RPC coercion, print spooler abuse) are awareness-only — **ROE** governs any testing. |
| **EPA** | Extended Protection for Authentication; channel-binding style mitigations for some authentication stacks when enabled — high-level hardening context, not an evasion topic. |
| **gMSA** | Group Managed Service Account; passwords rotated by the directory; service accounts using gMSA change **credential theft** narratives vs static passwords. |
| **LDAP signing / LDAPS** | Signing requirements and **LDAPS** (TLS) affect whether simple LDAP binds work and how “clear” traffic is; document policy in recon appendix. |

For methodology, see the `skills/` directory in this repository.
