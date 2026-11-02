---
type: working-group
title: Agentic Commerce Working Group
description: Technical working group establishing vendor-neutral capability maps,
  protocol gap analyses, and reference flows for autonomous and mediated transactions.
resource: https://github.com/aaif/wg-agentic-commerce/issues/8
tags:
- commerce
- working-group
- governance
- retention
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:21:01.683717+00:00'
sources:
- id: evt-wg-agentic-commerce-issue-8
  resource: https://github.com/aaif/wg-agentic-commerce/issues/8
  author: smcd
  last_modified: '2026-10-09T22:35:12+00:00'
---

# Overview

The Agentic Commerce Working Group establishes vendor-neutral capability maps, protocol gap analyses, and reference architectures governing autonomous and agent-assisted commercial transactions. It evaluates commerce-enabling protocols across discovery, identity, cart management, checkout negotiation, and payment settlement to ensure operational safety and regulatory alignment.

# Architecture / Specification

The working group assesses emerging and legacy transaction protocols—including UCP, ACP, AP2, and x402—against standardized operational requirements. Key dimensions under development include:
- **Buyer Capacity and Verification**: Addressing legal capacity, minor principal delegations, and jurisdiction-specific age validation mandates where an agent transacts without a human present at checkout [^evt-wg-agentic-commerce-issue-8].
- **Multi-Layer Record Retention**: Specifying data retention obligations across AI safety mandates (such as EU AI Act provider and deployer log retention), personal data protection limits, and financial anti-money laundering (AML) regulatory periods [^evt-wg-agentic-commerce-issue-8].
- **Delegated Authority and Settlement**: Analyzing boundaries between autonomous decision-making and human authorization checkpoints across payment execution.

# Lifecycle History

Active discussions within the working group identified structural gaps in protocol scoring frameworks, specifically highlighting that capability maps must capture principal capacity verification and multi-tier evidentiary retention across commercial jurisdictions [^evt-wg-agentic-commerce-issue-8].

# References

- [Agentic Checkout](../taxonomy/agentic-checkout.md)
- [Agent-Initiated Transaction](../taxonomy/agent-initiated-transaction.md)
- [Delegated Payment](../taxonomy/delegated-payment.md)

[^evt-wg-agentic-commerce-issue-8]: https://github.com/aaif/wg-agentic-commerce/issues/8
