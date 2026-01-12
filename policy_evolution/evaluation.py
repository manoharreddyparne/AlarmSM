"""
policy_evolution/evaluation.py

Defines the immutable data model representing
governance performance over a time window.

Phase: 3.1 (Read-only policy evaluation)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyEvaluation:
    """
    Aggregate evaluation of governance behavior
    over a simulation window.
    """

    # Evaluation window
    window_days: int

    # Core effectiveness
    alarm_trigger_rate: float
    success_rate: float
    false_alarm_rate: float

    # Human impact
    trust_delta: float
    fatigue_delta: float

    # Strategy usage ratios
    enforcement_ratio: float
    support_ratio: float
    stabilization_ratio: float

    # Overall verdict
    governance_health: str  # "healthy", "risky", "degrading"
