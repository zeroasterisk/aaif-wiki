---
type: resource
title: Agent-to-Tool Local CLI Boundary Deep Dive
description: Observability reference matrix and context propagation model analyzing
  direct agent invocations of local CLI child processes.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
tags:
- observability
- traceability
- cli
- tools
- opentelemetry
- w3c-trace-context
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:19:23.017127+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1699fc75df72-8956556b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
  author: Me1iodas
  last_modified: '2026-09-10T12:16:43+01:00'
---

# Overview
The Agent-to-Tool Local CLI Boundary Deep Dive establishes a telemetry reference matrix and context propagation architecture for direct agent invocations of local command-line interface (CLI) subprocesses [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]. When an agent launches an operating system subprocess directly without an intermediary skill runtime, the boundary bridges both an agent-level semantic decision (`Agent → Tool`) and an operating-system process execution (`Agent Runtime → Local Process`) [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b].

# Architecture / Specification
The boundary spans two interconnected execution surfaces: an agent execution surface where tool call identification, parameter serialization, and security policy checks occur, and an operating-system process surface where environment variables are constructed, child processes are spawned, and exit codes are observed [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b].

The causal invocation model follows:
- Upstream caller / turn
  - Tool execution span (`Agent → Tool` semantic boundary)
    - Optional CLI caller span
      - Local CLI execution span (`Agent Runtime → Local Process` boundary)
        - Downstream CLI operations

The matrix analyzes six observable telemetry dimensions across the boundary [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]:
- **Identity**: Binds agent, principal, turn/session, `gen_ai.tool.name`, `gen_ai.tool.call.id`, executable path, and process ID (PID). A critical remaining gap is the absence of an immutable binding between the tool call, the binary digest/version, and the delegating principal.
- **Context**: Propagates active trace context and optional baggage across the boundary using the OpenTelemetry environment-variable carrier specification (`TRACEPARENT`, `TRACESTATE`, `BAGGAGE`). Context must cross before process invocation; post-hoc transcript parsing cannot supply child-visible parent spans.
- **Relationship**: Preserves causal parent-child hierarchy from agent turn to tool span and process span. For detached, background, or fire-and-forget tasks, OpenTelemetry Span Links represent ownership to avoid misrepresenting lifecycle duration.
- **Lifecycle**: Maps the transition sequence `selected → authorized/denied → context prepared → spawn requested → process started → running → exited/errored/timed out/canceled`.
- **Outcome**: Captures process exit codes (`process.exit.code`), structured execution errors (`error.type`), partial standard output/error, and compensation results.
- **Provenance**: Records the tool schema source, invocation plugin, executable path, and observer attribution metadata.

# Lifecycle History
Authored by `@fangxiu-wf` for the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) in response to working group issue #29, this reference document incorporates real-world validation from the LoongSuite Pilot implementation and Claude Code execution models [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]. The model demonstrates that pre-execution span reservation and environment variable injection successfully preserve end-to-end distributed trace continuity prior to process execution [^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b].

[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
