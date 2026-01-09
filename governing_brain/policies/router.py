"""
router.py

Routes behavioral state through governance policies
and selects a strategy based on explicit priority order.

Design principles:
- Deterministic
- Auditable
- Priority-driven
- First-match-wins
"""

from typing import Callable, Iterable, Optional, Tuple

from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy

from governing_brain.policies.burnout import burnout_policy
from governing_brain.policies.support import early_support_policy
from governing_brain.policies.context import context_guard_policy
from governing_brain.policies.enforcement import enforcement_policy


# =========================================================
# Policy Contract
# =========================================================

PolicyFn = Callable[[BehavioralState], Optional[Strategy]]


# =========================================================
# Explicit Policy Priority Order
# (Higher = evaluated earlier)
# =========================================================

POLICY_PIPELINE: Tuple[PolicyFn, ...] = (
    burnout_policy,        # Human safety override
    early_support_policy,  # Burnout prevention
    context_guard_policy,  # Situational cost protection
    enforcement_policy,    # Discipline enforcement
)


# =========================================================
# Strategy Router
# =========================================================

def select_strategy(state: BehavioralState) -> Strategy:
    """
    Evaluates governance policies in explicit priority order
    and returns the first applicable strategy.

    Fallback strategy is STABILIZATION.
    """

    for policy in POLICY_PIPELINE:
        decision = policy(state)

        if decision is not None:
            return decision

    return Strategy.STABILIZATION
