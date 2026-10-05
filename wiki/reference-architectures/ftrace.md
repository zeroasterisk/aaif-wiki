---
type: architecture
title: 'Reference Architecture: FTrace'
description: In-kernel tracing framework providing zero-overhead function tracing
  and event recording via the tracefs filesystem interface.
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
  at: '2026-10-05T05:31:53.717543+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/ftrace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
FTrace is the built-in Linux kernel function tracing and event recording infrastructure managed via the virtual `tracefs` filesystem interface [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]. Curated under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture describes low-friction kernel execution inspection without mandatory external userspace dependencies [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

# Architecture / Specification
FTrace instrumentation relies on compiler-assisted hooks and in-kernel buffering [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]:
- **Dynamic Patching**: Kernel functions compiled with `-mfentry` contain 5-byte NOP instructions when inactive, dynamically patched via `text_poke_bp` to invoke tracing callers when enabled [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Tracefs Control**: Tracing configuration, event filtering, and output streams are managed through `/sys/kernel/tracing/` (or debugfs mounts) [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].
- **Tracer Engines**: Supports function tracing, function graph call-tree execution timing, static tracepoint events, and in-kernel histogram triggers written to per-CPU lock-free ring buffers [^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1].

[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/ftrace.md
