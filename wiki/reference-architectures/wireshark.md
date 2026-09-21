---
type: reference-architecture
title: Wireshark Reference Architecture
description: Reference architecture for Wireshark deep packet inspection, modular
  protocol dissection, and PCAPNG/JSON trace capture.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
tags:
- observability
- network
- packet-capture
- wireshark
- pcap
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Wireshark is an open-source network protocol analyzer and deep packet inspection framework providing packet capture, protocol dissection across over 3,000 protocols, and structured export capabilities [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1]. In the AAIF reference architecture taxonomy, it serves as the wire-level network tracing standard for cross-agent communication, RPC protocols, and infrastructure network inspection.

# Architecture / Specification

- **Privilege Separation**: Wireshark isolates capture operations in `dumpcap` (requiring `CAP_NET_RAW`) while running protocol parsing and UI components (Wireshark GUI / TShark CLI) with unprivileged user permissions to minimize attack surface [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].
- **Dissector Framework**: A modular engine mapping raw byte streams into layered protocol trees (Ethernet > IP > TCP/UDP > HTTP/gRPC/custom protocol), supporting TLS session key decryption via `SSLKEYLOGFILE`.
- **Storage and Export**: Captures standard PCAP/PCAPNG streams and provides structured export formats including JSON and PDML for automated analysis workflows.

[^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
