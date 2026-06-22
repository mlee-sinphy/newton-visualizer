import math

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