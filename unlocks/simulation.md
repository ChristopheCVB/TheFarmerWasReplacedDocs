[Documentation index](../README.md)

# Simulation

Test faster and under reproducible conditions.

`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

[Related guide](../guides/unlocks/simulation.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `timing` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 5,000 × Gold |
| Unlocks | `simulate` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1856` (`UnlockSO`).
