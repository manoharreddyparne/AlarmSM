from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def enforcement_policy(state: BehavioralState) -> Strategy | None:
    """
    Context-aware enforcement rules.
    """

    if (
        state.avoidance_tendency >= 0.7
        and state.context_importance >= 0.6
        and state.fatigue_index <= 0.4
        and state.momentum_trend >= -0.1
    ):
        return Strategy.ENFORCEMENT

    return None
