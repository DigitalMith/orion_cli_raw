"""General-purpose utilities for the Orion CLI."""

from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """Create a directory if it does not exist and return the path."""

    path.mkdir(parents=True, exist_ok=True)
    return path


__all__ = ["ensure_directory"]
