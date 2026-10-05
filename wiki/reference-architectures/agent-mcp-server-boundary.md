---
type: architecture
title: Agent to MCP Server Boundary Observability
description: Observability architecture and telemetry matrix defining context propagation,
  session versus request lifecycles, and evidence grades across Model Context Protocol
  boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/agent-mcp-server-boundary-deep-dive.md
tags:
- observability
- telemetry
- mcp
- architecture
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:55:01.516895+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/agent-mcp-server-boundary-deep-dive.md
  author: Empire Labs Pty Ltd
  last_modified: '2026-09-30T19:10:57+01:00'
- id: evt-wg-observability-and-traceability-pr-32
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
  author: narko4u
  last_modified: '2026-09-30T18:10:57+00:00'
---

# Overview
The Agent to MCP Server boundary observability architecture defines telemetry propagation, cross-boundary context correlation, and gap analysis for interactions between AI agents and Model Context Protocol servers [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]. While termed semantically as Agent to MCP Server, the underlying protocol transport executes between an MCP Client (such as a host application, agent runtime, or gateway) and an MCP Server over JSON-RPC 2.0 via stdio or Streamable HTTP [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

# Architecture / Specification
The specification separates session lifecycle instrumentation from request lifecycle instrumentation to prevent operational conflation [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]:
- **Session Lifecycle**: Spans connection establishment (`initialize` handshake, protocol capability negotiation), client and server metadata, capability sets, and session identity until shutdown or transport error [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].
- **Request Lifecycle**: Spans individual JSON-RPC method dispatches, request identifiers, parameter payloads, execution latencies, streaming progress subscriptions, and result or error outputs [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

Cross-boundary distributed tracing correlates client-side and server-side spans using W3C Trace Context propagated via `params._meta.traceparent` aligned with OpenTelemetry GenAI semantic conventions [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]. The architecture establishes that evidence grades are determined by telemetry consumers rather than producers, and highlights key open gaps including declared-versus-observed execution divergence, server-side side-effect manifests, and consent-chain verification [^evt-wg-observability-and-traceability-pr-32].

# References
See also [Agent-Tool CLI Boundary](../reference-architectures/agent-tool-cli-boundary.md) and [Agent Behavior Trace Model](../reference-architectures/agent-behavior-trace-model.md).

[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/agent-mcp-server-boundary-deep-dive.md
[^evt-wg-observability-and-traceability-pr-32]: https://github.com/aaif/wg-observability-and-traceability/pull/32
