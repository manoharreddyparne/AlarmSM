"""
policy_evolution/signals.py

Defines high-level governance condition signals
derived from policy evaluation.

Phase: 3.1 (Classification only)
"""

from enum import Enum


class EvolutionSignal(Enum):
    """
    High-level signals describing the current
    state of governance health.
    """

    HEALTHY = "healthy"
    RISKY = "risky"
    DEGRADING = "degrading"
