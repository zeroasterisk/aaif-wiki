---
type: skill
title: Issue Analysis Skill
description: Progressively disclosed Flue 2.0 agent skill structuring GitHub issue
  evaluation, reference comparison, output schema enforcement, and prompt injection
  detection.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
tags:
- aaif
- flue
- skill
- triage
- prompt-injection
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:48:32.935649+00:00'
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
The Issue Analysis Skill (`src/skills/issue-analysis`) is a modular, progressively disclosed agent capability within [Submission Analyser](../resources/submission-analyser.md) designed to perform first-pass technical assessments of GitHub issues[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]. Mounted explicitly in the Flue 2.0 runtime via `useSkill()`, the skill provides evaluation instructions, standardized report templates, and synthetic reference benchmarks while minimizing prompt token overhead[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# Architecture / Specification

## Progressive Disclosure Mechanics
The skill conforms to the progressive disclosure model of Flue 2.0 and [Agent Skills](../standards/agent-skills.md)[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]:
- **System Prompt Footprint:** Each mounted skill introduces only a single catalog entry line in the initial system prompt[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec].
- **Deferred Loading:** Comprehensive guidance contained in `SKILL.md` is loaded into context only when the language model invokes `activate_skill`[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. Supporting files—including output templates (`template.md`) and historical reference reviews (`references/`)—remain unloaded until explicitly requested, avoiding token consumption for unconsulted materials[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

## Schema and Injection Reporting
The skill defines an explicit output schema for issue evaluations that includes explicit fields for adversarial manipulation detection[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]:
- **`injectionSuspected`:** Boolean flag toggled when prompt injection, persona hijacking, or unauthorized instruction overrides are detected in untrusted issue text[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- **`injectionNotes`:** Explanatory field documenting the nature, vector, and content of detected manipulation attempts, transforming security events into actionable maintainer telemetry[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- **Substantive Triage Output:** Structured fields evaluating repository component boundaries, technical merit, dependencies, and alignment with working group standards[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

## Orchestration Tooling
The skill is paired with the `analyze_and_publish` harness tool in `src/tools/analyze-and-publish.ts`[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]. When invoked by the agent, this single tool executes the end-to-end integration sequence: fetching issue metadata, evaluating bot authorship (`isBot`), rendering formatted markdown, uploading the Google Doc via Google Drive API multipart uploads, and dispatching announcements to Discord[^evt-submission-analyser-file-a54ff182c7e8-7be29901][^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
[^evt-submission-analyser-file-a54ff182c7e8-7be29901]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
