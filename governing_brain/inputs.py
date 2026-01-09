"""
inputs.py

Defines normalized behavioral signal schemas
consumed by the Governing Brain.

This module contains no decision logic.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from typing import List

@dataclass
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
@dataclass
class SignalBatch:
    """
    Represents a collection of behavioral signals
    observed over a decision window.
    """

    signals: List[Signal]
    window_start: datetime
    window_end: datetime
