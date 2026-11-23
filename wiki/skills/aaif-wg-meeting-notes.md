---
type: skill
title: AAIF Working Group Meeting Notes Skill
description: Operational agent skill and CLI toolkit automating LFX transcript retrieval,
  structured decision synthesis, and meeting record publication.
resource: https://github.com/aaif/working-group-chairs/pull/3
tags:
- skills
- lfx
- governance
- meeting-notes
- mcp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:28:23.795944+00:00'
sources:
- id: evt-working-group-chairs-pr-3
  resource: https://github.com/aaif/working-group-chairs/pull/3
  author: 91pavan
  last_modified: '2026-10-19T16:57:39+00:00'
---

# Overview
The `aaif-wg-meeting-notes` skill provides an automated toolkit and agent workflow for retrieving, parsing, and summarizing AAIF working group meetings hosted on the Linux Foundation LFX platform.[^evt-working-group-chairs-pr-3] It extracts transcripts, structures agenda discussions, and synthesizes formal decision records in accordance with foundation reporting standards.[^evt-working-group-chairs-pr-3]

# Architecture / Specification
The toolkit comprises modular components designed for reproducible and secure execution:
- **LFX MCP Client:** Interfaces with the LFX platform over the Model Context Protocol using OAuth via `mcp-remote` or bearer token authentication, supporting tool discovery and result pagination.[^evt-working-group-chairs-pr-3]
- **Transcript Utilities:** Downloads and parses Zoom transcripts in WebVTT or plain-text formats, featuring an optional Playwright fallback for resilient retrieval.[^evt-working-group-chairs-pr-3]
- **Structured-Output Model Client:** Submits extracted dialogue through OpenAI-compatible endpoints enforcing strict JSON Schema completions for meeting agendas, action items, and formal consensus decisions.[^evt-working-group-chairs-pr-3]
- **Execution Safeguards:** Enforces date and URL validation, private no-overwrite local JSON export, and credential-safe error messaging to prevent token leakage in CI/CD logs.[^evt-working-group-chairs-pr-3]

# Lifecycle History
Developed across the working group chairs coordination repository, the toolkit evolved from custom scripts into a standardized package featuring pinned dependencies, unit tests, and multi-auth LFX clients.[^evt-working-group-chairs-pr-3]

[^evt-working-group-chairs-pr-3]: https://github.com/aaif/working-group-chairs/pull/3
