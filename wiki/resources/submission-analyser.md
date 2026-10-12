---
type: resource
title: Submission Analyser
description: Headless GitHub Actions workflow agent analyzing repository issues via
  Copilot inference and publishing reports to Google Docs and Discord without repo
  write permissions.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
tags:
- automation
- github-actions
- copilot
- security
- agent-runner
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:52:06.856195+00:00'
sources:
- id: evt-submission-analyser-file-cbe7142ed7e3-716e943f
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
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
The Submission Analyser is an automated, headless GitHub Actions agent designed to process public or private repository issues, execute analysis pipelines using multi-vendor language models brokered through GitHub Copilot, and output formatted assessments to external platforms such as Google Docs and Discord [^evt-submission-analyser-file-cbe7142ed7e3-716e943f][^evt-submission-analyser-file-973b5680342c-d651657e]. Built to inspect submissions across Foundation repositories without human intervention, it operates under a strictly scoped privilege boundary to mitigate prompt injection and unauthorized repository tampering [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

# Architecture / Specification

## Cross-Repository Invocation and Permissions
The workflow relies exclusively on the `workflow_dispatch` trigger to enable cross-repository operations, where upstream repositories run lightweight dispatcher actions that target the centralized tooling repository [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]. This dispatch model prevents event confusion and ensures uniform execution logic across projects. Execution concurrency is serialized using composite keys based on the target repository and issue number [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

To neutralize prompt injection risks inherent in parsing untrusted issue text with LLMs possessing shell access, the workflow enforces a strict privilege minimization model [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]:
- `contents: read`: Authorizes checking out workflow assets without allowing modifications to source files or workflow definitions [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
- `copilot-requests: write`: Grants access to make inference requests against GitHub Copilot endpoints billed to the repository organization [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
- No `issues: write`: Excludes repository write tokens entirely, eliminating the vector where untrusted prompt content coerces the agent into modifying repository files or commenting maliciously back onto GitHub [^evt-submission-analyser-file-cbe7142ed7e3-716e943f][^evt-submission-analyser-file-973b5680342c-d651657e].

## Copilot Authentication and Inference
Model inference is conducted exclusively through the GitHub Copilot provider, eliminating third-party API secret maintenance [^evt-submission-analyser-file-973b5680342c-d651657e][^evt-submission-analyser-file-4a20043f76a6-7597f83c]:
- **Token Exchange**: Inference endpoints do not accept raw Personal Access Tokens (PATs) or default Actions server-to-server tokens as bearer credentials [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73][^evt-submission-analyser-file-4a20043f76a6-7597f83c]. The runtime exchanges the workflow's `GITHUB_TOKEN` (bearing `copilot-requests: write`) via `https://api.github.com/copilot_internal/v2/token` for a short-lived session token with appropriate editor headers [^evt-submission-analyser-file-4a20043f76a6-7597f83c].
- **Model Redundancy**: Specifiers require a `<provider-id>/<model-id>` syntax (e.g., `github-copilot/claude-opus-4.7`) [^evt-submission-analyser-file-4a20043f76a6-7597f83c]. Operational configuration defines a primary model alongside a multi-vendor fallback (e.g., `github-copilot/gpt-5.4`), both served through the unified Copilot entitlement [^evt-submission-analyser-file-973b5680342c-d651657e].
- **Diagnostic Probing**: Diagnostic workflows (`probe-copilot.yml`) provide out-of-band verification of token entitlement and endpoint resolution without initiating billable inference [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73].

## External Delivery Pipeline
The agent delivers structured outputs to out-of-band channels via distinct credentials [^evt-submission-analyser-file-973b5680342c-d651657e]:
- `GOOGLE_SERVICE_ACCOUNT_JSON` and `GOOGLE_DRIVE_FOLDER_ID`: Facilitates publishing formatted assessment documents to a secure Google Drive repository [^evt-submission-analyser-file-973b5680342c-d651657e].
- `DISCORD_WEBHOOK_URL`: Transmits notifications and summary links into moderation and review channels [^evt-submission-analyser-file-973b5680342c-d651657e].
- Bot authors are identified and skipped prior to publishing to avoid automated recursive analysis loops [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

# References
- Related guidelines: [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md)
- Operational patterns: [Kill Switch](../patterns/kill-switch.md), [Proposal Execution Split](../patterns/proposal-execution-split.md)

[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/secrets.md
[^evt-submission-analyser-file-cbe7142ed7e3-716e943f]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/issue-analyst.yml
