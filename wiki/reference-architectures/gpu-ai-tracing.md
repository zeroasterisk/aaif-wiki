---
type: architecture
title: GPU Driver Tracing for AI Acceleration Reference Architecture
description: Cross-vendor GPU acceleration tracing architecture capturing tensor core
  utilization, driver submissions, and hardware metrics across NVIDIA, AMD, and Intel
  platforms.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
tags:
- hardware
- gpu
- tracing
- tensor-cores
- acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

GPU driver tracing for AI acceleration defines the architectural mechanisms used to monitor tensor operations, mixed-precision compute, high-bandwidth memory transfers, and multi-GPU collective communications across hardware vendors [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]. It provides complete visibility from framework-level dispatch (such as PyTorch or TensorFlow) down to hardware tensor execution units [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# Architecture / Specification

The cross-vendor GPU tracing stack spans three key hardware ecosystems [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]:

- **NVIDIA Ecosystem**: Uses CUPTI and Nsight tools alongside Data Center GPU Manager (DCGM) to capture Tensor Core active percentages (`TENSOR_ACTIVE`), SM occupancy, and NCCL multi-GPU collectives [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **AMD Ecosystem**: Uses `roctracer` and `rocprofiler` to trace HIP API launches, KFD driver scheduling, and Matrix Core instruction counts (`SQ_INSTS_VALU_MFMA_F16`) on CDNA architectures [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **Intel Ecosystem**: Uses oneAPI Level Zero tracing and Observation Architecture (OA) counters to measure Xe Matrix Extensions (XMX) engine utilization and command queue latencies [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **Framework Correlation**: Binds high-level operator markers (NVTX, ROCTX) to hardware performance counters via [PyTorch Profiler](../reference-architectures/pytorch-profiler.md) and [AMD rocprofiler](../reference-architectures/amd-rocprofiler.md) [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# References

- GPU AI Tracing Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
