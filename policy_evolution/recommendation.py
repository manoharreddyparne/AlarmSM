"""
policy_evolution/recommendation.py

Phase 3.3 — Policy Recommendation Model

Defines explainable, bounded policy recommendations
derived from evolution signals.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class PolicyRecommendation:
    """
    Non-binding recommendation for policy adjustment.
    """

    suggested_parameters: Dict[str, float]
    rationale: str
    triggering_signals: List[str]
