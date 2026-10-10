---
type: resource
title: Goose Agent Runtime
description: Open-source general-purpose AI agent framework providing local multi-turn
  execution, tool invocation, permission guardrails, and telemetry export.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
tags:
- agent-runtime
- mcp
- acp
- observability
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Goose is an open-source, general-purpose AI agent runtime that manages complete user desktop and CLI sessions, multi-turn LLM reasoning loops, extension orchestration, and operational telemetry [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]. Implemented in Rust, Goose operates as a local process (`goosed` / `goose-cli`) mediating interactions between client user interfaces, LLM backend providers, and external tools integrated via the Model Context Protocol (MCP) and [Agent Client Protocol](../standards/agent-client-protocol.md) [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

# Architecture / Specification

The Goose system architecture consists of several specialized subsystems [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]:

- **API & Routing Layer**: An Axum-based web router exposing REST and Server-Sent Events (SSE) endpoints for session state, chat replies, recipe execution, and tool proxying [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Agent Loop & Context Engine**: Coordinates prompt templating, multi-turn tool calling, context compaction, and subagent delegation [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Security & Permission Gateways**: Enforces security policies using pattern matching and ML scanners, coupled with explicit [human approval gates](../patterns/human-approval-gate.md) before executing high-risk tools [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].
- **Observability Pipeline**: Provides native distributed tracing through [OpenTelemetry](../resources/opentelemetry.md) collector export (OTLP over HTTP/protobuf), Langfuse trace integration, and privacy-sanitized analytics ingestion to [PostHog](../resources/posthog.md) [^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c].

[^evt-wg-observability-and-traceability-file-ebe69a7a8f5d-31c4429c]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-GOOSE.md
