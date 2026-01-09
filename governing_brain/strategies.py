"""
strategies.py

Defines high-level governance strategies
selectable by the Governing Brain.

Strategies are immutable and self-describing.
"""

from enum import Enum


class Strategy(Enum):
    """
    High-level governance strategies.
    """

    ENFORCEMENT = "enforcement"
    COMPENSATION = "compensation"
    STABILIZATION = "stabilization"
    SUPPORT = "support"
    STRATEGIC_PAUSE = "strategic_pause"

    # -------------------------------------------------
    # Semantic helpers (no logic, only meaning)
    # -------------------------------------------------

    @property
    def is_restrictive(self) -> bool:
        return self in {Strategy.ENFORCEMENT}

    @property
    def is_supportive(self) -> bool:
        return self in {Strategy.SUPPORT, Strategy.COMPENSATION}

    @property
    def is_neutral(self) -> bool:
        return self in {Strategy.STABILIZATION}

    @property
    def allows_recovery(self) -> bool:
        return self in {
            Strategy.SUPPORT,
            Strategy.COMPENSATION,
            Strategy.STRATEGIC_PAUSE,
        }
