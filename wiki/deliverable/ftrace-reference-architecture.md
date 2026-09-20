---
type: deliverable
title: FTrace Reference Architecture
description: A reference architecture evaluating Linux kernel FTrace function tracing
  and event recording via tracefs for low-overhead agent runtime host analysis.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
tags:
- observability
- kernel-tracing
- ftrace
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:51:45.199677+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The FTrace Reference Architecture documents the Linux kernel's built-in function tracing and event recording infrastructure via the `tracefs` virtual filesystem interface[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]. Assessed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it illustrates zero-overhead instrumentation when disabled and ubiquitous availability on Linux systems running agent workloads[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

# Architecture / Specification
The FTrace architecture relies on native Linux kernel mechanisms[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]:
- **Dynamic Patching**: Functions compiled with `-mfentry` default to a 5-byte NOP instruction and are dynamically patched to `call ftrace_caller` at runtime using kernel breakpoints[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Core Tracers**: Implements function tracers, function graph tracers, tracepoint event listeners, and in-kernel histogram aggregations[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Data Path**: Writes trace events to lock-free, per-CPU ring buffers exposed through `/sys/kernel/tracing/`[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
