---
type: resource
title: Submission Analyser
description: Headless triage agent and sandboxed GitHub Actions runner executing Flue
  2.0 workflows with automated dual-leg model health canaries.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- triage
- automation
- github-actions
- flue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:21:15.179990+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview
Submission Analyser is a headless triage agent and GitHub Actions runner deployed across AAIF repositories to evaluate incoming proposals, issues, and pull requests against working group submission guidelines and architectural taxonomy criteria[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. Built on Flue 2.0, the analyser executes structured assessment prompts using foundation model providers while enforcing strict read-only execution boundaries during automated diagnostic evaluations[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Architecture / Specification
The agent workflow operates in automated CI environments and incorporates a dedicated daily model canary pipeline to detect endpoint entitlement shifts, token expirations, and provider outages prior to production triage runs[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]:
- **Dual-Leg Canary Matrix**: Evaluates both primary (`claude-opus-4.7`) and fallback (`gpt-5.4`) Copilot models independently with `fail-fast: false` to ensure an outage on the primary path does not mask a broken fallback leg[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Dry-Run Isolation**: Canary executions set `DRY_RUN=1` against a fixed, closed issue, performing full analysis and rendering while omitting Google Workspace and Discord publishing credentials[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Least-Privilege Token Permissions**: Execution relies on GitHub token permissions (`copilot-requests: write`, `contents: read`, `issues: read`) rather than personal access tokens (PATs), binding Copilot inference entitlement directly to the repository organization[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Lifecycle History
The daily model canary pipeline was introduced into `.github/workflows/canary.yml` to protect against silent endpoint breaking changes and entitlement revocations on the individual Copilot endpoint[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
