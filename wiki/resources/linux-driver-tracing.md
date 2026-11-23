---
type: resource
title: Linux Driver Tracing
description: Layered kernel observability and debugging reference architecture defining
  structured logging, dynamic debug, tracepoints, and bus tracers for Linux device
  drivers.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
tags:
- tracing
- linux
- kernel
- drivers
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:49:05.846843+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-633832607329-9b56d321
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Linux Driver Tracing defines the kernel and subsystem-level instrumentation mechanisms used by device driver developers and system administrators to observe, trace, and debug driver behavior within the Linux operating system.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321] Maintained as a reference architecture by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this document connects generalized kernel tracing facilities such as [ftrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), and [LTTng](../resources/lttng-kernel.md) to driver-specific instrumentation points and hardware bus monitors.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

# Architecture / Specification
The driver tracing architecture spans five primary instrumentation layers targeting modern Linux kernels (version 6.x recommended, baseline ≥ 4.19) with `CONFIG_DYNAMIC_DEBUG`, `CONFIG_DEBUG_FS`, and `CONFIG_TRACEPOINTS` enabled:[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

- **Structured Device Logging**: Drivers record operational state and anomalies through standardized logging macros (`dev_dbg`, `dev_info`, `dev_warn`, `dev_err`) defined in `<linux/device.h>`. Messages include device identity prefixes and are routed through `printk` to the kernel ring buffer.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Dynamic Debug (`dyndbg`)**: Controls debug call sites at runtime without driver recompilation. Administrators query and toggle individual call sites by module, file, function, or line number via `/sys/kernel/debug/dynamic_debug/control` or kernel boot parameters.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Driver Tracepoints (`TRACE_EVENT`)**: Low-overhead structured tracepoints declared through the kernel `TRACE_EVENT` macro system expose binary data through `tracefs` (`/sys/kernel/tracing/`). Tracepoints can be filtered and consumed concurrently by tools such as `perf` or `trace-cmd`.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Bus and Subsystem Monitors**: Domain-specific tap interfaces capture I/O transactions directly from hardware subsystems, such as `usbmon` capturing USB Request Blocks (URBs) for packet analysis and `blktrace` capturing block queue request timelines.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Diagnostic Dumps and Debugfs Interfaces**: Drivers export non-standard diagnostic counters, hardware state tables, and crash memory dumps via `/sys/kernel/debug/` mounts and the `devcoredump` framework.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
