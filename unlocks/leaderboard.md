[Documentation index](../README.md)

# Leaderboard

Enter the leaderboard for the fastest times.

`leaderboard_run(Leaderboards.Hay, "hay_file", speedup)`

[Related guide](../guides/unlocks/leaderboard.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `simulation` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 1,000,000 × Gold, 2,000,000 × Bone |
| Unlocks | `leaderboard_run`, `Leaderboards` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1838` (`UnlockSO`).
