---
type: resource
title: Linux Device Driver Tracing Reference Architecture
description: Kernel-level driver observability architecture combining structured logging,
  dynamic debug, tracepoints, and bus-specific tracers across Linux subsystems.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
tags:
- kernel
- linux
- tracing
- drivers
- dynamic-debug
- tracepoints
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:13:09.843168+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-633832607329-9b56d321
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux driver tracing encompasses the diagnostic and telemetry mechanisms available to device driver developers and system administrators within the Linux kernel (kernel 4.19+ and 6.x)[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]. Positioned between generic kernel tracing infrastructure and hardware diagnostics, it details driver instrumentation surfaces across USB, network, block, GPU/DRM, and SPI/I2C subsystems[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].

# Architecture / Specification

The driver instrumentation and observability architecture comprises four core layers:

1. **Structured Device Logging**: Device-aware logging macros (`dev_dbg`, `dev_info`, `dev_warn`, `dev_err`) binding log output to specific device topology and bus addresses, streaming through `printk` to the kernel ring buffer[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
2. **Dynamic Debug (`dyndbg`)**: Zero-overhead runtime switching via `/sys/kernel/debug/dynamic_debug/control`, allowing selective activation of debug call sites filtered by module, function, file, or line number without kernel recompilation[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
3. **Custom Driver Tracepoints (`TRACE_EVENT`)**: Static tracepoints declared in driver headers via `<linux/tracepoint.h>` and exposed through `tracefs` (`/sys/kernel/tracing/`), consumable by [FTrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), and [LTTng](../resources/lttng-kernel.md)[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
4. **Subsystem Diagnostic Facilities**: Specialized tracing interfaces including `usbmon` (analyzed using [Wireshark](../resources/wireshark.md)), `blktrace` for block storage I/O tracing, and `devcoredump` for hardware state dumps upon driver crash[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].

# Lifecycle History

Documented by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as part of the unified Linux kernel tracing landscape in June 2026[^evt-wg-observability-and-traceability-file-633832607329-9b56d321].

[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
