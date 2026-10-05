---
type: architecture
title: NVIDIA Nsight
description: GPU profiling and timeline tracing suite for hardware counter analysis,
  kernel execution metrics, and multi-GPU communication across CUDA AI workloads.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
tags:
- observability
- profiling
- hardware-accelerators
- gpu
- cuda
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:16.200381+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

NVIDIA Nsight is a GPU profiling and performance analysis suite composed of Nsight Systems (`nsys`) for system-wide timeline tracing and Nsight Compute (`ncu`) for per-kernel hardware counter profiling [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. It evaluates hardware accelerator performance across model execution and AI workload dispatch [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

Evaluated within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), Nsight bridges the application framework layer (e.g., [PyTorch Profiler](pytorch-profiler.md)) and CUDA driver runtimes down to GPU hardware counters [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Architecture / Specification

The Nsight architecture operates at the orchestration and hardware execution layers [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]:

- **CUPTI Instrumentation**: The CUDA Profiling Tools Interface intercepts runtime API calls, kernel launches (`cuLaunchKernel`), memory transfers, and synchronization primitives [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **NVTX Range Annotations**: Enables applications and libraries (cuDNN, cuBLAS, NCCL) to inject user-defined markers and hierarchical range annotations across training and inference passes [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **Timeline Tracing vs. Kernel Replay**: Nsight Systems tracks end-to-end multi-GPU timelines with minimal overhead, while Nsight Compute uses multi-pass kernel replay to measure tensor core utilization, memory bandwidth, and occupancy [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

[^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
