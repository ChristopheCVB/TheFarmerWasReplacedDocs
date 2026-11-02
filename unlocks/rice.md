[Documentation index](../README.md)

# Rice

> Underground/DLC content.

It's just like wheat, if wheat grew on clay.

```python
if get_ground_type() == Grounds.Clay:
    plant(Entities.Rice)
```

## Upgrade description

Increases the yield and cost of rice plants.

[Related guide](../guides/unlocks/rice.md)

## Packaged gameplay settings

| Property | Stored value |
| --- | --- |
| Parent unlock | `mining` |
| Stored maximum level | 8 |
| Stored upgrade cost factor | 2 |
| Stored additive percent start | 0 |
| Stored additive percent factor | 2 |
| Enabled | Yes |
| Initial unlock cost | 10 × Coal |
| Stored upgrade cost 1 | 100 × Block |
| Stored upgrade cost 2 | 500 × Block |
| Stored upgrade cost 3 | 1,000 × Block |
| Additional requirement | Expand, level 2 or higher |
| Unlocks | `clay`, `dry_rice_terrace`, `rice_terrace` |

> These are stored base settings. Actual costs, growth, yields, hardness, and other behavior can depend on upgrades, depth, neighbors, or controller logic. Stored upgrade lists and factors are exported without inventing a runtime formula.

Source: `resources.assets`, object `1854` (`UnlockSO`).
