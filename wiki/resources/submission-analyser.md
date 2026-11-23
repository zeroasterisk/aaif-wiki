---
type: resource
title: Submission Analyser
description: Headless issue triage runner executing Flue agent skills within GitHub
  Actions, isolating untrusted inputs while routing model calls exclusively through
  GitHub Copilot via token exchanges.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
tags:
- ci-cd
- github-actions
- flue
- copilot
- triage
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:50:10.574709+00:00'
sources:
- id: evt-submission-analyser-file-973b5680342c-d651657e
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-31e1ac583aa4-9cc8bb73
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
- id: evt-submission-analyser-file-4a20043f76a6-7597f83c
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
---

# Overview

Submission Analyser is a headless triage runner executing [Flue](../../skills/issue-analysis.md) agent skills inside GitHub Actions workflows to evaluate project proposals and community issues [^evt-submission-analyser-file-973b5680342c-d651657e]. It enforces strict credential boundaries, operates without write access to monitored issue repositories, and routes all LLM invocations exclusively through GitHub Copilot [^evt-submission-analyser-file-4a20043f76a6-7597f83c].

# Architecture / Specification

### Model Access and Credential Isolation

All model inference routes strictly through GitHub Copilot using model specifiers formatted as `<provider-id>/<model-id>` with dotted versioning (such as `github-copilot/claude-opus-4.7` and fallback `github-copilot/gpt-5.4`) [^evt-submission-analyser-file-4a20043f76a6-7597f83c]. The runtime rejects non-Copilot providers at startup to prevent unintended data routing [^evt-submission-analyser-file-4a20043f76a6-7597f83c].

In CI environments, the agent does not maintain a static third-party API key; instead, it relies on workflow-scoped authorization via the `copilot-requests: write` GitHub Actions permission [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]. Copilot inference endpoints reject direct GitHub PAT tokens with HTTP 400 bad request responses, requiring an upstream token exchange against `https://api.github.com/copilot_internal/v2/token` using editor client headers to mint short-lived Copilot bearer tokens (`tid=...;exp=...;proxy-ep=...`) [^evt-submission-analyser-file-4a20043f76a6-7597f83c].

### Repository Permissions and Cross-Repo Isolation

Submission Analyser adheres to least privilege by enforcing `contents: read` permissions on GitHub tokens without repository write or issue modification rights [^evt-submission-analyser-file-973b5680342c-d651657e]. When running cross-repository triage, the target repository is explicitly declared via `TARGET_REPOSITORY` and verified in workflow assertions to prevent unintentional evaluation of the runner's local issues [^evt-submission-analyser-file-973b5680342c-d651657e]. Output publication is isolated to external channels via Google Drive service account integration and Discord webhooks [^evt-submission-analyser-file-973b5680342c-d651657e].

# Lifecycle History

- Detailed model routing rules, Copilot internal token exchange behaviors, and GitHub Actions `copilot-requests: write` permissions documented in repository specifications [^evt-submission-analyser-file-973b5680342c-d651657e] [^evt-submission-analyser-file-4a20043f76a6-7597f83c].

[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
