---
type: resource
title: FTrace Reference Architecture
description: Reference architecture for Linux kernel-internal function tracing and
  event recording via tracefs and dynamic NOP patching.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/ftrace.md
tags:
- observability
- tracing
- kernel-tracing
- linux
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:54:52.117085+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/ftrace.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
FTrace is a reference architecture cataloged by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) documenting the Linux kernel's built-in function tracing and event recording infrastructure.[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1] It utilizes dynamic NOP-to-call patching to achieve zero-overhead-when-disabled function instrumentation accessible directly via the tracefs virtual filesystem.[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]

# Architecture / Specification
FTrace operates within the kernel tracing layer through several primary mechanisms:[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]
- **Dynamic Binary Patching:** Uses compiler instrumentation hooks with 5-byte NOPs replaced by ftrace_caller invocations when tracing is active.
- **Tracefs Interface:** Configured and inspected through `/sys/kernel/tracing/` without requiring external userspace runtime dependencies.
- **Tracers and Ring Buffers:** Supports function tracing, function graph call graphs, tracepoint events, and in-kernel histogram aggregation written to per-CPU ring buffers.

[^evt-wg-observability-and-traceability-file-1b8b77018443-610a7fb1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/ftrace.md
