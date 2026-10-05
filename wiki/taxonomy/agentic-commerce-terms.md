---
type: taxonomy
title: Agentic Commerce Taxonomy Terms
description: Standardized vocabulary and classification taxonomy defining transaction
  autonomy tiers, checkout flows, payment delegation, and commerce protocols.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/70
tags:
- taxonomy
- agentic-commerce
- payments
- transactions
- protocols
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:17:15.984795+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-70
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/70
  author: galesky-a
  last_modified: '2026-09-29T06:51:07+00:00'
- id: evt-ws-taxonomy-landscape-pr-71
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/71
  author: galesky-a
  last_modified: '2026-09-29T06:49:46+00:00'
- id: evt-ws-taxonomy-landscape-pr-72
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/72
  author: galesky-a
  last_modified: '2026-09-29T06:49:07+00:00'
- id: evt-ws-taxonomy-landscape-pr-73
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/73
  author: galesky-a
  last_modified: '2026-09-29T06:47:51+00:00'
- id: evt-ws-taxonomy-landscape-pr-75
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/75
  author: galesky-a
  last_modified: '2026-09-29T06:46:21+00:00'
- id: evt-ws-taxonomy-landscape-pr-76
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/76
  author: galesky-a
  last_modified: '2026-09-29T06:45:39+00:00'
---

# Overview

The Agentic Commerce Taxonomy establishes standardized vocabulary and classification models for automated economic interactions, transaction autonomy levels, payment mechanics, and interoperability protocols within the Agentic AI Foundation. Curated collaboratively under the [Taxonomy and Landscape Initiative](../initiatives/taxonomy-and-landscape.md) in coordination with the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md), these terms provide foundational conceptual clarity across AI shopping agents, merchant systems, payment gateways, and regulatory boundaries.

# Architecture / Specification

### Transaction Autonomy Tiers

The taxonomy classifies commercial transactions by the degree of agent involvement, delegation boundary, and execution authority:

- **Agent-Initiated Transaction**: A commercial transaction triggered or orchestrated by an autonomous agent on behalf of a user, initiating checkout or settlement according to user-defined intents, parameter boundaries, or programmatic criteria[^evt-ws-taxonomy-landscape-pr-72].
- **Agent-in-the-Loop Transaction**: A commercial transaction where an AI agent assists, mediates, or negotiates elements of the transaction lifecycle while maintaining active user interaction or validation throughout the flow[^evt-ws-taxonomy-landscape-pr-71]. This term replaces earlier working drafts of 'agent-mediated transaction' following community harmonization.
- **Agent-Completed Transaction**: An end-to-end commercial transaction fully executed, settled, and confirmed by an AI agent from cart composition through fund transfer without requiring manual human steps during the terminal transaction phase[^evt-ws-taxonomy-landscape-pr-70].

### Payment and Checkout Primitives

- **Agentic Checkout**: The automated procedural workflow and technical interface through which an AI agent interacts with merchant checkout funnels, submits customer credentials or tokens, selects fulfillment terms, and confirms order placement[^evt-ws-taxonomy-landscape-pr-73].
- **Delegated Payment**: A payment processing mechanism and authorization architecture where a payer delegates bounded financial authorization or credential utilization to an agent to execute monetary transfers within pre-authorized thresholds, cryptographic constraints, or runtime allowances[^evt-ws-taxonomy-landscape-pr-76].

### Interoperability and Protocols

- **Agentic Commerce Protocols**: Standardized communication specifications, data exchange schemas, and negotiation protocols enabling autonomous agents, digital wallets, merchants, and aggregators to discover goods, verify terms, negotiate prices, and exchange transactional metadata interoperably[^evt-ws-taxonomy-landscape-pr-75].

# References

- [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)
- [Taxonomy and Landscape Initiative](../initiatives/taxonomy-and-landscape.md)
- [Core Workflow Terms](../taxonomy/core-workflow-terms.md)

[^evt-ws-taxonomy-landscape-pr-70]: https://github.com/aaif/ws-taxonomy-landscape/pull/70
[^evt-ws-taxonomy-landscape-pr-71]: https://github.com/aaif/ws-taxonomy-landscape/pull/71
[^evt-ws-taxonomy-landscape-pr-72]: https://github.com/aaif/ws-taxonomy-landscape/pull/72
[^evt-ws-taxonomy-landscape-pr-73]: https://github.com/aaif/ws-taxonomy-landscape/pull/73
[^evt-ws-taxonomy-landscape-pr-75]: https://github.com/aaif/ws-taxonomy-landscape/pull/75
[^evt-ws-taxonomy-landscape-pr-76]: https://github.com/aaif/ws-taxonomy-landscape/pull/76
