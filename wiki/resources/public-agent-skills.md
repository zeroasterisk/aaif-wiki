---
type: resource
title: Public Agent Skills Repository
description: Public repository packaging portable agent skills, recipes, prompt templates,
  and automated CI test harnesses across GitHub Models and Gemini APIs.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
tags:
- aaif
- skills
- recipes
- prompts
- testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T09:47:10.930550+00:00'
sources:
- id: evt-public-agents-file-b33563055168-20a6dfb7
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
  author: Manik Surtani
  last_modified: '2026-05-11T09:21:58+10:00'
---

# Overview
The Public Agent Skills repository (`aaif/public-agents`) is a public AAIF resource providing reusable agent capabilities, recipes, prompt templates, and automated validation actions for agentic workflows[^evt-public-agents-file-b33563055168-20a6dfb7]. It acts as a shared catalog enabling developers to consume standardized [agent skills](../standards/agent-skills.md) and portable multi-turn execution runtimes[^evt-public-agents-file-b33563055168-20a6dfb7].

# Architecture / Specification
The repository organizes agent assets into standardized top-level directories and execution pipelines[^evt-public-agents-file-b33563055168-20a6dfb7]:

- **Directory Layout**:
  - `skills/`: Installable agent skills providing reusable domain knowledge, brand guidance, and tool integration instructions.
  - `recipes/`: Repeatable task workflows and operational agent runbooks.
  - `prompts/`: Reusable prompt templates and evaluation queries.
  - `docs/`: User guides and contribution documentation.
- **Continuous Integration Test Workflows**:
  - `copilot-test-action`: Queries the GitHub Models inference catalog and executes test completions via the organization-scoped endpoint using default `GITHUB_TOKEN` authentication.
  - `gemini-test-action`: Executes direct prompt tests against Google Gemini endpoints (such as `gemini-2.5-flash`), securing credentials via GitHub repository secrets or environment isolation.

# Lifecycle History
Maintained as an open AAIF asset, the repository integrates standardized Agent Skills definitions with live model verification harnesses in GitHub Actions[^evt-public-agents-file-b33563055168-20a6dfb7].

[^evt-public-agents-file-b33563055168-20a6dfb7]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/README.md
