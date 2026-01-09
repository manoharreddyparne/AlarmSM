"""
burnout.py

Highest-priority policy.
Protects the user from cognitive and behavioral burnout.

This policy may override all others.
"""

from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def burnout_policy(state: BehavioralState) -> Strategy | None:
    """
    Burnout protection rules.

    Triggers SUPPORT when sustained overload,
    downward momentum, or stress-induced avoidance
    is detected.
    """

    # -------------------------------------------------
    # 1. Acute overload (classic burnout condition)
    # -------------------------------------------------
    if state.failure_risk >= 0.6 and state.fatigue_index >= 0.6:
        return Strategy.SUPPORT

    # -------------------------------------------------
    # 2. Downward spiral (early burnout)
    # -------------------------------------------------
    if state.fatigue_index >= 0.7 and state.momentum_trend <= -0.3:
        return Strategy.SUPPORT

    # -------------------------------------------------
    # 3. Discipline erosion under fatigue
    # -------------------------------------------------
    if state.discipline_level <= 0.3 and state.fatigue_index >= 0.6:
        return Strategy.SUPPORT

    # -------------------------------------------------
    # 4. Avoidance under load (silent burnout)
    # -------------------------------------------------
    if state.avoidance_tendency >= 0.6 and state.fatigue_index >= 0.5:
        return Strategy.SUPPORT

    return None
