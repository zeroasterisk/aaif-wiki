---
type: reference-architecture
title: Linux perf
description: Hardware-assisted CPU profiling and event tracing architecture leveraging
  the Linux perf_events subsystem and hardware PMU counters.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
tags:
- observability
- profiling
- perf
- linux
- hardware
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:35.951599+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Linux perf reference architecture outlines hardware-assisted performance profiling and kernel tracing via the `perf_events` subsystem, spanning sampling-based CPU profiling, hardware counter measurement, and dynamic instrumentation[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

Maintained as part of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing catalog, perf enables analysis from low-level Performance Monitoring Units (PMUs) up to user-space flame graphs and system call statistics[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

# Architecture / Specification

The perf architecture interfaces directly between hardware counters and userspace tooling[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]:

- **Hardware PMU Layer**: Interfaces with CPU Performance Monitoring Units to track instructions, clock cycles, cache misses, branch mispredictions, Intel PT packets, and Last Branch Record (LBR) stacks.
- **`perf_events` Subsystem**: Configures sampling and counting triggers via `perf_event_open()`, using Non-Maskable Interrupts (NMI) on counter overflows to record callchains into per-CPU mmap ring buffers.
- **Userspace Analysis Tools**: CLI utilities (`perf stat`, `perf record`, `perf report`, `perf trace`) enabling live profiling, trace analysis, and integration with downstream visualization tools[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1].

[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/perf.md
