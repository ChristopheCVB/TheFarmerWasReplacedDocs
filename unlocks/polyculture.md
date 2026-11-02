[Documentation index](../README.md)

# Polyculture

Use companion planting to increase the yield.

`plant_type, (x, y) = get_companion()`

## Upgrade description

Increases the yield multiplier of polyculture.

[Related guide](../guides/unlocks/polyculture.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `pumpkins` |
| Stored maximum level | 5 |
| Stored upgrade cost factor | 5 |
| Stored additive percent start | 900 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 3,000 × Pumpkin |
| Stored upgrade cost 1 | 10,000 × Bone |
| Unlocks | `get_companion` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1849` (`UnlockSO`).
