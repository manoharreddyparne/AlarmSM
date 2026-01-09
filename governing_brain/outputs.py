"""
outputs.py

Defines abstract governance directives emitted
by the Governing Brain.

Directives are immutable, validated, and bounded.
"""

from dataclasses import dataclass, field
from typing import List

from governing_brain.strategies import Strategy


@dataclass(frozen=True)
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

    def __post_init__(self):
        # Validate strictness bounds
        if not 0.0 <= self.required_strictness <= 1.0:
            raise ValueError(
                f"required_strictness must be in [0.0, 1.0], "
                f"got {self.required_strictness}"
            )

        # Validate escalation bounds
        if not 0.0 <= self.escalation_limit <= 1.0:
            raise ValueError(
                f"escalation_limit must be in [0.0, 1.0], "
                f"got {self.escalation_limit}"
            )

        # Normalize and validate capabilities
        normalized_caps = []
        for cap in self.allowed_capabilities:
            if not isinstance(cap, str) or not cap.strip():
                raise ValueError("allowed_capabilities must be non-empty strings")
            normalized_caps.append(cap.strip().lower())

        object.__setattr__(self, "allowed_capabilities", normalized_caps)
