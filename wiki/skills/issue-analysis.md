---
type: skill
title: Issue Analysis Skill
description: Agent skill executing read-only first-pass triage on GitHub issues using
  dynamic frontmatter matching against a curated historical reference corpus.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
tags:
- skill
- triage
- github
- issue-analysis
- reference-corpus
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:13:09.843168+00:00'
sources:
- id: evt-submission-analyser-file-562ca4e251fc-8c9734e5
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
---

# Overview

The Issue Analysis skill executes read-only first-pass triage on incoming repository issues by retrieving project-specific historical precedents and producing structured severity evaluations[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. It operates inside automated CI triage harnesses such as the [submission-analyser](../resources/submission-analyser.md) agent.

# Architecture / Specification

### Reference Corpus Retrieval

To align judgements with specific repository conventions, the skill utilizes a local reference corpus of historical analyses[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]:
- **Frontmatter Indexing**: Scans metadata headers (`issue-number`, `date`, `issue-type`, `severity`, `tags`, `components`) across reference files[^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Precedent Matching**: Matches tags and component paths against the issue under analysis to retrieve the 3–5 most relevant historical precedents into context[^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Synthetic Precedent Guardrails**: Marks synthetic fixtures with `example: true` frontmatter, instructing the agent to never cite synthetic files as authoritative precedent[^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Pre-commit Redaction Controls**: Imposes mandatory audit checks before committing reference analyses, preventing exposure of credentials, customer data, internal hostnames, or embargoed security details[^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

# Lifecycle History

Packaged in the `aaif/submission-analyser` repository as an operational triage skill conforming to AAIF skill packaging guidelines[^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
