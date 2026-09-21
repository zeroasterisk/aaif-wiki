---
type: reference-architecture
title: Eclipse Trace Compass Reference Architecture
description: Reference architecture for Eclipse Trace Compass multi-format trace analysis,
  state-system interval indexing, and Trace Server Protocol integration.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
tags:
- observability
- trace-analysis
- trace-compass
- eclipse
- ctf
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Eclipse Trace Compass is an extensible trace analysis and visualization platform designed to correlate kernel, userspace, GPU, network, and AI framework execution traces into unified timeline and resource state views [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]. Trace Compass does not generate traces directly; rather, it consumes heterogeneous trace formats—including [CTF / LTTng](../reference-architectures/ctf.md), [FTrace](../reference-architectures/ftrace.md), [perf](../reference-architectures/linux-perf.md), PCAP, and Chrome Trace JSON—and builds disk-backed interval trees for interactive querying.

# Architecture / Specification

- **State System Engine**: Indexes event streams into disk-backed interval trees that track system state attributes over time with logarithmic lookup complexity [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Trace Server Protocol (TSP)**: A REST/JSON API enabling headless, containerized Trace Compass deployments to serve trace indexing, queries, and timeline data to remote clients and machine learning tooling like [TMLL](../reference-architectures/tmll.md).
- **Cross-Layer Synchronization**: Aligns timestamps across disparate sources (e.g. Linux kernel context switches alongside [PyTorch Profiler](../reference-architectures/pytorch-profiler.md) operators) using convex hull time synchronization algorithms.

[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
