---
type: resource
title: LTTng-UST Userspace Tracing Reference Architecture
description: Reference architecture for LTTng-UST lock-free userspace tracing using
  compiled tracepoints and shared-memory ring buffers.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-ust.md
tags:
- observability
- tracing
- lttng
- userspace
- ctf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:21.864246+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-75b688d43571-9301816c
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-ust.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

LTTng-UST (Linux Trace Toolkit: next generation Userspace Tracer) provides high-throughput, low-overhead userspace tracing by compiling static tracepoints directly into application binaries and streaming events through shared-memory ring buffers without kernel context switches or locks on the fast path.[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), this reference architecture demonstrates how native C/C++ applications and higher-level runtimes (Python, Java JUL/Log4j) record structured binary events formatted according to the [Common Trace Format](common-trace-format.md).[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]

# Architecture / Specification

LTTng-UST operates within process memory and interacts with per-user or system session daemons without requiring root privileges:

- **Instrumentation Layer (`liblttng-ust`)**: Applications define tracepoint providers via C headers and link against `liblttng-ust` and Userspace RCU (`liburcu`). When disabled, tracepoints execute as single conditional branches. When enabled, probe functions write native binary payloads directly into per-process POSIX shared memory (`/dev/shm`).[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]
- **Session Coordination (`lttng-sessiond`)**: Coordinates registration of traced applications, manages session configurations, and orchestrates extraction.
- **Consumer Daemon (`lttng-consumerd`)**: Reads filled sub-buffers asynchronously and writes formatted CTF streams directly to persistent storage.
- **Language Bridges**: Runtimes such as Python leverage `lttng-ust-agent-python` to bind standard logging handlers directly to the LTTng userspace probe mechanism.[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]

[^evt-wg-observability-and-traceability-file-75b688d43571-9301816c]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/lttng-ust.md
