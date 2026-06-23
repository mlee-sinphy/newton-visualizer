from dataclasses import dataclass


@dataclass
class NewtonResult:
    root: float
    converged: bool
    iterations: int
    history: list[float]
    residual: float


def newton_raphson(
    f,
    df,
    x0: float,
    tolerance: float = 1e-8,
    max_iterations: int = 100,
) -> NewtonResult:
    if not callable(f):
        raise TypeError("f must be callable.")

    if not callable(df):
        raise TypeError("df must be callable.")

    if tolerance <= 0:
        raise ValueError("tolerance must be positive.")

    if max_iterations < 0:
        raise ValueError("max_iterations must be non-negative.")

    history = [x0]
    initial_residual = abs(f(x0))

    if initial_residual < tolerance:
        return NewtonResult(
            root=x0,
            converged=True,
            iterations=0,
            history=history,
            residual=initial_residual,
        )

    x = x0

    for iteration in range(1, max_iterations + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero during Newton-Raphson iteration.")

        x_next = x - fx / dfx
        history.append(x_next)

        residual = abs(f(x_next))

        if residual < tolerance or abs(x_next - x) < tolerance:
            return NewtonResult(
                root=x_next,
                converged=True,
                iterations=iteration,
                history=history,
                residual=residual,
            )

        x = x_next

    return NewtonResult(
        root=x,
        converged=False,
        iterations=max_iterations,
        history=history,
        residual=abs(f(x)),
    )