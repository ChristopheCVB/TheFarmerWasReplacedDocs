[Documentation index](../README.md)

# `simulate`

`simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`
Starts a simulation for the leaderboard using the specified `filename` as a starting point.

`sim_unlocks`: A sequence containing the starting unlocks.
`sim_items`: A dict mapping items to amounts. The simulation starts with these items.
`sim_globals`: A dict mapping variable names to values. The simulation starts with these variables in the global scope.
`seed`: The random seed of the simulation. Must be a positive integer.
`speedup`: The starting speedup.

returns the time it took to run the simulation.

takes `200` ticks to execute.

example:

```python
filename = "f1"
sim_unlocks = Unlocks
sim_items = {Items.Carrot : 10000, Items.Hay : 50}
sim_globals = {"a" : 13}
seed = 0
speedup = 64

run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_simulate`.
