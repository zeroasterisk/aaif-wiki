---
type: resource
title: Linux Driver Tracing
description: Reference architecture for Linux device driver instrumentation covering
  dev_dbg, dynamic debug (dyndbg), TRACE_EVENT macros, and debugfs interfaces.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
tags:
- tracing
- linux
- kernel
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:51:26.918221+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-633832607329-9b56d321
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
Linux Driver Tracing provides the foundational observability and debugging architecture for device drivers across the Linux kernel subsystem layer [^evt-wg-observability-and-traceability-file-633832607329-9b56d321]. Positioned between generic kernel tracing mechanisms and specialized hardware diagnostics, it details how developers instrument driver code and how administrators dynamically control trace event streams at runtime without recompilation [^evt-wg-observability-and-traceability-file-633832607329-9b56d321].

# Architecture / Specification
The driver tracing architecture spans structured logging, dynamic call-site modification, and custom tracepoint infrastructure:

- **Structured Device Logging**: Drivers implement structured logging through kernel macros (`dev_dbg`, `dev_info`, `dev_err`, `dev_warn`) that bind device context and driver identification directly to log entries routed through `printk` and the kernel ring buffer [^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
- **Dynamic Debug (`dyndbg`)**: When built with `CONFIG_DYNAMIC_DEBUG=y`, debug statements (`dev_dbg`, `pr_debug`) introduce zero runtime overhead until dynamically enabled via `/sys/kernel/debug/dynamic_debug/control` [^evt-wg-observability-and-traceability-file-633832607329-9b56d321]. Call sites can be queried and enabled per module, file, function, line number, or kernel boot parameter [^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
- **Custom `TRACE_EVENT()` Macros**: Drivers define high-performance, structured tracepoints using `TRACE_EVENT()` headers exported to `tracefs` under `/sys/kernel/tracing/events/` [^evt-wg-observability-and-traceability-file-633832607329-9b56d321]. These tracepoints integrate with kernel tooling including `perf` and `trace-cmd` [^evt-wg-observability-and-traceability-file-633832607329-9b56d321].
- **Subsystem-Specific Tracers and Interfaces**: Subsystem diagnostics extend through specialized tools such as `usbmon` for USB request block inspection, `blktrace` for block I/O profiling, and `devcoredump` for post-mortem driver crash capture [^evt-wg-observability-and-traceability-file-633832607329-9b56d321].

# References
- `linux-tracing-comparison.md`
- `ftrace.md`
- `linux-perf.md`

[^evt-wg-observability-and-traceability-file-633832607329-9b56d321]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/linux-driver-tracing.md
