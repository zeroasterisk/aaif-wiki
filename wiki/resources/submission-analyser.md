---
type: resource
title: Submission Analyser
description: Headless CI issue analysis agent executing triage via GitHub Actions,
  using Copilot credentials and publishing out-of-band to Google Docs and Discord.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
tags:
- analyser
- github-actions
- copilot
- ci-cd
- flue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:14:25.803140+00:00'
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
`submission-analyser` is a headless continuous integration (CI) issue triage agent designed to evaluate repository proposals and issues without write access to the monitored codebases [^evt-submission-analyser-file-973b5680342c-d651657e]. Built on the Flue runner runtime, the agent executes within GitHub Actions workflows to ingest issue descriptions, conduct multi-model evaluations through GitHub Copilot endpoints, and emit analysis artifacts strictly out-of-band to Google Docs and Discord [^evt-submission-analyser-file-973b5680342c-d651657e].

# Architecture / Specification
## Credential and Privilege Isolation
The agent implements a structural proposal-execution isolation model by stripping all write capabilities from its GitHub execution context [^evt-submission-analyser-file-973b5680342c-d651657e]. Workflow tokens default strictly to `contents: read` without `issues: write` permissions, eliminating prompt-injection paths that could modify issues, pull requests, or code in the monitored repositories [^evt-submission-analyser-file-973b5680342c-d651657e]. When executing across repositories against a distinct `TARGET_REPOSITORY`, it relies on a fine-grained read-only Personal Access Token (PAT) if the target is private [^evt-submission-analyser-file-973b5680342c-d651657e].

Model inference requires no long-lived vendor API keys. Within Actions runs, inference access is obtained by granting `copilot-requests: write` to the workflow's ephemeral `GITHUB_TOKEN` [^evt-submission-analyser-file-973b5680342c-d651657e][^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]. Publication occurs out-of-band using separate credentials:
- `GOOGLE_SERVICE_ACCOUNT_JSON`: Service account key used to create and populate Google Docs reports [^evt-submission-analyser-file-973b5680342c-d651657e].
- `GOOGLE_DRIVE_FOLDER_ID`: Destination folder identifier preventing public folder exposure [^evt-submission-analyser-file-973b5680342c-d651657e].
- `DISCORD_WEBHOOK_URL`: Webhook URL for broadcasting triage notifications to community channels [^evt-submission-analyser-file-973b5680342c-d651657e].

## Model Specifiers and Fallback Topology
The runtime enforces strict two-part dot-notated specifiers (`<provider-id>/<model-id>`) and restricts model calls exclusively to the `github-copilot` provider [^evt-submission-analyser-file-4a20043f76a6-7597f83c]:
- `PRIMARY_MODEL`: `github-copilot/claude-opus-4.7` as the default first-pass analyzer [^evt-submission-analyser-file-973b5680342c-d651657e][^evt-submission-analyser-file-4a20043f76a6-7597f83c].
- `FALLBACK_MODEL`: `github-copilot/gpt-5.4` as the automated secondary provider fallback [^evt-submission-analyser-file-973b5680342c-d651657e][^evt-submission-analyser-file-4a20043f76a6-7597f83c].

Copilot inference endpoints reject raw Personal Access Tokens or server-to-server tokens directly, requiring an exchange against `https://api.github.com/copilot_internal/v2/token` to mint short-lived Copilot bearer tokens with client editor headers [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73][^evt-submission-analyser-file-4a20043f76a6-7597f83c].

# References
- [Proposal Execution Split](../patterns/proposal-execution-split.md)
- [Single-Agent Human Approval Architecture](../architectures/single-agent-human-approval.md)

[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
