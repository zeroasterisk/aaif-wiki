---
type: deliverable
title: Wireshark Reference Architecture
description: A reference architecture evaluating Wireshark and TShark network packet
  capture, dissector frameworks, and structured export capabilities.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
tags:
- observability
- networking
- tracing
- wireshark
- pcap
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

Wireshark is a packet inspection and network protocol analysis framework providing network wire capture through privilege-separated capture engines, layered protocol dissectors, and structured data export [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1]. It enables real-time network traffic observation and offline forensic analysis across distributed systems, multi-agent network boundaries, and hardware interfaces [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].

Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), Wireshark and its headless CLI `tshark` serve as network-layer telemetry producers that output PCAPNG and JSON streams, which can be correlated with system traces using tools such as the [Eclipse Trace Compass Reference Architecture](../deliverable/trace-compass-reference-architecture.md) [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].

# Architecture / Specification

Wireshark captures raw frames from network interfaces and kernel packet sockets via `libpcap`/`dumpcap`, processes them through a modular dissector pipeline supporting over 3000 protocols, and exposes decoded structures through graphical (Qt6) and programmatic interfaces [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1]:
- **Capture Engine (`dumpcap`)**: Minimal privilege-separated binary holding `CAP_NET_RAW` to stream raw frames directly to storage [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].
- **Dissection Engine (`libwireshark`)**: Iteratively decodes protocols across link, network, transport, and application layers, supporting optional TLS/Kerberos decryption keys [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].
- **Export Surface**: Provides structured outputs including PCAP, PCAPNG, PDML, and JSON via `tshark` [^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1].

[^evt-wg-observability-and-traceability-file-c562de5e6df9-6055ebe1]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/04-network/wireshark.md
