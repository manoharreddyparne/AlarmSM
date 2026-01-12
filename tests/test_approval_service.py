from policy_evolution.approval import PolicyApprovalDecision
from policy_evolution.approval_service import ApprovalService
from pathlib import Path


def test_approval_is_recorded(tmp_path: Path):
    log_file = tmp_path / "approvals.jsonl"
    service = ApprovalService(log_path=str(log_file))

    decision = PolicyApprovalDecision(
        approved=True,
        reviewer="tester",
        comment="Looks good",
    )

    service.record(decision)

    content = log_file.read_text()
    assert "tester" in content
    assert "Looks good" in content
