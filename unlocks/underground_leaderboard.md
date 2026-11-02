[Documentation index](../README.md)

# Underground Leaderboard

> Underground/DLC content.

Enter the underground leaderboard for the fastest times.

`leaderboard_run(Leaderboards.Rice, "rice_file", speedup)`

[Related guide](../guides/unlocks/underground_leaderboard.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `dynamite` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 20,000 × Dynamite, 200,000 × Bamboo |
| Additional requirement | Simulation, level 1 or higher |
| Unlocks | `leaderboard_run`, `Leaderboards` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1865` (`UnlockSO`).
