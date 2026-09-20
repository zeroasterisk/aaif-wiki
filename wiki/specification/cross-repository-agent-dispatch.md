---
type: specification
title: Cross-Repository Agent Dispatch
description: A workflow pattern isolating privileged agent credentials by triggering
  headless runs across repository security boundaries.
resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
tags:
- specification
- security
- workflow-pattern
- github-actions
- dispatch
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:54:23.726606+00:00'
sources:
- id: evt-submission-analyser-file-cbe7142ed7e3-716e943f
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
  author: Manik Surtani
  last_modified: '2026-08-20T16:59:44+10:00'
- id: evt-submission-analyser-file-973b5680342c-d651657e
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/secrets.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
- id: evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4
  resource: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/TODO.md
  author: Manik Surtani
  last_modified: '2026-08-20T17:10:18+10:00'
---

# Overview

Cross-Repository Agent Dispatch is a security and operational pattern that decouples event triggers in untrusted or public target repositories from the privileged execution environment where AI agents run [^evt-submission-analyser-file-cbe7142ed7e3-716e943f]. Instead of executing agent tooling directly within the repository where an issue or pull request is opened, a lightweight dispatcher workflow triggers a `workflow_dispatch` event in a dedicated agent repository [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

# Architecture / Specification

```
[Target Repository]                     [Tooling / Agent Repository]
  Issue Created / Edited                   workflow_dispatch (restricted)
         │                                                │
         ▼                                                ▼
  Dispatcher Action ──────(REST Dispatch Token)─────► Agent Execution
  (No inference/doc secrets)                              ├── Read Target Issue
                                                          ├── Run Agent / Model
                                                          └── Publish External Artifact
```

## Core Invariants

1. **Credential Isolation**: Sensitive integration secrets (such as Google Service Account keys, Discord webhooks, or LLM credentials) reside exclusively in the central tooling repository and are never exposed to workflow contexts in target repositories [^evt-submission-analyser-file-973b5680342c-d651657e].
2. **Read-Only Scoping**: The executing agent workflow holds read-only token permissions against the target repository (`contents: read`, `issues: read`) and lacks write permissions (`issues: write`) to eliminate untrusted input writeback and tampering attacks [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].
3. **Target Validation & Anti-Spoofing**: The agent workflow accepts an explicit target repository variable or dispatch parameter (`TARGET_REPOSITORY`), validating that fetched issue metadata strictly corresponds to the intended target repository to prevent cross-repo confusion or misrouted publications [^evt-submission-analyser-file-973b5680342c-d651657e].
4. **Input Sanitization**: Dispatched input parameters (e.g., numeric `issue_number` validation and boolean flags) are validated before passing into shell commands or API queries to mitigate injection risks [^evt-submission-analyser-file-cbe7142ed7e3-716e943f].

# Lifecycle History

- Defined and adopted in AAIF tooling pipelines for repository issue triage and automated analysis (`aaif/submission-analyser`) [^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4].

# References

- [Issue Analysis Skill](../skills/issue-analysis.md)
- [Human Approval Gate](../specification/human-approval-gate.md)
- [Workflow Pattern Specification](../specification/workflow-pattern.md)

[^evt-submission-analyser-file-5c6a1301c6b5-a75aa6c4]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/TODO.md
[^evt-submission-analyser-file-973b5680342c-d651657e]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/docs/secrets.md
[^evt-submission-analyser-file-cbe7142ed7e3-716e943f]: https://github.com/aaif/submission-analyser/blob/de61e0e9fd709846c35c21cddb287f29a13c6aba/.github/workflows/issue-analyst.yml
