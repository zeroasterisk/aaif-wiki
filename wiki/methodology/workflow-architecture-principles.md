---
type: methodology
title: Workflow Architecture Principles
description: Eight shared architectural principles guiding the composition of patterns,
  capability roles, and execution boundaries in agentic workflow reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
tags:
- workflows
- reference-architectures
- methodology
- design-principles
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:57:41.806372+00:00'
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

The Workflow Architecture Principles provide shared design guidance for contributors and reviewers within the Agentic AI Foundation when composing patterns, capability roles, and boundaries into workflow reference architectures [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. Rather than prescribing specific vendors, frameworks, or deployment topologies, these principles establish baseline requirements for safety, bounded autonomy, portability, and failure handling across agentic systems [^evt-wg-workflows-and-process-integration-pr-27].

Maintained by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), the principles inform the development of [Job-Oriented Reference Architectures](job-oriented-reference-architectures.md) and associated design patterns such as the [Human Approval Gate](../patterns/human-approval-gate.md) [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# Architecture / Specification

The eight architecture principles are [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]:

1. **Design around practitioner jobs, not agent count:** Name and structure architectures around operational jobs and operational guarantees (e.g., human-approved operation or bounded remediation) rather than arbitrary "single-agent" or "multi-agent" categorizations.
2. **Prefer the smallest safe amount of autonomy:** Use deterministic workflow logic, validation, and policy where reliable; restrict LLM reasoning to interpretation, judgment, or generation while keeping scope, admission, and external effects under workflow control.
3. **Make authority and external effects explicit:** Clearly differentiate who proposes results, decides acceptability, authorizes effects, executes effects, and owns run state.
4. **Protect consequential effects structurally:** Prevent consequential side effects from relying solely on agent instruction adherence by enforcing boundaries such as policy gates, scoped credentials, controlled executors, and recorded evidence.
5. **Design for failure, recovery, and explicit outcomes:** Define terminal failure states, recovery procedures, state persistence, timeouts, retries, and escalation paths.
6. **Compose reusable patterns; do not duplicate their guarantees:** Reference discrete patterns for recurring problems and focus reference architectures on composition-level risks and interactions.
7. **Keep requirements portable and implementation-neutral:** Define abstract capability roles (e.g., "durable state store", "constrained effect executor") before binding to specific software products or cloud engines.
8. **Validate guidance against real scenarios:** Include at least one worked scenario and validation record in each reference architecture to prove fit and identify missing patterns.

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/principles.md
[^evt-wg-workflows-and-process-integration-pr-27]: https://github.com/aaif/wg-workflows-and-process-integration/pull/27
