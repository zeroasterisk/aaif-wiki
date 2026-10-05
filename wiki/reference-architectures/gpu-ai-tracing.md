---
type: reference-architecture
title: GPU Driver Tracing for AI Acceleration
description: Cross-vendor reference architecture capturing tensor core utilization,
  kernel dispatches, memory transfers, and multi-GPU coordination across NVIDIA CUPTI,
  AMD ROCm, and Intel oneAPI Level Zero driver stacks.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
tags:
- gpu
- tracing
- cupti
- rocm
- oneapi
- tensor-cores
- hardware-acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:00:16.963486+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The GPU Driver Tracing for AI Acceleration reference architecture demonstrates how GPU drivers and low-level hardware counters expose tensor execution units, kernel dispatch queues, direct memory transfers, and multi-GPU interconnects across major hardware accelerators.[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]

The architecture spans the entire AI execution path from high-level machine learning frameworks ([PyTorch](../reference-architectures/pytorch-profiler.md), TensorFlow, JAX) down through user-space acceleration runtimes (CUDA, HIP, Level Zero) and kernel drivers (`nvidia`, `amdgpu`, `i915`/`xe`) to specialized matrix math units including NVIDIA Tensor Cores, AMD Matrix FMA units, and Intel Xe Matrix Extensions (XMX).[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]

# Architecture / Specification

### Vendor Implementations

- **NVIDIA Stack**: Combines CUPTI Activity and Callback APIs, NVTX source annotations, and DCGM profiling counters to track `TENSOR_ACTIVE` metrics, SM occupancy, and NVLink/PCIe throughput.[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]
- **AMD Stack**: Uses [roctracer and rocprofiler](../reference-architectures/amd-rocprofiler.md) alongside ROCTX markers and `amdgpu` kernel tracepoints to observe HSA dispatch rings and MFMA floating-point pipelines.[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]
- **Intel Stack**: Implements oneAPI Level Zero tracing APIs (`zeCommandListAppendLaunchKernel`), OpenCL/Level Zero driver metrics, and `intel_gpu_top` JSON sampling to quantify compute engine and XMX utilization.[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]

# References

- [NVIDIA Nsight Architecture](../reference-architectures/nvidia-nsight.md)
- [AMD ROCm Profiling Architecture](../reference-architectures/amd-rocprofiler.md)
- [PyTorch Profiler Architecture](../reference-architectures/pytorch-profiler.md)

[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
