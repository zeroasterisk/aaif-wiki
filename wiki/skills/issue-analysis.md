---
type: skill
title: Issue Analysis Agent Skill
description: Standardized agent skill and Flue execution harness evaluating GitHub
  issues against repository context with read-only sandbox boundaries and multi-vendor
  Copilot routing.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
tags:
- skill
- flue
- security
- github-actions
- triage
- copilot
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:34:45.960863+00:00'
sources:
- id: evt-submission-analyser-file-cbe7142ed7e3-716e943f
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
- id: evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-973b5680342c-d651657e
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-4a20043f76a6-7597f83c
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
---

# Overview
The Issue Analysis skill and automated agent harness evaluates incoming GitHub issues against repository documentation, architecture guidelines, and taxonomy standards to produce structured triage assessments [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]. Operating on the Flue runtime, the agent routes inference requests through GitHub Copilot's multi-model provider catalog and publishes reports out-of-band to Google Docs and Discord without maintaining write access to the source code repository [^evt-submission-analyser-file-cbe7142ed7e3-716e943f] [^evt-submission-analyser-file-973b5680342c-d651657e].

# Architecture / Specification
The issue analysis agent architecture integrates execution constraints, authentication flows, and containment boundaries:

- **Execution Runtime and Model Routing**: Implemented using Flue and `pi-ai`, the harness routes all model completions through the `github-copilot` provider [^evt-submission-analyser-file-4a20043f76a6-7597f83c]. It configures a primary model (`github-copilot/claude-opus-4.7`) and an automated workflow fallback (`github-copilot/gpt-5.4`) across different model families without requiring secondary vendor credentials [^evt-submission-analyser-file-973b5680342c-d651657e]. `useModel()` scoping binds model selection to individual submission lifecycles without mid-run swapping [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- **Copilot Token Exchange**: Under CI workflows, `copilot-requests: write` permissions permit exchanging the workflow's built-in `GITHUB_TOKEN` for short-lived session bearer tokens at `https://api.github.com/copilot_internal/v2/token`, avoiding direct inference PAT restrictions [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73] [^evt-submission-analyser-file-4a20043f76a6-7597f83c].
- **Principle of Least Privilege**: Workflow permissions are constrained strictly to `contents: read` and `copilot-requests: write` [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]. Repository write permissions (`issues: write`) are explicitly denied, neutralizing prompt injection vectors that attempt to modify workflows or code through attacker-controlled issue text [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
- **Out-of-Band Integration**: Issues are ingested via read-only GitHub API adapters with bot-filtering guards (`isBot`) [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]. Analysis results are exported as Google Docs using single multipart Drive uploads and broadcast to Discord webhooks with mention sanitization (`allowed_mentions: { parse: [] }`) [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- **Injection Detection**: Output schemas include `injectionSuspected` and `injectionNotes` telemetry fields to record adversarial prompt injection attempts as structured findings [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# Lifecycle History
Developed under the AAIF tooling workstream as Flue 2.0, standardizing on built-in Copilot provider routing and decoupled cross-repository dispatch workflows [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/TODO.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
[^evt-submission-analyser-file-cbe7142ed7e3-716e943f]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
