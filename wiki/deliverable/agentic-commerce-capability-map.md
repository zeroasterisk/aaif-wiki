---
type: deliverable
title: Agentic Commerce Capability Map
description: A capability taxonomy and protocol mapping framework classifying agentic
  commerce transaction phases, signals, and evidence artifacts.
resource: https://github.com/aaif/wg-agentic-commerce/pull/6
tags:
- deliverable
- agentic-commerce
- protocols
- capability-map
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:58:28.995379+00:00'
sources:
- id: evt-wg-agentic-commerce-pr-6
  resource: https://github.com/aaif/wg-agentic-commerce/pull/6
  author: narko4u
  last_modified: '2026-09-01T07:30:12+00:00'
---

# Overview
The Agentic Commerce Capability Map is a foundational deliverable from the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md) defining structured capability rows, evidence artifacts, and protocol coverage across the agentic commerce lifecycle[^evt-wg-agentic-commerce-pr-6]. It establishes a standardized framework for analyzing protocol interoperability and ecosystem gaps across purchasing, post-purchase resolution, and settlement[^evt-wg-agentic-commerce-pr-6].

# Architecture / Specification
## Post-Purchase Capability Dimensions
The post-purchase capability model categorizes lifecycle interactions into seven structured capability rows (P1–P7)[^evt-wg-agentic-commerce-pr-6]:
- **P1: Eligibility Inquiry**: Validating return, refund, or warranty eligibility rules and conditions[^evt-wg-agentic-commerce-pr-6].
- **P2: Remedy Offer and Negotiation**: Automated negotiation and selection of remedies including refunds, replacements, or store credit[^evt-wg-agentic-commerce-pr-6].
- **P3: Buyer Authorization and Consent Evidence**: Capturing explicit user approval and cryptographic consent for financial and return operations[^evt-wg-agentic-commerce-pr-6].
- **P4: State-Change Execution Signals**: Emitting and tracking fulfillment, return shipping, and carrier status updates[^evt-wg-agentic-commerce-pr-6].
- **P5: Evidence Binding**: Contextual and cryptographic binding of inspection reports, return proofs, and interaction history[^evt-wg-agentic-commerce-pr-6].
- **P6: Dispute and Claims Initiation**: Protocol-mediated dispute filing across payment and commerce rails[^evt-wg-agentic-commerce-pr-6].
- **P7: Adjustment Ledger**: Reconciling ledgers, balance adjustments, and merchant-buyer settlements[^evt-wg-agentic-commerce-pr-6].

## Evidence Contract and Protocol Mapping
Capabilities are mapped against emerging agentic commerce protocols including UCP, ACP, AP2, and x402[^evt-wg-agentic-commerce-pr-6]. For cross-boundary verification and auditability, the specification defines an 8-field bounded verdict envelope comprising `verdict`, `verifier`, `verifier_signature`, `evidence_refs`, `evidence_fingerprints`, `verification_basis`, `witness_scope`, and `timestamp`[^evt-wg-agentic-commerce-pr-6].

# References
- Working Group: [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)
- Related Deliverable: [Agent Observability Use Cases](../deliverable/agent-observability-use-cases.md)

[^evt-wg-agentic-commerce-pr-6]: https://github.com/aaif/wg-agentic-commerce/pull/6
