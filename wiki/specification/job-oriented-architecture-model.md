---
type: specification
title: Job-Oriented Architecture Model
description: A methodology organizing workflow reference architectures around recognizable
  practitioner jobs, structural boundaries, and explicit autonomy guarantees.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
tags:
- workflows
- reference-architecture
- principles
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:54:58.415816+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
  author: Mario Zagar
  last_modified: '2026-08-20T06:14:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-27
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/27
  author: mzagar
  last_modified: '2026-08-20T13:14:15+00:00'
---

# Overview
The Job-Oriented Architecture Model is a design methodology established by the Workflows and Process Integration Working Group that organizes reference architectures around recognizable practitioner jobs and required operational guarantees rather than agent counts or framework topologies [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181] [^evt-wg-workflows-and-process-integration-pr-27]. It provides foundational design guidance to structure workflow patterns, capability roles, and system boundaries across heterogeneous agent runtimes.

# Architecture / Specification
The methodology defines eight foundational architecture principles for composing workflow reference architectures and patterns [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]:

1. **Design around practitioner jobs, not agent count**: Architectures are named and structured around specific outcomes and operational arrangements (e.g., human-approved operation, bounded autonomous remediation). Agent topology is treated as an internal design choice.
2. **Prefer the smallest safe amount of autonomy**: Use deterministic workflow logic, explicit validation, and policy checks by default. Restrict probabilistic agent reasoning to interpretation and generation where rules are insufficient.
3. **Make authority and external effects explicit**: Clearly define which component or actor may propose results, decide acceptability, authorize effects, execute effects, and maintain execution state.
4. **Protect consequential effects structurally**: Prevent external side-effects from relying solely on model instruction compliance by enforcing structural boundaries such as human gates, constrained credentials, and isolated execution.
5. **Design for failure, recovery, and explicit outcomes**: Account for invalid inputs, failed checks, process restarts, retry limits, idempotency, and timeouts, explicitly enumerating terminal exit states.
6. **Compose reusable patterns without duplicating guarantees**: Reference constituent patterns (such as `../specification/human-approval-gate.md`) and document composition-level risks rather than duplicating individual pattern semantics.
7. **Keep requirements portable and implementation-neutral**: Use abstract capability roles (e.g., durable state store, constrained executor) rather than vendor-specific runtime bindings.
8. **Validate guidance against real scenarios**: Ground reference architectures in worked scenarios and validation records to identify gaps, variants, and domain boundaries.

# Lifecycle History
The architecture principles and contributor guidance were drafted within the reference architectures workstream and merged via PR#27 in the Workflows and Process Integration Working Group (`../working-groups/workflows-and-process-integration.md`) [^evt-wg-workflows-and-process-integration-pr-27].

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
[^evt-wg-workflows-and-process-integration-pr-27]: https://github.com/aaif/wg-workflows-and-process-integration/pull/27
