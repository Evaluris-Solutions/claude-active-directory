#!/usr/bin/env bash
# Active Directory recon baseline — authorized assessments only.
# Usage: ad_recon.sh <domain.fqdn> [scope_lock]
set -euo pipefail

DOMAIN="${1:?Usage: ad_recon.sh <domain>}"
SCOPE_LOCK="${2:-0}"
BASE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${BASE}/recon/${DOMAIN}"

mkdir -p "${OUT}/"{dns,ldap,smb,notes,bloodhound,subdomains,live,urls}

# Checklist mirror of skills/ad-recon/SKILL.md LDAP cookbook (titles only)
cat > "${OUT}/notes/ldap-goals.txt" << 'LDAPGOALS'
LDAP goals (substitute base DN and bind per ROE) — see skills/ad-recon/SKILL.md for filters

[ ] All users
[ ] Users with SPN (Kerberoast candidates)
[ ] Pre-auth not required / DONT_REQUIRE_PREAUTH (AS-REP roast candidates)
[ ] Computers
[ ] Unconstrained delegation (TRUSTED_FOR_DELEGATION on computers)
[ ] Constrained delegation (msDS-AllowedToDelegateTo)
[ ] RBCD (msDS-AllowedToActOnBehalfOfOtherIdentity)
[ ] Sensitive group nested membership (e.g. Domain Admins — adjust group DN)
LDAPGOALS

{
  echo "Claude Active Directory — recon baseline"
  echo "Domain: ${DOMAIN}"
  echo "Time: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "scope_lock: ${SCOPE_LOCK}"
} > "${OUT}/notes/session.txt"

if command -v dig &>/dev/null; then
  dig +short "_ldap._tcp.dc._msdcs.${DOMAIN}" SRV > "${OUT}/dns/ldap_srv.txt" 2>&1 || true
  dig +short "${DOMAIN}" > "${OUT}/dns/a_records.txt" 2>&1 || true
fi

# Stubs for web-era recon adapters / agents that expect nested dirs
touch "${OUT}/subdomains/all.txt"
echo "https://${DOMAIN}" > "${OUT}/live/urls.txt" 2>/dev/null || true

echo "[ad_recon] Wrote ${OUT}"
echo "[ad_recon] Next: ldapsearch, CrackMapExec, SharpHound (per ROE)."
