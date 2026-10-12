---
type: resource
title: Agentic Use Case Classification and Inventory
description: Classification schema and empirical inventory mapping real-world production
  agentic workflows across structural dimensions and verified deployment criteria.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
tags:
- workflows
- classification
- use-cases
- taxonomy
- production-deployment
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:13:00.577812+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:35:55-07:00'
- id: evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
  author: Jodee Varney
  last_modified: '2026-10-01T07:35:55-07:00'
- id: evt-wg-workflows-and-process-integration-pr-41
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
  author: jodeev
  last_modified: '2026-10-01T14:35:56+00:00'
---

# Overview

The Agentic Use Case Classification and Inventory is a reference catalog and structural analysis framework maintained by the Critical Use Cases Workstream within the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]. It provides a standardized schema for describing, comparing, and designing real-world agentic workflows across cross-industry and domain-specific contexts[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]. Rather than functioning as a ranked or exhaustive registry, the inventory focuses on capturing diverse pattern coverage across real implementations to aid architectural design and scenario analysis[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

# Architecture / Specification

### Classification Dimensions

The framework organizes workflow records across twelve attributes, separating structural classification dimensions from supporting contextual fields[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]:

- **Trigger:** Identifies the initiating event of the workflow, categorized by external system signals, scheduled recurring timers, or manual human prompts[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].
- **HITL Pattern:** Defines points of mandatory human intervention, distinguishing autonomous execution from explicit [human-approval gates](../patterns/human-approval-gate.md)[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc][^evt-wg-workflows-and-process-integration-pr-41].
- **Agent Count:** Quantifies discrete reasoning entities and captures the architectural rationale for splitting duties (e.g., model specialization, bounded tool permissions, or domain separation)[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc][^evt-wg-workflows-and-process-integration-pr-41].
- **Coordination:** Specifies whether multi-step or multi-agent progression is orchestrated by static deterministic code or runtime language model reasoning[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].
- **Workflow Pattern:** Details the execution topology, spanning linear sequences, concurrent fan-out/fan-in branching, or iterative [bounded convergence loops](../patterns/bounded-convergence-loop.md)[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].

Supporting attributes document observed duration (strictly measuring active agent execution time), target tools and systems, key failure modes, execution preconditions, and empirical notes[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].

### Evidentiary Standard

Entries in the inventory must satisfy strict sourcing requirements to mitigate link rot and speculative marketing claims[^evt-wg-workflows-and-process-integration-pr-41]:
- **Preferred:** Primary vendor product pages or official announcements demonstrating a named customer production deployment[^evt-wg-workflows-and-process-integration-pr-41].
- **Acceptable:** Vendor product pages showing verifiable feature evidence operating in production at scale without a named client[^evt-wg-workflows-and-process-integration-pr-41].
- **Unacceptable:** Secondary blog posts, speculative analyst projections, academic preprints, or personal implementer write-ups lacking production confirmation[^evt-wg-workflows-and-process-integration-pr-41].

### Domain Coverage

The inventory categorizes implementations across horizontal enterprise capabilities (Sales, Marketing, Customer Support, Finance & Operations, HR & Recruiting, Research & Intelligence) as well as specialized industry verticals (Engineering, IT & Network Operations, SDLC, Platform Engineering, Healthcare, Supply Chain, Legal, Education, and Real Estate)[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae].

# Lifecycle History

The initial classification schema was drafted within the Critical Use Cases Workstream to structure workflow comparisons across industries[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]. Under PR #41, the workstream executed an evidentiary cleanup across all entries: speculative citations and defunct vendor references were excised, multi-agent classification rationales were standardized, and the evidentiary baseline requiring verified production deployments was codified[^evt-wg-workflows-and-process-integration-pr-41]. Alignment with the Reference Architecture Workstream remains active[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc].

[^evt-wg-workflows-and-process-integration-file-6cdd0fb97084-5ba45ebc]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/schema-agentic-use-cases.md
[^evt-wg-workflows-and-process-integration-file-c10bbaa87c3e-880211ae]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/critical-use-cases/use-case-inventory.md
[^evt-wg-workflows-and-process-integration-pr-41]: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
