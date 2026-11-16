---
type: skill
title: AAIF Working Group Meeting Notes Generator
description: Progressively disclosed agent skill converting LFX meeting recordings,
  transcripts, and AI summaries into standardized working group meeting notes.
resource: https://github.com/aaif/working-group-chairs/pull/2
tags:
- skills
- working-groups
- governance
- meeting-notes
- documentation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:27:33.326011+00:00'
sources:
- id: evt-working-group-chairs-pr-2
  resource: https://github.com/aaif/working-group-chairs/pull/2
  author: awfrazer
  last_modified: '2026-10-07T07:34:57+00:00'
---

# Overview

The `aaif-wg-meeting-notes` skill provides an automated, standardized procedure for transforming raw meeting records—including meeting recordings, automated transcripts, and AI-generated summaries—into structured Markdown meeting notes for Agentic AI Foundation working groups [^evt-working-group-chairs-pr-2]. Originally developed as internal prompts within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the skill has been genericized across the foundation to ensure consistent archival and reporting practices [^evt-working-group-chairs-pr-2].

To prevent unnecessary context consumption, the skill adheres to a strict on-demand loading model and requires explicit naming during agent invocation [^evt-working-group-chairs-pr-2].

# Architecture / Specification

### Package Layout and Progressive Disclosure

The skill is packaged as an independent folder containing two required artifacts [^evt-working-group-chairs-pr-2]:
- `SKILL.md`: Runtime instructions directing the agent how to parse transcript timelines, reconcile conflicting topic summaries, and extract firm consensus items.
- `template.md`: Canonical output schema constraining the generated document structure.

The skill does not load into the agent context window by default; users must explicitly invoke it by name (for example, `Using the aaif-wg-meeting-notes skill, write the notes for the meeting`) [^evt-working-group-chairs-pr-2].

### Ingestion and Section Mapping

The agent processes three primary inputs: LFX or platform meeting recordings, full transcripts, and automated AI summaries. It maps these sources into five standardized document sections [^evt-working-group-chairs-pr-2]:
1. **Topics Discussed**: Core technical discussions and debate threads.
2. **Decisions**: Explicit determinations reached by attendee consensus or chair ruling.
3. **Deliverables**: In-flight specifications, whitepapers, or repository contributions.
4. **Action Items**: Assigned tasks with designated owners and target completion dates.
5. **Source Links**: Direct references linking back to the raw recording, full transcript, and source AI summary.

# Lifecycle History

- Proposed in `aaif/working-group-chairs` PR #2 as part of the shared agent skills initiative for foundation leadership, adapting prompts proven in the Security & Privacy WG [^evt-working-group-chairs-pr-2].

[^evt-working-group-chairs-pr-2]: https://github.com/aaif/working-group-chairs/pull/2
