---
type: resource
title: Eclipse Trace Compass
description: Multi-format offline trace analysis and visualization framework correlating
  kernel, userspace, GPU, and PyTorch operator timelines via state systems.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/trace-compass.md
tags:
- tracing
- analysis
- kernel
- observability
- visualization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/trace-compass.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Eclipse Trace Compass is an open-source, multi-format trace analysis and visualization engine that correlates kernel, userspace, GPU, network, and AI framework traces through a unified state-system engine [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]. Rather than producing traces directly, Trace Compass functions as an offline consumer and analytical correlation layer spanning hardware counters to PyTorch operator execution timelines [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

Maintained as part of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape, Trace Compass supports diverse inputs including [Common Trace Format](../resources/common-trace-format.md) (LTTng), [ftrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), pcap network captures via [Wireshark](../resources/wireshark.md), and Chrome Trace JSON outputs from the [PyTorch Profiler](../resources/pytorch-profiler.md) [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

# Architecture / Specification

Trace Compass models trace data using an interval-tree-backed disk state system that indexes system and runtime states over time intervals [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]. The core architectural layers include:

- **Trace Parser Frontends**: Dedicated parsers for binary CTF, text/binary ftrace, GDB tracepoints, pcapng, and JSON execution events [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **State System Engine**: Builds history tree indices allowing fast logarithmic random-access queries to machine and thread state at any timestamp [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Time Synchronization & Convex Hull**: Correlates independent traces across multiple hosts and clocks by calculating timing drift and computing convex hulls across synchronizing network exchanges [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Trace Server Protocol (TSP)**: Enables headless server deployments queryable via REST/JSON, supporting programmatic consumption by machine learning frameworks such as [TMLL](../resources/tmll.md) [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/trace-compass.md
