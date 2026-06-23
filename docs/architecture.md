# Software Architecture

## Purpose

The purpose of this document is to describe the software architecture of the `newton-visualizer` project.

The project is designed around a documentation-driven and test-driven workflow. Mathematical documentation defines the theoretical foundation, design documentation specifies the expected behavior, tests verify the implementation, and the source code provides the computational core.

## Project Structure

```text
newton-visualizer/
├── docs/
│   ├── newton-method.md
│   ├── solver-design.md
│   └── architecture.md
├── notebooks/
│   └── newton_method_exploration.ipynb
├── src/
│   └── newton_visualizer/
│       ├── __init__.py
│       ├── solver.py
│       ├── plotting.py
│       └── cli.py
├── tests/
│   └── test_solver.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Architectural Overview

The project is organized into four main layers:

1. Documentation layer
2. Testing layer
3. Computational core
4. User interface layer

The central design principle is that all numerical computations must be implemented once in the computational core and reused by all interfaces.

## Documentation Layer

Location:

```text
docs/
```

This layer contains the theoretical, technical, and architectural documentation of the project.

Its responsibilities are:

- explain the Newton-Raphson method mathematically;
- define the expected behavior of the solver;
- document the software architecture;
- guide future implementation decisions.

The documentation layer defines what the system is supposed to do before the implementation is written.

## Testing Layer

Location:

```text
tests/
```

This layer contains automated tests that verify whether the implementation satisfies the documented requirements.

Its responsibilities are:

- verify numerical correctness;
- validate convergence behavior;
- check error handling;
- prevent regressions;
- provide executable specifications for the solver.

The tests do not implement numerical algorithms. They only check whether the computational core behaves correctly.

## Computational Core

Location:

```text
src/newton_visualizer/
```

This layer contains the reusable numerical implementation.

Currently, the main components are:

```text
solver.py
plotting.py
```

The `solver.py` module contains the Newton-Raphson implementation and the data structure used to represent the result of the computation.

The core function is:

```python
newton_raphson(...)
```

The core result object is:

```python
NewtonResult
```

The solver is responsible for computing numerical approximations, storing iteration history, reporting convergence status, and returning diagnostic information.

The computational core is the single source of truth for all numerical computations in the project.

## User Interface Layer

The project will expose two user interfaces:

1. A command-line interface.
2. A Jupyter notebook interface.

Both interfaces must use the computational core. They must not reimplement the Newton-Raphson algorithm.

### Command-Line Interface

Planned location:

```text
src/newton_visualizer/cli.py
```

The CLI will allow users to execute the solver from the terminal.

Its responsibilities will include:

- receiving user inputs through command-line arguments;
- calling the computational core;
- displaying numerical results;
- optionally saving output files;
- providing a scriptable interface for terminal-based usage.

A future example usage may look like:

```bash
newton solve --function "x**2 - 2" --derivative "2*x" --x0 1.0
```

### Notebook Interface

Location:

```text
notebooks/newton_method_exploration.ipynb
```

The notebook interface will support scientific exploration.

Its responsibilities will include:

- explaining the method interactively;
- running numerical experiments;
- displaying iteration tables;
- generating plots;
- visualizing convergence behavior;
- supporting educational and research-oriented usage.

The notebook should import and use the solver from the package instead of redefining the algorithm.

## Dependency Direction

The intended dependency direction is:

```text
Documentation
    ↓
Tests
    ↓
Computational Core
    ↓
User Interfaces
```

In practical terms:

```text
CLI
Notebook
    ↓
newton_raphson(...)
    ↓
NewtonResult
```

This means that the CLI and the notebook depend on the solver, but the solver does not depend on either interface.

## Design Principles

The project follows these principles:

- documentation-driven development;
- test-driven development;
- separation of concerns;
- single source of truth;
- reusable computational core;
- explicit numerical diagnostics;
- reproducible scientific experimentation;
- extensibility for future numerical methods.

## Current Status

At the current stage, the project includes:

- mathematical documentation of the Newton-Raphson method;
- solver design documentation;
- initial automated tests;
- an initial implementation of the Newton-Raphson solver.

The CLI and notebook interfaces are planned future layers.

## Future Extensions

The architecture should support future extensions such as:

- convergence plots;
- animated visualizations;
- comparison with other root-finding methods;
- bisection method;
- secant method;
- multidimensional Newton methods;
- symbolic differentiation;
- richer CLI commands;
- interactive notebooks;
- exported figures for documentation.