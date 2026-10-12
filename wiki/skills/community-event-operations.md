---
type: skill
title: Community Event Operations Skill Suite
description: Modular agent skill suite managing community chapters, event scheduling,
  automated Slack workspace audits, and social copy generation across Google Workspace
  and external platforms.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
tags:
- skills
- community
- operations
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:50:35.583468+00:00'
sources:
- id: evt-community-events-file-4c2672b57ca1-5e9465e1
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-52894c310bd9-02d85f04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-8b30d97e0275-3e6d8b8d
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/references/caches-and-composition.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-91886a9e0653-84165b73
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-953dd2e86174-aa074a1c
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The Community Event Operations skill suite is a collection of modular agent skills that automate administrative, auditing, and publishing workflows for Agentic AI Foundation chapters and online series[^evt-community-events-file-953dd2e86174-aa074a1c]. Designed for cross-client portability across runtimes such as [Goose](../resources/goose.md), Claude Desktop, Claude Code, and Cursor, the toolkit pairs local deterministic Python automation with Google Workspace CLI (`gws`), Slack APIs, and external event platforms[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

The skill suite operates under strict boundary constraints: content and audit engines are read-only or staged locally, and state-modifying actions—such as creating live Luma events or publishing external copy—require explicit human confirmation[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-91886a9e0653-84165b73]. Conformance and evaluation mechanisms for these operational skills are benchmarked by the [Community Events Evaluation Suite](../resources/community-events-eval-suite.md)[^evt-community-events-file-953dd2e86174-aa074a1c].

# Architecture / Specification

## Core Skill Modules

- **Event Creation (`aaif-create-event`)**: Clones standardized event sections within chapter or series `Event Tracker.docx` documents, programmatically back-calculating due dates for operational milestones relative to the scheduled event date[^evt-community-events-file-4c2672b57ca1-5e9465e1]. Can push drafted details to Luma via API, but strictly gates live creation on prior human approval aligned with the [Human Approval Gate](../patterns/human-approval-gate.md) pattern[^evt-community-events-file-4c2672b57ca1-5e9465e1].
- **Social Carousel Copy (`aaif-carousel-copy`)**: Generates structured 6-slide LinkedIn carousels based on official presentation templates, adhering to builder-focused house tone guidelines (Slide 1 hook, Slide 6 call-to-action)[^evt-community-events-file-52894c310bd9-02d85f04]. Enforces strict redactive rules prohibiting the leakage or repetition of private contact details in drafts or conversational reasoning[^evt-community-events-file-52894c310bd9-02d85f04].
- **Slack Workspace Audit (`aaif-audit-slack`)**: Independent read-only auditing layer dividing checks into three engines (Organizers, Topics, and Members) and a shared measurement layer (`audit_activity.py`)[^evt-community-events-file-91886a9e0653-84165b73]. Results are compiled into a unified HTML dashboard (`summarize_audits.py`) without modifying workspace channels or rosters[^evt-community-events-file-8b30d97e0275-3e6d8b8d][^evt-community-events-file-91886a9e0653-84165b73].

## Tooling Rules & Document Rendering

All interactions with Drive files are restricted to Python scripts driving the `gws` CLI[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-52894c310bd9-02d85f04]. Native Google Workspace document formats (`application/vnd.google-apps.*`) must be edited via native APIs, while legacy Office files (`.docx`, `.pptx`, `.xlsx`) undergo direct byte-level OOXML edits[^evt-community-events-file-4c2672b57ca1-5e9465e1]. Headless suites such as LibreOffice (`soffice`) and `unoconv` are strictly prohibited to avoid font substitution and OOXML degradation; document previews are rendered by converting temporary copies to PDF via the Google Drive export API[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-52894c310bd9-02d85f04].

## Data Hygiene & Untrusted Input

- **Untrusted Input Invariants**: Member profiles, channel topics, message payloads, and CRM sheet cells are strictly classified as untrusted external data rather than agent instructions[^evt-community-events-file-91886a9e0653-84165b73][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Text attempting to grant administrative roles or force channel membership changes is flagged to the operator and ignored by execution engines[^evt-community-events-file-91886a9e0653-84165b73].
- **Repository Privacy Controls**: Audit caches and reports are generated with restrictive permissions (`0600` inside `0700` directories) and engines refuse to execute unless output paths are verifiably safe from `git add -A` commits[^evt-community-events-file-8b30d97e0275-3e6d8b8d][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. In installed plugin contexts, persistent state is mapped away from working directories to standard OS data directories per [Agent Plugin Portability](../guidelines/agent-plugin-portability.md)[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

[^evt-community-events-file-4c2672b57ca1-5e9465e1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
[^evt-community-events-file-52894c310bd9-02d85f04]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
[^evt-community-events-file-8b30d97e0275-3e6d8b8d]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/references/caches-and-composition.md
[^evt-community-events-file-91886a9e0653-84165b73]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/SKILL.md
[^evt-community-events-file-953dd2e86174-aa074a1c]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
