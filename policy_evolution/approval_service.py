"""
policy_evolution/approval_service.py

Phase 4.3 — Human Approval Service

Persists approval decisions in a simple audit log.
"""

import json
from pathlib import Path
from dataclasses import asdict

from policy_evolution.approval import PolicyApprovalDecision


class ApprovalService:
    """
    Records human approval decisions to disk.
    """

    def __init__(self, log_path: str = "approvals_log.jsonl"):
        self.log_path = Path(log_path)

    def record(self, decision: PolicyApprovalDecision):
        """
        Append a decision to the approval log.
        """
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(decision), default=str) + "\n")
