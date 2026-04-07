#!/bin/bash
# Full engagement pipeline stub — Claude Active Directory
# Evaluris Solutions — https://evaluris.ae
set -euo pipefail

DOMAIN="${1:?Usage: $0 <domain.fqdn>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "═══════════════════════════════════════════════"
echo "  Claude Active Directory — $DOMAIN"
echo "═══════════════════════════════════════════════"

bash "${ROOT}/tools/ad_recon.sh" "$DOMAIN"
python3 "${ROOT}/tools/hunt.py" --target "$DOMAIN" --recon-only 2>/dev/null || true

echo "Done. Review recon/${DOMAIN}/ and proceed with /hunt in Claude."
