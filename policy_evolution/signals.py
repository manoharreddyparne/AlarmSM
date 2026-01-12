"""
policy_evolution/signals.py

Defines governance evolution signals derived
from policy evaluation.

Phase:
- 3.1: HEALTH classification
- 3.2: Warning & imbalance signals
"""

from enum import Enum


class EvolutionSignal(Enum):
    # Overall health
    HEALTHY = "healthy"
    RISKY = "risky"
    DEGRADING = "degrading"

    # Specific governance risks
    ALARM_FATIGUE = "alarm_fatigue"
    TRUST_COLLAPSE = "trust_collapse"
    OVER_ENFORCEMENT = "over_enforcement"
    UNDER_ENFORCEMENT = "under_enforcement"
    STRATEGY_STAGNATION = "strategy_stagnation"
