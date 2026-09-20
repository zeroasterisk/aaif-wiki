---
type: deliverable
title: LTTng-UST Reference Architecture
description: A reference architecture evaluating LTTng Userspace Tracing (LTTng-UST)
  for zero-overhead user-space ring buffer event recording and CTF output.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
tags:
- tracing
- lttng
- userspace
- ctf
- observability
- performance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-75b688d43571-9301816c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng-UST reference architecture specifies the implementation of low-overhead userspace tracing using the Linux Trace Toolkit: next generation Userspace Tracer (LTTng-UST) [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]. It evaluates how LTTng-UST enables near-zero-overhead application instrumentation by embedding static tracepoints into native application code and writing directly into per-process shared-memory ring buffers without kernel context switches or blocking locks on the fast path.

LTTng-UST operates without root privileges and integrates with language runtimes including Python and Java logging bridges [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

# Architecture / Specification

The LTTng-UST architecture comprises three core operational elements [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]:

- **Instrumentation & RCU Fast Path**: Application processes link against `liblttng-ust` and `liburcu` (Userspace Read-Copy Update). Tracepoint execution performs lock-free atomic space reservations in shared-memory (`/dev/shm`) ring buffers.
- **Session & Consumer Daemons**: A user session daemon (`lttng-sessiond`) coordinates tracing configuration, while asynchronous consumer daemons (`lttng-consumerd`) extract buffered events and write binary streams formatted according to the [Common Trace Format Reference Architecture](../deliverable/common-trace-format-reference-architecture.md).
- **Analysis Ecosystem**: Output traces are analyzed via `babeltrace2` or GUI tools like Eclipse Trace Compass for correlation with kernel-level traces.

# Lifecycle History

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) within the foundational kernel and userspace tracing landscape [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
