---
type: resource
title: Linux Device Driver Tracing Reference Architecture
description: Kernel-level device driver observability architecture combining structured
  logging, dynamic debug, tracepoints, and bus-level tracers.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
tags:
- kernel
- linux
- tracing
- observability
- drivers
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:47:34.950979+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-633832607329-9b56d321
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Linux device driver tracing encompasses the subsystem instrumentation and observability mechanisms exposed by the Linux kernel for device driver development, diagnostics, and production runtime troubleshooting.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321] Positioned between generic kernel tracing infrastructures (such as [Ftrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), and [LTTng](../resources/lttng-kernel.md)) and hardware-specific diagnostic tooling, driver tracing establishes visibility into device initialization, control bus exchanges, interrupt handling, and hardware state transitions.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

# Architecture / Specification
The driver tracing architecture spans five distinct instrumentation layers within the Linux kernel (version 4.19+ and 6.x).[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

## Instrumentation Mechanisms
- **Structured Device Logging**: Kernel macros (`dev_dbg`, `dev_info`, `dev_warn`, `dev_err`) prefix messages with device, bus, and driver identifiers to provide context-aware dmesg and journald logs.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Dynamic Debug (`dyndbg`)**: Configured via `CONFIG_DYNAMIC_DEBUG=y`, this mechanism allows selective runtime enabling of debug call sites per module, file, function, or line number via `/sys/kernel/debug/dynamic_debug/control` with near-zero overhead when disabled.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Custom Driver Tracepoints (`TRACE_EVENT`)**: Static kernel tracepoints defined within driver headers export structured binary event records into `tracefs` without string formatting overhead, enabling consumption by tools such as `trace-cmd` and [perf](../resources/linux-perf.md).[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Bus and Subsystem Monitors**: Specialized monitoring interfaces (e.g., `usbmon` for USB protocol exchanges, `blktrace` for block I/O requests) capture bus-specific packet streams for offline or live inspection.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]
- **Diagnostic File Systems and Crash Dumps**: `debugfs` endpoints expose internal driver state variables and hardware counters, while `devcoredump` captures ephemeral crash states when device hardware fails.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

## Runtime Interfaces and Prerequisites
Instrumentation requires kernel configuration options `CONFIG_DYNAMIC_DEBUG=y`, `CONFIG_DEBUG_FS=y`, and `CONFIG_TRACEPOINTS=y`, with `debugfs` mounted at `/sys/kernel/debug` and `tracefs` mounted at `/sys/kernel/tracing`.[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]

# References
- AAIF Working Group Observability and Traceability repository: https://github.com/aaif/wg-observability-and-traceability

[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
