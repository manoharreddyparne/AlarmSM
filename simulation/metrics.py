from dataclasses import dataclass
from typing import Dict, Optional

from governing_brain.state_model import BehavioralState
from governing_brain.inputs import SignalBatch
from governing_brain.outputs import GovernanceDirective
from governing_brain.explanations import ExplanationRecord
from governing_brain.strategies import Strategy


@dataclass(frozen=True)
class SimulationLog:
    """
    Immutable record of one simulated day.
    """

    day: int
    state: BehavioralState
    signals: SignalBatch
    directive: GovernanceDirective
    explanation: ExplanationRecord

    # --- Outcome tracking (simulation responsibility) ---
    alarm_triggered: bool
    outcome_success: Optional[bool] = None
    trust_delta: float = 0.0

    # -------------------------------------------------
    # Convenience accessors
    # -------------------------------------------------

    @property
    def strategy(self) -> Strategy:
        return self.directive.strategy

    @property
    def fatigue(self) -> float:
        return self.state.fatigue_index

    @property
    def failure_risk(self) -> float:
        return self.state.failure_risk

    @property
    def discipline(self) -> float:
        return self.state.discipline_level

    @property
    def avoidance(self) -> float:
        return self.state.avoidance_tendency

    @property
    def context(self) -> float:
        return self.state.context_importance

    @property
    def momentum(self) -> float:
        return self.state.momentum_trend

    # -------------------------------------------------
    # Serialization helper
    # -------------------------------------------------

    def to_dict(self) -> Dict:
        return {
            "day": self.day,
            "strategy": self.strategy.value,
            "discipline": self.discipline,
            "failure_risk": self.failure_risk,
            "fatigue": self.fatigue,
            "avoidance": self.avoidance,
            "context": self.context,
            "momentum": self.momentum,
            "signal_names": [s.name for s in self.signals.signals],
            "required_strictness": self.directive.required_strictness,
            "recovery_allowed": self.directive.recovery_allowed,
            "alarm_triggered": self.alarm_triggered,
            "outcome_success": self.outcome_success,
            "trust_delta": self.trust_delta,
            "explanation": self.explanation.summary,
        }
