"""
support.py

Early intervention support policy.

Provides supportive strategies for users showing
strain but not full burnout. Designed to prevent
collapse without enabling avoidance.
"""

from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def early_support_policy(state: BehavioralState) -> Strategy | None:
    """
    Early support rules.

    Triggers SUPPORT when strain is detected,
    discipline is still present, and avoidance
    has not become dominant.
    """

    # -------------------------------------------------
    # 1. Moderate risk + moderate fatigue (pre-burnout)
    # -------------------------------------------------
    if (
        0.45 <= state.failure_risk < 0.6
        and 0.45 <= state.fatigue_index < 0.6
        and state.discipline_level >= 0.4
        and state.avoidance_tendency <= 0.5
    ):
        return Strategy.SUPPORT

    # -------------------------------------------------
    # 2. Negative momentum with recoverable capacity
    # -------------------------------------------------
    if (
        state.momentum_trend <= -0.2
        and state.fatigue_index >= 0.45
        and state.discipline_level >= 0.35
        and state.avoidance_tendency <= 0.5
    ):
        return Strategy.SUPPORT

    return None
