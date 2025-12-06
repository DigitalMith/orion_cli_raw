"""Convenience helpers for configuration management."""

from pathlib import Path
from typing import Optional

from orion_cli.settings.config_loader import OrionConfig, load_config as _load_config


def load_config(path: Optional[Path] = None) -> OrionConfig:
    """Load Orion configuration, defaulting to the packaged config."""

    return _load_config(path)


__all__ = ["load_config", "OrionConfig"]
