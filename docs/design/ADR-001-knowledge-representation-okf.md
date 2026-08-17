# ADR-001: Knowledge Representation via Open Knowledge Format (OKF v0.2)

## Status
**Accepted**

## Context
The Agentic AI Foundation (AAIF) encompasses 15 repositories, 7 working groups plus 1 cross-group workstream (Taxonomy and Landscape), and dozens of active RFCs and pull requests. Traditional knowledge management approaches (flat document folders, monolithic vector databases, or proprietary notebook silos) suffer from:
1. **Opaque Retrieval**: Black-box vector search cannot distinguish between historical drafts, active proposals, and merged standards.
2. **Context Fragmentation**: Cross-cutting concepts (e.g. Attested Runtime in Security vs. Cross-Boundary Tracing in Observability) lack explicit relationships.
3. **High Maintenance Friction**: Manual documentation quickly becomes stale, while automated dumping produces noise.

We evaluated the [Open Knowledge Format (OKF v0.2)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) introduced by Google Cloud and implemented by projects like `langchain-ai/openwiki`.

## Decision
We adopt **Open Knowledge Format (OKF v0.2)** as the canonical knowledge representation standard for the entire AAIF wiki (`wiki/`).

### Specification Constraints
1. **Bundle Structure**:
   ```
   wiki/
   ├── index.md                 # Root directory and taxonomy index
   ├── log.md                   # Chronological update changelog
   ├── working-groups/          # Working Group concept pages
   ├── architectures/           # Reference architectures and RFC concepts
   ├── taxonomy/                # Consensus terms and definitions
   └── graph.json               # Pre-compiled node/edge graph
   ```
2. **Frontmatter Schema**:
   Every concept document MUST contain a YAML frontmatter block:
   ```yaml
   ---
   type: <Concept Type>          # e.g., Working Group, Architecture Pattern, RFC, Glossary Term
   title: <Display Title>
   description: <One-line functional summary>
   resource: <Canonical URI or GitHub URL>
   tags: [<tag1>, <tag2>]
   generated:
     by: <agent_id_and_model>    # e.g. aaif-wiki-curator/gemini-3.7-flash
     at: <ISO-8601 Timestamp>
   sources:
     - id: <source_id>
       resource: <source_url_or_commit_sha>
   ---
   ```
3. **Explicit Graph Linking**:
   Relationships between concepts are declared via **true relative** Markdown links:
   `[Attested Isolated Runtime](../architectures/attested-isolated-runtime.md)`.
   Root-absolute links (`/architectures/...`) are forbidden: they resolve incorrectly on
   GitHub Pages project sub-paths, in Obsidian, and in any nested-bundle consumer.
   These links form the edges of the compiled graph.

   > Note: OKF v0.2 has **no typed-relationship field** (typed edges remain an open upstream
   > proposal). Any edge typing emitted by this project is a producer extension and MUST be
   > namespaced so downstream consumers do not mistake it for standard OKF.
4. **Body Structure**:
   Documents use conventional headings (`# Overview`, `# Architecture / Specification`, `# Lifecycle History`, `# References`).

## Consequences

### Positive
* **Human & Agent Readable**: Zero proprietary database binaries; fully inspectable via `cat`, `git diff`, and standard Markdown previewers.
* **Portable**: Compatible with Obsidian, static site generators, and OpenWiki visualizer tooling.
* **Audit Trail**: Every concept explicitly lists its generating agent, timestamp, and source Git commits in its frontmatter.

### Negative / Trade-offs
* **Strict Frontmatter Linting**: Requires an automated parser/validator activity to reject invalid YAML or broken relative links.
