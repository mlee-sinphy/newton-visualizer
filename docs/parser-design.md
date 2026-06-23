# Parser Design

## Purpose

The parser is responsible for converting mathematical expressions written as strings into callable Python functions that can be used by the Newton-Raphson solver.

This component exists to support user-facing interfaces such as the CLI and the Jupyter notebook while keeping the numerical solver independent from input parsing.

## Motivation

The computational core expects callable functions:

```python
newton_raphson(
    f,
    df,
    x0,
)