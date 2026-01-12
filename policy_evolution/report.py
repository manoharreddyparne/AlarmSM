"""
policy_evolution/report.py

Phase 4.1 — Policy Evolution Report Generator

Produces a human-readable summary of:
- Governance evaluation
- Evolution signals
- Policy recommendations
- Proposed policy versions
"""

from typing import List, Optional

from policy_evolution.evaluation import PolicyEvaluation
from policy_evolution.signals import EvolutionSignal
from policy_evolution.recommendation import PolicyRecommendation
from policy_evolution.versioning import PolicyVersion


class PolicyEvolutionReport:
    """
    Generates a structured, human-readable report
    describing the system's governance reasoning.
    """

    def generate(
        self,
        evaluation: PolicyEvaluation,
        signals: List[EvolutionSignal],
        recommendation: Optional[PolicyRecommendation],
        proposed_version: Optional[PolicyVersion],
    ) -> str:
        lines: List[str] = []

        # -----------------------------
        # Header
        # -----------------------------
        lines.append("=" * 80)
        lines.append("AlarmSM — Policy Evolution Report")
        lines.append("=" * 80)
        lines.append("")

        # -----------------------------
        # Evaluation Summary
        # -----------------------------
        lines.append("1. Governance Evaluation")
        lines.append("-" * 40)
        lines.append(f"Window (days)        : {evaluation.window_days}")
        lines.append(f"Governance Health    : {evaluation.governance_health}")
        lines.append(f"Alarm Trigger Rate   : {evaluation.alarm_trigger_rate:.2f}")
        lines.append(f"Success Rate         : {evaluation.success_rate:.2f}")
        lines.append(f"False Alarm Rate     : {evaluation.false_alarm_rate:.2f}")
        lines.append(f"Trust Delta          : {evaluation.trust_delta:.2f}")
        lines.append(f"Fatigue Delta        : {evaluation.fatigue_delta:.2f}")
        lines.append("")

        # -----------------------------
        # Evolution Signals
        # -----------------------------
        lines.append("2. Evolution Signals")
        lines.append("-" * 40)

        if signals:
            for s in signals:
                lines.append(f"- {s.value}")
        else:
            lines.append("No evolution signals detected.")

        lines.append("")

        # -----------------------------
        # Recommendation
        # -----------------------------
        lines.append("3. Policy Recommendation")
        lines.append("-" * 40)

        if recommendation:
            lines.append("Rationale:")
            lines.append(f"  {recommendation.rationale}")
            lines.append("")
            lines.append("Suggested Parameter Changes:")
            for k, v in recommendation.suggested_parameters.items():
                lines.append(f"  - {k}: {v}")
        else:
            lines.append("No policy change recommended.")

        lines.append("")

        # -----------------------------
        # Proposed Policy Version
        # -----------------------------
        lines.append("4. Proposed Policy Version")
        lines.append("-" * 40)

        if proposed_version:
            lines.append(f"Version ID : {proposed_version.version_id}")
            lines.append(f"Reason     : {proposed_version.reason}")
        else:
            lines.append("No new policy version generated.")

        lines.append("")
        lines.append("=" * 80)
        lines.append("End of Report")
        lines.append("=" * 80)

        return "\n".join(lines)
