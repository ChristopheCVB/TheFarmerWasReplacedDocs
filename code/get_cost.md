[Documentation index](../README.md)

# `get_cost`

`get_cost(thing)` 
Gets the cost of a `thing`

If `thing` is an entity get the cost of planting it.
If `thing` is an unlock get the cost of unlocking it.

returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
returns `{}` when used on an upgradeable unlock that is already at the max level.

takes `1` tick to execute.

example:

```python
cost = get_cost(Unlocks.Carrots)
for item in cost:
    if num_items(item) < cost[item]:
        print("not enough items to unlock carrots")
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_get_cost`.
