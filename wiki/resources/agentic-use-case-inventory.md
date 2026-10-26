---
type: resource
title: Agentic Use Case Inventory
description: Production workflow repository classifying real-world agent deployments
  under verified multi-tiered evidentiary standards.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
tags:
- workflows
- use-cases
- inventory
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:45:03.901065+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:36:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-46
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
  author: jodeev
  last_modified: '2026-10-01T14:36:15+00:00'
---

# Overview

The Agentic Use Case Inventory is a curated repository of production agentic workflows maintained by the Critical Use Cases Workstream within the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]. Each entry documents an explicit, real-world implementation choice across varied industry verticals, serving as empirical evidence to identify recurring architectural patterns and workflow topologies [^evt-wg-workflows-and-process-integration-pr-46].

Workflows in the inventory are mapped against the five structural dimensions defined in the [Agentic Use Case Classification Schema](../resources/agentic-use-case-classification.md) [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].

# Architecture / Specification

### Evidentiary Standard

To ensure academic and operational rigor, all rows in the inventory must cite publicly accessible, independently verifiable proof of production deployment [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]. Unverifiable claims and personal assertions are explicitly disallowed. The workstream enforces a three-tier source qualification standard [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]:

1. **Preferred Sources**: Primary vendor product announcements or documentation confirming a named customer deployment operating in production (e.g., enterprise pairings demonstrating live utilization).
2. **Acceptable Sources**: Vendor product pages detailing explicit feature architectures clearly deployed at scale, even if specific customer identities are omitted.
3. **Unacceptable Sources**: Secondary blogs, analyst reports, market projection statistics, academic whitepapers, individual implementer blogs, and private knowledge.

Each inventory entry requires at least one verified primary citation, with three independent citations established as the operational target [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]. Technical guides and whitepapers may be used secondarily within classification notes to explain mechanics, provided they directly reference a qualified production vendor [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303].

### Derivation of Workflow Shapes

The inventory enables the automated derivation of recurring workflow shapes by analyzing structural dimension frequencies across domains [^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]. This empirical grounding allows the working group to prioritize reference architecture patterns based on demonstrated industry prevalence rather than speculative designs.

# Lifecycle History

Established under PR #46, the inventory structure and evidentiary rules achieved review readiness for Working Group approval in late 2026, with row-level citations undergoing continuous community verification [^evt-wg-workflows-and-process-integration-pr-46].

# References

- Companion schema: [Agentic Use Case Classification](../resources/agentic-use-case-classification.md)
- Working group: [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-file-5028db4c24a1-b054a303]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/README.md
[^evt-wg-workflows-and-process-integration-pr-46]: https://github.com/aaif/wg-workflows-and-process-integration/pull/46
