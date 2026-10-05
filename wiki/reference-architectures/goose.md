---
type: architecture
title: Goose Reference Architecture
description: Open-source extensible AI agent runtime integrating multi-turn tool execution,
  permission management, Model Context Protocol, and multi-sink telemetry export.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- agent-runtime
- mcp
- acp
- rust
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Goose is an open-source, general-purpose desktop and terminal AI agent runtime written in Rust [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. It coordinates the entire execution loop between client interfaces, LLM inference providers, extension capabilities via the Model Context Protocol (MCP) and [Agent Client Protocol](../projects/agent-client-protocol.md), security validation layers, and distributed telemetry export sinks [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification

The Goose system architecture consists of four primary structural tiers [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]:

- **Client Interfaces**: CLI binary (`goose`), Electron desktop application, or external IDE extensions communicating via REST, SSE, or stdio ACP [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Goose Server (`goosed`)**: Axum-based HTTP server managing session persistence in SQLite, context window compaction, permission gating, and scheduled execution [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Agent Core & Extension Engine**: Orchestrates multi-turn model interaction (`provider_chat`), security inspection (regex and ML scanners), and subagent delegation across local and remote MCP extensions [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Observability Layer**: Emits hierarchical spans (`agent_reply`, `provider_chat`, `tool_execution`) simultaneously to [OpenTelemetry](../reference-architectures/opentelemetry.md) collectors, [Langfuse](../reference-architectures/langfuse.md) tracing servers, and [PostHog](../reference-architectures/posthog.md) product analytics [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# References

- Goose Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
