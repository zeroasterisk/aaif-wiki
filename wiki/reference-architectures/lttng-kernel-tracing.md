---
type: reference-architecture
title: LTTng Kernel Tracing Reference Architecture
description: 'Reference architecture for Linux Trace Toolkit: next generation (LTTng)
  kernel tracing via lock-free per-CPU ring buffers and CTF event serialization.'
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
tags:
- observability
- lttng
- kernel
- tracing
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng Kernel Tracing reference architecture demonstrates high-throughput, low-overhead kernel-level instrumentation across the Linux kernel subsystem [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]. Curated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it details how `lttng-modules` instruments kernel tracepoints, scheduler events, syscalls, and block I/O with nanosecond precision [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# Architecture / Specification

LTTng kernel tracing operates via an infrastructure pipeline optimized for production environments [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]:

- **Kernel Probe Callbacks (`lttng-modules`)**: Serializes event fields directly into per-CPU lock-free kernel ring buffers using atomic reservations, avoiding system locks or costly context switches [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].
- **Daemon Pipeline**: The central `lttng-sessiond` coordinates tracing sessions and controls dynamic probe activation, while `lttng-consumerd` reads kernel buffers and writes out structured [Common Trace Format (CTF)](../reference-architectures/ctf.md) archives [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].
- **Kernel Subsystem Coverage**: Captures process scheduling (`sched_*`), block storage I/O, network device queues, and syscall enter/exit boundaries to trace system-level latency and resource contention [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
