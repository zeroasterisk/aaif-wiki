---
type: reference-architecture
title: LTTng-UST Reference Architecture
description: Reference architecture for LTTng Userspace Tracing (LTTng-UST) providing
  lock-free shared-memory ring buffer tracing for applications.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
tags:
- observability
- lttng
- ust
- tracing
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-75b688d43571-9301816c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng-UST reference architecture defines high-throughput, low-overhead userspace tracing within application processes without requiring kernel transitions or locks on the fast path [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]. Curated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), it details tracepoint provider instrumentation and shared-memory communication mechanisms [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

# Architecture / Specification

LTTng-UST instruments compiled applications (C/C++) and managed runtimes (Python, Java) via tracepoint providers [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]:

- **Fast-Path Ring Buffers**: Employs Userspace RCU (`liburcu`) and per-CPU shared-memory ring buffers (`/dev/shm`) to write binary trace events with sub-microsecond latency [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Session Coordination**: A per-user or root `lttng-sessiond` daemon manages tracing sessions, while a separate consumer daemon (`lttng-consumerd`) extracts ring buffer pages directly into [Common Trace Format (CTF)](../reference-architectures/ctf.md) trace streams [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **No Root Requirement**: Unlike kernel tracing, userspace tracing can run unprivileged, isolating instrumentation within the user session [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/02-kernel-tracing/lttng-ust.md
