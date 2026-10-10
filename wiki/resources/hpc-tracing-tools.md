---
type: resource
title: HPC Binary and Instruction Tracing Tools
description: Reference architecture evaluating dynamic binary instrumentation and
  post-mortem visualization across CPU (Intel PIN), GPU (AMD Luthier), and OTF2 traces
  (Vampir).
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/hpc-tracing.md
tags:
- observability
- hpc
- gpu-tracing
- instrumentation
- visualization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:43.095337+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/hpc-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview

HPC binary instrumentation and trace visualization tools operate at the micro-architectural and dynamic binary level to observe and replay execution across heterogeneous compute environments [^evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7]. By combining dynamic binary instrumentation (DBI) on CPU and GPU pipelines with scalable post-mortem visualization engines, this toolchain enables deep instruction-level profiling, memory access analysis, and distributed timeline visualization for AI training and agent infrastructure [^evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7].

# Architecture / Specification

The HPC instrumentation pipeline is divided across distinct execution layers [^evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7]:

- **Intel PIN**: CPU-level dynamic binary instrumentation engine that intercepts and JIT-recompiles x86/x86-64 machine instructions at runtime to insert arbitrary analysis callbacks without needing binary recompilation.
- **AMD Luthier**: Dynamic GPU ISA binary instrumentation framework operating at the HSA AQL packet dispatch level, patching GPU kernel binaries to track SIMD-lane memory accesses and latency on AMD Instinct hardware.
- **Vampir**: Distributed trace analysis and visualization tool that ingests Open Trace Format 2 (OTF2) files produced by tools like Score-P or TAU, utilizing a parallel `VampirServer` backend to render timelines and communication matrices across tens of thousands of processes [^evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7].

[^evt-wg-observability-and-traceability-file-0a6867909dde-4e2513a7]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/hpc-tracing.md
