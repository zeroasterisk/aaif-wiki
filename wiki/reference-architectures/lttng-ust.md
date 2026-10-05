---
type: reference-architecture
title: LTTng-UST Userspace Tracing Reference Architecture
description: Reference architecture capturing near-zero-overhead userspace tracepoints
  directly into shared-memory ring buffers without kernel transitions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
tags:
- observability
- lttng
- lttng-ust
- userspace
- ring-buffer
- ctf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:04.610410+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-75b688d43571-9301816c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The LTTng-UST reference architecture demonstrates high-throughput, low-overhead userspace tracing by compiling static tracepoints directly into application code [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]. It records events into lock-free shared-memory ring buffers without requiring kernel context switches on the fast path [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

# Architecture / Specification

LTTng-UST instruments application processes while decoupling event emission from trace persistence [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]:

- **In-Process Instrumentation**: Applications link `liblttng-ust` and Userspace RCU (`liburcu`), evaluating tracepoint activation status via single-instruction conditional branches [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Shared-Memory Ring Buffers**: Emitted events write directly into per-CPU ring buffers in `/dev/shm` without system calls or kernel locking [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Daemon Coordination**: An unprivileged `lttng-sessiond` coordinates tracing sessions and signals an asynchronous consumer daemon (`lttng-consumerd`) to extract ring buffer pages into Common Trace Format (CTF) files [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].
- **Runtime Bridges**: Provides language agents for Python (`logging`), Java JUL, and Log4j 2 [^evt-wg-observability-and-traceability-file-75b688d43571-9301816c].

# References

- [Linux Kernel Tracing Comparison](../assessments/linux-kernel-tracing-comparison.md)
- [FTrace Reference Architecture](ftrace.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/02-kernel-tracing/lttng-ust.md
