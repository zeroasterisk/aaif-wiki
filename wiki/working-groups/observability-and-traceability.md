---
type: working-group
title: Observability and Traceability Working Group
description: Technical working group standardizing agent telemetry, causal execution
  traces, cross-boundary verification, and the five-tier tracing reference architecture
  stack.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
tags:
- working-group
- observability
- tracing
- telemetry
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:18:09.925582+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview
The Observability and Traceability Working Group is an AAIF technical body developing telemetry specifications, execution trace models, and evaluation frameworks for AI agent infrastructure[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]. The working group standardizes how agent execution state, tool interactions, multi-agent coordination, and underlying hardware operations are captured, correlated, and audited across multi-tenant environments[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].

The group maintains structured reference architecture assessments spanning foundational binary formats up through runtime agent tracing, establishing unified evaluation dimensions for performance, overhead, and semantic fidelity[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].

# Architecture / Specification

The working group structures its technical assessments along a bottom-up five-layer observability stack[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]:

1. **Layer 01 — Foundations**: Baseline binary trace encodings and comparative evaluation frameworks, including the [Common Trace Format](../resources/common-trace-format.md) (CTF), the [Linux Tracing Comparison](../resources/linux-tracing-comparison.md), and [Trace Compass](../resources/trace-compass.md) for cross-domain state system analysis[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].
2. **Layer 02 — Kernel Tracing**: Operating system instrumentation and execution dynamics, evaluating [FTrace](../resources/ftrace.md), [Linux perf](../resources/linux-perf.md), [LTTng Kernel](../resources/lttng-kernel.md), [LTTng-UST](../resources/lttng-ust.md), device driver instrumentation ([Linux Driver Tracing](../resources/linux-driver-tracing.md)), [Virtualization Tracing](../resources/virtualization-tracing.md), [Container Orchestration Tracing](../resources/container-orchestration-tracing.md), [Tracy Profiler](../resources/tracy.md), and syscall inspection frameworks including [Sysdig](../resources/sysdig.md) and [Falco](../resources/falco.md)[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].
3. **Layer 03 — Hardware Accelerators**: GPU kernel dispatches, tensor core utilization, and host-device synchronization profiled via [NVIDIA Nsight](../resources/nvidia-nsight.md), [AMD ROCprofiler](../resources/amd-rocprofiler.md), [PyTorch Profiler](../resources/pytorch-profiler.md), and hardware processor tracing[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].
4. **Layer 04 — Network**: Wire-level protocol inspection, packet capture via [Wireshark](../resources/wireshark.md), and distributed communication fabrics[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].
5. **Layer 05 — AI Agent Observability**: High-level agent runtime telemetry, model interaction traces, and semantic metrics captured via [OpenTelemetry](../resources/opentelemetry.md), [Langfuse](../resources/langfuse.md), and [PostHog](../resources/posthog.md)[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].

# Lifecycle History
- **Authoritative Assessment**: Established the structured narrative and five-tier bottom-up stack in `tracing_landscape/README.md` to catalog observability technologies against agentic infrastructure[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721].

[^evt-wg-observability-and-traceability-file-69d00b3de313-cc8ae721]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/README.md
