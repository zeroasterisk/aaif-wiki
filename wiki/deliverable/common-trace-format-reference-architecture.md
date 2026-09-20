---
type: deliverable
title: Common Trace Format (CTF) Reference Architecture
description: A reference architecture evaluating the Common Trace Format (CTF) binary
  trace encoding standard and TSDL schema metadata for zero-copy high-throughput tracing.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
tags:
- tracing
- ctf
- tsdl
- specification
- binary-format
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:52:21.390792+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Common Trace Format (CTF) reference architecture evaluates the CTF binary trace format specification (v1.8.3 and v2.0) designed for high-performance, zero-copy trace production [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]. CTF serves as the standard binary encoding layer beneath high-frequency tracers such as LTTng and barectf, separating data streams into self-describing binary packet channels and an embedded Trace Software Description Language (TSDL) metadata stream.

CTF is format-only and runtime-agnostic, enabling producers to write bit-packed native-endian binary records with nanosecond timestamps that external decoders such as `babeltrace2` can parse without prior compilation dependencies [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# Architecture / Specification

The CTF data model organizes trace streams into structured directory layouts [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]:

- **TSDL Metadata Stream**: A plaintext or packetized metadata description defining trace environment properties, clock configurations (frequency, precision), packet context schemas, and event field layouts.
- **Binary Stream Files**: Per-CPU or per-channel binary files consisting of contiguous packets. Each packet includes a packet header (starting with magic number `0xC1FC1FC1`), packet context (timestamps, packet sizes, dropped event counters), and sequentially packed binary events.
- **Zero-Copy Serialization**: Tracers serialize variable fields and integers directly into memory buffers without string serialization or runtime schema interpretation overhead.

CTF forms the underlying persistence format for both the [LTTng Kernel Tracing Reference Architecture](../deliverable/lttng-kernel-tracing-reference-architecture.md) and the [LTTng-UST Reference Architecture](../deliverable/lttng-ust-reference-architecture.md) [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# Lifecycle History

Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) as a core trace format reference deliverable [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
