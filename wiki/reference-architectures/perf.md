---
type: architecture
title: Linux perf
description: Hardware-assisted CPU profiling and event tracing framework utilizing
  CPU Performance Monitoring Units and the perf_events kernel subsystem.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
tags:
- observability
- profiling
- pmu
- perf
- hardware-counters
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:50.363614+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux `perf` (perf_events) provides hardware-assisted performance profiling and execution tracing spanning from hardware Performance Monitoring Units (PMUs) through the kernel's `perf_events` subsystem to userspace analysis utilities [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]. It enables counting and sampling modes across hardware counters (CPU cycles, instructions, cache misses, branch mispredictions), software tracepoints, and dynamic probes [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

# Architecture / Specification

The perf architecture operates across three distinct operational layers [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]:
- **Hardware PMU Layer**: CPU hardware counters and advanced capture facilities (such as Intel PT branch packets and Last Branch Record rings) configured to trigger non-maskable interrupts (NMIs) upon counter overflow [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
- **Kernel `perf_events` Subsystem**: Managed via the `perf_event_open()` syscall, creating kernel event instances mapped to per-process or per-CPU ring buffers with lock-free mmap rings [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
- **Userspace Utilities**: CLI tooling (`perf stat`, `perf record`, `perf report`, `perf script`, `perf trace`) enabling live counter aggregation, stack unwinding (FP/DWARF/LBR), and flame graph generation [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

# References

- Working Group: [Observability and Traceability](../working-groups/observability-and-traceability.md)
- Architecture: [ftrace](./ftrace.md)
- Resource: [Linux Kernel Tracing Comparison](../resources/linux-kernel-tracing-comparison.md)

[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
