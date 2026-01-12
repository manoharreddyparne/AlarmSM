"""
synthetic_users.py

Defines synthetic user behavior models for simulation.

Purpose:
- Simulate human responses to governance directives
- Generate realistic signal patterns over time
- Inject controlled variability (not ML)

This module contains NO governance logic.
"""

import random
from typing import Optional, List
from datetime import datetime, timedelta
from dataclasses import dataclass

from governing_brain.inputs import Signal, SignalBatch
from governing_brain.outputs import GovernanceDirective
from governing_brain.state_model import BehavioralState
from governing_brain.strategies import Strategy


# -------------------------------------------------
# Observable reaction contract (ground truth)
# -------------------------------------------------

@dataclass(frozen=True)
class UserReaction:
    """
    Observable outcome of a governance directive.
    This is NOT a decision — it is ground truth.
    """
    alarm_triggered: bool
    complied: bool
    outcome_success: bool
    trust_delta: float


# -------------------------------------------------
# Synthetic user model
# -------------------------------------------------

class SyntheticUser:
    """
    Base synthetic user behavior model.
    """

    def __init__(
        self,
        name: str,
        compliance_bias: float = 0.6,
        fatigue_sensitivity: float = 0.5,
        avoidance_tendency: float = 0.3,
        seed: int = 42,
    ):
        self.name = name
        self.compliance_bias = compliance_bias
        self.fatigue_sensitivity = fatigue_sensitivity
        self.avoidance_tendency = avoidance_tendency

        self.random = random.Random(seed)

        # Internal memory (NOT governance state)
        self.last_directive: Optional[GovernanceDirective] = None

    # -------------------------------------------------
    # Signal generation (what the brain observes)
    # -------------------------------------------------

    def generate_signals(
        self,
        day: int,
        state: Optional[BehavioralState],
    ) -> SignalBatch:
        """
        Generate a batch of behavioral signals for the current day.
        """

        now = datetime.utcnow()
        signals: List[Signal] = []

        # Default assumptions
        fatigue = state.fatigue_index if state else 0.5

        # Base compliance probability
        compliance_prob = self.compliance_bias

        # Fatigue reduces compliance
        compliance_prob -= fatigue * self.fatigue_sensitivity

        # Enforcement pressure boosts short-term compliance
        if self.last_directive and self.last_directive.strategy == Strategy.ENFORCEMENT:
            compliance_prob += 0.15

        compliance_prob = max(0.0, min(1.0, compliance_prob))

        # Decide success or failure
        success = self.random.random() < compliance_prob

        if success:
            signals.append(
                Signal(
                    name="clean_alarm_dismissal",
                    value=1.0,
                    confidence=1.0,
                    timestamp=now - timedelta(minutes=5),
                )
            )

            if self.random.random() < 0.4:
                signals.append(
                    Signal(
                        name="early_wake_success",
                        value=1.0,
                        confidence=0.8,
                        timestamp=now - timedelta(minutes=10),
                    )
                )
        else:
            signals.append(
                Signal(
                    name="alarm_failure",
                    value=1.0,
                    confidence=1.0,
                    timestamp=now - timedelta(minutes=1),
                )
            )

            if self.random.random() < self.avoidance_tendency:
                signals.append(
                    Signal(
                        name="excessive_snooze",
                        value=1.0,
                        confidence=0.7,
                        timestamp=now - timedelta(minutes=2),
                    )
                )

        # Late-night usage (fatigue driver)
        if self.random.random() < fatigue:
            signals.append(
                Signal(
                    name="late_night_usage",
                    value=1.0,
                    confidence=0.8,
                    timestamp=now - timedelta(hours=6),
                )
            )

        return SignalBatch(
            signals=signals,
            window_start=now - timedelta(hours=8),
            window_end=now,
        )

    # -------------------------------------------------
    # Reaction to governance (ground truth)
    # -------------------------------------------------

    def react(self, directive: GovernanceDirective) -> UserReaction:
        """
        React to the governance directive.

        Returns observable outcomes for simulation metrics.
        """

        self.last_directive = directive

        # Was an alarm / intervention actually triggered?
        alarm_triggered = directive.required_strictness > 0.3

        # Compliance probability
        compliance_prob = self.compliance_bias

        if directive.strategy == Strategy.ENFORCEMENT:
            compliance_prob += 0.10
        elif directive.strategy == Strategy.SUPPORT:
            compliance_prob += 0.05

        compliance_prob = max(0.0, min(1.0, compliance_prob))
        complied = self.random.random() < compliance_prob

        # Ground-truth success
        outcome_success = alarm_triggered and complied

        # Trust dynamics
        if alarm_triggered and not complied:
            trust_delta = -0.05
        elif alarm_triggered and complied:
            trust_delta = 0.02
        else:
            trust_delta = 0.01  # calm day builds trust slowly

        return UserReaction(
            alarm_triggered=alarm_triggered,
            complied=complied,
            outcome_success=outcome_success,
            trust_delta=trust_delta,
        )
