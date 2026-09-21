---
type: governance
title: Working Group Reporting
description: Standardized monthly reporting cadence, pull request workflow, and template
  structure for AAIF working groups.
resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
tags:
- governance
- reporting
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T09:47:15.220541+00:00'
sources:
- id: evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
  author: Alex Frazer
  last_modified: '2026-07-21T10:11:53-04:00'
- id: evt-wg-security-and-privacy-file-9677055e316b-27369ef5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/TEMPLATE.md
  author: Alex Frazer
  last_modified: '2026-07-21T10:11:53-04:00'
---

# Overview

Working Groups (WGs) submit a monthly report to the Technical Committee (TC) to summarize progress, highlight ecosystem activity, identify blockers, and request decisions [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

Reports are due by the last business day of the month. The TC review window closes 7 calendar days after submission, and the report is merged once signed off or the window closes, whichever is sooner [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

# Specification

## Workflow

1. Copy `TEMPLATE.md` into a new file named `YYYY-MM-report.md`.
2. Fill in header fields: Reporting period, Date submitted, Working Group, and Chair(s).
3. Open a pull request titled `[Report] WG <Name> – Month YYYY` and add the TC (or designated TC GitHub team) as reviewers [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
4. Update the WG's `README.md` to index the new report [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

## Required Sections

Reports must be concise, scannable, and based on recorded evidence (meeting notes, charter, git history). Sections must be included even if they contain no content, in which case "None." or "None this month." should be written [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

The required sections are [^evt-wg-security-and-privacy-file-9677055e316b-27369ef5]:

1. **Summary:** 2–3 sentences capturing the month at a glance.
2. **Progress Against Objectives:** What shipped or advanced, tied back to stated objectives.
3. **Ecosystem Highlights:** Relevant activity, publications, or decisions happening in external groups (e.g., OWASP, AARM, MCP ACS).
4. **Blockers and Risks:** Anything the TC should be aware of.
5. **Decisions Needed from the TC:** Explicit asks stated clearly.
6. **Next Month's Focus:** Top 2–3 priorities for the coming month.
7. **Metrics / Links:** Status against charter Success Metrics (KPIs: Adoption, Quality, Community, Timeliness) and supporting links (PRs, issues, meeting notes) [^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
[^evt-wg-security-and-privacy-file-9677055e316b-27369ef5]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/TEMPLATE.md
