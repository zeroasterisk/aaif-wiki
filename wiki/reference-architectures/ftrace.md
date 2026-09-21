---
type: reference-architecture
title: FTrace Kernel Function Tracing
description: Reference architecture for Linux FTrace kernel function tracing, tracefs
  filesystem interface, and dynamic NOP-to-call patching.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
tags:
- kernel
- ftrace
- linux
- observability
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:00.429590+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

FTrace is the built-in Linux kernel tracing framework providing low-overhead function tracing, function graph recording, and static tracepoint capture [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]. Assessed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as a foundational OS-level tracing mechanism, FTrace offers system-wide observability without requiring external kernel modules [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

# Architecture / Specification

FTrace relies on kernel compiler support and per-CPU ring buffers accessed through a virtual filesystem [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]:

- **Dynamic Patching**: Kernel functions compiled with `-pg` or `-mfentry` insert 5-byte NOP instructions at entry points. When tracing is enabled, NOPs are dynamically patched to calls targeting `ftrace_caller` via `text_poke_bp`, achieving near-zero overhead when disabled [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Filesystem Interface**: Configuration and telemetry retrieval are controlled via `tracefs` (mounted at `/sys/kernel/tracing/`), providing human-readable text output as well as binary ring buffers consumed by tools like `trace-cmd` and KernelShark [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Tracer Capabilities**: Supports function execution tracing, call duration graphs (`function_graph`), static tracepoints, and in-kernel histogram aggregation [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/ftrace.md
