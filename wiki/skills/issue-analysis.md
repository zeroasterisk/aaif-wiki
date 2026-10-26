---
type: skill
title: Issue Analysis Skill
description: Progressively disclosed agent skill providing structured issue review
  templates, rubric guidance, and prompt injection detection schemas for Flue runtimes.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
tags:
- aaif
- skill
- triage
- prompt-injection
- flue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:14:28.311731+00:00'
sources:
- id: evt-submission-analyser-file-a54ff182c7e8-7be29901
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
  author: Manik Surtani
  last_modified: '2026-08-20T13:34:39+10:00'
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
The Issue Analysis Skill packages reusable triage instructions, analytical rubrics, and formatting templates used by automated review agents such as `../resources/submission-analyser.md` [^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. Formatted under the Flue 2.0 skill standard, it enforces consistent evaluation of incoming GitHub issues against project context while maintaining context efficiency through progressive disclosure [^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# Architecture / Specification

## Progressive Disclosure Mechanics
Mounted via Flue's `useSkill()` hook, the skill presents a single catalog line in the initial system prompt to minimize upfront token consumption [^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. Full instructions from `SKILL.md` are only loaded into active model context when the runtime invokes `activate_skill` [^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. Supporting documents, such as output templates and historical review references, remain unread on disk until explicitly queried during analysis [^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

## Asset Structure and Reference Examples
The skill directory includes:
- `SKILL.md`: Core evaluation instructions governing triage criteria, tone, and step-by-step workflow [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- `template.md`: Standardized Markdown template formatting the final analytical output [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- `references/`: Corpus of reference analyses illustrating expected evaluations across bug reports, feature proposals, and security vulnerability reports [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

## Adversarial Manipulation Detection
In addition to technical classification fields, the skill schema mandates explicit reporting attributes for adversarial prompt injection [^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]:
- `injectionSuspected`: Boolean flag set to `true` whenever an issue payload attempts to override system instructions or invoke unauthorized capabilities [^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- `injectionNotes`: Explanatory narrative detailing the suspected manipulation pattern [^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

The agent records these indicators in the output report while proceeding to evaluate any remaining legitimate technical content [^evt-submission-analyser-file-a54ff182c7e8-7be29901].

[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
[^evt-submission-analyser-file-a54ff182c7e8-7be29901]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
