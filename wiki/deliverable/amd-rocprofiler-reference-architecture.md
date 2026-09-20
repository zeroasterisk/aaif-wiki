---
type: deliverable
title: AMD ROCm Profiling Reference Architecture
description: A reference architecture evaluating AMD roctracer, rocprofiler, and rocprofiler-sdk
  for HIP dispatch tracing and GPU performance profiling.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
tags:
- observability
- tracing
- gpu
- rocm
- hardware-accelerators
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The AMD ROCm profiling stack provides hardware performance counter profiling and GPU kernel dispatch tracing for AMD Instinct accelerators across the open-source ROCm software ecosystem [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]. Consisting of `roctracer`, `rocprofiler`, and the unified `rocprofiler-sdk`, the stack observes HIP/HSA API dispatches, Matrix Core (MFMA) execution, High Bandwidth Memory (HBM) throughput, and inter-GPU communication [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

Reviewed by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), ROCm profiling forms the AMD accelerator counterpart to the [NVIDIA Nsight Reference Architecture](../deliverable/nvidia-nsight-reference-architecture.md) and integrates with the [PyTorch Profiler Reference Architecture](../deliverable/pytorch-profiler-reference-architecture.md) [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

# Architecture / Specification

The ROCm profiling architecture operates across multiple layers of the accelerator stack [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]:
- **Framework & Runtime Layer**: Intercepts HIP API runtime calls and HSA asynchronous activity queues via `roctracer` and user-defined ROCTX annotations [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Performance Counter Profiling**: Interrogates CDNA hardware execution units via `rocprofiler` / `rocprofiler-sdk` to measure MFMA instruction counts, VALU/SALU utilization, and memory bus metrics [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].
- **Driver & System Tracing**: Correlates compute events with `amdgpu` kernel driver tracepoints and `kfd` (Kernel Fusion Driver) events [^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f].

[^evt-wg-observability-and-traceability-file-d6cdc4e175fe-7b24cc0f]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/amd-rocprofiler.md
