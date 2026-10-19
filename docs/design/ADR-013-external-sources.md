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
   and changelogs stay out). Any `owner/name` not on the list is refused (`UnlistedRepo`), and
   lookup is case-insensitive, so `Coinbase/X402` cannot create a second copy.
2. **Same event store, distinct coordinates.** External events use `repository: owner/name`,
   ids prefixed `evt-ext-<owner>-<name>-<hash6>-` (the hash keeps the lossy slug collision-free),
   and labels `external`, `steward:<org>`, `topic:<t>`. Mirrors live under
   `raw/cache/repos/<owner>/<name>`. AAIF ids are unchanged; `aaif/<name>` resolves to the AAIF repo.
3. **Files only by default, spec first.** PRs and issues are off per source (`include_prs`,
   `include_issues`): other orgs' in-flight debates are not ours to summarise. `include_paths`
   order is priority order, so `file_limit` drops examples and guides, not the normative spec.
   Externals default to Markdown only.
4. **No token outside AAIF.** Clones and REST calls for external repos are anonymous.
5. **Provenance is derived from sources, not asserted.** A page is external if any `sources[]`
   resource is a GitHub repo outside the AAIF org (`aaif_wiki/provenance.py`). On apply:
   - the `external` tag is recomputed from sources, whatever the model returned;
   - an update may not drop a page's whole provenance class, so a single-class rewrite can't turn
     an AAIF page external or strip the steward from an external one (`provenance-overwrite`);
   - in a mixed batch, a mutation without valid `source_event_ids` is dropped, not attributed to
     the whole batch.
   The validator fails any page whose tag disagrees with its sources (`external-tag`). The prompt
   still marks external events `steward: X (EXTERNAL -- not AAIF)` and requires the overview's
   first sentence to name the steward.

## Consequences
- Weekly refresh ingests the allowlist after merge. A full external bootstrap (185 events) cost
  $0.60 (gemini-3.8-flash).
- Stewards change (AP2 moved to FIDO in 2026-04). The `steward` field is hand-maintained and must
  be checked against a primary source when edited.
- Concept links go to `github.com`; the prompt tells the curator to link the GitHub source file
  rather than the steward's site, so the ADR-007 link allowlist is unchanged.
