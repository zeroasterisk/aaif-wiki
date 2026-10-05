---
type: reference-architecture
title: Agent to MCP Server Boundary Observability
description: Cross-boundary telemetry model defining session versus request lifecycles,
  span correlation, and evidence capture across MCP client and server boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/agent-mcp-server-boundary-deep-dive.md
tags:
- observability
- mcp
- telemetry
- opentelemetry
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:20:53.122084+00:00'
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

The Agent to MCP Server boundary observability architecture defines the separation of semantic agent interactions from underlying Model Context Protocol (MCP) transport and client boundaries [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]. In standard deployments, the initiating agent or host application acts via an MCP Client communicating over JSON-RPC 2.0 (stdio or Streamable HTTP) to an MCP Server [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

# Architecture / Specification

The boundary model explicitly distinguishes between two independent lifecycles [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]:

1. **Session Lifecycle**: Established once per connection during protocol initialization and capability negotiation (`clientInfo`, `serverInfo`, protocol version), terminating upon shutdown or transport failure [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].
2. **Request Lifecycle**: Measured per JSON-RPC request (e.g., `tools/call`), capturing method names, request IDs, parameters, errors, and granular duration independently of overall session health [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

Distributed context is propagated using OpenTelemetry GenAI semantic conventions across W3C trace context passed via `params._meta.traceparent` [^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711].

# References

- Related: `../reference-architectures/agent-tool-cli-boundary.md`
- Related: `../reference-architectures/opentelemetry.md`
- Related: `../working-groups/observability-and-traceability.md`

[^evt-wg-observability-and-traceability-file-462a9edc1364-8b0b8711]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/working-documents/agent-mcp-server-boundary-deep-dive.md
