#!/usr/bin/env bash
# Best-effort: export skills for tools that expect a flat markdown tree.
# Usage: scripts/convert.sh [--flat DEST]
#   --flat DEST  — copy each SKILL.md to DEST/<skill-name>.md (no subfolders)

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ "${1:-}" == "--flat" && -n "${2:-}" ]]; then
  DEST="$2"
  mkdir -p "${DEST}"
  for skill_dir in "${ROOT}/skills/"*/; do
    [[ -d "$skill_dir" ]] || continue
    name="$(basename "$skill_dir")"
    cp "${skill_dir}SKILL.md" "${DEST}/${name}.md"
    echo "Wrote ${DEST}/${name}.md"
  done
  echo "Flat export complete."
  exit 0
fi

echo "Claude Active Directory — convert.sh"
echo ""
echo "Usage:"
echo "  $0 --flat <directory>   Copy each skill to <directory>/<skill-name>.md"
echo ""
echo "Limitations: does not rewrite YAML or slash-command formats; for other tools,"
echo "manually adjust frontmatter per that tool's documentation."
