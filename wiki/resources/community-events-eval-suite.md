---
type: resource
title: Community Events Evaluation Suite
description: CI test harness, pre-commit validation pipeline, and intent-matching
  evaluation graders for AAIF community event operations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
tags:
- testing
- evals
- ci
- community
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:06:25.969180+00:00'
sources:
- id: evt-community-events-file-cd95e0a9e63d-5578e7ad
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
---

# Overview
The Community Events Evaluation Suite is an automated CI test harness and validation framework verifying operational agent skills, event lifecycle automation, and chapter management pipelines [^evt-community-events-file-cd95e0a9e63d-5578e7ad]. Maintained within the AAIF community repository, the suite couples credential-isolated test runners with intent-matching graders to ensure agent skills trigger accurately on non-technical user input [^evt-community-events-file-cd95e0a9e63d-5578e7ad].

# Architecture / Specification

## Grader Architecture and Natural-Language Intent Verification
- **Skill Activation Graders**: Evaluates whether an agent runtime invokes the correct skill tool in response to conversational prompts without relying on explicit keyword triggers [^evt-community-events-file-cd95e0a9e63d-5578e7ad].
- **Setup Verification Pattern**: Implements frontmatter-based grader definitions matching regex invocations (e.g., `aaif-check-setup`) when non-technical inquiries such as "is it all working" are posed without containing keywords like "setup" or "check" [^evt-community-events-file-cd95e0a9e63d-5578e7ad].
- **Execution Isolation**: Runs verification checks inside isolated runner environments to evaluate [community event operations skills](../skills/community-event-operations.md) against regressions before changes are merged.

# Lifecycle History
- Established to provide regression testing and CI verification across event automation workflows.
- Authoritative commit added intent-matching graders in `evals/check-setup/graders/skill_fires.md` to evaluate tool activation against colloquial phrasing [^evt-community-events-file-cd95e0a9e63d-5578e7ad].

[^evt-community-events-file-cd95e0a9e63d-5578e7ad]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
