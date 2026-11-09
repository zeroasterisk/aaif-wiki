---
type: working-group
title: Observability and Traceability Working Group
description: AAIF technical working group establishing vendor-neutral agent telemetry
  standards, OpenTelemetry semantic conventions, and cross-framework trace interoperability.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/bbcac36693002be677c403bff7e400c15b23f39d/README.md
tags:
- governance
- working-group
- observability
- telemetry
- opentelemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:32:01.978591+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b33563055168-1e66868d
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/bbcac36693002be677c403bff7e400c15b23f39d/README.md
  author: Matt Lee
  last_modified: '2026-11-04T13:50:31+00:00'
- id: evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/bbcac36693002be677c403bff7e400c15b23f39d/LIAISONS.md
  author: Matt Lee
  last_modified: '2026-11-04T13:50:31+00:00'
---

# Overview
The Observability and Traceability Working Group is an Agentic AI Foundation technical body convening practitioners, platform vendors, and standards organizations to standardize agent observability signals, execution traces, and telemetry conventions.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d] The working group focuses on the intersection of agent reasoning, state transitions, and tool interactions with standard distributed tracing frameworks, emphasizing vendor-neutral interoperability across heterogeneous agent runtimes.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]

# Architecture / Specification

## Governance and Leadership
The working group operates under technical foundation governance with leadership appointed by Platinum and Gold members:[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- **Chair:** Pavan Sudheendra (Cisco)[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- **Co-Chair:** Matthew Lee (Datadog)[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- **Term of Office:** March 1, 2026 – January 31, 2027.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- **Meeting Cadence:** Biweekly on Wednesdays at 10:00 AM Pacific Time.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]

GitHub issues and pull requests serve as the primary source of record for durable status and consensus tracking, supported by recorded meetings and public mailing list archives.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]

## Core Deliverables and Workstreams
The working group maintains several foundational assets:
- **Agent Behavior Trace Model (ABTM):** A structured execution plan and vendor-neutral specification establishing semantic conventions for agent execution graphs, turns, and step spans.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d][^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]
- **Prior Work Survey:** A living comparative survey evaluating current agent observability specifications, APM tools, and distributed tracing protocols.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- **Observability Use Cases Inventory:** A practitioner-focused catalog documenting requirements across agent debugging, cost attribution, and behavioral compliance.[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]

## Liaison and Coordination Network
The working group maintains an active liaison roster tracking bidirectional coordination across industry standards and internal AAIF groups:[^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]
- **External Standards:** Primary liaison with the OpenTelemetry GenAI SIG (advancing turn and step span proposals), Agent Trace (Cursor), AGNTCY, libp2p, HOL, and Agent Action Capsule.[^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]
- **Foundation Workstreams:** Active collaboration with the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) (aligning terminology such as Turn and Agent Step), the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) (capturing agent evaluation telemetry), and the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]
- **Platform Reference Proving Grounds:** Coordination with AAIF implementation efforts including Goose, Model Context Protocol (MCP), and Agentic Resource Discovery (ARD).[^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]

# References
- Specification work: [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- Ecosystem analysis: [Agent Observability Prior Work](../resources/agent-observability-prior-work.md)[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]
- Requirements mapping: [Agent Observability Use Cases](../resources/agent-observability-use-cases.md)[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]

[^evt-wg-observability-and-traceability-file-b33563055168-1e66868d]: https://github.com/aaif/wg-observability-and-traceability/blob/bbcac36693002be677c403bff7e400c15b23f39d/README.md
[^evt-wg-observability-and-traceability-file-f5077fe55915-f29d3cf9]: https://github.com/aaif/wg-observability-and-traceability/blob/bbcac36693002be677c403bff7e400c15b23f39d/LIAISONS.md
