"""
policy_evolution/approval.py

Phase 4.3 — Human Approval Model
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Optional


@dataclass(frozen=True)
class PolicyApprovalDecision:
    """
    Immutable record of a human approval decision.
    """

    approved: bool
    reviewer: str
    comment: Optional[str] = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
