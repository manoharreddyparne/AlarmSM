from datetime import datetime

from governing_brain.state_model import BehavioralState
from governing_brain.policies.router import select_strategy
from governing_brain.outputs import GovernanceDirective
from governing_brain.explanations import ExplanationRecord
from governing_brain.strategies import Strategy

class GoverningBrain:
    """
    Central orchestration unit for behavioral governance decisions.
    """

    def decide(self, state: BehavioralState) -> tuple[GovernanceDirective, ExplanationRecord]:
        """
        Executes one governance decision cycle.
        """

        strategy = select_strategy(state)

        directive = self._build_directive(strategy)
        explanation = self._build_explanation(strategy, state)

        return directive, explanation
    def _build_directive(self, strategy: Strategy) -> GovernanceDirective:
        """
        Builds abstract governance directives based on strategy.
        """

        if strategy == Strategy.ENFORCEMENT:
            return GovernanceDirective(
                strategy=strategy,
                required_strictness=0.9,
                allowed_capabilities=["alarm_enforcement"],
                escalation_limit=1.0,
                recovery_allowed=False,
                explanation_required=True,
            )

        if strategy == Strategy.SUPPORT:
            return GovernanceDirective(
                strategy=strategy,
                required_strictness=0.3,
                allowed_capabilities=["coaching"],
                escalation_limit=0.2,
                recovery_allowed=True,
                explanation_required=True,
            )

        # Default for STABILIZATION, COMPENSATION, STRATEGIC_PAUSE (for now)
        return GovernanceDirective(
            strategy=strategy,
            required_strictness=0.5,
            allowed_capabilities=[],
            escalation_limit=0.5,
            recovery_allowed=True,
            explanation_required=False,
        )
    def _build_explanation(
        self, strategy: Strategy, state: BehavioralState
    ) -> ExplanationRecord:
        """
        Builds a structured explanation for the decision.
        """

        return ExplanationRecord(
            timestamp=datetime.utcnow(),
            trigger="Policy evaluation based on current behavioral state",
            state_summary=(
                f"failure_risk={state.failure_risk}, "
                f"fatigue_index={state.fatigue_index}, "
                f"avoidance_tendency={state.avoidance_tendency}, "
                f"context_importance={state.context_importance}"
            ),
            strategy_selected=strategy,
            action_summary=f"Selected {strategy.value} strategy",
            expected_outcome="Improved long-term behavioral stability",
            reversal_condition="State variables return to safe ranges",
        )
