---
type: deliverable
title: Agent to MCP Server Boundary Deep Dive
description: Analysis of cross-boundary observability across Model Context Protocol
  (MCP) connections, addressing declared-versus-observed divergence and evidence integrity.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
tags:
- observability
- mcp
- telemetry
- provenance
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:09:17.009858+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-32
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
  author: narko4u
  last_modified: '2026-09-19T04:56:36+00:00'
---

# Overview

The Agent to MCP Server boundary deep dive specifies the cross-boundary observability model when an agent interacts with external tools, resources, and prompts exposed via the Model Context Protocol (MCP) [^evt-wg-observability-and-traceability-pr-32]. Developed under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it maps MCP communication into the standardized eight-field cross-boundary telemetry matrix [^evt-wg-observability-and-traceability-pr-32].

# Architecture / Specification

### Telemetry Matrix Coverage

The deep dive aligns MCP protocol operations with the cross-boundary observability framework across eight core dimensions [^evt-wg-observability-and-traceability-pr-32]:
- **Identity**: MCP client/server identification, protocol versioning, and server-advertised capabilities.
- **Context**: Trace context propagation over MCP transports (JSON-RPC over stdio, SSE, or WebSockets).
- **Relationship**: Correlation between agent decision spans, MCP request/response cycles, and downstream side-effects.
- **Lifecycle**: Phased telemetry covering transport handshake, capability negotiation, tool invocation, and connection teardown.
- **Outcome**: Protocol-level error codes, application-level tool failures, and schema validation errors.
- **Provenance**: Lineage of returned context data, prompt expansions, and resource reads injected into model context.
- **Security**: Authentication credentials, authorization boundaries, and consent-chain verification.
- **Timing**: Transport transit latencies, queue durations, and tool execution runtimes [^evt-wg-observability-and-traceability-pr-32].

### Key Gaps and Challenges

The document highlights critical structural gaps in current MCP observability [^evt-wg-observability-and-traceability-pr-32]:
- **Declared vs. Observed Divergence**: Discrepancies between tool contracts declared during capability exchange and actual runtime behavior observed during execution.
- **Evidence Integrity**: Lack of cryptographic verification or tamper-evident logging for MCP response payloads.
- **Server-Side Side-Effect Manifests**: Inability of clients to deterministically observe state changes performed by autonomous MCP servers.
- **Consent-Chain Observability**: Telemetry blind spots when multi-party user consent flows span across MCP boundaries [^evt-wg-observability-and-traceability-pr-32].

[^evt-wg-observability-and-traceability-pr-32]: https://github.com/aaif/wg-observability-and-traceability/pull/32
