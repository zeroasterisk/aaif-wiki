---
type: assessment
title: Linux Kernel Tracing Technologies Assessment
description: Comparative assessment evaluating LTTng, perf, and FTrace across overhead,
  userspace tracing, ring buffer design, and AAIF dimensions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
tags:
- observability
- linux
- kernel
- lttng
- perf
- ftrace
- assessment
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:58:36.921938+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-313867ac2247-613905ef
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The Linux Kernel Tracing Technologies Assessment evaluates the three primary Linux tracing frameworks — LTTng, perf, and FTrace — across architectural mechanics, overhead profiles, and AAIF evaluation dimensions [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. Conducted by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the assessment identifies the operational trade-offs and structural gaps in existing low-level system tracing tools when applied to AI workloads [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

# Architectural Comparison
The assessment contrasts key technical characteristics across the three frameworks [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]:

- **FTrace**: Built directly into the Linux kernel with zero installation friction, using dynamic NOP patching and tracefs for kernel function and graph tracing [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]. See [FTrace Reference Architecture](../reference-architectures/ftrace.md).
- **perf**: Standard Linux userspace tool using `perf_events` and mmap'd ring buffers, excelling in PMU hardware performance counter correlation and profile sampling [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].
- **LTTng**: Kernel module and userspace tracer (`LTTng-UST`) writing standardized Common Trace Format (CTF) binary streams via splice, delivering low probe overhead (50–150 ns enabled) and correlation across kernel-userspace boundaries [^evt-wg-observability-and-traceability-file-313867ac2247-613905ef].

[^evt-wg-observability-and-traceability-file-313867ac2247-613905ef]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/linux-tracing-comparison.md
