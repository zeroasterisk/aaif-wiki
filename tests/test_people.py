"""Deterministic TC / WG-chair roster (ADR-014)."""

from __future__ import annotations

from datetime import UTC, datetime

from aaif_wiki import people
from aaif_wiki.models import Lifecycle, RawEvent, SourceType
from aaif_wiki.okf import parse_concept, render_concept
from aaif_wiki.validate.checks import validate_concept

NOW = datetime(2026, 10, 19, tzinfo=UTC)

TC_README = """# Technical Committee

## Members

* **Alan Blount [@zeroasterisk](https://github.com/zeroasterisk)** - Google
* **Caitie McCaffrey [TC CO-CHAIR] [@CaitieM20](https://github.com/CaitieM20)** - Microsoft
* **David Soria Parra [TC CHAIR] [@dsp](https://github.com/dsp)** - Anthropic

All founding TC members were appointed by the AAIF Governing Board.

Current term for TC Members is **March 1, 2026 - December 31, 2026**.

## Projects

* **Not A Person [@nobody](https://github.com/nobody)** - Should Not Parse
"""

WG_README = """# Governance, Risk and Regulatory Working Group

## Chairs

* **Chair: Ryan Hagemann (no GitHub)** - IBM
* **Co-Chair: Alper Dedeoğlu [@alperdedeoglu](https://github.com/alperdedeoglu)** - SAP SE
* **Secretary: Someone [@x](https://github.com/x)** - Nowhere

Current term for the Working Group Chairs is **March 1, 2026 - January 31, 2027**.

## Mission

* **Chair: Decoy Person [@decoy](https://github.com/decoy)** - Elsewhere
"""


def _ev(repo: str, ts: datetime = NOW, ref: str = "README.md", labels=None) -> RawEvent:
    return RawEvent(
        event_id=f"evt-{repo.split('/')[-1]}-file-{int(ts.timestamp())}",
        source_type=SourceType.REPO_FILE,
        lifecycle=Lifecycle.MERGED,
        repository=repo,
        reference_id=ref,
        title=ref,
        timestamp=ts,
        url=f"https://github.com/{repo}/blob/abc/{ref}",
        labels=labels or [],
    )


def test_tc_members_roles_and_term():
    g = people.parse_readme("technical-committee", TC_README, _ev("aaif/technical-committee"))
    assert g is not None
    by = {p.name: p for p in g.people}
    assert set(by) == {"Alan Blount", "Caitie McCaffrey", "David Soria Parra"}  # Projects section ignored
    assert by["David Soria Parra"].role == "TC Chair"
    assert by["Caitie McCaffrey"].role == "TC Co-Chair"
    assert by["Alan Blount"] == people.Person("Alan Blount", "Google", "TC Member", "zeroasterisk")
    assert g.term == "March 1, 2026 - December 31, 2026"


def test_wg_chairs_no_github_unicode_and_section_scoping():
    g = people.parse_readme("wg-governance-risk-and-regulatory", WG_README, _ev("aaif/wg-x"))
    assert g is not None
    assert [(p.role, p.name, p.org, p.handle) for p in g.people] == [
        ("Chair", "Ryan Hagemann", "IBM", None),
        ("Co-Chair", "Alper Dedeoğlu", "SAP SE", "alperdedeoglu"),
    ]  # Secretary row and the decoy under ## Mission are not chairs
    assert g.term == "March 1, 2026 - January 31, 2027"


def test_readme_without_roster_section_is_skipped():
    assert people.parse_readme("wg-x", "# WG\n\n## Mission\n\ntext\n", _ev("aaif/wg-x")) is None


def test_latest_readme_wins_and_externals_and_non_roster_repos_ignored():
    old = _ev("aaif/wg-a", datetime(2026, 1, 1, tzinfo=UTC))
    new = _ev("aaif/wg-a", datetime(2026, 9, 1, tzinfo=UTC))
    events = [
        new,
        old,
        _ev("aaif/wg-a", ref="charter.md"),
        _ev("aaif/community-events"),
        _ev("someorg/wg-evil", labels=["external", "steward:X"]),
    ]
    latest = people.latest_readmes(events)
    assert set(latest) == {"wg-a"}
    assert latest["wg-a"].event_id == new.event_id


def test_concept_is_valid_okf_cites_every_source_and_round_trips():
    tc_ev, wg_ev = _ev("aaif/technical-committee"), _ev("aaif/wg-governance-risk-and-regulatory")
    texts = {tc_ev.event_id: TC_README, wg_ev.event_id: WG_README}
    groups, _ = people.collect([tc_ev, wg_ev], lambda e: texts[e.event_id])
    known = {"working-groups/governance-risk-and-regulatory", "governance/technical-committee"}
    c = people.build_concept(groups, known, now=NOW)
    assert c is not None and c.slug == people.SLUG

    issues = validate_concept(
        c,
        known_slugs=known | {people.SLUG},
        known_event_ids={tc_ev.event_id, wg_ev.event_id},
        link_allowlist=["github.com", "aaif.io"],
    )
    assert [i for i in issues if i.severity == "error"] == []
    assert not [i for i in issues if i.check == "link-target"]

    for g in groups:
        assert f"[^{g.event.event_id}]" in c.body
    assert {s.id for s in c.sources} == {tc_ev.event_id, wg_ev.event_id}
    assert "| David Soria Parra | TC Chair | Anthropic |" in c.body
    assert "Ryan Hagemann (IBM) —" in c.body
    assert "Decoy" not in c.body and "Not A Person" not in c.body
    assert c.body.index("David Soria Parra") < c.body.index("Alan Blount")  # chair first

    back = parse_concept(render_concept(c), slug=c.slug)
    assert back.title == c.title and [s.id for s in back.sources] == [s.id for s in c.sources]


def test_unknown_wg_slug_is_not_linked():
    ev = _ev("aaif/wg-governance-risk-and-regulatory")
    c = people.build_concept(people.collect([ev], lambda e: WG_README)[0], known_slugs=set(), now=NOW)
    assert "](../working-groups/" not in c.body


def test_llm_mutation_of_people_page_is_refused(tmp_path, monkeypatch):
    import asyncio

    from aaif_wiki import pipeline
    from aaif_wiki.config import Config
    from aaif_wiki.models import Concept, CurateResult, Mutation

    cfg = Config(root=tmp_path)
    monkeypatch.setattr(pipeline, "get_config", lambda: cfg)
    m = Mutation(
        action="create",
        slug=people.SLUG,
        rationale="x",
        source_event_ids=["e"],
        concept=Concept(type="governance", title="t", description="d", body="# Overview\n\nfake"),
    )
    res = asyncio.run(pipeline.apply_mutations(CurateResult(mutations=[m])))
    assert res.checked == 0
    assert not (cfg.bundle_dir / "governance" / "people.md").exists()
    assert [i.check for i in res.issues] == ["deterministic-page"]


# --- review deleg_c932b394 #1, #5, #6, #7 ---------------------------------------


def _refresh_env(tmp_path, monkeypatch, readmes: dict[str, str]):
    """Real refresh_people over a real EventStore + bundle; READMEs served by rehydrate."""
    from aaif_wiki import pipeline
    from aaif_wiki.config import Config
    from aaif_wiki.store import EventStore

    cfg = Config(root=tmp_path)
    store = EventStore(cfg.events_dir)
    for repo, text in readmes.items():
        ev = _ev(f"aaif/{repo}")
        ev.inline_text = text or None
        store.append(ev)

    class _Conn:
        def __init__(self, *a, **k):
            pass

        def read_pointer(self, ptr):
            return None

    import aaif_wiki.connectors as connectors

    monkeypatch.setattr(connectors, "GitHubConnector", _Conn)
    return pipeline, cfg


def test_refresh_people_is_idempotent(tmp_path, monkeypatch):
    pipeline, cfg = _refresh_env(
        tmp_path, monkeypatch, {"technical-committee": TC_README, "wg-governance-risk-and-regulatory": WG_README}
    )
    first = pipeline.refresh_people(cfg)
    page = (cfg.bundle_dir / "governance" / "people.md").read_text()
    second = pipeline.refresh_people(cfg)
    assert first["written"] is True and second["written"] is False
    assert (cfg.bundle_dir / "governance" / "people.md").read_text() == page


def test_unreadable_readme_keeps_last_roster(tmp_path, monkeypatch):
    pipeline, cfg = _refresh_env(
        tmp_path, monkeypatch, {"technical-committee": TC_README, "wg-governance-risk-and-regulatory": ""}
    )
    out = pipeline.refresh_people(cfg)
    assert out["written"] is False and out["unreadable"] == ["wg-governance-risk-and-regulatory"]
    assert not (cfg.bundle_dir / "governance" / "people.md").exists()


def test_parser_variants_and_unparsed_bullets_are_surfaced():
    text = """# WG

```markdown
## Chairs
* **Chair: Fake Person** - Nowhere
```

## Chairs 👥

* **co-chairs: Bea Two [@bea](https://github.com/bea)** - Org B
+ **Chair: Ann One (no GitHub)** - Org A
* **Vice Chair: Vic Three** - Org C
* Chair: Malformed Row - Org D

### Emeritus

* **Chair: Old Guy** - Past
"""
    g = people.parse_readme("wg-x", text, _ev("aaif/wg-x"))
    assert g is not None
    assert [(p.name, p.role) for p in g.people] == [
        ("Bea Two", "Co-Chair"), ("Ann One", "Chair"), ("Vic Three", "Co-Chair")]
    assert g.unparsed == ["* Chair: Malformed Row - Org D"]


def test_members_section_stops_at_subheading():
    text = TC_README.replace("All founding", "### Emeritus\n\n* **Old Guy [@old](https://github.com/old)** - Past\n\nAll founding")
    g = people.parse_readme("technical-committee", text, _ev("aaif/technical-committee"))
    assert "Old Guy" not in [p.name for p in g.people]


def test_table_cells_are_escaped():
    text = "# WG\n\n## Chairs\n\n* **Chair: Eve** - Acme | [win](https://evil.example)\n"
    ev = _ev("aaif/wg-x")
    c = people.build_concept([people.parse_readme("wg-x", text, ev)], set(), now=NOW)
    row = next(ln for ln in c.body.splitlines() if "Eve" in ln)
    assert "https://evil.example" not in row and "Acme \\| win" in row
