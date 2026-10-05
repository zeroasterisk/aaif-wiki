---
type: skill
title: AAIF Reference Architecture Agent Skill
description: Standardized agent skill for analyzing AI agent tools and frameworks
  to produce structured AAIF reference architectures and telemetry assessments.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
tags:
- skills
- observability
- reference-architectures
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:29:28.001865+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
  author: Matthew Khouzam
  last_modified: '2026-08-05T11:32:54+01:00'
---

# Overview
The `aaif-ref-arch` skill is an automated agent capability curated by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) to evaluate open-source AI agent tools, frameworks, and specifications[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]. It automates the generation of structured AAIF reference architecture documents and observability assessments.

# Architecture / Specification
The skill executes a standardized multi-step evaluation workflow[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]:
1. **Source Gathering**: Inspects target repositories, READMEs, architecture schemas, APIs, and reference implementations.
2. **Reference Architecture Production**: Generates structured markdown specifying project metadata, scope layer (primitive, orchestration, or system), prerequisites, ASCII architecture diagrams, and instrumentation mechanics.
3. **Telemetry & Cost Assessment**: Compiles sample trace outputs, cost profiles, validation criteria, and known operational limitations.
4. **Structured Commit**: Formats and stores the evaluation assessment for inclusion in AAIF knowledge repositories.

[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
