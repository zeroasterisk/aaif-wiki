---
type: resource
title: Goose Agent Runtime Reference Architecture
description: Open-source general-purpose AI agent framework providing a local multi-turn
  execution runtime, extension integration via MCP and ACP, and telemetry export to
  OpenTelemetry and Langfuse.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- runtime
- agent-framework
- mcp
- acp
- observability
- opentelemetry
- langfuse
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:13:09.843168+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Goose is an open-source general-purpose AI agent runtime providing an end-to-end execution loop for multi-turn LLM tool execution, security scanning, permission inspection, and protocol extensibility via the Model Context Protocol (MCP) and [Agent Client Protocol](../standards/agent-client-protocol.md)[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Operating as a local service binding a user's CLI or desktop environment to models and extension subprocesses, Goose manages session lifecycles, context compaction, and subagent delegation[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification

The Goose architecture spans three operational layers:

1. **User Interfaces**: Client interactions are driven through the `goose` CLI, an Electron desktop application, or external ACP-compatible IDE editors (such as JetBrains or Zed) connecting over standard input/output (stdio)[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
2. **Server Daemon (`goosed`)**: A local background service implemented in Rust using an Axum routing layer that exposes endpoints for chat sessions (`/reply`, `/session`, `/session_events`), configuration, MCP application proxies, and telemetry export[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Session state is persisted locally via SQLite through sqlx[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
3. **Agent Core**: Executes the agent loop (`request` → `provider_chat` → `tool_calls` → `permission_check` → execution) guarded by permission inspectors and a security manager combining heuristic rule patterns with ML scanners[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

### Observability and Telemetry

Goose natively supports dual telemetry export paths:
- **[OpenTelemetry](../resources/opentelemetry.md)**: Streams hierarchical spans (`agent_reply`, `provider_chat`, `tool_execution`) over HTTP/protobuf to an OTLP collector on port 4318[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **[Langfuse](../resources/langfuse.md)**: Emits trace observations and token metrics to self-hosted or cloud Langfuse backends for generation-level inspection[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Lifecycle History

Donated as a foundational project to the Agentic AI Foundation, Goose v1.39.0 was formally benchmarked and documented by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) in June 2026[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
