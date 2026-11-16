---
type: skill
title: Community Event Operations
description: Procedural operations pipeline and shared infrastructure managing chapter
  provisioning, estate lifecycle automation, and cap constraints.
resource: https://github.com/aaif/community-events/pull/69
tags:
- skills
- operations
- community
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:45.603116+00:00'
sources:
- id: evt-community-events-pr-69
  resource: https://github.com/aaif/community-events/pull/69
  author: rparundekar
  last_modified: '2026-11-12T19:19:20+00:00'
---

# Overview
Community Event Operations provides automated procedures, validation guards, and sync scripts supporting the AAIF city chapter network and event lifecycle[^evt-community-events-pr-69]. It enforces operational governance limits on active chapters while orchestrating Drive folder creation, tracker synchronization, and roster management[^evt-community-events-pr-69].

# Architecture / Specification
The pipeline coordinates several automated utilities:
- **Chapter Provisioning Guard**: Enforces global chapter ceilings via `CHAPTER_CAP`, ensuring automated tools like `create_chapter.py` and `sync_chapters.py` do not exceed authorized organizational bandwidth[^evt-community-events-pr-69].
- **Sync Reconciliation**: Validates accepted organizers against official chapter lists, gating Drive folder generation and Luma feed updates until criteria are satisfied[^evt-community-events-pr-69].
- **Automated Verification**: Integrates unit and regression suites (`test_chapter_cap`, `test_chapter_health`, `test_sync`) to dynamically calculate expected boundaries and preserve estate integrity[^evt-community-events-pr-69].

# Lifecycle History
Following the onboarding of chapters in Columbus and Philadelphia that reached the initial 100-chapter ceiling, the operational chapter cap was expanded from 100 to 125 to permit continuous chapter intake without retiring active chapters[^evt-community-events-pr-69].

[^evt-community-events-pr-69]: https://github.com/aaif/community-events/pull/69
