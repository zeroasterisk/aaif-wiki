---
type: resource
title: Agent-to-Tool CLI Boundary Deep Dive
description: Observability reference matrix and telemetry propagation model analyzing
  direct agent subprocess invocations across semantic and process-launch boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
tags:
- observability
- telemetry
- opentelemetry
- cli
- traceability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:55:26.436578+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1699fc75df72-8956556b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
  author: Me1iodas
  last_modified: '2026-09-10T12:16:43+01:00'
---

# Overview

The Agent-to-Tool CLI Boundary Deep Dive defines the observable propagation mechanics between an agent runtime and directly invoked local CLI child processes.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] While an agent interacts with a tool at an abstract semantic level, local CLI realization concurrently crosses an operational operating-system process boundary where trace context, resource attribution, and causal relationships must cross during process creation rather than post-execution transcript ingestion.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]

# Architecture / Specification

## Boundary Decomposition

The reference execution hierarchy delineates agent decision context from local process execution:[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]

```text
optional upstream caller
  └── agent turn / invocation
      └── tool execution span              ← Agent → Tool semantic boundary
          └── [optional CLI caller span]
              └── local CLI execution span ← Agent Runtime → Local Process boundary
                  └── CLI sub-operations and downstream calls
```

The interaction spans two distinct operational surfaces:[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]
1. **Agent Execution Surface**: The model selects a tool, generating a call ID and sanitized arguments; the runtime checks authorizations and schedules execution.
2. **Operating-System Process Surface**: The runtime resolves binary paths, configures child process environment variables, spawns the child PID, monitors exit codes, and surfaces output back to the agent session.

## Filled Matrix Pass

| Observable Dimension | Telemetry Requirements | Standard Coverage | Identified Portability Gaps |
| :--- | :--- | :--- | :--- |
| **Identity** | Agent, principal, session/turn, tool call ID, executable path, process ID, telemetry service resource.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | OpenTelemetry GenAI (`gen_ai.tool.name`, `gen_ai.tool.call.id`) and OpenTelemetry CLI conventions.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Missing cross-runtime identity binding the agent call, child executable digest, and initiating principal.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |
| **Context** | Active trace parent, invocation baggage, sanitized arguments, working directory, budgets, policy constraints.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | W3C Trace Context and OpenTelemetry normalized environment-variable carrier specifications.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Runtimes filter child environments; no shared profile for passing turn deadline, execution budget, or security constraints.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |
| **Relationship** | Turn-level causal ownership spanning launch spans, synchronous execution children, and detached links.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | OpenTelemetry GenAI `execute_tool` spans and CLI caller/callee conventions.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Late transcript instrumentation breaks child-visible causality; detached runs require standard span link conventions.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |
| **Lifecycle** | Selection, authorization, context preparation, process spawn, execution, exit/timeout/cancellation.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | GenAI tool execution duration and OS exit codes.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Lack of standardized lifecycle representations joining agent policy approval delays, spawn failures, and background jobs.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |
| **Outcome** | Structured tool results, exit status, error classifications, side-effect manifestations.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | CLI `process.exit.code` and `error.type`.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Standard exit codes do not convey mutated files, downstream API calls, compensation actions, or sensitive payload masks.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |
| **Provenance** | Tool schema source, launching skill, binary hash, instrumentation scope, observer evidence class.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | OpenTelemetry Resource attributes and tool metadata.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] | Shell expansion and wrapper scripts obscure binaries; binary integrity hashes are rarely propagated into trace context.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b] |

## Implementation Patterns

Reference implementations (such as LoongSuite Pilot) validate that causal integrity requires pre-execution reservation: injecting `TRACEPARENT` into the process environment variables before child invocation, rather than reconciling spans asynchronously from completed session logs.[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]

# References

- [Cross-Boundary Observability Model](../resources/cross-boundary-observability-model.md)
- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-1699fc75df72-8956556b]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/working-documents/agent-tool-cli-boundary-deep-dive.md
