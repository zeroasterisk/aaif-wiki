---
type: reference-architecture
title: 'Reference Architecture: GPU Driver Tracing for AI Acceleration'
description: Reference architecture for tracing GPU kernel dispatch, tensor core utilization,
  memory transfers, and multi-GPU communication across hardware vendors.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
tags:
- observability
- reference-architecture
- gpu
- cupti
- rocm
- hardware-acceleration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:30.127413+00:00'
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
GPU Driver Tracing for AI Acceleration documents how GPU kernel drivers and hardware performance counters expose tensor execution unit activity, kernel dispatches, memory transfers, and multi-GPU coordination across AI workloads[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]. It covers cross-layer telemetry spanning from high-level AI frameworks (PyTorch, TensorFlow, JAX) down through vendor runtimes (CUDA, HIP, Level Zero) to kernel drivers and hardware matrix engines (NVIDIA Tensor Cores, AMD Matrix Cores, Intel XMX)[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# Architecture / Specification
The reference architecture details observation models and profiling tools across major hardware vendors[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]:
- **NVIDIA**: CUPTI activity tracing, DCGM tensor utilization monitoring (`TENSOR_ACTIVE`), and Nsight Systems/Compute instrumentation[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **AMD**: ROCm `roctracer` API tracing, `rocprof` hardware performance counters, and `amdgpu` kernel tracepoints[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **Intel**: oneAPI Level Zero API tracing, kernel execution timestamps, and `intel_gpu_top` engine metrics[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# References
- GPU Driver Tracing Reference Architecture by [../working-groups/observability-and-traceability.md](observability-and-traceability.md)[^evt-wg-observability-and-traceability-pr-20]

[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
[^evt-wg-observability-and-traceability-pr-20]: https://github.com/aaif/wg-observability-and-traceability/pull/20
