from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def burnout_policy(state: BehavioralState) -> Strategy | None:
    """
    Highest-priority burnout protection rules.
    """

    # High failure risk + high fatigue
    if state.failure_risk >= 0.6 and state.fatigue_index >= 0.6:
        return Strategy.SUPPORT

    return None
