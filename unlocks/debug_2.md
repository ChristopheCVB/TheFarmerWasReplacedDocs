[Documentation index](../README.md)

# Debug_2

Functions to temporarily slow down the execution and make the farm smaller.

```python
set_world_size(3)
set_execution_speed(1)
```

[Related guide](../guides/unlocks/debug2.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `debug` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 500 × Gold |
| Unlocks | `set_execution_speed`, `set_world_size`, `debug2` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1824` (`UnlockSO`).
