# CLI Design

## Purpose

The command-line interface (CLI) provides a terminal-based interface for interacting with the `newton-visualizer` package.

The CLI is responsible for receiving user input, converting mathematical expressions into callable functions, executing the Newton-Raphson solver, displaying numerical results, and optionally generating visualizations.

The CLI must not implement numerical algorithms directly. All computations must be delegated to the computational core.

## Architecture

The CLI integrates the existing layers of the project:

```text
User Input
    ↓
CLI
    ↓
Parser
    ↓
Solver
    ↓
NewtonResult
    ↓
Plotting
```

The solver remains the single source of truth for all numerical computations.

## Initial Command

The first CLI command will be:

```bash
python -m newton_visualizer.cli solve \
  --function "x**2 - 2" \
  --x0 1.0
```

This command should:

1. Parse the mathematical expression.
2. Generate the derivative automatically.
3. Execute the Newton-Raphson solver.
4. Display the numerical results.

## Optional Plot Generation

The CLI should optionally generate a visualization:

```bash
python -m newton_visualizer.cli solve \
  --function "x**2 - 2" \
  --x0 1.0 \
  --plot outputs/newton_plot.png
```

When the `--plot` argument is provided, the plotting module should be used to save the resulting figure.

## Supported Arguments

The initial version of the CLI should support:

| Argument | Description |
|-----------|-------------|
| `--function` | Mathematical expression written in terms of `x` |
| `--x0` | Initial approximation |
| `--tolerance` | Numerical tolerance |
| `--max-iterations` | Maximum number of iterations |
| `--plot` | Optional output path for generated plot |

## Numerical Output

The CLI should display a concise numerical summary.

Example:

```text
Root:        1.4142135623730951
Converged:   True
Iterations:  5
Residual:    4.440892098500626e-16
```

If a plot is generated:

```text
Root:        1.4142135623730951
Converged:   True
Iterations:  5
Residual:    4.440892098500626e-16
Plot saved:  outputs/newton_plot.png
```

## Error Handling

The CLI should provide clear error messages for:

- Invalid mathematical expressions.
- Unsupported variables.
- Invalid numerical arguments.
- Derivative equal to zero.
- Failure to converge within the iteration limit.
- Invalid output paths.

Example:

```text
Error: expression must depend only on the variable x.
```

## Design Principles

The CLI should:

- Use the parser for expression handling.
- Use the solver for numerical computation.
- Use the plotting module for visualization.
- Avoid duplicating logic from other layers.
- Remain scriptable and automation-friendly.
- Work inside GitHub Codespaces.
- Operate correctly in environments without graphical interfaces.

## Relationship with Future Interfaces

The CLI is the first user-facing interface of the project.

Future interfaces will include:

```text
CLI
Notebook
Web Interface
REST API
```

All of them should use the same parser, solver, and plotting modules.

## Future Extensions

Possible future improvements include:

- Iteration tables.
- Convergence plots.
- Tangent-line visualizations.
- CSV export.
- JSON export.
- Support for multiple numerical methods.
- Comparison between methods.
- Custom plotting ranges.
- Verbose mode.
- Interactive terminal mode.

## References

1. Burden, R. L., & Faires, J. D. *Numerical Analysis*. Cengage Learning.
2. Sauer, T. *Numerical Analysis*. Pearson.
3. SymPy Development Team. *SymPy Documentation*.
4. Matplotlib Development Team. *Matplotlib Documentation*.