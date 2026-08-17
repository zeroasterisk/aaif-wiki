# ADR-007: Pluggable Exporters & Privacy Boundary Guardrails

## Status
**Accepted**

## Context
`zeroasterisk/aaif-wiki` is designed as an open-source, vendor-neutral project. However, the operational environment where it executes may have access to internal enterprise tools, private proxies, or local testing harnesses.

Furthermore, different consumers require different output artifacts:
- Public GitHub Gists for dated bi-weekly executive digests.
- Interactive static web graphs for GitHub Pages visualizers.
- Local chat or email dispatches.

We must establish a **strict privacy boundary** to prevent internal infrastructure, corporate paths, or unreleased private APIs (such as private MCP proxy blades) from leaking into the public repository or exported artifacts.

## Decision
We implement a **Pluggable Exporter Interface** with strict privacy boundary validation.

```
       ┌───────────────────────────────────────────────────────────┐
       │             Canonical OKF v0.2 Knowledge Bundle           │
       │                   (/wiki/*.md in Git)                     │
       └─────────────────────────────┬─────────────────────────────┘
                                     │
                                     ▼
       ┌───────────────────────────────────────────────────────────┐
       │                 BaseExporter Interface                    │
       │      validate_privacy() ──► sanitize() ──► export()       │
       └──────┬──────────────────────┬──────────────────────┬──────┘
              │                      │                      │
              ▼                      ▼                      ▼
       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
       │ GistExporter │       │VisualizerExp.│       │Custom Plugins│
       │ (Public Gist)│       │(GitHub Pages)│       │ (Local Only) │
       └──────────────┘       └──────────────┘       └──────────────┘
```

### 1. Privacy Boundary Laws
1. **Zero Corporate Secrets or Paths in Repo**:
   - The repository MUST NOT contain corporate file paths (e.g. `/google/bin/...`), internal hostnames, or private MCP blade designations.
   - Any local-only enterprise integrations MUST reside outside the git tree or be loaded dynamically via local environment variables.
2. **Deterministic URL Normalization**:
   - All internal citations in generated reports and gists MUST be normalized to public GitHub URLs (`https://github.com/aaif/...`). Local file URIs (`file:///...`) are strictly stripped during export.
3. **Automated Leak Guard (Pre-Commit / Pre-Export)**:
   - Every exporter runs a deterministic regex audit checking for private tokens, internal domains, and local filesystem paths before publishing any artifact.

### 2. Supported Public Exporters
* **`GistExporter` (`aaif_wiki/exporters/gist.py`)**:
  - Compiles the bi-weekly delta from `wiki/log.md` into a structured executive briefing.
  - Publishes a dated public GitHub Gist via `gh` CLI or GitHub API.
* **`VisualizerExporter` (`aaif_wiki/exporters/visualizer.py`)**:
  - Compiles `wiki/graph.json` containing node metadata and directional wikilink edges.
  - Bundles the static D3/HTML visualizer for deployment to GitHub Pages.

## Consequences

### Positive
* **Safe Open-Source Collaboration**: Clean boundary guarantees zero accidental leaks of private developer environments or internal tooling.
* **Extensible Output Channels**: New export targets (e.g. Discord webhooks, Slack bots, static site generators) can be added by implementing `BaseExporter`.

### Negative / Trade-offs
* **Strict Sanitization Overhead**: Requires automated sanitization passes before publishing any public document.
