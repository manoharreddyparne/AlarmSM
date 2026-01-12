from policy_evolution.updater import PolicyUpdater
from policy_evolution.versioning import PolicyVersion
from policy_evolution.signals import EvolutionSignal


def test_policy_updater_generates_recommendation():
    current = PolicyVersion(
        parameters={
            "alarm_strictness": 0.6,
            "support_weight": 0.4,
            "enforcement_weight": 0.5,
        },
        reason="Initial baseline policy",
    )

    updater = PolicyUpdater(current)

    signals = {
        EvolutionSignal.ALARM_FATIGUE,
        EvolutionSignal.TRUST_COLLAPSE,
    }

    recommendation = updater.propose_update(signals)

    assert recommendation is not None
    assert "alarm_strictness" in recommendation.suggested_parameters
    assert recommendation.rationale
    assert len(recommendation.triggering_signals) == 2
