---
type: resource
title: GPU Driver Tracing for AI Acceleration
description: Cross-vendor reference architecture capturing tensor core activity, kernel
  dispatch, memory transfers, and multi-GPU interconnects across NVIDIA, AMD, and
  Intel hardware.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
tags:
- gpu
- tensor-cores
- hardware-tracing
- observability
- cuda
- rocm
- level-zero
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

GPU driver tracing for AI workloads encompasses the specialized interfaces, counters, and tracepoints used to observe tensor matrix computation, memory hierarchies, and multi-accelerator fabrics across modern hardware architectures [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]. It bridges high-level model execution in frameworks like [PyTorch](../resources/pytorch-profiler.md) with low-level kernel driver scheduling and hardware execution units [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

# Architecture / Specification

The cross-vendor GPU tracing stack spans three major hardware paradigms [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]:

- **NVIDIA Ecosystem**: Uses CUPTI and [NVIDIA Nsight](../resources/nvidia-nsight.md) for CUDA API timeline collection and Tensor Core instruction tracking, paired with Data Center GPU Manager (DCGM) for telemetry fields including `TENSOR_ACTIVE`, `SM_OCCUPANCY`, and NVLink interconnect metrics [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **AMD Ecosystem**: Leverages [AMD ROCm profiling](../resources/amd-rocprofiler.md) (`roctracer` and `rocprofiler`) to trace HIP dispatch queues, HSA asynchronous signals, and CDNA Matrix Core (MFMA) hardware counters alongside kernel-level `amdgpu` scheduler tracepoints [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].
- **Intel Ecosystem**: Implements Intel oneAPI Level Zero tracing APIs and Open Source Observation Architecture (OA) metrics to monitor Xe Matrix Extensions (XMX) engine utilization and command queue latencies [^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826].

[^evt-wg-observability-and-traceability-file-f612edccd3bb-3e43a826]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/gpu-ai-tracing.md
