"""
context.py

Context-based governance guard.

Adjusts strategy selection on low-stakes days
without undermining safety or long-term discipline.
"""

from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def context_guard_policy(state: BehavioralState) -> Strategy | None:
    """
    Context guard rules.

    Returns STABILIZATION when contextual cost is low
    and there is no immediate risk requiring intervention.
    """

    # -------------------------------------------------
    # Low-stakes context + stable condition
    # -------------------------------------------------
    if (
        state.context_importance <= 0.4
        and state.failure_risk <= 0.5
        and state.fatigue_index <= 0.6
        and state.avoidance_tendency <= 0.5
    ):
        return Strategy.STABILIZATION

    return None
