from tracewise.cli import main


def test_analyze_stub(capsys) -> None:
    exit_code = main([
        "analyze",
        "--input",
        "slow.log",
        "--format",
        "json",
        "--top",
        "5",
        "--min-time",
        "0.5",
    ])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "tracewise analyze (stub)" in captured.out
