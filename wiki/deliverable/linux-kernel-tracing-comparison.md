---
type: deliverable
title: Linux Kernel Tracing Comparison Assessment
description: A comparative assessment evaluating LTTng, perf, and FTrace across observability
  dimensions for agentic host environments.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
tags:
- observability
- kernel-tracing
- perf
- lttng
- ftrace
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:51:45.199677+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-313867ac2247-613905ef
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The Linux Kernel Tracing Comparison Assessment provides an architectural evaluation of the three primary Linux tracing frameworks—LTTng, Linux perf, and FTrace—across core observability, security, and performance dimensions[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. Published by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it provides guidance on selecting tracing tools for lower-layer host and runtime observability[^evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6][^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

# Architecture / Specification
The assessment compares the technologies across several architectural axes[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]:
- **FTrace**: Built-in, zero external dependencies, primary strength in kernel function flow and entry/exit graphs via `tracefs`[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **perf**: Built-in kernel subsystem optimized for hardware Performance Monitoring Unit (PMU) counters and statistical sampling[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **LTTng**: External module system with per-CPU lock-free ring buffers outputting Common Trace Format (CTF), tailored for unified kernel and userspace tracing (LTTng-UST)[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/linux-tracing-comparison.md
[^evt-wg-observability-and-traceability-file-69d00b3de313-41c8aea6]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/README.md
