---
type: reference-architecture
title: Common Trace Format (CTF) Reference Architecture
description: Reference architecture for the Common Trace Format binary trace encoding
  optimized for zero-copy write paths and self-describing metadata.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
tags:
- observability
- ctf
- standards
- tracing
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:55:33.829608+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Common Trace Format (CTF) reference architecture documents the binary encoding and self-describing metadata standard used for high-throughput, low-overhead system and application tracing [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]. Maintained in the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape, CTF serves as the primary wire and storage format for tools like [LTTng Kernel Tracing](../reference-architectures/lttng-kernel-tracing.md) and [LTTng-UST](../reference-architectures/lttng-ust.md) [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

# Architecture / Specification

CTF separates trace layout descriptions from raw binary event streams [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]:

- **Trace Streams and Packets**: Binary trace files are organized into packetized streams containing packet headers, context, and sequential bit-packed event records written in native endianness [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].
- **TSDL Metadata**: A dedicated metadata stream written in Trace Stream Description Language (TSDL) defines the exact schema, types, clock frequencies, and layout of events, allowing generic decoders (`babeltrace2`, Trace Compass) to parse traces without pre-compiled schema dependencies [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].
- **Zero-Copy Performance**: Enables producers to emit high-frequency telemetry at nanosecond precision with minimal compute and storage overhead [^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf].

[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/01-foundations/ctf.md
