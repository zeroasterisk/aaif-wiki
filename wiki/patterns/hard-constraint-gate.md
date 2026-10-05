---
type: pattern
title: Hard Constraint Gate
description: Human-in-the-loop pattern enforcing permanent, non-negotiable regulatory
  or policy accountability requirements that do not relax as agent reliability improves.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
tags:
- hitl
- governance
- compliance
- workflow-pattern
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:46:04.724106+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-42
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
  author: askulkarni2
  last_modified: '2026-09-24T01:00:06+00:00'
---

# Overview
The Hard Constraint Gate is a human-in-the-loop (HITL) workflow pattern where human execution or authorization is mandatory due to external regulatory, legal, or institutional policy requirements rather than agent capability limitations.[^evt-wg-workflows-and-process-integration-pr-42] Unlike confidence-driven checkpoints, hard constraint gates are structural invariants that remain permanent throughout the system lifecycle and are explicitly excluded from autonomy graduation.[^evt-wg-workflows-and-process-integration-pr-42]

# Architecture / Specification
In agentic workflows, oversight checkpoints historically collapsed two distinct failure modes into generic approval gates: temporary verification because the model is not yet sufficiently trusted, and permanent verification mandated by external accountability structures.[^evt-wg-workflows-and-process-integration-pr-42]

Hard constraint gates enforce non-negotiable boundaries, such as:
- Physician signatures and medical order approvals in clinical workflows.[^evt-wg-workflows-and-process-integration-pr-42]
- Licensed attorney certifications and statutory filings in legal systems.[^evt-wg-workflows-and-process-integration-pr-42]
- Fiduciary and board-level financial authorizations exceeding specified transaction thresholds.[^evt-wg-workflows-and-process-integration-pr-42]

The pattern operates alongside [Human Approval Gate](./human-approval-gate.md) and [Deterministic Acceptance Gate](./deterministic-acceptance-gate.md), but is formally decoupled from [Autonomy Graduation](./autonomy-graduation.md). While transitional approval gates relax into exception escalation as empirical trust increases, hard constraint gates cannot be bypassed or automated away regardless of model performance.[^evt-wg-workflows-and-process-integration-pr-42]

# Lifecycle History
Proposed within the Workflows and Process Integration Working Group to resolve classification ambiguities in human oversight schemas and distinguish capability-based gates from regulatory requirements.[^evt-wg-workflows-and-process-integration-pr-42]

[^evt-wg-workflows-and-process-integration-pr-42]: https://github.com/aaif/wg-workflows-and-process-integration/pull/42
