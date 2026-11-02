[Documentation index](../README.md)

# Sunflower

Sunflowers collect the power from the sun. Harvesting them will give you `Items.Power`.
If you harvest a sunflower with the maximum number of petals you get bonus power.

[Related guide](../guides/unlocks/sunflowers.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Behavior controller | `Sunflower` |
| Plantable | Yes |
| Can be planted over | No |
| Swappable | No |
| Can have a companion | No |
| Can be infected | Yes |
| Mean base growth time (seconds) | 7 |
| Stored growth deviation fraction | 0.2 |
| Base drop item | `power` |
| Stored base drop amount | 1 |
| Stored base planting cost | 1 × Carrot |
| Can be planted on | Soil, Loam |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1625` (`EntitySO`).
