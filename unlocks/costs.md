[Documentation index](../README.md)

# Costs

Allows access to the cost of things.

```python
cost = get_cost(Entities.Carrot)
for item in cost:
	amount_needed = cost[item]
```

[Related guide](../guides/unlocks/costs.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `dictionaries` |
| Stored maximum level | 1 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 2,500 × Pumpkin |
| Unlocks | `get_cost`, `Unlocks` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1822` (`UnlockSO`).
