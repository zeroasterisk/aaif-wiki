---
type: reference-architecture
title: Linux Driver Tracing Reference Architecture
description: Reference architecture detailing Linux kernel device driver observability
  via dev_dbg, dynamic debug, TRACE_EVENT, debugfs, and subsystem-specific tooling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- observability
- kernel
- drivers
- tracing
- debugfs
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Linux Driver Tracing reference architecture outlines the layered observability mechanisms available across Linux device driver subsystems [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. Developed under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it explains how driver developers and operators inspect hardware interactions, I/O paths, and runtime driver states without modifying kernel source code [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

# Architecture / Specification

Linux provides structured observability primitives spanning logging, event recording, and hardware state inspection [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:

- **Structured Device Logging**: Driver logging via `dev_dbg()`, `dev_info()`, and `dev_err()` associates kernel log output with explicit `struct device` hierarchy identifiers [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
- **Dynamic Debug (`dyndbg`)**: Enables or disables individual debug callsites at runtime based on module, file, function, line, or format string queries without kernel recompilation [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
- **Static Kernel Tracepoints (`TRACE_EVENT`)**: Built-in static tracepoints consumed via `tracefs` and tools such as [FTrace](../reference-architectures/ftrace.md) or [LTTng Kernel Tracing](../reference-architectures/lttng-kernel-tracing.md) [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
- **State Snapshots and Subsystem Tracing**: Subsystem-specific tools (`usbmon`, `blktrace`) alongside `debugfs` nodes and `devcoredump` crash snapshots capture device register states and hardware transfer queues [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/driver-tracing.md
