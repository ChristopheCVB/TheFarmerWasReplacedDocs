[Documentation index](../README.md)

# Operators

Arithmetic, comparison and logic operators.

```python
if not can_harvest() and (1 + 1 == 4 / 2):
    do_a_flip()
```

[Related guide](../guides/scripting/operators.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `plant` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 150 × Hay, 10 × Wood |
| Unlocks | `and`, `or`, `not` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1845` (`UnlockSO`).
