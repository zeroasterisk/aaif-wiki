---
type: guideline
title: Taxonomy Contribution Guide
description: Authoring standards, automated schema validation workflows, and pull
  request review gates governing contributions to the AAIF taxonomy.
resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/.github/workflows/validate-taxonomy.yml
tags:
- taxonomy
- ci
- governance
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:45:37.921247+00:00'
sources:
- id: evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5
  resource: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/.github/workflows/validate-taxonomy.yml
  author: Matt Lee
  last_modified: '2026-11-15T16:56:33-08:00'
---

# Overview

The Taxonomy Contribution Guide establishes the authoring standards, schema constraints, and pull request gating procedures required for modifications to the Agentic AI Foundation taxonomy repository [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5]. It ensures data integrity and protects shared repository infrastructure against compute abuse during community review cycles [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].

# Architecture / Specification

Contributions modifying `taxonomy/taxonomy.json` must pass automated structural validation prior to merge into the push-protected `main` branch [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].

## Continuous Integration and Gating

To mitigate compute-abuse risks from anonymous pushes, automated validation workflows are gated behind maintainer actions [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5]:
- **Trigger Events**: The validation workflow fires on `pull_request_review` events (submitted or edited) and maintainer `workflow_dispatch` invocations [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].
- **Execution Environment**: Runs under Node.js 20 on Ubuntu with a strict five-minute timeout and automatic cancellation of superseded runs via GitHub concurrency groups [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].
- **Merge Reference Validation**: Pull request validation checks out the computed merge reference (`refs/pull/{number}/merge`) to evaluate the exact candidate state that would land on `main` [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].
- **Execution Checks**: Dependencies are installed with `npm ci --ignore-scripts` before executing `npm run check` to verify JSON syntax and schema compliance [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].

# Lifecycle History

The automated validation workflow was instituted following data corruption regressions (such as unescaped quotes in taxonomy scope notes) to ensure machine-readable taxonomy integrity [^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5].

[^evt-ws-taxonomy-landscape-file-eda84dd4e776-75f907b5]: https://github.com/aaif/ws-taxonomy-landscape/blob/719905a88f11ab6846080313dfe4b8c423411235/.github/workflows/validate-taxonomy.yml
