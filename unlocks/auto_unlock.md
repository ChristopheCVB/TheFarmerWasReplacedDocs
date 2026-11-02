[Documentation index](../README.md)

# Auto Unlock

Automatically unlock things.

`unlock(Unlocks.Megafarm)`

[Related guide](../guides/unlocks/auto_unlock.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `costs` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 5,000 × Pumpkin |
| Unlocks | `Unlocks`, `unlock`, `num_unlocked` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1817` (`UnlockSO`).
