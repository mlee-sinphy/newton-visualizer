import argparse
import sys
import os
import subprocess

from newton_visualizer.parser import parse_function_and_derivative
from newton_visualizer.plotting import plot_function_with_iterations
from newton_visualizer.solver import newton_raphson


def build_parser():
    parser = argparse.ArgumentParser(
        prog="newton-visualizer",
        description="Newton-Raphson root finding and visualization tool.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    solve_parser = subparsers.add_parser(
        "solve",
        help="Solve a nonlinear equation using the Newton-Raphson method.",
    )

    solve_parser.add_argument("--function", required=True)
    solve_parser.add_argument("--x0", type=float, required=True)
    solve_parser.add_argument("--tolerance", type=float, default=1e-8)
    solve_parser.add_argument("--max-iterations", type=int, default=100)
    solve_parser.add_argument("--plot", default=None)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "solve":
            f, df = parse_function_and_derivative(args.function)

            result = newton_raphson(
                f=f,
                df=df,
                x0=args.x0,
                tolerance=args.tolerance,
                max_iterations=args.max_iterations,
            )

            print(f"Root:        {result.root}")
            print(f"Converged:   {result.converged}")
            print(f"Iterations:  {result.iterations}")
            print(f"Residual:    {result.residual}")

            if args.plot:
                plot_function_with_iterations(
                    f=f,
                    result=result,
                    x_min=min(result.history) - 1,
                    x_max=max(result.history) + 1,
                    output_path=args.plot,
                )
                print(f"Plot saved:  {args.plot}")

            return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())