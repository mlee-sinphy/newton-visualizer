# Advanced Plotting Design

## Purpose

The purpose of this feature is to improve the visual representation of the Newton-Raphson method.

The current plotting module displays the function graph and the iteration points. The advanced plotting feature should make the geometric interpretation of the method clearer by displaying tangent lines and highlighting the approximate root.

## Scope

This feature should add:

- tangent lines for Newton-Raphson iterations;
- highlighted approximation points;
- highlighted final root approximation;
- clearer axis labels;
- improved title and legend;
- optional saving to disk.

## Out of Scope

This feature will not include:

- animations;
- interactive widgets;
- notebook-specific logic;
- web visualizations;
- new numerical algorithms.

## Architecture

The advanced plotting functionality must continue to depend on the computational core.

```text
Parser
    ↓
Solver
    ↓
NewtonResult
    ↓
Advanced Plotting
```

The plotting module must not reimplement the Newton-Raphson method. It should consume the function, its derivative, and the `NewtonResult` object produced by the solver.

## Planned Function

The module should expose a function such as:

```python
plot_newton_iterations_with_tangents(
    f,
    df,
    result,
    x_min,
    x_max,
    output_path=None,
)
```

This function should plot:

- the function graph;
- the horizontal axis;
- the Newton-Raphson iteration points;
- tangent lines at selected iteration points;
- the final root approximation.

## Inputs

- `f`: callable representing the function.
- `df`: callable representing the derivative.
- `result`: instance of `NewtonResult`.
- `x_min`: lower bound of the plotting interval.
- `x_max`: upper bound of the plotting interval.
- `output_path`: optional path where the figure should be saved.

## Output

The function should return:

```python
fig, ax
```

where `fig` is a Matplotlib figure and `ax` is a Matplotlib axis.

## Error Handling

The function should reject:

- empty iteration histories;
- invalid plotting intervals;
- non-callable functions;
- non-callable derivatives.

## Future Extensions

Future features may include:

- animation of tangent construction;
- convergence plots;
- residual plots;
- export to GIF;
- interactive notebook widgets;
- comparison with bisection and secant methods.