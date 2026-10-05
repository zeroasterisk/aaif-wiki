---
type: taxonomy
title: Universal Agent Terms
description: Standardized universal vocabulary defining foundational AI agent concepts
  including agents, tools, skills, and models.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/86
tags:
- definitions
- skos
- taxonomy
- vocabulary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:01:41.918137+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-86
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/86
  author: julianna-ciq
  last_modified: '2026-10-02T20:21:39+00:00'
---

# Overview
Universal agent terms establish the vendor-neutral vocabulary used across Agentic AI Foundation specifications, reference architectures, and governance frameworks [^evt-ws-taxonomy-landscape-pr-86].

# Architecture / Specification
- **Agent**: An autonomous or semi-autonomous software entity that perceives context, evaluates goals, and invokes tools to achieve desired outcomes.
- **Tool**: A discrete interface, function, or API through which an agent interacts with external systems or retrieves information.
- **Skill**: A packaged collection of instructions, schemas, and assets enabling an agent to perform a specific operational capability.
- **Model**: A computational artifact capable of reading and generating structured or unstructured text and data [^evt-ws-taxonomy-landscape-pr-86]. While agent implementations primarily employ Large Language Models (LLMs), Small Language Models (SLMs), or Vision-Language Models (VLMs), the concept also includes non-language approaches (such as Hidden Markov Models), serialized weight representations (such as GGUF artifacts), and their execution via inference engines [^evt-ws-taxonomy-landscape-pr-86].

# Lifecycle History
Curated by the Taxonomy and Landscape workstream [../workstreams/taxonomy-and-landscape.md](../workstreams/taxonomy-and-landscape.md) to maintain consistent foundational semantics across AAIF work products [^evt-ws-taxonomy-landscape-pr-86].

[^evt-ws-taxonomy-landscape-pr-86]: https://github.com/aaif/ws-taxonomy-landscape/pull/86
