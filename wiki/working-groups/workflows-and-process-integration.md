---
type: working-group
title: Workflows and Process Integration Working Group
description: Technical working group establishing shared agentic workflow execution
  models, reference architectures, and boundary control patterns.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
tags:
- working-group
- workflows
- architecture
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
  author: Yaron Schneider
  last_modified: '2026-11-05T08:38:51-08:00'
---

# Overview
The Workflows and Process Integration Working Group (WG Workflows & Process Integration) develops vendor-neutral execution models, reference architectures, workflow primitives, and boundary control patterns for agentic systems within the Agentic AI Foundation.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e] Co-chaired by Yaron Schneider (Diagrid) and Adam Seligman (Workato), the group defines reliable integration patterns uniting non-deterministic LLM behaviors with deterministic enterprise process controls.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# Architecture / Specification
The group's core activities span three workstreams:[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **Reference Architectures**: Authors foundational workflow patterns and composite architectures, notably the [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md) and [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md).[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **Critical Use Cases**: Curates real-world production agent implementations across industry verticals. In September 2026, the workstream adopted the designation "workflow shape" and "HITL shape" to distinguish empirical observations from prescriptive reference architecture patterns.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **Taxonomy Alignment**: Coordinates with the cross-WG taxonomy workstream to harmonize execution nomenclature, defining "activity" for workflow execution subunits and adopting "business task" as the overarching problem handled by a workflow.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# Lifecycle History
- **2026-08-29**: Core specification for Bounded Autonomous Remediation merged via PR #26.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **2026-09-17**: Single-Agent Process with Human Approval passed plenary vote unanimously, becoming the WG's second voted artifact.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **2026-09-22**: Critical Use Cases and Reference Architectures aligned to differentiate observational "shapes" from normative patterns.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# References
- [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md)
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)
- [Proposal/Execution Split](../patterns/proposal-execution-split.md)
- [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md)

[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
