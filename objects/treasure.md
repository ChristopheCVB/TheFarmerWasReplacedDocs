[Documentation index](../README.md)

# Treasure

A treasure that contains gold equal to the area of the maze in which it is hidden. It can be harvested like a plant.

[Related guide](../guides/unlocks/mazes.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `Treasure` |
| Plantable | No |
| Can be planted over | No |
| Swappable | No |
| Can have a companion | No |
| Can be infected | Yes |
| Mean base growth time (seconds) | 0 |
| Stored growth deviation fraction | 0 |
| Base drop item | `gold` |
| Stored base drop amount | 1 |
| Yield upgrade | `mazes` |
| Stored base planting cost | 1 × Weird Substance |
| Can be planted on | Soil, Grassland |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1626` (`EntitySO`).
