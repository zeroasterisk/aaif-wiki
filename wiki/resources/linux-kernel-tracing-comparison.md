---
type: resource
title: Linux Kernel Tracing Comparative Assessment
description: Comparative assessment of Linux tracing frameworks analyzing architectural
  trade-offs between LTTng, perf, and FTrace.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
tags:
- observability
- linux
- kernel
- ftrace
- perf
- lttng
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:31:53.717543+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-313867ac2247-613905ef
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The Linux kernel tracing assessment compares the three primary kernel instrumentation frameworks—LTTng, perf, and FTrace—evaluating their data paths, performance overheads, and suitability for system-level observability [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. Curated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the evaluation highlights architectural trade-offs across userspace tracing, hardware performance counters, and built-in kernel diagnostics [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

# Architecture / Specification
The frameworks present distinct operational models and feature coverage [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]:
- **LTTng**: Employs external kernel modules and userspace daemons (LTTng-UST) with lock-free per-CPU ring buffers, exporting Common Trace Format (CTF) binary streams optimized for high throughput with minimal overhead (~50–150 ns per enabled tracepoint) [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **perf**: Integrates directly into the kernel and userspace tooling (`perf_events`), specializing in hardware Performance Monitoring Unit (PMU) counters, sampling, uprobes, and system profiling writing to `perf.data` [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **FTrace**: Standard in-tree kernel infrastructure operated via `tracefs`, optimized for function entry/exit graph tracing and zero-dependency debugging [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
