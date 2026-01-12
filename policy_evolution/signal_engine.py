"""
policy_evolution/signal_engine.py

Phase 3.2 — Evolution Signal Engine

Translates policy evaluation metrics into
high-level evolution signals.

NO policy mutation occurs here.
"""

from typing import Set

from policy_evolution.evaluation import PolicyEvaluation
from policy_evolution.signals import EvolutionSignal


class EvolutionSignalEngine:
    """
    Derives governance evolution signals from
    policy evaluation results.
    """

    def derive(self, evaluation: PolicyEvaluation) -> Set[EvolutionSignal]:
        signals: Set[EvolutionSignal] = set()

        # -----------------------------
        # Primary health classification
        # -----------------------------
        if evaluation.governance_health == "healthy":
            signals.add(EvolutionSignal.HEALTHY)
            return signals  # short-circuit: no warnings

        if evaluation.governance_health == "risky":
            signals.add(EvolutionSignal.RISKY)

        if evaluation.governance_health == "degrading":
            signals.add(EvolutionSignal.DEGRADING)

        # -----------------------------
        # Secondary interpretive signals
        # -----------------------------

        # Alarm fatigue risk
        if evaluation.alarm_trigger_rate > 0.6 and evaluation.false_alarm_rate > 0.25:
            signals.add(EvolutionSignal.ALARM_FATIGUE)

        # Trust collapse
        if evaluation.trust_delta < 0:
            signals.add(EvolutionSignal.TRUST_COLLAPSE)

        # Enforcement imbalance
        if evaluation.enforcement_ratio > 0.6:
            signals.add(EvolutionSignal.OVER_ENFORCEMENT)

        if evaluation.enforcement_ratio < 0.1 and evaluation.failure_risk > 0.7:
            signals.add(EvolutionSignal.UNDER_ENFORCEMENT)

        # Strategy stagnation
        if (
            evaluation.support_ratio > 0.8
            or evaluation.stabilization_ratio > 0.8
            or evaluation.enforcement_ratio > 0.8
        ):
            signals.add(EvolutionSignal.STRATEGY_STAGNATION)

        return signals
