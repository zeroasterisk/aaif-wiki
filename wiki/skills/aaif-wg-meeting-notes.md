---
type: skill
title: AAIF Working Group Meeting Notes Generator
description: Progressively disclosed agent skill converting LFX meeting recordings,
  transcripts, and AI summaries into standardized, evidence-cited working group minutes.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/63
tags:
- skill
- tooling
- meeting-notes
- automation
- working-groups
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:25:30.692233+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-63
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/63
  author: 91pavan
  last_modified: '2026-10-13T09:37:59+00:00'
---

# Overview

The AAIF Working Group Meeting Notes Generator is an operational agent skill designed to ingest raw LFX meeting recordings, transcripts, and AI summaries to produce standardized working group minutes [^evt-wg-observability-and-traceability-pr-63]. The generator enforces consistent recording of decisions, action item ownership, and factual verification grounded in meeting evidence [^evt-wg-observability-and-traceability-pr-63].

Minutes generation follows the reporting standards defined in the [Taxonomy and Landscape Meeting Notes Guidelines](../guidelines/taxonomy-landscape-meeting-notes.md) while maintaining human editorial approval prior to pull request submission [^evt-wg-observability-and-traceability-pr-63].

# Architecture / Specification

## Toolkit and Integration Layer

The skill leverages a modular Python CLI and tool suite providing [^evt-wg-observability-and-traceability-pr-63]:

- **LFX MCP Integration**: Connectors interfacing with the Linux Foundation LFX Model Context Protocol endpoints to extract committee metadata, schedules, and raw audio transcripts [^evt-wg-observability-and-traceability-pr-63].
- **Transcript and Summary Synthesis**: Date-driven processing pipeline that cross-correlates automated LFX summaries against raw speech-to-text transcripts to verify claim accuracy [^evt-wg-observability-and-traceability-pr-63].
- **Evidence Grounding**: Heuristics ensuring action items and recorded consensus decisions cite corresponding timestamped evidence from meeting dialog [^evt-wg-observability-and-traceability-pr-63].
- **Credential Isolation and Portability**: Managed under `uv` virtual environments, designed to transition generic components to the shared `working-groups-chair` repository while preserving WG-specific meeting configurations locally [^evt-wg-observability-and-traceability-pr-63].

## Governance Invariants

Generated output is strictly advisory; human chair review is required before publishing minutes to GitHub repositories, ensuring automated summaries cannot misrepresent working group consensus [^evt-wg-observability-and-traceability-pr-63].

# Lifecycle History

- **2026-03**: Initial implementation proposed in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) PR #63 as a reusable cross-WG date-driven minutes tool [^evt-wg-observability-and-traceability-pr-63].

[^evt-wg-observability-and-traceability-pr-63]: https://github.com/aaif/wg-observability-and-traceability/pull/63
