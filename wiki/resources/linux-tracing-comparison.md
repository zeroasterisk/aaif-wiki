---
type: resource
title: Linux Kernel Tracing Technologies Comparison
description: Comparative assessment of primary Linux kernel tracing frameworks—LTTng,
  perf, and FTrace—evaluating architecture, overhead, and AAIF capability dimensions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/linux-tracing-comparison.md
tags:
- tracing
- linux
- kernel
- observability
- lttng
- perf
- ftrace
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:50:42.327804+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-313867ac2247-613905ef
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/linux-tracing-comparison.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The Linux kernel tracing ecosystem is anchored by three primary frameworks: LTTng, perf, and FTrace[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. The [Working Group Observability and Traceability](../working-groups/observability-and-traceability.md) evaluated these technologies across runtime overhead, data extraction mechanics, architectural design, and AAIF capability dimensions to establish architectural fit and identify universal capability gaps[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

# Architecture / Specification
Each framework exhibits distinct architectural tradeoffs across data acquisition, buffering, and extraction pipelines[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]:

- **[LTTng](../resources/lttng-kernel.md)**: Maintained by EfficiOS Inc. (initial release 2006, 2.0 in 2012), LTTng utilizes out-of-tree kernel modules (`lttng-modules`) and userspace daemons (`lttng-tools`)[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. It features lock-free per-CPU ring buffers extracted via kernel splice into standardized [Common Trace Format (CTF)](../resources/common-trace-format.md) binary payloads, achieving 50–150 ns probe latency when enabled with ~0 ns disabled overhead[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. Together with [LTTng-UST](../resources/lttng-ust.md), it provides unified kernel-userspace correlation visualized in [Trace Compass](../resources/trace-compass.md)[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **[perf](../resources/linux-perf.md)**: Maintained in-tree by the kernel community since Linux 2.6.31 (2009), perf integrates hardware PMU counter sampling and `perf_events` with per-event mmap buffers shared directly with userspace[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. While requiring only `linux-tools`, it incurs 100–300 ns enabled probe latency and writes to proprietary `perf.data` files analyzed via `perf report`[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **[FTrace](../resources/ftrace.md)**: Maintained in-tree by Steven Rostedt since Linux 2.6.27 (2008), FTrace provides zero-dependency kernel instrumentation built directly into `tracefs` and `trace-cmd`[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. It offers static-branch disabled latency (1–3 ns) and low enabled latency (40–100 ns) using per-CPU lock-free buffers emitting plain text or `.dat` outputs, though it lacks native userspace tracing and hardware counter support[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

# References
- [LTTng Kernel Tracing](../resources/lttng-kernel.md)
- [Linux perf](../resources/linux-perf.md)
- [FTrace Architecture](../resources/ftrace.md)
- [Common Trace Format](../resources/common-trace-format.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/linux-tracing-comparison.md
