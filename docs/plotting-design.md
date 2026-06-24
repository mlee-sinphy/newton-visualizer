## Architecture

The plotting layer depends on the computational core.

```text
Parser
    ↓
Solver
    ↓
NewtonResult
    ↓
Plotting
```

The plotting module will use the iteration history stored in `NewtonResult`.