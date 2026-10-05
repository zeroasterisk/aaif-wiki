---
type: architecture
title: LTTng-UST
description: High-throughput, low-overhead userspace tracing framework recording application
  events into shared-memory ring buffers without kernel transitions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
tags:
- observability
- tracing
- userspace
- low-overhead
- ctf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:16.200381+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-75b688d43571-9301816c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

LTTng Userspace Tracing (LTTng-UST) is a high-performance instrumentation library that records trace events directly from application code into shared-memory ring buffers with near-zero overhead [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]. It executes on the fast path without kernel transitions or system call locks [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

Maintained under the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) tracing taxonomy, LTTng-UST complements kernel tracing solutions like [ftrace](ftrace.md) and provides unprivileged userspace event extraction in Common Trace Format (CTF) [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

# Architecture / Specification

LTTng-UST instrumentation operates via decoupled daemons and shared memory [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]:

- **Tracepoint Providers**: Static C/C++ tracepoints or language agents (Python, Java JUL/Log4j) compiled into the application execute Userspace RCU (`liburcu`) primitives to check trace enablement and write payload data [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Shared-Memory Buffers**: Per-process or per-channel ring buffers residing in `/dev/shm` isolate writer threads from consumer threads [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Consumer and Session Daemons**: Unprivileged user session daemons coordinate tracing sessions while asynchronous consumer daemons extract event streams into binary CTF files on disk [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
