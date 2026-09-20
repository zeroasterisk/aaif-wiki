---
type: taxonomy-term
title: Business Task
description: The bounded business problem or work item admitted to and handled by
  a single agent execution run.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- workflow
- terminology
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:07:48.378508+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-49
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
  author: mzagar
  last_modified: '2026-09-17T04:59:03+00:00'
---

# Overview

A Business Task represents the specific, bounded problem that an agent or agentic workflow is commissioned to resolve or execute. It is the unit of work defined by the business context, distinct from the internal subunits of the workflow execution itself [^evt-wg-workflows-and-process-integration-pr-49].

In the context of the [deliverable/bounded-autonomous-remediation-ra](../deliverable/bounded-autonomous-remediation-ra.md), the Business Task is the problem admitted to and handled by the run.

# Architecture / Specification

The Business Task is typically composed of one or more internal workflow subunits, referred to as 'activities' [^evt-wg-workflows-and-process-integration-pr-49].

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
