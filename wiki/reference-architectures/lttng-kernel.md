---
type: architecture
title: LTTng Kernel Tracing
description: High-throughput, low-overhead Linux kernel tracing framework capturing
  system events into per-CPU lock-free ring buffers formatted as CTF.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
tags:
- observability
- kernel
- tracing
- lttng
- ctf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:50.363614+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

LTTng (Linux Trace Toolkit: next generation) provides high-throughput, low-overhead Linux kernel tracing through per-CPU lock-free ring buffers and the [Common Trace Format](./common-trace-format.md), enabling always-on production tracing with nanosecond-precision timestamping [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

Operating at the system infrastructure layer, LTTng instruments kernel subsystems—such as task scheduling, block I/O, networking, memory management, and system call entry/exit hooks—streaming binary events through a multi-daemon pipeline to persistent trace archives [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# Architecture / Specification

The LTTng kernel tracing pipeline is composed of the following components [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]:
- **Kernel Probe Modules (`lttng-modules`)**: Attach callbacks to static kernel tracepoints, evaluate in-kernel filter bytecode, and serialize binary event fields directly into memory [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].
- **Lock-Free Ring Buffers**: Per-CPU shared-memory buffers divided into sub-buffers allowing atomic index reservation without locking or syscall overhead on the recording path [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].
- **Session and Consumer Daemons**: The `lttng-sessiond` service manages session orchestration and probe activation, while `lttng-consumerd` asynchronously drains completed sub-buffers to disk or relay networks in CTF binary format [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# References

- Working Group: [Observability and Traceability](../working-groups/observability-and-traceability.md)
- Architecture: [Common Trace Format](./common-trace-format.md)
- Architecture: [LTTng Userspace Tracing](./lttng-ust.md)
- Resource: [Linux Kernel Tracing Comparison](../resources/linux-kernel-tracing-comparison.md)

[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
