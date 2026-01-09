"""
state_model.py

Maintains the internal behavioral state model
used by the Governing Brain.

Design guarantees:
- Deterministic
- Conservative
- Explainable
- Bounded
- Single entry point for mutation

No policy decisions are made here.
"""

from dataclasses import dataclass
from typing import Optional

from governing_brain.inputs import SignalBatch


# =========================================================
# Behavioral State Definition
# =========================================================

@dataclass
class BehavioralState:
    """
    Represents the Governing Brain's internal belief
    about the user's behavioral condition.
    """

    discipline_level: float
    failure_risk: float
    avoidance_tendency: float
    fatigue_index: float
    context_importance: float
    momentum_trend: float


# =========================================================
# Update Coefficients (Behavioral Knobs)
# =========================================================

FAILURE_RISK_INC = 0.10
FAILURE_RISK_DEC = 0.10

FATIGUE_INC = 0.05
FATIGUE_DEC = 0.05

AVOIDANCE_INC = 0.05
AVOIDANCE_DEC = 0.03

DISCIPLINE_INC = 0.04
DISCIPLINE_DEC = 0.04

MOMENTUM_STEP = 0.03
MOMENTUM_DECAY = 0.95

CONTEXT_STRONG_SHIFT = 0.20


# =========================================================
# Signal Categories
# =========================================================

FAILURE_SIGNALS = {
    "alarm_failure",
    "excessive_snooze",
    "late_night_usage",
}

SUCCESS_SIGNALS = {
    "clean_alarm_dismissal",
    "early_wake_success",
}

FATIGUE_SIGNALS = {
    "sleep_debt",
    "late_night_usage",
    "repeated_enforcement",
    "short_sleep_duration",
}

RECOVERY_SIGNALS = {
    "adequate_sleep",
    "recovery_day",
    "low_enforcement_day",
}

AVOIDANCE_SIGNALS = {
    "volume_evasion",
    "power_off_attempt",
    "fake_dismissal",
    "dismissal_latency_spike",
}

COMPLIANCE_SIGNALS = {
    "clean_compliance_streak",
    "no_avoidance_detected",
}

DISCIPLINE_POSITIVE = {
    "early_wake_success",
    "clean_alarm_dismissal",
    "consistent_sleep_routine",
}

DISCIPLINE_NEGATIVE = {
    "alarm_failure",
    "excessive_snooze",
    "routine_break",
}

MOMENTUM_POSITIVE = {
    "early_wake_success",
    "clean_alarm_dismissal",
    "consistent_sleep_routine",
    "adequate_sleep",
}

MOMENTUM_NEGATIVE = {
    "alarm_failure",
    "excessive_snooze",
    "late_night_usage",
    "routine_break",
}

HIGH_STAKES_CONTEXT = {
    "exam_day",
    "important_meeting",
    "deadline_day",
    "travel_day",
}

LOW_STAKES_CONTEXT = {
    "weekend",
    "holiday",
    "recovery_day",
}


# =========================================================
# State Update Function (Single Mutation Path)
# =========================================================

def update_state(
    previous_state: Optional[BehavioralState],
    signals: SignalBatch
) -> BehavioralState:
    """
    Updates the BehavioralState based on a batch of observed signals.

    Rules:
    - Deterministic
    - Conservative
    - Explainable
    - No irreversible jumps

    This function is the ONLY allowed entry
    point for state evolution.
    """

    # ----- Cold start -----
    if previous_state is None:
        return BehavioralState(
            discipline_level=0.5,
            failure_risk=0.5,
            avoidance_tendency=0.3,
            fatigue_index=0.5,
            context_importance=0.5,
            momentum_trend=0.0,
        )

    # ----- Initialize from previous state -----
    failure_risk = previous_state.failure_risk
    fatigue_index = previous_state.fatigue_index
    avoidance_tendency = previous_state.avoidance_tendency
    discipline_level = previous_state.discipline_level
    momentum_trend = previous_state.momentum_trend
    context_importance = previous_state.context_importance

    # =========================================================
    # FAILURE RISK
    # =========================================================
    for signal in signals.signals:
        if signal.name in FAILURE_SIGNALS:
            failure_risk += FAILURE_RISK_INC * signal.confidence
        elif signal.name in SUCCESS_SIGNALS:
            failure_risk -= FAILURE_RISK_DEC * signal.confidence

    failure_risk = max(0.0, min(1.0, failure_risk))

    # =========================================================
    # FATIGUE INDEX
    # =========================================================
    for signal in signals.signals:
        if signal.name in FATIGUE_SIGNALS:
            fatigue_index += FATIGUE_INC * signal.confidence
        elif signal.name in RECOVERY_SIGNALS:
            fatigue_index -= FATIGUE_DEC * signal.confidence

    fatigue_index = max(0.0, min(1.0, fatigue_index))

    # =========================================================
    # AVOIDANCE TENDENCY
    # =========================================================
    for signal in signals.signals:
        if signal.name in AVOIDANCE_SIGNALS:
            avoidance_tendency += AVOIDANCE_INC * signal.confidence
        elif signal.name in COMPLIANCE_SIGNALS:
            avoidance_tendency -= AVOIDANCE_DEC * signal.confidence

    avoidance_tendency = max(0.0, min(1.0, avoidance_tendency))

    # =========================================================
    # DISCIPLINE LEVEL
    # =========================================================
    for signal in signals.signals:
        if signal.name in DISCIPLINE_POSITIVE:
            discipline_level += DISCIPLINE_INC * signal.confidence
        elif signal.name in DISCIPLINE_NEGATIVE:
            discipline_level -= DISCIPLINE_DEC * signal.confidence

    discipline_level = max(0.0, min(1.0, discipline_level))

    # =========================================================
    # MOMENTUM TREND (DIRECTIONAL)
    # =========================================================
    for signal in signals.signals:
        if signal.name in MOMENTUM_POSITIVE:
            momentum_trend += MOMENTUM_STEP * signal.confidence
        elif signal.name in MOMENTUM_NEGATIVE:
            momentum_trend -= MOMENTUM_STEP * signal.confidence

    momentum_trend *= MOMENTUM_DECAY
    momentum_trend = max(-1.0, min(1.0, momentum_trend))

    # =========================================================
    # CONTEXT IMPORTANCE (SITUATIONAL COST)
    # =========================================================
    for signal in signals.signals:
        if signal.name in HIGH_STAKES_CONTEXT:
            context_importance += CONTEXT_STRONG_SHIFT * signal.confidence
        elif signal.name in LOW_STAKES_CONTEXT:
            context_importance -= CONTEXT_STRONG_SHIFT * signal.confidence

    context_importance = max(0.0, min(1.0, context_importance))

    # ----- Return updated state -----
    return BehavioralState(
        discipline_level=discipline_level,
        failure_risk=failure_risk,
        avoidance_tendency=avoidance_tendency,
        fatigue_index=fatigue_index,
        context_importance=context_importance,
        momentum_trend=momentum_trend,
    )
