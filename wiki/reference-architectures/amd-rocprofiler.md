---
type: reference-architecture
title: AMD ROCm Profiling Reference Architecture
description: Reference architecture for AMD roctracer, rocprofiler, and rocprofiler-sdk
  GPU kernel dispatch tracing and Matrix Core hardware counter collection.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
tags:
- observability
- gpu
- profiling
- amd
- rocm
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

AMD's ROCm profiling ecosystem—comprising `roctracer`, `rocprofiler`, and the unified `rocprofiler-sdk`—provides hardware counter collection, HIP/HSA API tracing, and kernel dispatch monitoring for AMD Instinct accelerators (CDNA architecture) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]. It provides an open-source counterpart to [NVIDIA Nsight](../reference-architectures/nvidia-nsight.md) for GPU execution observability in AI model training and inference workloads.

# Architecture / Specification

- **API & Activity Tracing (`roctracer`)**: Captures HIP and HSA runtime API invocations, asynchronous memory transfers, and GPU kernel execution intervals [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Hardware Performance Counters (`rocprofiler`)**: Accesses CDNA Performance Counters directly via the `amdgpu` kernel driver and Kernel Fusion Driver (KFD), measuring Matrix Core (MFMA) instruction execution, HBM bandwidth, and compute unit occupancy.
- **User Annotations (ROCTX)**: C/C++ and Python API allowing frameworks like [PyTorch](../reference-architectures/pytorch-profiler.md) to insert range markers and correlation IDs across host execution and GPU dispatches.

[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
