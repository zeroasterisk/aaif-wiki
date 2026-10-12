---
type: taxonomy
title: Skill
description: Universal taxonomy term defining a packaged, reusable set of instructions
  loaded into context on demand to guide agent task performance.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/47
tags:
- taxonomy
- skills
- prompting
- tools
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:17:10.786573+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-47
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/47
  author: asish-singh
  last_modified: '2026-08-22T12:07:58+00:00'
---

# Overview

A skill is a packaged, reusable set of instructions and supporting resources that changes how an agent performs a class of task, loaded into the model's context when relevant rather than built into the model or executed as code [^evt-ws-taxonomy-landscape-issue-47].

The fundamental discriminator of a skill is that it instructs rather than executes, establishing a clear architectural boundary between a skill and a tool [^evt-ws-taxonomy-landscape-issue-47]:
- **Skill**: Informs and alters what the model itself does next by injecting behavioral guidance, schemas, or domain procedures into [taxonomy/context](../taxonomy/context.md). Removing a skill affects how well or in what style possible actions are executed [^evt-ws-taxonomy-landscape-issue-47].
- **Tool**: Executed external to the model runtime across APIs, filesystems, or services. Removing a [taxonomy/tool](../taxonomy/tool.md) restricts what actions are possible [^evt-ws-taxonomy-landscape-issue-47].

# Architecture / Specification

A skill is characterized by explicit packaging, lifecycle loading, and agent-agnostic consumption [^evt-ws-taxonomy-landscape-issue-47]:
- **Packaging and Lifecycle**: Raw instructions pasted into an isolated prompt constitute ad-hoc [taxonomy/prompt](../taxonomy/prompt.md) input, not a skill. A skill is uniquely named, versioned, discoverable, and loaded on demand across sessions and disparate agent harnesses [^evt-ws-taxonomy-landscape-issue-47].
- **Authoring Orthogonality**: Whether a skill is manually authored by developers or synthesized dynamically by autonomous agents is orthogonal to its taxonomic qualification [^evt-ws-taxonomy-landscape-issue-47].
- **Standardization**: Portable skill packaging formats and manifest structures are defined by [standards/agent-skills](../standards/agent-skills.md) and governed by [guidelines/agent-plugin-portability](../guidelines/agent-plugin-portability.md).

### Taxonomic Relationships
- **Contrasts With**: [taxonomy/tool](../taxonomy/tool.md) [^evt-ws-taxonomy-landscape-issue-47]
- **Related Terms**: `Harness`, [taxonomy/prompt](../taxonomy/prompt.md), [taxonomy/context](../taxonomy/context.md) [^evt-ws-taxonomy-landscape-issue-47]

[^evt-ws-taxonomy-landscape-issue-47]: https://github.com/aaif/ws-taxonomy-landscape/issues/47
