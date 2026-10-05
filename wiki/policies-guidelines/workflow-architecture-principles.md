---
type: guideline
title: Workflow Architecture Principles
description: Eight core design principles for composing patterns, capability roles,
  and control boundaries into workflow reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
tags:
- architecture
- workflows
- patterns
- governance
- principles
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:35:21.675802+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
  author: Mario Zagar
  last_modified: '2026-08-20T06:14:14-07:00'
---

# Overview

The AAIF Workflow Architecture Principles guide contributors and reviewers in composing patterns, capability roles, and boundaries into agentic workflow reference architectures[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. Established by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), they serve as shared, vendor-neutral design guidance rather than prescriptive runtime or topology constraints[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# Architecture / Specification

The specification defines eight foundational design principles[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]:

1. **Design around practitioner jobs, not agent count**: Name and organize architectures around recognizable practitioner jobs (e.g., human-approved operation, bounded autonomous remediation) rather than arbitrary agent counts or topologies[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. See also [Job-Oriented Architecture Model](../decisions/job-oriented-architecture-model.md).
2. **Prefer the smallest safe amount of autonomy**: Maximize deterministic workflow logic, rules, and policy checks for admission and effect control; restrict agent model reasoning to open-ended interpretation or candidate generation[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
3. **Make authority and external effects explicit**: Clearly define distinct roles for proposing results, validating acceptability, authorizing actions, executing effects, and holding run state[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
4. **Protect consequential effects structurally**: Ensure critical external mutations do not rely purely on agent instruction following. Enforce boundaries via human gates, policy engines, constrained executors, and idempotent reconciliation[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]. See [Human Approval Gate](../patterns/human-approval-gate.md).
5. **Design for failure, recovery, and explicit outcomes**: Systematically handle invalid inputs, failed checks, restarts, duplicates, timeouts, budget exhaustion, and escalations, explicitly recording terminal states[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
6. **Compose reusable patterns; do not duplicate their guarantees**: Reference established patterns for recurring problems and address only composition-level risks and boundary interactions[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
7. **Keep requirements portable and implementation-neutral**: Use logical capability roles (e.g., "durable state store", "constrained effect executor") rather than specific vendor runtimes or hosting providers[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].
8. **Validate guidance against real scenarios**: Ground reference architectures in worked scenarios and validation records to confirm job fit and uncover missing pattern invariants[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

# Lifecycle History

- **2026**: Merged into `wg-workflows-and-process-integration` repository under `workstreams/reference-architectures/principles.md`[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181].

[^evt-wg-workflows-and-process-integration-file-9dabf9708248-88f92181]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/principles.md
