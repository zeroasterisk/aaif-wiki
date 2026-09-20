---
type: specification
title: Agent Skill Specification
description: A portable bundle of instructions, frontmatter metadata, scripts, and
  asset references providing modular agent capabilities with standardized trigger
  evals and secret safety.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CONTRIBUTING.md
tags:
- skills
- specification
- runtime
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:08:25.774551+00:00'
sources:
- id: evt-community-events-file-eca12c0a30e2-e4dc57b4
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-a1a9eeb43d4d-942740dd
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-8570bc08b106-eb1aa55d
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview

An agent skill is a modular directory bundle comprising a `SKILL.md` instruction document with structured YAML frontmatter and optional executable scripts, designed to dynamically equip AI agents with specific domain workflows and tool integrations.[^evt-community-events-file-eca12c0a30e2-e4dc57b4] Skill activation relies on intent-matching descriptions, robust argument hinting, strict credential segregation from command-line arguments, and empirical two-arm behavioral evaluation.[^evt-community-events-file-a1a9eeb43d4d-942740dd]

# Architecture / Specification

## Structure and Metadata
A skill repository conforms to a standardized layout:[^evt-community-events-file-eca12c0a30e2-e4dc57b4]
- `SKILL.md`: Root configuration document starting with YAML frontmatter specifying `name`, an action-oriented `description` defining both what the skill performs and its auto-activation trigger ("Use when asked to..."), and an optional `argument-hint`.[^evt-community-events-file-eca12c0a30e2-e4dc57b4]
- `scripts/`: Optional directory containing deterministic helper scripts invoked using standardized environment paths (such as `${CLAUDE_SKILL_DIR}/scripts/...`) rather than hardcoded locations.[^evt-community-events-file-eca12c0a30e2-e4dc57b4]

Frontmatter values such as `argument-hint` must be fully quoted to prevent YAML parsing failures that silently drop skill descriptions and break auto-activation.[^evt-community-events-file-eca12c0a30e2-e4dc57b4]

## Security and Secrets Isolation
Skills enforce strict credential handling rules: secrets (API keys, authorization tokens) must never be passed via command-line arguments (`argv`), as command arguments are exposed in process tables (`ps`) and process logging.[^evt-community-events-file-eca12c0a30e2-e4dc57b4] Bundled scripts must read tokens and keys exclusively from environment variables, local `.env` files, or secure keychains.[^evt-community-events-file-eca12c0a30e2-e4dc57b4]

## Behavioral Evaluation and Two-Arm Testing
Skill trigger fidelity and behavioral guardrails are validated through empirical evaluation test cases comparing runs with and without the skill enabled:[^evt-community-events-file-a1a9eeb43d4d-942740dd]
- **Delta Measurement (`arm: with-only`)**: Distinguishes base model capability from instructions supplied by the skill specification.[^evt-community-events-file-a1a9eeb43d4d-942740dd]
- **Neighbor Disambiguation**: Verifies that prompts targeting a specific workflow activate the intended skill rather than semantically adjacent skills sharing similar vocabulary.[^evt-community-events-file-8570bc08b106-eb1aa55d][^evt-community-events-file-a1a9eeb43d4d-942740dd]
- **Untrusted Input and Public-Copy Guardrails**: Tests defense against prompt injection and ensures strict omission of sensitive personal identifiable information (PII) from public outputs.[^evt-community-events-file-a1a9eeb43d4d-942740dd]
- **Write-Gate Verification**: Verifies that agents default to read-only/reporting modes and execute mutations only upon explicit human authorization.[^evt-community-events-file-a1a9eeb43d4d-942740dd]

[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
[^evt-community-events-file-eca12c0a30e2-e4dc57b4]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CONTRIBUTING.md
