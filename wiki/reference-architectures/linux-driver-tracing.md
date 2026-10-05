---
type: reference-architecture
title: Linux Driver Tracing Mechanisms
description: Kernel driver subsystem instrumentation and hardware interaction observation
  framework spanning dynamic debug, tracepoints, and post-mortem dumps.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/driver-tracing.md
tags:
- linux
- kernel
- drivers
- tracing
- hardware
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:35.951599+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/driver-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Linux Driver Tracing reference architecture establishes standard observability mechanisms across device driver layers, enabling hardware interaction inspection without code modifications or custom kernel rebuilds[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]. It bridges physical hardware interfaces with kernel driver subsystems and userspace diagnostics.

This framework operates in coordination with [Linux FTrace](ftrace.md) and [Linux perf](perf.md) under the guidance of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md).

# Architecture / Specification

Linux driver observability is structured across layered mechanisms[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]:

- **Structured Device Logging (`dev_dbg`, `dev_info`, `dev_err`)**: Standard kernel log functions binding device-tree identifiers, bus addresses, and driver state to log events.
- **Dynamic Debug (`dyndbg`)**: Runtime jump-label patching allowing selective enablement of debug print callsites by file, function, module, or line number via debugfs.
- **Subsystem Tracepoints (`TRACE_EVENT`)**: Fast path instrumentation for I/O requests, queue management, and hardware interrupts accessible via tracefs.
- **Subsystem Tracers & Dumps**: Specialized protocol monitors (`usbmon`, `blktrace`), `debugfs` register dumps, and `devcoredump` state captures upon hardware crash events[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1].

[^evt-wg-observability-and-traceability-file-8cb302c8ed1b-a2ffbef1]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/driver-tracing.md
