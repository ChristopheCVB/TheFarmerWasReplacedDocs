[Documentation index](../README.md)

# Trees

Unlocks trees.

`plant(Entities.Trees)`

## Upgrade description

Increases the yield of bushes and trees.

[Related guide](../guides/unlocks/trees.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `carrots` |
| Stored maximum level | 10 |
| Stored upgrade cost factor | 4 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Wood, 70 × Carrot |
| Stored upgrade cost 1 | 300 × Hay |
| Unlocks | `tree` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1864` (`UnlockSO`).
