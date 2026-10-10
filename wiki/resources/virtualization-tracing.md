---
type: resource
title: Virtualization and Hypervisor Tracing
description: Reference architecture analyzing hypervisor scheduling, stolen time timestamp
  distortion, and host-level KVM, Xen, and VFIO tracepoint observability.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/virtualization.md
tags:
- observability
- virtualization
- kvm
- hypervisor
- kernel
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:43.095337+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/virtualization.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview

Virtualization inserts a hypervisor scheduling layer between physical hardware and guest operating systems that fundamentally alters trace accuracy through vCPU preemption, stolen time, and virtualized timers [^evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1]. Because guest-side tools like [Linux perf](../resources/linux-perf.md) and [FTrace](../resources/ftrace.md) experience distorted durations during hypervisor preemption, host-level OS tracepoints are required to expose the scheduling decisions, VM exit/entry traps, and device passthrough operations otherwise invisible to the guest [^evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1].

# Architecture / Specification

Virtualization tracing operates across multiple host and guest boundaries [^evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1]:

- **Host-Side KVM Tracepoints**: Exposed under `events/kvm/` via tracefs, `perf kvm stat`, and `trace-cmd`, capturing VM exits (`kvm_exit`), page faults, I/O traps, and guest MMU updates.
- **Paravirtualized Guest Interfaces**: Includes `kvmclock`/`pvclock` for corrected timing and `steal_time` accounting (via MSR `0x4b564d03`) to measure preemption cycles.
- **VFIO and SR-IOV Device Passthrough**: Captures IOMMU page table mappings, unmappings, and I/O page faults (`amd_iommu` / `intel_iommu`), enabling unmediated, bare-metal-equivalent tracing for guest GPU workloads [^evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1].

[^evt-wg-observability-and-traceability-file-619fab4e6c1b-fae151e1]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/virtualization.md
