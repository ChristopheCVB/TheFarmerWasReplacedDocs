[Documentation index](../README.md)

# `num_drones`

`num_drones()`

returns the number of drones currently in the farm.

takes `1` tick to execute.

example:

```python
while num_drones() < max_drones():
    spawn_drone(task)
    move(East)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_num_drones`.
