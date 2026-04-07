#!/bin/bash
# Claude Active Directory — install skills into ~/.claude/skills/

set -e

INSTALL_DIR="${HOME}/.claude/skills"
mkdir -p "${INSTALL_DIR}"

echo "Installing Claude Active Directory skills..."
echo ""

for skill_dir in skills/*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "${INSTALL_DIR}/${skill_name}"
    cp "${skill_dir}SKILL.md" "${INSTALL_DIR}/${skill_name}/SKILL.md"
    echo "✓ Installed skill: ${skill_name}"
done

COMMANDS_DIR="${HOME}/.claude/commands"
mkdir -p "${COMMANDS_DIR}"

for cmd_file in commands/*.md; do
    cmd_name=$(basename "$cmd_file")
    cp "$cmd_file" "${COMMANDS_DIR}/${cmd_name}"
    echo "✓ Installed command: ${cmd_name}"
done

echo ""
echo "Done! Skills installed to ${INSTALL_DIR}"
echo "Commands installed to ${COMMANDS_DIR}"
echo ""
echo "─────────────────────────────────────────────"
echo "Optional: Burp MCP (OWA / AD FS / cert enrollment web)"
echo "─────────────────────────────────────────────"
echo ""
echo "See mcp/burp-mcp-client/README.md for setup."
echo ""
read -p "Show Burp MCP config snippet? (y/N): " setup_burp
if [[ "$setup_burp" =~ ^[Yy]$ ]]; then
    echo ""
    if [[ -f mcp/burp-mcp-client/config.json ]]; then
        cat mcp/burp-mcp-client/config.json | head -20
    fi
    echo ""
fi

echo "Start:"
echo "  claude"
echo "  /scope"
echo "  /recon corp.local"
echo ""
echo "Evaluris Solutions — https://evaluris.ae"
