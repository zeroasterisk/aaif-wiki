---
type: proposal
title: Evidence Record Specification
description: Testable data model and schema standardizing tamper-evident agent execution
  records across observation, compliance, and regulatory audit surfaces.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
tags:
- evidence
- audit
- compliance
- logging
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:25:24.695424+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-01T15:08:11+00:00'
---

# Overview
The Evidence Record Specification defines a standardized, tamper-evident log record schema capturing agent execution state, authorization decisions, and runtime interactions [^evt-wg-governance-risk-and-regulatory-issue-9]. It operationalizes regulatory logging mandates across EU AI Act Art 12/19/26(6), China TC260, Singapore Agentic Framework, SOC 2, PCI DSS v4.0.1, and ISO/IEC 42001 into checkable technical artifacts [^evt-wg-governance-risk-and-regulatory-issue-9].

# Architecture / Specification
The record structure aligns with converging international standards (ISO/IEC 24970, prEN 18229-1, and IETF `draft-sharif-agent-audit-trail`) around shared technical properties [^evt-wg-governance-risk-and-regulatory-issue-9]:
- **Cryptographic Tamper-Evidence**: Cryptographically hash-chained and timestamped log records providing verifiable non-repudiation [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Pre-Execution Capture**: Mandatory capture of authorization checks, permission denials, and human escalation gates prior to execution [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Recording-Independence Gradient**: Enforcement of independent recording boundaries ensuring high-trust actions are not logged solely by the acting agent [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Reproducibility Metadata**: Structured execution context and decision metadata supporting external timestamp anchoring and audit reproducibility [^evt-wg-governance-risk-and-regulatory-issue-9].

# Lifecycle History
Identified during Phase 2 regulatory gap analysis within the Governance, Risk & Regulatory Working Group as a machine-checkable conformity target bridging policy and runtime implementations [^evt-wg-governance-risk-and-regulatory-issue-9].

# References
- Cross-references: [Governance, Risk and Regulatory Working Group](../working-groups/governance-risk-and-regulatory.md), [Control-Plane Telemetry Evidence Model](../guidelines/control-plane-telemetry-evidence-model.md).

[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
