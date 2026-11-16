---
type: taxonomy
title: Infrastructure
description: The runtime, orchestration, networking, messaging, and data services
  supporting agent execution, distinct from tools and harnesses.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/105
tags:
- taxonomy
- infrastructure
- runtime
- architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:14.647197+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-105
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/105
  author: jordanauge
  last_modified: '2026-11-10T17:33:09+00:00'
---

# Overview
Infrastructure encompasses the runtime, orchestration, networking, messaging, and data services upon which an AI agent operates [^evt-ws-taxonomy-landscape-pr-105]. Voted as a universal taxonomy term within the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) Deliverable 1 glossary, it demarcates foundational execution environments from cognitive frameworks and external integrations [^evt-ws-taxonomy-landscape-pr-105].

# Architecture / Specification
The term establishes a taxonomic boundary separating infrastructure layers from higher-level agent components [^evt-ws-taxonomy-landscape-pr-105]:
- **Boundary from Harness and Tools**: Infrastructure provides foundational compute platforms and communication fabrics, distinctly separated from agent harness scaffolding and callable [tools](../taxonomy/tool.md).
- **Failure Attribution**: Establishes an explicit order of attribution when diagnosing agent anomalies, isolating whether failures originate in underlying network, storage, and orchestration platforms or within agent reasoning and tool interfaces.

# References
- Taxonomy workstream PR #105 [^evt-ws-taxonomy-landscape-pr-105]

[^evt-ws-taxonomy-landscape-pr-105]: https://github.com/aaif/ws-taxonomy-landscape/pull/105
