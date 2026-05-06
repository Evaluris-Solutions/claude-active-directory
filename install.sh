#!/usr/bin/env bash
# Claude Active Directory — install skills and commands (wrapper)
# Default: Claude Code paths. Other targets: ./install.sh cursor | gemini | all
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-claude}"
exec "${ROOT}/scripts/install.sh" "${TARGET}"
