"""Workspace-aware path resolution helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from orion_cli.shared.utils import ensure_directory
from orion_cli.settings.config_loader import OrionConfig


class OrionPaths:
    """Resolve common directories used by the Orion CLI."""

    def __init__(self, config: Optional[OrionConfig] = None):
        self.config = config or OrionConfig()
        self.workspace_root = Path(self.config.workspace_dir).expanduser()
        self.embeddings_root = Path(self.config.embeddings_dir).expanduser()

    @property
    def chroma_dir(self) -> Path:
        """Directory for ChromaDB collections within the workspace."""

        return self.workspace_root / "chroma"

    def ensure_workspace(self) -> None:
        """Ensure workspace-related directories exist."""

        ensure_directory(self.workspace_root)
        ensure_directory(self.embeddings_root)
        ensure_directory(self.chroma_dir)

    def path_summary(self) -> dict[str, Path]:
        """Return a mapping of key path labels to resolved paths."""

        return {
            "workspace": self.workspace_root.resolve(),
            "embeddings": self.embeddings_root.resolve(),
            "chroma": self.chroma_dir.resolve(),
        }


__all__ = ["OrionPaths"]
