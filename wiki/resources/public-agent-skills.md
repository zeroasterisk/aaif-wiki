---
type: resource
title: Public Agent Skills
description: Repository of modular procedural agent skills, orchestrator workflows,
  and deterministic automation engines for community operations and governance.
resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-create-chapter/references/engine-internals.md
tags:
- skills
- tooling
- automation
- community-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:15:19.537183+00:00'
sources:
- id: evt-community-events-file-0dc3d95afe1f-91fcca49
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-create-chapter/references/engine-internals.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-133151709c55-f5700710
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-announcement-post/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-2a0ccd906b70-3a886c30
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-event-status/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-2ca2907cf349-5ea9efbb
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-audit-slack/references/engine-reports.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The Public Agent Skills repository provides a collection of modular, procedural agent skills, orchestrator workflows, and deterministic execution scripts designed for community operations, issue triage, repository synchronization, and asset generation across the Agentic AI Foundation.[^evt-community-events-file-133151709c55-f5700710][^evt-community-events-file-2a0ccd906b70-3a886c30] The skills enforce strict operational constraints, including privacy guardrails, identity matching, format-preserving document manipulation, and calibrated visual asset placement.[^evt-community-events-file-0dc3d95afe1f-91fcca49][^evt-community-events-file-2ca2907cf349-5ea9efbb]

# Architecture / Specification

### Operational Community Skills
- **`aaif-announcement-post`**: Generates LinkedIn launch and announcement posts when event RSVPs open, integrating with Luma and Gradual.AI.[^evt-community-events-file-133151709c55-f5700710] Enforces the *Public-Copy Rule*, forbidding agent outputs and conversational reasoning transcripts from echoing sensitive intake details (speaker emails, door codes, attendee contact information), and attaches mandatory LF Code of Conduct and Privacy Policy footers.[^evt-community-events-file-133151709c55-f5700710]
- **`aaif-event-status`**: Reads chapter and online series task health from `Event Tracker.docx` files using authenticated Google Workspace (`gws`) CLI integration.[^evt-community-events-file-2a0ccd906b70-3a886c30] Prohibits headless office suites (e.g., LibreOffice/`soffice`) to prevent font substitution and OOXML metadata corruption, preferring native Docs APIs and byte-level zip patching.[^evt-community-events-file-2a0ccd906b70-3a886c30]
- **`aaif-audit-slack`**: Validates chapter Slack workspaces, checking channel existence, organizer rosters, and membership alignments.[^evt-community-events-file-2ca2907cf349-5ea9efbb] Flags high-severity security anomalies such as publicly readable `-organizers` channels and supports `--planned-ok` flags during pre-provisioning lifecycle states.[^evt-community-events-file-2ca2907cf349-5ea9efbb]
- **`aaif-create-chapter`**: Automates chapter asset generation using paragraph-level text transformation and a mathematical Gall Stereographic map projection (`lon2x` linear in longitude, `lat2y` linear in `(1 + √2/2)·tan(lat/2)`) fitted to Natural Earth coastlines for precise map marker placement.[^evt-community-events-file-0dc3d95afe1f-91fcca49]

### Operational and Privacy Guardrails
1. **Public-Copy Redaction**: Prohibits emitting private intake data in draft copy or agent transcripts; private fields must only be referenced by name.[^evt-community-events-file-133151709c55-f5700710]
2. **Deterministic Precedence**: Source of truth is reconciled against central registers (e.g., Chapters List, Intake Ops) with strict precedence rules over heuristic matches.[^evt-community-events-file-2ca2907cf349-5ea9efbb]
3. **Format Integrity**: Restricts editing of cloud documents to native Google Workspace APIs and deterministic Python tooling to avoid formatting degradation.[^evt-community-events-file-2a0ccd906b70-3a886c30]

# References
- [Code of Conduct Policy](../policies/code-of-conduct.md)
- [Issue Analysis Skill](../skills/issue-analysis.md)
- [Taxonomy Contributions Skill](../skills/taxonomy-contributions.md)

[^evt-community-events-file-0dc3d95afe1f-91fcca49]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-create-chapter/references/engine-internals.md
[^evt-community-events-file-133151709c55-f5700710]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-announcement-post/SKILL.md
[^evt-community-events-file-2a0ccd906b70-3a886c30]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-event-status/SKILL.md
[^evt-community-events-file-2ca2907cf349-5ea9efbb]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-audit-slack/references/engine-reports.md
