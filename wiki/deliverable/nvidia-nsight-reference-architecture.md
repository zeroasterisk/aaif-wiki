---
type: deliverable
title: NVIDIA Nsight Reference Architecture
description: A reference architecture evaluating NVIDIA Nsight Systems timeline tracing
  and Nsight Compute per-kernel profiling across GPU-accelerated AI execution paths.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
tags:
- tracing
- gpu
- hardware-accelerators
- observability
- cuda
- nsight
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The NVIDIA Nsight reference architecture defines the evaluation of GPU profiling and tracing tools across CUDA-accelerated machine learning and AI agent infrastructure [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]. It covers two complementary profilers built on the CUDA Profiling Tools Interface (CUPTI) and the NVIDIA Tools Extension (NVTX) annotation framework: Nsight Systems (`nsys`) for end-to-end timeline tracing and Nsight Compute (`ncu`) for per-kernel hardware counter analysis.

Nsight operates between higher-level AI frameworks such as PyTorch or JAX and the underlying GPU hardware, capturing execution metrics from application layer dispatches down to kernel execution, memory transfers, and multi-GPU NCCL communication [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Architecture / Specification

The Nsight architecture consists of two primary operational paths for observability [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]:

- **Nsight Systems (Timeline Observability)**: Uses CUPTI activity and callback APIs combined with OS-level sampling to record unified timeline traces spanning CPU thread dispatches, CUDA runtime API calls, GPU kernel execution intervals, memory copies, and user-defined NVTX markers. Traces are emitted as SQLite databases or exported to Chrome trace JSON format.
- **Nsight Compute (Kernel Profiling)**: Intercepts individual GPU kernel launches using hardware performance monitor (PM) counters and kernel replay. It provides granular hardware utilization statistics, including Tensor Core activity, roofline model analysis, memory throughput, and Warp occupancy.

Integration with upstream AI frameworks builds upon the model evaluated in the [PyTorch Profiler Reference Architecture](../deliverable/pytorch-profiler-reference-architecture.md), linking software runtime events to hardware kernel invocations [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

# Lifecycle History

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) within the hardware accelerator tracing landscape workstream [^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff].

[^evt-wg-observability-and-traceability-file-6ce558ba5e3a-530b02ff]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/03-hardware-accelerators/nvidia-nsight.md
