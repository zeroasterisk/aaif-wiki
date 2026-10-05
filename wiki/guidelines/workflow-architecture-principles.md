---
type: guideline
title: Workflow Architecture Principles
description: Eight architectural design principles establishing practitioner job focus,
  minimal autonomy, structural protections, and implementation neutrality for AAIF
  workflow reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
tags:
- guidelines
- workflows
- reference-architectures
- system-design
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:01:27.309987+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
  author: Mario Zagar
  last_modified: '2026-08-20T06:14:14-07:00'
---

# Overview

The Workflow Architecture Principles provide shared design guidance for contributors and reviewers within the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) when composing patterns, capability roles, and boundaries into workflow reference architectures [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. Rather than prescribing specific vendors, frameworks, deployment topologies, or model providers, these principles define how concrete reference architectures must structure autonomy, authority, failures, and portability [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# Architecture / Specification

Reference architectures within the AAIF must align with eight foundational principles [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]:

1. **Design around practitioner jobs, not agent count**: Reference architectures describe recognizable practitioner jobs (such as human-approved operations or bounded autonomous remediation) and their required operational guarantees rather than classifying systems primarily by agent count [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. See also [Job-Oriented Architecture Model](../decisions/job-oriented-architecture-model.md).
2. **Prefer the smallest safe amount of autonomy**: Workflows prioritize deterministic logic, validation, and explicit policy checks, reserving model reasoning strictly for tasks where interpretation cannot be expressed as rules [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
3. **Make authority and external effects explicit**: Architectures explicitly define which entities propose results, decide acceptability, authorize external effects, execute effects, and own run state [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
4. **Protect consequential effects structurally**: Consequential external actions must not rely solely on model prompt compliance; they require enforceable boundaries such as [Human Approval Gates](../patterns/human-approval-gate.md), constrained credentials, controlled executors, and immutable evidence [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
5. **Design for failure, recovery, and explicit outcomes**: Architectures must account for invalid inputs, restart recovery, timeouts, duplicate events, budget exhaustion, and escalations, defining explicit terminal states and audit records [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
6. **Compose reusable patterns without duplicating guarantees**: Reusable patterns solve specific recurring problems; reference architectures compose them and focus on composition-level risks (e.g., stale approvals across durable waits) rather than re-specifying underlying pattern invariants [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
7. **Keep requirements portable and implementation-neutral**: Capabilities are expressed as logical roles (e.g., "durable state store", "constrained effect executor") before product choices [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
8. **Validate guidance against real scenarios**: Architectures must include worked scenarios and validation records to confirm real-world fitness [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# References

- [AAIF Workflows Working Group Principles Specification](https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md) [^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
