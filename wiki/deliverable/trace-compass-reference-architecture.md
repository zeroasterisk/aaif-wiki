---
type: deliverable
title: Eclipse Trace Compass Reference Architecture
description: A reference architecture evaluating Eclipse Trace Compass multi-format
  trace parsing, interval tree state-systems, and cross-layer trace correlation.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
tags:
- observability
- tracing
- trace-compass
- ctf
- timeline-analysis
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Eclipse Trace Compass is a multi-format trace analysis and visualization framework that correlates kernel, userspace, GPU, network, and AI framework traces through a disk-backed state-system engine [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]. Rather than generating traces directly, Trace Compass functions as an analysis sink that synchronizes events across diverse formats including [Common Trace Format (CTF)](../deliverable/common-trace-format-reference-architecture.md) from [LTTng](../deliverable/lttng-kernel-tracing-reference-architecture.md), FTrace, PCAP, and Chrome Trace JSON [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

Developed under the Eclipse Foundation and evaluated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), Trace Compass provides both rich desktop interfaces and headless server modes via the Trace Server Protocol (TSP), connecting to AI-driven analysis via the [TMLL Reference Architecture](../deliverable/tmll-reference-architecture.md) [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

# Architecture / Specification

Trace Compass analysis relies on several core architectural constructs [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]:
- **Input Parser Layer**: Consumes CTF, text/binary ftrace, pcap/pcapng, and Chrome Trace JSON files [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Generic State System**: Maps point-in-time trace events into interval tree state histories on disk, allowing fast querying of resource states (threads, CPUs, memory) at arbitrary timestamps [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].
- **Trace Server Protocol (TSP)**: Exposes a REST API over HTTP for headless trace indexing, experiment creation, and model querying [^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a].

[^evt-wg-observability-and-traceability-file-c7aa6ff812ce-5a7ffc2a]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/trace-compass.md
