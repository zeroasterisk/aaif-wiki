---
type: reference-architecture
title: Linux perf Reference Architecture
description: Reference architecture for Linux perf hardware-assisted profiling, PMU
  counter measurement, and kernel tracepoint sampling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
tags:
- observability
- profiling
- linux
- kernel
- pmu
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux `perf` (the `perf_events` subsystem) is the canonical Linux kernel performance profiling and hardware-assisted event counting framework [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]. It operates from the CPU hardware Performance Monitoring Unit (PMU) through kernel ring buffers up to userspace analysis tools, providing sampling-based CPU profiling, hardware counter measurement, kernel tracepoints, and dynamic probes with configurable overhead.

Within the broader observability stack evaluated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), `perf` provides hardware-grounded performance metrics (such as IPC, cache misses, branch mispredictions, and instruction execution) complementing software tracing tools like [FTrace](../reference-architectures/ftrace.md) and [LTTng](../reference-architectures/lttng-kernel-tracing.md).

# Architecture / Specification

- **Hardware PMU Layer**: Captures architectural and model-specific hardware events, CPU cycle overflows (generating non-maskable interrupts / NMIs), Last Branch Records (LBR), and processor trace streams [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
- **Kernel Subsystem (`perf_events`)**: Managed via the `perf_event_open()` system call, creating per-event or per-process `struct perf_event` instances with circular `mmap` ring buffers for lock-free event streaming.
- **Modes of Operation**:
  - *Counting mode (`perf stat`)*: Hardware counter accumulation with near-zero runtime overhead [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
  - *Sampling mode (`perf record`)*: Periodic PMU interrupt-driven callstack sampling outputting to `perf.data` for profile aggregation and flame graph generation.
  - *Tracing mode (`perf trace`)*: System call and tracepoint event logging.

[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
