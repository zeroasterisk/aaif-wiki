---
type: resource
title: NVIDIA Nsight Reference Architecture
description: Reference architecture for GPU profiling across AI workloads using Nsight
  Systems timeline tracing and Nsight Compute kernel profiling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
tags:
- gpu
- cuda
- profiling
- nsight
- hardware-acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:55:28.695732+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

NVIDIA Nsight provides system-level and kernel-level GPU profiling infrastructure for CUDA-accelerated artificial intelligence workloads [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. It encompasses two primary tools: Nsight Systems (`nsys`) for cross-process timeline tracing and Nsight Compute (`ncu`) for detailed single-kernel hardware counter analysis [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

Nsight complements framework-level profilers like the [PyTorch Profiler](../resources/pytorch-profiler.md) and informs hardware telemetry within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Architecture / Specification

The architecture spans from framework dispatches through the CUDA driver down to GPU hardware counters [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]:

- **Annotation Layer**: User code and runtime libraries emit NVIDIA Tools Extension (NVTX) range annotations to identify operations such as forward/backward passes and communication barriers [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **CUPTI Instrumentation**: The CUDA Profiling Tools Interface hooks runtime API dispatches, memory copies, and kernel launches [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **Timeline vs. Kernel Profiling**: Nsight Systems aggregates multi-GPU timeline traces with minimal runtime overhead, while Nsight Compute executes kernel replay passes to measure Tensor Core utilization, memory throughput, and warp scheduling efficiency [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

[^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
