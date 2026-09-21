---
type: reference-architecture
title: Linux Kernel Tracing Comparison (LTTng, perf, FTrace)
description: Comparative assessment of LTTng, perf, and FTrace across overhead, interfaces,
  and observability dimensions for system infrastructure.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
tags:
- kernel
- tracing
- benchmarks
- observability
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:00.429590+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-313867ac2247-613905ef
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Linux kernel tracing comparative assessment evaluates LTTng, perf, and FTrace across foundational observability and infrastructure performance dimensions [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. Conducted by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the analysis establishes the relative strengths, data path architectures, and overhead profiles of core Linux tracing frameworks [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef, ^evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6].

# Architecture / Specification

The three frameworks specialize in distinct tracing paradigms [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]:

- **LTTng**: Implements external kernel modules and userspace tracing (LTTng-UST) with lock-free per-CPU ring buffers, exporting structured binary traces in Common Trace Format (CTF) for high-throughput, low-overhead production monitoring [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **Linux perf**: Focuses on hardware Performance Monitoring Unit (PMU) counters, statistical sampling, and dynamic userspace probes (uprobes/USDT), utilizing per-event memory-mapped ring buffers and `perf.data` files [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **FTrace**: Built directly into the Linux kernel with zero external package dependencies, using dynamic binary NOP patching and text-based `tracefs` interfaces for function call graphing and kernel subsystem debugging [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
