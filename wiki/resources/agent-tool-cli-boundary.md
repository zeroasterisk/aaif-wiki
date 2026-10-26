---
type: resource
title: Agent-to-Tool Local CLI Observability Boundary
description: Observability reference matrix and context propagation model analyzing
  direct agent subprocess invocations of local CLI tools over environment variable
  carriers.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- opentelemetry
- cli
- subprocess
- trace-context
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:33:36.401023+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-35
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
  author: fangxiu-wf
  last_modified: '2026-09-19T04:53:44+00:00'
- id: evt-wg-observability-and-traceability-issue-29
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/29
  author: 91pavan
  last_modified: '2026-09-19T04:53:41+00:00'
---

# Overview
The agent-to-tool local CLI boundary specifies observability capture and context propagation when an agent runtime executes tools as local subprocesses [^evt-wg-observability-and-traceability-pr-35]. It distinguishes the canonical semantic boundary (Agent → Tool) from the concrete operational realization (Agent Runtime → Local Process) [^evt-wg-observability-and-traceability-pr-35].

This boundary deep-dive instantiates the broader [cross-boundary observability model](../resources/cross-boundary-observability-model.md), mapping how execution context, identity, lifecycle events, and outcomes cross the process barrier [^evt-wg-observability-and-traceability-issue-29] [^evt-wg-observability-and-traceability-pr-35].

# Architecture / Specification
### Semantic vs. Operational Boundary
The specification separates the semantic invocation—where an agent requests a capability—from the local subprocess execution boundary where the harness launches a CLI command [^evt-wg-observability-and-traceability-pr-35]:
- **Semantic Boundary (Agent → Tool):** Governs tool invocation semantics, model call intent, parameter schemas, and logical returns [^evt-wg-observability-and-traceability-pr-35].
- **Operational Boundary (Agent Runtime → Local Process):** Governs standard input/output streams, process lifecycle (fork/exec/exit codes), process-level resource bootstrap, and environment variable carriers [^evt-wg-observability-and-traceability-pr-35].

### Context Propagation and Carrier Semantics
Propagation across direct process boundaries relies on standardized environment variable carriers:
- **Environment Variable Carrier:** Utilizes the OpenTelemetry Release Candidate specification for environment variables as context carriers (e.g., `TRACEPARENT` and `TRACESTATE`), superseding previous views that local process carriers were unstandardized [^evt-wg-observability-and-traceability-pr-35].
- **Trace Context & Baggage:** Carries W3C Trace Context and W3C Baggage into child processes via sanitized environment injection [^evt-wg-observability-and-traceability-pr-35].
- **Resource Bootstrap:** Operational runtime metadata (such as host attributes and container cgroups) is treated as Resource bootstrap distinct from the dynamic invocation context [^evt-wg-observability-and-traceability-pr-35].

### Span Ownership and Detached Execution
- **Span Hierarchy:** Distinguishes whether `gen_ai.execute_tool` spans and CLI caller spans nest, share IDs, or suppress internal traces for direct process launch [^evt-wg-observability-and-traceability-pr-35].
- **Pre-execution Span ID Reservation:** Validated via Pilot PR #316 (LoongSuite Pilot) where the runtime pre-reserves span IDs to inject deterministically into subprocess environments before process initialization [^evt-wg-observability-and-traceability-pr-35].
- **Span Links for Detached Work:** Recommends OpenTelemetry Span Links instead of strict parent-child causality when tools spawn detached or asynchronous background jobs [^evt-wg-observability-and-traceability-pr-35].

# Lifecycle History
Derived from the gap analysis in the observability workstream [^evt-wg-observability-and-traceability-issue-29], the local CLI boundary was formally documented and merged as the initial completed boundary realization [^evt-wg-observability-and-traceability-pr-35]. Follow-up work targets PowerShell, Model Context Protocol ([resources/agent-mcp-server-boundary](../resources/agent-mcp-server-boundary.md)), containerized runners, and remote A2A calls [^evt-wg-observability-and-traceability-pr-35].

[^evt-wg-observability-and-traceability-issue-29]: https://github.com/aaif/wg-observability-and-traceability/issues/29
[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
