[Documentation index](../README.md)

# Functions

Define your own functions.

```python
def do_two_flips():
    do_a_flip()
    do_a_flip()

do_two_flips()
```

[Related guide](../guides/scripting/functions.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `variables` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 40 × Carrot |
| Unlocks | `functions`, `def`, `return`, `global`, `tuples`, `scopes` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1832` (`UnlockSO`).
