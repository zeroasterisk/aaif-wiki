---
type: resource
title: Submission Analyser
description: Headless CI issue analysis agent built on Flue 2.0 that evaluates external
  GitHub submissions and pull requests with dual-model canary verification.
resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
tags:
- tooling
- automation
- ci
- github-actions
- flue
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:08:57.753284+00:00'
sources:
- id: evt-submission-analyser-file-4b56c7c159ef-381bcc10
  resource: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
  author: Manik Surtani
  last_modified: '2026-09-29T10:55:53+10:00'
---

# Overview

The Submission Analyser is a headless continuous integration (CI) agent implementation built on the Flue 2.0 framework that automatically evaluates external GitHub issues and pull requests submitted to AAIF repositories. It provides structured feedback, reference comparisons, and triage analysis against foundational working group guidelines without requiring interactive human dispatch.

# Architecture / Specification

The analyzer executes in GitHub Actions workflows with strict permission scoping and automated model access verification[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

## Model Access and Canary Testing

Because external foundation model inference endpoints represent a fragile dependency subject to shifting header requirements and entitlement expirations, the project operates an automated daily model canary workflow[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]:
- **Dry-Run Execution**: The canary executes the real agent over a fixed known issue with `DRY_RUN=1`. The agent analyses and renders output but halts before creating Google Docs, commenting on issues, or posting to external notification channels[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Dual-Leg Matrix**: The canary runs independent matrix legs for both a primary model (`github-copilot/claude-opus-4.7`) and a fallback model (`github-copilot/gpt-5.4`) with `fail-fast: false`[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. Independent execution ensures that a failure in the primary provider does not mask a broken fallback path[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].
- **Least-Privilege Security**: Canary jobs run with read-only repository permissions (`contents: read`, `issues: read`) and `copilot-requests: write`[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]. Model inference relies directly on workflow-scoped tokens carrying organization Copilot entitlements rather than personal access tokens (PATs), and publishing secrets are excluded to limit credential exposure[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

# Lifecycle History

- Implemented automated daily model canary workflow to detect endpoint drift and entitlement revocation across primary and fallback inference providers[^evt-submission-analyser-file-4b56c7c159ef-381bcc10].

[^evt-submission-analyser-file-4b56c7c159ef-381bcc10]: https://github.com/aaif/submission-analyser/blob/df50b968b54196c39fa1037cf2e90f359f1ea7ab/.github/workflows/canary.yml
