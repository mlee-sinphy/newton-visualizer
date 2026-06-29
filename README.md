# Newton Visualizer

A Python toolkit for studying and visualizing the Newton-Raphson method.

The project provides a complete implementation of the Newton-Raphson algorithm together with visualization tools, a command-line interface (CLI), and an interactive Jupyter notebook for educational and scientific exploration.

---

## Features

- Parse mathematical expressions using SymPy.
- Compute roots with the Newton-Raphson method.
- Store iteration history.
- Visualize the function together with Newton iterations.
- Plot tangent lines during each iteration.
- Plot residual convergence.
- Command-line interface (CLI).
- Interactive Jupyter notebook.
- Unit-tested implementation.

---

## Project Structure

```
newton-visualizer/
│
├── docs/
│   ├── parser-design.md
│   ├── plotting-design.md
│   ├── advanced-plotting-design.md
│   ├── convergence-plot-design.md
│   ├── cli-design.md
│   └── notebook-design.md
│
├── notebooks/
│   └── newton_method_exploration.ipynb
│
├── src/
│   └── newton_visualizer/
│       ├── parser.py
│       ├── solver.py
│       ├── plotting.py
│       └── cli.py
│
├── tests/
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/newton-visualizer.git
cd newton-visualizer
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install the project

```bash
pip install -e .
```

---

## Running the Tests

Run the complete test suite

```bash
pytest -v
```

---

## Using the Library

```python
from newton_visualizer.parser import parse_function_and_derivative
from newton_visualizer.solver import newton_raphson

f, df = parse_function_and_derivative("x**2 - 2")

result = newton_raphson(
    f=f,
    df=df,
    x0=1.0,
)

print(result.root)
```

---

## Plotting

### Function and Iterations

```python
from newton_visualizer.plotting import plot_function_with_iterations

plot_function_with_iterations(
    f,
    result,
    x_min=0,
    x_max=2,
)
```

### Tangent Visualization

```python
from newton_visualizer.plotting import (
    plot_newton_iterations_with_tangents,
)

plot_newton_iterations_with_tangents(
    f,
    df,
    result,
    x_min=0,
    x_max=2,
)
```

### Residual Convergence

```python
from newton_visualizer.plotting import (
    plot_residual_convergence,
)

plot_residual_convergence(
    f,
    result,
)
```

---

## Command-Line Interface

Solve an equation

```bash
python -m newton_visualizer.cli solve \
    --function "x**2 - 2" \
    --x0 1.0
```

Generate a plot

```bash
python -m newton_visualizer.cli solve \
    --function "x**2 - 2" \
    --x0 1.0 \
    --plot output.png
```

---

## Jupyter Notebook

An interactive notebook is provided in

```
notebooks/newton_method_exploration.ipynb
```

The notebook demonstrates

- parsing mathematical expressions;
- solving nonlinear equations;
- inspecting the numerical result;
- plotting Newton iterations;
- tangent visualization;
- residual convergence analysis.

---

## Development Workflow

This project follows a documentation-driven workflow.

Each feature is developed according to the following sequence:

```
Design
    ↓
Tests
    ↓
Implementation
    ↓
Validation
```

All new functionality is introduced through feature branches before being merged into the main branch.

---

## Future Improvements

- Interactive widgets
- Animated Newton iterations
- Comparison with the Secant Method
- Comparison with the Bisection Method
- Performance benchmarks
- Support for multivariable Newton's method
- Automatic convergence analysis

---

## License

This project is licensed under the MIT License.