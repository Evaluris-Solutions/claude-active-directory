#!/usr/bin/env bash
# Claude Active Directory — multi-target installer
# Usage: scripts/install.sh [claude|cursor|gemini|all]
#   claude  — ~/.claude/skills + ~/.claude/commands (default)
#   cursor  — ~/.cursor/skills + ~/.cursor/commands (Cursor Agent Skills / custom commands)
#   gemini  — prints copy instructions (no single official global path across versions)
#   all     — claude + cursor

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-claude}"

install_claude() {
  local INSTALL_DIR="${HOME}/.claude/skills"
  local COMMANDS_DIR="${HOME}/.claude/commands"
  mkdir -p "${INSTALL_DIR}" "${COMMANDS_DIR}"
  echo "Installing skills → ${INSTALL_DIR}"
  for skill_dir in "${ROOT}/skills/"*/; do
    [[ -d "$skill_dir" ]] || continue
    skill_name="$(basename "$skill_dir")"
    mkdir -p "${INSTALL_DIR}/${skill_name}"
    cp "${skill_dir}SKILL.md" "${INSTALL_DIR}/${skill_name}/SKILL.md"
    echo "  ✓ ${skill_name}"
  done
  echo "Installing commands → ${COMMANDS_DIR}"
  for cmd_file in "${ROOT}/commands/"*.md; do
    [[ -f "$cmd_file" ]] || continue
    cp "$cmd_file" "${COMMANDS_DIR}/$(basename "$cmd_file")"
    echo "  ✓ $(basename "$cmd_file")"
  done
  echo ""
  echo "Done (Claude Code). Optional: Burp MCP — see ${ROOT}/mcp/burp-mcp-client/README.md"
  if [[ -t 0 ]]; then
    read -r -p "Show Burp MCP config snippet? (y/N): " setup_burp || true
    if [[ "${setup_burp:-}" =~ ^[Yy]$ ]] && [[ -f "${ROOT}/mcp/burp-mcp-client/config.json" ]]; then
      head -20 "${ROOT}/mcp/burp-mcp-client/config.json" || true
    fi
  fi
}

install_cursor() {
  local SK="${HOME}/.cursor/skills"
  local CMD="${HOME}/.cursor/commands"
  mkdir -p "${SK}" "${CMD}"
  echo "Installing skills → ${SK}"
  for skill_dir in "${ROOT}/skills/"*/; do
    [[ -d "$skill_dir" ]] || continue
    skill_name="$(basename "$skill_dir")"
    mkdir -p "${SK}/${skill_name}"
    cp "${skill_dir}SKILL.md" "${SK}/${skill_name}/SKILL.md"
    echo "  ✓ ${skill_name}"
  done
  echo "Installing commands → ${CMD}"
  for cmd_file in "${ROOT}/commands/"*.md; do
    [[ -f "$cmd_file" ]] || continue
    cp "$cmd_file" "${CMD}/$(basename "$cmd_file")"
    echo "  ✓ $(basename "$cmd_file")"
  done
  echo "Done (Cursor). If your Cursor build uses project-local .cursor/skills, copy from ${SK} or re-run with a custom DEST (see README)."
}

install_gemini() {
  echo "Gemini / Google AI CLI: there is no single guaranteed global skills path across versions."
  echo "Copy manually:"
  echo "  Skills:   cp -R ${ROOT}/skills/<name>/SKILL.md <your-cli-skills-dir>/<name>/"
  echo "  Commands: cp ${ROOT}/commands/*.md <your-cli-commands-dir>/"
  echo "Open an issue if you document a stable default path for a specific Gemini CLI release."
}

case "${TARGET}" in
  claude)  install_claude ;;
  cursor)  install_cursor ;;
  gemini)  install_gemini ;;
  all)     install_claude; echo ""; install_cursor ;;
  -h|--help|help)
    echo "Usage: $0 [claude|cursor|gemini|all]"
    exit 0
    ;;
  *)
    echo "Unknown target: ${TARGET}. Use: claude | cursor | gemini | all" >&2
    exit 1
    ;;
esac

echo ""
echo "Evaluris Solutions — https://evaluris.ae"
