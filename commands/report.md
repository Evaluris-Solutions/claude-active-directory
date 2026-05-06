---
description: Generate internal penetration test / red team report structure for Active Directory engagements — executive summary, scope, methodology, findings, remediation. Usage: /report
---

# /report

## Command contract

| Field | Detail |
|-------|--------|
| **Invocation** | `/report` |
| **ROE gate** | Report **scope** section must mirror `/scope`; only **validated** (or explicitly pilot) findings belong in customer-facing text. |
| **Outputs** | Skeleton under `reports/` from `tools/report_generator.py`; fill per `engagement-reporting` skill. |
| **Stop conditions** | Unvalidated critical claims → remove or mark “pending validation.” |
| **Related** | [`skills/engagement-reporting`](../skills/engagement-reporting/SKILL.md), [`commands/validate`](validate.md) |

## Tool

```bash
python3 tools/report_generator.py --target <domain>
```

Produces a skeleton under `reports/` aligned with `skills/engagement-reporting/SKILL.md`.

## Sections to fill

1. Executive summary  
2. Scope and limitations  
3. Methodology (high level)  
4. Findings (severity, evidence, remediation each)  
5. Roadmap  

**Evaluris Solutions** report quality: defensible, reproducible, professional.
