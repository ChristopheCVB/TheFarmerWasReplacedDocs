[Documentation index](../README.md)

# Tree

Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

[Related guide](../guides/unlocks/trees.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `TreePlant` |
| Plantable | Yes |
| Can be planted over | No |
| Swappable | No |
| Can have a companion | Yes |
| Can be infected | Yes |
| Mean base growth time (seconds) | 7 |
| Stored growth deviation fraction | 0.2 |
| Base drop item | `wood` |
| Stored base drop amount | 5 |
| Yield upgrade | `trees` |
| Stored base planting cost | None |
| Can be planted on | Soil, Grassland, Perlite |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1627` (`EntitySO`).
