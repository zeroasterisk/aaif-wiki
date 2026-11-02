---
type: resource
title: Submission Analyser
description: Headless triage agent executing in GitHub Actions that analyses repository
  issues and publishes assessments using GitHub Copilot model credentials.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
tags:
- agent
- ci-cd
- github-actions
- github-copilot
- triage
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:48:58.418352+00:00'
sources:
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
Submission Analyser is a headless triage agent deployed in GitHub Actions workflows to parse and assess incoming repository issues against codebase documentation.[^evt-submission-analyser-file-4a20043f76a6-7597f83c] The runtime executes via Flue and restricts model inference strictly to GitHub Copilot endpoints to prevent accidental data disclosure to unauthorized third-party model vendors.[^evt-submission-analyser-file-4a20043f76a6-7597f83c]

# Architecture / Specification

## Model Specifier Validation
Model endpoints are configured using the format `<provider-id>/<model-id>`, where version numbers strictly use dots instead of dashes (for example, `github-copilot/claude-opus-4.7` and `github-copilot/gpt-5.4`).[^evt-submission-analyser-file-4a20043f76a6-7597f83c] Runtime initialization strictly validates that specifiers consist of two non-empty segments and enforces that `provider-id` is `github-copilot`, preventing repository variable overrides from silently invoking unapproved alternative providers.[^evt-submission-analyser-file-4a20043f76a6-7597f83c]

## Copilot Credential and Token Exchange
Direct requests bearing standard Personal Access Tokens (PATs) or Actions server-to-server tokens are rejected by Copilot inference backends with HTTP 400 errors.[^evt-submission-analyser-file-4a20043f76a6-7597f83c] Valid model access requires exchanging an authenticated GitHub token at `https://api.github.com/copilot_internal/v2/token` for a short-lived Copilot bearer token.[^evt-submission-analyser-file-4a20043f76a6-7597f83c] In GitHub Actions, the workflow's built-in `GITHUB_TOKEN` is granted `copilot-requests: write` permissions, entitling Copilot requests billed to the repository organization without granting broader repository write access.[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73][^evt-submission-analyser-file-4a20043f76a6-7597f83c]

## Entitlement Probing Workflow
A manual diagnostic workflow (`probe-copilot.yml`) allows maintainers to validate Copilot entitlement and host connectivity without invoking model inference or incurring usage charges.[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73] The probe executes read-only listing requests and strips credential strings from logs to ensure sensitive bearer tokens are not leaked into issue reports.[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]

# References
- Model specification and Copilot credential exchange in `docs/models.md`.[^evt-submission-analyser-file-4a20043f76a6-7597f83c]
- Automated Copilot entitlement check workflow in `.github/workflows/probe-copilot.yml`.[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]

[^evt-submission-analyser-file-31e1ac583aa4-9cc8bb73]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/probe-copilot.yml
[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/docs/models.md
