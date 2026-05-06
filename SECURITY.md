# Security policy

## Scope of this policy

This document covers **security vulnerabilities in the Claude Active Directory plugin repository itself** (code, scripts, install paths, dependency confusion, etc.).

It does **not** govern how you report findings from **customer Active Directory** environments — that follows your **statement of work** and **customer disclosure** process.

## Supported versions

We address security issues affecting the **default branch** of [Evaluris-Solutions/claude-active-directory](https://github.com/Evaluris-Solutions/claude-active-directory). Tag maintainers may backport critical fixes on request.

## Reporting a vulnerability

1. **Do not** open a public GitHub issue for undisclosed security bugs in this repo.
2. Email **Evaluris Solutions** at the security contact published on [https://evaluris.ae](https://evaluris.ae) with subject line: `[SECURITY] claude-active-directory`.
3. Include: affected component (`tools/`, `install.sh`, etc.), reproduction steps, and impact.

We aim to acknowledge within **5 business days** and coordinate disclosure timeline.

## Out of scope

- Theoretical AD attacks without a defect in **this** repository.
- Findings from **third-party tools** (Impacket, Certipy, etc.) — report those to their maintainers.
- **Unauthorized testing** of any network — illegal; not supported.

## Safe use

This software is for **authorized** penetration tests and red teams only. Misuse is a violation of law and license.

MIT License — see [LICENSE](LICENSE).
