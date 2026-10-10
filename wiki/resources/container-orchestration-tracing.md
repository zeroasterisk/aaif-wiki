---
type: resource
title: Container Orchestration Tracing
description: Reference architecture evaluating container scheduling layers, cgroup
  CPU bandwidth throttling, and namespace tracepoints across orchestration platforms.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/orchestration.md
tags:
- tracing
- kubernetes
- containers
- cgroups
- ebpf
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:07.614488+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/orchestration.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
- id: evt-wg-observability-and-traceability-pr-34
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/34
  author: MatthewKhouzam
  last_modified: '2026-10-07T06:18:15+00:00'
---

# Overview

Container orchestration tracing analyzes the scheduling, resource isolation, and namespace boundaries introduced by Kubernetes, k3s, containerd, CRI-O, and Podman.[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331] Orchestration platforms introduce layers such as Completely Fair Scheduler (CFS) pre-emption, cgroup CPU bandwidth throttling, and namespace isolations that cause timing distortions in application-level traces without exposing internal causes.[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]

# Architecture / Specification

Container orchestration tracing bridges application tracing with low-level kernel observability tools like [ftrace](ftrace.md), [Linux perf](linux-perf.md), and [LTTng](lttng-kernel.md):[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]

- **Scheduler & CFS Throttling**: Monitors `sched:sched_switch` and `cgroup:cgroup_rstat_updated` / CFS bandwidth control tracepoints (`sched_cfs_throttle`, `sched_cfs_unthrottle`) to detect when CPU quotas pause container execution.[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]
- **Namespace & Lifecycle Boundaries**: Observes container runtime events (`tasks/create`, `tasks/start`, `tasks/exit`, `tasks/oom`) and namespace switches across PID, mount, and network namespaces.[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]
- **Control Plane & Runtime Observability**: Correlates `kube-apiserver` OpenTelemetry spans, `kubelet` CRI gRPC calls, and network flow observability tools (such as Cilium/Hubble and Inspektor Gadget) to provide end-to-end pod scheduling and communication visibility.[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]

[^evt-wg-observability-and-traceability-file-cb40ed13def2-473ff331]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/orchestration.md
