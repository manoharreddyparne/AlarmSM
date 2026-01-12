from simulation.run_simulation import run_basic_simulation
from policy_evolution.evaluator import PolicyEvaluator
from policy_evolution.signal_engine import EvolutionSignalEngine
from policy_evolution.signals import EvolutionSignal


def test_evolution_signals_generated():
    logs = run_basic_simulation(days=7)
    evaluation = PolicyEvaluator(logs).evaluate()

    engine = EvolutionSignalEngine()
    signals = engine.derive(evaluation)

    assert isinstance(signals, set)
    assert len(signals) >= 1
    assert all(isinstance(s, EvolutionSignal) for s in signals)
