---
type: deliverable
title: Agent Trace Reference Architecture
description: A reference architecture specifying line-level code attribution tracing
  for AI coding agents using the Agent Trace specification.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/agent-trace.md
tags:
- observability
- agent-trace
- code-attribution
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:51:45.199677+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/agent-trace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The Agent Trace Reference Architecture specifies a local-first instrumentation mechanism for AI coding agents to emit line-level code attribution traces into version-controlled repositories[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]. Developed under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it enables vendor-neutral verification of AI model contributions during automated file edits and tool executions[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

# Architecture / Specification
The specification operates within a single invocation session without requiring external collector backends[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]:
- **Hook Integration**: Hooks into IDE and agent runtime lifecycle events such as `afterFileEdit`, `afterTabFileEdit`, and `PostToolUse`[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Local Persistence**: Records trace data as newline-delimited JSON (`.agent-trace/traces.jsonl`) bound to version control revisions[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].
- **Attribution Metadata**: Captures contributor identities, active models, modified file ranges, and conversation session IDs[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756].

[^evt-wg-observability-and-traceability-file-58f77875accc-fcdb4756]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/agent-trace.md
