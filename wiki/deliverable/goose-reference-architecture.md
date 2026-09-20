---
type: deliverable
title: Goose Reference Architecture
description: A reference architecture evaluating Goose agent runtime execution lifecycle,
  MCP/ACP extensibility, and OpenTelemetry/Langfuse export.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- observability
- reference-architecture
- goose
- agent-runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:26.447775+00:00'
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

The Goose Reference Architecture assesses Goose, an open-source general-purpose AI agent framework that provides a complete system runtime for LLM-driven tool execution with built-in observability, security scanning, permission management, and protocol extensibility [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Produced under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing landscape collection, this architecture analyzes agent execution across the five core AAIF evaluation dimensions [^evt-wg-observability-and-traceability-pr-20].

Goose operates at the system layer as a local service binding desktop and terminal sessions to LLM providers and extension processes, managing UI presentation, a local Axum REST/SSE API server (`goosed`), the multi-turn agent loop, context compaction, subagent delegation, session persistence, and telemetry export [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification

Goose integrates multiple functional subsystems into a cohesive execution environment [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]:

- **Client Interfaces**: Supports terminal CLI (`goose`), desktop Electron UI, and external editor clients (e.g., JetBrains, Zed) connecting via the Agent Client Protocol (ACP) over standard I/O [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Server & Agent Core**: An Axum HTTP server hosting the agent loop, permission inspector, ML-based security scanners, and provider integration supporting over 15 LLM backends [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Extension Protocols**: Connects tools via Model Context Protocol (MCP) over `stdio` and SSE transports [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Telemetry Pipelines**: Implements Rust `tracing` instrumentation exporting structured spans (`agent_reply`, `provider_chat`, `tool_execution`) to [OpenTelemetry Collector](../deliverable/opentelemetry-reference-architecture.md) endpoints and [Langfuse](../deliverable/langfuse-reference-architecture.md) backends [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Lifecycle History

- 2026-06-29: Added as part of the WG Observability & Traceability reference architecture landscape import [^evt-wg-observability-and-traceability-pr-20].

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
