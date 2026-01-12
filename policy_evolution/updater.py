"""
policy_evolution/updater.py

Phase 3 — Policy Evolution (future work)

This module defines the interface for proposing
policy updates based on governance evaluation.

NOTE:
- No policy mutation occurs in Phase 3.1
- This remains a stub until Phase 3.3
"""

from policy_evolution.evaluation import PolicyEvaluation
from policy_evolution.versioning import PolicyVersion


class PolicyUpdater:
    """
    Proposes bounded policy adjustments
    based on evaluation outcomes.

    This class is intentionally inactive
    during Phase 3.1.
    """

    def __init__(self, current_policy: PolicyVersion):
        self.current_policy = current_policy

    def propose_update(self, evaluation: PolicyEvaluation) -> PolicyVersion:
        """
        Return a NEW policy version with small,
        explainable adjustments.

        Phase 3.1: Not implemented by design.
        """
        raise NotImplementedError(
            "PolicyUpdater is inactive in Phase 3.1 (evaluation-only phase)"
        )
