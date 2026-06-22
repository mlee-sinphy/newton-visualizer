import math
import pytest

from newton_visualizer.solver import newton_raphson


def test_newton_raphson_converges_to_sqrt_2():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x

    result = newton_raphson(
        f=f,
        df=df,
        x0=1.0,
        tolerance=1e-10,
        max_iterations=100,
    )

    assert result.converged is True
    assert math.isclose(result.root, math.sqrt(2), rel_tol=1e-10)
    assert result.iterations > 0
    assert len(result.history) == result.iterations + 1
    assert abs(result.residual) < 1e-10


def test_newton_raphson_converges_to_cubic_root():
    f = lambda x: x**3 - 8
    df = lambda x: 3 * x**2

    result = newton_raphson(
        f=f,
        df=df,
        x0=3.0,
        tolerance=1e-10,
        max_iterations=100,
    )

    assert result.converged is True
    assert math.isclose(result.root, 2.0, rel_tol=1e-10)
    assert abs(result.residual) < 1e-10


def test_newton_raphson_raises_when_derivative_is_zero():
    f = lambda x: x**3
    df = lambda x: 3 * x**2

    with pytest.raises(ZeroDivisionError):
        newton_raphson(
            f=f,
            df=df,
            x0=0.0,
            tolerance=1e-10,
            max_iterations=100,
        )


def test_newton_raphson_reports_non_convergence_when_iteration_limit_is_reached():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x

    result = newton_raphson(
        f=f,
        df=df,
        x0=1.0,
        tolerance=1e-15,
        max_iterations=1,
    )

    assert result.converged is False
    assert result.iterations == 1
    assert len(result.history) == result.iterations + 1
    assert abs(result.residual) >= 1e-15