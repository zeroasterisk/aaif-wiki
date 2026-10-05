---
type: architecture
title: 'Reference Architecture: PyTorch Profiler'
description: Execution tracing framework bridging PyTorch operator dispatch and ATen
  backend execution to GPU kernels and Chrome Trace timeline formats.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
tags:
- observability
- pytorch
- gpu
- profiling
- cuda
- rocm
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:31:53.717543+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The PyTorch Profiler reference architecture documents runtime execution path capture from Python-level tensor operator dispatch through the C++ ATen backend to underlying GPU hardware kernel execution [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]. Coordinated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it details how framework-level semantics are correlated with accelerator activities [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

# Architecture / Specification
The profiler integrates directly into PyTorch's execution dispatcher and hardware tracing backends [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]:
- **Op Dispatch Callbacks**: `RecordFunction` hooks capture operator names, input tensor shapes, data types, and Python/C++ stack traces at dispatch time [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].
- **Hardware Tracing Substrate**: Bundled Kineto runtime interfaces with NVIDIA CUPTI and AMD roctracer to trace CUDA/HIP kernel launches, memory allocations, and inter-device communication [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].
- **Trace Output**: Generates Chrome Trace Format JSON consumable by timeline analysis tools including Perfetto, TensorBoard, and Holistic Trace Analysis [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
