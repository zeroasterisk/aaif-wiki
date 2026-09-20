---
type: deliverable
title: Linux Driver Tracing Reference Architecture
description: A reference architecture detailing instrumentation mechanisms and debugging
  interfaces across Linux device drivers, dynamic debug, and hardware sub-systems.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- linux
- kernel
- driver-tracing
- observability
- debugfs
- tracepoints
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Linux Driver Tracing reference architecture establishes the multi-layer observability model for Linux kernel device drivers and hardware interfaces [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. It categorizes mechanisms spanning structured logging (`dev_dbg`), dynamic debug (`dyndbg`), subsystem tracepoints (`TRACE_EVENT`), debugfs inspection interfaces, subsystem-specific tracers (such as `usbmon` and `blktrace`), and crash-dump capture via `devcoredump`.

These facilities allow developers and system engineers to observe hardware-software interactions, I/O dispatch queues, and peripheral driver state transitions without kernel recompilation [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

# Architecture / Specification

The driver observation model operates across three primary patterns [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:

- **Structured Logging & Dynamic Debug**: Kernel logging primitives (`dev_info`, `dev_err`, `dev_dbg`) are dynamically toggled at runtime via `/sys/kernel/debug/dynamic_debug/control` on a per-file, per-function, or per-line basis using jump-label patching with zero overhead when disabled.
- **Event-Driven Subsystem Tracepoints**: Subsystem-specific tracepoints (e.g., block, DRM, NVMe, USB) expose discrete state transitions and I/O requests to consumers like [FTrace Reference Architecture](../deliverable/ftrace-reference-architecture.md) and [LTTng Kernel Tracing Reference Architecture](../deliverable/lttng-kernel-tracing-reference-architecture.md).
- **State Snapshots & Diagnostics**: Exposes device register state, PCIe Advanced Error Reporting (AER) counters, and debugfs telemetry for hardware diagnostic inspection.

# Lifecycle History

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as part of the operating system tracing landscape [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
