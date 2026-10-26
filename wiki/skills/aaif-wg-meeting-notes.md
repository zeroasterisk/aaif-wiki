---
type: skill
title: AAIF Working Group Meeting Notes Skill
description: Progressively disclosed agent skill converting working group LFX audio
  transcripts and AI summaries into standardized Markdown meeting notes.
resource: https://github.com/aaif/working-group-chairs/pull/2
tags:
- governance
- working-groups
- documentation
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:50:53.998977+00:00'
sources:
- id: evt-working-group-chairs-pr-2
  resource: https://github.com/aaif/working-group-chairs/pull/2
  author: awfrazer
  last_modified: '2026-10-07T07:34:57+00:00'
---

# Overview
The AAIF Working Group Meeting Notes skill (`aaif-wg-meeting-notes`) is an agent skill that converts raw meeting materials into standardized Markdown documentation for Agentic AI Foundation working groups[^evt-working-group-chairs-pr-2]. Originally adapted from operational prompts established in the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), the skill formats meeting transcripts, audio recordings, and AI summaries into clean consensus records[^evt-working-group-chairs-pr-2].

# Architecture / Specification
## Packaging and Invocation Structure
The skill uses progressive disclosure to minimize context overhead across general agent sessions[^evt-working-group-chairs-pr-2]:
- **Directory Structure**: Maintained within an isolated directory containing `SKILL.md` (agent instructions) and `template.md` (target output layout)[^evt-working-group-chairs-pr-2].
- **Agent Integration**: Deployed directly into an agent skills path (such as `~/.cursor/skills/` or `~/.claude/skills/`)[^evt-working-group-chairs-pr-2].
- **Explicit Activation**: Configured to load only when named explicitly in a user prompt, ensuring deterministic processing without passive context consumption[^evt-working-group-chairs-pr-2].

## Output Schema
The output format standardizes meeting records across all foundation working groups[^evt-working-group-chairs-pr-2]:
- **Topics Discussed**: Structured breakdown of agenda items and technical deliberations.
- **Decisions**: Explicit list of formal consensus points and technical determinations reached.
- **Deliverables**: Status tracking for specifications, whitepapers, and shared repositories.
- **Action Items**: Concrete operational tasks mapped to designated owners.
- **Artifact Hyperlinks**: References linking directly to LFX AI summaries, audio transcripts, and video recordings.

# Lifecycle History
Contributed via PR #2 in `aaif/working-group-chairs` to provide portable meeting documentation tooling across all working group chairs[^evt-working-group-chairs-pr-2].

[^evt-working-group-chairs-pr-2]: https://github.com/aaif/working-group-chairs/pull/2
