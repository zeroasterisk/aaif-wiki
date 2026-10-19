"""Page provenance (ADR-013): which sources are AAIF and which are external.

One definition, used by the apply gate, the tag normaliser and the validator, so
the three can't disagree. Provenance is read from the source's GitHub URL owner,
not from the event-id prefix: an AAIF repo could legitimately be named ``ext-*``.
"""

from __future__ import annotations

from urllib.parse import urlparse

from .models import Concept, ConceptSource

AAIF_ORG = "aaif"
EXTERNAL_TAG = "external"


def source_is_external(src: ConceptSource, org: str = AAIF_ORG) -> bool:
    url = urlparse(src.resource or "")
    if url.hostname in ("github.com", "www.github.com"):
        owner = url.path.strip("/").split("/", 1)[0].lower()
        return bool(owner) and owner != org.lower()
    # Non-GitHub or missing resource: fall back to the connector's id coordinate.
    return src.id.startswith("evt-ext-")


def classes(concept: Concept | None, org: str = AAIF_ORG) -> set[str]:
    """The provenance classes ("aaif", "external") present in a page's sources."""
    if concept is None:
        return set()
    return {"external" if source_is_external(s, org) else "aaif" for s in concept.sources}


def dropped_classes(existing: Concept | None, new: Concept | None, org: str = AAIF_ORG) -> set[str]:
    """Classes an update would erase. Updates replace sources wholesale, so a
    single-class rewrite of a page would silently flip its provenance: an AAIF
    page restated in another body's words, or an external standard losing its
    steward citation. Mixed rewrites keep both and are allowed."""
    if existing is None or new is None:
        return set()
    return classes(existing, org) - classes(new, org)


def normalise_tags(concept: Concept, org: str = AAIF_ORG) -> None:
    """Make the ``external`` tag exactly mirror the sources, whatever the model wrote."""
    tags = [t for t in concept.tags if t != EXTERNAL_TAG]
    if "external" in classes(concept, org):
        tags = [EXTERNAL_TAG, *tags]
    concept.tags = tags[:8]
