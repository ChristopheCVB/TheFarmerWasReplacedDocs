[Documentation index](../README.md)

# Import

Import things from other files.

```python
import other_file
other_file.function()
```

[Related guide](../guides/scripting/import.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `functions` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 80 × Carrot |
| Unlocks | `from` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1835` (`UnlockSO`).
