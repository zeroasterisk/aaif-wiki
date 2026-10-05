---
type: reference-architecture
title: FTrace Linux Kernel Tracing Reference Architecture
description: Reference architecture implementing zero-overhead dynamic NOP-to-call
  patched kernel function tracing and event recording via tracefs.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/ftrace.md
tags:
- observability
- linux
- kernel
- ftrace
- tracing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:58:36.921938+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/ftrace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
FTrace is the built-in Linux kernel tracing infrastructure providing function tracing and event recording via the `tracefs` virtual filesystem interface [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]. Evaluated within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), FTrace provides zero-overhead-when-disabled instrumentation by dynamically patching 5-byte NOPs to call instructions at kernel function entry points [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

# Architecture / Specification
FTrace operates within the system kernel layer without requiring third-party kernel modules [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]:

- **Instrumentation Mechanism**: Compiled with `-pg`/`-mfentry`, kernel function entry points default to 5-byte NOPs and are dynamically replaced via `text_poke_bp` with calls to `ftrace_caller` when tracing is activated [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Core Tracers**: Offers `function` (entry logging), `function_graph` (call duration and call graph hierarchy), and tracepoint event recording [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Ring Buffers and Interface**: Writes records to lock-free per-CPU ring buffers in kernel memory, exposed to userspace through `/sys/kernel/tracing/` (or `trace-cmd`) in human-readable text and binary formats [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/ftrace.md
