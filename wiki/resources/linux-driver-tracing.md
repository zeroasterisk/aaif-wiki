---
type: resource
title: Linux Driver Tracing Reference Architecture
description: Layered kernel observability framework capturing device driver hardware
  interactions, I/O requests, and error states via dynamic debug, TRACE_EVENT, and
  devcoredump.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:47:35.806001+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux driver tracing comprises a layered collection of kernel-integrated debugging, logging, and performance instrumentation mechanisms dedicated to observing device driver behavior and hardware interactions without reallocating or recompiling driver code [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. It provides low-overhead visibility into communication flows across PCIe, USB, NVMe, and GPU subsystem boundaries.

Within the broader hardware analysis landscape documented by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), driver tracing links operating system scheduling and containerized agent execution with underlying device controller states.

# Architecture / Specification

The driver observation model distinguishes between discrete hardware events and persistent subsystem states [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:

- **Structured Device Logging:** Primitives such as `dev_dbg()`, `dev_info()`, and `dev_err()` bind log output directly to kernel `struct device` identifiers and sysfs topology.
- **Dynamic Debug (`dyndbg`):** Controlled via `debugfs` (`/sys/kernel/debug/dynamic_debug/control`), allowing administrators to toggle debug callsites at runtime on a per-file, per-function, or per-line basis without performance penalties when disabled.
- **Static Tracepoints (`TRACE_EVENT`):** Subsystem instrumentation exposed through `tracefs` (`/sys/kernel/tracing/`) consumed by tools such as `perf`, `trace-cmd`, or [bpftrace](bpftrace.md).
- **Specialized Subsystem Tracers:** Dedicated facilities including `usbmon` for raw USB packet sniffing and `blktrace` for block layer request lifecycles.
- **Crash and Snapshot Facilities:** `devcoredump` captures ephemeral hardware register snapshots and firmware state upon device failure for post-mortem extraction.

# References

- Linux Kernel Driver Tracing Documentation (Linux 6.x) [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
- Subsystem Tracing APIs: `blktrace`, `usbmon`, and `devcoredump` [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
