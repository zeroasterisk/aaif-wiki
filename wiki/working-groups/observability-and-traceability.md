---
type: working-group
title: Observability and Traceability Working Group
description: Technical working group establishing vendor-neutral agent telemetry standards,
  cross-boundary trace correlation, and compliance-aware evidence models.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/71
tags:
- working-group
- observability
- opentelemetry
- tracing
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:33:38.696754+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-71
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/71
  author: mr-lee
  last_modified: '2026-11-02T02:43:16+00:00'
- id: evt-wg-observability-and-traceability-pr-72
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/72
  author: mr-lee
  last_modified: '2026-11-02T02:43:22+00:00'
- id: evt-wg-observability-and-traceability-pr-73
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/73
  author: mr-lee
  last_modified: '2026-11-02T02:49:14+00:00'
- id: evt-wg-observability-and-traceability-pr-74
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/74
  author: mr-lee
  last_modified: '2026-11-02T06:07:46+00:00'
---

# Overview

The Observability and Traceability Working Group is an AAIF technical body tasked with establishing vendor-neutral telemetry specifications, distributed tracing conventions, and evaluation frameworks for AI agent architectures.[^evt-wg-observability-and-traceability-pr-73] The group harmonizes telemetry across client SDKs, gateway proxies, tool sandboxes, and execution runtimes while liaising directly with upstream standards bodies such as OpenTelemetry.[^evt-wg-observability-and-traceability-pr-72][^evt-wg-observability-and-traceability-pr-73]

# Architecture / Specification

### Active Deliverables and Workstreams

- **[Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)**: Standardizing span graphs, causal linking, and execution models. Recent work includes a gap analysis identifying seven major OpenTelemetry instrumentation shortfalls in agent SDKs and coding tools,[^evt-wg-observability-and-traceability-pr-71] and a formal proposal standardizing Turn, Agent Step, and Turn Segment semantics.[^evt-wg-observability-and-traceability-pr-72]
- **[Agent Observability Use Cases](../resources/agent-observability-use-cases.md)**: Cataloging diagnostic, operational, and audit profiles, including GDPR- and AI Act-compliant evidence retention with typed tombstones.[^evt-wg-observability-and-traceability-pr-71]
- **Cross-Boundary Telemetry Models**: Defining correlation headers across MCP server, subprocess CLI, and agent-to-agent boundaries.

### Upstream Liaisons

The working group maintains a structured liaison roster (`LIAISONS.md`) tracking outbound follow-ups and inbound requests across peer foundations and standards initiatives.[^evt-wg-observability-and-traceability-pr-73] Primary upstream collaboration focuses on the OpenTelemetry GenAI SIG to contribute native agent semantic conventions.[^evt-wg-observability-and-traceability-pr-72][^evt-wg-observability-and-traceability-pr-73]

# Lifecycle History

- **October 2026**: Established the working group liaison roster tracking formal touchpoints with OpenTelemetry and partner foundations.[^evt-wg-observability-and-traceability-pr-73]
- **October 2026**: Published Gap Analysis for the Agent Behavior Trace Model and scheduled upstream turn modeling proposals for the OpenTelemetry GenAI SIG.[^evt-wg-observability-and-traceability-pr-71][^evt-wg-observability-and-traceability-pr-72]
- **October 2026**: Submitted monthly working group operating report.[^evt-wg-observability-and-traceability-pr-74]

# References

- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [Agent Observability Use Cases Catalog](../resources/agent-observability-use-cases.md)
- [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md)
- [Working Group Reporting Template](../guidelines/working-group-reporting-template.md)

[^evt-wg-observability-and-traceability-pr-71]: https://github.com/aaif/wg-observability-and-traceability/pull/71
[^evt-wg-observability-and-traceability-pr-72]: https://github.com/aaif/wg-observability-and-traceability/pull/72
[^evt-wg-observability-and-traceability-pr-73]: https://github.com/aaif/wg-observability-and-traceability/pull/73
[^evt-wg-observability-and-traceability-pr-74]: https://github.com/aaif/wg-observability-and-traceability/pull/74
