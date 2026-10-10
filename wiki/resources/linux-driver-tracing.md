---
type: resource
title: Linux Driver Tracing Reference Architecture
description: Reference architecture covering Linux device driver instrumentation mechanisms
  including dynamic debug, TRACE_EVENT macros, debugfs, and devcoredump.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- observability
- tracing
- kernel
- drivers
- hardware
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:21.864246+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Linux Driver Tracing encompasses the kernel-integrated facilities used to inspect hardware interaction, I/O dispatch queues, and internal device driver state without modifying or recompiling running driver code.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

Cataloged by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture defines how driver observability spans structured runtime logging, dynamic debug (`dyndbg`), compile-time tracepoints (`TRACE_EVENT`), subsystem-specific tracers (such as `usbmon` and `blktrace`), debugfs file interfaces, and post-mortem crash dumps (`devcoredump`).[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

# Architecture / Specification

Driver observability operates across five primary layers:

- **Structured Logging (`dev_dbg`, `dev_info`, `dev_err`)**: Kernel logging functions bound to device topology (`struct device`), automatically prefixing subsystem, bus, and device IDs in `dmesg`.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
- **Dynamic Debug (`dyndbg`)**: Runtime control via `/sys/kernel/debug/dynamic_debug/control` that dynamically enables or disables debug callsites per module, file, function, or line number with zero runtime overhead when inactive.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
- **Static Tracepoints (`TRACE_EVENT`)**: Low-overhead binary instrumentation points exposed through `tracefs` (`/sys/kernel/tracing/events/`) consumable by [ftrace](ftrace.md), [perf](linux-perf.md), and [LTTng](lttng-kernel.md).[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
- **Subsystem & Hardware Monitors**: Hardware-level statistics exposed via `sysfs`, specialized subsystem tracers (`blktrace`, `usbmon`), and PCIe Advanced Error Reporting (AER) counters.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]
- **Post-Mortem State (`devcoredump`)**: Crash capture mechanism providing synthetic device memory and register dumps in `/sys/class/devcoredump/` upon hardware hang or fatal timeout.[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
