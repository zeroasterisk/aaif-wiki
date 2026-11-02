---
type: skill
title: Issue Analysis
description: Modular agent skill standardizing first-pass GitHub issue triage, codebase
  grounding, and precedent retrieval across structured reference analyses.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
tags:
- agent-skills
- issue-triage
- reference-corpus
- flue
- context-grounding
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:48:11.568438+00:00'
sources:
- id: evt-submission-analyser-file-562ca4e251fc-8c9734e5
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
- id: evt-submission-analyser-file-b803fcb7f17e-c4652926
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/ci.yml
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
---

# Overview

The Issue Analysis skill (`issue-analysis`) is a modular agent skill executed within the [../resources/submission-analyser.md](../resources/submission-analyser.md) runtime to perform automated first-pass triage and deep technical assessment of GitHub issues [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. It grounds agent reasoning in project-specific historical precedents using an indexed reference corpus of past analyses [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

During execution, the skill balances broad issue interpretation against project conventions by loading relevant historical precedents into model context and preventing prompt injection vulnerabilities from unvetted issue text [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

# Architecture / Specification

### Reference Corpus and Precedent Matching

The skill incorporates an extensible reference directory (`src/skills/issue-analysis/references/`) containing validated hand-written historical assessments [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]:
- **Metadata Inspection**: The skill reads the YAML frontmatter of every file in the reference corpus without loading full bodies immediately [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. Frontmatter attributes include `issue-number`, `date`, `issue-type`, `severity`, `tags`, and `components` [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Relevance Retrieval**: The agent matches reporter keywords against `tags` and `components`, selecting the 3–5 most relevant documents to read in full into working context [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Synthetic vs. Real Baselines**: Synthetic examples (`example: true`) provide structural formatting baselines for unit testing and CI but are explicitly excluded from being cited as legal or operational precedent during actual triage [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

### Frontmatter Validation and Build Integration

Skill metadata and frontmatter constraints are strictly enforced at load time [^evt-submission-analyser-file-b803fcb7f17e-c4652926]:
- In Flue 2.0, skill loading via `flue run` serves as the primary validation gate, rejecting malformed frontmatter and exiting with code 1 before any model inference or tool dispatch occurs [^evt-submission-analyser-file-b803fcb7f17e-c4652926].
- Offline verification harnesses test skill mounting and execution paths with zero secrets using mock in-memory providers [^evt-submission-analyser-file-b803fcb7f17e-c4652926].

### Data Sanitization and Committing Rules

Because corpus entries are loaded into LLM prompts and quoted in published Google Docs and Discord alerts, contributors must audit candidate reference files prior to committing [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. The guidelines strictly prohibit committing customer names, internal infrastructure hostnames, credentials, unreleased roadmap commitments, or details under active security embargos [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

# References

- Harness and runtime environment: [../resources/submission-analyser.md](../resources/submission-analyser.md)
- Packaging specification: [../standards/agent-skills.md](../standards/agent-skills.md)

[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
[^evt-submission-analyser-file-b803fcb7f17e-c4652926]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/ci.yml
