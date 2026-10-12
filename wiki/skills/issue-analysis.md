---
type: skill
title: Issue Analysis Skill
description: Modular Flue 2.0 skill providing automated GitHub issue analysis, reference
  corpus retrieval, and prompt injection reporting.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
tags:
- skill
- triage
- prompt-injection
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:51:26.918221+00:00'
sources:
- id: evt-submission-analyser-file-562ca4e251fc-8c9734e5
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
- id: evt-submission-analyser-file-a54ff182c7e8-7be29901
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
---

# Overview
The Issue Analysis skill is a modular capability package within Flue 2.0 that automates triage, technical risk assessment, and policy compliance verification for incoming GitHub issues [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. It executes inside the `submission-analyser` agent harness, extracting relevant architectural precedents from a local reference corpus to inform project-specific evaluations [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].

# Architecture / Specification
The skill implements structured data retrieval, prompt isolation, and telemetry reporting:

- **Reference Corpus Retrieval**: The skill maintains a library of historical hand-written analyses in a local directory [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. Each analysis defines frontmatter metadata including `issue-number`, `date`, `issue-type`, `severity`, `tags`, and `components` [^evt-submission-analyser-file-562ca4e251fc-8c9734e5]. The retrieval layer scans frontmatter across the corpus, dynamically selects the 3 to 5 most relevant reference cases using tag and component matching, and loads their full contents into context to guide decision making [^evt-submission-analyser-file-562ca4e251fc-8c9734e5].
- **Injection Isolation and Telemetry**: The skill enforces strict prompt containment by isolating untrusted input from system instructions [^evt-submission-analyser-file-a54ff182c7e8-7be29901]. When an issue body attempts prompt override or jailbreaking, the model is instructed to mark `injectionSuspected: true` and record the incident details in `injectionNotes` while continuing to evaluate any genuine technical elements [^evt-submission-analyser-file-a54ff182c7e8-7be29901].
- **Tool Invocation Contract**: The skill operates via a single consolidated tool invocation (`analyze_and_publish`), enforcing a read-only stance that forbids direct file writes, environment variable inspections, or outbound network calls outside configured publishing endpoints [^evt-submission-analyser-file-a54ff182c7e8-7be29901].

# References
- `../resources/submission-analyser.md`
- `../guidelines/agentic-ai-security-best-practices.md`

[^evt-submission-analyser-file-562ca4e251fc-8c9734e5]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/src/skills/issue-analysis/references/README.md
[^evt-submission-analyser-file-a54ff182c7e8-7be29901]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
