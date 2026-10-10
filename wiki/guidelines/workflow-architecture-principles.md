---
type: guideline
title: Workflow Architecture Principles
description: Eight core design principles governing the composition of capability
  roles, boundary controls, and patterns in AAIF workflow reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
tags:
- workflows
- architecture
- design-principles
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:58:15.666127+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
  author: Mario Zagar
  last_modified: '2026-08-20T06:14:14-07:00'
---

# Overview

The Workflow Architecture Principles provide shared design guidance for composing patterns, capability roles, and boundary controls into vendor-neutral reference architectures within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. Rather than prescribing specific model providers, cloud hosts, or agent frameworks, the principles establish enforceable boundaries and structural guarantees for AI-assisted business processes.

# Architecture / Specification

The framework defines eight core design principles[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]:

1. **Design around practitioner jobs, not agent count**: Name architectures by the operational job and guarantees required (e.g., human-approved operation, bounded autonomous remediation) rather than agent topology.
2. **Prefer the smallest safe amount of autonomy**: Retain deterministic workflow control over admission, scope limits, policy checks, external effects, and terminal outcomes, restricting model reasoning to non-deterministic interpretation or generation.
3. **Make authority and external effects explicit**: Clearly separate proposal generation, evaluation, authorization, execution, and state ownership roles.
4. **Protect consequential effects structurally**: Prevent agents from directly executing high-impact side effects by enforcing policy gates, constrained credentials, or patterns such as the [Human Approval Gate](../patterns/human-approval-gate.md).
5. **Design for failure, recovery, and explicit outcomes**: Define explicit terminal outcomes, retry behavior, reconciliation paths, timeouts, and state preservation for non-happy path conditions.
6. **Compose reusable patterns; do not duplicate their guarantees**: Reference established patterns and focus architecture documentation on composition-level integration risks.
7. **Keep requirements portable and implementation-neutral**: Specify abstract capability roles (e.g., durable state store, constrained executor) before product choices.
8. **Validate guidance against real scenarios**: Ground reference architectures in worked real-world scenarios and validation records.

# References

- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)
- [Human Approval Gate Pattern](../patterns/human-approval-gate.md)

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
