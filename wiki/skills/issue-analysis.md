---
type: skill
title: Issue Analysis
description: Progressively disclosed Flue skill formatting maintainer issue reviews,
  classifying architectural claims, and surfacing prompt injection indicators.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
tags:
- aaif
- flue
- prompt-injection
- security
- skill
- triage
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:01:50.574988+00:00'
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

The Issue Analysis skill packages standardized maintainer evaluation criteria, section templates, and reference review artifacts into a modular Flue 2.0 skill.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4] Executed as part of the [`resources/submission-analyser.md`](../resources/submission-analyser.md) pipeline, it enables an LLM agent to evaluate public GitHub issues against technical scope and security prerequisites without requiring manual per-issue prompt tuning.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]

The skill incorporates explicit prompt injection reporting conventions. When an agent detects manipulative phrasing, authority spoofing, or instruction injection embedded within untrusted issue text, it records these occurrences in structured metadata while proceeding to review the underlying technical proposal.[^evt-submission-analyser-file-a54ff182c7e8-7be29901] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

# Architecture / Specification

### Progressive Disclosure and Loading

The skill resides under `src/skills/issue-analysis/` and is mounted explicitly using `useSkill()` in the agent entry point rather than via automatic workspace discovery.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

- **Context Budgeting**: Mounting the skill exposes only a single catalog descriptor line in the base system prompt.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec] The full guidance in `SKILL.md` is loaded only when the model invokes `activate_skill`.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]
- **Reference Grounding**: Supporting assets—such as `template.md` and synthetic example analyses in `references/`—remain unread on disk until explicitly referenced, preventing context window bloat on straightforward reviews.[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

### Output Schema and Injection Detection

The analysis output schema mandates structured extraction across problem statements, ecosystem alignment, and safety boundaries.[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4] Crucially, the schema defines dedicated fields for defensive telemetry:[^evt-submission-analyser-file-a54ff182c7e8-7be29901] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

- `injectionSuspected`: Boolean flag set to `true` whenever user-supplied issue content attempts to alter system constraints, inspect environmental variables, or redirect tool execution.[^evt-submission-analyser-file-a54ff182c7e8-7be29901] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]
- `injectionNotes`: Explanatory narrative detailing the detected attack vector or manipulation attempt.[^evt-submission-analyser-file-a54ff182c7e8-7be29901] [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]

By treating adversarial inputs as analysis signal rather than unhandled abort conditions, the skill provides maintainers with audit trails of hostile activity.[^evt-submission-analyser-file-a54ff182c7e8-7be29901]

# References

- [`resources/submission-analyser.md`](../resources/submission-analyser.md)
- [`standards/agent-skills.md`](../standards/agent-skills.md)
- [`guidelines/agentic-ai-security-best-practices.md`](../guidelines/agentic-ai-security-best-practices.md)

[^evt-submission-analyser-file-3dc5dd454e08-fa24a9ec]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/DESIGN.md
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
[^evt-submission-analyser-file-a54ff182c7e8-7be29901]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/AGENTS.md
