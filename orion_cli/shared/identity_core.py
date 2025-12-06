"""Identity and self-state helpers (placeholder implementations)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class IdentityProfile:
    """Simple identity profile stub."""

    persona_path: Path
    identity_path: Path

    def refresh(self) -> None:  # pragma: no cover - placeholder
        """Reload identity artifacts from disk (not implemented)."""

        # TODO: Implement reload logic when identity lifecycle is defined.
        return None


__all__ = ["IdentityProfile"]
