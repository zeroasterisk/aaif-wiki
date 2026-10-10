---
type: resource
title: Common Trace Format (CTF) Reference Architecture
description: Reference architecture for the Common Trace Format (CTF) binary specification,
  TSDL metadata syntax, and zero-copy packet layout.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/ctf.md
tags:
- observability
- tracing
- ctf
- standards
- binary-format
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:21.864246+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/ctf.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

The Common Trace Format (CTF) is an open, self-describing binary trace format optimized for zero-copy write paths in high-throughput tracing systems such as [LTTng-UST](lttng-ust.md), [LTTng Kernel Tracing](lttng-kernel.md), and barectf.[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]

CTF separates trace metadata from binary stream payloads. By embedding a Trace Software Description Language (TSDL) schema, decoders such as `babeltrace2` dynamically reconstruct packet layouts, native-endian bit-packed structures, and nanosecond timestamps without external compilation or schema registries.[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]

# Architecture / Specification

A CTF trace is stored as a directory containing metadata and binary data streams:

- **Metadata Stream (`metadata`)**: Plain text or packetized TSDL defining trace UUIDs, clock frequencies (e.g. 1 GHz monotonic), stream descriptions, packet contexts, and typed event layouts (fields, integers, floating points, compound structures).[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]
- **Data Streams (`channel_*`)**: Binary channels broken into independent packets. Each packet begins with a magic header (`0xC1FC1FC1`), stream ID, packet size, content size, and CPU/stream context registers followed by packed binary events.[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]
- **Zero-Copy Serialization**: Trace producers write native struct layouts directly into ring buffers with no intermediate JSON/string formatting overhead.[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]

[^evt-wg-observability-and-traceability-file-794378d347ca-5370ccaf]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/01-foundations/ctf.md
