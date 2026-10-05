---
type: architecture
title: Agent Trace
description: Open specification and reference hook architecture capturing line-level
  code attribution traces emitted during AI coding agent sessions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
tags:
- observability
- telemetry
- tracing
- coding-agents
- attribution
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:16.200381+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Agent Trace is an open telemetry specification for capturing granular, line-level code attribution and execution history from AI coding agents like Cursor and Claude Code [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]. It operates as a local-first telemetry layer recording model provenance, prompt interactions, file edits, and shell command executions within a version-controlled repository [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

Maintained under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the architecture defines event dispatch hooks and structured JSONL append logging without requiring centralized collection backends [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

# Architecture / Specification

Agent Trace captures lifecycle hooks emitted during agent editing and execution sessions [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]:

- **Hook Dispatcher**: Intercepts IDE and agent events (`afterFileEdit`, `afterTabFileEdit`, `afterShellExecution`, `PostToolUse`, `sessionStart/End`) passed via JSON on standard input [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Trace Output**: Appends structured trace records to `.agent-trace/traces.jsonl`, binding edits to file paths, diffs, model identifiers, conversation context, and VCS revisions [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Decoupled Consumption**: Decouples write-path trace emission from downstream aggregation tools, CI policy gates, or compliance dashboards [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
