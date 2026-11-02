---
type: resource
title: Community Events CI Evaluation and Hygiene Suite
description: Automated testing harness, pre-commit validation pipeline, and credential-isolated
  GitHub Actions workflow verifying AAIF community skills and plugins.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
tags:
- testing
- ci-cd
- community-events
- validation
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:13:06.696072+00:00'
sources:
- id: evt-community-events-file-63a9c44a44ac-37822210
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-a5c0f08bc43f-b99183b6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.github/workflows/validate.yml
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-pr-54
  resource: https://github.com/aaif/community-events/pull/54
  author: rparundekar
  last_modified: '2026-10-01T02:01:13+00:00'
---

# Overview
The Community Events Evaluation Suite is an automated validation pipeline and behavioral testing harness verifying skill definitions, portability manifests, OOXML transformations, and security boundaries across the `aaif/community-events` repository [^evt-community-events-file-a5c0f08bc43f-b99183b6]. It enforces strict operational separation between untrusted pull request checks and privileged credentialed workflows [^evt-community-events-file-a5c0f08bc43f-b99183b6].

# Architecture / Specification
The evaluation infrastructure is organized across multi-tier verification gates:

- **Credential Isolation & Workflow Gate**: The primary pull request pipeline (`validate.yml`) runs in a strictly read-only execution context with zero access to Google Workspace, Slack, or Luma credentials [^evt-community-events-file-a5c0f08bc43f-b99183b6]. A structural check script (`scripts/check_workflows.py`) scans workflow configurations to ensure no secret tokens can be leaked via fork pull requests, restricting credentialed jobs exclusively to gated manual triggers [^evt-community-events-file-a5c0f08bc43f-b99183b6].
- **Pre-Commit Hygiene**: Pre-commit hooks enforce formatting, syntax integrity, and security policies across files [^evt-community-events-file-63a9c44a44ac-37822210]:
  - **Static Linting**: Employs Ruff for syntax and defect detection without disruptive auto-formatting [^evt-community-events-file-63a9c44a44ac-37822210].
  - **Secret Detection**: Leverages Gitleaks to inspect staged commits for exposed secrets [^evt-community-events-file-63a9c44a44ac-37822210].
  - **Targeted Exclusions**: Skips byte-level churn on vendored self-extracting payloads such as `design/aaif-design-system.html` [^evt-community-events-file-63a9c44a44ac-37822210].
  - **Operational Safeguards**: Enforces that secrets are never passed via process arguments (`argv`), that redactor mechanisms remain centralized to prevent unmasked personal data in public logs, and that tooling rule banners do not drift between copies across skills [^evt-community-events-file-63a9c44a44ac-37822210].
- **Manifest and Portability Conformance**: Automated checkers (`check_manifests.py`, `check_skill_portability.py`, and `check_frontmatter.py`) validate root Agent Plugins v1 specifications and skill frontmatter compliance, while the Claude Code CLI validates marketplace manifests [^evt-community-events-file-a5c0f08bc43f-b99183b6] [^evt-community-events-pr-54].
- **Deterministic Python Test Suite**: Executes unit tests across the standard-library event toolkit (`lib/aaif_events`), design token extractors, and skill scripts, requiring full git history checkout to evaluate deep archive transforms such as OOXML font-embed strip tests [^evt-community-events-file-a5c0f08bc43f-b99183b6].

# Related Concepts
- [Agent Plugin Portability](../guidelines/agent-plugin-portability.md)
- [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md)
- [Community Event Operations](../skills/community-event-operations.md)

[^evt-community-events-file-63a9c44a44ac-37822210]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
[^evt-community-events-file-a5c0f08bc43f-b99183b6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.github/workflows/validate.yml
[^evt-community-events-pr-54]: https://github.com/aaif/community-events/pull/54
