#!/bin/bash
# Optional tooling for Claude Active Directory (authorized assessments only).
# Installs common CLI helpers via Homebrew where available.

set -euo pipefail

echo "============================================="
echo "  Claude Active Directory — optional tools"
echo "  Evaluris Solutions — https://evaluris.ae"
echo "============================================="

if ! command -v brew &>/dev/null; then
  echo "Install Homebrew first, or install tools manually: nmap, dig (bind), python3."
  exit 0
fi

for pkg in nmap bind python3; do
  if brew list "$pkg" &>/dev/null; then
    echo "[ok] $pkg"
  else
    echo "[*] brew install $pkg ..."
    brew install "$pkg" || true
  fi
done

echo ""
echo "Also recommended (manual): Impacket, Certipy, CrackMapExec, SharpHound/BloodHound."
echo "See README.md and skills/ad-arsenal/SKILL.md."
