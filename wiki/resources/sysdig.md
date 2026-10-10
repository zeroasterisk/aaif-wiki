---
type: resource
title: sysdig
description: Reference architecture for open-source sysdig capturing kernel syscalls,
  enriching container context, and replaying system traces.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/sysdig.md
tags:
- tracing
- ebpf
- kernel
- observability
- forensics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:07.614488+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/sysdig.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
- id: evt-wg-observability-and-traceability-pr-34
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/34
  author: MatthewKhouzam
  last_modified: '2026-10-07T06:18:15+00:00'
---

# Overview

sysdig is an open-source system-level tracing and forensics tool that captures the complete Linux kernel syscall stream via modern eBPF probes, legacy eBPF, or a kernel module.[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b] Operating as a system-wide tracer analogous to strace and tcpdump combined, sysdig records events into `.scap` capture files, performs interactive filtering, and executes Lua-based analysis scripts known as chisels.[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]

sysdig shares its core lower stack—including kernel drivers, the `libscap` capture engine, and the `libsinsp` state and metadata enrichment library—with its runtime security sibling, [Falco](falco.md).[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]

# Architecture / Specification

sysdig operates at the system layer by intercepting kernel syscall enter and exit events and sending them to userspace over per-CPU ring buffers:[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]

- **Kernel Probe Layer**: Modern eBPF CO-RE (Compile Once – Run Everywhere) probe requiring Linux kernel ≥ 5.8 with BPF ring buffers, or fallback legacy eBPF / kernel module (`scap.ko`).[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]
- **libscap**: Userspace library responsible for draining ring buffers, decoding raw syscall events, and reading or writing `.scap` format trace files.[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]
- **libsinsp**: State engine that reconstructs process trees, tracks open file descriptors, network connections, and enriches events with container (Docker, containerd, CRI-O) and Kubernetes (pod, namespace, labels) metadata.[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]
- **Inspection & Analysis Interfaces**: CLI (`sysdig`), ncurses interactive interface (`csysdig`), structured JSON export, and Lua analysis scripts (chisels) for computing top I/O consumers, network connections, and user activity.[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]

[^evt-wg-observability-and-traceability-file-8d913ff52178-e9043c6b]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/sysdig.md
