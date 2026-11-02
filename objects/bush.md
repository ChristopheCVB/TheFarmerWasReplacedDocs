[Documentation index](../README.md)

# Bush

A small bush that drops `Items.Wood`.

[Related guide](../guides/unlocks/plant.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `BushPlant` |
| Plantable | Yes |
| Can be planted over | No |
| Swappable | No |
| Can have a companion | Yes |
| Can be infected | Yes |
| Mean base growth time (seconds) | 4 |
| Stored growth deviation fraction | 0.2 |
| Base drop item | `wood` |
| Stored base drop amount | 1 |
| Yield upgrade | `trees` |
| Stored base planting cost | None |
| Can be planted on | Grassland, Soil, Perlite |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1614` (`EntitySO`).
