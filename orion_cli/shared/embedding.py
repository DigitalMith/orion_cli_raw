"""Embedding abstraction placeholders for Orion CLI."""

from __future__ import annotations

from typing import Iterable, List


class EmbeddingBackend:
    """Abstract interface for embedding models."""

    model_name: str = "jina-embeddings-v2"

    def embed_texts(self, texts: Iterable[str]) -> List[list[float]]:  # pragma: no cover - placeholder
        """Return embeddings for provided texts (not implemented)."""

        raise NotImplementedError("Embedding backend is not yet implemented.")


__all__ = ["EmbeddingBackend"]
