from datetime import datetime, timedelta

from governing_brain.inputs import Signal, SignalBatch
from governing_brain.state_model import update_state


def print_context(state, label):
    print(f"{label} → Context Importance: {state.context_importance:.2f}")


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

    # -------------------------
    # Day 2 — Exam day
    # -------------------------
    signals_day_2 = SignalBatch(
        signals=[
            Signal("exam_day", 1.0, 1.0, now + timedelta(days=1))
        ],
        window_start=now,
        window_end=now + timedelta(days=1),
    )

    state = update_state(state, signals_day_2)
    print_context(state, "Day 2 (Exam Day)")

    # -------------------------
    # Day 3 — Weekend
    # -------------------------
    signals_day_3 = SignalBatch(
        signals=[
            Signal("weekend", 1.0, 1.0, now + timedelta(days=2))
        ],
        window_start=now + timedelta(days=1),
        window_end=now + timedelta(days=2),
    )

    state = update_state(state, signals_day_3)
    print_context(state, "Day 3 (Weekend)")
