[Documentation index](../README.md)

# `spawn_drone`

`spawn_drone(function, *args)`
Spawns a new drone in the same position as the drone that ran the `spawn_drone(function, *args)` command. The new drone then begins executing the specified function. The rest of the arguments are copied and passed into the specified function. After the drone is done, it will disappear automatically.

returns the handle of the new drone or `None` if all drones are already spawned.

takes `200` ticks to execute if a drone was spawned, `1` otherwise.

example:

```python
def harvest_column(message):
    for _ in range(get_world_size()):
        harvest()
        move(North)
    print(message)

i = 0
while True:
    if spawn_drone(harvest_column, i):
        move(East)
        i = (i + 1) % 10
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_spawn_drone`.
