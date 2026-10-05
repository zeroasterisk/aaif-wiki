---
type: reference-architecture
title: Eclipse Trace Compass
description: Multi-format trace analysis and visualization framework correlating kernel,
  userspace, GPU, and AI model execution traces via interval-tree state systems.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
tags:
- observability
- tracing
- trace-compass
- visualization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:35.951599+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Eclipse Trace Compass reference architecture defines a multi-format trace analysis framework that correlates heterogeneous kernel, userspace, GPU, network, and AI framework traces through a unified state-system engine[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

Rather than producing traces, Trace Compass ingests traces from across the AAIF observability stack—including [Common Trace Format](common-trace-format.md), [LTTng Kernel Tracing](lttng-kernel-tracing.md), [Linux FTrace](ftrace.md), [PyTorch Profiler](pytorch-profiler.md), and [Wireshark](wireshark.md)—correlating them on synchronized timelines[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

# Architecture / Specification

Trace Compass executes offline and headless multi-trace correlation[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]:

- **State System Engine**: Builds disk-backed interval trees representing resource, thread, and process states over continuous time ranges from raw discrete events.
- **Experiment & Trace Synchronization**: Computes convex hull time synchronizations across disparate trace clocks and timestamps.
- **Trace Server Protocol (TSP)**: Headless REST API exposing time-graph models, XY data series, and state systems to remote web clients and agentic tools.
- **AI & Cross-Layer Analysis**: Correlates high-level PyTorch operator execution timelines with low-level kernel scheduling and GPU hardware tracepoints[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
