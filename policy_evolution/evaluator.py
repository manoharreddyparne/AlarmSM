"""
policy_evolution/evaluator.py

Phase 3.1 — Policy Evaluation Engine

Computes governance health metrics from
Phase 2 simulation logs.

This module is READ-ONLY:
- No policy mutation
- No side effects
"""

from typing import List
from collections import Counter

from simulation.metrics import SimulationLog
from policy_evolution.evaluation import PolicyEvaluation
from governing_brain.strategies import Strategy


class PolicyEvaluator:
    """
    Evaluates governance performance over a window
    of simulation logs.
    """

    def __init__(self, logs: List[SimulationLog]):
        if not logs:
            raise ValueError("PolicyEvaluator requires non-empty logs")
        self.logs = logs

    def evaluate(self) -> PolicyEvaluation:
        days = len(self.logs)

        # -----------------------------
        # Alarm & outcome statistics
        # -----------------------------
        total_alarms = sum(1 for log in self.logs if log.alarm_triggered)
        successful_outcomes = sum(
            1 for log in self.logs
            if log.alarm_triggered and log.outcome_success is True
        )
        false_alarms = sum(
            1 for log in self.logs
            if log.alarm_triggered and log.outcome_success is False
        )

        alarm_trigger_rate = total_alarms / days
        success_rate = (
            successful_outcomes / total_alarms
            if total_alarms > 0 else 0.0
        )
        false_alarm_rate = (
            false_alarms / total_alarms
            if total_alarms > 0 else 0.0
        )

        # -----------------------------
        # Human impact
        # -----------------------------
        trust_delta = sum(log.trust_delta for log in self.logs)
        fatigue_delta = self.logs[-1].fatigue - self.logs[0].fatigue

        # -----------------------------
        # Strategy usage ratios
        # -----------------------------
        strategies = [log.strategy for log in self.logs]
        counts = Counter(strategies)

        enforcement_ratio = counts.get(Strategy.ENFORCEMENT, 0) / days
        support_ratio = counts.get(Strategy.SUPPORT, 0) / days
        stabilization_ratio = counts.get(Strategy.STABILIZATION, 0) / days

        # -----------------------------
        # Governance health heuristic
        # -----------------------------
        if false_alarm_rate > 0.3:
            governance_health = "risky"
        elif trust_delta < 0:
            governance_health = "degrading"
        else:
            governance_health = "healthy"

        return PolicyEvaluation(
            window_days=days,
            alarm_trigger_rate=alarm_trigger_rate,
            success_rate=success_rate,
            false_alarm_rate=false_alarm_rate,
            trust_delta=trust_delta,
            fatigue_delta=fatigue_delta,
            enforcement_ratio=enforcement_ratio,
            support_ratio=support_ratio,
            stabilization_ratio=stabilization_ratio,
            governance_health=governance_health,
        )
