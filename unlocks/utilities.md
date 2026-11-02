[Documentation index](../README.md)

# Utilities

Unlocks the `min()`, `max()`, `abs()` and `random()` functions.

`random_index = random() * len(list) // 1`

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `functions` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 1,000 × Pumpkin |
| Unlocks | `min`, `max`, `abs`, `random` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1867` (`UnlockSO`).
