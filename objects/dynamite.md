[Documentation index](../README.md)

# Dynamite

Explodes when dug into. Planting and harvesting always uses and yields 1 dynamite.

[Related guide](../guides/unlocks/dynamite.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `Dynamite` |
| Plantable | Yes |
| Can be planted over | No |
| Swappable | No |
| Can have a companion | No |
| Can be infected | Yes |
| Mean base growth time (seconds) | 0 |
| Stored growth deviation fraction | 0 |
| Base drop item | `dynamite` |
| Stored base drop amount | 1 |
| Stored base planting cost | 1 × Dynamite |
| Can be planted on | All |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1620` (`EntitySO`).
