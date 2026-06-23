import sympy as sp


def _parse_expression(expression: str):
    x = sp.Symbol("x")

    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("expression must be a non-empty string.")

    try:
        expr = sp.sympify(expression)
    except Exception as exc:
        raise ValueError("invalid mathematical expression.") from exc

    if expr.free_symbols != {x}:
        raise ValueError("expression must depend only on the variable x.")

    return x, expr


def parse_function(expression: str):
    x, expr = _parse_expression(expression)
    return sp.lambdify(x, expr, "math")


def parse_function_and_derivative(expression: str):
    x, expr = _parse_expression(expression)
    derivative = sp.diff(expr, x)

    f = sp.lambdify(x, expr, "math")
    df = sp.lambdify(x, derivative, "math")

    return f, df