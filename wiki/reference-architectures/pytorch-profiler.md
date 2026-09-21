---
type: reference-architecture
title: PyTorch Profiler Reference Architecture
description: Reference architecture for capturing tensor operations and GPU kernel
  execution traces via PyTorch Profiler into Chrome Trace format.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
tags:
- observability
- tracing
- hardware-accelerators
- pytorch
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:54:28.893595+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The PyTorch Profiler reference architecture demonstrates how PyTorch's built-in profiling instrumentation captures the full execution path of tensor operations—from Python-level operator dispatch through the C++ ATen backend to GPU kernel execution on hardware accelerators[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]. Developed within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture bridges framework-level semantics (such as model layers and optimizer steps) with underlying hardware execution details (such as CUDA/HIP kernels, memory allocations, and collective communications)[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

# Architecture / Specification

The profiler operates across Python user code, PyTorch ATen dispatcher hooks, and GPU execution backends using the bundled Kineto tracing library[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]:

- **Python User Code**: Instrumentation occurs via the `torch.profiler.profile` context manager, tracking execution iterations and marking step boundaries with `prof.step()`.
- **Dispatcher and Hooks**: ATen operator dispatch triggers `RecordFunction` callbacks that capture operator names, input tensor shapes, data types, and stack traces.
- **Hardware Tracing**: Leverages CUPTI (on NVIDIA via CUDA Toolkit 12.x+) or roctracer (on AMD via ROCm 6.x+) to record kernel launches, memory allocations/deallocations, and execution timing.
- **Output Formats**: Generates standardized Chrome Trace JSON (`traceEvents` array) exportable for analysis in Chrome tracing (`chrome://tracing`), Perfetto, TensorBoard (via `tensorboard_trace_handler`), and Holistic Trace Analysis (HTA).

[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
