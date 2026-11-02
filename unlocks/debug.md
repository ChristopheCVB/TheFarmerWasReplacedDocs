[Documentation index](../README.md)

# Debug

Tools to help with debugging programs.

`print("hi")`

[Related guide](../guides/scripting/debug.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `plant` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Hay, 50 × Wood |
| Unlocks | `print`, `quick_print`, `Unlocks`, `str`, `output` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1823` (`UnlockSO`).
