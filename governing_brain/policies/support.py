from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def early_support_policy(state: BehavioralState) -> Strategy | None:
    """
    Early intervention support rules.
    """

    # Moderate risk + moderate fatigue
    if state.failure_risk >= 0.55 and state.fatigue_index >= 0.5:
        return Strategy.SUPPORT

    # Negative momentum + rising fatigue
    if state.momentum_trend <= -0.2 and state.fatigue_index >= 0.5:
        return Strategy.SUPPORT

    return None
