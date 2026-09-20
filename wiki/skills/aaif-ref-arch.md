---
type: skill
title: AAIF Reference Architecture Skill
description: An agent skill for generating standardized reference architecture assessments
  and telemetry walkthroughs for AI agent technologies.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
tags:
- skill
- observability
- reference-architecture
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:48:01.743574+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
  author: Matthew Khouzam
  last_modified: '2026-08-05T11:32:54+01:00'
- id: evt-wg-observability-and-traceability-pr-22
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/22
  author: MatthewKhouzam
  last_modified: '2026-08-05T10:32:55+00:00'
---

# Overview
The AAIF Reference Architecture Skill (`aaif-ref-arch`) is an [Agent Skill](../specification/agent-skill.md) maintained within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) designed to produce standardized architecture evaluations for open-source AI agent tools, frameworks, and specifications.[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b][^evt-wg-observability-and-traceability-pr-22]

# Architecture / Specification
The skill automates a structured evaluation workflow:
- **Source Material Ingestion**: Analyzes target repository documentation, data models, schema definitions, APIs, runtime behavior, and reference implementations.[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]
- **Assessment Generation**: Produces a standardized markdown assessment covering objective, zoom level (primitive, orchestration, or system layer), pinned prerequisites, component architecture diagrams, telemetry instrumentation walkthroughs, sample trace outputs, cost profiles, and validation criteria.[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]
- **Runtime Requirements**: Configured for the `kiro` runtime and requires internet access for git and GitHub repository content retrieval.[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]

# Lifecycle History
- **PR #22**: Merged initial `aaif-ref-arch` skill definition under the tracing landscape project to support technology investigation workflows.[^evt-wg-observability-and-traceability-pr-22]

# References
- Specification: [Agent Skill](../specification/agent-skill.md)
- Working Group: [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
[^evt-wg-observability-and-traceability-pr-22]: https://github.com/aaif/wg-observability-and-traceability/pull/22
