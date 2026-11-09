---
type: working-group
title: Governance, Risk & Regulatory Alignment Working Group
description: Technical working group bridging global AI policy developments and technical
  agentic systems through regulation tracking, governance patterns, and audit record
  standards.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/bfcefbf1250c2d3d6b6f2dcf20829a7ab24136a2/charter.md
tags:
- governance
- regulation
- risk
- audit
- compliance
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:17:35.329762+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/bfcefbf1250c2d3d6b6f2dcf20829a7ab24136a2/charter.md
  author: Manik Surtani
  last_modified: '2026-10-09T17:38:46+11:00'
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-08T03:11:06+00:00'
---

# Overview
The Governance, Risk & Regulatory Alignment Working Group (GRRA WG) bridges global AI policy developments and technical implementations of agentic AI systems [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf]. The group analyzes the regulatory treatment of agentic AI, evaluates organizational protocol implementations, and establishes technical alignment across emerging standards and policy regimes [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].

# Architecture / Specification

## Scope and Charter
Chartered under the Agentic AI Foundation, the working group addresses gaps between high-level regulatory mandates and verifiable engineering controls [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf]. Key scope areas include:
- Tracking and monitoring global AI regulations, standards, and policy frameworks affecting agentic architectures [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].
- Organizational governance of protocols such as MCP [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].
- Developing standard specifications for [AI Agent Bill of Materials](../taxonomy/ai-agent-bill-of-materials.md), incident reporting, action reversibility, and human-in-the-loop patterns [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].
- Exclusions: The working group does not provide formal legal advice or compliance certification solutions [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].

## Phase 2 Gap Analysis: Logging and Evidence Convergence
In its Phase 2 mapping initiative, the working group correlates regulatory and compliance instruments—including EU AI Act Articles 12, 19, and 26(6), China TC260 agent guidelines, Singapore's agentic framework, SOC 2, PCI DSS v4.0.1, and ISO/IEC 42001—against emerging technical logging specifications [^evt-wg-governance-risk-and-regulatory-issue-9]. The analysis focuses on three converging standards defining machine-checkable record shapes:
- **ISO/IEC 24970**: AI system logging standard developed jointly by JTC 1/SC 42 and CEN-CENELEC JTC 21 [^evt-wg-governance-risk-and-regulatory-issue-9].
- **prEN 18229-1**: CEN AI Trustworthiness Framework Part 1 (Logging) [^evt-wg-governance-risk-and-regulatory-issue-9].
- **IETF draft-sharif-agent-audit-trail**: Structured JSON record schema defining agent audit trails [^evt-wg-governance-risk-and-regulatory-issue-9].

These specifications converge on shared structural invariants: hash-chained tamper-evident structures, pre-execution capture of denials and escalations, recording-independence gradients to ensure agents do not solely record high-trust actions, optional external timestamp anchoring, and metadata enabling decision reproducibility [^evt-wg-governance-risk-and-regulatory-issue-9]. This shifts compliance evaluation from asking whether a system logs to evaluating whether record structures meet independently attestable formats [^evt-wg-governance-risk-and-regulatory-issue-9].

# Lifecycle History
The working group was formally approved on 2026-06-01 and updated on 2026-10-09, chaired by Deborah Eng (JPMorgan) with co-chair Sriram Natarajan (Google) [^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf].

[^evt-wg-governance-risk-and-regulatory-file-d22b3d6550c3-13ea07bf]: https://github.com/aaif/wg-governance-risk-and-regulatory/blob/bfcefbf1250c2d3d6b6f2dcf20829a7ab24136a2/charter.md
[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
