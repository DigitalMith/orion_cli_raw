"""Configuration loading utilities for the Orion CLI."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, Field

_DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "default_config.yaml"


class OrionConfig(BaseModel):
    """Minimal configuration model for Orion CLI defaults."""

    workspace_dir: Path = Field(default=Path("workspace"), description="Root workspace directory for user data.")
    embeddings_dir: Path = Field(
        default=Path("models/embeddings"), description="Directory for local embedding model artifacts."
    )
    persona_template: Path = Field(
        default=Path("orion_cli/data/persona_template.yaml"), description="Path to the packaged persona template."
    )
    identity_template: Path = Field(
        default=Path("orion_cli/data/identity_template.yaml"), description="Path to the packaged identity template."
    )


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        content = yaml.safe_load(handle) or {}
    if not isinstance(content, dict):
        raise ValueError(f"Configuration file {path} must contain a mapping at the top level.")
    return content


def load_config(path: Optional[Path] = None) -> OrionConfig:
    """Load configuration from YAML, merging with defaults."""

    config_path = path or _DEFAULT_CONFIG_PATH
    raw_data = _load_yaml(config_path)
    return OrionConfig.model_validate(raw_data)


__all__ = ["OrionConfig", "load_config"]
