---
type: resource
title: Falco
description: Reference architecture evaluating Falco runtime security detection across
  kernel syscall streams, container metadata, and audit events.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/falco.md
tags:
- security
- ebpf
- runtime-detection
- observability
- kubernetes
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:07.614488+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/falco.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
- id: evt-wg-observability-and-traceability-pr-34
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/34
  author: MatthewKhouzam
  last_modified: '2026-10-07T06:18:15+00:00'
---

# Overview

Falco is an open-source runtime threat detection engine that evaluates real-time Linux kernel syscall streams and audit logs against rule assertions to detect anomalous and malicious workload behavior.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4] While [sysdig](sysdig.md) is focused on recording, inspecting, and replaying full trace files, Falco acts as a detection engine and runtime policy enforcement point, generating prioritized alerts to outputs like Falcosidekick, standard out, and webhooks.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]

# Architecture / Specification

Falco operates by consuming kernel events, enriching them with operational metadata, and checking them against a declarative rule set:[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]

- **Kernel Event Ingestion**: Intercepts syscalls (`execve`, `open`, `connect`, `setuid`, `ptrace`) using modern eBPF CO-RE probes, legacy eBPF, or the `falco.ko` kernel module via per-CPU ring buffers.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]
- **State Enrichment (`libscap` / `libsinsp`)**: Translates raw syscall entries into enriched contexts incorporating container runtimes, Kubernetes pod and namespace attributes, and process execution genealogies.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]
- **Plugin Framework**: Extends detection beyond kernel syscalls to ingest structured audit feeds such as Kubernetes Audit Logs and cloud provider audit trails.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]
- **Rules Engine**: Compiles YAML-defined detection rules containing filter conditions, priorities, and formatted output schemas for real-time evaluation.[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]

[^evt-wg-observability-and-traceability-file-b5129046f665-3fb33cb4]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/falco.md
