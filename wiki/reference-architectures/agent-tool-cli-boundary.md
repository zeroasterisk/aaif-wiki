---
type: reference-architecture
title: Agent to Tool CLI Boundary
description: Observability architecture and context propagation model for agent runtimes
  executing local command-line interface subprocesses.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
tags:
- observability
- reference-architecture
- cli
- telemetry
- opentelemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:16:08.415721+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-35
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/35
  author: fangxiu-wf
  last_modified: '2026-09-19T04:53:44+00:00'
---

# Overview

The Agent to Tool CLI boundary specification defines the telemetry propagation and span model for local process execution when an AI agent runtime invokes a command-line interface (CLI) tool [^evt-wg-observability-and-traceability-pr-35]. The specification distinguishes between the canonical Agent-to-Tool semantic boundary and its concrete Agent Runtime-to-Local Process realization.

# Architecture / Specification

### Context Propagation
- **Carrier:** The OpenTelemetry Release Candidate specification for environment variables is used as the standard context carrier across process execution boundaries [^evt-wg-observability-and-traceability-pr-35].
- **Identifiers:** W3C Trace Context and W3C Baggage are injected into subprocess environment variables prior to launch [^evt-wg-observability-and-traceability-pr-35].
- **Span Reservation:** Validated implementations, such as LoongSuite Pilot, utilize pre-execution span-ID reservation to establish parent-child linkage before subprocess fork [^evt-wg-observability-and-traceability-pr-35].

### Causality and Detached Execution
- Synchronous tool calls maintain direct parent-child causality between the agent runtime's execute-tool span and CLI caller spans [^evt-wg-observability-and-traceability-pr-35].
- Detached or background processes are represented using OpenTelemetry Span Links rather than strict child causality to prevent dangling trace hierarchies [^evt-wg-observability-and-traceability-pr-35].

# Lifecycle History

Documented as part of the Observability and Traceability Working Group's cross-boundary matrix under issue #29 [^evt-wg-observability-and-traceability-pr-35].

[^evt-wg-observability-and-traceability-pr-35]: https://github.com/aaif/wg-observability-and-traceability/pull/35
