---
type: deliverable
title: GPU Driver Tracing Reference Architecture
description: A reference architecture evaluating GPU driver instrumentation, hardware
  performance counters, and tensor execution profiling across NVIDIA, AMD, and Intel.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
tags:
- observability
- reference-architecture
- gpu
- hardware-acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:26.447775+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
- id: evt-wg-observability-and-traceability-pr-20
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/20
  author: MatthewKhouzam
  last_modified: '2026-08-19T19:04:49+00:00'
---

# Overview

The GPU Driver Tracing Reference Architecture demonstrates how GPU drivers expose tensor core utilization, compute kernel dispatch, memory management, and multi-GPU communication through vendor-specific tracing APIs and hardware performance counters [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]. Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the document establishes end-to-end observation across the entire AI acceleration path [^evt-wg-observability-and-traceability-pr-20].

The architecture spans AI frameworks ([PyTorch](../deliverable/pytorch-profiler-reference-architecture.md), TensorFlow, JAX), vendor runtimes (CUDA, HIP, Level Zero), kernel drivers (`nvidia`, `amdgpu`, `i915`/`xe`), and hardware matrix accelerators (Tensor Cores, Matrix Cores/MFMA, Intel XMX) [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# Architecture / Specification

The architecture categorizes GPU instrumentation across three primary hardware ecosystems [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]:

- **NVIDIA**: Traces CUDA driver/runtime calls with CUPTI, timeline execution via [Nsight Systems](../deliverable/nvidia-nsight-reference-architecture.md), kernel analysis through Nsight Compute, and system-level telemetry using Data Center GPU Manager (DCGM) metrics [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **AMD**: Profiles Matrix Core (MFMA) execution, HIP API calls, and kernel dispatches using [rocprofiler/roctracer](../deliverable/amd-rocprofiler-reference-architecture.md) alongside `amdgpu` kernel tracepoints [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **Intel**: Inspects Level Zero API dispatches and Xe Matrix Extensions (XMX) utilization with VTune, Level Zero programmatic timestamp queries, and `intel_gpu_top` [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# Lifecycle History

- 2026-06-25: Merged as part of the hardware accelerator section in the tracing landscape collection [^evt-wg-observability-and-traceability-pr-20].

[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
