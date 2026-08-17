# ADR-005: Horizon-Inspired Agent Harness & Context Management

## Status
**Accepted**

## Context
When an AI agent curates and updates a knowledge graph across dozens of documents, standard single-prompt or naive multi-turn architectures degrade rapidly:
1. **Context Drift**: The model loses focus on the core taxonomy rules as the conversation fills with file diffs.
2. **Token Bloat**: Ingesting entire files on every turn burns tokens and slows latency.
3. **Model Vendor Lock-In**: Tightly coupling prompt logic to one specific model makes testing alternatives (e.g. Gemini 3.7 Flash vs. Claude 3.7 Sonnet vs. local weights) difficult.

Google's reference implementation in [`google/adk-samples/core/python/long-horizon-harness`](https://github.com/google/adk-samples/tree/main/core/python/long-horizon-harness) (Horizon) solves these problems through structured context management, 3-tier prompt assembly, and context compaction.

## Decision
We adopt the core architectural patterns of the **Horizon Agent Harness** within `aaif_wiki/curator/`:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   3-Tier System Prompt Assembler                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Stable Tier (Static Prefix):                                        │
│    • OKF v0.2 Specification rules                                      │
│    • YAML Frontmatter validation laws                                  │
│    • Output Markdown conventions                                       │
├────────────────────────────────────────────────────────────────────────┤
│ 2. Cached Tier (Context Graph):                                        │
│    • Current graph index (working groups, active topics, taxonomies)   │
│    • Canonical charter summaries                                       │
├────────────────────────────────────────────────────────────────────────┤
│ 3. Volatile Tier (Dynamic Turn Input):                                 │
│    • Current event batch (Git diffs, PR metadata)                      │
│    • Immediate curation objective                                      │
└────────────────────────────────────────────────────────────────────────┘
```

### Key Horizon Patterns Adopted

1. **Three-Tier Prompt Assembly**:
   - Isolates invariant schema instructions (Tier 1) from knowledge graph state (Tier 2) and turn-specific event inputs (Tier 3).
   - Enables high cache hit rates when using LLM providers supporting context caching (e.g. Gemini 3.7 Flash).
2. **Context Compaction (`HorizonSummarizer`)**:
   - When a curation session approaches the compaction threshold (e.g. $> 40$ tool turns), the `HorizonSummarizer` compresses completed tool outputs into concise mutation summaries, keeping the context window sharp and focused.
3. **Model-Agnostic Routing (`DispatchingLlm`)**:
   - The agent interfaces with a `DispatchingLlm` abstraction. While Gemini 3.7 Flash is the default model for speed, reasoning, and large context windows, the harness can route sub-tasks to any model provider without code modifications.

## Consequences

### Positive
* **High Reasoning Precision**: Strict prompt tiers prevent the model from forgetting OKF schema requirements mid-run.
* **Cost Efficiency**: Minimizes token waste through aggressive context caching and compaction.
* **Model Agnostic**: Fully decoupled from any single vendor SDK.

### Negative / Trade-offs
* **Implementation Complexity**: Requires prompt assembling pipelines and token counting hooks before each LLM turn.
