[Documentation index](../README.md)

# Bamboo

> Underground/DLC content.

Plant bamboo and watch it grow.

`plant(Entities.Bamboo)`

## Upgrade description

Increases the yield and cost of bamboo.

[Related guide](../guides/unlocks/bamboo.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `rice` |
| Stored maximum level | 8 |
| Stored upgrade cost factor | 4 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Rice |
| Stored upgrade cost 1 | 400 × Rice |
| Stored upgrade cost 2 | 800 × Rice |
| Stored upgrade cost 3 | 100 × Mushroom |
| Unlocks | `bamboo`, `measure`, `hover`, `get_hover` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1818` (`UnlockSO`).
