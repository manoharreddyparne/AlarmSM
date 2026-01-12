from cli.report_cli import run_report


def test_report_cli_runs_without_error():
    # Smoke test: should execute without raising
    run_report(days=3)
