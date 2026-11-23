---
type: resource
title: Goose Agent Framework and Runtime
description: Open-source general-purpose agent framework and Rust runtime coordinating
  multi-turn tool calling, ACP and MCP extension interfaces, and OpenTelemetry and
  Langfuse telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- agent-runtime
- reference-architecture
- mcp
- acp
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:49:56.541571+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Goose is an open-source general-purpose AI agent framework and runtime providing an autonomous execution loop for LLM-driven tool calling, security scanning, and multi-protocol extensibility [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Implemented in Rust, Goose operates as a local server daemon (`goosed`) and command-line interface (`goose`) that connects desktop clients, IDEs, and terminal environments to foundational model providers and external tools [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification
Goose operates at the system runtime layer, coordinating the complete agent execution lifecycle across several core subsystems [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]:

- **Server and API Tier (`goose-server` / `goosed`)**: Built on the Axum web framework, exposing endpoints for inference replies (`/reply`), session management (`/session`), streaming event notifications (`/session_events` via Server-Sent Events), configuration, scheduling, and proxy interfaces (`/mcp_app_proxy`, `/mcp_ui_proxy`) [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Client Interfaces**: Supports multiple interaction surfaces including the `goose-cli` terminal client, an Electron desktop application, and third-party code editors (such as JetBrains and Zed) communicating over the [Agent Client Protocol (ACP)](../standards/agent-client-protocol.md) via `stdio` [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Agent Core and Execution Loop**: Coordinates multi-turn conversation context, context compaction, and subagent delegation. It integrates provider chat integrations supporting over 15 LLM backends, alongside a Permission Inspector and a Security Manager that pairs pattern matching with ML scanners [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Extension Protocols**: Connects to tool extensions using the Model Context Protocol ([MCP](../standards/agent-plugins.md)) over `stdio` and SSE transports [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **State Storage**: Persists local conversation histories and session checkpoints in an embedded SQLite database using `sqlx` [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Observability and Telemetry**: Emits structured traces via dual telemetry channels: an [OpenTelemetry](../resources/opentelemetry.md) collector exporter (HTTP/protobuf on port 4318) capturing `agent_reply`, `provider_chat`, and `tool_execution` spans, and direct generation observation traces exported to [Langfuse](../resources/langfuse.md) [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Lifecycle History
The AAIF Observability and Traceability Working Group documented the reference architecture for Goose v1.39.0 on 2026-06-29 under the AI agent observability landscape [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
