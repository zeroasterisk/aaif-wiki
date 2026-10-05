---
type: reference-architecture
title: PyTorch Profiler Reference Architecture
description: Reference architecture capturing tensor operation execution from Python
  op dispatch through ATen backend to hardware kernel execution in Chrome Trace JSON.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
tags:
- observability
- hardware
- gpu
- profiling
- pytorch
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:58:36.921938+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The PyTorch Profiler reference architecture demonstrates how PyTorch's native profiler captures the full execution path of tensor operations from Python-level dispatch through the C++ ATen backend to hardware execution on GPUs [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]. Maintained as part of the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing landscape, it produces standardized Chrome Trace Format JSON consumable by timeline visualization tools like Perfetto, TensorBoard, and Holistic Trace Analysis [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

# Architecture / Specification
The profiler operates across the orchestration and framework layers to bridge high-level model semantics with low-level execution metrics [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]:

- **ATen Dispatcher Hooks**: Uses `RecordFunction` callbacks during operation dispatch to capture operator names, input shapes, data types, and call stack traces [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].
- **Hardware Tracing Integration**: Wraps underlying driver libraries via Kineto, interfacing with NVIDIA CUPTI for CUDA activity tracing and AMD roctracer for HIP activity tracing [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].
- **Trace Output**: Generates Chrome Trace JSON timelines and tabular key averages (`prof.key_averages()`) detailing CPU execution time, CUDA kernel durations, and memory allocations [^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
