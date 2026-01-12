from policy_evolution.report import PolicyEvolutionReport
from policy_evolution.evaluation import PolicyEvaluation
from policy_evolution.signals import EvolutionSignal
from policy_evolution.recommendation import PolicyRecommendation
from policy_evolution.versioning import PolicyVersion


def test_policy_evolution_report_generation():
    evaluation = PolicyEvaluation(
        window_days=7,
        alarm_trigger_rate=0.5,
        success_rate=0.7,
        false_alarm_rate=0.2,
        trust_delta=-0.1,
        fatigue_delta=0.1,
        enforcement_ratio=0.6,
        support_ratio=0.3,
        stabilization_ratio=0.1,
        governance_health="risky",
    )

    signals = [
        EvolutionSignal.TRUST_COLLAPSE,
        EvolutionSignal.ALARM_FATIGUE,
    ]

    recommendation = PolicyRecommendation(
        suggested_parameters={"alarm_strictness": 0.5},
        rationale="Reduce fatigue and rebuild trust",
        triggering_signals=["alarm_fatigue", "trust_collapse"],
    )

    proposed = PolicyVersion(
        parameters={"alarm_strictness": 0.5},
        reason="Evolved due to fatigue and trust degradation",
    )

    report = PolicyEvolutionReport().generate(
        evaluation=evaluation,
        signals=signals,
        recommendation=recommendation,
        proposed_version=proposed,
    )

    assert "Policy Evolution Report" in report
    assert "Governance Evaluation" in report
    assert "Evolution Signals" in report
    assert "Policy Recommendation" in report
