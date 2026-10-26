---
type: resource
title: Linux Driver Tracing Mechanisms
description: Kernel-level driver observability architecture combining structured logging,
  dynamic debug, tracepoints, and post-mortem dumps.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- observability
- linux
- kernel
- tracing
- hardware
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:13:28.544386+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Linux driver tracing encompasses the kernel-level observability subsystems that allow developers and administrators to monitor hardware interactions, I/O paths, and device states without recompiling driver code [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. Developed within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture categorizes dynamic instrumentation, structured logs, and hardware telemetry across Linux subsystems [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

# Architecture / Specification
The reference architecture defines five primary layers of driver observability [^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:
- **Structured Device Logging:** Primitives such as `dev_dbg()`, `dev_info()`, and `dev_err()` bind log messages directly to the `struct device` hierarchy and device tree identifiers.
- **Dynamic Debug (`dyndbg`):** Controlled via `debugfs` (`/sys/kernel/debug/dynamic_debug/control`), allowing runtime callsite enablement by module, file, function, or line format without driver recompilation.
- **Kernel Tracepoints (`TRACE_EVENT`):** Statically defined kernel tracepoints in `tracefs` (`/sys/kernel/tracing/`) consumed by tools like `trace-cmd` and `perf` to capture hardware event flows across NVMe commands, GPU DRM dispatch, and network interfaces.
- **Subsystem-Specific Tracers:** Dedicated facilities such as `usbmon` for USB packet inspection and `blktrace` for block layer I/O queues.
- **Post-Mortem State Capture:** Diagnostic mechanisms including `devcoredump` for capturing device register snapshots on hardware failure, and hardware counters exposed via `sysfs` or PCIe AER reporting.

# References
- [Linux Driver Tracing Reference Architecture](https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md)
- Related comparison: [Linux Tracing Comparison](../resources/linux-tracing-comparison.md)

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/driver-tracing.md
