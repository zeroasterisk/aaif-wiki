---
type: resource
title: AAIF Public Agent Resources and Skills
description: Public repository packaging portable agent skills, repeatable recipes,
  prompt templates, and CI canary workflows for foundation automation.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
tags:
- skills
- recipes
- prompts
- github-actions
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:35:53.136890+00:00'
sources:
- id: evt-public-agents-file-b33563055168-20a6dfb7
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
  author: Manik Surtani
  last_modified: '2026-05-11T09:21:58+10:00'
---

# Overview
The AAIF Public Agents repository (`aaif/public-agents`) provides reusable, modular assets designed for autonomous and semi-autonomous agent execution across foundation workflows[^evt-public-agents-file-b33563055168-20a6dfb7]. The repository organizes functional extensions into distinct operational tiers, including installable agent skills, repeatable task recipes, reusable prompt templates, and validation documentation[^evt-public-agents-file-b33563055168-20a6dfb7].

The repository adheres to [Agent Skills](../standards/agent-skills.md) conventions and provides foundational automation for administrative triage and community management[^evt-public-agents-file-b33563055168-20a6dfb7].

# Architecture / Specification

## Repository Structure
The repository is partitioned into modular resource collections[^evt-public-agents-file-b33563055168-20a6dfb7]:
- `skills/`: Agent skills encapsulating domain expertise, formatting rules, brand guidelines, and tool execution instructions.
- `recipes/`: Structured, multi-step agent workflows and repeatable task definitions.
- `prompts/`: Reusable prompt templates and instruction sets for specific LLM roles.
- `docs/`: Architectural specifications and contributor guidance.

## Inference Validation and Canary Actions
The repository maintains manually triggered GitHub Actions workflows in `.github/workflows/` to validate model connectivity and test LLM inference pipelines without third-party orchestrators[^evt-public-agents-file-b33563055168-20a6dfb7]:
- **GitHub Models (`copilot-test-action`)**: Connects to GitHub Models (`https://models.github.ai`) using the standard built-in `GITHUB_TOKEN` across organization-scoped chat completion endpoints (`/orgs/{org}/inference/chat/completions`), requiring no external secrets[^evt-public-agents-file-b33563055168-20a6dfb7].
- **Google Gemini (`gemini-test-action`)**: Dispatches prompt workloads to Google Gemini endpoints (such as `gemini-2.5-flash` or `gemini-2.5-pro`) using secret headers (`x-goog-api-key`) scoped either to repository secrets or restricted deployment environments[^evt-public-agents-file-b33563055168-20a6dfb7].

# Lifecycle History
- **Repository Initialization**: Structured baseline directories for skills, recipes, and prompts, alongside GitHub Models and Gemini inference verification workflows[^evt-public-agents-file-b33563055168-20a6dfb7].

[^evt-public-agents-file-b33563055168-20a6dfb7]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
