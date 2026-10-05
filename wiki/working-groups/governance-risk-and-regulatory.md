---
type: working-group
title: Governance, Risk, and Regulatory Alignment Working Group
description: AAIF working group aligning technical agentic architectures with global
  regulatory frameworks, compliance controls, and risk taxonomy.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/71b58c4f7fcc68f8001291436a75d8b0f60877e9/reporting/2026-08-report.md
tags:
- governance
- risk
- regulatory
- compliance
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:14:45.253933+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-file-922f59c26329-d5a40319
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/71b58c4f7fcc68f8001291436a75d8b0f60877e9/reporting/2026-08-report.md
  author: Sriram Natarajan
  last_modified: '2026-09-24T15:48:19-07:00'
---

# Overview

The Governance, Risk, and Regulatory Alignment Working Group aligns technical agentic architectures with international regulatory frameworks, statutory compliance obligations, and risk management best practices [^evt-wg-governance-risk-and-regulatory-file-922f59c26329-d5a40319]. The group is chaired by Ryan Hagemann (IBM) and Deborah Eng (JPMorgan Chase).

# Architecture / Specification

The working group conducts comparative regulatory and gap analyses against a baseline of 16 core governance themes [^evt-wg-governance-risk-and-regulatory-file-922f59c26329-d5a40319]:

1. **Governance & accountability**: Ownership, approvals, RACI frameworks, and risk acceptance.
2. **Use-case classification & risk tiering**: Prohibited vs. permitted systems and tiered control schemas.
3. **Architecture**: Reference patterns, trust boundaries, and control placement.
4. **Agent identity & delegation**: Authentication/authorization models, acting-on-behalf-of delegation, and registries.
5. **Guardrails & policy constraints**: Business rules, policy-as-code enforcement, and operational constraints.
6. **Data protection & privacy**: PII management, data minimization, retention schedules, and data residency.
7. **Security & access controls**: Least privilege, secrets isolation, workload segmentation, and tool permissions.
8. **Model/agent risk management**: Model validation, robustness benchmarks, drift detection, and change control.
9. **Human oversight**: HITL/HOTL escalation mechanisms, override/kill switches, and automated oversight.
10. **Action management**: Pre-execution checks, dual-control validation, and reversible operations.
11. **Monitoring & logging**: Audit trails, prompt/tool invocation logs, and deterministic decision logs.
12. **Testing & red teaming**: Adversarial prompt injection defense, tool abuse mitigations, and autonomy failure modes.
13. **Third-party & supply chain**: Vendor due diligence, model weight provenance, and tool dependency tracking.
14. **Incident response**: Detection procedures, containment policies, and regulatory reporting triggers.
15. **Transparency & user disclosure**: AI interaction notices, explainability records, and user expectation framing.
16. **Recordkeeping & auditability**: Statutory retention schedules, tamper-evident logs, and execution reproducibility.

# Lifecycle History

In August 2026, the working group established the 16-theme baseline and developed standardized extraction prompts for multi-jurisdictional policy comparisons [^evt-wg-governance-risk-and-regulatory-file-922f59c26329-d5a40319].

# References

- [WG Governance, Risk & Regulatory Alignment August 2026 Report](https://github.com/aaif/wg-governance-risk-and-regulatory/blob/71b58c4f7fcc68f8001291436a75d8b0f60877e9/reporting/2026-08-report.md)
- [Deterministic Acceptance Gate Pattern](../patterns/deterministic-acceptance-gate.md)
- [Hard-Constraint Human Oversight Pattern](../patterns/hard-constraint-human-oversight.md)

[^evt-wg-governance-risk-and-regulatory-file-922f59c26329-d5a40319]: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/71b58c4f7fcc68f8001291436a75d8b0f60877e9/reporting/2026-08-report.md
