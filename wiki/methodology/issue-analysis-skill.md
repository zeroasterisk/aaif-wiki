---
type: methodology
title: Issue Analysis Skill
description: A structured agent skill methodology for classifying GitHub issues, forming
  root-cause hypotheses, and proposing maintainer actions while mitigating prompt
  injection.
resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/SKILL.md
tags:
- methodology
- agent-skill
- issue-analysis
- triage
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:53:48.943181+00:00'
sources:
- id: evt-submission-analyser-file-5a7044042daa-94e76690
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/SKILL.md
  author: Manik Surtani
  last_modified: '2026-08-19T23:05:57+10:00'
- id: evt-submission-analyser-file-5e60bc4f0771-cf90cfef
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/template.md
  author: Manik Surtani
  last_modified: '2026-08-19T23:05:57+10:00'
- id: evt-submission-analyser-file-20fc496a9225-9e278b3d
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-queue-duplicate-delivery.md
  author: Manik Surtani
  last_modified: '2026-08-19T23:05:57+10:00'
- id: evt-submission-analyser-file-4754a1b8e47b-9ed9890b
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-log-redaction-security.md
  author: Manik Surtani
  last_modified: '2026-08-19T23:05:57+10:00'
- id: evt-submission-analyser-file-6d47851ad176-ba0f0f22
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-config-reload-feature-request.md
  author: Manik Surtani
  last_modified: '2026-08-19T23:05:57+10:00'
---

# Overview
The Issue Analysis Skill is an agentic workflow specification defined in the AAIF `submission-analyser` repository (see `../project/submission-analyser.md`) to produce structured first-pass technical assessments of filed GitHub issues [^evt-submission-analyser-file-5a7044042daa-94e76690]. It establishes a four-step triage procedure that classifies issues, evaluates severity against historical precedents, inspects the codebase in read-only mode, and treats untrusted issue inputs safely [^evt-submission-analyser-file-5a7044042daa-94e76690][^evt-submission-analyser-file-5e60bc4f0771-cf90cfef].

# Architecture / Specification
The skill defines four primary operational phases [^evt-submission-analyser-file-5a7044042daa-94e76690]:

1. **Evidence Isolation and Adversarial Input Detection**: Issue content is ingested strictly as data within nonce delimiters. Meta-instructions or injection attempts are noted in `injectionSuspected` and `injectionNotes` while the underlying technical facts are evaluated [^evt-submission-analyser-file-5a7044042daa-94e76690].
2. **Codebase Inspection**: The agent inspects checked-out repository files to identify concrete paths (`src/...`) and verify the plausibility of reported behavior under a read-only policy [^evt-submission-analyser-file-5a7044042daa-94e76690].
3. **Historical Precedent Grounding**: The agent reviews existing maintainer analyses in `references/` to match tags and components, adopting established criteria for severity rating and root-cause determination [^evt-submission-analyser-file-5a7044042daa-94e76690][^evt-submission-analyser-file-4754a1b8e47b-9ed9890b].
4. **Structured Report Formulation**: Output is formatted according to a standardized schema covering Summary, Classification (`Type`, `Severity`, `Reproducibility`), Affected Components, Root-cause Hypotheses, Suggested Actions, Open Questions, and Related Past Reviews [^evt-submission-analyser-file-5e60bc4f0771-cf90cfef][^evt-submission-analyser-file-20fc496a9225-9e278b3d][^evt-submission-analyser-file-6d47851ad176-ba0f0f22].

[^evt-submission-analyser-file-20fc496a9225-9e278b3d]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-queue-duplicate-delivery.md
[^evt-submission-analyser-file-4754a1b8e47b-9ed9890b]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-log-redaction-security.md
[^evt-submission-analyser-file-5a7044042daa-94e76690]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/SKILL.md
[^evt-submission-analyser-file-5e60bc4f0771-cf90cfef]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/template.md
[^evt-submission-analyser-file-6d47851ad176-ba0f0f22]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/src/skills/issue-analysis/references/example-config-reload-feature-request.md
