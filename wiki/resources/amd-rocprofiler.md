---
type: resource
title: AMD ROCm Profiling Stack
description: Open-source GPU kernel dispatch tracing and hardware counter profiling
  architecture for AMD Instinct accelerators across HIP, HSA, and CDNA architectures.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
tags:
- gpu
- amd
- rocm
- hardware-counters
- profiling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The AMD ROCm profiling stack comprises roctracer, rocprofiler, and the unified rocprofiler-sdk for deep hardware and driver observability across AMD Instinct accelerators (CDNA architecture) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]. It provides end-to-end tracing across the full AI acceleration path, spanning PyTorch operator dispatches, HIP/HSA runtime API interactions, kernel driver job queues, and hardware Matrix Core (MFMA) execution units [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

# Architecture / Specification

The ROCm instrumentation architecture operates across several abstraction boundaries [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]:

- **Application & Framework Annotations**: PyTorch and ML frameworks leverage ROCTX markers to delimit training iterations, forward/backward passes, and collective communications [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **API & Activity Tracing (`roctracer`)**: Intercepts HIP and HSA runtime calls, tracking asynchronous kernel dispatches, queue latencies, and signal synchronizations [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Hardware Performance Counters (`rocprofiler` / `rocprofiler-sdk`)**: Interfaces with on-chip performance monitoring counters to quantify Matrix Core (MFMA) instruction counts, High Bandwidth Memory (HBM) throughput, and ALU vector unit saturation [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Kernel Driver Subsystem**: Integrates with the upstream `amdgpu` driver and Kernel Fusion Driver (KFD) via [ftrace](../resources/ftrace.md) tracepoints (`amdgpu_cs_ioctl`, `amdgpu_sched_run_job`) to observe GPU command submission rings and fence completions [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
