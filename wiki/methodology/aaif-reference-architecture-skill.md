---
type: methodology
title: AAIF Reference Architecture Skill
description: A structured process and tool used by the AAIF Observability and Traceability
  WG to generate reference architecture assessments for AI/agent technologies.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
tags:
- assessment
- tool
- observability
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T09:50:31.546742+00:00'
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
The AAIF Reference Architecture Skill (`aaif-ref-arch`) is a defined process and associated tool used primarily by the Observability and Traceability Working Group to produce structured reference architecture documents and evaluation assessments for AI agent technologies, frameworks, and specifications [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

The skill is designed to analyze open-source AI agent tools, frameworks, or specifications and provide a standardized assessment of their architecture, instrumentation, and telemetry capabilities [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

# Architecture / Specification
The process involves four main steps:
1. **Gather Source Material:** Fetching documentation, architecture docs, and schema definitions to identify core components, data models, APIs, and runtime behavior.
2. **Produce Reference Architecture Document:** Generating a structured Markdown file detailing the technology.
3. **Produce Evaluation Assessment:** (Details truncated in source, but listed as a step).
4. **Commit:** Committing the resulting documents.

The Reference Architecture Document structure requires specific sections, including:
*   **Objective** and **Scope / Zoom Level** (e.g., primitive layer, orchestration layer, or system layer).
*   **Prerequisites** (pinned versions of components).
*   **Architecture Diagram** (ASCII diagram showing components, data flows, and telemetry emission points).
*   **Instrumentation Walkthrough** (what is captured and the mechanism used).
*   **Sample Trace Output**.
*   **Cost Profile**.
*   **Validation Criteria**.
*   **Limitations / Out of Scope** [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

The skill requires internet access and git CLI, and is compatible with runtimes such as `kiro` [^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b].

[^evt-wg-observability-and-traceability-file-1cf101000b0c-bfd60e7b]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/.agents/skills/aaif-ref-arch/SKILL.md
