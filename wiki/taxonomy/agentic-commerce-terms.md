---
type: taxonomy
title: Agentic Commerce Terms
description: Standardized vocabulary defining transaction autonomy levels, checkout
  interactions, delegated payment models, and commerce protocols.
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
  at: '2026-10-05T05:49:21.087865+00:00'
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

The Agentic Commerce taxonomy defines standardized terms for AI agent interactions across purchasing, transactions, payment delegation, and commerce protocol exchanges. Maintained in coordination with the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md) and the [Taxonomy and Landscape Workstream](../workstreams/taxonomy-and-landscape.md), these terms establish clear boundaries between human oversight levels and autonomous agent execution in financial interactions.

# Architecture / Specification

The agentic commerce domain categorizes interactions into transaction autonomy tiers, execution checkpoints, payment mechanisms, and protocol layers:

## Transaction Classifications

- **Agent-Completed Transaction**: An end-to-end commerce transaction where an AI agent executes discovery, negotiation, checkout, and settlement fulfillment autonomously without inline human intervention during execution [^evt-ws-taxonomy-landscape-pr-70].
- **Agent-in-the-Loop Transaction**: A commerce transaction where an AI agent assists, mediates, or executes specific stages of the transaction lifecycle while maintaining human oversight or interactive verification gates (renamed from *Agent-mediated transaction*) [^evt-ws-taxonomy-landscape-pr-71].
- **Agent-Initiated Transaction**: A commerce transaction triggered autonomously or programmatically by an AI agent based on predefined criteria, environmental triggers, or delegated objectives, regardless of whether downstream fulfillment requires human approval [^evt-ws-taxonomy-landscape-pr-72].

## Checkout and Payment Mechanisms

- **Agentic Checkout**: The automated or assisted workflow through which an AI agent traverses merchant interfaces, cart evaluations, shipping configurations, and payment authorizations to finalize a purchase on behalf of a principal [^evt-ws-taxonomy-landscape-pr-73].
- **Delegated Payment**: A payment execution pattern wherein an authorized agent is granted scoped financial authority (such as spending limits, merchant constraints, or time-bounded credentials) to transact funds on behalf of a human principal or corporate entity [^evt-ws-taxonomy-landscape-pr-76].

## Protocol Infrastructure

- **Agentic Commerce Protocols**: Standardized communication specifications, interchange schemas, and interaction flows governing how autonomous agents discover merchants, negotiate terms, transmit cart payloads, and process transactions interoperably across distributed commerce ecosystems [^evt-ws-taxonomy-landscape-pr-75].

# Lifecycle History

- PR#70 introduced definitions for *Agent-completed transaction* [^evt-ws-taxonomy-landscape-pr-70].
- PR#71 introduced *Agent-in-the-loop transaction*, renaming the prior draft term *Agent-mediated transaction* based on working group consensus [^evt-ws-taxonomy-landscape-pr-71].
- PR#72 introduced definitions for *Agent-initiated transaction* [^evt-ws-taxonomy-landscape-pr-72].
- PR#73 introduced definitions for *Agentic checkout* [^evt-ws-taxonomy-landscape-pr-73].
- PR#75 defined *Agentic commerce protocols*, pluralizing and formalizing the protocol classification [^evt-ws-taxonomy-landscape-pr-75].
- PR#76 introduced definitions for *Delegated payment* [^evt-ws-taxonomy-landscape-pr-76].

[^evt-ws-taxonomy-landscape-pr-70]: https://github.com/aaif/ws-taxonomy-landscape/pull/70
[^evt-ws-taxonomy-landscape-pr-71]: https://github.com/aaif/ws-taxonomy-landscape/pull/71
[^evt-ws-taxonomy-landscape-pr-72]: https://github.com/aaif/ws-taxonomy-landscape/pull/72
[^evt-ws-taxonomy-landscape-pr-73]: https://github.com/aaif/ws-taxonomy-landscape/pull/73
[^evt-ws-taxonomy-landscape-pr-75]: https://github.com/aaif/ws-taxonomy-landscape/pull/75
[^evt-ws-taxonomy-landscape-pr-76]: https://github.com/aaif/ws-taxonomy-landscape/pull/76
