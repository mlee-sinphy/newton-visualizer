import matplotlib.pyplot as plt


def plot_function_with_iterations(
    f,
    result,
    x_min: float,
    x_max: float,
    output_path=None,
):
    if not result.history:
        raise ValueError("result history must not be empty.")

    if x_min >= x_max:
        raise ValueError("x_min must be smaller than x_max.")

    xs = [x_min + i * (x_max - x_min) / 400 for i in range(401)]
    ys = [f(x) for x in xs]

    iteration_xs = result.history
    iteration_ys = [f(x) for x in iteration_xs]

    fig, ax = plt.subplots()

    ax.plot(xs, ys, label="f(x)")
    ax.axhline(0, linewidth=1)
    ax.scatter(iteration_xs, iteration_ys, label="Newton iterations")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Newton-Raphson Iterations")
    ax.legend()
    ax.grid(True)

    if output_path is not None:
        fig.savefig(output_path)

    return fig, ax


def plot_residual_convergence(
    f,
    result,
    output_path=None,
):
    if not callable(f):
        raise TypeError("f must be callable.")

    if not result.history:
        raise ValueError("result history must not be empty.")

    iterations = list(range(len(result.history)))
    residuals = [abs(f(x)) for x in result.history]

    fig, ax = plt.subplots()

    ax.plot(iterations, residuals, marker="o", label="Residual")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("|f(x_n)|")
    ax.set_title("Residual Convergence")
    ax.grid(True)
    ax.legend()

    if output_path is not None:
        fig.savefig(output_path)

    return fig, ax