import pytest
import matplotlib

matplotlib.use("Agg")

from newton_visualizer.plotting import plot_residual_convergence
from newton_visualizer.solver import NewtonResult


def make_sample_result():
    return NewtonResult(
        root=1.4142135623730951,
        converged=True,
        iterations=4,
        history=[1.0, 1.5, 1.4166666667, 1.4142156863, 1.4142135624],
        residual=1e-12,
    )


def test_plot_residual_convergence_returns_figure_and_axis():
    f = lambda x: x**2 - 2
    result = make_sample_result()

    fig, ax = plot_residual_convergence(
        f=f,
        result=result,
    )

    assert fig is not None
    assert ax is not None


def test_plot_residual_convergence_saves_output_file(tmp_path):
    f = lambda x: x**2 - 2
    result = make_sample_result()
    output_file = tmp_path / "residual_convergence.png"

    fig, ax = plot_residual_convergence(
        f=f,
        result=result,
        output_path=output_file,
    )

    assert fig is not None
    assert ax is not None
    assert output_file.exists()


def test_plot_residual_convergence_rejects_non_callable_function():
    result = make_sample_result()

    with pytest.raises(TypeError):
        plot_residual_convergence(
            f=None,
            result=result,
        )


def test_plot_residual_convergence_rejects_empty_history():
    f = lambda x: x**2 - 2

    result = NewtonResult(
        root=0.0,
        converged=False,
        iterations=0,
        history=[],
        residual=0.0,
    )

    with pytest.raises(ValueError):
        plot_residual_convergence(
            f=f,
            result=result,
        )