# Convergence Plot Design

## Purpose

The purpose of this feature is to visualize the convergence behavior of the Newton-Raphson method.

While the existing plotting functions show the geometric construction of the method, the convergence plot focuses on the numerical behavior of the iteration process.

## Scope

This feature should add a residual convergence plot.

For each approximation stored in `result.history`, the plotting function should compute:

```text
|f(x_n)|
```

and plot the residual as a function of the iteration index.

## Planned Function

The plotting module should expose the following function:

```python
plot_residual_convergence(
    f,
    result,
    output_path=None,
)
```

## Inputs

- `f`: callable representing the function.
- `result`: instance of `NewtonResult`.
- `output_path`: optional path where the figure should be saved.

## Output

The function should return:

```python
fig, ax
```

## Error Handling

The function should reject:

- non-callable functions;
- empty iteration histories.

## Out of Scope

This feature will not include:

- relative error plots;
- animated convergence;
- comparison between methods;
- logarithmic scale configuration;
- notebook-specific widgets.

## Future Extensions

Future versions may include:

- logarithmic residual plots;
- absolute error plots when the exact root is known;
- comparison between Newton-Raphson, bisection, and secant methods;
- convergence-rate estimation.