---
type: resource
title: Public Agent Skills Repository
description: Public repository packaging portable agent skills, recipes, prompt templates,
  and automated CI test workflows across multi-model providers.
resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/.github/workflows/copilot-test-action.yml
tags:
- skills
- agent-skills
- ci
- github-models
- gemini
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T09:41:59.414343+00:00'
sources:
- id: evt-public-agents-file-b248ae41d1f0-0667ce2f
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/.github/workflows/copilot-test-action.yml
  author: Manik Surtani
  last_modified: '2026-05-07T10:21:09+10:00'
- id: evt-public-agents-file-ae1d68d00103-0e76c626
  resource: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/.github/workflows/gemini-test-action.yml
  author: Manik Surtani
  last_modified: '2026-05-11T09:21:58+10:00'
---

# Overview

The `aaif/public-agents` repository maintains public, portable agent skills, integration recipes, and automated verification suites for the Agentic AI Foundation [^evt-public-agents-file-b248ae41d1f0-0667ce2f][^evt-public-agents-file-ae1d68d00103-0e76c626]. It provides reusable templates alongside CI-driven test harnesses to validate multi-model execution and provider interoperability [^evt-public-agents-file-b248ae41d1f0-0667ce2f][^evt-public-agents-file-ae1d68d00103-0e76c626].

# Architecture / Specification

The repository incorporates continuous integration workflows to test multi-model inference capabilities:
- **GitHub Models Integration**: The `copilot-test-action` workflow queries the GitHub Models catalog endpoint (`https://models.github.ai/catalog/models`) and executes chat completion inferences against selected models under organization-level credentials [^evt-public-agents-file-b248ae41d1f0-0667ce2f].
- **Gemini API Integration**: The `gemini-test-action` workflow verifies connectivity and content generation across Gemini model versions (such as `gemini-2.5-flash` and `gemini-2.5-pro`) using direct REST API endpoints [^evt-public-agents-file-ae1d68d00103-0e76c626].

[^evt-public-agents-file-ae1d68d00103-0e76c626]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/.github/workflows/gemini-test-action.yml
[^evt-public-agents-file-b248ae41d1f0-0667ce2f]: https://github.com/aaif/public-agents/blob/fcc3ebc4db293e01305373fc9c2f2c46845ee015/.github/workflows/copilot-test-action.yml
