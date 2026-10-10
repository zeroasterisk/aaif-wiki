---
type: standard
title: Agent Trace Specification
description: Open specification and reference architecture for line-level AI code
  attribution tracing in version-controlled repositories.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/agent-trace.md
tags:
- standards
- agent-trace
- code-attribution
- observability
- git
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:55:28.695732+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/agent-trace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Agent Trace is an open RFC specification demonstrating how AI coding agents emit line-level code attribution traces to track which models produced specific file edits within a repository [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]. It addresses the need for vendor-neutral provenance of AI-generated source code across multi-agent coding sessions [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

The specification is tracked under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape catalog [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

# Architecture / Specification

Agent Trace operates as a local-first telemetry format without requiring an active external collector [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]:

- **Emission Hooks**: Coding assistants (e.g., Cursor hook events or Claude Code tool invocations) emit event payloads containing edited ranges, contributor metadata, and shell execution context [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Trace Dispatcher**: A local dispatcher formats the events and appends JSONL records to `.agent-trace/traces.jsonl` within the target repository [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **VCS Binding**: Traces reference local repository commits and revisions to provide auditable code provenance for downstream compliance and CI evaluation gates [^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/agent-trace.md
