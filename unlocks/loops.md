[Documentation index](../README.md)

# Loops

Unlocks a simple while loop.

```python
while True:
    harvest()
```

[Related guide](../guides/scripting/while.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 5 × Hay |
| Unlocks | `while`, `True`, `False`, `break`, `continue` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1840` (`UnlockSO`).
