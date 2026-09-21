---
type: project
title: Submission Analyser
description: Headless CI-invoked Flue 2.0 agent automating prompt-injection-resilient
  GitHub issue analysis with multi-model fallback and external publishing.
resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/canary.yml
tags:
- project
- flue
- ci-cd
- github-actions
- observability
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:57:07.578361+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-37a7feb5
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
- id: evt-submission-analyser-file-cbe7142ed7e3-716e943f
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
- id: evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/TODO.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-973b5680342c-d651657e
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/secrets.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-31e1ac583aa4-9cc8bb73
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/probe-copilot.yml
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
- id: evt-submission-analyser-file-4a20043f76a6-7597f83c
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/models.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
---

# Overview

The Submission Analyser is an automated, headless issue analysis agent framework built on Flue 2.0 that processes incoming GitHub issues and generates structured assessment documents and notifications [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]. Triggered across repositories via GitHub Actions, the agent extracts issue telemetry, evaluates proposed submissions against structured skills such as `../methodology/issue-analysis-skill.md`, formats findings, and publishes output to Google Docs and Discord channels without retaining write permissions to source repositories [^evt-submission-analyser-file-cbe7142ed7e3-716e943f] [^evt-submission-analyser-file-973b5680342c-d651657e].

# Architecture / Specification

### Permission Boundary and Execution Model

The analyser runs inside GitHub Actions runners under strict principle-of-least-privilege boundaries [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]:
- **Token Permissions**: The workflow operates with `contents: read` and `copilot-requests: write`, intentionally omitting `issues: write` [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]. Because target issue bodies contain untrusted user inputs, revoking repository write access prevents prompt-injection attacks from tampering with source files or CI configurations [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
- **Target Dispatching**: Workflow execution is invoked via `workflow_dispatch`, enabling cross-repository analysis where the target issue resides in external repositories (such as `aaif/project-proposals`) [^evt-submission-analyser-file-cbe7142ed7e3-716e943f] [^evt-submission-analyser-file-973b5680342c-d651657e].

### Model Inference and Token Exchange

All model requests route exclusively through GitHub Copilot endpoints [^evt-submission-analyser-file-4a20043f76a6-7597f83c]:
- **Authentication**: Copilot inference endpoints require short-lived tokens obtained via internal token exchange against `https://api.github.com/copilot_internal/v2/token` using standard editor headers, which is handled using the runner's GITHUB_TOKEN under `copilot-requests: write` [^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73] [^evt-submission-analyser-file-4a20043f76a6-7597f83c].
- **Model Fallback**: Models are addressed using `<provider-id>/<model-id>` specifiers [^evt-submission-analyser-file-4a20043f76a6-7597f83c]. The system configures a primary model (e.g., `github-copilot/claude-opus-4.7`) and a vendor-diverse fallback model (e.g., `github-copilot/gpt-5.4`) executed at the workflow level if the primary leg fails [^evt-submission-analyser-file-4b56c7c159ef-37a7feb5] [^evt-submission-analyser-file-973b5680342c-d651657e].

### Monitoring and Canary Validation

A scheduled daily canary workflow runs at an off-peak interval (`07:15 UTC`) against a known baseline issue with `DRY_RUN=1` [^evt-submission-analyser-file-4b56c7c159ef-37a7feb5]. The canary matrix independently evaluates both primary and fallback legs with `fail-fast: false` to detect credential expiration, endpoint drift, or header requirement changes prior to production failures [^evt-submission-analyser-file-4b56c7c159ef-37a7feb5].

[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/probe-copilot.yml
[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/models.md
[^evt-submission-analyser-file-4b56c7c159ef-37a7feb5]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/canary.yml
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/TODO.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/secrets.md
[^evt-submission-analyser-file-cbe7142ed7e3-716e943f]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
