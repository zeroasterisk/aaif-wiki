---
type: skill
title: Issue Analysis
description: Maintainer-focused triage skill that evaluates incoming issues against
  historical reference analyses retrieved by component and tag metadata.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
tags:
- skill
- triage
- issue-analysis
- context-retrieval
- flue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:49:56.541571+00:00'
sources:
- id: evt-submission-analyser-file-562ca4e251fc-8c9734e5
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
- id: evt-submission-analyser-file-6ae19f00f4c0-5634c5c6
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/threat-model.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
---

# Overview
Issue Analysis is an automated agent skill executing structured triage, categorization, and severity evaluation on incoming issues filed against open-source repositories [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. Deployed via the [Submission Analyser](../resources/submission-analyser.md) runner, the skill combines project context retrieval with strict threat modeling to prevent untrusted issue text from executing prompt injection attacks or leaking credentials [^evt-submission-analyser-file-6ae19f00f4c0-5634c5c6].

# Architecture / Specification
The skill operates via standardized prompt evaluation and indexed reference retrieval [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]:

- **Reference Corpus Retrieval**: The skill scans a local corpus of historical handwritten analyses, reading YAML frontmatter to match incoming issue properties against `tags` and `components` fields. It selects the 3 to 5 most relevant past analyses to load in full [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Precedent Grounding**: Synthetic bootstrap examples carry `example: true` in their frontmatter, instructing the agent to exercise the retrieval pipeline without citing fabricated examples as factual precedent [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Auditing and Redaction Rules**: Because corpus conclusions are cited directly in published Google Docs and Discord announcements, corpus entries are audited to exclude customer names, internal hostnames, secrets, unannounced roadmap items, or private security embargoes [^evt-submission-analyser-file-562ca4e251fc-8c9734e5][^evt-submission-analyser-file-6ae19f00f4c0-5634c5c6].
- **Untrusted Input Handling**: Issue titles, descriptions, labels, author metadata, and comments are classified as untrusted input and evaluated without granting repository write privileges [^evt-submission-analyser-file-6ae19f00f4c0-5634c5c6].

# References
- Packaged and executed by [Submission Analyser](../resources/submission-analyser.md) [^evt-submission-analyser-file-6ae19f00f4c0-5634c5c6].
- Adheres to the [Agent Skills](../standards/agent-skills.md) specification.

[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
[^evt-submission-analyser-file-6ae19f00f4c0-5634c5c6]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/threat-model.md
