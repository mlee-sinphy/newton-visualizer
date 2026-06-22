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

be a real-valued function, where both the domain and codomain of $begin:math:text$f$end:math:text$ are the set of real numbers.

The objective is to determine a value

$$
r\in\mathbb{R}
$$

such that

$$
f(r)=0.
$$

The value $begin:math:text$r$end:math:text$ is called a **root** or **zero** of the function $begin:math:text$f$end:math:text$. Geometrically, $begin:math:text$r$end:math:text$ corresponds to a point at which the graph of $begin:math:text$f$end:math:text$ intersects the horizontal axis.

In general, an exact expression for $begin:math:text$r$end:math:text$ may not exist or may be difficult to obtain analytically. Numerical methods therefore seek to construct a sequence of approximations

$$
\{x_n\}_{n=0}^{\infty},
\qquad
x_n\in\mathbb{R},
$$

satisfying

$$
\lim_{n\rightarrow\infty}x_n=r.
$$

The Newton-Raphson method provides one such iterative procedure by recursively generating successive approximations that, under appropriate assumptions, converge to the desired root.

## Geometric Motivation

Suppose that an initial approximation

$$
x_0\in\mathbb{R}
$$

is available and that

$$
f(x_0)\neq 0.
$$

Since the exact root is unknown, a direct solution of

$$
f(x)=0
$$

may be difficult or impossible to obtain analytically.

If the function $begin:math:text$f$end:math:text$ is differentiable in a neighborhood of $begin:math:text$x\_0$end:math:text$, then its local behavior can be approximated by its tangent line at that point. The central idea of the Newton-Raphson method is therefore to replace the original nonlinear function by its linear approximation in the vicinity of $begin:math:text$x\_0$end:math:text$.

The intersection of the tangent line with the horizontal axis provides a new approximation to the root. Repeating this construction recursively produces a sequence of approximations that, under suitable assumptions, converges to the desired solution.

## Mathematical Derivation

Let $begin:math:text$x\_n$end:math:text$ be the current approximation to a root of $begin:math:text$f$end:math:text$. If $begin:math:text$f$end:math:text$ is differentiable near $begin:math:text$x\_n$end:math:text$, its first-order Taylor approximation around $begin:math:text$x\_n$end:math:text$ is

$$
f(x)
\approx
f(x_n)
+
f'(x_n)(x-x_n).
$$

The Newton-Raphson method replaces the nonlinear equation

$$
f(x)=0
$$

by the linearized equation

$$
f(x_n)
+
f'(x_n)(x-x_n)
=
0.
$$

Assuming that

$$
f'(x_n)\neq 0,
$$

solving for $begin:math:text$x$end:math:text$ yields

$$
x
=
x_n
-
\frac{f(x_n)}{f'(x_n)}.
$$

The next approximation is therefore defined by

$$
x_{n+1}
=
x_n
-
\frac{f(x_n)}{f'(x_n)}.
$$

This recurrence relation constitutes the Newton-Raphson iteration formula.

Starting from an initial approximation $begin:math:text$x\_0$end:math:text$, the method generates a sequence

$$
x_0,x_1,x_2,\ldots
$$

which, under suitable regularity and initialization conditions, may converge to a root $begin:math:text$r$end:math:text$ of the function.

## Algorithm

Given a differentiable function

$$
f:\mathbb{R}\rightarrow\mathbb{R},
$$

its derivative $begin:math:text$f\'$end:math:text$, an initial approximation $begin:math:text$x\_0$end:math:text$, a tolerance $begin:math:text$\\varepsilon\>0$end:math:text$, and a maximum number of iterations $begin:math:text$N\_\{\\max\}$end:math:text$, the Newton-Raphson method proceeds as follows:

1. Set $begin:math:text$n\=0$end:math:text$.
2. Evaluate $begin:math:text$f\(x\_n\)$end:math:text$ and $begin:math:text$f\'\(x\_n\)$end:math:text$.
3. Compute

   $$
   x_{n+1}
   =
   x_n
   -
   \frac{f(x_n)}{f'(x_n)}.
   $$

4. Verify whether a stopping criterion has been satisfied.
5. Otherwise, increment $begin:math:text$n$end:math:text$ and repeat the procedure.

The output of the algorithm is the final approximation together with the sequence of intermediate approximations generated during the iterative process.

## Stopping Criteria

Since the Newton-Raphson method is iterative, a stopping criterion is required to determine when the approximation is sufficiently accurate.

A common criterion is based on the residual:

$$
|f(x_n)|<\varepsilon,
$$

where $begin:math:text$\\varepsilon\>0$end:math:text$ denotes a prescribed tolerance.

Another criterion is based on the difference between successive approximations:

$$
|x_{n+1}-x_n|<\varepsilon.
$$

This condition indicates that the iterative sequence is no longer changing significantly.

In practice, it is also necessary to impose a maximum number of iterations $begin:math:text$N\_\{\\max\}$end:math:text$, preventing the algorithm from running indefinitely in cases where convergence does not occur.

## Convergence and Limitations

The convergence properties of the Newton-Raphson method depend strongly on the regularity of the function and on the quality of the initial approximation.

Suppose that $begin:math:text$r$end:math:text$ is a root of $begin:math:text$f$end:math:text$ satisfying

$$
f(r)=0
$$

and assume that $begin:math:text$f$end:math:text$ is sufficiently smooth in a neighborhood of $begin:math:text$r$end:math:text$ and that

$$
f'(r)\neq 0.
$$

Under these assumptions, if the initial approximation $begin:math:text$x\_0$end:math:text$ is sufficiently close to $begin:math:text$r$end:math:text$, the sequence generated by the Newton-Raphson iteration converges to the root.

Moreover, the convergence is locally quadratic, meaning that the approximation error decreases very rapidly once the iterates enter a sufficiently small neighborhood of the solution.

Despite its excellent local convergence properties, the method is not globally convergent and may fail under several circumstances. In particular, difficulties may arise when:

- the initial approximation is too far from the desired root;
- the derivative vanishes or becomes numerically small;
- the function possesses singularities or discontinuities;
- the iterative sequence oscillates or diverges.

Consequently, practical implementations of the Newton-Raphson method generally combine convergence criteria, iteration limits, and diagnostic information in order to improve robustness.

## Computational Complexity

Let $begin:math:text$k$end:math:text$ denote the number of iterations required to satisfy a stopping criterion.

At each iteration, the method performs:

1. one evaluation of the function $begin:math:text$f$end:math:text$;
2. one evaluation of its derivative $begin:math:text$f\'$end:math:text$;
3. a constant number of arithmetic operations.

Assuming that the evaluations of $begin:math:text$f$end:math:text$ and $begin:math:text$f\'$end:math:text$ have constant cost, the computational complexity of the algorithm is

$$
T(k)=O(k).
$$

The algorithm itself stores only the current approximation and a small number of auxiliary variables. Therefore, its space complexity is

$$
S(k)=O(1).
$$

In this project, the complete sequence of approximations will also be stored in order to enable visualization and convergence analysis. Under this implementation, the memory complexity becomes

$$
S(k)=O(k).
$$

## References

[1] J. Stoer and R. Bulirsch, *Introduction to Numerical Analysis*. Springer, 2002.

[2] R. L. Burden and J. D. Faires, *Numerical Analysis*. Brooks/Cole, 2011.

[3] W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, *Numerical Recipes: The Art of Scientific Computing*. Cambridge University Press, 2007.

[4] K. E. Atkinson, *An Introduction to Numerical Analysis*. Wiley, 1989.