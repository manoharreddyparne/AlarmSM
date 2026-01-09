"""
inputs.py

Defines normalized behavioral signal schemas
consumed by the Governing Brain.

This module contains no decision logic.
It enforces input validity and normalization.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List


# =========================================================
# Signal Definition
# =========================================================

@dataclass(frozen=True)
class Signal:
    """
    Represents a normalized behavioral signal
    consumed by the Governing Brain.
    """

    name: str
    value: float
    confidence: float
    timestamp: datetime
    source: Optional[str] = None

    def __post_init__(self):
        # Normalize and validate name
        normalized_name = self.name.strip().lower()
        if not normalized_name:
            raise ValueError("Signal name must be a non-empty string")

        object.__setattr__(self, "name", normalized_name)

        # Validate confidence
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                f"Signal confidence must be in [0.0, 1.0], got {self.confidence}"
            )

        # Value is domain-specific but must be finite
        if not isinstance(self.value, (int, float)):
            raise ValueError("Signal value must be numeric")


# =========================================================
# Signal Batch Definition
# =========================================================

@dataclass(frozen=True)
class SignalBatch:
    """
    Represents a collection of behavioral signals
    observed over a decision window.
    """

    signals: List[Signal] = field(default_factory=list)
    window_start: datetime = field(default_factory=datetime.utcnow)
    window_end: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if self.window_start > self.window_end:
            raise ValueError("SignalBatch window_start must be <= window_end")

        for signal in self.signals:
            if not (self.window_start <= signal.timestamp <= self.window_end):
                raise ValueError(
                    f"Signal timestamp {signal.timestamp} "
                    f"outside batch window [{self.window_start}, {self.window_end}]"
                )
