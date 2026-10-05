---
type: working-group
title: Governance, Risk, and Regulatory Working Group
description: AAIF working group bridging global AI policy instruments with machine-checkable
  logging, evidence, and risk controls.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
tags:
- governance
- compliance
- regulatory
- audit-trail
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:59:46.074542+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-01T15:08:11+00:00'
---

# Overview
The Governance, Risk, and Regulatory Working Group bridges international AI governance frameworks, legal instruments, and compliance mandates with machine-checkable technical specifications [^evt-wg-governance-risk-and-regulatory-issue-9]. It conducts gap analyses mapping regulatory requirements (e.g., EU AI Act, SOC 2, PCI DSS v4.0.1, ISO/IEC 42001) to concrete architectural verification artifacts [^evt-wg-governance-risk-and-regulatory-issue-9].

# Architecture / Specification
### Converging Evidence and Logging Standards
The Phase 2 gap analysis identifies convergence across emerging international standards defining checkable audit record shapes [^evt-wg-governance-risk-and-regulatory-issue-9]:
- **ISO/IEC 24970 & prEN 18229-1**: Joint international standards specifying machine-checkable logging for AI trustworthiness [^evt-wg-governance-risk-and-regulatory-issue-9].
- **IETF Agent Audit Trail (`draft-sharif-agent-audit-trail`)**: Open JSON record schema mapping directly to EU AI Act and SOC 2 audit trail mandates [^evt-wg-governance-risk-and-regulatory-issue-9].

These specifications establish shared technical requirements for agent auditability [^evt-wg-governance-risk-and-regulatory-issue-9]:
- Hash-chained, timestamped, tamper-evident log records [^evt-wg-governance-risk-and-regulatory-issue-9].
- Mandatory pre-execution capture of authorization denials and escalation events [^evt-wg-governance-risk-and-regulatory-issue-9].
- A recording-independence gradient ensuring an autonomous agent cannot act as the sole recorder of its own high-trust actions [^evt-wg-governance-risk-and-regulatory-issue-9].
- Support for external timestamp anchoring and decision reproducibility metadata [^evt-wg-governance-risk-and-regulatory-issue-9].

[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
