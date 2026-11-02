---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF technical working group establishing shared workflow execution models,
  reference architectures, execution profiles, and workflow pattern catalogs.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
tags:
- working-group
- workflows
- patterns
- reference-architecture
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:08:37.616955+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
  author: Yaron Schneider
  last_modified: '2026-09-28T06:29:14-07:00'
- id: evt-wg-workflows-and-process-integration-pr-24
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/24
  author: yaron2
  last_modified: '2026-09-28T13:29:14+00:00'
---

# Overview
The Workflows and Process Integration Working Group is an AAIF technical body establishing shared workflow execution models, reference architectures, execution profiles, and reusable pattern catalogs for agentic automation[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# Architecture / Specification
The working group is co-chaired by Yaron Schneider (Diagrid) and Adam Seligman (Workato)[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. It executes its charter across three core workstreams:
- **Reference Architectures**: Defines seven execution profiles spanning from Profile 1 (fully deterministic) to Profile 7 (fully agentic), advocates a proposed "least agentic default" recommendation principle, and develops six charter-derived archetypes (including bounded automation and gated operations)[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]. The workstream demonstrates an automated specification-driven design flow compiling machine-readable YAML definitions into visual diagrams and technical documentation across standard and agentic variants[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Critical Use Cases**: Maintains a catalog of 89 categorized production workflows classified by execution primitives (trigger, human-in-the-loop pattern, agent count, coordination model, workflow pattern) and maps them to a reusable pattern catalog that includes patterns such as the autonomous convergence loop[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].
- **Taxonomy Alignment**: Coordinates cross-working group term harmonization, testing use case primitive classifications against universal taxonomy definitions to prevent terminology fragmentation[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26].

# References
- Workflow Primitives: `../taxonomy/workflow-primitives.md`
- Bounded Convergence Loop: `../patterns/bounded-convergence-loop.md`
- Bounded Autonomous Remediation: `../architectures/bounded-autonomous-remediation.md`

[^evt-wg-workflows-and-process-integration-file-fa4050a9f626-89594a26]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-07-report.md
