---
type: resource
title: PyTorch Profiler Reference Architecture
description: Reference architecture documenting PyTorch Profiler instrumentation across
  Python dispatch, ATen backend, and GPU kernel execution.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
tags:
- observability
- tracing
- hardware-accelerators
- pytorch
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:54:52.117085+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
PyTorch Profiler is a reference architecture maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) demonstrating how PyTorch captures tensor execution paths from Python dispatch down to hardware GPU kernel execution.[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7] It produces standardized Chrome Trace Format JSON consumable by visualization and analysis tools such as Perfetto, TensorBoard, and Holistic Trace Analysis.[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]

# Architecture / Specification
The profiler bridges framework semantics and hardware execution across key architectural layers:[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]
- **PyTorch Dispatcher (ATen):** Uses RecordFunction callbacks at op dispatch points to record operator names, input tensor shapes, data types, and stack traces.
- **Hardware Activity Tracing:** Utilizes the bundled Kineto library to interface with NVIDIA CUPTI or AMD roctracer for GPU kernel activities, memory allocations, and communication collectives.
- **Output & Consumption:** Exports execution data as Chrome Trace JSON files and formatted key average summary tables for latency analysis.

[^evt-wg-observability-and-traceability-file-0ab0d50c96e0-9cea1fd7]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/pytorch-profiler.md
