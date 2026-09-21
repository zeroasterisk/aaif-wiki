---
type: reference-architecture
title: NVIDIA Nsight Reference Architecture
description: Reference architecture for NVIDIA Nsight profiling tools (Nsight Systems
  and Nsight Compute) across GPU timeline tracing and kernel hardware counter analysis.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
tags:
- observability
- gpu
- tracing
- hardware
- cupti
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The NVIDIA Nsight reference architecture covers GPU workload profiling across system-level timeline tracing and per-kernel hardware counter analysis [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. Produced by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it details how NVIDIA Nsight Systems (`nsys`) and NVIDIA Nsight Compute (`ncu`) operate at the orchestration layer between application frameworks and GPU hardware [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Architecture / Specification

Nsight provides two complementary instrumentation and analysis workflows [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]:

- **Nsight Systems (`nsys`)**: Captures unified system timelines including CPU thread activity, CUDA API runtime dispatch, memory transfers (HtoD/DtoH), kernel execution durations, and user-level range annotations via the NVIDIA Tools Extension (NVTX) [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].
- **Nsight Compute (`ncu`)**: Provides deep per-kernel profiling by replaying kernel execution against hardware performance counters to assess compute throughput, tensor core utilization, memory bandwidth, and warp occupancy [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

Both tools interface with the CUDA Profiling Tools Interface (CUPTI) backend and driver performance counters [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. Integrations with frameworks such as [PyTorch Profiler](../reference-architectures/pytorch-profiler.md) allow correlated traces linking high-level model forward/backward steps down to exact kernel launches [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

[^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
