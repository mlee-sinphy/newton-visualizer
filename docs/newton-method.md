# Newton-Raphson Method

## Introduction

The determination of roots of nonlinear equations constitutes a fundamental problem in scientific computing. In numerous applications arising in physics, engineering, optimization, and machine learning, equations of the form

$$
f(x)=0
$$

cannot be solved analytically, or their analytical solutions may be computationally impractical to obtain. Consequently, numerical methods are employed to construct approximations to the desired solutions.

Among these methods, the Newton-Raphson method occupies a prominent position due to its conceptual simplicity, computational efficiency, and rapid local convergence under suitable regularity assumptions.

## Problem Statement

Let

$$
f:\mathbb{R}\rightarrow\mathbb{R}
$$

be a real-valued function, where both the domain and codomain of \(f\) are the set of real numbers.

The objective is to determine a value

$$
r\in\mathbb{R}
$$

such that

$$
f(r)=0.
$$

The value \(r\) is called a **root** or **zero** of the function \(f\). Geometrically, \(r\) corresponds to a point at which the graph of \(f\) intersects the horizontal axis.

In general, an exact expression for \(r\) may not exist or may be difficult to obtain analytically. Numerical methods therefore seek to construct a sequence of approximations

$$
\{x_n\}_{n=0}^{\infty},
\qquad
x_n\in\mathbb{R},
$$

satisfying

$$
\lim_{n\rightarrow\infty} x_n=r.
$$

The Newton-Raphson method provides one such iterative procedure by recursively generating successive approximations that, under appropriate assumptions, converge to the desired root.