---
type: resource
title: Submission Analyser
description: Headless GitHub Actions agent utilizing Copilot inference and dry-run
  canary pipelines to triage and evaluate foundation submissions.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- ci-cd
- github-actions
- triage
- copilot
- canary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:12:31.354401+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview

Submission Analyser is a headless GitHub Actions agent designed to evaluate incoming issue submissions, perform rubric assessments, and draft triage summaries for AAIF repositories [^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. It executes autonomous triage pipelines without requiring local infrastructure by relying on GitHub-native workflow execution and model inference entitlements [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Architecture / Specification

The submission analyser architecture incorporates automated model resilience and permission containment mechanisms:

- **Canary Verification Pipeline**: Implements independent primary (e.g. `claude-opus-4.7`) and fallback (e.g. `gpt-5.4`) matrix legs configured with `fail-fast: false` to ensure fallback availability is continuously validated without masking silent failures [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Dry-Run Isolation**: Supports `DRY_RUN=1` modes for execution runs, analyzing and rendering output without mutating issues or publishing external documents, thereby avoiding unnecessary secret and credential exposure [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Scoped Inference Permissions**: Operates under minimal read-only token permissions (`contents: read`, `issues: read`) coupled with `copilot-requests: write` to grant model inference directly through organization-billed tokens rather than personal access tokens (PATs) [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Lifecycle History

The canary workflow was integrated to provide daily health verification against fragile model provider endpoints and header shifts [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
