---
type: architecture
title: AMD roctracer and rocprofiler Reference Architecture
description: Open-source GPU profiling stack for tracing HIP/HSA runtime API dispatches,
  hardware performance counters, and matrix core utilization on AMD Instinct accelerators.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
tags:
- hardware
- gpu
- profiling
- amd
- rocm
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The AMD ROCm profiling stack—comprising `roctracer`, `rocprofiler`, and the unified `rocprofiler-sdk`—provides deterministic performance counter collection and API dispatch tracing across AMD Instinct accelerators (CDNA2/CDNA3 architectures) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]. It allows AI runtime maintainers to correlate high-level framework operations with low-level Matrix Core (MFMA) execution and High Bandwidth Memory (HBM) throughput [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

# Architecture / Specification

The ROCm profiling architecture operates across multiple runtime layers [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]:

- **Application and Framework Layer**: PyTorch, TensorFlow, and JAX emit user annotations via `ROCTX` markers, interacting with `rocBLAS`, `MIOpen`, and `RCCL` [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Runtime Interception**: `roctracer` hooks HIP and HSA runtime calls, recording kernel launch timestamps (`hipLaunchKernel`) and activity duration [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Hardware Performance Counters**: `rocprofiler` queries hardware Performance Monitoring Units (PMUs) via the Kernel Fusion Driver (KFD) and `amdgpu` kernel module, measuring VALU/MFMA instruction counts (`SQ_INSTS_VALU_MFMA_F16`) and memory bus activity (`FETCH_SIZE`) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Timeline Correlation**: Tools such as Omnitrace and Omniperf export timeline traces in Perfetto-compatible JSON formats and state graphs, complementing [PyTorch Profiler](../reference-architectures/pytorch-profiler.md) and [NVIDIA Nsight](../reference-architectures/nvidia-nsight.md) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

# References

- AMD roctracer/rocprofiler Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
