import pytest
import matplotlib

matplotlib.use("Agg")

from newton_visualizer.plotting import plot_newton_iterations_with_tangents
from newton_visualizer.solver import NewtonResult


def make_sample_result():
    return NewtonResult(
        root=1.4142135623730951,
        converged=True,
        iterations=4,
        history=[1.0, 1.5, 1.4166666667, 1.4142156863, 1.4142135624],
        residual=1e-12,
    )


def test_plot_newton_iterations_with_tangents_returns_figure_and_axis():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    result = make_sample_result()

    fig, ax = plot_newton_iterations_with_tangents(
        f=f,
        df=df,
        result=result,
        x_min=0.0,
        x_max=2.0,
    )

    assert fig is not None
    assert ax is not None


def test_plot_newton_iterations_with_tangents_saves_output_file(tmp_path):
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    result = make_sample_result()
    output_file = tmp_path / "advanced_plot.png"

    fig, ax = plot_newton_iterations_with_tangents(
        f=f,
        df=df,
        result=result,
        x_min=0.0,
        x_max=2.0,
        output_path=output_file,
    )

    assert fig is not None
    assert ax is not None
    assert output_file.exists()


def test_plot_newton_iterations_with_tangents_rejects_empty_history():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x

    result = NewtonResult(
        root=0.0,
        converged=False,
        iterations=0,
        history=[],
        residual=0.0,
    )

    with pytest.raises(ValueError):
        plot_newton_iterations_with_tangents(
            f=f,
            df=df,
            result=result,
            x_min=0.0,
            x_max=2.0,
        )


def test_plot_newton_iterations_with_tangents_rejects_invalid_interval():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    result = make_sample_result()

    with pytest.raises(ValueError):
        plot_newton_iterations_with_tangents(
            f=f,
            df=df,
            result=result,
            x_min=2.0,
            x_max=0.0,
        )