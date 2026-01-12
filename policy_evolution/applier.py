"""
policy_evolution/applier.py

Phase 3.4 — Policy Version Applier (Offline)

Creates new immutable policy versions from
policy recommendations.

NO automatic deployment occurs here.
"""

from policy_evolution.versioning import PolicyVersion
from policy_evolution.recommendation import PolicyRecommendation


class PolicyVersionApplier:
    """
    Applies a policy recommendation by producing
    a new PolicyVersion (offline).
    """

    def apply(
        self,
        current: PolicyVersion,
        recommendation: PolicyRecommendation,
    ) -> PolicyVersion:
        """
        Return a NEW policy version reflecting
        the recommendation.
        """

        return PolicyVersion(
            parameters=recommendation.suggested_parameters,
            reason=(
                "Evolved from version "
                f"{current.version_id}: {recommendation.rationale}"
            ),
        )
