"""
policy_evolution/versioning.py

Defines immutable, versioned policy records.

Phase:
- Introduced in Phase 3.1
- Actively used in Phase 3.3+
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict
from uuid import uuid4


@dataclass(frozen=True)
class PolicyVersion:
    """
    Immutable record of a policy configuration.
    """

    # -----------------------------
    # Policy definition (required)
    # -----------------------------
    parameters: Dict[str, float]
    reason: str

    # -----------------------------
    # Version metadata (auto)
    # -----------------------------
    version_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
