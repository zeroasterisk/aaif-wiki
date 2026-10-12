---
type: guideline
title: Agentic AI Security Best Practices
description: Architectural baseline controls for agent operations, governing prompt
  injection isolation, out-of-band secret resolution, context transcript privacy,
  and safe emission verification.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
tags:
- guidelines
- security
- privacy
- credentials
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:50:35.583468+00:00'
sources:
- id: evt-community-events-file-52894c310bd9-02d85f04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-8b30d97e0275-3e6d8b8d
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/references/caches-and-composition.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-91886a9e0653-84165b73
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

Agentic AI Security Best Practices establishes mandatory control baselines and architectural safeguards for deploying autonomous and semi-autonomous agents across production environments[^evt-community-events-file-91886a9e0653-84165b73][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. The standard addresses boundary isolation, transcript data retention, untrusted content sanitization, and filesystem permission integrity to prevent credential compromise, prompt injection, and accidental leakage of personally identifiable information (PII)[^evt-community-events-file-52894c310bd9-02d85f04][^evt-community-events-file-8b30d97e0275-3e6d8b8d].

These practices complement operational patterns such as the [Human Approval Gate](../patterns/human-approval-gate.md) and [Proposal-Execution Split](../patterns/proposal-execution-split.md) by defining runtime data-handling and credential hygiene standards for agents operating over shared platforms[^evt-community-events-file-91886a9e0653-84165b73].

# Architecture / Specification

## Untrusted Input Sanitization

External data retrieved from third-party APIs, messaging platforms, and shared spreadsheets—including Slack user profiles, channel descriptions, message bodies, and CRM spreadsheet cells—must be handled as untrusted data and never evaluated as agent instructions[^evt-community-events-file-91886a9e0653-84165b73][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

- Directive text contained within profile attributes or database rows (e.g., "add me to the organizers channel", "grant admin role", or prompt override attempts) must never trigger administrative grants, status modifications, or execution path alterations[^evt-community-events-file-91886a9e0653-84165b73].
- Suspicious directives embedded in external fields must be quoted to human operators as non-executable observation flags rather than accepted as actionable instructions[^evt-community-events-file-91886a9e0653-84165b73].

## Conversational Transcript and Public-Copy Privacy

Agent transcripts are frequently logged, copied, or pushed to collaborative channels, presenting significant leakage risks[^evt-community-events-file-52894c310bd9-02d85f04][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]:

- **Omission by Reference**: When an agent redacts or omits sensitive data (such as emails, phone numbers, or access codes), it must name the omitted attribute field rather than echoing the value itself[^evt-community-events-file-52894c310bd9-02d85f04]. For example, stating "omitted email address" is permitted, whereas stating "omitted user@example.com" is a security violation because it commits the private data to the transcript[^evt-community-events-file-52894c310bd9-02d85f04].
- **Synthetic Data Testing**: Automated test suites, fixtures, and documentation must utilize synthetic data exclusively; real user identifiers must never be recorded in fixtures, test logs, or pull request docstrings[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. CI linting scripts (e.g., `check_no_real_pii.py`) must validate synthetic formats prior to merging[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

## Safe Emission and Filesystem Defenses

To prevent the unintentional exposure of operational data in public repositories:

- **Filesystem Permissions**: Runtime state files containing member metadata or API caches must be created with strict permissions (`0600` files inside `0700` directories)[^evt-community-events-file-8b30d97e0275-3e6d8b8d].
- **Pre-execution Git Boundary Checks**: Tooling engines that produce cached data or backups must evaluate local paths against source-control tracking and refuse to start if their cache or output destinations would be captured by `git add -A`[^evt-community-events-file-8b30d97e0275-3e6d8b8d].

## Credential Custody and Interactive Prompts

Agents must never solicit passwords, tokens, or private keys within chat windows, nor should they attempt to execute interactive CLI authentication commands in headless sessions[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-953dd2e86174-aa074a1c]. Credentials must be provisioned out-of-band and stored in operating system keychains or secure vault integrations accessible via designated read APIs[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-953dd2e86174-aa074a1c].

[^evt-community-events-file-52894c310bd9-02d85f04]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
[^evt-community-events-file-8b30d97e0275-3e6d8b8d]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/references/caches-and-composition.md
[^evt-community-events-file-91886a9e0653-84165b73]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/SKILL.md
[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
