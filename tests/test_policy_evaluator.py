"""
tests/test_policy_evaluator.py

Phase 3.1 validation test.

Ensures that policy evaluation can be computed
from Phase 2 simulation logs without errors.
"""

from simulation.run_simulation import run_basic_simulation
from policy_evolution.evaluator import PolicyEvaluator


def test_policy_evaluation_runs():
    # Run Phase 2 simulation (data source)
    logs = run_basic_simulation(days=7)

    # Evaluate governance health (Phase 3.1)
    evaluation = PolicyEvaluator(logs).evaluate()

    # Core assertions
    assert evaluation.window_days == 7
    assert evaluation.governance_health in {
        "healthy",
        "risky",
        "degrading",
    }
