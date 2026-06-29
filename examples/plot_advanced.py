from newton_visualizer.plotting import plot_newton_iterations_with_tangents
from newton_visualizer.solver import NewtonResult

f = lambda x: x**2 - 2
df = lambda x: 2 * x

result = NewtonResult(
    root=2**0.5,
    converged=True,
    iterations=4,
    history=[
        1.0,
        1.5,
        1.4166666667,
        1.4142156863,
        1.4142135624,
    ],
    residual=1e-12,
)

plot_newton_iterations_with_tangents(
    f=f,
    df=df,
    result=result,
    x_min=0,
    x_max=2,
    output_path="outputs/advanced_plot.png",
)

print("Plot saved to outputs/advanced_plot.png")