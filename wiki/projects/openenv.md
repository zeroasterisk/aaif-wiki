---
type: project
title: OpenEnv
description: Unified open-source framework and container packaging specification for
  agentic reinforcement learning execution environments.
resource: https://github.com/aaif/project-proposals/issues/50
tags:
- aaif
- project
- reinforcement-learning
- environments
- mcp
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:49:55.277955+00:00'
sources:
- id: evt-project-proposals-issue-50
  resource: https://github.com/aaif/project-proposals/issues/50
  author: burtenshaw
  last_modified: '2026-09-29T21:03:42+00:00'
---

# Overview
OpenEnv is an open-source framework for building, packaging, deploying, and interacting with isolated execution environments for agentic reinforcement learning (RL)[^evt-project-proposals-issue-50]. It provides Gymnasium-style lifecycle APIs (`reset`, `step`, `state`) and standardizes the model-to-environment boundary using the Model Context Protocol (MCP) to ensure consistency between agent training, evaluation, and production deployment[^evt-project-proposals-issue-50].

# Architecture / Specification
OpenEnv standardizes agent RL environments as containerized units published to hubs and executed across trainers, harnesses, and sandboxes[^evt-project-proposals-issue-50]:
- **Model-to-Environment Protocol**: Uses MCP (built on `fastmcp`) as the communication interface so environments expose tools identical to production runtime surfaces[^evt-project-proposals-issue-50].
- **RL Lifecycle Interface**: Exposes standardized step, reset, reward, rubric, and state inspection operations[^evt-project-proposals-issue-50].
- **Harness & Sandbox Support**: Integrates with agent harnesses such as Goose ([`../reference-architectures/goose.md`](../reference-architectures/goose.md)) via RFC 005 wrapping patterns, alongside execution sandboxes like Modal, Daytona, and Azure Container Apps[^evt-project-proposals-issue-50].
- **Trainer Compatibility**: Compatible with RL post-training frameworks and inference engines including TRL, Unsloth, SkyRL, Axolotl, Lightning AI, vLLM, and SGLang[^evt-project-proposals-issue-50].

# Lifecycle History
- **October 2025**: Launched as a joint initiative between Hugging Face and Meta (Meta-PyTorch) at the PyTorch Conference[^evt-project-proposals-issue-50].
- **June 2026**: Transitioned repository to `huggingface/OpenEnv` under a multi-company Technical Committee spanning Meta, NVIDIA, Microsoft, Hugging Face, Modal, and others[^evt-project-proposals-issue-50].
- **September 2026**: Proposed for AAIF hosted project status under the sponsorship of Caitie McCaffrey (Microsoft)[^evt-project-proposals-issue-50].

[^evt-project-proposals-issue-50]: https://github.com/aaif/project-proposals/issues/50
