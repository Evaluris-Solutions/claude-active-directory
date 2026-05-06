# Contributing to Claude Active Directory

Thank you for helping improve this **authorized Active Directory offensive security** plugin for Claude Code and compatible tools.

## Principles

1. **ROE-safe content only** — Skills, commands, and examples must assume **written authorization** and clear scope. Do not add step-by-step instructions aimed at unauthorized systems. See [rules/hunting.md](rules/hunting.md).
2. **No customer data** — Do not commit real hostnames, DNs, tickets, hashes, or credentials from engagements.
3. **Evidence-oriented** — Prefer repeatable **patterns** and **validation** language over exploit delivery.

## What to contribute

| Change type | Where | Notes |
|-------------|--------|--------|
| New or updated AD technique notes | `skills/*/SKILL.md` or `skills/<domain>/references/` | Keep `description` in YAML under ~500 chars when possible; use **third person** and **“Use when …”** in descriptions. |
| Slash command behavior | `commands/*.md` | Every impactful command must state an **ROE gate** (see `/scope`). |
| Agent behavior | `agents/*.md` | Clarify **inputs**, **outputs**, and **handoff**; avoid overlapping scope with other agents. |
| External pointers only | `docs/ad-resources.md` | Link out; do not paste large third-party bodies of text. |
| Tooling / tests | `tools/`, `tests/` | Run `pytest` before opening a PR. |

## Pull request checklist

- [ ] Linked issue (if substantive change).
- [ ] `SKILL.md` YAML: `name` + `description` valid; description includes activation trigger language.
- [ ] No secrets or engagement-specific data in the diff.
- [ ] `python -m pytest tests/` passes (use Python 3.8+).
- [ ] README / CLAUDE.md updated if user-facing paths or counts change.

## Local development

```bash
chmod +x install.sh scripts/install.sh scripts/convert.sh
python3 -m venv .venv && source .venv/bin/activate
pip install pytest
python -m pytest tests/
```

## Questions

Open an issue for **technique requests** or **doc gaps**. For **security vulnerabilities in this repository** (not customer AD), see [SECURITY.md](SECURITY.md).

— **Evaluris Solutions** · [evaluris.ae](https://evaluris.ae)
