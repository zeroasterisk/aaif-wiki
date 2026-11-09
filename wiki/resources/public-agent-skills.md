---
type: resource
title: AAIF Public Agent Skills Repository
description: Public repository packaging portable, reusable agent skills, manifest
  configurations, and automated validation tests.
resource: https://github.com/aaif/public-agents/pull/2
tags:
- skills
- repository
- agent-skills
- packaging
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:38:48.174844+00:00'
sources:
- id: evt-public-agents-pr-2
  resource: https://github.com/aaif/public-agents/pull/2
  author: moezdil
  last_modified: '2026-06-27T05:21:39+00:00'
---

# Overview

The `aaif/public-agents` repository is an open catalog managed by the Agentic AI Foundation to package portable, modular agent skills adhering to the [Agent Skills Standard](../standards/agent-skills.md) [^evt-public-agents-pr-2]. It provides tested, vendor-neutral capabilities that can be loaded dynamically across compliant harnesses and runtimes.

# Architecture / Specification

### Repository Layout

While early documentation described planned subdirectories for prompts and recipes, the repository structure focuses strictly on modular skill packages located within the `skills/` directory tree [^evt-public-agents-pr-2]. References to unimplemented structures such as `recipes/`, `prompts/`, and `docs/` have been removed to align documentation with actual repository layout [^evt-public-agents-pr-2].

Skills stored within the catalog undergo automated testing harnesses to verify manifest schemas, parameter handling, and security boundaries before inclusion [^evt-public-agents-pr-2].

[^evt-public-agents-pr-2]: https://github.com/aaif/public-agents/pull/2
