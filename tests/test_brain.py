from datetime import datetime, timedelta

from governing_brain.inputs import Signal, SignalBatch
from governing_brain.state_model import update_state
from governing_brain.brain import GoverningBrain
from governing_brain.strategies import Strategy


def print_state(state, title):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)
    print(
        f"Discipline={state.discipline_level:.2f}, "
        f"FailureRisk={state.failure_risk:.2f}, "
        f"Fatigue={state.fatigue_index:.2f}, "
        f"Avoidance={state.avoidance_tendency:.2f}, "
        f"Momentum={state.momentum_trend:.2f}, "
        f"Context={state.context_importance:.2f}"
    )


def run_cycle(previous_state, signals, description, expected_strategies):
    print("\n" + "=" * 70)
    print(description)
    print("=" * 70)

    new_state = update_state(previous_state, signals)
    print_state(new_state, "Updated State")

    brain = GoverningBrain()
    directive, explanation = brain.decide(new_state)

    print("\nDecision:")
    print("Strategy:", directive.strategy)
    print("Strictness:", directive.required_strictness)
    print("Capabilities:", directive.allowed_capabilities)
    print("Recovery Allowed:", directive.recovery_allowed)
    print("Explanation ID:", explanation.decision_id)

    assert directive.strategy in expected_strategies

    return new_state


if __name__ == "__main__":
    now = datetime.utcnow()

    # -------------------------------------------------
    # Cycle 1 — Cold start + fatigue + alarm failure
    # -------------------------------------------------
    signals_1 = SignalBatch(
        signals=[
            Signal("late_night_usage", 1.0, 0.9, now - timedelta(hours=6)),
            Signal("alarm_failure", 1.0, 0.8, now - timedelta(minutes=1)),
        ],
        window_start=now - timedelta(hours=8),
        window_end=now,
    )

    state = None
    state = run_cycle(
        state,
        signals_1,
        "Cycle 1: Cold start with fatigue + alarm failure",
        expected_strategies={Strategy.SUPPORT},
    )

    # -------------------------------------------------
    # Cycle 2 — Avoidance + enforcement stress
    # -------------------------------------------------
    signals_2 = SignalBatch(
        signals=[
            Signal("excessive_snooze", 1.0, 0.7, now + timedelta(hours=12)),
            Signal("repeated_enforcement", 1.0, 0.6, now + timedelta(hours=12)),
            Signal("volume_evasion", 1.0, 0.6, now + timedelta(hours=12)),
        ],
        window_start=now,
        window_end=now + timedelta(days=1),
    )

    state = run_cycle(
        state,
        signals_2,
        "Cycle 2: Snoozing + avoidance + enforcement stress",
        expected_strategies={Strategy.SUPPORT, Strategy.STABILIZATION},
    )

    # -------------------------------------------------
    # Cycle 3 — Recovery + success
    # -------------------------------------------------
    signals_3 = SignalBatch(
        signals=[
            Signal(
                "adequate_sleep",
                1.0,
                0.9,
                now + timedelta(days=1, hours=6),
            ),
            Signal(
                "early_wake_success",
                1.0,
                0.8,
                now + timedelta(days=1, hours=6),
            ),
            Signal(
                "clean_alarm_dismissal",
                1.0,
                0.8,
                now + timedelta(days=1, hours=6),
            ),
        ],
        window_start=now + timedelta(days=1),
        window_end=now + timedelta(days=2),
    )
