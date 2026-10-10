---
type: resource
title: Trace-Server Machine Learning Library (TMLL)
description: Python analysis library and Model Context Protocol server applying machine
  learning pipelines and anomaly detection to Trace Compass telemetry for AI agents.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
tags:
- mcp
- machine-learning
- trace-analysis
- anomaly-detection
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

TMLL (Trace-Server Machine Learning Library) is an open-source Python library and Model Context Protocol (MCP) server that applies statistical and machine learning algorithms to low-level execution traces [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]. By interfacing with [Eclipse Trace Compass](../resources/trace-compass.md) through the Trace Server Protocol (TSP), TMLL transforms deterministic system state metrics into automated anomaly detections, change point segments, and resource forecasts queryable by AI agents [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

# Architecture / Specification

TMLL acts as an analytical bridge connecting deterministic trace state trees with autonomous agent workflows [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]:

- **TSP Client Backend**: Communicates with Trace Compass Server instances over REST APIs to extract time-series intervals, CPU states, memory usage, and thread activity [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **Statistical & ML Engines**: Utilizes scikit-learn (Isolation Forest, Local Outlier Factor), statsmodels (ARIMA forecasting), and ruptures (PELT change-point detection) to process aggregated telemetry [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **MCP Tool Provider**: Exposes analytical tool endpoints (`detect_anomalies`, `detect_changepoints`, `detect_memory_leak`, `detect_idle_resources`, `plan_capacity`) over stdio JSON-RPC for interactive debugging by AI agents [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
