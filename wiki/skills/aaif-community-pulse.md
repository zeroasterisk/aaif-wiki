---
type: skill
title: AAIF Community Pulse
description: An agent skill for aggregating community updates across Slack, Drive,
  Sheets, and Luma to draft organization-facing reports, now using synthetic data
  in examples.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
tags:
- community
- reporting
- governance
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
This skill aggregates community updates across various platforms (Slack, Google Drive, Sheets, Luma) to generate a consolidated report summarizing organizational activity and progress.

# Lifecycle History
In version 0.6.0 of the Community Events Toolkit, a worked example within this skill was updated to use synthetic cast members instead of real organizer names, ensuring privacy in public repositories [^evt-community-events-file-06572a96a58d-3b18db49] [^evt-community-events-pr-47].

[^evt-community-events-file-06572a96a58d-3b18db49]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
[^evt-community-events-pr-47]: https://github.com/aaif/community-events/pull/47
