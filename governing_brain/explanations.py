"""
explanations.py

Defines structured, auditable explanations
for governance decisions.

Explanations are immutable records intended for:
- Transparency
- Debugging
- Auditing
- Long-term analysis
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict, Any
from uuid import uuid4

from governing_brain.strategies import Strategy


@dataclass(frozen=True)
class ExplanationRecord:
    """
    Structured explanation for a governance decision.
    """

    # =========================================================
    # REQUIRED FIELDS (no defaults — must come first)
    # =========================================================

    trigger: str
    strategy_selected: Strategy

    state_snapshot: Dict[str, Any]
    state_summary: str

    action_summary: str
    expected_outcome: str
    reversal_condition: str

    # =========================================================
    # OPTIONAL / AUTO-GENERATED FIELDS (defaults allowed)
    # =========================================================

    decision_confidence: float = 1.0
    decision_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
