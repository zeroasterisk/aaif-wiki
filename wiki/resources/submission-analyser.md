---
type: resource
title: Submission Analyser
description: Headless CI triage agent utilizing GitHub Actions, Copilot inference,
  and multi-model fallback to validate incoming issue submissions in a read-only environment.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- tooling
- ci-cd
- triage
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:35:07.018920+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview

Submission Analyser is a headless continuous integration (CI) triage agent designed to parse, validate, and evaluate incoming GitHub issue submissions against foundation requirements [^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. It executes automated first-pass evaluations within containerized workflows without requiring persistent interactive execution environments [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Architecture / Specification

The analyser incorporates specific architectural resilience and security mechanisms:

- **Model Access Canary**: Employs an out-of-band scheduled daily canary workflow running in dry-run mode (`DRY_RUN=1`) against a fixed issue baseline to proactively detect expired PATs, broken Copilot individual endpoints, and header drift before live triage failures occur [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Dual-Matrix Fallback Validation**: Operates an independent primary and fallback execution matrix (running `fail-fast: false`), preventing a broken fallback model configuration from being masked when the primary endpoint is healthy [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Least Privilege Execution**: Uses scoped repository permissions (`contents: read`, `issues: read`, `copilot-requests: write`) and eliminates third-party publication credentials during validation runs [^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. Model inference utilizes repository-level GITHUB_TOKEN Copilot entitlements rather than external personal access tokens [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# References

- [Submission Analyser Repository](https://github.com/aaif/submission-analyser)

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
