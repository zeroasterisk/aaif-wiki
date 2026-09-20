---
type: deliverable
title: LTTng Kernel Tracing Reference Architecture
description: A reference architecture evaluating LTTng kernel tracing, lock-free per-CPU
  ring buffers, and CTF serialization for production OS telemetry.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
tags:
- tracing
- lttng
- kernel
- linux
- ctf
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng Kernel Tracing reference architecture specifies low-overhead, high-throughput operating system tracing using LTTng kernel modules [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]. It evaluates how LTTng instruments core Linux kernel subsystems—including the task scheduler, block I/O, network stack, memory subsystem, and system call boundaries—using compiled probe modules and per-CPU lock-free ring buffers.

LTTng kernel tracing records nanosecond-precision binary events directly into the [Common Trace Format Reference Architecture](../deliverable/common-trace-format-reference-architecture.md), supporting production tracing with sub-microsecond overhead per event [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# Architecture / Specification

The kernel tracing pipeline consists of three major tiers [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]:

- **Kernel Probe Modules (`lttng-modules`)**: Dynamically loaded kernel modules that attach callbacks to Linux kernel tracepoints, kprobes, and syscall entry/exit points, serializing arguments into binary CTF layouts.
- **Per-CPU Ring Buffers**: Kernel-space memory buffers partitioned per CPU where trace events are written using atomic reservations without global kernel locks.
- **Userspace Control & Consumption**: The `lttng-sessiond` daemon manages sessions, channel configurations, and kernel-side filtering bytecodes, while `lttng-consumerd` streams buffered pages to disk or remote relay daemons.

Comparative trade-offs between LTTng, perf, and FTrace are further explored in the [Linux Kernel Tracing Comparison](../deliverable/linux-kernel-tracing-comparison.md) [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# Lifecycle History

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) within the kernel-level tracing landscape deliverable track [^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
