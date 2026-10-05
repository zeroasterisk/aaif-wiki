---
type: architecture
title: TMLL Reference Architecture
description: Trace analysis machine learning library bridging Eclipse Trace Compass
  time-series states to AI agent workflows via Model Context Protocol tools.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
tags:
- trace-analysis
- mcp
- machine-learning
- trace-compass
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

TMLL (Trace-Server Machine Learning Library) is an analytical orchestration framework that applies automated machine learning pipelines (such as Isolation Forest, changepoint detection, and ARIMA forecasting) to execution traces produced by [Trace Compass](../reference-architectures/trace-compass.md) [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]. It exposes deterministic trace analytics as Model Context Protocol (MCP) tools for AI agents to diagnose latency regressions and anomalies [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

# Architecture / Specification

TMLL acts as an intermediate bridge between deterministic trace servers and reasoning agents [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]:

- **Trace Ingestion Layer**: Connects via REST using the Trace Server Protocol (TSP) to Trace Compass Server, reading state system time-series data without parsing raw trace binaries directly [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **Statistical & ML Engine**: Utilizes scikit-learn, statsmodels, and ruptures to perform anomaly detection, change-point analysis (PELT/BOCPD), idle resource detection, and memory leak analysis [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **MCP Server Surface**: Exposes standardized tools (`ensure_server`, `detect_anomalies`, `detect_changepoints`, `detect_memory_leak`, `plot_xy_with_anomalies`) over standard I/O (stdio JSON-RPC) directly consumable by AI agent environments [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

# References

- TMLL Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].

[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
