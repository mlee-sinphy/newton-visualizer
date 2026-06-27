import matplotlib.pyplot as plt


def plot_function_with_iterations(
    f,
    result,
    x_min: float,
    x_max: float,
    output_path=None,
):
    if not callable(f):
        raise TypeError("f must be callable.")

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
    ax.axhline(0, color="black", linewidth=1)
    ax.scatter(iteration_xs, iteration_ys, color="red", label="Iteration points")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Newton-Raphson Iterations")
    ax.legend()
    ax.grid(True)

    if output_path is not None:
        fig.savefig(output_path)

    return fig, ax


def plot_newton_iterations_with_tangents(
    f,
    df,
    result,
    x_min: float,
    x_max: float,
    output_path=None,
):
    if not callable(f):
        raise TypeError("f must be callable.")

    if not callable(df):
        raise TypeError("df must be callable.")

    if not result.history:
        raise ValueError("result history must not be empty.")

    if x_min >= x_max:
        raise ValueError("x_min must be smaller than x_max.")

    xs = [x_min + i * (x_max - x_min) / 400 for i in range(401)]
    ys = [f(x) for x in xs]

    fig, ax = plt.subplots()

    ax.plot(xs, ys, label="f(x)")
    ax.axhline(0, color="black", linewidth=1)

    # Plot tangent lines
    for x_n in result.history[:-1]:
        y_n = f(x_n)
        slope = df(x_n)

        tangent_ys = [
            y_n + slope * (x - x_n)
            for x in xs
        ]

        ax.plot(
            xs,
            tangent_ys,
            linestyle="--",
            alpha=0.5,
        )

    # Plot iteration points
    iteration_xs = result.history
    iteration_ys = [f(x) for x in iteration_xs]

    ax.scatter(
        iteration_xs,
        iteration_ys,
        color="red",
        label="Iteration points",
    )

    # Highlight root approximation
    ax.scatter(
        [result.root],
        [0],
        marker="x",
        s=100,
        label="Root approximation",
    )

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Newton-Raphson Iterations with Tangents")
    ax.legend()
    ax.grid(True)

    if output_path is not None:
        fig.savefig(output_path)

    return fig, ax