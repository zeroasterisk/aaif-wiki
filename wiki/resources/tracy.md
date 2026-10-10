---
type: resource
title: Tracy Frame Profiler
description: Reference architecture evaluating Tracy's compile-time RAII zone instrumentation,
  call-stack sampling, and live TCP streaming client-server frame profiling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/tracy.md
tags:
- observability
- profiling
- tracy
- performance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:43.095337+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/tracy.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview

Tracy is a nanosecond-resolution hybrid frame profiler combining compile-time source instrumentation with statistical call-stack sampling into a single client-server architecture [^evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1]. Designed for interactive and latency-critical systems, Tracy streams captured telemetry from an instrumented client application to a remote graphical viewer or headless capture utility over TCP, correlating CPU execution zones, GPU queues, memory allocations, and lock contention across a unified time axis [^evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1].

# Architecture / Specification

Tracy's architecture centers around a decoupled instrumentation and streaming pipeline [^evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1]:

- **Client Instrumentation**: Provides RAII-based macros (`ZoneScoped`, `TracyAlloc`, `TracyGpuZone`, `FrameMark`) compiled into the host process, which compile to no-ops when disabled via `-DTRACY_ENABLE`.
- **Lock-Free Event Queues**: Enqueues thread-local events into lock-free multi-producer single-consumer (MPSC) queues using RDTSC hardware timestamps.
- **Network Streaming Engine**: A background worker thread compresses and transmits event streams over TCP (default port 8086) to `tracy-profiler` or `tracy-capture` for live inspection and `.tracy` trace serialization [^evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1].

[^evt-wg-observability-and-traceability-file-87697da76c8f-8c1cdaf1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/tracy.md
