---
type: working-group
title: Agentic Commerce Working Group
description: Technical working group establishing vendor-neutral capability maps,
  protocol alignments, buyer capacity verification, and dispute standards for autonomous
  commercial transactions.
resource: https://github.com/aaif/wg-agentic-commerce/issues/8
tags:
- working-group
- commerce
- payments
- identity
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:21:46.728232+00:00'
sources:
- id: evt-wg-agentic-commerce-issue-8
  resource: https://github.com/aaif/wg-agentic-commerce/issues/8
  author: smcd
  last_modified: '2026-10-09T22:35:12+00:00'
---

# Overview

The Agentic Commerce Working Group standardizes protocols, capability maps, and transaction lifecycle models for autonomous and semi-autonomous commercial interactions. Its scope spans identity delegation, checkout flows, payment settlement interfaces, and dispute arbitration across agent-to-merchant and agent-to-agent transactions.

Workstreams include the comparative evaluation of emerging commerce specifications against legal frameworks governing principal capacity and statutory data retention [^evt-wg-agentic-commerce-issue-8].

# Architecture / Specification

### Capability Mapping and Protocol Evaluation

The working group benchmarks emerging commerce protocols against enterprise and regulatory requirements, prioritizing two missing protocol dimensions [^evt-wg-agentic-commerce-issue-8]:

1. **Buyer Legal Capacity and Age**: Commercial protocols currently lack standardized attributes asserting principal capacity or minor status. Because delegation from minors may be legally void or voidable, and age-restricted goods require legal verification of the [Principal](../taxonomy/principal.md) rather than the autonomous agent, protocol identity layers must explicitly support verifiable capacity attestations [^evt-wg-agentic-commerce-issue-8].
2. **Layered Record Retention Matrix**: Autonomous transactions distribute recordkeeping across new intermediary entities. The group is drafting a multi-layered retention model encompassing:
   - *AI Governance Layer*: Mandated six-month log retention for high-risk deployments under Article 19 and Article 26(6) of the EU AI Act [^evt-wg-agentic-commerce-issue-8].
   - *Personal Data Layer*: Data protection storage limitations defining statutory retention ceilings [^evt-wg-agentic-commerce-issue-8].
   - *Financial Compliance Layer*: Anti-money laundering and electronic funds transfer preservation periods (e.g., five years under the US Bank Secrecy Act and EU AMLD, and two years under Regulation E) [^evt-wg-agentic-commerce-issue-8].

# Lifecycle History

- Issue #8 opened discussion on protocol capability scorecards, highlighting gaps in capacity verification and cross-jurisdictional transaction log retention duties [^evt-wg-agentic-commerce-issue-8].

[^evt-wg-agentic-commerce-issue-8]: https://github.com/aaif/wg-agentic-commerce/issues/8
