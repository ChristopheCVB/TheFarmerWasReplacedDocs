[Documentation index](../README.md)

# `wait_for`

`wait_for(drone)`
Waits until the given `drone` terminates.

returns the return value of the function that the `drone` was running.

takes `1` tick to execute if the awaited `drone` is already done.

example:

```python
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
handle = spawn_drone(zero_arg_wrapper)
print(wait_for(handle))
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_wait_for`.
