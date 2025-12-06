"""Core long-term memory helpers (placeholder implementations)."""

from __future__ import annotations

from typing import Any, List


class MemoryStore:
    """Stub representing a long-term memory store."""

    def __init__(self) -> None:
        self._store: list[Any] = []

    def add(self, item: Any) -> None:  # pragma: no cover - placeholder
        """Add an item to the memory store (not implemented)."""

        self._store.append(item)

    def search(self, query: str) -> List[Any]:  # pragma: no cover - placeholder
        """Search memory for relevant items (not implemented)."""

        return []


__all__ = ["MemoryStore"]
