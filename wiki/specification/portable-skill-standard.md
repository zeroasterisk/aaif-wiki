---
type: specification
title: Portable Skill Standard
description: A set of rules and tooling checks enforcing skill portability, dependency
  management, and consistent use of shared utilities across AAIF agent skills.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
tags:
- skill
- portability
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:08:49.080313+00:00'
sources:
- id: evt-community-events-file-06572a96a58d-3b18db49
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:12:15-07:00'
- id: evt-community-events-pr-47
  resource: https://github.com/aaif/community-events/pull/47
  author: rparundekar
  last_modified: '2026-09-17T05:27:45+00:00'
---

# Overview
The Portable Skill Standard defines the requirements necessary for an AAIF agent skill to be considered portable, particularly for execution environments like claude.ai which require skills to be zipped without external library dependencies [^evt-community-events-pr-47].

# Architecture / Specification
Skills are categorized based on their dependency profile. Skills intended to be standalone must not import shared libraries (`lib/aaif_events`). This standard is enforced by tooling such as `check_portable_skills.py` [^evt-community-events-pr-47].

To maintain consistency and reliability across skills that *do* use shared libraries, common functionality has been centralized:
*   **Redaction:** Redaction logic and flag handling are centralized in `lib/aaif_events/redact.py` to prevent drift and ensure consistent privacy controls [^evt-community-events-file-06572a96a58d-3b18db49].
*   **API Clients:** Google Workspace (GWS) client wrappers (`lib/aaif_events/gws.py`, `lib/aaif_events/sheets.py`) are standardized to ensure consistent retry logic, error handling, and safety guards against permanent API errors [^evt-community-events-file-06572a96a58d-3b18db49].

This standardization ensures that critical operational logic, such as retry tables and safety guards, is uniform across all dependent skills [^evt-community-events-pr-47].

[^evt-community-events-file-06572a96a58d-3b18db49]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
[^evt-community-events-pr-47]: https://github.com/aaif/community-events/pull/47
