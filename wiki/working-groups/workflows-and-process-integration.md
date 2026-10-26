---
type: working-group
title: Workflows and Process Integration Working Group
description: AAIF technical working group establishing shared workflow execution models,
  common terminology, reference architectures, and enterprise integration patterns
  for AI agents.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
tags:
- working-group
- workflows
- process-integration
- reference-architectures
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:37:49.719958+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
  author: Yaron Schneider
  last_modified: '2026-09-27T17:45:13-07:00'
- id: evt-wg-workflows-and-process-integration-pr-38
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/38
  author: yaron2
  last_modified: '2026-09-28T00:45:18+00:00'
---

# Overview

The Workflows and Process Integration Working Group (WG Workflows & Process Integration) develops vendor-neutral execution models, taxonomy, and reference architectures governing the integration of AI agents into automated workflows and enterprise systems [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. The group is co-chaired by Yaron Schneider (Diagrid) and Adam Seligman (Workato) [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

In August 2026, the group delivered the Phase One Core Terms draft, becoming the first working group in the Agentic AI Foundation to ship a formally voted asset [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Architecture / Specification

The working group organizes its technical agenda across three primary workstreams [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]:

- **Reference Architectures**: Standardizes foundational interaction patterns for agent execution. Completed items include core architecture principles and contributing guidelines (via PR #27) as well as the "human-approved operation" architecture (`architectures/single-agent-human-approval`). A second reference architecture, "bounded autonomous remediation" (`architectures/bounded-autonomous-remediation`), covers internal agent remediation with limit escalation [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Architectural fit is evaluated against an inventory using a four-outcome method: validated, partial, candidate, or no fit [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Taxonomy**: Harmonizes workflow definitions. The Phase One Core Terms established "activity" over "step" as the foundational non-circular primitive from which "workflow" is composed [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Gate, check, and evaluation vocabulary is explicitly out of scope, deferred to related groups such as [Security and Privacy](../working-groups/security-and-privacy.md) and [Accuracy and Reliability](../working-groups/accuracy-and-reliability.md) [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].
- **Critical Use Cases**: Maintains a catalog of real-world enterprise agent scenarios categorized across cohorts including human-approved operations, bounded remediation, and exception detection/escalation [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

# Lifecycle History

- **August 2026**: Phase One Core Terms formally approved by plenary vote [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Reference Architecture deliverable locked to two architectures plus principles and contributing guides [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]. Established a standing rule capping pull requests at roughly 10 files [^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7].

[^evt-wg-workflows-and-process-integration-file-922f59c26329-f75096f7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/reporting/2026-08-report.md
