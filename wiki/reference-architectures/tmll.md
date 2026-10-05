---
type: reference-architecture
title: TMLL Trace Machine Learning Architecture
description: Reference architecture for TMLL applying automated machine learning pipelines
  to Trace Compass server outputs and exposing anomaly detection and capacity insights
  via Model Context Protocol tools.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
tags:
- trace-analysis
- machine-learning
- mcp
- trace-compass
- observability
- tmll
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:00:16.963486+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The TMLL (Trace-Server Machine Learning Library) reference architecture defines an orchestration framework that applies statistical modeling and automated machine learning pipelines to deterministic trace analysis data retrieved from Eclipse Trace Compass via the Trace Server Protocol (TSP), exposing analysis capabilities directly to AI agents through the Model Context Protocol (MCP).[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]

TMLL acts as an intermediate analysis bridge: it does not capture or store raw traces, but rather queries time-series state history from a headless [Trace Compass](../reference-architectures/trace-compass.md) server, executes Python-based anomaly detection or change point algorithms, and surfaces high-level diagnostic tools to AI agent runtimes over standard JSON-RPC stdio channels.[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]

# Architecture / Specification

### Analytical Pipeline and Tool Surface

- **Trace Server Protocol (TSP) Integration**: `TMLLClient` communicates with Trace Compass Server over REST endpoints to manage experiments, fetch aggregated data intervals, and pull state system metrics.[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]
- **Algorithmic Engine**: Utilizes scikit-learn (Isolation Forest, Local Outlier Factor), statsmodels (ARIMA, seasonal decomposition), and ruptures (PELT change point detection) to analyze CPU usage, memory leaks, and performance regressions.[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]
- **MCP Server Endpoint**: Exposes structured agent tools including `detect_anomalies`, `detect_changepoints`, `detect_memory_leak`, `analyze_correlation`, and `plan_capacity`, enabling autonomous reasoning agents to interrogate system performance without raw trace parsing overhead.[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]

# References

- [TMLL Repository](https://github.com/eclipse-tracecompass/tmll)
- [Eclipse Trace Compass Reference Architecture](../reference-architectures/trace-compass.md)

[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
