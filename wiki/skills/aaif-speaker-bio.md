---
type: skill
title: AAIF Speaker Bio Skill
description: An agent skill for drafting concise third-person speaker bios and one-line
  summaries while strictly excluding private contact information and PII.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
tags:
- skill
- speaker
- privacy
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:07:25.718896+00:00'
sources:
- id: evt-community-events-file-a54ff182c7e8-696f1c6d
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-04506118534c-e5137094
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/speaker-bio/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
---

# Overview

The `aaif-speaker-bio` skill formats technical profiles and talk descriptions into standardized, third-person bios for AAIF event agendas, marketing assets, and session descriptions.[^evt-community-events-file-04506118534c-e5137094]

# Architecture / Specification

### PII Redaction & Publication Boundary
In accordance with repository privacy standards, the skill explicitly suppresses direct contact information (such as personal phone numbers, email addresses, and unverified private handles) from generated copy, while retaining professional affiliations, technical talk summaries, and public social handles.[^evt-community-events-file-a54ff182c7e8-696f1c6d][^evt-community-events-file-04506118534c-e5137094]

# Lifecycle History

Maintained in `aaif/community-events` and validated through evaluation suites checking triggering behavior and PII leakage prevention.[^evt-community-events-file-04506118534c-e5137094]

[^evt-community-events-file-04506118534c-e5137094]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/speaker-bio/prompt.md
[^evt-community-events-file-a54ff182c7e8-696f1c6d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
