---
type: skill
title: Issue Analysis Skill
description: An agent skill and runtime workflow for automated, context-grounded issue
  triage, analysis drafting, and multi-channel publication.
resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/canary.yml
tags:
- skill
- automation
- security
- issue-triage
- canary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:54:23.726606+00:00'
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
- id: evt-submission-analyser-file-4a20043f76a6-7597f83c
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/models.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
- id: evt-submission-analyser-file-31e1ac583aa4-9cc8bb73
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/probe-copilot.yml
  author: Manik Surtani
  last_modified: '2026-08-20T17:58:39+10:00'
---

# Overview

The Issue Analysis Skill defines an automated, context-grounded workflow for triaging GitHub issue submissions, conducting structured multi-dimensional evaluation, and publishing formatted analysis documents and channel announcements [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]. It operates within headless runtime harnesses like Flue to parse issue payloads, cross-reference proposal references, evaluate security and technical feasibility, and generate structured output artifacts without granting write permissions to the analyzed code repository [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

# Architecture / Specification

## Permission Boundaries and Least Privilege

The issue analysis execution lifecycle is strictly isolated from target repository write permissions [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]:
- **Token Scoping**: Workflows operate with minimal `contents: read` permissions and deliberately omit `issues: write`. Because issue text constitutes untrusted, attacker-controlled input read by an LLM with execution capabilities, eliminating repository write permissions prevents prompt injection attacks from altering repository code, workflow configurations, or issue metadata [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
- **Inference Entitlement**: Inference access relies on `copilot-requests: write`, which authorizes GitHub Copilot inference requests billed to the organization without granting repository write access [^evt-submission-analyser-file-973b5680342c-d651657e].
- **Out-of-Band Delivery**: Output artifacts are published to external services (e.g., Google Drive/Docs API and Discord webhooks with suppressed mentions) rather than committing comments or PRs back to the target repository [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

## Resilience and Canary Validation

- **Primary & Fallback Multi-Model Routing**: Model invocation routes primarily through a designated primary model (e.g., `github-copilot/claude-opus-4.7`) and automatically falls back to an alternate multi-vendor model (e.g., `github-copilot/gpt-5.4`) at the workflow level if primary inference fails [^evt-submission-analyser-file-4a20043f76a6-7597f83c].
- **Scheduled Canary Health Checks**: A daily automated canary executes dry runs (`DRY_RUN=1`) against a fixed issue across an independent job matrix with `fail-fast: false` [^evt-submission-analyser-file-4b56c7c159ef-37a7feb5]. Running matrix legs independently guarantees that broken fallback endpoints or expired token entitlements are detected prior to primary provider outages [^evt-submission-analyser-file-4b56c7c159ef-37a7feb5].
- **Injection Detection**: Output schemas capture explicit `injectionSuspected` and `injectionNotes` fields, treating prompt injection attempts as structured review findings rather than silent failures [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# Lifecycle History

- Implemented in `aaif/submission-analyser` under the Flue 2.0 runtime architecture [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].
- Standardized on GitHub Copilot token exchange integration for unified multi-vendor model inference [^evt-submission-analyser-file-4a20043f76a6-7597f83c].

# References

- [Cross-Repository Agent Dispatch](../specification/cross-repository-agent-dispatch.md)
- [Agent Skill Specification](../specification/agent-skill.md)
- [Execution Harness Taxonomy](../taxonomy/harness.md)

[^evt-submission-analyser-file-4a20043f76a6-7597f83c]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/models.md
[^evt-submission-analyser-file-4b56c7c159ef-37a7feb5]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/canary.yml
[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/TODO.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/secrets.md
[^evt-submission-analyser-file-cbe7142ed7e3-716e943f]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
