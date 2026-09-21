---
type: reference-architecture
title: 'Reference Architecture: Goose'
description: Reference architecture for Goose, an open-source general-purpose AI agent
  runtime with built-in telemetry, security scanning, and protocol extensibility.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- observability
- reference-architecture
- agent-runtime
- goose
- mcp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:30.127413+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-pr-20
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/20
  author: MatthewKhouzam
  last_modified: '2026-08-19T19:04:49+00:00'
---

# Overview
Goose is an open-source, general-purpose AI agent framework and local runtime that manages LLM-driven tool execution with integrated observability, security scanning, permission management, and extensibility via the Model Context Protocol (MCP) and Agent Client Protocol (ACP)[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Operating as a system-layer local daemon (`goosed`) and CLI/desktop client, Goose orchestrates multi-turn tool execution loops, context compaction, and subagent delegation across multiple LLM providers[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification
The Goose architecture comprises a client presentation tier (CLI, Electron desktop, ACP clients), an Axum-based HTTP/SSE server (`goosed`), and an Agent Core incorporating provider chat clients, permission inspection, ML/pattern-based security management, and session state persistence in SQLite[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Observability instrumentation is implemented via Rust's `tracing` ecosystem, emitting structured execution traces (`agent_reply`, `provider_chat`, `tool_execution`) to sinks including OpenTelemetry collectors ([../reference-architectures/opentelemetry.md](opentelemetry.md)) and Langfuse ([../reference-architectures/langfuse.md](langfuse.md))[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# References
- Goose Reference Architecture by [../working-groups/observability-and-traceability.md](observability-and-traceability.md)[^evt-wg-observability-and-traceability-pr-20]

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
