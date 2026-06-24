import os
import subprocess
import sys


def run_cli(args):
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"

    return subprocess.run(
        [sys.executable, "-m", "newton_visualizer.cli", *args],
        capture_output=True,
        text=True,
        env=env,
    )


def test_cli_solves_square_root_problem():
    result = run_cli(
        [
            "solve",
            "--function",
            "x**2 - 2",
            "--x0",
            "1.0",
        ]
    )

    assert result.returncode == 0
    assert "Root:" in result.stdout
    assert "Converged:" in result.stdout


def test_cli_generates_plot(tmp_path):
    output_file = tmp_path / "plot.png"

    result = run_cli(
        [
            "solve",
            "--function",
            "x**2 - 2",
            "--x0",
            "1.0",
            "--plot",
            str(output_file),
        ]
    )

    assert result.returncode == 0
    assert output_file.exists()


def test_cli_rejects_invalid_expression():
    result = run_cli(
        [
            "solve",
            "--function",
            "y**2 - 2",
            "--x0",
            "1.0",
        ]
    )

    assert result.returncode != 0


def test_cli_rejects_missing_arguments():
    result = run_cli([])

    assert result.returncode != 0