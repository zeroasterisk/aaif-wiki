---
type: deliverable
title: PyTorch Profiler Reference Architecture
description: A reference architecture defining full execution path capture from Python
  tensor operations to GPU kernels using PyTorch Profiler and Chrome Trace JSON.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
tags:
- observability
- traceability
- hardware-accelerators
- pytorch
- profiling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:51:03.171918+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
The PyTorch Profiler Reference Architecture defines mechanisms for capturing the complete execution path of tensor operations—from Python-level operation dispatch through the C++ ATen backend down to GPU kernel execution[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]. Maintained within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability), it establishes standard telemetry capture patterns across hardware accelerators.

The profile captures operator names, input shapes, data types, stack traces, GPU kernel launches, and memory allocations, producing standardized Chrome Trace Format JSON consumable by timeline visualization tools such as Perfetto, TensorBoard, and Holistic Trace Analysis[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

# Architecture / Specification
The reference architecture specifies integration points across execution tiers[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]:

- **Python User Code**: Scoped profiling contexts using `torch.profiler.profile` with step iteration boundaries to capture forward, backward, and optimizer execution.
- **ATen Dispatcher**: `RecordFunction` callbacks hooked at operation dispatch to record input shapes, dtypes, and call stacks.
- **Hardware Acceleration Layer**: Activity tracing bridging the bundled Kineto tracing library with NVIDIA CUDA (via CUPTI) and AMD ROCm (via roctracer) to measure kernel execution and memory allocations.
- **Trace Export**: Generation of Chrome Trace JSON and aggregated summary tables indexed by operator names and input shapes.

# Lifecycle History
- **2026-06-25**: Documented as an authoritative tracing landscape reference architecture within the Observability and Traceability Working Group[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7].

[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
