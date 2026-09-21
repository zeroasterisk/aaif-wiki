---
type: working-group
title: Agentic Commerce Working Group
description: AAIF working group cataloging, aligning, and harmonizing open specifications
  and reference architectures across autonomous commercial interactions.
resource: https://github.com/aaif/wg-agentic-commerce/pull/6
tags:
- working-group
- commerce
- protocols
- specifications
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:03:42.691231+00:00'
sources:
- id: evt-wg-agentic-commerce-pr-6
  resource: https://github.com/aaif/wg-agentic-commerce/pull/6
  author: narko4u
  last_modified: '2026-09-01T07:30:12+00:00'
---

# Overview
The Agentic Commerce Working Group standardizes, aligns, and develops reference architectures and open specifications for autonomous AI commerce, transaction lifecycles, negotiation, and settlement.

# Architecture / Specification
The working group structures its core outputs into key deliverables:

- **Capability Map (Deliverable 1)**: Maps end-to-end commercial interaction capabilities across pre-purchase, purchase, and post-purchase lifecycle phases [^evt-wg-agentic-commerce-pr-6].
- **Post-Purchase Capabilities (P1–P7)**: Proposed functional areas covering eligibility inquiry, remedy offer and negotiation, buyer authorization and consent evidence, state-change execution signals, evidence binding, dispute and claims initiation, and adjustment ledgers [^evt-wg-agentic-commerce-pr-6].
- **Evidence and Auditability Contract**: Employs an 8-field bounded verdict envelope (`verdict`, `verifier`, `verifier_signature`, `evidence_refs`, `evidence_fingerprints`, `verification_basis`, `witness_scope`, `timestamp`) to ensure verifiable, machine-readable post-transaction settlement across systems [^evt-wg-agentic-commerce-pr-6].
- **Gap Analysis (Deliverable 2)**: Identifies gaps in existing commercial protocols (such as UCP, ACP, AP2, and x402) and aligns requirements with sibling foundation groups.

# Cross-Working-Group Alignment
- Telemetry and evidence records align with `../working-groups/observability-and-traceability.md` [^evt-wg-agentic-commerce-pr-6].
- Agent identity, consent, and verifiable delegation coordinate with `../working-groups/identity-and-trust.md` [^evt-wg-agentic-commerce-pr-6].

[^evt-wg-agentic-commerce-pr-6]: https://github.com/aaif/wg-agentic-commerce/pull/6
