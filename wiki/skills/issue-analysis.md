---
type: skill
title: Issue Analysis Skill
description: Modular agent skill providing automated, read-only first-pass triage
  and adversarial injection detection for GitHub issue submissions.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
tags:
- skill
- triage
- github-issues
- security
- prompt-injection
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:16:10.100447+00:00'
sources:
- id: evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
---

# Overview
The Issue Analysis Skill (`skills/issue-analysis`) is a modular agent skill that packages domain prompts, schema templates, and evaluation criteria for performing automated, read-only first-pass triage of GitHub issues.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4] Orchestrated within the [Submission Analyser](../resources/submission-analyser.md) harness, the skill inspects incoming bug reports, feature requests, and vulnerability reports to verify submission completeness and detect prompt injection attempts.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

# Architecture / Specification
The skill conforms to the packaging conventions established in the AAIF [Agent Skills Standard](../standards/agent-skills.md):[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

- **Manifest & Skill Loading**: Defined at `src/skills/issue-analysis/SKILL.md` and explicitly loaded into the agent via `useSkill()`, avoiding ambient directory auto-discovery to guarantee deterministic loading.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4] The skill manifest is strictly validated by Flue at process startup prior to invoking model completions.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]
- **Reporting Template**: Uses `template.md` to structure generated triage documents, categorizing submissions by problem type, required reproduction steps, missing environment context, and suggested triage labels.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]
- **Reference Grounding**: Ships with synthetic reference analyses under `references/` covering bug reports, feature proposals, and security disclosures, marked with explicit `example: true` banners to ensure clarity during few-shot context assembly.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]
- **Injection Detection Schema**: Enforces structured outputs containing `injectionSuspected` (boolean) and `injectionNotes` (string), allowing the agent to capture, isolate, and flag adversarial prompt payloads within untrusted issue bodies.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

# Lifecycle History
- **2026-08-19**: Skill implementation finalized in `src/skills/issue-analysis/` under `TODO.md`.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4] Adopted explicit `useSkill()` invocation over implicit discovery and incorporated synthetic benchmark suites alongside automated prompt-injection test harnesses.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
