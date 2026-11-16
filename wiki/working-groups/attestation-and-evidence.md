---
type: working-group
title: Attestation and Evidence Working Group
description: Cross-cutting AAIF working group establishing decentralized standards,
  evidence classes, and witness verification frameworks for agent actions and decisions.
resource: https://github.com/aaif/working-group-proposals/issues/6
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:37:01.936664+00:00'
sources:
- id: evt-working-group-proposals-issue-6
  resource: https://github.com/aaif/working-group-proposals/issues/6
  author: StevenMih
  last_modified: '2026-10-25T15:10:07+00:00'
---

# Overview
The Attestation and Evidence Working Group (AE-WG) is a cross-cutting technical working group within the Agentic AI Foundation established to define how statements about AI agent actions, decisions, authorizations, and outcomes are attested and verified across organizational boundaries without central authorities[^evt-working-group-proposals-issue-6]. The working group standardizes evidence classes, portable self-describing bundles, witness models, and offline verification mechanisms to ensure records remain independently checkable across systems[^evt-working-group-proposals-issue-6].

# Architecture / Specification
## Scope and Boundaries
- **In Scope**: Evidence vocabulary and grading scales; attestation formats for autonomous decisions, actions, and authorizations; commitment-before-observation mechanics; bilateral and multi-party attestation at runtime boundaries; verifiable offline disclosure and request bundles; and obligation mapping in coordination with Governance, Risk, and Regulatory[^evt-working-group-proposals-issue-6].
- **Out of Scope**: Telemetry transport wire formats (coordinated with [Observability & Traceability](observability-and-traceability.md)), identity credentials (coordinated with [Identity & Trust](identity-and-trust.md)), threat modeling (coordinated with [Security & Privacy](security-and-privacy.md)), payment settlement protocols (coordinated with [Agentic Commerce](agentic-commerce.md)), and foundation-managed central ledgers[^evt-working-group-proposals-issue-6].

## Governance and Deliverables
- **Cross-Group Coordination**: Governed by two co-chairs and seats dedicated liaison representatives from every active AAIF working group under [Technical Committee](../governance/technical-committee.md) oversight[^evt-working-group-proposals-issue-6].
- **90-Day Roadmap**: Delivers Evidence Vocabulary v0, a witness and root-of-trust matrix (covering logs, cosigners, timestamp authorities, TEEs, and HSMs), evidence requirement analyses for sibling working group use cases, and an Evidence Classes and Gap Analysis 1.0 document for Technical Committee ratification[^evt-working-group-proposals-issue-6].

[^evt-working-group-proposals-issue-6]: https://github.com/aaif/working-group-proposals/issues/6
