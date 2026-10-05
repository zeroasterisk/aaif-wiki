---
type: reference-architecture
title: Agent Trace Specification Reference Architecture
description: Reference architecture capturing line-level AI code attribution traces
  locally via editor hooks into append-only JSONL files.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
tags:
- observability
- agent-trace
- provenance
- code-attribution
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:04.610410+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Agent Trace reference architecture demonstrates how AI coding agents emit line-level code attribution traces using the Agent Trace open specification, enabling vendor-neutral tracking of which AI models produced which lines of code in a version-controlled repository [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]. It is maintained under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing landscape [^evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6].

# Architecture / Specification

Agent Trace operates inside single agent invocations at the primitive execution layer [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]. It records write-path events directly as JSONL records persisted in `.agent-trace/traces.jsonl`:

- **Hook Dispatch**: Listens to IDE and agent runtime hook events such as `afterFileEdit`, `afterTabFileEdit`, `afterShellExecution` (Cursor), or `PostToolUse` (Claude Code) [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Local-First Trace Capture**: Formats execution traces into structured records with file diffs, prompt conversation IDs, contributor model metadata, and version control revision bindings [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **No External Collector Dependency**: Storage relies on local append-only JSONL files without requiring external SaaS ingest pipelines on the critical path [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

# References

- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)
- [OpenTelemetry Reference Architecture](opentelemetry.md)

[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/agent-trace.md
