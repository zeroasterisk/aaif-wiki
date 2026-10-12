---
type: skill
title: AAIF Reference Architecture Generator Skill
description: Modular agent skill producing structured AAIF reference architectures
  and technology evaluation assessments for AI agent frameworks and specifications.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
tags:
- skill
- reference-architecture
- observability
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:47:31.904164+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
  author: Matthew Khouzam
  last_modified: '2026-08-05T11:32:54+01:00'
---

# Overview

The AAIF Reference Architecture skill (`aaif-ref-arch`) is a modular agent skill designed to analyze open-source AI agent tools, frameworks, and specifications to generate structured reference architectures and evaluation assessments [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]. It automates repository inspection, architecture decomposition across primitive, orchestration, and system layers, and telemetry tracing analysis.

# Architecture / Specification

The skill provides a deterministic 4-stage process [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]:
1. **Source Gathering**: Inspects repository READMEs, architectural blueprints, schemas, and reference implementations.
2. **Reference Architecture Generation**: Formats output documentation covering Zoom Level scope, prerequisites, ASCII architecture diagrams, instrumentation walkthroughs, sample trace outputs, cost profiles, validation criteria, and operational boundaries.
3. **Evaluation Assessment**: Produces structured maturity assessments against AAIF guidelines.
4. **Commit & Packaging**: Validates git cleanliness and aligns documentation with foundation standards [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

# Lifecycle History

Authored by Matthew Khouzam under MIT license in the Tracing Landscape repository under `tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md` [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
