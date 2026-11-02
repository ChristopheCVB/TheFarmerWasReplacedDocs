[Documentation index](../README.md)

# Pumpkins

Pumpkins!

`plant(Entities.Pumpkin)`

## Upgrade description

Increases the yield and cost of pumpkins.

[Related guide](../guides/unlocks/pumpkins.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `trees` |
| Stored maximum level | 10 |
| Stored upgrade cost factor | 4 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 500 × Wood, 200 × Carrot |
| Stored upgrade cost 1 | 1,000 × Carrot |
| Unlocks | `pumpkin`, `pumpkin_seed`, `dead_pumpkin` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1851` (`UnlockSO`).
