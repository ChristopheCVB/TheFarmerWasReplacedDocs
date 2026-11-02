[Documentation index](../README.md)

# Plant

Unlocks planting.

`plant(Entities.Bush)`

[Related guide](../guides/unlocks/plant.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `speed` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Hay |
| Unlocks | `wood`, `bush`, `Entities`, `clear` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1848` (`UnlockSO`).
