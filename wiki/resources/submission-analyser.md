---
type: resource
title: Submission Analyser
description: Headless Flue 2.0 agent running in GitHub Actions that analyses repository
  issues and publishes reports, incorporating dual-matrix dry-run canary verification.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- agents
- ci-cd
- github-actions
- flue
- tools
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:38:42.139689+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview

The Submission Analyser is a headless agent built on Flue 2.0 and automated via GitHub Actions to inspect intake repository issues, apply structured rubric assessments, and generate evaluation summaries [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

To manage upstream LLM provider volatility, the analyser incorporates a daily dry-run canary workflow verifying both primary and fallback model pipelines across real model endpoints without performing publication actions [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Architecture / Specification

### Model Canary Verification

The canary workflow (`canary.yml`) isolates model availability risks from production analysis pipelines [^evt-submission-analyser-file-4b56c7c159ef-381bcc10]:

- **Dual Matrix Execution:** Evaluates both primary and fallback model legs independently with `fail-fast: false`, ensuring a failure in the primary model does not mask a silent outage in the fallback engine [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Dry-Run Confinement:** Operates with `DRY_RUN=1` and minimal permissions (`contents: read`, `issues: read`, `copilot-requests: write`), explicitly excluding downstream write credentials (such as Google Drive or Discord secrets) to limit security exposure [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Token Attestation:** Uses repository workflow identity tokens rather than personal access tokens (PATs) to authenticate against individual Copilot endpoints, avoiding permission revocation issues [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Scheduled Frequency:** Scheduled off-peak daily (07:15 UTC) against a fixed reference issue to detect header or credential drifts prior to production triage [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Lifecycle History

Deployed across foundation repositories for automated issue intake analysis alongside guidelines documented in [skills/issue-analysis](../skills/issue-analysis.md) and [guidelines/working-group-submission-guidelines](../guidelines/working-group-submission-guidelines.md) [^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
