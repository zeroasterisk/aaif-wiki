---
type: reference-architecture
title: AMD ROCm Profiling Architecture
description: Reference architecture for AMD ROCm profiling covering roctracer HIP/HSA
  API tracing, rocprofiler hardware performance counter collection, and rocprofiler-sdk
  on AMD Instinct accelerators.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
tags:
- amd
- rocm
- gpu
- profiling
- roctracer
- rocprofiler
- hardware-acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:00:16.963486+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The AMD ROCm Profiling reference architecture specifies the instrumentation stack used to trace compute dispatches, collect hardware performance counters, and profile Matrix Core (MFMA) instruction execution on AMD Instinct GPUs (MI200/MI300 series).[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]

Spanning from the user application and framework level down through the HIP/HSA runtimes to the `amdgpu` kernel driver and CDNA hardware execution units, the stack provides deep visibility into memory bandwidth (HBM), collective communication (RCCL), and mixed-precision matrix compute operations.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]

# Architecture / Specification

### Core Components

- **roctracer**: Captures HIP and HSA runtime API calls and asynchronous activity records (kernel launch durations, memory copies) using dynamic interception.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]
- **rocprofiler & rocprof CLI**: Samples and multiplexes hardware performance counters, monitoring matrix instruction execution (`SQ_INSTS_VALU_MFMA`), memory fetch volumes, and compute unit occupancy.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]
- **rocprofiler-sdk**: The unified next-generation C/C++ profiling API introduced in ROCm 6.0+ that combines tracing, counter sampling, and tool callbacks.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]
- **ROCTX**: User-space code annotation API embedded in ML frameworks like [PyTorch](../reference-architectures/pytorch-profiler.md) to delineate training steps, forward passes, and backward graph execution.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]
- **Kernel Fusion Driver (KFD) & ftrace**: Mainline `amdgpu` kernel module tracepoints exposing command submission ioctls (`amdgpu_cs_ioctl`) and scheduler fence events.[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]

# References

- [AMD ROCm Documentation](https://rocm.docs.amd.com/)
- [GPU Driver Tracing for AI Acceleration](../reference-architectures/gpu-ai-tracing.md)
- [NVIDIA Nsight Architecture](../reference-architectures/nvidia-nsight.md)

[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
