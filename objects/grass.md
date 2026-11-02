[Documentation index](../README.md)

# Grass

Grows automatically on grassland. Harvest it to obtain `Items.Hay`.

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `Growable` |
| Plantable | Yes |
| Can be planted over | Yes |
| Swappable | No |
| Can have a companion | Yes |
| Can be infected | Yes |
| Mean base growth time (seconds) | 0.5 |
| Stored growth deviation fraction | 0 |
| Base drop item | `hay` |
| Stored base drop amount | 1 |
| Yield upgrade | `grass` |
| Stored base planting cost | None |
| Can be planted on | Soil, Grassland |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1621` (`EntitySO`).
