---
type: resource
title: Linux Driver Tracing Mechanisms
description: Layered kernel observability and debugging framework enabling runtime
  inspection of hardware interactions, device drivers, and I/O subsystems without
  recompilation.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- kernel
- tracing
- linux
- drivers
- hardware
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:01:14.908330+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Linux Driver Tracing mechanisms provide a layered set of observability, debugging, and instrumentation facilities specifically tailored for kernel device drivers and hardware interfaces [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. Spanning structured logging (`dev_dbg`), dynamic debug (`dyndbg`), static tracepoints (`TRACE_EVENT`), subsystem-specific tracers (`usbmon`, `blktrace`), `debugfs` state inspection, and crash dumps (`devcoredump`), these facilities allow developers and operators to monitor hardware interactions and I/O request flows without modifying or recompiling driver code [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

# Architecture / Specification
The reference architecture details driver observation layers across hardware and kernel subsystems [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:

- **Observation Primitives**:
  - *Structured Logging*: `dev_dbg()`, `dev_info()`, and `dev_err()` bind log messages directly to device topologies and sysfs paths [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
  - *Dynamic Debug (`dyndbg`)*: Allows runtime enablement and filtering of debug callsites by module, function, file, or line number via `debugfs` control files [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
  - *Custom Tracepoints*: Statically compiled `TRACE_EVENT()` hooks expose low-overhead event streams through `tracefs` for capture by consumers such as `perf` and `trace-cmd` [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
  - *Post-Mortem Analysis*: Kernel `devcoredump` records device-specific state snapshots upon driver crashes or timeout events [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
- **Observation Models**:
  - *Event Model*: Captures discrete state transitions, register writes, interrupt deliveries, and command submissions rather than application-level duration spans [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
  - *Hardware Counter Model*: Exposes low-level telemetry including NVMe statistics, network interface packet and error metrics, PCIe Advanced Error Reporting (AER) counters, and GPU engine utilization [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].
  - *State Snapshot Model*: Inspects active runtime controller registers, engine schedules, USB device descriptors, and link states via `sysfs` and `debugfs` [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

# References
- Related resource: [Linux Tracing Comparison](../resources/linux-tracing-comparison.md)
- Related working group: [Observability and Traceability WG](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
