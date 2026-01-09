"""
state_model.py

Maintains the internal behavioral state model
used by the Governing Brain.

This module defines:
- The BehavioralState data structure
- The governed interface for state evolution

No policy decisions are made here.
"""

from dataclasses import dataclass
from typing import Optional

from governing_brain.inputs import SignalBatch


@dataclass
class BehavioralState:
    """
    Represents the Governing Brain's internal
    belief about the user's behavioral condition.
    """

    discipline_level: float
    failure_risk: float
    avoidance_tendency: float
    fatigue_index: float
    context_importance: float
    momentum_trend: float


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

    # ----- Start from previous values -----
    failure_risk = previous_state.failure_risk
    fatigue_index = previous_state.fatigue_index
    avoidance_tendency = previous_state.avoidance_tendency
    discipline_level = previous_state.discipline_level
    momentum_trend = previous_state.momentum_trend
    context_importance = previous_state.context_importance

    # =========================================================
    # FAILURE RISK UPDATE
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "alarm_failure",
            "excessive_snooze",
            "late_night_usage",
        }:
            failure_risk += 0.1 * signal.confidence

        if signal.name in {
            "clean_alarm_dismissal",
            "early_wake_success",
        }:
            failure_risk -= 0.1 * signal.confidence

    failure_risk = max(0.0, min(1.0, failure_risk))

    # =========================================================
    # FATIGUE INDEX UPDATE
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "sleep_debt",
            "late_night_usage",
            "repeated_enforcement",
            "short_sleep_duration",
        }:
            fatigue_index += 0.05 * signal.confidence

        if signal.name in {
            "adequate_sleep",
            "recovery_day",
            "low_enforcement_day",
        }:
            fatigue_index -= 0.05 * signal.confidence

    fatigue_index = max(0.0, min(1.0, fatigue_index))

    # =========================================================
    # AVOIDANCE TENDENCY UPDATE
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "volume_evasion",
            "power_off_attempt",
            "fake_dismissal",
            "dismissal_latency_spike",
        }:
            avoidance_tendency += 0.05 * signal.confidence

        if signal.name in {
            "clean_compliance_streak",
            "no_avoidance_detected",
        }:
            avoidance_tendency -= 0.03 * signal.confidence

    avoidance_tendency = max(0.0, min(1.0, avoidance_tendency))

    # =========================================================
    # DISCIPLINE LEVEL UPDATE
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "early_wake_success",
            "clean_alarm_dismissal",
            "consistent_sleep_routine",
        }:
            discipline_level += 0.04 * signal.confidence

        if signal.name in {
            "alarm_failure",
            "excessive_snooze",
            "routine_break",
        }:
            discipline_level -= 0.04 * signal.confidence

    discipline_level = max(0.0, min(1.0, discipline_level))

    # =========================================================
    # MOMENTUM TREND UPDATE (DIRECTION ONLY)
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "early_wake_success",
            "clean_alarm_dismissal",
            "consistent_sleep_routine",
            "adequate_sleep",
        }:
            momentum_trend += 0.03 * signal.confidence

        if signal.name in {
            "alarm_failure",
            "excessive_snooze",
            "late_night_usage",
            "routine_break",
        }:
            momentum_trend -= 0.03 * signal.confidence

    # Gentle decay toward neutral
    momentum_trend *= 0.95

    momentum_trend = max(-1.0, min(1.0, momentum_trend))
    # =========================================================
    # CONTEXT IMPORTANCE UPDATE (SITUATIONAL COST)
    # =========================================================
    for signal in signals.signals:
        if signal.name in {
            "exam_day",
            "important_meeting",
            "deadline_day",
            "travel_day",
        }:
            context_importance += 0.2 * signal.confidence

        if signal.name in {
            "weekend",
            "holiday",
        "recovery_day",
        }:
            context_importance -= 0.2 * signal.confidence

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
