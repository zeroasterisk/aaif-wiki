---
type: skill
title: AAIF Working Group Meeting Notes Skill
description: Standardized agent skill restructuring raw meeting recordings, transcripts,
  and AI summaries into unified AAIF working group notes.
resource: https://github.com/aaif/working-group-chairs/pull/2
tags:
- skills
- working-groups
- governance
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:16:27.684579+00:00'
sources:
- id: evt-working-group-chairs-pr-2
  resource: https://github.com/aaif/working-group-chairs/pull/2
  author: awfrazer
  last_modified: '2026-10-07T07:34:57+00:00'
---

# Overview
The `aaif-wg-meeting-notes` skill provides a standardized workflow for AI agents to process raw meeting recordings, transcripts, and automated summaries into structured AAIF working group meeting records[^evt-working-group-chairs-pr-2]. Originally adapted from operational prompts in the Security and Privacy Working Group, the skill establishes consistent documentation standards across all Agentic AI Foundation working groups[^evt-working-group-chairs-pr-2].

# Architecture / Specification
The skill is packaged as an on-demand directory containing agent instructions (`SKILL.md`) and a target output format (`template.md`)[^evt-working-group-chairs-pr-2]. It is designed for explicit invocation within compliant agent runtimes (such as Claude Code or Cursor) by explicitly referencing the skill during a prompt session[^evt-working-group-chairs-pr-2].

### Processing Pipeline
1. **Intake Processing**: Ingests meeting AI summaries, full raw transcripts, and recording metadata[^evt-working-group-chairs-pr-2].
2. **Structural Extraction**: Identifies and extracts key discussion topics, formal decisions, deliverable updates, and assigned action items[^evt-working-group-chairs-pr-2].
3. **Artifact Linking**: Generates normalized references linking to the AI summary, raw transcript, and session recording[^evt-working-group-chairs-pr-2].
4. **Standard Output**: Renders markdown output conforming to the common AAIF working group meeting notes format[^evt-working-group-chairs-pr-2].

# Lifecycle History
- **PR #2 (working-group-chairs)**: Introduced shared agent skills genericized from Security and Privacy Working Group prompts for foundation-wide working group chair use[^evt-working-group-chairs-pr-2].

[^evt-working-group-chairs-pr-2]: https://github.com/aaif/working-group-chairs/pull/2
