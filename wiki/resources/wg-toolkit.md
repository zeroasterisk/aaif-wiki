---
type: resource
title: WG Toolkit
description: Python utility library providing LFX MCP client interfaces, Zoom transcript
  download fallbacks, and structured model completion for AAIF working group automation.
resource: https://github.com/aaif/working-group-chairs/blob/8f87f60854c20fc6acf909767ed9ab6199ed644a/scripts/wg-toolkit/README.md
tags:
- tooling
- lfx
- mcp
- automation
- transcripts
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:17.639051+00:00'
sources:
- id: evt-working-group-chairs-file-537f2936247b-4efa392f
  resource: https://github.com/aaif/working-group-chairs/blob/8f87f60854c20fc6acf909767ed9ab6199ed644a/scripts/wg-toolkit/README.md
  author: Pavan Sudheendra
  last_modified: '2026-11-18T18:00:48+00:00'
---

# Overview
The WG Toolkit is a shared Python package (`wg-toolkit`) maintained in the `aaif/working-group-chairs` repository that provides foundational building blocks for Agentic AI Foundation automation scripts reading LFX meeting platform data [^evt-working-group-chairs-file-537f2936247b-4efa392f]. It provides common infrastructure for scripts that generate meeting minutes, compile status reports, and process committee transcripts across working groups [^evt-working-group-chairs-file-537f2936247b-4efa392f].

# Architecture / Specification
The package is organized into four core functional modules:
- `wg_toolkit.lfx`: Manages LFID OAuth and authentication through an `mcp-remote` bridge or explicit bearer token, dynamic tool discovery by name suffix, and automated pagination via `collect_pages` [^evt-working-group-chairs-file-537f2936247b-4efa392f]. Environment token isolation withholds credentials such as `LFX_MCP_TOKEN` and `OPENAI_API_KEY` from helper child processes [^evt-working-group-chairs-file-537f2936247b-4efa392f].
- `wg_toolkit.transcripts`: Handles WebVTT and plain-text cue parsing, implementing `TranscriptDownloader` to pull Zoom VTT files directly or fall back to a headless Playwright automation flow via the Zoom recording player [^evt-working-group-chairs-file-537f2936247b-4efa392f].
- `wg_toolkit.llm`: Exposes `StructuredModelClient` and `ModelConfig` executing strict JSON Schema completions against OpenAI-compatible Chat Completions endpoints, evaluating refusal, transport failures, and token truncation [^evt-working-group-chairs-file-537f2936247b-4efa392f].
- `wg_toolkit.common`: Standardizes date and HTTPS URL validation, file output collision protection with owner-only permissions, and credential-safe error messages [^evt-working-group-chairs-file-537f2936247b-4efa392f].

The toolkit is designed to be declared as an editable path dependency in downstream automation scripts, including [skills/aaif-wg-meeting-notes](../skills/aaif-wg-meeting-notes.md) and [skills/aaif-wg-monthly-report](../skills/aaif-wg-monthly-report.md) [^evt-working-group-chairs-file-537f2936247b-4efa392f].

[^evt-working-group-chairs-file-537f2936247b-4efa392f]: https://github.com/aaif/working-group-chairs/blob/8f87f60854c20fc6acf909767ed9ab6199ed644a/scripts/wg-toolkit/README.md
