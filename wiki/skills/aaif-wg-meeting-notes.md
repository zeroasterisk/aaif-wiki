---
type: skill
title: AAIF Working Group Meeting Notes Generator
description: Modular agent skill and CLI toolkit converting working group LFX audio
  transcripts and AI summaries into standardized AAIF meeting minutes.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/63
tags:
- agent-skill
- meeting-notes
- automation
- lfx
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:11:30.472250+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-63
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/63
  author: 91pavan
  last_modified: '2026-10-13T09:37:59+00:00'
---

# Overview
The AAIF Working Group Meeting Notes Generator is an automated agent skill and command-line toolkit designed to convert raw meeting audio transcripts and LFX summaries into standardized, publication-ready working group meeting minutes[^evt-wg-observability-and-traceability-pr-63]. It enforces consistent synthesis across decisions, action items, and evidence citations across Agentic AI Foundation working groups[^evt-wg-observability-and-traceability-pr-63].

Operating in accordance with standards established in [Taxonomy Landscape Meeting Notes Guidelines](../guidelines/taxonomy-landscape-meeting-notes.md), the tool standardizes note formatting while ensuring that all generated minutes require human review prior to publication[^evt-wg-observability-and-traceability-pr-63].

# Architecture / Specification
The meeting notes generation workflow relies on a modular Python toolkit and date-driven CLI pipeline[^evt-wg-observability-and-traceability-pr-63]:

- **LFX MCP Integration**: Connects via Model Context Protocol (MCP) to Linux Foundation LFX APIs to retrieve official meeting audio transcripts and structured summaries[^evt-wg-observability-and-traceability-pr-63].
- **Transcript Synthesis & Fallback**: Correlates high-level LFX summaries with detailed timestamped transcripts, incorporating fallback handling when primary summaries or raw audio transcripts are incomplete[^evt-wg-observability-and-traceability-pr-63].
- **Structured Output Generation**: Generates Markdown meeting minutes structuring logged decisions, explicit action item ownership, and cited evidence[^evt-wg-observability-and-traceability-pr-63].
- **Cross-WG Parameterization**: Configurable across foundation groups via parameter overrides for project, committee, and meeting identifiers[^evt-wg-observability-and-traceability-pr-63].
- **Human Verification Gate**: Requires manual maintainer or working group chair review to verify decision accuracy and task assignments before notes are published[^evt-wg-observability-and-traceability-pr-63].

# Lifecycle History
Developed in the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the toolkit was implemented as a reusable Python module with plans to migrate the shared CLI logic into the foundation's centralized `working-groups-chair` tooling repository for broad WG adoption[^evt-wg-observability-and-traceability-pr-63].

[^evt-wg-observability-and-traceability-pr-63]: https://github.com/aaif/wg-observability-and-traceability/pull/63
