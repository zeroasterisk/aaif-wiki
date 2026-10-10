---
type: resource
title: bpftrace
description: Reference architecture for bpftrace providing high-level dynamic kernel
  and userspace instrumentation via LLVM-compiled BPF bytecode.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/bpftrace.md
tags:
- tracing
- ebpf
- kernel
- dsl
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:07.614488+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/bpftrace.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
- id: evt-wg-observability-and-traceability-pr-34
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/34
  author: MatthewKhouzam
  last_modified: '2026-10-07T06:18:15+00:00'
---

# Overview

bpftrace is a high-level dynamic tracing language for Linux that compiles AWK-inspired scripts into BPF bytecode using LLVM.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191] It enables dynamic, safe instrumentation of kernel functions, userspace binaries, static tracepoints, and hardware performance counters with zero-copy in-kernel aggregation via BPF maps.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]

# Architecture / Specification

bpftrace sits above raw kernel BPF interfaces and [Linux perf](linux-perf.md) subsystems to provide an interactive query and instrumentation interface:[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]

- **Frontend Compilation Pipeline**: Uses Lexer/Parser (`flex`/`bison`) to construct an Abstract Syntax Tree (AST), performs type checking and map inference, resolves type layouts via BPF Type Format (BTF) without needing full kernel headers, and emits LLVM IR.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]
- **Verification & Execution**: JIT-compiles IR into BPF bytecode, submits programs to the kernel BPF verifier for safety guarantees, and attaches them to probes.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]
- **Probe Attach Points**: Supports `kprobe`/`kretprobe` (kernel dynamic tracing), `kfunc`/`kretfunc` (fentry/fexit BPF tracing), `uprobe`/`uretprobe` (userspace dynamic tracing), `tracepoint` (kernel static markers), `usdt` (userspace tracepoints), `profile`/`interval` (timer sampling), and hardware PMU counters.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]
- **Aggregation Engine**: Performs in-kernel map aggregations (`count()`, `sum()`, `hist()`, `lhist()`, `stats()`) to minimize user-kernel context switching overhead.[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]

[^evt-wg-observability-and-traceability-file-dc53a6dd724c-b96da191]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/02-kernel-tracing/bpftrace.md
