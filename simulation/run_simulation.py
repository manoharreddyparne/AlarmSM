"""
simulation/run_simulation.py

Entry point for running AlarmSM behavioral simulations.

Phase 2:
- Executes closed-loop governance simulation
- Prints interpretable daily output

Phase 3+:
- RETURNS simulation logs for analysis and policy evolution
"""

from governing_brain.brain import GoverningBrain
from simulation.time_engine import TimeEngine
from simulation.synthetic_users import SyntheticUser


def run_basic_simulation(days: int = 7):
    """
    Runs a basic simulation with a single synthetic user.

    IMPORTANT:
    - Prints human-readable output (Phase 2)
    - Returns simulation logs for analysis (Phase 3+)
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

        # Outcome tracking — pulled from SimulationLog (NOT directive)
        if getattr(log, "alarm_triggered", False):
            print("Alarm Triggered    : True")
            alarms_triggered += 1
        else:
            print("Alarm Triggered    : False")

        if log.outcome_success is not None:
            print(f"Outcome Success   : {log.outcome_success}")
            successful_outcomes += int(log.outcome_success)

        total_trust += log.trust_delta

    # 6. Simulation-level summary
    print("\n" + "=" * 80)
    print("Simulation Summary")
    print("=" * 80)
    print(f"Total Days Simulated : {len(logs)}")
    print(f"Alarms Triggered     : {alarms_triggered}")
    print(f"Successful Outcomes : {successful_outcomes}")
    print(f"Net Trust Change    : {total_trust:.2f}")
    print("=" * 80)

    # 🔑 Critical for Phase 3+
    return logs


if __name__ == "__main__":
    run_basic_simulation(days=7)
