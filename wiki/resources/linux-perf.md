---
type: resource
title: Linux perf Reference Architecture
description: Reference architecture for Linux perf covering hardware PMU sampling,
  kernel tracepoints, and perf_events subsystem analysis.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/perf.md
tags:
- observability
- profiling
- perf
- kernel
- hardware
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:21.864246+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/perf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux perf (also known as `perf_events`) is a hardware-assisted performance profiling and dynamic tracing subsystem integrated into the Linux kernel, enabling sampling-based CPU profiling, hardware performance monitoring unit (PMU) counter tracking, and kernel/userspace tracepoint observation.[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]

Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing landscape, perf serves as the standard interface for measuring low-level CPU execution metrics (e.g., instructions per cycle, cache misses, branch mispredictions, Intel PT branch traces) across system processes.[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]

# Architecture / Specification

The subsystem is structured across three core layers:

- **Hardware PMU Layer**: CPU hardware counters generate non-maskable interrupts (NMIs) upon counter overflow, recording instruction pointers and register state.
- **Kernel `perf_events` Subsystem**: Configured via the `perf_event_open()` system call, managing per-thread or per-CPU ring buffers with event filtering and call-chain unwinding.[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]
- **Userspace Tooling**: `perf stat` (counting mode), `perf record`/`perf report` (sampling mode with DWARF call graph unwinding), and `perf trace` (system call tracking).[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]

[^evt-wg-observability-and-traceability-file-b86b123293cf-ed4113f1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/perf.md
