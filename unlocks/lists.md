[Documentation index](../README.md)

# Lists

Use lists to store lots of values.

```python
plants = [Entities.Grass, Entities.Bush, Entities.Tree]

for p in plants:
    plant(p)
    move(North)
```

[Related guide](../guides/scripting/lists.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `variables` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 500 × Carrot |
| Unlocks | `append`, `remove`, `pop`, `insert`, `len`, `list` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1839` (`UnlockSO`).
