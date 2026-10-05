---
type: reference-architecture
title: LTTng Kernel Tracing
description: High-throughput kernel tracing infrastructure capturing system calls
  and subsystem events via per-CPU lock-free ring buffers into CTF archives.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
tags:
- observability
- tracing
- lttng
- kernel
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:35.951599+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng Kernel Tracing reference architecture details the Linux Trace Toolkit: next generation (LTTng) kernel instrumentation pipeline, providing high-throughput, low-overhead system tracing for production workloads[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

Operating at the system infrastructure layer below application telemetry, LTTng instruments the scheduler, block I/O, network stack, memory allocator, and syscall entry/exit points, emitting structured traces encoded in the [Common Trace Format](common-trace-format.md)[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

# Architecture / Specification

The LTTng kernel tracing pipeline consists of modular kernel and userspace components[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]:

- **Kernel Probe Modules (`lttng-modules`)**: Hooks into kernel tracepoints, serializing event fields into binary CTF format with kernel-side bytecode filtering.
- **Per-CPU Ring Buffers**: Lock-free atomic shared-memory buffers providing sub-microsecond event capture latency without locking system threads.
- **Control and Consumer Daemons (`lttng-tools`)**: Manages session configuration (`lttng-sessiond`) and asynchronous trace consumption (`lttng-consumerd`) streaming to disk or remote relay daemons.
- **Analysis Pipeline**: Compatible with reader tooling including `babeltrace2` and [Eclipse Trace Compass](trace-compass.md)[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e].

[^evt-wg-observability-and-traceability-file-a89c345fb239-c8c4744e]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-kernel-tracing.md
