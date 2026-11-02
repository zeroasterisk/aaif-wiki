---
type: resource
title: Goose Reference Architecture
description: Reference architecture for Goose, an open-source general-purpose AI agent
  runtime with built-in telemetry, security scanning, MCP, and ACP extensibility.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- agent-runtime
- observability
- mcp
- acp
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:47:34.950979+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Goose is an open-source, general-purpose AI agent runtime that executes multi-turn tool workflows driven by large language models, providing integrated telemetry collection, security filtering, and permission management.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c] It operates as a local service binding desktop or terminal interfaces to language model providers and local extension processes using the Model Context Protocol (MCP) and [Agent Client Protocol](../standards/agent-client-protocol.md).[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

# Architecture / Specification
The Goose architecture operates at the system runtime layer and is partitioned across user interfaces, a centralized daemon server, and an extensible agent core.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

## Interface Layer
Goose supports multiple client surfaces interacting with the underlying daemon:
- **CLI (`goose-cli`)**: Terminal interface communicating over REST and Server-Sent Events (SSE).[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Desktop Application**: Electron-based interface connecting to the daemon over local REST and SSE endpoints.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **ACP Clients**: Direct editor integrations (such as JetBrains and Zed) connecting via the [Agent Client Protocol](../standards/agent-client-protocol.md) over standard input/output (stdio).[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

## Server Daemon (`goosed`)
The core service is implemented in Rust using an Axum HTTP router, exposing endpoints for session management (`/session`), reply streaming (`/reply`), event broadcasting (`/session_events`), configuration, recipes, scheduling, telemetry, and MCP proxies.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c] State persistence relies on an embedded SQLite database managed through `sqlx`.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

## Agent Core and Execution Loop
The agent core coordinates:
- **Provider Manager**: Interfaces with over 15 language model providers using API keys or OAuth credentials.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Permission Inspector**: Evaluates tool calls against configured user authorization policies.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Security Manager**: Combines regex pattern filtering with machine learning scanners to detect prompt injection and dangerous invocations prior to tool execution.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Execution Loop**: Handles iterative request cycles, subagent delegation, context compaction, and MCP extension invocation over stdio or SSE transports.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

## Observability and Telemetry
Goose emits native distributed tracing and telemetry:
- **OpenTelemetry Export**: Emits hierarchical spans (`agent_reply`, `provider_chat`, and `tool_execution`) over OTLP HTTP/protobuf to an [OpenTelemetry](../resources/opentelemetry.md) collector.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Langfuse Integration**: Direct integration with [Langfuse](../resources/langfuse.md) captures generation traces, token metrics, and multi-turn execution graphs.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

# References
- AAIF Working Group Observability and Traceability repository: https://github.com/aaif/wg-observability-and-traceability
- Goose source repository: https://github.com/aaif-goose/goose

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
