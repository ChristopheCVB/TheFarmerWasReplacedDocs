[Documentation index](../README.md)

# `num_unlocked`

`num_unlocked(thing)`
Used to check if an unlock, entity, ground, item or hat is already unlocked.

returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

takes `1` tick to execute.

example:

```python
plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_num_unlocked`.
