---
type: initiative
title: Submission Analyser Initiative
description: Automated cross-repository agent workflow generating structured issue
  analysis, triage reports, and candidate evaluations for AAIF proposals.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- governance
- automation
- triage
- canary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:16:56.665932+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview
The Submission Analyser is an automated AAIF workflow that executes an autonomous triage agent against incoming repository issues and proposals, producing structured evaluation reports, risk summaries, and candidate classifications [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Architecture / Specification
The analyzer workflow integrates scheduled and dispatchable execution pipelines designed for operational resilience and model availability verification:

- **Model Canary Workflow**: Executes automated dry-run analyses against fixed, known reference issues to continuously monitor model inference endpoints and credentials before production failures occur [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Matrix Isolation**: Runs primary and fallback model legs independently with `fail-fast: false`, ensuring silent degradation in fallback model paths is identified rather than masked by primary endpoint failures [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Least-Privilege Execution**: Operates in dry-run mode under read-only repository permissions (`contents: read`, `issues: read`) coupled with scoped inference tokens (`copilot-requests: write`), omitting write credentials and publication destinations during verification runs [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Lifecycle History
Automated canary pipelines were integrated into repository CI workflows to validate GitHub Copilot model endpoints and organizational token access [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
