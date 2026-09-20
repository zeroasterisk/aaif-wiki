---
type: specification
title: Write Gate
description: A workflow pattern requiring explicit, separate authorization (e.g.,
  a command-line flag or parameter) before an agent executes a destructive or state-changing
  operation.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/sync-chapters-write-gate/prompt.md
tags:
- workflow-pattern
- security
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:07:48.378508+00:00'
sources:
- id: evt-community-events-file-729b1652037d-3b77c603
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/sync-chapters-write-gate/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-3fa41791e6fd-adb85036
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/references/completed-migrations.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview

The Write Gate is a security and operational pattern applied to agent execution environments, ensuring that any operation capable of modifying persistent state or external systems is explicitly authorized by the user or calling process [^evt-community-events-file-729b1652037d-3b77c603].

This pattern is crucial for safety, particularly in operations like data migrations or synchronization tasks, where the default behavior should be reporting or dry-run, and the write action must be gated [^evt-community-events-file-3fa41791e6fd-adb85036].

# Architecture / Specification

In AAIF operational skills, the Write Gate is often implemented via a `--write` flag. If the flag is absent, the agent performs all computation and reporting necessary to execute the task but stops short of committing the changes. This allows for verification before execution, aligning with principles of [taxonomy/human-in-the-loop](../taxonomy/human-in-the-loop.md) control over critical operations.

[^evt-community-events-file-3fa41791e6fd-adb85036]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/references/completed-migrations.md
[^evt-community-events-file-729b1652037d-3b77c603]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/sync-chapters-write-gate/prompt.md
