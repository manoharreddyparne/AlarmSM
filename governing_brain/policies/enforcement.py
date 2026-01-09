"""
enforcement.py

Context-aware enforcement policy.

Applies strict strategies when intentional avoidance
is detected and the user has sufficient capacity
to comply.
"""

from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def enforcement_policy(state: BehavioralState) -> Strategy | None:
    """
    Enforcement rules.

    Triggers ENFORCEMENT when avoidance is high,
    capacity exists, and context justifies firmness.
    """

    if (
        state.avoidance_tendency >= 0.65          # Intentional resistance
        and state.context_importance >= 0.6       # High-stakes context
        and state.fatigue_index <= 0.45           # Sufficient capacity
        and state.discipline_level >= 0.4         # Enforcement can still work
        and state.momentum_trend >= -0.15         # Not in a downward spiral
        and state.failure_risk >= 0.4             # Pattern of risk exists
    ):
        return Strategy.ENFORCEMENT

    return None
