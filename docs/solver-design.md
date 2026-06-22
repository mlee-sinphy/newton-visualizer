# Newton-Raphson Solver Design

## Objectives

The objective of the solver is to approximate real roots of differentiable functions using the Newton-Raphson method. The implementation must provide sufficient information to support numerical analysis, convergence studies, and graphical visualization.

The project exposes two user interfaces:

1. A command-line interface (CLI) for direct execution from the terminal.
2. A Jupyter notebook interface for interactive scientific exploration.

Both interfaces rely on a common computational core implemented in `solver.py`.

## Architecture

The project follows a layered architecture:

```text
CLI
Notebook
    ↓
Newton-Raphson Solver
    ↓
Numerical Results
```

The solver constitutes the single source of truth for all numerical computations. User interfaces must never reimplement the Newton-Raphson algorithm.

## Function Signature

```python
newton_raphson(
    f,
    df,
    x0,
    tolerance=1e-8,
    max_iterations=100
)
```

## Input Parameters

- `f`: callable representing the function $f(x)$.
- `df`: callable representing the derivative $f'(x)$.
- `x0`: initial approximation.
- `tolerance`: numerical tolerance used in the stopping criteria.
- `max_iterations`: maximum number of iterations.

## Return Type

The solver should return an object containing:

- `root`: final approximation;
- `converged`: convergence status;
- `iterations`: number of iterations performed;
- `history`: sequence of approximations;
- `residual`: final value of $|f(x_n)|$.

The stored iteration history will be used by both the CLI and the notebook to generate tables, convergence analyses, and visualizations.

## Stopping Criteria

The solver shall terminate when one of the following conditions is satisfied.

### Residual Criterion

$$
|f(x_n)| < \varepsilon.
$$

### Step Criterion

$$
|x_{n+1} - x_n| < \varepsilon.
$$

### Iteration Limit

$$
n = N_{\max}.
$$

## Error Handling

The solver should detect and report situations including:

- vanishing derivatives;
- non-convergence;
- invalid inputs;
- numerical overflow;
- undefined function evaluations.

## Future Extensions

The architecture should support future extensions, including:

- comparison with other root-finding methods;
- convergence diagnostics;
- animated visualizations;
- multidimensional Newton methods;
- symbolic differentiation interfaces.