---
type: working-group
title: Governance, Risk, and Regulatory Working Group
description: Technical working group aligning agentic AI architectures with global
  AI regulations, compliance frameworks, and checkable audit record standards.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
tags:
- governance
- compliance
- audit-trail
- regulatory
- logging
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:44:24.452685+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-08T03:11:06+00:00'
---

# Overview

The Governance, Risk, and Regulatory Working Group (WG-GRR) within the Agentic AI Foundation evaluates regulatory instruments, assurance requirements, and risk management standards affecting autonomous AI agents. The group establishes technical mappings between legal compliance mandates—such as the EU AI Act, SOC 2, PCI DSS v4.0.1, China TC260 agent guidelines, and ISO/IEC 42001—and concrete architectural controls, focusing on turning high-level compliance outcomes into machine-verifiable artifacts [^evt-wg-governance-risk-and-regulatory-issue-9].

# Architecture / Specification

The working group structures its compliance mapping across major policy and assurance themes, specifically contrasting self-reported telemetry with independently attestable records:

- **Record-Shape Standardization**: Evaluating converging technical standards including ISO/IEC 24970 (AI system logging), prEN 18229-1 (AI Trustworthiness Framework Part 1: Logging), and IETF draft-sharif-agent-audit-trail to establish verifiable schemas for agent audit trails [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Tamper-Evident Logging**: Specifying hash-chained, timestamped records, external timestamp anchoring, and decision reproducibility metadata necessary to satisfy auditability mandates [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Recording Independence Gradient**: Enforcing boundary requirements where an agent cannot serve as the sole recorder of its own high-trust actions, capturing pre-execution denials and escalations [^evt-wg-governance-risk-and-regulatory-issue-9].
- **Related Frameworks**: Correlating these record requirements with the [Action Record](../taxonomy/action-record.md) and [Evidence Record Specification](../standards/evidence-record-spec.md) developed across AAIF workstreams.

# Lifecycle History

WG-GRR conducts ongoing gap analyses mapping external policy instruments to technical controls. Phase 2 initiatives expanded the analysis from legal outcome requirements to emerging machine-checkable logging standards [^evt-wg-governance-risk-and-regulatory-issue-9].

[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
