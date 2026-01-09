from dataclasses import dataclass
from typing import List
from governing_brain.strategies import Strategy
@dataclass
class GovernanceDirective:
    """
    Represents abstract control directives
    emitted by the Governing Brain.
    """

    strategy: Strategy
    required_strictness: float
    allowed_capabilities: List[str]
    escalation_limit: float
    recovery_allowed: bool
    explanation_required: bool
