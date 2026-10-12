---
type: guideline
title: Agent Plugin Portability Guidelines
description: Engineering standards for packaging multi-client agent plugins and skills
  across repository checkouts, Goose CLI, and Claude Desktop runtimes.
resource: https://github.com/aaif/community-events/pull/60
tags:
- guidelines
- standards
- packaging
- portability
- plugins
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:27:04.970951+00:00'
sources:
- id: evt-community-events-pr-60
  resource: https://github.com/aaif/community-events/pull/60
  author: rparundekar
  last_modified: '2026-10-11T15:58:20+00:00'
- id: evt-community-events-file-f922f666d0ff-e2dbe3f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-d236c244f6dc-0c36b708
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

Agent plugin portability guidelines define runtime architectures, directory isolation policies, and credential lookup protocols required to run agent skills across multiple client environments [^evt-community-events-pr-60]. While early agent skill toolkits assumed execution within a local git repository checkout possessing a configured shell and ambient environment variables, modern production plugins must execute interchangeably within headful desktop applications (such as Claude Desktop), CLI runtimes like [Goose](../resources/goose.md), and git-less cache directories [^evt-community-events-pr-60].

These guidelines establish uniform design principles for managing script path resolution, persistent application data, credential cascades, and self-diagnostic readiness checks [^evt-community-events-pr-60].

# Architecture / Specification

## 1. Relative Script & Asset Resolution
Portable skills must never rely on process working directories (`cwd`), global `PYTHONPATH` modifications, or repository-root relative paths (`python3 skills/...`) [^evt-community-events-pr-60]:
- Skill instructions and manifests must define paths relative to `<skill-root>`, dynamically resolving the parent directory of the active skill definition (`SKILL.md`) [^evt-community-events-file-d236c244f6dc-0c36b708], [^evt-community-events-pr-60].
- Automated linter checks (such as `check_skill_portability.py`) must validate skill instruction files to prevent hardcoded repository paths [^evt-community-events-pr-60].

## 2. Dynamic Data Directory Resolution (`datadir`)
Agent plugins must decouple internal transient files, output artifacts, and cache directories from the host workspace [^evt-community-events-pr-60]:
- In developer git checkouts, outputs may default to the repository root [^evt-community-events-pr-60].
- In installed plugin environments (such as `.git`-less copies in application plugin caches), outputs and caches must resolve to standard OS application support paths (e.g., `~/Library/Application Support/AAIF/` on macOS) rather than the active workspace directory [^evt-community-events-file-f922f666d0ff-e2dbe3f7], [^evt-community-events-pr-60].
- Relative user overrides for data directories must be rejected or normalized to protect host filesystem integrity [^evt-community-events-pr-60].

## 3. Hierarchical Credential Cascades
Installed agent tools often run without user shell profiles or pre-loaded environment variables. Credential resolution must implement a defined fallback cascade [^evt-community-events-pr-60]:
1. **Environment Variables**: Explicit process environment variables.
2. **Local Repository Config**: `.env` files located at the repository root (bypassed if running from an external plugin install).
3. **OS Credential Stores**: Platform keychains (such as macOS Keychain via `security`), cached per execution session to minimize repeated auth prompts.

Failure modes must produce actionable error diagnostics pointing directly to setup remediation tools rather than printing generic authentication tracebacks [^evt-community-events-pr-60].

## 4. Git-Independent Execution
Plugins must operate seamlessly in environments where the `.git` directory has been stripped by plugin managers (e.g., Claude Desktop plugin caches) [^evt-community-events-pr-60]:
- Synchronization and deployment utilities must not call out to `git` binaries or assume branch tracking state [^evt-community-events-pr-60].
- Gitignore safety guards must dynamically evaluate whether the active directory resides inside a valid git worktree prior to issuing VCS queries [^evt-community-events-pr-60].

## 5. Self-Diagnostic Readiness Checks
Plugins must supply a dedicated setup verification command (such as `aaif-check-setup`) [^evt-community-events-pr-60]:
- Evaluates API token presence, OS credential availability, CLI dependencies (`gws`), and network reachability without altering system state [^evt-community-events-pr-60].
- Outputs plain-language diagnostics detailing specific missing permissions and the exact scoped sign-in command required for resolution [^evt-community-events-pr-60].

Related implementations are demonstrated in [skills/community-event-operations](../skills/community-event-operations.md) and governed under the [Agent Skills standard](../standards/agent-skills.md).

[^evt-community-events-file-d236c244f6dc-0c36b708]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-file-f922f666d0ff-e2dbe3f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
