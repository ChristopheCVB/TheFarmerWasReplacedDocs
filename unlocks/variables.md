[Documentation index](../README.md)

# Variables

Assign values to variables.

```python
next_plant = Entities.Bush
plant(next_plant)
```

[Related guide](../guides/scripting/variables.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `operators` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 35 × Carrot |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1868` (`UnlockSO`).
