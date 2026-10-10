---
type: resource
title: Processor Tracing (Intel PT, ARM ETM, AMD IBS)
description: Reference architecture evaluating hardware processor tracing (Intel PT,
  ARM ETM, AMD IBS/BRS) for cycle-accurate control flow reconstruction and micro-architectural
  analysis.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/processor-tracing.md
tags:
- observability
- hardware
- cpu-tracing
- profiling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:43.095337+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/processor-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview

Hardware processor tracing provides instruction-level control flow capture and micro-architectural observability with sub-5% runtime overhead by recording execution directly within CPU pipeline hardware [^evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee]. Operating below kernel tracing systems like [FTrace](../resources/ftrace.md) and [LTTng](../resources/lttng-kernel.md), processor tracing generates ground truth execution streams that allow exact deterministic replay, precise memory access profiling, and complete call-graph recovery for AI runtimes and inference engines [^evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee].

# Architecture / Specification

Processor tracing spans two complementary architectural models across major CPU architectures [^evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee]:

- **Continuous Full-Stream Tracing (Intel PT and ARM ETM)**: Records every control flow branch, interrupt, and hardware exception into compressed packet streams. Decoding requires the exact unstripped binary on disk to reconstruct full instruction streams between recorded branches.
- **Sampled Micro-architectural Snapshots (AMD IBS / BRS / LBR)**: Samples instruction operations with full hardware pipeline context, capturing L1/L2/L3 cache misses, translation lookaside buffer (TLB) misses, and NUMA memory latency data.

Integration with userspace analysis tooling is managed via Linux [perf](../resources/linux-perf.md) subsystems, `libipt` (for Intel PT decode), and OpenCSD (for ARM CoreSight ETMv4 decode) [^evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee].

[^evt-wg-observability-and-traceability-file-627b985ddbc5-b81f64ee]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/processor-tracing.md
