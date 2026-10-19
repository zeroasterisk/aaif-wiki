---
type: working-group
title: Observability and Traceability Working Group
description: AAIF technical working group standardizing telemetry schemas, OpenTelemetry
  semantic conformance, and cross-layer tracing reference architectures from kernel
  to AI agents.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
tags:
- working-groups
- observability
- tracing
- telemetry
- opentelemetry
- architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:59:33.542673+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview
The Observability and Traceability Working Group is an AAIF technical body chartered to establish vendor-neutral telemetry specifications, tracing frameworks, and evidence-grade observability models for agentic AI systems.[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721] The group's work covers end-to-end tracing methodologies spanning low-level operating system mechanisms, hardware accelerators, network protocols, and high-level agent runtime behaviors.[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]

# Architecture / Specification

## Five-Layer Reference Architecture Framework
The working group organizes its technology assessments and reference architectures along a bottom-up narrative stack structured into five discrete architectural layers:[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]

1. **Layer 01 — Foundations**: Focuses on trace encoding, binary formats, and comparative frameworks, including the [Common Trace Format](../resources/common-trace-format.md) (CTF) for zero-copy nanosecond recording and [Trace Compass](../resources/trace-compass.md) for cross-domain trace visualization.[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]
2. **Layer 02 — Kernel Tracing**: Analyzes operating system observability facilities, including [FTrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), [LTTng Kernel](../resources/lttng-kernel.md), [LTTng-UST](../resources/lttng-ust.md), kernel driver tracing, container scheduling and CFS throttling ([Container Orchestration Tracing](../resources/container-orchestration-tracing.md)), hypervisor stolen-time distortion ([Virtualization Tracing](../resources/virtualization-tracing.md)), [Tracy](../resources/tracy.md), [sysdig](../resources/sysdig.md), and [Falco](../resources/falco.md).[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]
3. **Layer 03 — Hardware Accelerators**: Evaluates hardware profiling mechanisms, GPU kernel dispatches, tensor core utilization, and correlation across frameworks and accelerators (e.g., [NVIDIA Nsight](../resources/nvidia-nsight.md), [AMD ROCprofiler](../resources/amd-rocprofiler.md), and [PyTorch Profiler](../resources/pytorch-profiler.md)).[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]
4. **Layer 04 — Network**: Analyzes on-the-wire communication, protocol verification, and packet capture using tools such as [Wireshark](../resources/wireshark.md).[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]
5. **Layer 05 — AI Agent Observability**: Governs agent runtimes, LLM distributed tracing backends, product analytics, and semantic conventions mapping agent decisions to underlying system events.[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]

## Core Initiatives and Specifications
- Telemetry specifications including the [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md).
- Cross-boundary observability mapping telemetry propagation across agent harnesses, tool calls, and host environments via the [Cross-Boundary Observability Model](../resources/cross-boundary-observability-model.md).
- Telemetry ingestion through vendor-neutral standards such as [OpenTelemetry](../resources/opentelemetry.md).

# Lifecycle History
- Authoritative reference architecture assessments established covering foundational encoding through AI agent observability layers.[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]

[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
