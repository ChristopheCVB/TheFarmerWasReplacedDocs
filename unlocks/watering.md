[Documentation index](../README.md)

# Watering

Water the plants to make them grow faster.

`use_item(Items.Water)`

## Upgrade description

Receive more water.

[Related guide](../guides/unlocks/watering.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `carrots` |
| Stored maximum level | 9 |
| Stored upgrade cost factor | 4 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Wood |
| Stored upgrade cost 1 | 200 × Wood |
| Unlocks | `water`, `use_item`, `get_water` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1869` (`UnlockSO`).
