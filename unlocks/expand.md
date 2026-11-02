[Documentation index](../README.md)

# Expand

Expands the farm land and unlocks movement.

## Upgrade description

Expands the farm. This also clears the farm.

[Related guide](../guides/unlocks/expand_1.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `speed` |
| Stored maximum level | 9 |
| Stored upgrade cost factor | 8 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 30 × Hay |
| Stored upgrade cost 1 | 20 × Wood |
| Stored upgrade cost 2 | 30 × Wood, 20 × Carrot |
| Stored upgrade cost 3 | 100 × Wood, 50 × Carrot |
| Stored upgrade cost 4 | 1,000 × Pumpkin |
| Unlocks | `move`, `North`, `South`, `East`, `West`, `expand_1`, `2for`, `2range`, `2get_world_size`, `2expand_2` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1829` (`UnlockSO`).
