[Documentation index](../README.md)

# Carrots

Till the soil and plant carrots.

```python
till()
plant(Entities.Carrot)
```

## Upgrade description

Increases the yield and cost of carrots.

[Related guide](../guides/unlocks/carrots.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `plant` |
| Stored maximum level | 10 |
| Stored upgrade cost factor | 5 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 50 × Wood |
| Stored upgrade cost 1 | 250 × Wood |
| Unlocks | `carrot`, `till`, `can_trade`, `trade`, `Items`, `carrot_seed` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1820` (`UnlockSO`).
