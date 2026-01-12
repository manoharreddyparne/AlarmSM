"""
signal_generator.py

Translates synthetic behavioral outcomes into
governing_brain Signal objects.

Purpose:
- Centralize signal construction
- Decouple behavior modeling from telemetry semantics
- Keep signals consistent and auditable

This module contains NO governance logic.
"""

from datetime import datetime, timedelta
from typing import List

from governing_brain.inputs import Signal


class SignalGenerator:
    """
    Stateless helper for generating standardized signals.
    """

    @staticmethod
    def alarm_success(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="clean_alarm_dismissal",
                confidence=1.0,
                timestamp=now - timedelta(minutes=5),
            ),
            Signal(
                name="early_wake_success",
                confidence=0.8,
                timestamp=now - timedelta(minutes=10),
            ),
        ]

    @staticmethod
    def alarm_failure(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="alarm_failure",
                confidence=1.0,
                timestamp=now - timedelta(minutes=1),
            )
        ]

    @staticmethod
    def snooze_abuse(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="excessive_snooze",
                confidence=0.7,
                timestamp=now - timedelta(minutes=2),
            )
        ]

    @staticmethod
    def late_night_usage(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="late_night_usage",
                confidence=0.8,
                timestamp=now - timedelta(hours=6),
            )
        ]

    @staticmethod
    def recovery_sleep(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="adequate_sleep",
                confidence=0.9,
                timestamp=now - timedelta(hours=7),
            )
        ]

    @staticmethod
    def avoidance_event(now: datetime) -> List[Signal]:
        return [
            Signal(
                name="volume_evasion",
                confidence=0.6,
                timestamp=now - timedelta(minutes=3),
            )
        ]
