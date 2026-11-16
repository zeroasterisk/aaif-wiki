---
type: guideline
title: Taxonomy and Landscape Meeting Notes Guideline
description: Standardized file-naming, structural requirements, table index maintenance,
  and editorial style rules for authoring Taxonomy and Landscape meeting notes.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
tags:
- guideline
- taxonomy
- meeting-notes
- operations
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T09:51:53.045436+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
  author: mindpower
  last_modified: '2026-06-27T21:46:55-07:00'
---

# Overview
The Taxonomy and Landscape Meeting Notes Guideline specifies the repository structure, ingestion procedure, editorial style, and index management rules for documenting meetings within the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) [^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]. It provides automated agents and human contributors with repeatable instructions for creating uniform records from call recordings, transcripts, and AI-generated summaries.

# Architecture / Specification

## File Naming and Location
Each meeting's notes must be authored in the `meeting-notes/` directory as `YYYY-MM-DD.md` using the exact date of the meeting (such as `2026-03-17.md`), initialized directly from `TEMPLATE.md` [^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

## Ingestion and Assembly Workflow
Contributors and automated document generation agents must follow an eight-step procedure [^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]:
1. Copy `TEMPLATE.md` into the new `YYYY-MM-DD.md` file.
2. Replace the `YYYY-MM-DD` placeholder in the title with the actual meeting date.
3. Populate the **Resources** section with links to the recording, transcript, and AI summary.
4. Detail the discussion points under **Topics Discussed**, keeping each item to 1–2 concise sentences.
5. Document any formal agreements under **Decisions**; if none occurred, write "None."
6. Document expected outputs under **Deliverables**; if none occurred, write "None."
7. Fill in the **Action Items** table with owner name, task description, and due date.
8. Add a new row to the table in `README.md` directly below the table header to maintain descending chronological order. The row must contain the meeting date, a markdown link labeled "Full notes" referencing the file, and a 1–2 sentence summary of key topics.

## Section Handling Rules
Sections that have no recorded activity must never be omitted or deleted. The section heading must remain intact with the content set to "None." to guarantee structural consistency across all repository notes [^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

## Editorial and Communication Style
All documentation, commit messages, pull request descriptions, and agent responses across the repository must comply with specific stylistic requirements [^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]:
- Format entries as concise bullet points rather than narrative paragraphs.
- Attribute action items to named individuals whenever possible.
- Do not use contrastive language.
- Do not insert horizontal rules for line breaks.
- Avoid sycophancy or deferential filler.
- Be direct while avoiding incomplete clauses or fragmented sentence structures.
- Maintain a neutral, professional tone that remains approachable and playful.

[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
