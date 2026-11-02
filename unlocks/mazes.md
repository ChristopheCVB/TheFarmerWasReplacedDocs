[Documentation index](../README.md)

# Mazes

A maze with a treasure in the middle.

```python
if get_entity_type() == Entities.Treasure:
    harvest()
```

## Upgrade description

Increases the gold in treasure chests and the amount of weird substance needed to spawn a maze.

[Related guide](../guides/unlocks/mazes.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `fertilizer` |
| Stored maximum level | 6 |
| Stored upgrade cost factor | 6 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 1,000 × Weird Substance |
| Stored upgrade cost 1 | 12,000 × Cactus |
| Unlocks | `hedge`, `treasure`, `gold`, `measure`, `can_move` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1841` (`UnlockSO`).
