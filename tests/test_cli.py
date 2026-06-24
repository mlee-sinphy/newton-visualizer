import subprocess
import sys


def test_cli_solves_square_root_problem():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "newton_visualizer.cli",
            "solve",
            "--function",
            "x**2 - 2",
            "--x0",
            "1.0",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Root:" in result.stdout
    assert "Converged:" in result.stdout


def test_cli_generates_plot(tmp_path):
    output_file = tmp_path / "plot.png"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "newton_visualizer.cli",
            "solve",
            "--function",
            "x**2 - 2",
            "--x0",
            "1.0",
            "--plot",
            str(output_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_file.exists()


def test_cli_rejects_invalid_expression():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "newton_visualizer.cli",
            "solve",
            "--function",
            "y**2 - 2",
            "--x0",
            "1.0",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0


def test_cli_rejects_missing_arguments():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "newton_visualizer.cli",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0