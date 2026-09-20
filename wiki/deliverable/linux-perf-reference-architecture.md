---
type: deliverable
title: Linux perf Reference Architecture
description: A reference architecture evaluating Linux perf hardware PMU counters,
  kernel tracepoints, and sampling-based execution profiling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
tags:
- observability
- tracing
- profiling
- linux-kernel
- pmu
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux perf provides hardware-assisted performance profiling and tracing through the kernel `perf_events` subsystem, spanning Performance Monitoring Units (PMUs), kernel tracepoints, and dynamic probes [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]. It operates across hardware, kernel, and user spaces to measure instruction execution, cache behavior, branch mispredictions, and kernel events with overhead ranging from near-zero in counting mode to moderate in high-frequency sampling [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

Maintained as part of the upstream Linux kernel source tree, `perf` functions in the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape alongside comparative tools detailed in the [Linux Kernel Tracing Comparison](../deliverable/linux-kernel-tracing-comparison.md) and [FTrace Reference Architecture](../deliverable/ftrace-reference-architecture.md) [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

# Architecture / Specification

Linux perf instrumentation operates across several structural layers [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]:
- **Hardware PMU Layer**: Captures hardware events (CPU cycles, instructions retired, cache misses, branch records via LBR, and instruction execution traces via Intel PT) via non-maskable interrupts (NMI) on counter overflow [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
- **Kernel Subsystem (`perf_events`)**: Configured via the `perf_event_open()` system call, providing per-CPU and per-task ring buffers and event filtering [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].
- **Userspace Tooling**: Utilities such as `perf stat` (counting mode), `perf record` / `perf report` (sampling mode), `perf script`, and `perf trace` (system call tracing) [^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/perf.md
