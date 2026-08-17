"""Immutable event store and its derived index."""

from .events import EventStore
from .index import EventIndex

__all__ = ["EventStore", "EventIndex"]
