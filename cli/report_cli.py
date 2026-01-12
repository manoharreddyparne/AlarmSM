"""
cli/report_cli.py

Phase 4.2 — CLI Report Viewer

Run:
    python -m cli.report_cli
"""

from simulation.run_simulation import run_basic_simulation
from policy_evolution.evaluator import PolicyEvaluator
from policy_evolution.signal_engine import EvolutionSignalEngine
from policy_evolution.updater import PolicyUpdater
from policy_evolution.applier import PolicyVersionApplier
from policy_evolution.report import PolicyEvolutionReport
from policy_evolution.versioning import PolicyVersion


def run_report(days: int = 7):
    # 1) Run simulation
    logs = run_basic_simulation(days=days)

    # 2) Evaluate governance
    evaluation = PolicyEvaluator(logs).evaluate()

    # 3) Derive evolution signals
    signal_engine = EvolutionSignalEngine()
    signals = list(signal_engine.derive(evaluation))

    # 4) Prepare current policy (baseline)
    current_policy = PolicyVersion(
        parameters={
            "alarm_strictness": 0.6,
            "support_weight": 0.4,
            "enforcement_weight": 0.5,
        },
        reason="Baseline policy",
    )

    # 5) Generate recommendation (dry run)
    updater = PolicyUpdater(current_policy)
    recommendation = updater.propose_update(set(signals))

    # 6) Produce proposed policy version (offline)
    proposed_version = None
    if recommendation:
        applier = PolicyVersionApplier()
        proposed_version = applier.apply(current_policy, recommendation)

    # 7) Generate report
    report = PolicyEvolutionReport().generate(
        evaluation=evaluation,
        signals=signals,
        recommendation=recommendation,
        proposed_version=proposed_version,
    )

    print("\n" + report)


if __name__ == "__main__":
    run_report()
