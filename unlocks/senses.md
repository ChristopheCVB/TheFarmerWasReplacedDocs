[Documentation index](../README.md)

# Senses

The drone can see what's under it and where it is.

```python
if get_pos_x() < 5 and num_items(Items.Wood) < 200:
    plant(Entities.Bush)
```

[Related guide](../guides/unlocks/senses.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `operators` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 100 × Hay |
| Unlocks | `get_entity_type`, `get_pos_x`, `get_pos_y`, `None`, `num_items`, `Items`, `num_unlocked`, `get_ground_type`, `Grounds` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1855` (`UnlockSO`).
