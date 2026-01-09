from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


def context_guard_policy(state: BehavioralState) -> Strategy | None:
    """
    Context-based enforcement guard.
    """

    # Low-importance day guard
    if state.context_importance <= 0.4:
        return Strategy.STABILIZATION

    return None
