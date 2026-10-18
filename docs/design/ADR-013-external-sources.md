# ADR-013: External (Non-AAIF) Sources on Adjacent Topics

## Status
**Proposed** (2026-10-18), feature branch `feat/external-sources`.

## Context
AAIF's working groups (agentic commerce, identity and trust, discovery) overlap with standards
governed elsewhere: AP2 (FIDO Alliance), UCP (its own Governing Council), ACP (OpenAI and Stripe),
x402 (x402 Foundation, Linux Foundation), AI Catalog (Agent Card WG, Linux Foundation), and
independent landscape maps such as `frmoretto/agentic-standards-map`. A reader of an AAIF commerce
page needs that context. Before this ADR the connector could only read the `aaif` org.

The risk is the one ADR-010 exists for: an AAIF-branded wiki that presents another body's work as
AAIF's.

## Decision
1. **Explicit allowlist, never discovery.** `sources.github.external` in `config.yaml` lists
   `owner/name` repos. Each entry names a `steward`, `topics`, and `include_paths` (CLAs, examples
   and changelogs stay out).
2. **Same event store, distinct coordinates.** External events use `repository: owner/name`,
   ids prefixed `evt-ext-<owner>-<name>-`, and labels `external`, `steward:<org>`, `topic:<t>`.
   Mirrors live under `raw/cache/repos/<owner>/<name>`. AAIF ids are unchanged.
3. **Files only by default.** PRs and issues are off per source (`include_prs`, `include_issues`):
   other orgs' in-flight debates are not ours to summarise.
4. **Anonymous clone.** The AAIF sources token is never sent to non-AAIF repos.
5. **Attribution is enforced in two places.** The prompt marks every external event
   `steward: X (EXTERNAL -- not AAIF)` and requires the overview's first sentence to name the
   steward. The curator adds the `external` tag server-side, whatever the model returns.

## Consequences
- Weekly refresh ingests the allowlist after merge; bootstrap cost measured at about $0.01 per
  batch of three events (gemini-3.8-flash).
- Stewards change (AP2 moved to FIDO in 2026-04). The `steward` field is hand-maintained and must
  be checked against a primary source when edited.
- Concept links still go to `github.com`, so the ADR-007 link allowlist is unchanged.
