---
type: reference-architecture
title: TMLL Reference Architecture
description: Reference architecture for Trace-Server Machine Learning Library applying
  anomaly detection to Trace Compass outputs via Model Context Protocol.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
tags:
- observability
- machine-learning
- mcp
- trace-compass
- tmll
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

TMLL (Trace-Server Machine Learning Library) is a Python library and MCP (Model Context Protocol) server that applies automated statistical and machine learning algorithms to trace time-series exported by [Eclipse Trace Compass](../reference-architectures/trace-compass.md) [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]. TMLL sits at the orchestration layer, translating raw state-system metrics into structured anomaly detections and diagnostic insights accessible to AI agents.

# Architecture / Specification

- **Trace Compass Integration**: Communicates with headless Trace Compass Server instances over the REST-based Trace Server Protocol (TSP) to retrieve thread state and resource metric time series [^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b].
- **ML Pipeline**: Implements unsupervised anomaly detection (Isolation Forest, Local Outlier Factor), change-point detection (PELT, BOCPD via `ruptures`), and time-series forecasting (ARIMA).
- **Model Context Protocol (MCP) Server**: Exposes trace analysis tools (`detect_anomalies`, `detect_changepoints`, `detect_memory_leak`, `plan_capacity`) over stdio JSON-RPC, enabling AI agents to autonomously query and interpret complex trace data.

[^evt-wg-observability-and-traceability-file-e04f039081a4-3b16801b]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-TMLL.md
