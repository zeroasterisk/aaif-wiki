---
type: working-group
title: Agentic Commerce Working Group
description: AAIF working group addressing protocol fragmentation, capability mapping,
  agent wallets, and post-purchase workflows across agentic transactions.
resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-02-report.md
tags:
- commerce
- working-group
- protocols
- payments
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:48:01.743574+00:00'
sources:
- id: evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-02-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
- id: evt-wg-agentic-commerce-file-fa4050a9f626-c7520564
  resource: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-07-report.md
  author: Ilya Grigorik
  last_modified: '2026-08-03T22:02:18-07:00'
---

# Overview
The Agentic Commerce Working Group maps commerce capabilities, protocol interoperability, transaction execution, and trust mechanisms across autonomous agent transactions.[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26] Chaired by Ilya Grigorik (Shopify) and Rahul Bansal (OpenAI), the group addresses challenges including protocol fragmentation, merchant integration burden, delegated authority, and dispute resolution.[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26]

# Architecture / Specification
The working group evaluates candidate protocols and frameworks across the complete commerce lifecycle:
- **Capability Mapping**: Defining structured commerce lifecycles spanning discovery, eligibility checks, checkout, payment execution, and post-purchase state mutations such as cancellations, returns, refunds, and adjustments.[^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]
- **Protocol & Mandate Analysis**: Evaluating input protocols including Universal Commerce Protocol (UCP), Agentic Commerce Protocol (ACP), Agent Payments Protocol (AP2), and x402 payment responses.[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26][^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]
- **Agent Wallets & Authority**: Analyzing how bounded intents, payment mandates, and credential capabilities integrate into transactions without requiring complete commerce system reimplementation by merchants.[^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]

# Lifecycle History
- **February 2026**: Working group launched under co-chairs Ilya Grigorik and Rahul Bansal, compiling an actor and capability inventory spanning consumers, agents, merchants, wallets, payment providers, and banks.[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26]
- **July 2026**: Advanced post-purchase workflow analysis using UCP policy structures and explored agent wallet integration models with AP2 payment mandates.[^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]

# References
- Working Group Governance: [Working Group Lifecycle](../governance/working-group-lifecycle.md)
- Foundation Taxonomy: [Taxonomy](../specification/taxonomy.md)

[^evt-wg-agentic-commerce-file-baf22ae9aa4b-28feda26]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-02-report.md
[^evt-wg-agentic-commerce-file-fa4050a9f626-c7520564]: https://github.com/aaif/wg-agentic-commerce/blob/8458b003a68de58c8bc24900ebd931d3112eb7ca/reporting/2026-07-report.md
