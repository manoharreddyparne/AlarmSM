from policy_evolution.versioning import PolicyVersion
from policy_evolution.recommendation import PolicyRecommendation
from policy_evolution.applier import PolicyVersionApplier


def test_policy_version_applier_creates_new_version():
    current = PolicyVersion(
        parameters={
            "alarm_strictness": 0.6,
            "support_weight": 0.4,
            "enforcement_weight": 0.5,
        },
        reason="Initial baseline policy",
    )

    recommendation = PolicyRecommendation(
        suggested_parameters={
            "alarm_strictness": 0.5,
            "support_weight": 0.5,
            "enforcement_weight": 0.5,
        },
        rationale="Reduce alarm fatigue and rebuild trust",
        triggering_signals=["alarm_fatigue", "trust_collapse"],
    )

    applier = PolicyVersionApplier()
    new_version = applier.apply(current, recommendation)

    assert new_version is not current
    assert new_version.parameters != current.parameters
    assert "Reduce alarm fatigue" in new_version.reason
