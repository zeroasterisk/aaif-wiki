---
type: resource
title: Linux Driver Tracing Reference Architecture
description: Kernel-level driver observability architecture combining structured logging,
  dynamic debug, tracepoints, subsystem-specific tracers, and devcoredump crash records.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- linux
- kernel
- tracing
- observability
- hardware
- drivers
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:15:10.316983+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux driver tracing provides a layered observability architecture designed for device drivers across storage, networking, GPU accelerators, and peripheral buses.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1] It enables developers and system administrators to inspect hardware communications, I/O request flows, and internal driver states without recompiling kernel modules or modifying driver codebases.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

# Architecture / Specification

## Observation Primitives

Driver observability spans several kernel facilities operating at distinct points along the hardware interaction path:[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

1. **Structured Logging (`dev_dbg`, `dev_info`, `dev_err`):** Device-aware logging macros that prefix messages with device topology names and bus addresses, routing structured text into the kernel log buffer.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
2. **Dynamic Debug (`dyndbg`):** Controlled via `/sys/kernel/debug/dynamic_debug/control`, allowing runtime activation and deactivation of `dev_dbg` callsites without kernel recompilation. Debug points can be selectively enabled by driver filename, module, line number, or function.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
3. **Static Tracepoints (`TRACE_EVENT`):** High-throughput, low-overhead binary tracepoints exposed under `/sys/kernel/tracing/events/`, consumable by `perf`, `trace-cmd`, or LTTng for low-latency hardware event timelines.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
4. **Subsystem-Specific Tracers:** Purpose-built inspection mechanisms including `blktrace` for block layer queue latency and request dispatch, as well as `usbmon` for raw USB packet capture.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
5. **Post-Mortem Analysis (`devcoredump`):** Automatic crash snapshot infrastructure that captures controller registers and memory state upon driver fault or timeout, exposing snapshot dumps under `/sys/class/devcoredump/`.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

## Hardware State and Counter Model

Unlike userspace tracing models oriented around causal spans, driver observation operates on continuous hardware state queries and discrete event streams.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1] System performance counters monitor hardware health via PCIe Advanced Error Reporting (AER) counters, NVMe controller metrics via sysfs, and GPU performance monitoring units (PMUs), correlating device-level events with operating system dispatch latency.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

# References

- `../resources/linux-tracing-comparison.md`
- `../resources/ftrace.md`
- `../resources/linux-perf.md`
- `../working-groups/observability-and-traceability.md`

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
