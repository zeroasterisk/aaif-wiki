---
type: reference-architecture
title: Goose Agent Runtime Architecture
description: Reference architecture for Goose, an open-source general-purpose AI agent
  framework providing a full execution runtime with multi-turn loops, tool invocation,
  security scanning, ACP/MCP support, and multi-sink telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- agent-runtime
- goose
- mcp
- acp
- telemetry
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:00:16.963486+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Goose reference architecture specifies the system design of an open-source, general-purpose AI agent runtime that manages complete user sessions, multi-turn LLM reasoning loops, tool invocation, security enforcement, and multi-protocol integration across the Model Context Protocol (MCP) and [Agent Client Protocol](../proposals/agent-client-protocol.md).[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

Goose executes as a local background daemon (`goosed`) backed by an embedded SQLite database, exposing REST and Server-Sent Event (SSE) routes to terminal CLIs, desktop applications, and external IDE clients. It coordinates LLM provider communication, inspects tool execution permissions, applies pattern- and ML-based security scanners, and exports telemetry across multiple observability backends.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

# Architecture / Specification

### System Components

- **Core Runtime & Router**: Built on Rust and Axum, the `goose-server` handles session lifecycle, recipes, scheduling, context compaction, and subagent delegation.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Protocol Integration**: Supports ACP for bi-directional editor integration and MCP (stdio and SSE transports) for dynamically discovering and launching third-party tool extensions.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Security and Policy**: Features a Permission Inspector and Security Manager that scan incoming commands and tool inputs against dangerous patterns and model-based anomaly filters.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]
- **Observability Stack**: Emits structured Rust `tracing` events routed through dedicated subscriber layers to [OpenTelemetry](../reference-architectures/opentelemetry.md) collectors, [Langfuse](../reference-architectures/langfuse.md) for hierarchical LLM generation tracing, and [PostHog](../reference-architectures/posthog.md) for sanitized behavioral analytics.[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]

# References

- [Goose Project Repository](https://github.com/aaif-goose/goose)
- [Agent Client Protocol Proposal](../proposals/agent-client-protocol.md)
- [Langfuse Reference Architecture](../reference-architectures/langfuse.md)
- [PostHog Reference Architecture](../reference-architectures/posthog.md)

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
