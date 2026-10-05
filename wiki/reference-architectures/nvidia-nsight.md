---
type: reference-architecture
title: NVIDIA Nsight Reference Architecture
description: Reference architecture detailing system-wide timeline tracing and per-kernel
  hardware counter profiling across CUDA workloads via CUPTI and NVTX.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
tags:
- observability
- gpu
- nvidia
- profiling
- cuda
- hardware-accelerators
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:04.610410+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The NVIDIA Nsight reference architecture provides end-to-end tracing and profiling for CUDA-accelerated workloads across AI frameworks, runtimes, and hardware accelerators [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. It covers system-wide timeline capture via Nsight Systems and detailed per-kernel hardware counter analysis via Nsight Compute [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Architecture / Specification

The architecture operates between AI application frameworks (PyTorch, TensorFlow, JAX) and physical GPU hardware [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]:

- **NVTX Annotations**: Frameworks and libraries (cuDNN, cuBLAS, NCCL) emit user-defined hierarchical ranges annotating training loops, forward/backward passes, and communication barriers [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **Nsight Systems (`nsys`)**: Instruments the CUDA runtime via CUPTI (CUDA Profiling Tools Interface) to build comprehensive multi-GPU timelines correlating CPU thread scheduling, memory copies, and kernel launches [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **Nsight Compute (`ncu`)**: Executes kernel replay to read physical performance monitors (PMUs), evaluating Warp occupancy, Tensor Core utilization, memory throughput, and instruction stalls [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# References

- [PyTorch Profiler Reference Architecture](pytorch-profiler.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
