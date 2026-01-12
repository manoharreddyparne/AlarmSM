from governing_brain.brain import GoverningBrain
from simulation.time_engine import TimeEngine
from simulation.synthetic_users import SyntheticUser


def run_basic_simulation(days: int = 7):
    """
    Runs a basic simulation with a single synthetic user.
    """

    print("\n" + "=" * 80)
    print(f"Running AlarmSM Behavioral Simulation ({days} days)")
    print("=" * 80)

    # 1. Initialize governing brain
    brain = GoverningBrain()

    # 2. Create a synthetic user profile
    user = SyntheticUser(
        name="Burnout-Prone Student",
        compliance_bias=0.65,
        fatigue_sensitivity=0.6,
        avoidance_tendency=0.35,
        seed=42,
    )

    # 3. Create time engine
    engine = TimeEngine(
        brain=brain,
        user=user,
        total_days=days,
    )

    # 4. Run simulation
    logs = engine.run()

    total_trust = 0.0
    alarms_triggered = 0
    successful_outcomes = 0

    # 5. Print daily summary
    for log in logs:
        print("\n" + "-" * 70)
        print(f"Day {log.day}")
        print("-" * 70)
        print(f"Strategy           : {log.strategy.value}")
        print(f"Discipline Level   : {log.discipline:.2f}")
        print(f"Failure Risk       : {log.failure_risk:.2f}")
        print(f"Fatigue Index      : {log.fatigue:.2f}")
        print(f"Avoidance Tendency : {log.avoidance:.2f}")
        print(f"Momentum Trend     : {log.momentum:.2f}")
        print(f"Signals Observed   : {[s.name for s in log.signals.signals]}")

        # Explainability
        print(f"Decision Rationale : {log.explanation.summary}")

        # Outcome tracking (if available)
        if hasattr(log, "alarm_triggered"):
            print(f"Alarm Triggered    : {log.alarm_triggered}")
            alarms_triggered += int(log.alarm_triggered)

        if log.outcome_success is not None:
            print(f"Outcome Success   : {log.outcome_success}")
            successful_outcomes += int(log.outcome_success)

        total_trust += getattr(log, "trust_delta", 0.0)

    # 6. Simulation-level summary
    print("\n" + "=" * 80)
    print("Simulation Summary")
    print("=" * 80)
    print(f"Total Days Simulated : {len(logs)}")
    print(f"Alarms Triggered     : {alarms_triggered}")
    print(f"Successful Outcomes : {successful_outcomes}")
    print(f"Net Trust Change    : {total_trust:.2f}")
    print("=" * 80)


if __name__ == "__main__":
    run_basic_simulation(days=7)
