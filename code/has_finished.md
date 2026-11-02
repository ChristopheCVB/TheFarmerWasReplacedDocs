[Documentation index](../README.md)

# `has_finished`

`has_finished(drone)`
Checks if the given `drone` has finished.

returns `True` if the `drone` has finished, `False` otherwise.

takes `1` tick to execute.

example:

```python
drone = spawn_drone(function)
while not has_finished(drone):
    do_something_else()
result = wait_for(drone)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_has_finished`.
