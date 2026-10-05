---
type: architecture
title: Common Trace Format (CTF)
description: Self-describing binary trace encoding format optimized for zero-copy
  write paths and nanosecond-precision event capture via embedded TSDL metadata.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
tags:
- observability
- tracing
- ctf
- binary-format
- metadata
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:32:50.363614+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Common Trace Format (CTF) specification defines a self-describing binary trace encoding optimized for zero-copy write paths, enabling trace producers to record high-frequency events at nanosecond precision with minimal compute overhead [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]. CTF operates as the wire and storage encoding layer beneath tracing infrastructure rather than a standalone runtime tool [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

CTF is produced by tracers such as [LTTng-UST](./lttng-ust.md) and barectf and consumed by diagnostic readers including Babeltrace2 and [Trace Compass](./trace-compass.md) [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# Architecture / Specification

A CTF trace is organized as a file system directory containing an embedded plain-text metadata stream written in Trace Stream Description Language (TSDL) alongside one or more binary event data streams [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]:
- **TSDL Metadata (`metadata`)**: Defines trace environment parameters, clock sources (frequencies, precisions), packet context layouts, and event field payload schemas [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].
- **Binary Data Streams (`channel*_*`)**: Native-endian, bit-packed event streams segmented into discrete packets with header contexts (timestamps, packet sizes, content sizes, packet sequence numbers, and dropped event counters) [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].
- **Zero-Copy Serialization**: Producers append raw binary structs directly to ring buffer allocations without intermediate text serialization or memory copies [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# Validation and Diagnostics

Trace validity is verified by inspecting packet magic headers (`0xc1fc1fc1`) and parsing stream contents against metadata using Babeltrace2 CLI utilities [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# References

- Working Group: [Observability and Traceability](../working-groups/observability-and-traceability.md)
- Related Architecture: [LTTng Userspace Tracing](./lttng-ust.md)
- Related Architecture: [Eclipse Trace Compass](./trace-compass.md)

[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/01-foundations/ctf.md
