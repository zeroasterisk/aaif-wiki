---
type: guideline
title: Working Group Monthly Reporting Guidelines and Template
description: Standardized cadence, structure, review timeline, and pull request workflow
  for AAIF working groups reporting monthly to the Technical Committee.
resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
tags:
- guidelines
- governance
- reporting
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:39:03.792256+00:00'
sources:
- id: evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
  author: Alex Frazer
  last_modified: '2026-07-21T10:11:53-04:00'
- id: evt-wg-security-and-privacy-file-9677055e316b-27369ef5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/TEMPLATE.md
  author: Alex Frazer
  last_modified: '2026-07-21T10:11:53-04:00'
- id: evt-wg-security-and-privacy-file-a17a580f85c2-2e81780d
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-06-report.md
  author: Alex Frazer
  last_modified: '2026-07-21T10:11:53-04:00'
---

# Overview
The Working Group Monthly Reporting Guidelines define the mandatory format, submission cadence, and review workflow for progress reports delivered by AAIF working groups to the `../governance/technical-committee.md`[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28]. These updates maintain asynchronous transparency across working group activities, track deliverable velocity against charter milestones, and surface explicit governance requests requiring Technical Committee review[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-a17a580f85c2-2e81780d].

# Architecture / Specification

## Cadence and Review Lifecycles
Monthly reports follow strict scheduling invariants[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28]:
- **Submission Deadline**: Due by the last business day of each reporting calendar month under the naming convention `reporting/YYYY-MM-report.md`[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
- **Review Window**: The Technical Committee review window closes seven calendar days following submission[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
- **Merge Criteria**: The pull request is merged once the Technical Committee liaison signs off or when the seven-day review window elapses without objection, whichever occurs sooner[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-aef0bad9a49f-35abad8d].

## Document Structure
Each report implements the canonical template structure[^evt-wg-security-and-privacy-file-9677055e316b-27369ef5]:
1. **Header Metadata**: Working Group name, reporting period (`Month YYYY`), Chair(s) and affiliations, and submission date (`YYYY-MM-DD`)[^evt-wg-security-and-privacy-file-9677055e316b-27369ef5].
2. **Summary**: High-level two-to-three sentence narrative summarizing overall monthly progress[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-9677055e316b-27369ef5].
3. **Progress Against Objectives**: Concise bullet points tying delivered or progressed work directly back to charter deliverables[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
4. **Ecosystem Highlights**: External engagement updates with complementary standards organizations (e.g. OWASP, AARM, MCP ACS)[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-9677055e316b-27369ef5].
5. **Blockers and Risks**: Operational, scheduling, or technical risks affecting workstream pacing[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
6. **Decisions Needed from the TC**: Unambiguous, actionable governance questions or mandate requests requiring formal Technical Committee decision[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-9677055e316b-27369ef5].
7. **Next Month's Focus**: Top two to three forward-looking priorities[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
8. **Metrics / Links**: Progress against charter Key Performance Indicators across Adoption, Quality, Community, and Timeliness, followed by supporting URLs to pull requests and meeting records[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28][^evt-wg-security-and-privacy-file-a17a580f85c2-2e81780d].

## Authoring and Evidence Constraints
Authors and automated agents preparing reports must observe strict sourcing rules[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28]:
- Every claim must be grounded in repository git history, deliverables indexes, or authoritative meeting minutes[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
- Uncommitted deliverables may only be described as "drafted" or "in progress"[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
- Sections lacking activity must retain headings with explicit "None." or "None this month." placeholders rather than being omitted[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].
- Reports are linked in reverse-chronological order within the working group's `reporting/README.md` index table[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28].

# References
- Governance policy: `../policies/working-group-lifecycle-policy.md`
- Technical Committee: `../governance/technical-committee.md`
- Report synthesis skill: `../skills/aaif-wg-monthly-report.md`

[^evt-wg-security-and-privacy-file-33d3ff4f1e08-f33f7a28]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/AGENTS.md
[^evt-wg-security-and-privacy-file-9677055e316b-27369ef5]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/TEMPLATE.md
[^evt-wg-security-and-privacy-file-a17a580f85c2-2e81780d]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-06-report.md
