from dataclasses import dataclass
from datetime import datetime
from  governing_brain.strategies import Strategy
@dataclass
class ExplanationRecord:
    """
    Structured explanation for a governance decision.
    """

    timestamp: datetime
    trigger: str
    state_summary: str
    strategy_selected: Strategy
    action_summary: str
    expected_outcome: str
    reversal_condition: str
