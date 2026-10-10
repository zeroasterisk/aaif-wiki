---
type: resource
title: LTTng Kernel Tracing Reference Architecture
description: Reference architecture for LTTng kernel tracing via lock-free per-CPU
  ring buffers and Common Trace Format generation.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
tags:
- observability
- tracing
- lttng
- kernel
- linux
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:21.864246+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

LTTng Kernel Tracing provides low-overhead, production-grade Linux kernel observability by attaching probe modules to kernel tracepoints, system call boundaries, and kprobes, recording binary event streams into per-CPU ring buffers in the [Common Trace Format](common-trace-format.md).[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]

Maintained as part of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape, LTTng Kernel Tracing enables nanosecond-accurate multi-core correlation of scheduler switches (`sched_switch`), block I/O, network packets, and page faults.[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]

# Architecture / Specification

The LTTng kernel subsystem architecture comprises:

- **Kernel Probe Modules (`lttng-modules`)**: Out-of-tree kernel modules linking tracepoint hooks directly to lock-free atomic ring buffer allocators with in-kernel bytecode filtering.[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]
- **Per-CPU Ring Buffers**: High-speed memory allocations partitioned across CPU cores to eliminate lock contention during event recording.
- **Daemon Pipeline**: `lttng-sessiond` controls kernel sessions over `ioctl` control channels, while `lttng-consumerd` reads kernel sub-buffers and writes trace archives to disk or streams them to remote relay daemons.[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]
- **Analysis Pipeline**: Trace outputs are decoded and correlated with userspace events using `babeltrace2` or Eclipse Trace Compass.[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]

[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
