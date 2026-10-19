---
type: guideline
title: Taxonomy and Landscape Meeting Notes Agent Instructions
description: Operational instructions and communication standards governing automated
  agent meeting notes generation and repository contributions in the Taxonomy and
  Landscape workstream.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
tags:
- guidelines
- taxonomy-and-landscape
- meeting-notes
- agents
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T09:56:38.080269+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
  author: mindpower
  last_modified: '2026-06-27T21:46:55-07:00'
---

# Overview

The Taxonomy and Landscape workstream maintains standardized instructions for automated agents and contributors generating meeting notes and submitting repository text[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]. Managed within the workstream's meeting documentation, these rules govern file naming conventions, template processing workflows, empty section retention, and conversational tone across all repository activities in coordination with the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md)[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

# Architecture / Specification

### File Naming and Workflow

Notes are generated from `TEMPLATE.md` and saved using the date pattern `YYYY-MM-DD.md`[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]. The agent generation sequence requires eight discrete steps:
1. Copy `TEMPLATE.md` to a new date-stamped file[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
2. Update the document heading date[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
3. Populate the Resources section with links to AI summaries, transcripts, and recordings[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
4. Detail the subjects covered under Topics Discussed[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
5. Document formal decisions or mark "None." if none occurred[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
6. Record expected outputs under Deliverables or mark "None." if none occurred[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
7. Construct the Action Items table with owner attribution, descriptions, and due dates[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
8. Insert a row at the top of the `README.md` table beneath the header to preserve reverse chronological order, including a link to the full notes and a 1–2 sentence topic summary[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

### Editorial Constraints

Documentation must adhere to concise bullet points rather than narrative paragraphs, limit topic descriptions to 1–2 sentences, and explicitly attribute action items to individuals[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]. Empty sections must retain their heading and state "None." to ensure consistent document schemas across meetings[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

### Repository Communication Style

Agents and contributors interacting with the repository—including documentation drafting, commit messages, pull request summaries, and issue responses—must adhere to strict style guidelines[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]:
- Avoid contrastive language[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
- Avoid using horizontal rules for visual line breaks[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
- Eliminate sycophantic framing[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
- Maintain directness without relying on partial clauses[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
- Formulate complete thoughts that flow naturally[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].
- Maintain a neutral voice balancing playful tone with professional conduct[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea].

These automated interaction standards complement the schema routing provided by the [Taxonomy Contributions Skill](../skills/taxonomy-contributions.md).

[^evt-ws-taxonomy-landscape-file-eb9c68e792e7-e45bd7ea]: https://github.com/aaif/ws-taxonomy-landscape/blob/6ac90f517a064054d4113b3331c8c06e380258b8/meeting-notes/AGENTS.md
