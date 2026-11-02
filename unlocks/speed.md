[Documentation index](../README.md)

# Speed

Increases the speed of both the drone and code execution.

## Upgrade description

Increases the speed of both the drone and code execution.

[Related guide](../guides/unlocks/speed.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `loops` |
| Stored maximum level | 5 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 50 |
| Stored additive percent factor | 1.5 |
| Enabled | Yes |
| Initial unlock cost | 20 × Hay |
| Stored upgrade cost 1 | 20 × Wood |
| Stored upgrade cost 2 | 50 × Wood, 50 × Carrot |
| Stored upgrade cost 3 | 500 × Carrot |
| Unlocks | `can_harvest`, `if`, `else`, `elif` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1858` (`UnlockSO`).
