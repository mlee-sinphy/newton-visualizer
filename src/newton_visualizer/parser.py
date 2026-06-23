import sympy as sp


def parse_function(expression: str):
    x = sp.Symbol("x")
    expr = sp.sympify(expression)

    return sp.lambdify(x, expr, "math")


def parse_function_and_derivative(expression: str):
    x = sp.Symbol("x")
    expr = sp.sympify(expression)
    derivative = sp.diff(expr, x)

    f = sp.lambdify(x, expr, "math")
    df = sp.lambdify(x, derivative, "math")

    return f, df