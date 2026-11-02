[Documentation index](../README.md)

# Megafarm

More drones!

`spawn_drone(task)`

## Upgrade description

Increase drone count further.

[Related guide](../guides/unlocks/megafarm.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `mazes` |
| Stored maximum level | 5 |
| Stored upgrade cost factor | 4 |
| Stored additive percent start | 100 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 2,000 × Gold |
| Stored upgrade cost 1 | 8,000 × Gold |
| Unlocks | `get_drone_id`, `num_drones`, `max_drones`, `wait_for`, `spawn_drone`, `has_finished` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1842` (`UnlockSO`).
