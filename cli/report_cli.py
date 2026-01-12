"""
cli/report_cli.py

Phase 4.2 — CLI Report Viewer
Phase 4.3 — Human Approval Workflow

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
from policy_evolution.approval import PolicyApprovalDecision
from policy_evolution.approval_service import ApprovalService


def prompt_for_approval() -> bool:
    """
    Prompt a human reviewer to approve or reject
    the proposed policy update.
    """
    while True:
        choice = input("Approve proposed policy? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def run_report(days: int = 7):
    # -------------------------------------------------
    # 1. Run simulation (Phase 2)
    # -------------------------------------------------
    logs = run_basic_simulation(days=days)

    # -------------------------------------------------
    # 2. Evaluate governance (Phase 3.1)
    # -------------------------------------------------
    evaluation = PolicyEvaluator(logs).evaluate()

    # -------------------------------------------------
    # 3. Derive evolution signals (Phase 3.2)
    # -------------------------------------------------
    signal_engine = EvolutionSignalEngine()
    signals = list(signal_engine.derive(evaluation))

    # -------------------------------------------------
    # 4. Define current policy (baseline)
    # -------------------------------------------------
    current_policy = PolicyVersion(
        parameters={
            "alarm_strictness": 0.6,
            "support_weight": 0.4,
            "enforcement_weight": 0.5,
        },
        reason="Baseline policy",
    )

    # -------------------------------------------------
    # 5. Generate recommendation (Phase 3.3)
    # -------------------------------------------------
    updater = PolicyUpdater(current_policy)
    recommendation = updater.propose_update(set(signals))

    # -------------------------------------------------
    # 6. Apply recommendation (Phase 3.4, offline)
    # -------------------------------------------------
    proposed_version = None
    if recommendation:
        applier = PolicyVersionApplier()
        proposed_version = applier.apply(current_policy, recommendation)

    # -------------------------------------------------
    # 7. Generate human-readable report (Phase 4.1)
    # -------------------------------------------------
    report = PolicyEvolutionReport().generate(
        evaluation=evaluation,
        signals=signals,
        recommendation=recommendation,
        proposed_version=proposed_version,
    )

    print("\n" + report)

    # -------------------------------------------------
    # 8. Human approval workflow (Phase 4.3)
    # -------------------------------------------------
    if recommendation:
        approved = prompt_for_approval()
        comment = input("Optional comment: ").strip() or None

        decision = PolicyApprovalDecision(
            approved=approved,
            reviewer="local-user",
            comment=comment,
        )

        ApprovalService().record(decision)

        print("\nDecision recorded.")
    else:
        print("\nNo recommendation to approve.")


if __name__ == "__main__":
    run_report()
