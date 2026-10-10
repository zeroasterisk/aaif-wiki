---
type: resource
title: Agent to MCP Server Boundary Deep-Dive
description: Observability reference matrix and telemetry propagation model analyzing
  the protocol boundary between MCP clients and MCP servers.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-mcp-server-boundary-deep-dive.md
tags:
- observability
- mcp
- telemetry
- tracing
- opentelemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:14:36.909764+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-mcp-server-boundary-deep-dive.md
  author: Empire Labs Pty Ltd
  last_modified: '2026-09-30T19:10:57+01:00'
- id: evt-wg-observability-and-traceability-pr-32
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
  author: narko4u
  last_modified: '2026-09-30T18:10:57+00:00'
---

# Overview
The Agent to MCP Server boundary deep-dive defines the observability requirements, metadata field mappings, and telemetry propagation mechanisms across the Model Context Protocol (MCP) boundary[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]. While conceptually labeled as an Agent → MCP Server relationship, the operational protocol boundary occurs between an MCP Client (often a host application, agent runtime, or gateway) and an MCP Server over JSON-RPC 2.0 transport[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

# Architecture / Specification
The specification separates lifecycle concerns and trace propagation rules into distinct architectural layers:

- **Session Lifecycle vs. Request Lifecycle**: Session lifecycle governs connection initialization, capability negotiation (`clientInfo`, `serverInfo`, protocol version), and transport state over stdio or Streamable HTTP. Request lifecycle governs individual JSON-RPC invocations, parameters, results, streaming responses, and errors. The two must be instrumented independently so request-level errors do not corrupt session metadata[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].
- **Context Propagation**: Distributed trace context across client and server spans is correlated via W3C trace context passed within the `params._meta.traceparent` protocol field, aligning with OpenTelemetry GenAI MCP semantic conventions[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].
- **Core Observability Matrix Dimensions**: Maps identity, context, relationship, lifecycle, outcome, provenance, security, and timing across declared and observed states[^evt-wg-observability-pr-32].
- **Load-Bearing Open Gaps**: Identifies divergences between declared tool capabilities and runtime observed behavior, missing server-side side-effect manifests, consent-chain observability, and consumer-evaluated evidence integrity[^evt-wg-observability-pr-32].

# Lifecycle History
Developed under the Observability and Traceability Working Group ([`../working-groups/observability-and-traceability.md`](../working-groups/observability-and-traceability.md)) as part of the cross-boundary observability work package complementing the Agent to CLI tool model in [`../resources/agent-tool-cli-boundary.md`](../resources/agent-tool-cli-boundary.md)[^evt-wg-observability-pr-32].

[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-mcp-server-boundary-deep-dive.md
