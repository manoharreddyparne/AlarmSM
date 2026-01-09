from datetime import datetime, timedelta

from governing_brain.inputs import Signal, SignalBatch
from governing_brain.state_model import update_state


def print_context(state, label):
    print(f"{label} → Context Importance: {state.context_importance:.2f}")
    assert 0.0 <= state.context_importance <= 1.0


if __name__ == "__main__":
    now = datetime.utcnow()

    # -------------------------
    # Day 1 — Normal day
    # -------------------------
    signals_day_1 = SignalBatch(
        signals=[],
        window_start=now - timedelta(days=1),
        window_end=now,
    )

    state = None
    state = update_state(state, signals_day_1)
    print_context(state, "Day 1 (Normal)")
    assert state.context_importance == 0.5

    # -------------------------
    # Day 2 — Exam day
    # -------------------------
    signals_day_2 = SignalBatch(
        signals=[
            Signal(
                name="exam_day",
                value=1.0,
                confidence=1.0,
                timestamp=now + timedelta(hours=12),
            )
        ],
        window_start=now,
        window_end=now + timedelta(days=1),
    )

    state = update_state(state, signals_day_2)
    print_context(state, "Day 2 (Exam Day)")
    assert state.context_importance > 0.5

    # -------------------------
    # Day 3 — Weekend
    # -------------------------
    signals_day_3 = SignalBatch(
        signals=[
            Signal(
                name="weekend",
                value=1.0,
                confidence=1.0,
                timestamp=now + timedelta(days=1, hours=12),
            )
        ],
        window_start=now + timedelta(days=1),
        window_end=now + timedelta(days=2),
    )

    state = update_state(state, signals_day_3)
    print_context(state, "Day 3 (Weekend)")
    assert state.context_importance < 1.0
