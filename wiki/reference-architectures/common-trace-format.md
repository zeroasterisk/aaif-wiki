---
type: reference-architecture
title: Common Trace Format (CTF)
description: Self-describing binary trace encoding specification optimized for native-endian
  bit-packed data serialization with embedded TSDL metadata.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
tags:
- observability
- tracing
- ctf
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T09:59:35.951599+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Common Trace Format (CTF) reference architecture defines a self-describing binary trace encoding designed for zero-copy write paths in high-throughput observability runtimes[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]. It allows event producers to record high-frequency events at nanosecond precision with minimal compute and I/O overhead.

CTF sits at the data format and wire encoding layer beneath tracing tools like [LTTng Kernel Tracing](lttng-kernel-tracing.md) and [LTTng UST](lttng-ust.md), separating binary data stream serialization from schema representation[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]. Trace analysis platforms such as [Eclipse Trace Compass](trace-compass.md) consume CTF files directly.

# Architecture / Specification

A standard CTF trace is organized as a directory containing an embedded Trace Software Description Language (TSDL) metadata stream alongside one or more binary data streams[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]:

- **TSDL Metadata (`metadata`)**: Defines trace environment, clock frequency, stream structures, and event field types.
- **Binary Packet Streams (`channel0_0`, `channel0_N`)**: Contains native-endian binary packets structured into packet headers, packet contexts, event headers, and variable-length event payload fields.
- **Zero-Copy Serialization**: Producers pack struct bitfields directly without intermediate parsing or conversion, allowing reader tools like `babeltrace2` to decode traces dynamically using the embedded schema[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
