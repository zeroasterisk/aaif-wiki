---
type: resource
title: MPI and OpenMP Unified Tracing
description: Reference architecture for unified HPC tracing of MPI inter-process communication
  and OpenMP threading via PMPI, OMPT, and Score-P OTF2 binaries.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/mpi-openmp-tracing.md
tags:
- observability
- tracing
- hpc
- mpi
- openmp
- score-p
- otf2
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:21:10.371889+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/mpi-openmp-tracing.md
  author: Matthew Khouzam
  last_modified: '2026-10-07T07:18:15+01:00'
---

# Overview
MPI/OpenMP tracing provides standardized performance profiling across distributed high-performance computing (HPC) nodes and multi-threaded shared memory processes [^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711]. By combining PMPI interposition for message passing and OMPT callbacks for shared-memory parallelism, tools like Score-P unify instrumentation into Open Trace Format 2 (OTF2) binary streams and CUBE profile summaries [^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711].

# Architecture / Specification
The tracing architecture spans multiple layers of the parallel execution stack [^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711]:
- **PMPI Interposition**: Intercepts MPI calls (`MPI_Send`, `MPI_Recv`, `MPI_Allreduce`, `MPI_Barrier`) via link-time symbol wrapping to measure inter-process communication latencies and transfer volumes.
- **OMPT Callbacks**: Hooks into OpenMP runtime thread events (`ompt_callback_parallel_begin`, `ompt_callback_task_create`, `ompt_callback_work`) without requiring compiler source modifications.
- **Score-P Measurement Core**: Unifies PMPI and OMPT events into process-local lock-free memory buffers, correlating distributed timestamps across nodes.
- **OTF2 & CUBE Formats**: Persists event traces to disk in binary OTF2 format or aggregates performance metrics into CUBE hierarchy files for analysis in Scalasca and Vampir [^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711].

This architecture integrates into agentic infrastructure alongside GPU profiling systems such as [AMD ROCprofiler](../resources/amd-rocprofiler.md) and [NVIDIA Nsight](../resources/nvidia-nsight.md) as part of the broader [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape [^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711].

[^evt-wg-observability-and-traceability-file-0335a90fd535-bebc1711]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/03-hardware-accelerators/mpi-openmp-tracing.md
