[Documentation index](../README.md)

# Dictionaries

Get access to dictionaries and sets.

`right_of = {North:East, East:South, South:West, West:North}`

[Related guide](../guides/scripting/dicts.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `lists` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 2,500 × Pumpkin |
| Unlocks | `dicts`, `sets`, `add`, `dict`, `set` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1826` (`UnlockSO`).
