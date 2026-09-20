---
type: deliverable
title: TMLL Reference Architecture
description: A reference architecture evaluating TMLL machine learning pipelines on
  Trace Compass state data exposed via Model Context Protocol (MCP).
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
tags:
- observability
- machine-learning
- mcp
- trace-analysis
- ai-agents
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

TMLL (Trace-Server Machine Learning Library) is a Python library and Model Context Protocol (MCP) server that applies automated statistical and machine learning algorithms to system trace data retrieved from Eclipse Trace Compass [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]. It acts as an orchestration bridge, querying the Trace Server Protocol (TSP) REST API to extract interval-tree time-series data, executing statistical modeling, and exposing derived diagnostic tools to AI agents via standard MCP interfaces [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

In the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) ecosystem, TMLL directly couples the deterministic trace modeling of the [Eclipse Trace Compass Reference Architecture](../deliverable/trace-compass-reference-architecture.md) with agentic inspection workflows [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

# Architecture / Specification

TMLL bridges trace servers with agentic runtimes through a layered workflow [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]:
- **TSP Client (`TMLLClient`)**: Communicates with Trace Compass Server instances over HTTP REST to open trace experiments and fetch XY or time-graph data series [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **ML & Statistical Pipeline**: Employs algorithms such as Isolation Forest, Local Outlier Factor (LOF), ARIMA, and changepoint detection (PELT/BOCPD) via standard Python scientific packages (`scikit-learn`, `statsmodels`, `ruptures`) to detect anomalies, resource leaks, and state shifts [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **MCP Interface**: Implements a standard Model Context Protocol server exposing tool endpoints (`detect_anomalies`, `detect_memory_leak`, `detect_changepoints`, `fetch_data`) consumable by AI agents [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
