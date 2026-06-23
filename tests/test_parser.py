import math
import pytest

from newton_visualizer.parser import (
    parse_function,
    parse_function_and_derivative,
)


def test_parse_quadratic_function():
    f = parse_function("x**2 - 2")

    assert math.isclose(f(2.0), 2.0)
    assert math.isclose(f(0.0), -2.0)


def test_parse_cubic_function():
    f = parse_function("x**3 - 8")

    assert math.isclose(f(2.0), 0.0)
    assert math.isclose(f(3.0), 19.0)


def test_parse_trigonometric_function():
    f = parse_function("sin(x)")

    assert math.isclose(f(0.0), 0.0)
    assert math.isclose(f(math.pi / 2), 1.0)


def test_parse_exponential_function():
    f = parse_function("exp(x)")

    assert math.isclose(f(0.0), 1.0)


def test_parse_logarithmic_function():
    f = parse_function("log(x)")

    assert math.isclose(f(math.e), 1.0)


def test_generate_derivative():
    f, df = parse_function_and_derivative(
        "x**2 - 2"
    )

    assert math.isclose(f(2.0), 2.0)
    assert math.isclose(df(2.0), 4.0)


def test_generate_trigonometric_derivative():
    f, df = parse_function_and_derivative(
        "sin(x)"
    )

    assert math.isclose(
        df(0.0),
        1.0,
        rel_tol=1e-10,
    )


def test_invalid_expression():
    with pytest.raises(Exception):
        parse_function("x***2")


def test_invalid_variable():
    with pytest.raises(Exception):
        parse_function("y**2 - 2")


def test_empty_expression():
    with pytest.raises(Exception):
        parse_function("")


def test_constant_expression():
    with pytest.raises(Exception):
        parse_function("5")


def test_multiple_variables():
    with pytest.raises(Exception):
        parse_function("x + y")


def test_returned_object_is_callable():
    f = parse_function("x**2 - 2")

    assert callable(f)


def test_returned_derivative_is_callable():
    f, df = parse_function_and_derivative(
        "x**2 - 2"
    )

    assert callable(f)
    assert callable(df)