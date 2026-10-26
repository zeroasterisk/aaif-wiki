---
type: working-group
title: Governance, Risk, and Regulatory Working Group
description: AAIF technical working group bridging global AI policy developments and
  technical implementation through gap analysis, compliance mapping, and audit trail
  standards.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
tags:
- governance
- compliance
- regulation
- working-group
- audit-trail
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:51:37.206517+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-08T03:11:06+00:00'
---

# Overview
The Governance, Risk, and Regulatory Working Group bridges international artificial intelligence regulatory requirements, compliance frameworks, and concrete technical implementations for agentic systems. It conducts comprehensive policy-to-technical mapping exercises to translate high-level legal and audit mandates into verifiable engineering artifacts and operational controls.

# Architecture / Specification
The working group's Phase 2 gap analysis focuses on mapping cross-jurisdictional policy instruments to core engineering themes[^evt-wg-governance-risk-and-regulatory-issue-9]. Key areas of evaluation include:

- **Policy Mapping Clusters**: Evaluating requirements across the EU AI Act (Articles 12, 19, and 26(6)), China TC260 agent guidelines, Singapore's Model AI Governance Framework for Agentic AI, SOC 2, PCI DSS v4.0.1, and ISO/IEC 42001[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Converging Record-Shape Standards**: Shifting compliance assessment from subjective policy outcomes ("logging required") to machine-checkable artifact verification by tracking converging audit trail standards:
  - **ISO/IEC 24970**: AI system logging standard developed jointly by JTC 1/SC 42 and CEN-CENELEC JTC 21[^evt-wg-governance-risk-and-regulatory-issue-9].
  - **prEN 18229-1**: CEN AI Trustworthiness Framework Part 1 (Logging), maintaining a normative reference relationship to ISO/IEC 24970[^evt-wg-governance-risk-and-regulatory-issue-9].
  - **IETF draft-sharif-agent-audit-trail**: JSON-based record structure specifying mandatory schema fields mapped directly to major regulatory and certification regimes[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Evidence Verification Criteria**: Standardizing the operational distinction between [self-reported](../taxonomy/self-reported.md) telemetry and independently attestable [action records](../taxonomy/action-record.md), incorporating recording-independence gradients, pre-execution denial and escalation logging, external timestamp anchoring, and metadata for decision reproducibility[^evt-wg-governance-risk-and-regulatory-issue-9].

# References
- [Evidence Record Specification](../standards/evidence-record-spec.md)
- [Evidence Strength Labels](../taxonomy/evidence-strength-labels.md)

[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
