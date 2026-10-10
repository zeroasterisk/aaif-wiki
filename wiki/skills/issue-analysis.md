---
type: skill
title: Issue Analysis Skill
description: Modular agent skill providing structured GitHub issue triage, rubric
  evaluation, and report drafting without repository write access.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
tags:
- skills
- issue-triage
- flue
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:57:51.428767+00:00'
sources:
- id: evt-submission-analyser-file-3dc5dd454e08-fa24a9ec
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
- id: evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
---

# Overview
The Issue Analysis Skill provides a standardized prompt, rubric, and template package for automated agent evaluation of newly opened GitHub issues and project submissions[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. Designed for execution within the Flue 2.0 runtime, the skill isolates analysis templates and reference examples to maintain deterministic evaluations across diverse submissions[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# Architecture / Specification
The skill implements progressive context disclosure through Flue's `useSkill()` pattern[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]:
- **Catalog Entry**: Mounts a single catalog line in the model's system prompt to minimize idle context token consumption[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec].
- **Activation**: Full instructions and schema constraints are injected only upon the model invoking `activate_skill`[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec].
- **Reference Retrieval**: Supporting review references (including synthetic bug, feature request, and security reviews) remain unread on disk until explicitly referenced[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- **Security and Injection Handling**: Schema definitions require explicit `injectionSuspected` flags and diagnostic notes rather than failing silently when adversarial prompts are detected in untrusted issue bodies[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# References
- [Submission Analyser](../resources/submission-analyser.md)

[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
