"""
policy_evolution/updater.py

Phase 3.3 — PolicyUpdater (Dry Run)

Generates explainable policy recommendations
based on evolution signals.

NO automatic policy application occurs here.
"""

from typing import Set

from policy_evolution.versioning import PolicyVersion
from policy_evolution.recommendation import PolicyRecommendation
from policy_evolution.signals import EvolutionSignal


class PolicyUpdater:
    """
    Proposes bounded policy adjustments
    based on governance evolution signals.
    """

    def __init__(self, current_policy: PolicyVersion):
        self.current_policy = current_policy

    def propose_update(
        self,
        signals: Set[EvolutionSignal],
    ) -> PolicyRecommendation | None:
        """
        Return a policy recommendation if adjustment is warranted.
        Returns None if no change is advised.
        """

        params = dict(self.current_policy.parameters)
        rationale_parts = []
        triggered = []

        # -----------------------------
        # Signal-driven adjustments
        # -----------------------------

        if EvolutionSignal.ALARM_FATIGUE in signals:
            params["alarm_strictness"] = max(
                0.1, params.get("alarm_strictness", 0.5) - 0.1
            )
            rationale_parts.append("Reduce alarm strictness to mitigate fatigue")
            triggered.append(EvolutionSignal.ALARM_FATIGUE.value)

        if EvolutionSignal.TRUST_COLLAPSE in signals:
            params["support_weight"] = min(
                1.0, params.get("support_weight", 0.5) + 0.1
            )
            rationale_parts.append("Increase support emphasis to rebuild trust")
            triggered.append(EvolutionSignal.TRUST_COLLAPSE.value)

        if EvolutionSignal.OVER_ENFORCEMENT in signals:
            params["enforcement_weight"] = max(
                0.0, params.get("enforcement_weight", 0.4) - 0.1
            )
            rationale_parts.append("Decrease enforcement to avoid burnout")
            triggered.append(EvolutionSignal.OVER_ENFORCEMENT.value)

        if EvolutionSignal.UNDER_ENFORCEMENT in signals:
            params["enforcement_weight"] = min(
                1.0, params.get("enforcement_weight", 0.4) + 0.1
            )
            rationale_parts.append("Increase enforcement to restore compliance")
            triggered.append(EvolutionSignal.UNDER_ENFORCEMENT.value)

        # -----------------------------
        # Final decision
        # -----------------------------

        if not rationale_parts:
            return None  # No recommendation needed

        return PolicyRecommendation(
            suggested_parameters=params,
            rationale="; ".join(rationale_parts),
            triggering_signals=triggered,
        )
