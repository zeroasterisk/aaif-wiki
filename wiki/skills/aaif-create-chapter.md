---
type: skill
title: AAIF Create Chapter Skill
description: Automated provisioning skill managing chapter Google Drive asset hierarchies,
  OOXML presentation rebranding, and web banner rendering.
resource: https://github.com/aaif/community-events/pull/65
tags:
- community-events
- provisioning
- skills
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:31:06.215058+00:00'
sources:
- id: evt-community-events-pr-65
  resource: https://github.com/aaif/community-events/pull/65
  author: rparundekar
  last_modified: '2026-11-03T21:50:00+00:00'
---

# Overview

The AAIF Create Chapter skill automates the provisioning, asset rebranding, and Drive estate configuration for regional AAIF community chapters. It creates isolated chapter directory hierarchies, copies required presentation and governance templates, and executes text and branding transformations across templates to prepare chapters for local organizers.[^evt-community-events-pr-65]

# Architecture / Specification

Chapter provisioning orchestrates several sequential transformation stages:

- **Drive Hierarchy Provisioning**: Duplicates chapter workspace templates into target regional directories, provisioning folder trees for banners, decks, and operating documentation.
- **OOXML Rebranding**: Modifies OpenXML presentation payloads directly to substitute template naming tokens with authorized chapter titles.
- **Web Banner Rendering**: Rather than copying static template PNG assets—which historically produced city name mismatches across chapter directories—the workflow renders `Web Banner.png` directly from the fourth slide of `Banners/Square Logo.pptx` using `render_web_banner.py` and Google Slides export APIs.[^evt-community-events-pr-65]
- **Verification Guards**: Asserts that rendered slide text strictly contains "AAIF Community Events" concatenated with the chapter name.[^evt-community-events-pr-65] Generated banners are stamped with the source presentation's `md5Checksum` and chapter name within Drive `appProperties` to ensure idempotency and permit safe re-runs without duplicate exports.[^evt-community-events-pr-65]
- **Error Handlers**: A failed banner render exits with code 2 during creation and halts dirty resumes, while temporary Slides export copies that fail trashing cleanly trigger operational errors.[^evt-community-events-pr-65]

# Lifecycle History

Originally, chapter generation duplicated `Web Banner.png` byte-for-byte from TemplateCity, causing at least 37 chapters to retain default template imagery.[^evt-community-events-pr-65] PR #65 introduced dynamic rendering from slide templates and automated verification stamps across all active chapter estates.[^evt-community-events-pr-65]

# References

- [Community Event Operations](../skills/community-event-operations.md)
- [AAIF Check Setup](../skills/aaif-check-setup.md)

[^evt-community-events-pr-65]: https://github.com/aaif/community-events/pull/65
