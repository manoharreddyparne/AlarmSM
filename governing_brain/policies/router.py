from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy

from governing_brain.policies.burnout import burnout_policy
from governing_brain.policies.support import early_support_policy
from governing_brain.policies.context import context_guard_policy
from governing_brain.policies.enforcement import enforcement_policy


def select_strategy(state: BehavioralState) -> Strategy:
    """
    Routes policy evaluation in strict priority order.
    """

    for policy in (
        burnout_policy,
        early_support_policy,
        context_guard_policy,
        enforcement_policy,
    ):
        decision = policy(state)
        if decision is not None:
            return decision

    return Strategy.STABILIZATION
