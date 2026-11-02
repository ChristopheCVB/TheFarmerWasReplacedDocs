[Documentation index](../README.md)

# Underground Senses

> Underground/DLC content.

Drone sensors to interact with underground tiles

```python
while get_pos_z() < 100:
    while get_hardness() > 5:
        while get_hardness(North):
            dig(North)
        move(North)
    dig()
```

[Related guide](../guides/unlocks/underground_senses.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `mining` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Block |
| Unlocks | `get_ground_type`, `Grounds`, `get_pos_z`, `get_hardness`, `get_stability`, `num_unlocked`, `None` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1866` (`UnlockSO`).
