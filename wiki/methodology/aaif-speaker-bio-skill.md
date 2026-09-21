---
type: methodology
title: AAIF Speaker Bio Skill
description: Operational agent skill for drafting concise speaker bios and summaries
  while preventing PII exposure.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
tags:
- community
- events
- skill
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:14:06.592159+00:00'
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
The `aaif-speaker-bio` skill drafts concise 60–80 word speaker biographies and one-line summaries for AAIF chapter events and community meetups.[^evt-community-events-file-04506118534c-e5137094]

# Architecture / Specification
The skill ingests speaker talk abstracts, professional roles, and background topics to compose public event collateral.[^evt-community-events-file-04506118534c-e5137094]

## Privacy and Data Safeguards
- **PII Suppression**: Evaluation test cases enforce the omission of personal contact details (such as direct email addresses and phone numbers) from generated public copy, retaining only approved public social handles and professional affiliations.[^evt-community-events-file-04506118534c-e5137094] [^evt-community-events-file-a54ff182c7e8-696f1c6d]
- **Synthetic Test Fixtures**: Test suites and developer runs require synthetic placeholder data to eliminate risk of committing real organizer or speaker contact information into public git history.[^evt-community-events-file-a54ff182c7e8-696f1c6d]

# References
- `../methodology/aaif-speaker-invite-skill.md`
- `../guidelines/brand-guidelines.md`

[^evt-community-events-file-04506118534c-e5137094]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/speaker-bio/prompt.md
[^evt-community-events-file-a54ff182c7e8-696f1c6d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
