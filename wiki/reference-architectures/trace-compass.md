---
type: architecture
title: Eclipse Trace Compass
description: Multi-format trace analysis and visualization framework correlating kernel,
  userspace, GPU, and network traces via a disk-backed state system engine.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
tags:
- observability
- trace-analysis
- trace-compass
- ctf
- correlation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:50.363614+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Eclipse Trace Compass is a multi-format trace analysis and visualization framework that correlates heterogeneous trace streams—including kernel, userspace, GPU, network, and AI framework traces—through a unified state-system engine [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]. Instead of acting as a trace producer, Trace Compass ingests multi-source traces to reconstruct end-to-end timeline state across hardware counters, OS schedulers, and high-level execution graphs [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

# Architecture / Specification

Trace Compass centers on a modular trace intake, state reconstruction, and presentation pipeline [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]:
- **Multi-Format Input Parsers**: Native ingestion for [Common Trace Format (CTF)](./common-trace-format.md), [ftrace](./ftrace.md), [perf](./perf.md), PCAP/PCAPNG, and Chrome Trace JSON (such as [PyTorch Profiler](./pytorch-profiler.md) outputs) [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **State System Engine**: Builds history trees and disk-backed interval trees that track attribute state transitions over time, enabling sub-millisecond timeline queries across gigabyte-scale trace archives without full re-scans [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Trace Synchronization**: Correlates independent clock domains across multi-node or host-guest systems using convex-hull algorithms and shared network or RPC exchange points [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Trace Server Protocol (TSP)**: Enables headless and remote trace querying via RESTful APIs, decoupling trace computation backends from front-end analysis clients and AI model inspection extensions [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

# References

- Working Group: [Observability and Traceability](../working-groups/observability-and-traceability.md)
- Architecture: [Common Trace Format (CTF)](./common-trace-format.md)
- Architecture: [LTTng Userspace Tracing](./lttng-ust.md)
- Architecture: [PyTorch Profiler](./pytorch-profiler.md)

[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/trace-compass.md
