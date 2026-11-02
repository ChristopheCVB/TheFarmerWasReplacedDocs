[Documentation index](../README.md)

# Timing

It's about time!

`passed_time = get_time()`

[Related guide](../guides/unlocks/timing.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `debug` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 1,000 × Pumpkin |
| Unlocks | `get_time`, `get_tick_count` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1861` (`UnlockSO`).
